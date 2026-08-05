from config.constants.morphism.contract.validation.configuration.capture.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.configuration.capture.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.configuration.capture.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.configuration.capture.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.configuration.capture.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(value.frame), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
