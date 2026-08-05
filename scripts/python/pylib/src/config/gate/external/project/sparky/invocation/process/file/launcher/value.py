from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB

APPLY = IMPORTLIB.import_module("silmaril.sparky.lambda.invocation.process.file.apply").apply
Launcher = IMPORTLIB.import_module(
    "silmaril.sparky.lambda.invocation.process.file.launcher.signature.value"
).Value

VALUE: Launcher = lambda value: APPLY(value)
