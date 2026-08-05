from config.gate.external.python.morphism.codebase.volume.table.project_tasks.construct.library import PROJECT
from silmaril.sparky.morphism.codebase.volume.table.project_tasks.frame.value import Value as Frame
from silmaril.sparky.morphism.codebase.volume.table.project_tasks.input.value import Value as Input


def apply(value: Input) -> Frame:
    return PROJECT(value)
