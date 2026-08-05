from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from ....projection.linkml.instance.section.s0000.apply import apply as S0000
from ....projection.linkml.instance.section.s0001.apply import apply as S0001
from ....projection.linkml.instance.section.s0002.apply import apply as S0002
from ....projection.linkml.instance.section.s0003.apply import apply as S0003
from ....projection.linkml.instance.section.s0004.apply import apply as S0004
from ....projection.linkml.instance.section.s0005.apply import apply as S0005
def apply(payload: Bytes) -> Bytes: return S0000(payload) + S0001(payload) + S0002(payload) + S0003(payload) + S0004(payload) + S0005(payload)
