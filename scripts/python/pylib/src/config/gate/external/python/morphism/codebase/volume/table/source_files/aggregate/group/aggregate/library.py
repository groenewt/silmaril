from config.gate.external.python.morphism.codebase.volume.codec.library import DECODE
from config.gate.external.python.morphism.codebase.volume.codec.library import ENCODE
from config.gate.external.python.morphism.codebase.volume.lexical.value.library import VALUE
from config.gate.external.python.morphism.codebase.volume.table.source_files.boundary.frame.library import FRAME
from config.gate.external.python.morphism.codebase.volume.table.aggregate.transform.source_files.group.library import STATE
from silmaril.sparky.morphism.codebase.volume.table.source_files.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.source_files.input.value import Value as Input


def PROJECT(value: Input) -> Frame:
    return FRAME(ENCODE(STATE(DECODE(VALUE(value)))))
