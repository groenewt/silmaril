import re as REGEX

from config.constants.morphism.contract.validation.mechanic.format.effect.applied.identity.value import VALUE as APPLIED_EFFECT
from config.constants.morphism.contract.validation.mechanic.format.effect.decode.failure.identity.value import VALUE as DECODE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.format.effect.parse.failure.identity.value import VALUE as PARSE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.format.effect.rejected.identity.value import VALUE as REJECTED_EFFECT
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.python.morphism.contract.validation.schema.format.date.time.pattern.value import VALUE as DATE_TIME
from config.gate.external.python.morphism.contract.validation.schema.format.uri.pattern.value import VALUE as URI
from config.gate.external.python.morphism.contract.validation.schema.format.uri.reference.pattern.value import VALUE as URI_REFERENCE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.mechanic.format.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mechanic.format.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.format.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.mechanic.format.output.value import Value as Output

SEPARATOR = b"\x00"
ACCEPTED_FORMAT = rb"(?:uri\x00" + URI + rb"|uri-reference\x00" + URI_REFERENCE + rb"|date-time\x00" + DATE_TIME + rb")"
CLASSIFIER = REGEX.compile(rb"(?P<accepted>" + ACCEPTED_FORMAT + rb")|(?P<decode_failure>[\x00-\xff]*[\x80-\xff][\x00-\xff]*)|(?P<parse_failure>(?!(?:uri|uri-reference|date-time)\x00)[\x00-\x7f]*)|(?P<rejected>[\x00-\x7f]*)")
FRAMES = {
    "accepted": Frame(Output(ByteVector(ACCEPTED)), Effect(ByteVector(APPLIED_EFFECT))),
    "decode_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(DECODE_FAILURE_EFFECT))),
    "parse_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(PARSE_FAILURE_EFFECT))),
    "rejected": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(REJECTED_EFFECT))),
}

def PROJECT(value: Input) -> Frame: return FRAMES[CLASSIFIER.fullmatch(value.format.payload + SEPARATOR + value.value.payload).lastgroup]
