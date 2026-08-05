from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.fragments.library import FRAGMENTS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.locator.library import LOCATOR
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv.documents.library import CSV_DOCUMENTS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.identity.library import INVENTORY_IDENTITIES


def STATE(state: dict) -> dict:
    documents = CSV_DOCUMENTS(state)
    fragments = FRAGMENTS(state)
    return {**state, INVENTORIES_KEY: [LOCATOR(identity, documents, fragments) for identity in INVENTORY_IDENTITIES(state)]}
