from config.gate.external.python.morphism.codebase.volume.source.observation.state.keys.library import KEYS

VIOLATION = "observation_duplicate_key_count="


def STATE(state: dict) -> dict:
    keys = KEYS(state)
    if len(set(keys)) != len(keys):
        raise ValueError(VIOLATION + str(len(keys) - len(set(keys))))
    return state
