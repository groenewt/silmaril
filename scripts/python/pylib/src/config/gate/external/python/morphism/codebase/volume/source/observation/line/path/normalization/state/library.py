from config.constants.morphism.codebase.volume.source.observation.state.records.key.value import VALUE as RECORDS_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.relative.library import RELATIVE
from config.gate.external.python.morphism.codebase.volume.source.observation.record.number.library import RECORD_NUMBER
from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.source.observation.record.text.library import RECORD_TEXT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    return {**state, RECORDS_KEY: [[RELATIVE(RECORD_PATH(record)), RECORD_NUMBER(record), RECORD_TEXT(record)] for record in RECORDS(state)]}
