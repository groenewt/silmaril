from config.constants.morphism.codebase.volume.table.aggregate.state.keyed.key.value import VALUE as KEYED_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.keyed.library import KEYED


def STATE(state: dict) -> dict:
    return {**state, KEYED_KEY: sorted(KEYED(state), key=lambda pair: [str(field) for field in pair[0]])}
