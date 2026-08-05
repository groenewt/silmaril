from config.gate.external.python.morphism.codebase.volume.artifact.manifest.csv_artifact.observed.canonical_order.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.artifact.manifest.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
