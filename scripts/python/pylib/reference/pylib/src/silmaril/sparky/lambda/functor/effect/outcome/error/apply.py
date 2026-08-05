from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.value.effect.outcome.malformed_packet.value import VALUE as ERROR_PACKET
def apply(payload: Bytes) -> Bytes: return ERROR_PACKET
