from config.gate.external.python.morphism.codebase.volume.shared.component.projection_wrapper.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.shared.component.projection_wrapper.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.shared.component.projection_wrapper.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
