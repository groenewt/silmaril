from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.source.observation.symlink.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.source.observation.transform.line.encode.library import RENDER
from silmaril.sparky.morphism.codebase.volume.source.observation.symlink.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.symlink.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(RENDER(DECODE(VALUE(value)))))
