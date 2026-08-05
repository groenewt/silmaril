from config.constants.morphism.codebase.volume.phase14.envelope.records.field.value import VALUE as RECORDS_FIELD
from config.constants.morphism.codebase.volume.phase14.error.record.object.value import VALUE as RECORD_NOT_OBJECT
from config.constants.morphism.codebase.volume.phase14.error.records.array.value import VALUE as RECORDS_NOT_ARRAY


def RECORDS(envelope: dict) -> tuple:
    records = envelope.get(RECORDS_FIELD)
    if not isinstance(records, list):
        raise ValueError(RECORDS_NOT_ARRAY)
    for record in records:
        if not isinstance(record, dict):
            raise ValueError(RECORD_NOT_OBJECT)
    return tuple(records)
