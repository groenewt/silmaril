from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.observed.key.value import VALUE as CSV_ARTIFACT_OBSERVED_KEY


def CSV_ARTIFACT_OBSERVED(state: dict) -> list:
    return state[CSV_ARTIFACT_OBSERVED_KEY]
