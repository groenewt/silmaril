from config.gate.external.python.morphism.codebase.volume.lexical.payload.library import PAYLOAD
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.lexical.vector.library import VECTOR
from config.gate.external.python.morphism.codebase.volume.table.encode.library import ENCODE_TABLE
from config.gate.external.python.morphism.codebase.volume.table.phase14.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.table.phase14.envelope.decode.library import DECODE
from config.gate.external.python.morphism.codebase.volume.table.phase14.envelope.records.library import RECORDS
from config.gate.external.python.morphism.codebase.volume.table.transform.construct.phase14.library import RENDER
from silmaril.sparky.morphism.codebase.volume.table.phase14.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.phase14.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(VECTOR(ENCODE_TABLE(RENDER(RECORDS(DECODE(PAYLOAD(VALUE(value))))))))
