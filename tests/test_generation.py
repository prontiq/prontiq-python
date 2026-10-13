import importlib.util
from pathlib import Path

module_spec = importlib.util.spec_from_file_location(
    "generate", Path(__file__).parents[1] / "scripts/generate.py"
)
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)
normalize = module.normalize_annotations


def test_annotation_only_intersection_preserves_reference():
    reference = {"$ref": "#/components/schemas/AustralianStateCodeQuery"}
    assert normalize({"schema": {"allOf": [reference, {"example": "NSW"}]}}) == {
        "schema": reference
    }


def test_validation_intersections_are_preserved():
    schema = {"allOf": [{"type": "string"}, {"minLength": 3}]}
    assert normalize(schema) == schema


def test_sibling_constraints_and_nullable_unions_are_preserved():
    schema = {"allOf": [{"type": "string"}], "maxLength": 3}
    nullable = {"anyOf": [{"type": "string"}, {"type": "null"}]}
    assert normalize(schema) == schema
    assert normalize(nullable) == nullable
