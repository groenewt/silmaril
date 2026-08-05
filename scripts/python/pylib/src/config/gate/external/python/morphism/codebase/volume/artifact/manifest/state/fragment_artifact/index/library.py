from config.constants.morphism.codebase.volume.artifact.manifest.state.fragment_artifact.index.key.value import VALUE as FRAGMENT_ARTIFACT_INDEX_KEY


def FRAGMENT_ARTIFACT_INDEX(state: dict) -> int:
    return state[FRAGMENT_ARTIFACT_INDEX_KEY]
