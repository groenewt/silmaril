from config.constants.morphism.codebase.volume.artifact.manifest.inventory.identifier.key.value import VALUE as IDENTIFIER_KEY


def IDENTIFIER(inventory: dict) -> str:
    return inventory[IDENTIFIER_KEY]
