from config.constants.lambda_blotto.invocation.process.directory.crawl.gap.directory.snapshot.value import VALUE as SNAPSHOT_GAP
from config.constants.lambda_blotto.invocation.process.directory.crawl.gap.listdir.whole.observation.value import VALUE as LISTDIR_GAP
from config.constants.lambda_blotto.invocation.process.directory.crawl.source.evidence.value import VALUE as SOURCE_EVIDENCE
from config.gate.external.python.stdlib.dataclasses.library import DEPENDENCY as DATACLASSES
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.provenance.map.drilldown.value import Value as DrilldownProvenance
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.provenance.value import Value as ArtifactProvenance
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.locator.value import Value as Locator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector

@DATACLASSES.dataclass(frozen=True, slots=True)
class Value:
    locator: Locator
    artifact_provenance: ArtifactProvenance
    drilldown_provenance: DrilldownProvenance
    scan_identity: ByteVector
    attempt: ByteVector
    maximum_entries: Natural
    maximum_depth: Natural
    depth: Natural
    hidden_policy: ByteVector
    file_chunk_size: Natural
    file_maximum_bytes: Natural
    file_format_evidence: ByteVector
    source_evidence = SOURCE_EVIDENCE
    listdir_gap = LISTDIR_GAP
    snapshot_gap = SNAPSHOT_GAP
