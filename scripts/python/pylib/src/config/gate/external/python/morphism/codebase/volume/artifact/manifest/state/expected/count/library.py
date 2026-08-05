from config.constants.morphism.codebase.volume.artifact.manifest.state.expected.count.key.value import VALUE as EXPECTED_COUNT_KEY


def EXPECTED_ARTIFACT_COUNT(state: dict) -> int:
    return state[EXPECTED_COUNT_KEY]
