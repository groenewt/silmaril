from config.constants.morphism.codebase.volume.table.aggregate.state.keyed.key.value import VALUE as KEYED_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.domain.library import DOMAIN


def STATE(state: dict) -> dict:
    return {**state, KEYED_KEY: [[row, row] for row in DOMAIN(state)]}
