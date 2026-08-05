from config.gate.external.python.morphism.codebase.volume.shared.component.table.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.table.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.table.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
