from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.unsafe.paths.library import UNSAFE_ARTIFACT_PATHS
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "artifact_path_unsafe="
JOINER = ","


def STATE(state: dict) -> dict:
    unsafe = UNSAFE_ARTIFACT_PATHS(state)
    if unsafe and STRICT():
        raise ValueError(VIOLATION + JOINER.join(unsafe))
    return state
