from config.gate.external.python.morphism.codebase.volume.table.telephone_topology.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.telephone_topology.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.telephone_topology.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
