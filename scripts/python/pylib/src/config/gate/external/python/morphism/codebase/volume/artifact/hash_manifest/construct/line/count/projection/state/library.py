from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.counts.key.value import VALUE as COUNTS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.payloads.library import PAYLOADS
from config.gate.external.python.morphism.codebase.volume.lexical.lines.library import LINES


def STATE(state: dict) -> dict:
    return {**state, COUNTS_KEY: [len(LINES(payload)) for payload in PAYLOADS(state)]}
