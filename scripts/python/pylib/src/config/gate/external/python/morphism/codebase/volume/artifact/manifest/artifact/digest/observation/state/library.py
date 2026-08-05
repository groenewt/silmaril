from config.constants.morphism.codebase.volume.artifact.manifest.state.digests.key.value import VALUE as ARTIFACT_DIGESTS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.digest.library import DIGEST
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.artifact.library import MANIFEST_ARTIFACTS


def STATE(state: dict) -> dict:
    return {**state, ARTIFACT_DIGESTS_KEY: {path: DIGEST(path) for path in MANIFEST_ARTIFACTS(state)}}
