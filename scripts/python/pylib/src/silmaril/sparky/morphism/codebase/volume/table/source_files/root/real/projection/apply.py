from config.gate.external.python.morphism.codebase.volume.table.source_files.root.real.projection.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.source_files.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.source_files.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
