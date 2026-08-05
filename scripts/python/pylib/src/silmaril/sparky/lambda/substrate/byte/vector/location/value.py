from config.constants.substrate.byte.vector.location.relation.identity.value import VALUE as RELATION_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from ..value import Value as Vector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: Vector
    relation_identity = RELATION_IDENTITY
