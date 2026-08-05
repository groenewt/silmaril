from config.constants.morphism.codebase.volume.artifact.manifest.state.observed.csv.artifacts.key.value import VALUE as OBSERVED_CSV_ARTIFACTS_KEY


def OBSERVED_CSV_ARTIFACTS(state: dict) -> list:
    return state[OBSERVED_CSV_ARTIFACTS_KEY]
