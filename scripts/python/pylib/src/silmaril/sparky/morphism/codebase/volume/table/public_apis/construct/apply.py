from config.gate.external.python.morphism.codebase.volume.table.public_apis.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.public_apis.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.public_apis.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
