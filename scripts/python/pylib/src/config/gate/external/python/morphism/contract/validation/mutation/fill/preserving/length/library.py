from config.constants.morphism.contract.validation.mutation.fill.preserving.length.effect.provisional.evidence.value import VALUE as PROVISIONAL_EVIDENCE
from config.constants.morphism.contract.validation.mutation.fill.preserving.length.mechanic.translation.table.value import VALUE as TRANSLATION_TABLE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.output.value import Value as Output

def PROJECT(value: Input) -> Frame: return Frame(Output(ByteVector(value.target.payload.translate(TRANSLATION_TABLE))), Effect(ByteVector(PROVISIONAL_EVIDENCE)))
