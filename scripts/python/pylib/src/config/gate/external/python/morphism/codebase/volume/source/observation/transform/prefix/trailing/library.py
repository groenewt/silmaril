from config.constants.morphism.codebase.volume.source.observation.state.prefixes.key.value import VALUE as PREFIXES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES

SEPARATOR = "/"


def STATE(state: dict) -> dict:
    return {**state, PREFIXES_KEY: [prefix.removesuffix(SEPARATOR) for prefix in PREFIXES(state)]}
