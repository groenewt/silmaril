from config.constants.morphism.codebase.volume.artifact.manifest.inventory.unique.count.value import VALUE as UNIQUE_OCCURRENCE


def DUPLICATES(values: list) -> list:
    return [value for value in dict.fromkeys(values) if values.count(value) != UNIQUE_OCCURRENCE]
