from config.gate.external.python.morphism.codebase.volume.artifact.manifest.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.artifact.manifest.expected.body.construction.state.library import STATE
from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(ENCODE(STATE(DECODE(VALUE(value)))))
