from config.gate.external.project.sparky.invocation.process.file.effect.library import GAP_IDENTITY, LINEAGE_IDENTITY, PROVISIONAL_EVIDENCE, PROVISIONAL_IDENTITY, SCHEMA_IDENTITY, STATE_IDENTITY
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from .....substrate.byte.vector.value import Value as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    frame: ByteVector
    schema_identity = SCHEMA_IDENTITY
    lineage_identity = LINEAGE_IDENTITY
    identity = PROVISIONAL_IDENTITY
    evidence = PROVISIONAL_EVIDENCE
    state_identity = STATE_IDENTITY
    gap_identity = GAP_IDENTITY
