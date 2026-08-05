from config.constants.morphism.codebase.volume.artifact.manifest.state.unsafe.paths.key.value import VALUE as UNSAFE_PATHS_KEY


def UNSAFE_ARTIFACT_PATHS(state: dict) -> list:
    return state[UNSAFE_PATHS_KEY]
