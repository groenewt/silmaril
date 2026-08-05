from config.constants.morphism.contract.validation.contract.bundle.capture.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.contract.bundle.capture.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.contract.bundle.capture.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.contract.bundle.capture.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.contract.bundle.capture.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(value.frame), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
