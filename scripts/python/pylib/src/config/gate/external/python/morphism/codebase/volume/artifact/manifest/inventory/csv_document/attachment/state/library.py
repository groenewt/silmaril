from config.constants.morphism.codebase.volume.artifact.manifest.inventory.document.key.value import VALUE as DOCUMENT_KEY
from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.csv.path.library import CSV_PATH
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv.documents.library import CSV_DOCUMENTS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventories.library import INVENTORIES


def STATE(state: dict) -> dict:
    documents = CSV_DOCUMENTS(state)
    return {**state, INVENTORIES_KEY: [{**inventory, DOCUMENT_KEY: documents[CSV_PATH(inventory)]} for inventory in INVENTORIES(state)]}
