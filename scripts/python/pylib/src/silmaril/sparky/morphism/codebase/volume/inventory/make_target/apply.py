from config.gate.external.python.morphism.codebase.volume.inventory.make_target.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.make_target.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.make_target.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
