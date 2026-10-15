"""Generate the client from the committed public OpenAPI contract."""

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


def replace_generated(path: Path, old: str, new: str) -> None:
    source = path.read_text(encoding="utf-8")
    if source.count(old) != 1:
        raise SystemExit(f"Review generated {path.name}: expected one {old!r}")
    path.write_text(source.replace(old, new), encoding="utf-8")


def normalize_annotations(value: object) -> object:
    if isinstance(value, list):
        return [normalize_annotations(item) for item in value]
    if not isinstance(value, dict):
        return value
    value = {key: normalize_annotations(item) for key, item in value.items()}
    # Zod emits scalar references intersected with example-only annotations.
    # Drop only annotation-only branches; preserve every validation constraint.
    if set(value) == {"allOf"}:
        constraints = [
            item
            for item in value["allOf"]
            if set(item) - {"title", "description", "example", "examples"}
        ]
        if len(constraints) == 1:
            return constraints[0]
    return value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    with TemporaryDirectory() as temp:
        document = Path(temp) / "openapi.json"
        document.write_text(
            json.dumps(
                normalize_annotations(
                    json.loads((ROOT / "spec/openapi.json").read_text())
                )
            )
        )
        output = Path(temp) / "client"
        subprocess.run(
            [
                "openapi-python-client",
                "generate",
                "--path",
                str(document),
                "--config",
                str(ROOT / "generator.yaml"),
                "--meta",
                "none",
                "--output-path",
                str(output),
                "--fail-on-warning",
            ],
            check=True,
            cwd=ROOT,
            env={**os.environ, "RUFF_CACHE_DIR": str(Path(temp) / "ruff-cache")},
        )
        # --meta none omits the marker needed by installed-package type checkers.
        (output / "py.typed").touch()
        # attrs' default repr exposes tokens and mutable transport credentials.
        for name in ("Client", "AuthenticatedClient"):
            replace_generated(
                output / "client.py",
                f"@define\nclass {name}:",
                f"@define(repr=False)\nclass {name}:",
            )
        # HTTP permits codes absent from Python's enum; preserve the raw status.
        replace_generated(output / "types.py", "from http import HTTPStatus\n", "")
        replace_generated(output / "types.py", "status_code: HTTPStatus", "status_code: int")
        for endpoint in (output / "api").rglob("*.py"):
            if endpoint.name == "__init__.py":
                continue
            replace_generated(endpoint, "from http import HTTPStatus\n", "")
            replace_generated(
                endpoint,
                "status_code=HTTPStatus(response.status_code)",
                "status_code=response.status_code",
            )
        target = ROOT / "src/prontiq"
        if args.check:

            def files(directory: Path) -> dict[str, bytes]:
                return {
                    str(path.relative_to(directory)): path.read_bytes()
                    for path in directory.rglob("*")
                    if path.is_file() and "__pycache__" not in path.parts
                }

            expected, actual = files(output), files(target)
            changed = sorted(
                path
                for path in expected.keys() | actual.keys()
                if expected.get(path) != actual.get(path)
            )
            if changed:
                raise SystemExit(
                    "Changed generated files: "
                    + ", ".join(changed)
                    + "\n"
                    + "Generated client differs: run uv run python scripts/generate.py"
                )
        else:
            shutil.rmtree(target, ignore_errors=True)
            shutil.copytree(output, target)


if __name__ == "__main__":
    main()
