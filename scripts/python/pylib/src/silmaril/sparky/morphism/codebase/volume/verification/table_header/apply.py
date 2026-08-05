from config.gate.external.python.morphism.codebase.volume.verification.table_header.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.verification.table_header.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.verification.table_header.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
