from config.constants.morphism.codebase.volume.table.aggregate.ring_families.arity.value import VALUE as ARITY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.sourced.library import SOURCED

VIOLATION = "aggregate_row_arity="


def STATE(state: dict) -> dict:
    wrong = [pair for pair in SOURCED(state) if len(pair[1]) != ARITY]
    if wrong:
        raise ValueError(VIOLATION + str(len(wrong[0][1])))
    return state
