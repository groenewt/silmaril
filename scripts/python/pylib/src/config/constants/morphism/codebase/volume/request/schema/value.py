VALUE = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "urn:silmaril:morphism:codebase:volume:request:1",
    "type": "object",
    "additionalProperties": False,
    "required": ("schema_identity", "mode", "bindings"),
    "properties": {
        "schema_identity": {
            "const": "urn:silmaril:morphism:codebase:volume:request:1",
        },
        "mode": {
            "enum": ("generate", "check"),
        },
        "bindings": {
            "type": "object",
            "additionalProperties": False,
            "required": (
                "repository",
                "source_roots",
                "output_root",
                "final_working_root",
            ),
            "properties": {
                "repository": {"type": "string", "minLength": 1},
                "source_roots": {
                    "type": "array",
                    "minItems": 1,
                    "items": {"type": "string", "minLength": 1},
                },
                "output_root": {"type": "string", "minLength": 1},
                "final_working_root": {"type": "string", "minLength": 1},
            },
        },
    },
}
