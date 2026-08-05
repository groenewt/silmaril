from config.gate.external.python.morphism.codebase.volume.inventory.relation.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.relation.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.relation.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
