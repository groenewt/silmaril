from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES

VIOLATION = "observation_prefix_duplicate_count="


def STATE(state: dict) -> dict:
    prefixes = PREFIXES(state)
    if len(set(prefixes)) != len(prefixes):
        raise ValueError(VIOLATION + str(len(prefixes) - len(set(prefixes))))
    return state
