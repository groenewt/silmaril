import re as REGEX

from config.constants.morphism.contract.validation.mechanic.artifact.kind.effect.applied.identity.value import VALUE as APPLIED_EFFECT
from config.constants.morphism.contract.validation.mechanic.artifact.kind.effect.decode.failure.identity.value import VALUE as DECODE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.artifact.kind.effect.parse.failure.identity.value import VALUE as PARSE_FAILURE_EFFECT
from config.constants.morphism.contract.validation.mechanic.artifact.kind.effect.rejected.identity.value import VALUE as REJECTED_EFFECT
from config.constants.morphism.contract.validation.truth.accepted.value import VALUE as ACCEPTED
from config.constants.morphism.contract.validation.truth.rejected.value import VALUE as REJECTED
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.effect.value import Value as Effect
from silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.frame.value import Value as Frame
from silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.input.value import Value as Input
from silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.output.value import Value as Output

SEPARATOR = b"\x00"
NONEMPTY_FIELD = rb"[^\x00]+"
FIELD = rb"[^\x00]*"
KNOWN_KIND = rb"(?:code-property-language-topology|scene|lexicon|validation-profile|lambda-runtime-constants|lambda-runtime-gateway|source-continuation)"
KNOWN_REGISTRATION = rb"(?:true|false)\x00" + KNOWN_KIND + rb"\x00" + NONEMPTY_FIELD + rb"\x00" + NONEMPTY_FIELD + rb"\x00" + FIELD + rb"\x00" + FIELD + rb"\x00" + FIELD + rb"\x00" + FIELD + rb"\x00" + FIELD
OPEN_PROVISIONAL_REGISTRATION = rb"false\x00" + NONEMPTY_FIELD + rb"\x00" + NONEMPTY_FIELD + rb"\x00" + NONEMPTY_FIELD + rb"\x00(?P<registration_schema>[^\x00]+)\x00provisional\x00" + NONEMPTY_FIELD + rb"\x00(?P=registration_schema)\x00(?P=registration_schema)"
CLASSIFIER = REGEX.compile(rb"(?:" + KNOWN_REGISTRATION + rb"|" + OPEN_PROVISIONAL_REGISTRATION + rb")(?P<accepted>)|(?P<decode_failure>[\x00-\xff]*[\x80-\xff][\x00-\xff]*)|(?P<parse_failure>(?!(?:true|false)\x00)[\x00-\x7f]*)|(?P<rejected>[\x00-\x7f]*)")
FRAMES = {
    "accepted": Frame(Output(ByteVector(ACCEPTED)), Effect(ByteVector(APPLIED_EFFECT))),
    "decode_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(DECODE_FAILURE_EFFECT))),
    "parse_failure": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(PARSE_FAILURE_EFFECT))),
    "rejected": Frame(Output(ByteVector(REJECTED)), Effect(ByteVector(REJECTED_EFFECT))),
}

def PROJECT(value: Input) -> Frame: return FRAMES[CLASSIFIER.fullmatch(value.closed_enumeration.payload + SEPARATOR + value.registration_kind.payload + SEPARATOR + value.registration_identity.payload + SEPARATOR + value.registration_path.payload + SEPARATOR + value.registration_schema.payload + SEPARATOR + value.registration_status.payload + SEPARATOR + value.registration_source_evidence.payload + SEPARATOR + value.document_schema.payload + SEPARATOR + value.schema_document_schema.payload).lastgroup]
