from config.gate.external.python.morphism.codebase.volume.native.gdb.hash.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.native.gdb.hash.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.native.gdb.hash.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
