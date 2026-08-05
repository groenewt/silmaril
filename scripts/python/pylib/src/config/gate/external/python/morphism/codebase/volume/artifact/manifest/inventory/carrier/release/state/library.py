from config.constants.morphism.codebase.volume.artifact.manifest.state.csv.documents.key.value import VALUE as CSV_DOCUMENTS_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.released.library import RELEASED
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventories.library import INVENTORIES


def STATE(state: dict) -> dict:
    carrier = {key: value for key, value in state.items() if key != CSV_DOCUMENTS_KEY}
    return {**carrier, INVENTORIES_KEY: [RELEASED(inventory) for inventory in INVENTORIES(state)]}
