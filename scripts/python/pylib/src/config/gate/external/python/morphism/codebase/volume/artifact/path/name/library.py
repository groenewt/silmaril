from config.constants.morphism.codebase.volume.artifact.path.last.index.value import VALUE as LAST
from config.gate.external.python.morphism.codebase.volume.artifact.path.segments.library import SEGMENTS


def NAME(path: str) -> str:
    return SEGMENTS(path)[LAST]
