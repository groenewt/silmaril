from config.constants.morphism.codebase.volume.table.aggregate.shared_components.identity.column.value import VALUE as IDENTITY_COLUMN
from config.constants.morphism.codebase.volume.table.aggregate.state.observed_keys.key.value import VALUE as OBSERVED_KEYS_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.sourced.library import SOURCED


def STATE(state: dict) -> dict:
    return {**state, OBSERVED_KEYS_KEY: [pair[1][IDENTITY_COLUMN] for pair in SOURCED(state)]}
