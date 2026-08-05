from config.constants.morphism.codebase.volume.projection.filetree.manifest.separator.value import VALUE as SEPARATOR
from silmaril.sparky.morphism.codebase.volume.projection.filetree.record.value import Value as Record


def FIELDS(line: str) -> tuple:
    return tuple(line.split(SEPARATOR))


def RECORD(line: str) -> Record:
    return Record(*FIELDS(line))
