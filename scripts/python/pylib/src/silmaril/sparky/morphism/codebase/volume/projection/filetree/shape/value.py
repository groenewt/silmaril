from config.constants.morphism.codebase.volume.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.codebase.volume.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from ..record.value import Value as Record


@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    record: Record
    resolution: dict
    header: tuple
    reader: object
    group_index: int
    detail_indexes: tuple
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
