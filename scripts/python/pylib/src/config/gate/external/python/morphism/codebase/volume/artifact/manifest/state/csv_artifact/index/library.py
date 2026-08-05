from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.index.key.value import VALUE as CSV_ARTIFACT_INDEX_KEY


def CSV_ARTIFACT_INDEX(state: dict) -> int:
    return state[CSV_ARTIFACT_INDEX_KEY]
