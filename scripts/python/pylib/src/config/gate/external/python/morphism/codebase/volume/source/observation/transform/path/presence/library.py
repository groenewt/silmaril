from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS

VIOLATION = "observation_path_empty"
EMPTY = ""


def STATE(state: dict) -> dict:
    if any(path == EMPTY for path in PATHS(state)):
        raise ValueError(VIOLATION)
    return state
