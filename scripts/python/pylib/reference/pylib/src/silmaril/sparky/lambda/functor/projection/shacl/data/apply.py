from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from ....projection.shacl.data.section.s0000.apply import apply as S0000
from ....projection.shacl.data.section.s0001.apply import apply as S0001
from ....projection.shacl.data.section.s0002.apply import apply as S0002
from ....projection.shacl.data.section.s0003.apply import apply as S0003
from ....projection.shacl.data.section.s0004.apply import apply as S0004
from ....projection.shacl.data.section.s0005.apply import apply as S0005
from ....projection.shacl.data.section.s0006.apply import apply as S0006
def apply(payload: Bytes) -> Bytes: return S0000(payload) + S0001(payload) + S0002(payload) + S0003(payload) + S0004(payload) + S0005(payload) + S0006(payload)
