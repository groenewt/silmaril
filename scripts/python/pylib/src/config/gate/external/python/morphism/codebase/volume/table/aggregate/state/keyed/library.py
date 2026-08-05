from config.constants.morphism.codebase.volume.table.aggregate.state.keyed.key.value import VALUE as KEYED_KEY


def KEYED(state: dict) -> list:
    return state[KEYED_KEY]
