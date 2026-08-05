from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.python.base.builtins.int.value import VALUE as Int
from config.gate.value.protocol.packet.unit_separator.value import VALUE as SEPARATOR
from config.gate.value.protocol.field.index.workspace.value import VALUE as INDEX
def apply(payload: Bytes) -> Bytes: return payload.split(SEPARATOR)[Int(INDEX)]
