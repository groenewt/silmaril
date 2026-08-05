from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.builtins.int.value import VALUE as Int
from config.gate.value.protocol.packet.unit_separator.value import VALUE as SEPARATOR
from config.gate.value.protocol.packet.expected_separator_count.value import VALUE as EXPECTED
from config.gate.value.protocol.boolean.true.value import VALUE as TRUE
from config.gate.value.protocol.boolean.false.value import VALUE as FALSE
def apply(payload: Bytes) -> Bytes: return TRUE if payload.count(SEPARATOR) == Int(EXPECTED) else FALSE
