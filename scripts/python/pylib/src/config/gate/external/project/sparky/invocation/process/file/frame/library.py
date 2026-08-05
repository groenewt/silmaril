from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB


def _value(module_name: str) -> object:
    return IMPORTLIB.import_module(module_name).VALUE


LINEAGE_IDENTITY = _value("config.constants.lambda.invocation.frame.lineage.identity.value")
SCHEMA_IDENTITY = _value("config.constants.lambda.invocation.frame.schema.identity.value")
Effect = IMPORTLIB.import_module("silmaril.sparky.lambda.invocation.process.file.effect.value").Value
Output = IMPORTLIB.import_module("silmaril.sparky.lambda.invocation.process.file.output.value").Value
