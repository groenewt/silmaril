from config.constants.morphism.codebase.volume.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.codebase.volume.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from ..source.value import Value as Source


@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    source: Source
    reader: object
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
