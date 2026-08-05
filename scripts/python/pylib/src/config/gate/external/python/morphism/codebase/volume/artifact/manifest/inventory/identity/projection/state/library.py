from config.constants.morphism.codebase.volume.artifact.manifest.state.inventory.identity.key.value import VALUE as INVENTORY_IDENTITY_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.identity.index.library import INVENTORY_IDENTITY_INDEX
from config.gate.external.python.morphism.codebase.volume.tabular.body.library import BODY
from config.gate.external.python.morphism.codebase.volume.tabular.column.library import COLUMN


def STATE(state: dict) -> dict:
    rows = BODY(CONTRACT_ROWS(state))
    return {**state, INVENTORY_IDENTITY_KEY: COLUMN(rows, INVENTORY_IDENTITY_INDEX(state))}
