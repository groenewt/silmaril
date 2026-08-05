from config.constants.morphism.codebase.volume.artifact.manifest.state.bytes.key.value import VALUE as ARTIFACT_BYTES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.size.library import SIZE


def STATE(state: dict) -> dict:
    return {**state, ARTIFACT_BYTES_KEY: {path: SIZE(path) for path in MANIFEST_ARTIFACTS(state)}}
