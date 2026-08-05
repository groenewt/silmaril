from config.constants.morphism.codebase.volume.table.aggregate.state.observed_keys.key.value import VALUE as OBSERVED_KEYS_KEY


def OBSERVED_KEYS(state: dict) -> list:
    return state[OBSERVED_KEYS_KEY]
