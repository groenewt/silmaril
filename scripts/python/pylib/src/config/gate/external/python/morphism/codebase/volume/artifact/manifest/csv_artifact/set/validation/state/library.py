from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.expected.library import CSV_ARTIFACT_EXPECTED
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.observed.library import CSV_ARTIFACT_OBSERVED
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.morphism.codebase.volume.lexical.absent.library import ABSENT
from config.gate.external.python.morphism.codebase.volume.lexical.joined.library import JOINED

UNEXPECTED = ";manifest_csv_artifact_unexpected="
VIOLATION = "manifest_csv_artifact_missing="


def STATE(state: dict) -> dict:
    expected = CSV_ARTIFACT_EXPECTED(state)
    observed = CSV_ARTIFACT_OBSERVED(state)
    missing = ABSENT(expected, observed)
    unexpected = ABSENT(observed, expected)
    if (missing or unexpected) and STRICT():
        raise ValueError(VIOLATION + JOINED(missing) + UNEXPECTED + JOINED(unexpected))
    return state
