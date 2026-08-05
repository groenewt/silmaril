from config.gate.external.python.morphism.codebase.volume.table.tests.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.tests.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.tests.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
