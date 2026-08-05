from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from config.gate.external.python.morphism.codebase.volume.lexical.lines.library import LINES
from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.text.library import TEXT
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.table.shared_components.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.table.aggregate.transform.shared_components.parse.library import STATE
from silmaril.sparky.morphism.codebase.volume.table.shared_components.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.shared_components.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(ENCODE(STATE(LINES(TEXT(PAYLOAD(VALUE(value)))))))
