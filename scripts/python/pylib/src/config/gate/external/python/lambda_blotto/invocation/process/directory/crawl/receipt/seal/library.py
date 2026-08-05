from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from config.constants.lambda_blotto.invocation.process.file.capture.evidence.classification.observed.identity.value import VALUE as OBSERVED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.serialize.project import PROJECT as SERIALIZE
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.seal.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.seal.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.seal.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.seal.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.receipt.value import Value as Receipt
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    request = value.frame.request
    if request.artifact_provenance.evidence_class.payload != OBSERVED or request.drilldown_provenance.evidence_class.payload != OBSERVED:
        issue = Issue(ByteVector(b"non-observed-directory-seal-rejected"), request.artifact_provenance.evidence_class)
        return Frame(Output(issue), Effect(ByteVector(REJECTED)))
    serialized = SERIALIZE(value.frame)
    receipt = Receipt(serialized, ByteVector(SHA256(serialized.payload + value.revision.digest.payload).digest()), value.revision, request.artifact_provenance, request.drilldown_provenance, request.attempt)
    return Frame(Output(receipt), Effect(ByteVector(APPLIED)))
