from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.contract.rows.library import CONTRACT_ROWS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.fragment_artifact.index.library import FRAGMENT_ARTIFACT_INDEX
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventory.identity.index.library import INVENTORY_IDENTITY_INDEX


def FRAGMENTS(state: dict) -> dict:
    identity_index = INVENTORY_IDENTITY_INDEX(state)
    fragment_index = FRAGMENT_ARTIFACT_INDEX(state)
    return {row[identity_index]: row[fragment_index] for row in CONTRACT_ROWS(state)}
