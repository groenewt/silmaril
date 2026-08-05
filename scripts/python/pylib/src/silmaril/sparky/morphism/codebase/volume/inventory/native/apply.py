from config.gate.external.python.morphism.codebase.volume.inventory.native.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.native.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.native.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
