from config.constants.morphism.codebase.volume.table.aggregate.state.observed_keys.key.value import VALUE as OBSERVED_KEYS_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.observed_keys.library import OBSERVED_KEYS


def STATE(state: dict) -> dict:
    return {**state, OBSERVED_KEYS_KEY: sorted(set(OBSERVED_KEYS(state)))}
