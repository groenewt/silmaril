from config.constants.morphism.codebase.volume.artifact.manifest.state.empty.paths.key.value import VALUE as EMPTY_PATHS_KEY
from config.constants.morphism.codebase.volume.artifact.size.empty.value import VALUE as EMPTY_SIZE
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.size.library import SIZE


def STATE(state: dict) -> dict:
    return {**state, EMPTY_PATHS_KEY: [path for path in MANIFEST_ARTIFACTS(state) if SIZE(path) == EMPTY_SIZE]}
