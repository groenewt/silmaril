from config.constants.morphism.codebase.volume.table.aggregate.state.table.key.value import VALUE as TABLE_KEY


def TABLE(state: dict) -> list:
    return state[TABLE_KEY]
