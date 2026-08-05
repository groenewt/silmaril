from config.constants.morphism.codebase.volume.source.observation.state.keyed.key.value import VALUE as KEYED_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.first.library import FIRST
from config.gate.external.python.morphism.codebase.volume.source.observation.state.keyed.library import KEYED


def STATE(state: dict) -> dict:
    return {**state, KEYED_KEY: sorted(KEYED(state), key=FIRST)}
