from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    map_root: ByteVector
    mapped_target: ByteVector
    map_unit: ByteVector
    map_revision: ByteVector
    drilldown_chain: ByteVector
    evidence_class: ByteVector
