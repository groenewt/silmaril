from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.observed.key.value import VALUE as CSV_ARTIFACT_OBSERVED_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.entry.library import CSV_ARTIFACT_ENTRY
from config.gate.external.python.morphism.codebase.volume.lexical.order.library import ORDER


def STATE(state: dict) -> dict:
    return {**state, CSV_ARTIFACT_OBSERVED_KEY: ORDER(CSV_ARTIFACT_ENTRY(state))}
