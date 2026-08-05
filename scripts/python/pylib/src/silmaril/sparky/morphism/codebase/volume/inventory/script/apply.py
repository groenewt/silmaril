from config.gate.external.python.morphism.codebase.volume.inventory.script.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.script.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.script.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
