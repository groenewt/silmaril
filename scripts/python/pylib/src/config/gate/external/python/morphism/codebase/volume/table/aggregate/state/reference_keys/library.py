from config.constants.morphism.codebase.volume.table.aggregate.state.reference_keys.key.value import VALUE as REFERENCE_KEYS_KEY


def REFERENCE_KEYS(state: dict) -> list:
    return state[REFERENCE_KEYS_KEY]
