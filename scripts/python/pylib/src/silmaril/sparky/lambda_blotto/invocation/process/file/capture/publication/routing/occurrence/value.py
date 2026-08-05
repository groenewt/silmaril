from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    occurrence_key: ByteVector
    source_kind: ByteVector
    authority_role: ByteVector
    route_relation: ByteVector
    exact_text: ByteVector
    source_path: ByteVector
    source_locus: ByteVector
    source_revision: ByteVector
    frame_time: ByteVector
    authority_scope: ByteVector
    resolution_status: ByteVector
    non_exclusivity: ByteVector
    evidence_class: ByteVector
    claim_classification: ByteVector
    support_boundary: ByteVector
    target_volume_route: ByteVector
    target_chapter_route: ByteVector
    target_subsection_route: ByteVector
    semantic_drilldown_route: ByteVector
    diagram_route: ByteVector
    citation_key: ByteVector
    publication_header: ByteVector
    publication_footer: ByteVector
    readback_artifact: ByteVector
