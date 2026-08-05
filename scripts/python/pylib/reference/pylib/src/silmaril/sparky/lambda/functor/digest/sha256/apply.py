from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.hashlib.sha256.value import VALUE as Sha256
def apply(payload: Bytes) -> Bytes: return Sha256(payload).hexdigest().encode()
