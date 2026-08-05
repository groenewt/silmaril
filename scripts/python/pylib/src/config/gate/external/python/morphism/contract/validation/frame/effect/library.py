from config.constants.morphism.contract.validation.frame.kind.effect.prefix.value import VALUE as PREFIX
from config.gate.external.python.base.builtins.bytes.value import VALUE as Bytes
from config.gate.external.project.sparky.substrate.byte.frame.library import PROJECT as BYTE_FRAME

def PROJECT(value: Bytes) -> Bytes: return BYTE_FRAME(PREFIX + value)
