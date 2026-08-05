from config.constants.morphism.codebase.volume.phase14.error.envelope.object.value import VALUE as ENVELOPE_NOT_OBJECT
from config.gate.external.python.stdlib.json.library import DEPENDENCY as JSON


def DECODE(payload: bytes) -> dict:
    envelope = JSON.loads(payload)
    if not isinstance(envelope, dict):
        raise ValueError(ENVELOPE_NOT_OBJECT)
    return envelope
