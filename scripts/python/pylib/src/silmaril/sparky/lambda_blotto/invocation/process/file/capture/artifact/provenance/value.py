from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.source.diversity.value import Value as SourceDiversity
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.value import Value as PublicationRouting

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    source_root: ByteVector
    root_key: ByteVector
    mapping_identity: ByteVector
    revision_reference: ByteVector
    drilldown_chain: ByteVector
    source_diversity: SourceDiversity
    publication_routing: PublicationRouting
    evidence_class: ByteVector
