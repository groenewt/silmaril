from config.gate.external.project.sparky.invocation.process.file.library import PROJECT
from .frame.value import Value as Frame
from .input.value import Value as Input

def apply(value: Input) -> Frame: return PROJECT(value)
