from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from ....projection.linkml.receipt.section.s0000.apply import apply as S0000
from ....projection.linkml.receipt.section.s0001.apply import apply as S0001
def apply(payload: Bytes) -> Bytes: return S0000(payload) + S0001(payload)
