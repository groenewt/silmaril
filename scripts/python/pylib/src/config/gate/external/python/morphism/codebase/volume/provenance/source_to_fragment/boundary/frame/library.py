from config.constants.morphism.codebase.volume.source.observation.effect.pure.identity.value import VALUE as PURE_EFFECT
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.effect.value import Value as Effect
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.output.value import Value as Output

PURE = Effect(ByteVector(PURE_EFFECT))


def FRAME(vector: ByteVector) -> Frame:
    return Frame(Output(vector), PURE)
