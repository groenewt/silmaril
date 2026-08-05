from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.expected.key.value import VALUE as CSV_ARTIFACT_EXPECTED_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.expected.library import CSV_ARTIFACT_EXPECTED
from config.gate.external.python.morphism.codebase.volume.lexical.order.library import ORDER


def STATE(state: dict) -> dict:
    return {**state, CSV_ARTIFACT_EXPECTED_KEY: ORDER(CSV_ARTIFACT_EXPECTED(state))}
