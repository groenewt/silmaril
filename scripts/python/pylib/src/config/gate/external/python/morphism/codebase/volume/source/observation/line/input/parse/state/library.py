from config.constants.morphism.codebase.volume.source.observation.state.ignored.empty.value import VALUE as IGNORED_EMPTY
from config.constants.morphism.codebase.volume.source.observation.state.ignored.key.value import VALUE as IGNORED_KEY
from config.constants.morphism.codebase.volume.source.observation.state.records.key.value import VALUE as RECORDS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.line.input.parse.record.library import RECORD


def STATE(lines: list) -> dict:
    return {IGNORED_KEY: IGNORED_EMPTY, RECORDS_KEY: [RECORD(raw) for raw in lines]}
