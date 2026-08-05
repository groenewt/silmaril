from config.gate.external.python.stdlib.importlib.library import DEPENDENCY as IMPORTLIB


def _value(module_name: str) -> object:
    return IMPORTLIB.import_module(module_name).VALUE


LINEAGE_IDENTITY = _value("config.constants.lambda.invocation.output.lineage.identity.value")
SCHEMA_IDENTITY = _value("config.constants.lambda.invocation.output.schema.identity.value")
REPOSITORY_COORDINATE_IDENTITY = _value("config.constants.lambda.invocation.process.file.input.coordinate.repository.identity.value")
REQUEST_COORDINATE_IDENTITY = _value("config.constants.lambda.invocation.process.file.input.coordinate.request.identity.value")
RESPONSE_COORDINATE_IDENTITY = _value("config.constants.lambda.invocation.process.file.input.coordinate.response.identity.value")
STAGE_IDENTITY = _value("config.constants.lambda.invocation.process.file.stage.output.state.continue.host.client.readback.identity.value")
TRANSITION_IDENTITY = _value("config.constants.lambda.invocation.process.file.stage.transition.identity.value")
