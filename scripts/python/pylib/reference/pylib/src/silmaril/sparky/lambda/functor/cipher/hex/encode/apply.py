from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.binascii.hexlify.value import VALUE as Hexlify
def apply(payload: Bytes) -> Bytes: return Hexlify(payload)
