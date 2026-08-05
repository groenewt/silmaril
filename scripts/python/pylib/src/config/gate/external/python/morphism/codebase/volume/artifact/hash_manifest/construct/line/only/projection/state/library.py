from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.lines.key.value import VALUE as LINES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.payloads.library import PAYLOADS
from config.gate.external.python.morphism.codebase.volume.lexical.chomp.library import CHOMP
from config.gate.external.python.morphism.codebase.volume.lexical.first.library import FIRST
from config.gate.external.python.morphism.codebase.volume.lexical.lines.library import LINES


def STATE(state: dict) -> dict:
    return {**state, LINES_KEY: [CHOMP(FIRST(LINES(payload))) for payload in PAYLOADS(state)]}
