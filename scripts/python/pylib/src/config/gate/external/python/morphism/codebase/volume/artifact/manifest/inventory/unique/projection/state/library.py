from config.constants.morphism.codebase.volume.artifact.manifest.state.inventory.unique.key.value import VALUE as INVENTORY_UNIQUE_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.identity.library import INVENTORY_IDENTITIES
from config.gate.external.python.morphism.codebase.volume.lexical.unique.library import UNIQUE


def STATE(state: dict) -> dict:
    return {**state, INVENTORY_UNIQUE_KEY: UNIQUE(INVENTORY_IDENTITIES(state))}
