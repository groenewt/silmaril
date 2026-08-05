from config.constants.morphism.codebase.volume.table.aggregate.state.groups.key.value import VALUE as GROUPS_KEY
from config.gate.external.python.morphism.codebase.volume.table.aggregate.state.groups.library import GROUPS


def STATE(state: dict) -> dict:
    return {**state, GROUPS_KEY: [[[name, row] for row in rows] for name, rows in GROUPS(state)]}
