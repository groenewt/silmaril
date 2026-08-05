from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from ....projection.self.apply import apply as RenderSelf
from ....digest.sha256.apply import apply as Digest
def apply(payload: Bytes) -> Bytes: return Digest(RenderSelf(payload))
