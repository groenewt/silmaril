from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.provenance.map.drilldown.value import Value as DrilldownProvenance
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.revision.value import Value as Revision
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.provenance.value import Value as ArtifactProvenance
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    serialized: ByteVector
    digest: ByteVector
    revision: Revision
    artifact_provenance: ArtifactProvenance
    drilldown_provenance: DrilldownProvenance
    attempt: ByteVector
