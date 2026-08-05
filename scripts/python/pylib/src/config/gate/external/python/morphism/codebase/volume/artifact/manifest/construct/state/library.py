from config.constants.morphism.codebase.volume.artifact.manifest.envelope.field.order.value import VALUE as ENVELOPE_ORDER
from config.constants.morphism.codebase.volume.artifact.manifest.schema.version.value import VALUE as SCHEMA_VERSION
from config.constants.morphism.codebase.volume.artifact.manifest.state.gaps.key.value import VALUE as GAPS_KEY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.construct.artifacts.library import ARTIFACTS
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.construct.publication.library import PUBLICATION
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.entry.library import ENTRY
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.state.inventories.library import INVENTORIES

ARTIFACTS_FIELD, GAPS_FIELD, INVENTORIES_FIELD, PUBLICATION_FIELD, SCHEMA_VERSION_FIELD = ENVELOPE_ORDER
VIOLATION = "manifest_envelope_field_order_drift="


def STATE(state: dict) -> dict:
    envelope = {
        ARTIFACTS_FIELD: ARTIFACTS(state),
        GAPS_FIELD: list(state[GAPS_KEY]),
        INVENTORIES_FIELD: [ENTRY(inventory) for inventory in INVENTORIES(state)],
        PUBLICATION_FIELD: PUBLICATION(state),
        SCHEMA_VERSION_FIELD: SCHEMA_VERSION,
    }
    if tuple(envelope) != ENVELOPE_ORDER:
        raise ValueError(VIOLATION + ",".join(envelope))
    return envelope
