from config.constants.morphism.codebase.volume.phase14.error.event.duplicate.value import VALUE as DUPLICATE_EVENT
from config.constants.morphism.codebase.volume.phase14.matrix.event.name.value import VALUE as EVENT_NAMES
from config.constants.morphism.codebase.volume.phase14.matrix.record.event.field.value import VALUE as EVENT_FIELD

CANONICAL = frozenset(EVENT_NAMES)
SEPARATOR = "="


def INDEX(records: tuple) -> dict:
    index = {}
    for record in records:
        event = record.get(EVENT_FIELD)
        if event not in CANONICAL:
            continue
        if event in index:
            raise ValueError(f"{DUPLICATE_EVENT}{SEPARATOR}{event}")
        index[event] = record
    return index
