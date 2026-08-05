from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.identity.library import INVENTORY_IDENTITIES
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.unique.library import INVENTORY_UNIQUE
from config.gate.external.python.morphism.codebase.volume.artifact.strict.library import STRICT
from config.gate.external.python.morphism.codebase.volume.lexical.cardinality.library import CARDINALITY
from config.gate.external.python.morphism.codebase.volume.lexical.joined.library import JOINED
from config.gate.external.python.morphism.codebase.volume.lexical.repeated.library import REPEATED

VIOLATION = "manifest_inventory_identity_repeated="


def STATE(state: dict) -> dict:
    identities = INVENTORY_IDENTITIES(state)
    if CARDINALITY(INVENTORY_UNIQUE(state)) != CARDINALITY(identities) and STRICT():
        raise ValueError(VIOLATION + JOINED(REPEATED(identities)))
    return state
