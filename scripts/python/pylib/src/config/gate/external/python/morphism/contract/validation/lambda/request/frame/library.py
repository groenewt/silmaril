from config.gate.external.project.sparky.morphism.contract.validation.request.frame.prefix.library import DEPENDENCY as PREFIX
from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.project.sparky.substrate.byte.frame.library import PROJECT as BYTE_FRAME

def PROJECT(value: Bytes) -> Bytes: return BYTE_FRAME(PREFIX + value)
