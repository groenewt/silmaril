from config.gate.external.python.morphism.codebase.volume.inventory.module.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.module.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.module.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
