from config.gate.external.python.morphism.codebase.volume.inventory.telephone.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.telephone.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.telephone.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
