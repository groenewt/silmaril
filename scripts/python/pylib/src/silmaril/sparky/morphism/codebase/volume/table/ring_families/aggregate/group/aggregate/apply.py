from config.gate.external.python.morphism.codebase.volume.table.ring_families.aggregate.group.aggregate.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.ring_families.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.ring_families.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
