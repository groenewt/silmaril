from config.constants.morphism.codebase.volume.artifact.manifest.state.unsafe.paths.key.value import VALUE as UNSAFE_PATHS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.path.unsafe.library import UNSAFE


def STATE(state: dict) -> dict:
    return {**state, UNSAFE_PATHS_KEY: [path for path in MANIFEST_ARTIFACTS(state) if UNSAFE(path)]}
