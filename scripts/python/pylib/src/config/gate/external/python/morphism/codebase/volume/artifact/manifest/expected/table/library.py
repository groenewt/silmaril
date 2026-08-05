from config.constants.morphism.codebase.volume.artifact.manifest.expected.table.prefix.value import VALUE as TABLE_PREFIX
from config.constants.morphism.codebase.volume.artifact.manifest.expected.table.suffix.value import VALUE as TABLE_SUFFIX


def TABLES(identities: list) -> list:
    return [TABLE_PREFIX + identity + TABLE_SUFFIX for identity in identities]
