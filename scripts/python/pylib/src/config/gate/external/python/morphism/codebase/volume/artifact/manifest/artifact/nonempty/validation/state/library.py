from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.empty.paths.library import EMPTY_ARTIFACT_PATHS
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "artifact_empty="
JOINER = ","


def STATE(state: dict) -> dict:
    empty = EMPTY_ARTIFACT_PATHS(state)
    if empty and STRICT():
        raise ValueError(VIOLATION + JOINER.join(empty))
    return state
