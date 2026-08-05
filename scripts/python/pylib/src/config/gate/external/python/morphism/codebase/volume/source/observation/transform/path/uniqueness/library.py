from config.gate.external.python.morphism.codebase.volume.source.observation.state.paths.library import PATHS

VIOLATION = "observation_path_duplicate_count="


def STATE(state: dict) -> dict:
    paths = PATHS(state)
    if len(set(paths)) != len(paths):
        raise ValueError(VIOLATION + str(len(paths) - len(set(paths))))
    return state
