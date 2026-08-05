from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.builtins.format.value import VALUE as Format
from config.gate.value.protocol.byte.empty.value import VALUE as EMPTY
from config.gate.value.protocol.format.binary_08.value import VALUE as FORMAT_SPEC
def apply(payload: Bytes) -> Bytes: return EMPTY.join(Format(byte, FORMAT_SPEC.decode()).encode() for byte in payload)
