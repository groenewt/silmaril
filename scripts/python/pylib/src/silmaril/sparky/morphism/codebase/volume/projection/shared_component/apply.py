from config.gate.external.python.morphism.codebase.volume.projection.shared_component.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.projection.shared_component.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.shared_component.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
