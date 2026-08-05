from config.constants.morphism.codebase.volume.table.evidence.state.digests.key.value import VALUE as DIGESTS_KEY
from config.gate.external.python.morphism.codebase.volume.lexical.digest.library import DIGEST
from config.gate.external.python.morphism.codebase.volume.source.observation.record.text.library import RECORD_TEXT
from config.gate.external.python.morphism.codebase.volume.table.evidence.state.records.library import RECORDS


def STATE(state: dict) -> dict:
    return {**state, DIGESTS_KEY: [DIGEST(RECORD_TEXT(record)) for record in RECORDS(state)]}
