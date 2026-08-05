from config.gate.external.python.morphism.codebase.volume.native.gdb.source_frame.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.native.gdb.source_frame.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.native.gdb.source_frame.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
