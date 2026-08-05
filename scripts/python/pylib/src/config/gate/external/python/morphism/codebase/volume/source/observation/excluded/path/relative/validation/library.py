from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.source.observation.excluded.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.source.observation.transform.path.relative.library import STATE
from silmaril.sparky.morphism.codebase.volume.source.observation.excluded.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.source.observation.excluded.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(ENCODE(STATE(DECODE(VALUE(value)))))
