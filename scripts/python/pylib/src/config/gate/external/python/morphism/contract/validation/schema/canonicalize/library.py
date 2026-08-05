from config.constants.morphism.contract.validation.schema.canonicalize.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.schema.canonicalize.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.schema.canonicalize.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.canonicalize.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.schema.canonicalize.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(value.frame.payload.strip())), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
