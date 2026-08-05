from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.artifact.key.value import VALUE as EXPECTED_ARTIFACT_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.expected.artifact.library import EXPECTED_ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.lexical.relative.library import RELATIVE


def STATE(state: dict) -> dict:
    artifacts = EXPECTED_ARTIFACTS(state)
    return {**state, EXPECTED_ARTIFACT_KEY: [RELATIVE(artifact) for artifact in artifacts]}
