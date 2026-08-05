from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    scan_identity: ByteVector
    attempt: ByteVector
    transition_identity: ByteVector
    from_state: ByteVector
    to_state: ByteVector
    effect: ByteVector
    evidence_class: ByteVector
    serialized: ByteVector
    digest: ByteVector
