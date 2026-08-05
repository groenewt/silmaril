from config.gate.external.python.morphism.codebase.volume.native.gdb.verifier.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.native.gdb.verifier.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.native.gdb.verifier.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
