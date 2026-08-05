from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.records.library import RECORDS

VIOLATION = "evidence_rows_record_without_path"
EMPTY = ""


def STATE(state: dict) -> dict:
    if any(RECORD_PATH(record) == EMPTY for record in RECORDS(state)):
        raise ValueError(VIOLATION)
    return state
