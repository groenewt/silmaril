from config.gate.external.python.morphism.codebase.volume.table.phase14.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.phase14.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.phase14.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
