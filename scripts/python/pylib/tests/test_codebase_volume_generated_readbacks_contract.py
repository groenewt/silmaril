from config.constants.morphism.codebase.volume.artifact.generated.readback.name.value import VALUE as READBACKS


def test_generated_readback_contract() -> None:
    assert READBACKS == ("manifest.json", "source_to_fragment.csv", "sha256sums.txt")
