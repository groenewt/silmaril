from config.constants.morphism.codebase.volume.source.observation.state.numbers.key.value import VALUE as NUMBERS_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.integer.library import INTEGER
from config.gate.external.python.morphism.codebase.volume.source.observation.record.number.library import RECORD_NUMBER
from config.gate.external.python.morphism.codebase.volume.source.observation.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    return {**state, NUMBERS_KEY: [INTEGER(RECORD_NUMBER(record)) for record in RECORDS(state)]}
