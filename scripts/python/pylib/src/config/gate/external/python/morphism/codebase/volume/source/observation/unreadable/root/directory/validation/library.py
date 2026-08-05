from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.source.observation.transform.root.directory.library import STATE
from config.gate.external.python.morphism.codebase.volume.source.observation.unreadable.boundary.frame.library import FRAME
from silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(ENCODE(STATE(DECODE(VALUE(value)))))
