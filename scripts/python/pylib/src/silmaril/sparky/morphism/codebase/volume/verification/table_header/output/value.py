from config.constants.morphism.codebase.volume.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.morphism.codebase.volume.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES


@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    value: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
