from config.gate.external.python.morphism.codebase.volume.provenance.volume_matrix.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.provenance.volume_matrix.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.provenance.volume_matrix.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
