from config.gate.external.python.morphism.codebase.volume.table.native_tree.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.native_tree.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.native_tree.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
