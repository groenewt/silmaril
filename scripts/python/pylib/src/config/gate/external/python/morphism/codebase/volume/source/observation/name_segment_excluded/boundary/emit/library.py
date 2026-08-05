from config.gate.external.python.morphism.codebase.volume.frame.output.library import OUTPUT
from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.frame.value import Value as Frame


def EMIT(frame: Frame) -> bytes:
    return PAYLOAD(VALUE(OUTPUT(frame)))
