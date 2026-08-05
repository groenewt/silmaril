from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.entry.key.value import VALUE as CSV_ARTIFACT_ENTRY_KEY


def CSV_ARTIFACT_ENTRY(state: dict) -> list:
    return state[CSV_ARTIFACT_ENTRY_KEY]
