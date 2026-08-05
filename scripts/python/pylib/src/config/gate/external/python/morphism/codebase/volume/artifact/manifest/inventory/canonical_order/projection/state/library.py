from config.constants.morphism.codebase.volume.artifact.manifest.state.inventories.key.value import VALUE as INVENTORIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.identifier.library import IDENTIFIER
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventories.library import INVENTORIES


def STATE(state: dict) -> dict:
    return {**state, INVENTORIES_KEY: sorted(INVENTORIES(state), key=IDENTIFIER)}
