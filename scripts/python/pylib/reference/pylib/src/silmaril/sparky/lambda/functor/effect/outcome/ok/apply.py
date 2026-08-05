from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.value.effect.outcome.ok_prefix.value import VALUE as OK_PREFIX
def apply(payload: Bytes) -> Bytes: return OK_PREFIX + payload
