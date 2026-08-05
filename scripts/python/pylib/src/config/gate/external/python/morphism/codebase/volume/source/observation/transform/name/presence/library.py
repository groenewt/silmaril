from config.gate.external.python.morphism.codebase.volume.source.observation.state.names.library import NAMES

VIOLATION = "observation_names_empty"


def STATE(state: dict) -> dict:
    if not NAMES(state):
        raise ValueError(VIOLATION)
    return state
