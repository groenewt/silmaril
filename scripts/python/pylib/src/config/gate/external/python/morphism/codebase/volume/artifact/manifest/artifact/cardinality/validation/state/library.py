from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.count.library import EXPECTED_ARTIFACT_COUNT
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.observed.count.library import OBSERVED_ARTIFACT_COUNT
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "artifact_cardinality_mismatch="
DELIMITER = "!="


def STATE(state: dict) -> dict:
    expected = EXPECTED_ARTIFACT_COUNT(state)
    observed = OBSERVED_ARTIFACT_COUNT(state)
    if expected != observed and STRICT():
        raise ValueError(VIOLATION + str(expected) + DELIMITER + str(observed))
    return state
