from config.constants.morphism.contract.validation.determinism.reverse.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.determinism.reverse.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.determinism.reverse.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.determinism.reverse.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.determinism.reverse.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(value.target.payload[::-1])), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
