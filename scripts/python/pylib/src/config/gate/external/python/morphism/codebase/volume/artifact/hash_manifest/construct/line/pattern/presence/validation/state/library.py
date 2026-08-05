from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.lines.library import LINES_OF
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.matches.library import MATCHES
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "hash_manifest_line_malformed="


def STATE(state: dict) -> dict:
    malformed = [line for line, groups in zip(LINES_OF(state), MATCHES(state)) if not groups]
    if malformed and STRICT():
        raise ValueError(VIOLATION + malformed[0])
    return state
