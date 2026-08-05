from config.gate.external.python.morphism.codebase.volume.inventory.public_api.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.inventory.public_api.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.inventory.public_api.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
