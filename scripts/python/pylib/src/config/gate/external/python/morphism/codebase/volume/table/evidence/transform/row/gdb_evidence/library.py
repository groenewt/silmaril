from config.constants.morphism.codebase.volume.table.state.rows.key.value import VALUE as ROWS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.record.number.library import RECORD_NUMBER
from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.source.observation.record.text.library import RECORD_TEXT
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.family.library import FAMILY
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.identifier.library import IDENTIFIER
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.label.library import LABEL
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.records.library import RECORDS
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.digests.library import DIGESTS


def STATE(state: dict) -> dict:
    digests = DIGESTS(state)
    return {**state, ROWS_KEY: [[IDENTIFIER(state), RECORD_PATH(record), RECORD_NUMBER(record), digests[index], RECORD_TEXT(record)] for index, record in enumerate(RECORDS(state))]}
