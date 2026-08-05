from config.constants.morphism.contract.validation.entry.twin.readback.effect.observed.identity.value import VALUE as OBSERVED
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.entry.twin.readback.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.entry.twin.readback.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.entry.twin.readback.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.entry.twin.readback.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(ACCEPTED if value.source.payload == value.twin.payload else REJECTED)), Effect(ByteVector(OBSERVED)))
