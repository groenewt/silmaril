from config.constants.morphism.codebase.volume.artifact.manifest.inventory.csv.path.key.value import VALUE as CSV_PATH_KEY


def CSV_PATH(inventory: dict) -> str:
    return inventory[CSV_PATH_KEY]
