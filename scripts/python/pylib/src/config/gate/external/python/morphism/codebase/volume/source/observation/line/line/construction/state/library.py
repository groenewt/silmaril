from config.constants.morphism.codebase.volume.source.observation.state.lines.key.value import VALUE as LINES_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.record.number.library import RECORD_NUMBER
from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.source.observation.record.text.library import RECORD_TEXT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.records.library import RECORDS

FIELD_SEPARATOR = ":"
LINE_FEED = "\n"


def STATE(state: dict) -> dict:
    return {**state, LINES_KEY: [RECORD_PATH(record) + FIELD_SEPARATOR + RECORD_NUMBER(record) + FIELD_SEPARATOR + RECORD_TEXT(record) + LINE_FEED for record in RECORDS(state)]}
