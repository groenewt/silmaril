from config.constants.morphism.codebase.volume.artifact.hash_manifest.state.entries.key.value import VALUE as ENTRIES_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.entries.library import ENTRIES
from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.paths.library import PATHS
from config.gate.external.python.morphism.codebase.volume.lexical.first.library import FIRST


def STATE(state: dict) -> dict:
    return {**state, ENTRIES_KEY: [[FIRST(entry), path] for entry, path in zip(ENTRIES(state), PATHS(state))]}
