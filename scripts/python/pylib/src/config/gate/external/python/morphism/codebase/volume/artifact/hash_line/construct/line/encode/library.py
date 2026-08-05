from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.artifact.hash_line.construct.line.encode.render.library import RENDER
from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(DECODE(VALUE(value)))))
