from config.gate.external.python.stdlib.pathlib.path.library import DEPENDENCY as Path


def CONTENT(locus: Path) -> bytes:
    return locus.read_bytes()
