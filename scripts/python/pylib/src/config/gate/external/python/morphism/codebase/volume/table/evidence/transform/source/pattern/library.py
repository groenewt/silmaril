from config.constants.morphism.codebase.volume.table.evidence.state.records.key.value import VALUE as RECORDS_KEY
from config.gate.external.python.morphism.codebase.volume.source.observation.line.input.parse.record.library import RECORD
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    return {**state, RECORDS_KEY: [RECORD(record) for record in RECORDS(state) if record]}
