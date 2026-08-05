from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB


def _value(module_name: str) -> object:
    return IMPORTLIB.import_module(module_name).VALUE


LINEAGE_IDENTITY = _value("config.constants.lambda.invocation.effect.lineage.identity.value")
PROVISIONAL_EVIDENCE = _value("config.constants.lambda.invocation.effect.provisional.evidence.value")
PROVISIONAL_IDENTITY = _value("config.constants.lambda.invocation.effect.provisional.identity.value")
SCHEMA_IDENTITY = _value("config.constants.lambda.invocation.effect.schema.identity.value")
STATE_IDENTITY = _value("config.constants.lambda.invocation.process.file.effect.state.provisional.identity.value")
GAP_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.gap.identity.value")
