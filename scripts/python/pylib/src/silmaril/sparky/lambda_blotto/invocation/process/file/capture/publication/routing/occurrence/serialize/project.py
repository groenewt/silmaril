from silmaril.sparky.lambda_blotto.invocation.process.file.capture.encoding.field.project import PROJECT as FIELD
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.occurrence.value import Value as Occurrence
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

def PROJECT(value: Occurrence) -> ByteVector:
    fields = (ByteVector(b"lambda-blotto-corpus-route-occurrence-v3"), value.occurrence_key, value.source_kind, value.authority_role, value.route_relation, value.exact_text, value.source_path, value.source_locus, value.source_revision, value.frame_time, value.authority_scope, value.resolution_status, value.non_exclusivity, value.evidence_class, value.claim_classification, value.support_boundary, value.target_volume_route, value.target_chapter_route, value.target_subsection_route, value.semantic_drilldown_route, value.diagram_route, value.citation_key, value.publication_header, value.publication_footer, value.readback_artifact)
    return ByteVector(b"".join(FIELD(field).payload for field in fields))
