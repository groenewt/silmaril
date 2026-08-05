from config.gate.external.python.morphism.codebase.volume.table.scripts.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.scripts.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.scripts.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
