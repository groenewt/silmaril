from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.missing.paths.library import MISSING_ARTIFACT_PATHS
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "artifact_missing="
JOINER = ","


def STATE(state: dict) -> dict:
    missing = MISSING_ARTIFACT_PATHS(state)
    if missing and STRICT():
        raise ValueError(VIOLATION + JOINER.join(missing))
    return state
