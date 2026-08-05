from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.entries.key.value import VALUE as ENTRIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.ordinal.library import ORDINAL
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.entries.library import ENTRIES


def STATE(state: dict) -> dict:
    return {**state, ENTRIES_KEY: sorted(ENTRIES(state), key=ORDINAL)}
