from config.constants.morphism.codebase.volume.artifact.manifest.inventory.document.key.value import VALUE as DOCUMENT_KEY


def RELEASED(inventory: dict) -> dict:
    return {key: value for key, value in inventory.items() if key != DOCUMENT_KEY}
