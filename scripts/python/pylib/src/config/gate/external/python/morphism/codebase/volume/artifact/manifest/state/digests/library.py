from config.constants.morphism.codebase.volume.artifact.manifest.state.digests.key.value import VALUE as ARTIFACT_DIGESTS_KEY


def ARTIFACT_DIGESTS(state: dict) -> dict:
    return state[ARTIFACT_DIGESTS_KEY]
