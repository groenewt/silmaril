from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.projection.fragment.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.projection.fragment.document.library import DOCUMENT
from config.gate.external.python.morphism.codebase.volume.projection.fragment.inclusion.library import INCLUSIONS
from config.gate.external.python.morphism.codebase.volume.projection.fragment.line.library import LINES
from config.gate.external.python.morphism.codebase.volume.projection.fragment.vector.library import VECTOR
from silmaril.sparky.morphism.codebase.volume.projection.fragment.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.fragment.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(DOCUMENT(INCLUSIONS(LINES(PAYLOAD(VALUE(value)))))))
