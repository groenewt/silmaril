from config.constants.morphism.codebase.volume.source.observation.state.segments.key.value import VALUE as SEGMENTS_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.split.library import SPLIT
from config.gate.external.python.morphism.codebase.volume.source.observation.record.path.library import RECORD_PATH
from config.gate.external.python.morphism.codebase.volume.source.observation.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    return {**state, SEGMENTS_KEY: [SPLIT(RECORD_PATH(record)) for record in RECORDS(state)]}
