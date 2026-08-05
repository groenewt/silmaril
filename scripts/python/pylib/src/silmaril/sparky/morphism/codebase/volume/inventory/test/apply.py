from config.gate.external.python.morphism.codebase.volume.inventory.test.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.test.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.test.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
