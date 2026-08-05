from config.constants.morphism.codebase.volume.table.state.rows.key.value import VALUE as ROWS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.record.number.library import RECORD_NUMBER
from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.source.observation.record.text.library import RECORD_TEXT
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.family.library import FAMILY
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.identifier.library import IDENTIFIER
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.label.library import LABEL
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    return {**state, ROWS_KEY: [[IDENTIFIER(state), RECORD_PATH(record), RECORD_NUMBER(record), RECORD_TEXT(record)] for record in RECORDS(state)]}
