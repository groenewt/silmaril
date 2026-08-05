from config.constants.morphism.contract.validation.entry.self.test.effect.observed.identity.value import VALUE as OBSERVED
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.entry.self.test.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.entry.self.test.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.entry.self.test.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.entry.self.test.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(ACCEPTED if value.expected.payload == value.observed.payload else REJECTED)), Effect(ByteVector(OBSERVED)))
