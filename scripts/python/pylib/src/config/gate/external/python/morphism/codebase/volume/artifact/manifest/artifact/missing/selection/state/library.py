from config.constants.morphism.codebase.volume.artifact.manifest.state.missing.paths.key.value import VALUE as MISSING_PATHS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.stdlib.os.path.lexists.library import DEPENDENCY as LEXISTS


def STATE(state: dict) -> dict:
    return {**state, MISSING_PATHS_KEY: [path for path in MANIFEST_ARTIFACTS(state) if not LEXISTS(path)]}
