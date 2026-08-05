from config.constants.morphism.contract.validation.mutation.append.copy.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.mutation.append.copy.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mutation.append.copy.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mutation.append.copy.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.mutation.append.copy.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(value.target.payload + value.copy.payload)), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
