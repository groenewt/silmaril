from config.constants.morphism.codebase.volume.artifact.manifest.state.missing.paths.key.value import VALUE as MISSING_PATHS_KEY


def MISSING_ARTIFACT_PATHS(state: dict) -> list:
    return state[MISSING_PATHS_KEY]
