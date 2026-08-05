from config.constants.morphism.contract.validation.application.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.application.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.application.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.application.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.application.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(value.frame), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
