from config.constants.morphism.codebase.volume.artifact.manifest.contract.column.inventory.identity.value import VALUE as INVENTORY_IDENTITY_COLUMN
from config.constants.morphism.codebase.volume.artifact.manifest.state.inventory.identity.index.key.value import VALUE as INVENTORY_IDENTITY_INDEX_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.lexical.position.library import POSITION
from config.gate.external.python.morphism.codebase.volume.tabular.header.library import HEADER


def STATE(state: dict) -> dict:
    header = HEADER(CONTRACT_ROWS(state))
    return {**state, INVENTORY_IDENTITY_INDEX_KEY: POSITION(header, INVENTORY_IDENTITY_COLUMN)}
