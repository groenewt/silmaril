from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB


def _value(module_name: str) -> object:
    return IMPORTLIB.import_module(module_name).VALUE


LINEAGE_IDENTITY = _value("config.constants.lambda.invocation.input.lineage.identity.value")
SCHEMA_IDENTITY = _value("config.constants.lambda.invocation.input.schema.identity.value")
BINDING_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.binding.identity.value")
OPERATION_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.operation.identity.value")
OBJECT_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.role.object.identity.value")
PREDICATE_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.role.predicate.identity.value")
SUBJECT_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.role.subject.identity.value")
SOURCE_EVIDENCE = _value("config.constants.lambda.invocation.process.file.request.source.evidence.value")
VECTOR_IDENTITY = _value("config.constants.lambda.invocation.process.file.request.vector.identity.value")
STAGE_IDENTITY = _value("config.constants.lambda.invocation.process.file.stage.input.state.identity.value")
Effect = IMPORTLIB.import_module("silmaril.sparky.lambda.invocation.process.file.effect.value").Value
Output = IMPORTLIB.import_module("silmaril.sparky.lambda.invocation.process.file.output.value").Value
