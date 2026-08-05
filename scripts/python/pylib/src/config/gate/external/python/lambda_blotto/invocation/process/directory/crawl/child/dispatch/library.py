from config.constants.lambda_blotto.invocation.process.directory.crawl.effect.applied.identity.value import VALUE as APPLIED
from config.gate.external.python.stdlib.hashlib.sha256.value import VALUE as SHA256
from config.gate.external.python.stdlib.os.path.join.value import VALUE as JOIN
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.dispatch.effect.value import Value as Effect
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.dispatch.frame.value import Value as Frame
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.dispatch.input.value import Value as Input
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.child.dispatch.output.value import Value as Output
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.directory.work.value import Value as DirectoryWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.none.value import Value as NoDispatch
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.provenance.map.drilldown.value import Value as DrilldownProvenance
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.request.value import Value as DirectoryRequest
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.provenance.value import Value as ArtifactProvenance
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.locator.value import Value as Locator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as FileRequest
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.entry.value import Value as FileAwaitingEntry
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Input) -> Frame:
    if value.hidden.decision.payload != b"include":
        return Frame(Output(NoDispatch(ByteVector(b"excluded-by-explicit-hidden-policy"))), Effect(ByteVector(APPLIED)))
    if value.classification.kind.payload == b"link":
        return Frame(Output(NoDispatch(ByteVector(b"symlink-recorded-never-followed"))), Effect(ByteVector(APPLIED)))
    parent = value.request.locator.value.payload.decode("utf-8", "surrogateescape")
    name = value.name.name.payload.decode("utf-8", "surrogateescape")
    locator = Locator(ByteVector(JOIN(parent, name).encode("utf-8", "surrogateescape")))
    inherited = value.request.artifact_provenance
    mapped = value.request.drilldown_provenance
    chain = ByteVector(FIELD(mapped.drilldown_chain).payload + FIELD(value.name.name).payload)
    artifact = ArtifactProvenance(inherited.source_root, inherited.root_key, inherited.mapping_identity, inherited.revision_reference, chain, inherited.source_diversity, inherited.publication_routing, inherited.evidence_class)
    drilldown = DrilldownProvenance(mapped.map_root, mapped.mapped_target, mapped.map_unit, mapped.map_revision, chain, mapped.evidence_class)
    ordinal = ByteVector(value.name.ordinal.value.to_bytes(16, "big", signed=False))
    attempt_material = FIELD(value.request.scan_identity).payload + FIELD(value.request.attempt).payload + FIELD(value.name.name).payload + FIELD(ordinal).payload
    attempt = ByteVector(SHA256(attempt_material).digest())
    evidence_class = inherited.evidence_class
    if value.classification.kind.payload == b"regular":
        request = FileRequest(locator, artifact, attempt, value.request.file_chunk_size, value.request.file_maximum_bytes, value.request.file_format_evidence)
        return Frame(Output(FileWork(FileAwaitingEntry(request), evidence_class)), Effect(ByteVector(APPLIED)))
    if value.classification.kind.payload == b"directory" and value.request.depth.value < value.request.maximum_depth.value:
        request = DirectoryRequest(locator, artifact, drilldown, value.request.scan_identity, attempt, value.request.maximum_entries, value.request.maximum_depth, Natural(value.request.depth.value + 1), value.request.hidden_policy, value.request.file_chunk_size, value.request.file_maximum_bytes, value.request.file_format_evidence)
        return Frame(Output(DirectoryWork(request, evidence_class)), Effect(ByteVector(APPLIED)))
    reason = b"depth-bound-reached" if value.classification.kind.payload == b"directory" else b"non-file-non-directory-recorded"
    return Frame(Output(NoDispatch(ByteVector(reason))), Effect(ByteVector(APPLIED)))
