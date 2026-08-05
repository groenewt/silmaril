from config.constants.morphism.codebase.volume.artifact.manifest.expected.body.artifact.value import VALUE as BODY_ARTIFACT
from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.body.key.value import VALUE as EXPECTED_BODY_KEY


def STATE(state: dict) -> dict:
    return {**state, EXPECTED_BODY_KEY: [BODY_ARTIFACT]}
