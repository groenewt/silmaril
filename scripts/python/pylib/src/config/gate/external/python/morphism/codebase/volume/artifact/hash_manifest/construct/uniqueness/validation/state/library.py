from config.gate.external.python.morphism.codebase.volume.artifact.hash_manifest.state.identities.library import IDENTITIES
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT

VIOLATION = "hash_manifest_path_duplicate_count="


def STATE(state: dict) -> dict:
    identities = IDENTITIES(state)
    distinct = set(identities)
    if len(distinct) != len(identities) and STRICT():
        raise ValueError(VIOLATION + str(len(identities) - len(distinct)))
    return state
