from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from ....packet.valid.apply import apply as Valid
from ....projection.self.apply import apply as Render
from ....effect.outcome.ok.apply import apply as Ok
from config.gate.value.protocol.boolean.true.value import VALUE as TRUE
from config.gate.value.effect.outcome.malformed_packet.value import VALUE as ERROR
def apply(payload: Bytes) -> Bytes: return Ok(Render(payload)) if Valid(payload) == TRUE else ERROR
