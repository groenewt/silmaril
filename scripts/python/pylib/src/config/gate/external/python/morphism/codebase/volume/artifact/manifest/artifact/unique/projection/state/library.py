from config.constants.morphism.codebase.volume.artifact.manifest.state.artifact.key.value import VALUE as ARTIFACT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.unique.library import UNIQUE


def STATE(state: dict) -> dict:
    return {**state, ARTIFACT_KEY: UNIQUE(MANIFEST_ARTIFACTS(state))}
