from config.gate.external.python.morphism.codebase.volume.table.make_targets.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.make_targets.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.make_targets.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
