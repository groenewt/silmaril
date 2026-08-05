from config.constants.lambda_blotto.invocation.process.file.capture.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.file.capture.effect.rejected.identity.value import VALUE as REJECTED
from config.constants.lambda_blotto.invocation.process.file.capture.evidence.classification.observed.identity.value import VALUE as OBSERVED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.serialize.project import PROJECT as SERIALIZE
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.serialize.project import PROJECT as ROUTING
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.seal.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.seal.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.seal.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.seal.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.receipt.value import Value as Receipt
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    if value.request.provenance.evidence_class.payload != OBSERVED:
        issue = Issue(ByteVector(b"non-observed-seal-rejected"), value.request.provenance.evidence_class)
        return Frame(Output(issue), Effect(ByteVector(REJECTED)))
    diversity = value.request.provenance.source_diversity
    routing = value.request.provenance.publication_routing
    fields = (ByteVector(b"lambda-blotto-file-capture-receipt-v3"), value.request.attempt, value.request.locator.value, value.request.provenance.source_root, value.request.provenance.root_key, value.request.provenance.mapping_identity, value.request.provenance.revision_reference, value.request.provenance.drilldown_chain, diversity.source_kind, diversity.source_family, diversity.source_identity, ROUTING(routing), value.request.provenance.evidence_class, value.request.format_evidence, SERIALIZE(value.entry), SERIALIZE(value.pre), SERIALIZE(value.post), value.stability.verdict, value.stability.evidence, value.revision.algorithm, value.revision.digest)
    serialized = ByteVector(b"".join(FIELD(field).payload for field in fields))
    receipt = Receipt(serialized, ByteVector(SHA256(serialized.payload).digest()), value.revision, value.request.attempt, value.request.provenance)
    return Frame(Output(receipt), Effect(ByteVector(APPLIED)))
