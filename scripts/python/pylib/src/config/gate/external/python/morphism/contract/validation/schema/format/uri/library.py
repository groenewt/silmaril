import re as REGEX

from config.constants.morphism.contract.validation.schema.format.uri.effect.applied.identity.value import VALUE as APPLIED_EFFECT
from config.constants.morphism.contract.validation.schema.format.uri.effect.decode.failure.identity.value import VALUE as DECODE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.schema.format.uri.effect.rejected.identity.value import VALUE as REJECTED_EFFECT
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.python.morphism.contract.validation.schema.format.uri.pattern.value import VALUE as URI
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.schema.format.uri.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.schema.format.uri.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.schema.format.uri.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.schema.format.uri.output.value import Value as Output

CLASSIFIER = REGEX.compile(rb"(?P<accepted>" + URI + rb")|(?P<decode_failure>[\x00-\xff]*[\x80-\xff][\x00-\xff]*)|(?P<rejected>[\x00-\x7f]*)")
FRAMES = {
    "accepted": Frame(Output(ByteVector(ACCEPTED)), Effect(ByteVector(APPLIED_EFFECT))),
    "decode_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(DECODE_FAILURE_EFFECT))),
    "rejected": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(REJECTED_EFFECT))),
}

def PROJECT(value: Input) -> Frame: return FRAMES[CLASSIFIER.fullmatch(value.value.payload).lastgroup]
