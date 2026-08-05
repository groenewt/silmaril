from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.sources.library import SOURCES
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.stdlib.os.path.isfile.library import DEPENDENCY as ISFILE

VIOLATION = "hash_manifest_line_file_missing="


def STATE(state: dict) -> dict:
    vanished = [source for source in SOURCES(state) if not ISFILE(source)]
    if vanished and STRICT():
        raise ValueError(VIOLATION + vanished[0])
    return state
