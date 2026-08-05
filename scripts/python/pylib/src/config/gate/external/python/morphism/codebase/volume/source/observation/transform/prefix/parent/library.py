from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES

VIOLATION = "observation_prefix_parent="
PARENT_SEGMENT = ".."


def STATE(state: dict) -> dict:
    traversals = [prefix for prefix in PREFIXES(state) if PARENT_SEGMENT in SPLIT(prefix)]
    if traversals:
        raise ValueError(VIOLATION + traversals[0])
    return state
