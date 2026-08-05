from config.constants.morphism.contract.validation.schema.diagnostic.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.schema.diagnostic.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.schema.diagnostic.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.diagnostic.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.schema.diagnostic.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(value.frame), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
