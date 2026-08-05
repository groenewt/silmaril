from config.constants.morphism.codebase.volume.request.schema.value import VALUE as REQUEST_SCHEMA


def test_volume_40_request_schema_is_closed_and_configurable() -> None:
    assert REQUEST_SCHEMA["$id"] == "urn:silmaril:morphism:codebase:volume:request:1"
    assert REQUEST_SCHEMA["additionalProperties"] is False
    assert REQUEST_SCHEMA["required"] == ("schema_identity", "mode", "bindings")
    assert REQUEST_SCHEMA["properties"]["mode"]["enum"] == ("generate", "check")

    bindings = REQUEST_SCHEMA["properties"]["bindings"]
    assert bindings["additionalProperties"] is False
    assert bindings["required"] == (
        "repository",
        "source_roots",
        "output_root",
        "final_working_root",
    )
    assert set(bindings["properties"]) == {
        "repository",
        "source_roots",
        "output_root",
        "final_working_root",
    }
