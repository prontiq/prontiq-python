"""Verify the built wheel without generator dependencies or editable imports."""

import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    wheels = list((ROOT / "dist").glob("*.whl"))
    if len(wheels) != 1:
        raise SystemExit("Build exactly one wheel in dist/ before checking the package")
    with TemporaryDirectory() as directory:
        env = Path(directory) / "venv"
        python = env / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        constraints = Path(directory) / "constraints.txt"
        commands = [
            [
                "uv",
                "export",
                "--frozen",
                "--no-emit-project",
                "--no-hashes",
                "--quiet",
                "--output-file",
                str(constraints),
            ],
            ["uv", "venv", "--python", sys.executable, str(env)],
            [
                "uv",
                "pip",
                "install",
                "--python",
                str(python),
                "--constraint",
                str(constraints),
                str(wheels[0]),
                "pytest",
                "pytest-asyncio",
                "mypy",
            ],
            [str(python), "-I", "-m", "pytest", "tests/test_contract.py"],
            [
                str(python),
                "-I",
                "-m",
                "mypy",
                "--no-incremental",
                "tests/typing/consumer.py",
            ],
        ]
        for command in commands:
            subprocess.run(command, cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
