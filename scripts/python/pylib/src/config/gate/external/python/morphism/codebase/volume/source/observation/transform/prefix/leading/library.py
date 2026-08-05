from config.constants.morphism.codebase.volume.source.observation.state.prefixes.key.value import VALUE as PREFIXES_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.relative.library import RELATIVE
from config.gate.external.python.morphism.codebase.volume.source.observation.state.prefixes.library import PREFIXES


def STATE(state: dict) -> dict:
    return {**state, PREFIXES_KEY: [RELATIVE(prefix) for prefix in PREFIXES(state)]}
