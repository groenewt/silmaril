import re as REGEX

from config.constants.morphism.contract.validation.mechanic.digest.support.effect.applied.identity.value import VALUE as APPLIED_EFFECT
from config.constants.morphism.contract.validation.mechanic.digest.support.effect.decode.failure.identity.value import VALUE as DECODE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.digest.support.effect.parse.failure.identity.value import VALUE as PARSE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.digest.support.effect.rejected.identity.value import VALUE as REJECTED_EFFECT
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.mechanic.digest.support.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mechanic.digest.support.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.digest.support.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.mechanic.digest.support.output.value import Value as Output

SEPARATOR = b"\x00"
CLASSIFIER = REGEX.compile(rb"(?P<accepted>(?:algorithm\x00sha256|encoding\x00utf-8))|(?P<decode_failure>[\x00-\xff]*[\x80-\xff][\x00-\xff]*)|(?P<parse_failure>(?!(?:algorithm|encoding)\x00)[\x00-\x7f]*)|(?P<rejected>[\x00-\x7f]*)")
FRAMES = {
    "accepted": Frame(Output(ByteVector(ACCEPTED)), Effect(ByteVector(APPLIED_EFFECT))),
    "decode_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(DECODE_FAILURE_EFFECT))),
    "parse_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(PARSE_FAILURE_EFFECT))),
    "rejected": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(REJECTED_EFFECT))),
}

def PROJECT(value: Input) -> Frame: return FRAMES[CLASSIFIER.fullmatch(value.coordinate.payload + SEPARATOR + value.value.payload).lastgroup]
