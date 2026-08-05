from config.gate.external.python.morphism.codebase.volume.projection.fragment.line.library import LINES
from config.gate.external.python.morphism.codebase.volume.projection.filetree.record.library import RECORD


def MANIFEST(payload: bytes) -> tuple:
    return tuple(RECORD(line) for line in LINES(payload))
