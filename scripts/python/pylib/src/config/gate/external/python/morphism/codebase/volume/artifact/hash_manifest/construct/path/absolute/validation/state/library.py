from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.pathnames.library import PATHNAMES
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.stdlib.os.path.isabs.library import DEPENDENCY as ISABS

VIOLATION = "hash_manifest_path_absolute="


def STATE(state: dict) -> dict:
    absolutes = [pathname for pathname in PATHNAMES(state) if ISABS(pathname)]
    if absolutes and STRICT():
        raise ValueError(VIOLATION + absolutes[0])
    return state
