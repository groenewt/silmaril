from config.gate.external.python.morphism.codebase.volume.source.observation.state.names.library import NAMES

VIOLATION = "observation_name_element_empty"
EMPTY = ""


def STATE(state: dict) -> dict:
    if any(name == EMPTY for name in NAMES(state)):
        raise ValueError(VIOLATION)
    return state
