from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.source.observation.line.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.source.observation.line.line.encode.render.library import RENDER
from silmaril.sparky.morphism.codebase.volume.source.observation.line.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.line.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(DECODE(VALUE(value)))))
