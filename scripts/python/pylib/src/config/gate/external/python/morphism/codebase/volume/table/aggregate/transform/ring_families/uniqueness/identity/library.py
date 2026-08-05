from config.constants.morphism.codebase.volume.table.aggregate.state.identities.key.value import VALUE as IDENTITIES_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.sourced.library import SOURCED


def STATE(state: dict) -> dict:
    return {**state, IDENTITIES_KEY: [pair[1] for pair in SOURCED(state)]}
