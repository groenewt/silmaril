from config.constants.morphism.codebase.volume.artifact.manifest.contract.column.inventory.identity.value import VALUE as INVENTORY_IDENTITY_COLUMN
from config.constants.morphism.codebase.volume.lexical.position.absent.value import VALUE as ABSENT_POSITION
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.identity.index.library import INVENTORY_IDENTITY_INDEX
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "manifest_contract_column_absent="


def STATE(state: dict) -> dict:
    if INVENTORY_IDENTITY_INDEX(state) == ABSENT_POSITION and STRICT():
        raise ValueError(VIOLATION + INVENTORY_IDENTITY_COLUMN)
    return state
