from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.construct.input.parse.state.library import STATE as PARSED
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.construct.receipt.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.construct.relation.state.library import STATE as RELATED
from config.gate.external.python.morphism.codebase.volume.provenance.source_to_fragment.construct.validation.state.library import STATE as VALIDATED
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(VALIDATED(RELATED(PARSED(DECODE(VALUE(value))))))))
