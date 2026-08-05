from config.constants.morphism.codebase.volume.table.aggregate.state.sourced.key.value import VALUE as SOURCED_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.sourced.library import SOURCED


def STATE(state: dict) -> dict:
    return {SOURCED_KEY: SOURCED(state)}
