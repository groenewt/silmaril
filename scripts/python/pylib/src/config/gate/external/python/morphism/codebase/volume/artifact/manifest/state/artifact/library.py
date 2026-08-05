from config.constants.morphism.codebase.volume.artifact.manifest.state.artifact.key.value import VALUE as ARTIFACT_KEY


def MANIFEST_ARTIFACTS(state: dict) -> list:
    return state[ARTIFACT_KEY]
