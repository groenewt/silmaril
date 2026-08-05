from config.constants.morphism.codebase.volume.artifact.manifest.contract.column.csv_artifact.value import VALUE as CSV_ARTIFACT_COLUMN
from config.constants.morphism.codebase.volume.lexical.position.absent.value import VALUE as ABSENT_POSITION
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.index.library import CSV_ARTIFACT_INDEX
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "manifest_contract_column_absent="


def STATE(state: dict) -> dict:
    if CSV_ARTIFACT_INDEX(state) == ABSENT_POSITION and STRICT():
        raise ValueError(VIOLATION + CSV_ARTIFACT_COLUMN)
    return state
