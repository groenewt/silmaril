from config.gate.external.python.morphism.codebase.volume.table.shared_components.aggregate.required.set.uniqueness.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.shared_components.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.shared_components.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
