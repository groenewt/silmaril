from config.constants.morphism.codebase.volume.artifact.manifest.state.observed.count.key.value import VALUE as OBSERVED_COUNT_KEY


def OBSERVED_ARTIFACT_COUNT(state: dict) -> int:
    return state[OBSERVED_COUNT_KEY]
