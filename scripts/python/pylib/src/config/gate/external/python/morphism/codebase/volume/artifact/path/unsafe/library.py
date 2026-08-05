from config.gate.external.python.morphism.codebase.volume.artifact.path.absolute.library import ABSOLUTE
from config.gate.external.python.morphism.codebase.volume.artifact.path.escape.library import ESCAPE


def UNSAFE(path: str) -> bool:
    return ABSOLUTE(path) or ESCAPE(path)
