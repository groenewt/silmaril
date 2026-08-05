from config.constants.morphism.codebase.volume.projection.chapter.provenance_relations_gaps.construct.title.value import VALUE as TITLE
from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.projection.fragment.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.projection.fragment.document.library import DOCUMENT
from config.gate.external.python.morphism.codebase.volume.projection.fragment.heading.library import HEADING
from config.gate.external.python.morphism.codebase.volume.projection.fragment.inclusion.library import INCLUSIONS
from config.gate.external.python.morphism.codebase.volume.projection.fragment.line.library import LINES
from config.gate.external.python.morphism.codebase.volume.projection.fragment.vector.library import VECTOR
from silmaril.sparky.morphism.codebase.volume.projection.fragment.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.fragment.input.value import Value as Input

HEADER = HEADING(TITLE)


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(DOCUMENT((HEADER, *INCLUSIONS(LINES(PAYLOAD(VALUE(value))))))))
