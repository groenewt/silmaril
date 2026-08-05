from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.table.gdb_evidence.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.table.aggregate.transform.gdb_evidence.required.set.uniqueness.library import STATE
from silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(ENCODE(STATE(DECODE(VALUE(value)))))
