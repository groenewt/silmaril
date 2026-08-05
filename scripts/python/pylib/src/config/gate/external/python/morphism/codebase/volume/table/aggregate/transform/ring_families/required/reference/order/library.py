from config.constants.morphism.codebase.volume.table.aggregate.state.reference_keys.key.value import VALUE as REFERENCE_KEYS_KEY
from config.constants.morphism.codebase.volume.table.ring_families.required.name.value import VALUE as REQUIRED


def STATE(state: dict) -> dict:
    return {**state, REFERENCE_KEYS_KEY: sorted(REQUIRED)}
