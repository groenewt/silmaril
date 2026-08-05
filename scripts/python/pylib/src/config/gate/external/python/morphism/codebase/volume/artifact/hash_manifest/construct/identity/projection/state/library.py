from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.identities.key.value import VALUE as IDENTITIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.entries.library import ENTRIES
from config.gate.external.python.morphism.codebase.volume.lexical.last.library import LAST


def STATE(state: dict) -> dict:
    return {**state, IDENTITIES_KEY: [LAST(entry) for entry in ENTRIES(state)]}
