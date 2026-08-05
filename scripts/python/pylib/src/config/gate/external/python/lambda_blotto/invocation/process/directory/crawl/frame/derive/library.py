from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.rejected.identity.value import VALUE as REJECTED
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.derive.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.derive.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.derive.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.derive.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.value import Value as DirectoryFrame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.issue.value import Value as Issue
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.serialize.project import PROJECT as SERIALIZE
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    metadata_stable = SERIALIZE(value.pre).payload == SERIALIZE(value.post).payload
    count_stable = value.accumulator.drift_identity.payload != b"drift" and value.accumulator.expected_total.value == value.end.observed_total.value
    provenance_stable = value.request.artifact_provenance.evidence_class.payload == value.request.drilldown_provenance.evidence_class.payload
    complete = value.end.bounded_identity.payload == b"unbounded" and value.accumulator.next_ordinal.value == value.end.observed_total.value
    if not (metadata_stable and count_stable and provenance_stable and complete):
        detail = b"directory-metadata-or-count-drift" if not metadata_stable or not count_stable else b"provenance-class-mismatch" if not provenance_stable else b"entry-bound-exceeded"
        return Frame(Output(Issue(ByteVector(b"unstable-directory-frame"), ByteVector(detail))), Effect(ByteVector(REJECTED)))
    result = DirectoryFrame(value.request, value.pre, value.post, value.accumulator, ByteVector(b"stable"), ByteVector(b"same-descriptor-pre-post-count-and-complete-bound"))
    return Frame(Output(result), Effect(ByteVector(APPLIED)))
