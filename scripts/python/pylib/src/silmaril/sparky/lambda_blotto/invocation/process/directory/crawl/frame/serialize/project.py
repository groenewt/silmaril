from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.frame.value import Value as DirectoryFrame
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.metadata.observation.serialize.project import PROJECT as METADATA
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.serialize.project import PROJECT as ROUTING
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: DirectoryFrame) -> ByteVector:
    request = value.request
    provenance = request.artifact_provenance
    drilldown = request.drilldown_provenance
    diversity = provenance.source_diversity
    routing = provenance.publication_routing
    depth = ByteVector(request.depth.value.to_bytes(16, "big", signed=False))
    observed = ByteVector(value.accumulator.frontier.observed_children.value.to_bytes(16, "big", signed=False))
    fields = (ByteVector(b"lambda-blotto-directory-frame-v3"), request.scan_identity, request.attempt, request.locator.value, provenance.source_root, provenance.root_key, provenance.mapping_identity, provenance.revision_reference, provenance.drilldown_chain, diversity.source_kind, diversity.source_family, diversity.source_identity, ROUTING(routing), provenance.evidence_class, drilldown.map_root, drilldown.mapped_target, drilldown.map_unit, drilldown.map_revision, drilldown.drilldown_chain, drilldown.evidence_class, depth, request.hidden_policy, METADATA(value.pre), METADATA(value.post), observed, value.accumulator.serialized_children, value.stability, value.evidence)
    return ByteVector(b"".join(FIELD(field).payload for field in fields))
