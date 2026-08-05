from config.constants.morphism.codebase.volume.artifact.manifest.state.artifact.key.value import VALUE as ARTIFACT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.path.segments.library import SEGMENTS


def STATE(state: dict) -> dict:
    return {**state, ARTIFACT_KEY: [SEGMENTS(path) for path in MANIFEST_ARTIFACTS(state)]}
