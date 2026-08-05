from config.gate.external.python.morphism.codebase.volume.table.gdb_evidence.aggregate.required.set.validation.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
