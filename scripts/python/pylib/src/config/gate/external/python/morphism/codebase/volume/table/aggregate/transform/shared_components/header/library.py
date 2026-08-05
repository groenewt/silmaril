from config.constants.morphism.codebase.volume.table.aggregate.shared_components.header.value import VALUE as HEADER
from config.constants.morphism.codebase.volume.table.aggregate.state.table.key.value import VALUE as TABLE_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.domain.library import DOMAIN


def STATE(state: dict) -> dict:
    return {TABLE_KEY: [list(HEADER)] + DOMAIN(state)}
