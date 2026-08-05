from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.artifact.library import EXPECTED_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "artifact_set_mismatch=undeclared_expected="
SURPLUS = ";unexpected_declared="
JOINER = ","


def STATE(state: dict) -> dict:
    declared = set(MANIFEST_ARTIFACTS(state))
    expected = set(EXPECTED_ARTIFACTS(state))
    if declared != expected and STRICT():
        raise ValueError(VIOLATION + JOINER.join(sorted(expected - declared)) + SURPLUS + JOINER.join(sorted(declared - expected)))
    return state
