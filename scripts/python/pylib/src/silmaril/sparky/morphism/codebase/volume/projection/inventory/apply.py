from config.gate.external.python.morphism.codebase.volume.projection.inventory.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.projection.inventory.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.projection.inventory.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
