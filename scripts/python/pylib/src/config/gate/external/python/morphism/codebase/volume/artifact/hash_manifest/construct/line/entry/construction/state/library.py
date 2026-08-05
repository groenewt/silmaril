from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.entries.key.value import VALUE as ENTRIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.matches.library import MATCHES


def STATE(state: dict) -> dict:
    return {**state, ENTRIES_KEY: [list(groups) for groups in MATCHES(state)]}
