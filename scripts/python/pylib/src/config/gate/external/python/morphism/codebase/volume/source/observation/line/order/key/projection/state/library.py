from config.constants.morphism.codebase.volume.source.observation.state.keyed.key.value import VALUE as KEYED_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.source.observation.record.text.library import RECORD_TEXT
from config.gate.external.python.morphism.codebase.volume.source.observation.state.indices.library import INDICES
from config.gate.external.python.morphism.codebase.volume.source.observation.state.numbers.library import NUMBERS
from config.gate.external.python.morphism.codebase.volume.source.observation.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    records = RECORDS(state)
    numbers = NUMBERS(state)
    return {**state, KEYED_KEY: [[[RECORD_PATH(records[index]), numbers[index], RECORD_TEXT(records[index])], index] for index in INDICES(state)]}
