from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES

VIOLATION = "observation_prefixes_empty"


def STATE(state: dict) -> dict:
    if not PREFIXES(state):
        raise ValueError(VIOLATION)
    return state
