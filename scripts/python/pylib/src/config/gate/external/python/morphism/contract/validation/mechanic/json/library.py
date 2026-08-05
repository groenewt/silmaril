import re as REGEX

from config.constants.morphism.contract.validation.mechanic.json.effect.applied.identity.value import VALUE as APPLIED_EFFECT
from config.constants.morphism.contract.validation.mechanic.json.effect.decode.failure.identity.value import VALUE as DECODE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.json.effect.parse.failure.identity.value import VALUE as PARSE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.json.effect.rejected.identity.value import VALUE as REJECTED_EFFECT
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.mechanic.json.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mechanic.json.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.json.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.mechanic.json.output.value import Value as Output

JSON_STRING_CONTENT = rb"(?:\\(?:[\"\\/bfnrt]|u[0-9A-Fa-f]{4})|[\x20-\x21\x23-\x5b\x5d-\x7e])*"
JSON_STRING = rb"\"" + JSON_STRING_CONTENT + rb"\""
JSON_NUMBER = rb"-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"
JSON_SCALAR = rb"(?:" + JSON_STRING + rb"|" + JSON_NUMBER + rb"|true|false|null)"
JSON_MEMBER = JSON_STRING + rb"\s*:\s*" + JSON_SCALAR
JSON_OBJECT = rb"\{\s*(?:" + JSON_MEMBER + rb"(?:\s*,\s*" + JSON_MEMBER + rb")*)?\s*\}"
JSON_ARRAY = rb"\[\s*(?:" + JSON_SCALAR + rb"(?:\s*,\s*" + JSON_SCALAR + rb")*)?\s*\]"
JSON_DOCUMENT = rb"(?:" + JSON_OBJECT + rb"|" + JSON_ARRAY + rb"|" + JSON_SCALAR + rb")"
UNIQUE_OBJECT_KEYS = rb"(?![\x00-\xff]*\"(?P<accepted_key>" + JSON_STRING_CONTENT + rb")\"\s*:[\x00-\xff]*\"(?P=accepted_key)\"\s*:)"
DUPLICATE_OBJECT_KEY = rb"(?=[\x00-\xff]*\"(?P<duplicate_key>" + JSON_STRING_CONTENT + rb")\"\s*:[\x00-\xff]*\"(?P=duplicate_key)\"\s*:)"
CLASSIFIER = REGEX.compile(rb"(?P<accepted>" + UNIQUE_OBJECT_KEYS + JSON_DOCUMENT + rb")|" + DUPLICATE_OBJECT_KEY + rb"(?:" + JSON_OBJECT + rb")(?P<rejected>)|(?P<decode_failure>[\x00-\xff]*[\x80-\xff][\x00-\xff]*)|(?P<parse_failure>[\x00-\x7f]*)")
FRAMES = {
    "accepted": Frame(Output(ByteVector(ACCEPTED)), Effect(ByteVector(APPLIED_EFFECT))),
    "decode_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(DECODE_FAILURE_EFFECT))),
    "parse_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(PARSE_FAILURE_EFFECT))),
    "rejected": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(REJECTED_EFFECT))),
}

def PROJECT(value: Input) -> Frame: return FRAMES[CLASSIFIER.fullmatch(value.value.payload).lastgroup]
