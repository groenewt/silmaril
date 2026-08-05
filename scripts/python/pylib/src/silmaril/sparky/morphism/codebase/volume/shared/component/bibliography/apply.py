from config.gate.external.python.morphism.codebase.volume.shared.component.bibliography.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.bibliography.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.bibliography.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
