from config.constants.morphism.codebase.volume.artifact.manifest.inventory.rows.key.value import VALUE as ROWS_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.csv.path.library import CSV_PATH
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.document.library import INVENTORY_DOCUMENT
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.rows.library import ROW_COUNT
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventories.library import INVENTORIES


def STATE(state: dict) -> dict:
    return {**state, INVENTORIES_KEY: [{**inventory, ROWS_KEY: ROW_COUNT(INVENTORY_DOCUMENT(inventory), CSV_PATH(inventory))} for inventory in INVENTORIES(state)]}
