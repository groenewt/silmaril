from config.gate.external.python.morphism.codebase.volume.shared.component.diagram.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.diagram.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.diagram.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
