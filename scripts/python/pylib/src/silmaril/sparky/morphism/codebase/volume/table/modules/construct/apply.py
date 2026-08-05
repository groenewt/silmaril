from config.gate.external.python.morphism.codebase.volume.table.modules.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.modules.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.modules.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
