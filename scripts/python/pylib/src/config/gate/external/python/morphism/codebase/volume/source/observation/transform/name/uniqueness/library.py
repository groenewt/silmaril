from config.gate.external.python.morphism.codebase.volume.source.observation.state.names.library import NAMES

VIOLATION = "observation_name_duplicate_count="


def STATE(state: dict) -> dict:
    names = NAMES(state)
    if len(set(names)) != len(names):
        raise ValueError(VIOLATION + str(len(names) - len(set(names))))
    return state
