from config.constants.lambda_.invocation.effect.lineage.identity.value import VALUE as LINEAGE_IDENTITY
from config.constants.lambda_.invocation.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.constants.lambda_.invocation.effect.provisional.identity.value import VALUE as PROVISIONAL_IDENTITY
from config.constants.lambda_.invocation.effect.schema.identity.value import VALUE as SCHEMA_IDENTITY
from config.constants.lambda_.invocation.process.file.effect.state.provisional.identity.value import VALUE as STATE_IDENTITY
from config.constants.lambda_.invocation.process.file.request.gap.identity.value import VALUE as GAP_IDENTITY
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
