from config.gate.external.python.morphism.codebase.volume.lexical.lines.library import LINES
from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.text.library import TEXT
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.table.public_apis.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.table.transform.construct.public_apis.library import RENDER
from config.gate.external.python.morphism.codebase.volume.table.encode.library import ENCODE_TABLE
from silmaril.sparky.morphism.codebase.volume.table.public_apis.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.public_apis.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(ENCODE_TABLE(RENDER(LINES(TEXT(PAYLOAD(VALUE(value))))))))
