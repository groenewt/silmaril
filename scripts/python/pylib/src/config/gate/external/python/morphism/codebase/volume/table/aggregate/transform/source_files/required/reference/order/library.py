from config.constants.morphism.codebase.volume.table.aggregate.state.reference_keys.key.value import VALUE as REFERENCE_KEYS_KEY
REQUIRED = ()


def STATE(state: dict) -> dict:
    return {**state, REFERENCE_KEYS_KEY: sorted(REQUIRED)}
