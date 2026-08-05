from config.constants.morphism.codebase.volume.artifact.manifest.state.inventory.identity.key.value import VALUE as INVENTORY_IDENTITY_KEY


def INVENTORY_IDENTITIES(state: dict) -> list:
    return state[INVENTORY_IDENTITY_KEY]
