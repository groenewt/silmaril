from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.table.key.value import VALUE as EXPECTED_TABLE_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.expected.table.library import TABLES
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.unique.library import INVENTORY_UNIQUE
from config.gate.external.python.morphism.codebase.volume.lexical.unique.library import UNIQUE


def STATE(state: dict) -> dict:
    return {**state, EXPECTED_TABLE_KEY: UNIQUE(TABLES(INVENTORY_UNIQUE(state)))}
