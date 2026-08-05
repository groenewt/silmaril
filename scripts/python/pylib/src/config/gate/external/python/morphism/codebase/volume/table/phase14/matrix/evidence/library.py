from config.constants.morphism.codebase.volume.phase14.error.record.identity.value import VALUE as IDENTITY_ABSENT
from config.constants.morphism.codebase.volume.phase14.matrix.record.event.field.value import VALUE as EVENT_FIELD
from config.constants.morphism.codebase.volume.phase14.matrix.record.identity.field.value import VALUE as IDENTITY_FIELDS
from config.gate.external.python.stdlib.json.library import DEPENDENCY as JSON

ABSENT = ""
SEPARATOR = "="
ITEM_SEPARATOR = ","
KEY_SEPARATOR = ":"


def EVIDENCE(record: dict) -> str:
    if record is None:
        return ABSENT
    identity = {field: record[field] for field in IDENTITY_FIELDS if record.get(field) is not None}
    if not identity:
        raise ValueError(f"{IDENTITY_ABSENT}{SEPARATOR}{record.get(EVENT_FIELD)}")
    return JSON.dumps(dict(sorted(identity.items())), separators=(ITEM_SEPARATOR, KEY_SEPARATOR))
