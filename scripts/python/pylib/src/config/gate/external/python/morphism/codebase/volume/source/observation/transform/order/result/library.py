from config.constants.morphism.codebase.volume.source.observation.state.indices.key.value import VALUE as INDICES_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.last.library import LAST
from config.gate.external.python.morphism.codebase.volume.source.observation.state.keyed.library import KEYED


def STATE(state: dict) -> dict:
    return {**state, INDICES_KEY: [LAST(pair) for pair in KEYED(state)]}
