from config.constants.morphism.codebase.volume.artifact.manifest.envelope.field.order.value import VALUE as ENVELOPE_ORDER
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.inventory.entry.library import ENTRY

INVENTORIES_POSITION = 2
VIOLATION = "manifest_envelope_field_absent="


def REORDER(envelope: dict) -> dict:
    missing = [field for field in ENVELOPE_ORDER if field not in envelope]
    if missing:
        raise ValueError(VIOLATION + ",".join(missing))
    inventories = ENVELOPE_ORDER[INVENTORIES_POSITION]
    ordered = {field: envelope[field] for field in ENVELOPE_ORDER}
    ordered[inventories] = [ENTRY(inventory) for inventory in ordered[inventories]]
    return ordered
