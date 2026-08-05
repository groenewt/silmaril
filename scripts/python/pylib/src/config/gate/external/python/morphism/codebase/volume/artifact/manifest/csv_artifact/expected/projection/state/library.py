from config.constants.morphism.codebase.volume.artifact.manifest.state.csv_artifact.expected.key.value import VALUE as CSV_ARTIFACT_EXPECTED_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.csv_artifact.index.library import CSV_ARTIFACT_INDEX
from config.gate.external.python.morphism.codebase.volume.tabular.body.library import BODY
from config.gate.external.python.morphism.codebase.volume.tabular.column.library import COLUMN


def STATE(state: dict) -> dict:
    rows = BODY(CONTRACT_ROWS(state))
    return {**state, CSV_ARTIFACT_EXPECTED_KEY: COLUMN(rows, CSV_ARTIFACT_INDEX(state))}
