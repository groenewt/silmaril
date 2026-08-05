from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.binascii.unhexlify.value import VALUE as Unhexlify
def apply(payload: Bytes) -> Bytes: return Unhexlify(payload)
