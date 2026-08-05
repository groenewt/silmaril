from config.constants.morphism.codebase.volume.table.aggregate.state.sourced.key.value import VALUE as SOURCED_KEY


def SOURCED(state: dict) -> list:
    return state[SOURCED_KEY]
