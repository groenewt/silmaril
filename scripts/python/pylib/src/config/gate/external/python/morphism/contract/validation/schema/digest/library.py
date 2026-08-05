from config.constants.morphism.contract.validation.schema.digest.effect.applied.identity.value import VALUE as APPLIED
from config.gate.external.python.stdlib.hashlib.library import DEPENDENCY as HASH
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.schema.digest.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.schema.digest.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.digest.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.schema.digest.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(HASH.sha256(value.frame.payload).digest())), Effect(ByteVector(APPLIED)))
