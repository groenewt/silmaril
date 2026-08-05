from config.constants.morphism.codebase.volume.artifact.path.parent.value import VALUE as PARENT
from config.gate.external.python.morphism.codebase.volume.artifact.path.segments.library import SEGMENTS


def ESCAPE(path: str) -> bool:
    return PARENT in SEGMENTS(path)
