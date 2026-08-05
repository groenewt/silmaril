from config.constants.morphism.codebase.volume.table.aggregate.state.domain.key.value import VALUE as DOMAIN_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.keyed.library import KEYED


def STATE(state: dict) -> dict:
    return {DOMAIN_KEY: [pair[1] for pair in KEYED(state)]}
