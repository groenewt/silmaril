from config.gate.external.python.morphism.codebase.volume.table.provenance.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.provenance.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.provenance.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
