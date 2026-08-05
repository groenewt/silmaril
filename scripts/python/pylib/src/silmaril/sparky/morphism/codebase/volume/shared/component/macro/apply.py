from config.gate.external.python.morphism.codebase.volume.shared.component.macro.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.macro.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.macro.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
