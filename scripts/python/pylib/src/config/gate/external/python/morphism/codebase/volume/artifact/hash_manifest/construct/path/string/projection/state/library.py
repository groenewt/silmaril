from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.paths.key.value import VALUE as PATHS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.pathnames.library import PATHNAMES


def STATE(state: dict) -> dict:
    return {**state, PATHS_KEY: [str(pathname) for pathname in PATHNAMES(state)]}
