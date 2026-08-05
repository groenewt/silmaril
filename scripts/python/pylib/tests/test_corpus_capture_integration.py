import hashlib
import json
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE_SRC = Path("/data/src/scripts/pylib/src")
sys.path.insert(0, str(ROOT / "src"))
if LIVE_SRC.is_dir():
    sys.path.append(str(LIVE_SRC))

from config.constants.lambda_blotto.invocation.process.file.capture.evidence.classification.admitted.identity.value import VALUE as ADMITTED
from config.constants.lambda_blotto.invocation.process.file.capture.evidence.classification.counterfactual.identity.value import VALUE as COUNTERFACTUAL
from config.constants.lambda_blotto.invocation.process.file.capture.evidence.classification.observed.identity.value import VALUE as OBSERVED
from config.constants.lambda_blotto.invocation.process.file.capture.evidence.classification.predicted.identity.value import VALUE as PREDICTED
from config.gate.external.project.sparky.substrate.byte.vector.library import DEPENDENCY as ByteVector
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.file.work.value import Value as FileWork
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.dispatch.none.value import Value as NoDispatch
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.provenance.map.drilldown.value import Value as DrilldownProvenance
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.request.value import Value as DirectoryRequest
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.apply import apply as DIRECTORY_STEP
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.scheduler.transition.input.value import Value as DirectoryStepInput
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.awaiting.open.value import Value as DirectoryAwaitingOpen
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.complete.value import Value as DirectoryComplete
from silmaril.sparky.lambda_blotto.invocation.process.directory.crawl.state.failed.value import Value as DirectoryFailed
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.provenance.value import Value as ArtifactProvenance
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.artifact.source.diversity.value import Value as SourceDiversity
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.locator.value import Value as Locator
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.natural.value import Value as Natural
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.value import Value as PublicationRouting
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.publication.routing.occurrence.value import Value as RouteOccurrence
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.request.value import Value as FileRequest
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.apply import apply as FILE_STEP
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.scheduler.transition.input.value import Value as FileStepInput
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.awaiting.entry.value import Value as FileAwaitingEntry
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.complete.value import Value as FileComplete
from silmaril.sparky.lambda_blotto.invocation.process.file.capture.state.failed.value import Value as FileFailed


def vector(value: str | bytes) -> ByteVector:
    return ByteVector(value if isinstance(value, bytes) else value.encode("utf-8"))


def canonical_occurrences() -> tuple[RouteOccurrence, ...]:
    manifests = tuple(
        json.loads((ROOT / name).read_text())
        for name in ("phoenix-disintegration-routing.json", "federated-computing-substrate-routing.json")
    )
    def projected_occurrence(manifest, occurrence):
        coordinates = tuple(
            coordinate
            for coordinate in manifest["publication_coordinates"]
            if occurrence["occurrence_key"] in coordinate["applies_to_occurrence_keys"]
        )
        if len(coordinates) != 1:
            raise AssertionError(f"expected one publication coordinate for {occurrence['occurrence_key']}")
        coordinate = coordinates[0]
        return RouteOccurrence(
            vector(occurrence["occurrence_key"]),
            vector(occurrence["source_kind"]),
            vector(occurrence["authority_role"]),
            vector(occurrence["route_relation"]),
            vector(occurrence["exact_text"]),
            vector(occurrence["source_path"]),
            vector(occurrence["source_locus"]),
            vector(occurrence["source_revision"]),
            vector(occurrence.get("frame_time", "frame-time-not-recorded")),
            vector(occurrence.get("authority_scope", occurrence["authority_role"])),
            vector(occurrence.get("resolution_status", "resolved")),
            vector(occurrence.get("non_exclusivity", "one occurrence in an open corpus")),
            vector(occurrence["evidence_class"]),
            vector(occurrence["claim_classification"]),
            vector(occurrence["support_boundary"]),
            vector(occurrence["target_volume_route"]),
            vector(occurrence["target_chapter_route"]),
            vector(coordinate["subsection_route"]),
            vector(coordinate["semantic_drilldown_route"]),
            vector(coordinate["diagram_route"]),
            vector(coordinate["citation_key"]),
            vector(coordinate["header_artifact"]),
            vector(coordinate["footer_artifact"]),
            vector(coordinate["readback_artifact"]),
        )
    return tuple(
        projected_occurrence(manifest, occurrence)
        for manifest in manifests
        for occurrence in manifest["occurrences"]
    )


def provenance(root: Path, evidence_class: bytes) -> ArtifactProvenance:
    diversity = SourceDiversity(vector("capture-map"), vector("lambda-blotto-architecture"), vector("source-identity-001"))
    routing = PublicationRouting(vector("claim-001"), vector("volume-07"), vector("chapter-03"), vector("appendix-a"), canonical_occurrences())
    return ArtifactProvenance(vector(str(root)), vector("capture-root"), vector("map-identity"), vector("revision-001"), vector(".maps/root -> anchor -> source"), diversity, routing, ByteVector(evidence_class))


def file_request(path: Path, evidence_class: bytes) -> FileRequest:
    return FileRequest(Locator(vector(str(path))), provenance(path.parent, evidence_class), vector("file-attempt-001"), Natural(4), Natural(4096), vector("text/plain; explicit"))


def run_file(request: FileRequest, maximum_steps: int = 128):
    state = FileAwaitingEntry(request)
    evidence_class = request.provenance.evidence_class
    frames = []
    for _ in range(maximum_steps):
        frame = FILE_STEP(FileStepInput(state, evidence_class))
        frames.append(frame)
        state = frame.output.state
        if isinstance(state, (FileComplete, FileFailed)):
            return state, tuple(frames)
    raise AssertionError("file scheduler did not terminate inside explicit test bound")


def directory_request(path: Path, evidence_class: bytes, maximum_entries: int = 32) -> DirectoryRequest:
    artifact = provenance(path, evidence_class)
    drilldown = DrilldownProvenance(vector(str(path)), vector("mapped-target"), vector("map-unit"), vector("map-revision"), vector(".maps/root -> anchor"), ByteVector(evidence_class))
    return DirectoryRequest(Locator(vector(str(path))), artifact, drilldown, vector("scan-001"), vector("directory-attempt-001"), Natural(maximum_entries), Natural(4), Natural(0), vector("include-all"), Natural(4), Natural(4096), vector("text/plain; explicit"))


def run_directory(request: DirectoryRequest, maximum_steps: int = 256):
    state = DirectoryAwaitingOpen(request)
    frames = []
    for ordinal in range(maximum_steps):
        transition = vector(f"transition-{ordinal:04d}")
        frame = DIRECTORY_STEP(DirectoryStepInput(state, request.artifact_provenance.evidence_class, transition, request.scan_identity, request.attempt))
        frames.append(frame)
        state = frame.output.state
        if isinstance(state, (DirectoryComplete, DirectoryFailed)):
            return state, tuple(frames)
    raise AssertionError("directory scheduler did not terminate inside explicit test bound")


class CorpusCaptureIntegrationTest(unittest.TestCase):
    def test_file_capture_seals_same_descriptor_sha_and_publication_route(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "artifact.txt"
            path.write_bytes(b"lambda-blotto-corpus")
            request = file_request(path, OBSERVED)
            state, frames = run_file(request)
            self.assertIsInstance(state, FileComplete)
            self.assertTrue(all(frame.effect.evidence_class.payload == OBSERVED for frame in frames))
            self.assertEqual(state.receipt.digest.payload, hashlib.sha256(state.receipt.serialized.payload).digest())
            self.assertEqual(state.readback.verdict.payload, b"accepted")
            self.assertIn(b"chapter-03", state.receipt.serialized.payload)
            self.assertIn(b".maps/root -> anchor -> source", state.receipt.serialized.payload)
            self.assertIn(b"In the corpus, disintegration/reassimilation is the mythic Phoenix run.  This", state.receipt.serialized.payload)
            self.assertIn(b"declared-synthesis", state.receipt.serialized.payload)
            self.assertIn(b"OUR ecosystem", state.receipt.serialized.payload)
            self.assertIn(b"Icarus is the platform and carries Daedalus", state.receipt.serialized.payload)
            self.assertIn(b"full sauce in HELIOS later", state.receipt.serialized.payload)
            self.assertIn(b"12th Gen Intel(R) Core(TM) i9-12900K", state.receipt.serialized.payload)
            self.assertIn(b"RISC-V Instruction Set Manual, Volume I", state.receipt.serialized.payload)
            self.assertIn(b"language and compiler centered around the concept of tile", state.receipt.serialized.payload)
            self.assertIn(b"required-unresolved", state.receipt.serialized.payload)
            self.assertIn(b"whole heterogeneous computing field as open-ended federation", state.receipt.serialized.payload)
            self.assertIn(b"fig:30-phoenix-progressive-run", state.receipt.serialized.payload)
            self.assertIn(b"fig:34-uefi-isa-progressive-boundary", state.receipt.serialized.payload)
            self.assertIn(b"rendered-page footer artifact", state.receipt.serialized.payload)
            self.assertIn(b"citation-resolution readback", state.receipt.serialized.payload)
            with self.assertRaises(FrozenInstanceError):
                request.provenance.source_root = vector("mutated")

    def test_fib_and_admitted_file_frames_never_become_observed(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "predicted.txt"
            path.write_bytes(b"counterfactual-input")
            for evidence_class in (PREDICTED, COUNTERFACTUAL, ADMITTED):
                with self.subTest(evidence_class=evidence_class):
                    state, frames = run_file(file_request(path, evidence_class))
                    self.assertIsInstance(state, FileFailed)
                    self.assertEqual(state.issue.code.payload, b"non-observed-seal-rejected")
                    self.assertTrue(all(frame.effect.evidence_class.payload == evidence_class for frame in frames))

    def test_hidden_entries_are_included_and_symlinks_are_never_followed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "visible.txt").write_bytes(b"visible")
            (root / ".hidden-map").write_bytes(b"hidden")
            (root / "target").mkdir()
            (root / "target" / "inside.txt").write_bytes(b"inside")
            (root / "link-to-directory").symlink_to(root / "target", target_is_directory=True)
            request = directory_request(root, OBSERVED)
            state, frames = run_directory(request)
            self.assertIsInstance(state, DirectoryComplete)
            self.assertTrue(all(frame.effect.evidence_class.payload == OBSERVED for frame in frames))
            for frame in frames:
                receipt = frame.output.receipt
                self.assertEqual(receipt.scan_identity.payload, request.scan_identity.payload)
                self.assertEqual(receipt.attempt.payload, request.attempt.payload)
                self.assertEqual(receipt.digest.payload, hashlib.sha256(receipt.serialized.payload).digest())
            children = {child.name.name.payload: child for child in state.frame.accumulator.children}
            self.assertEqual(children[b".hidden-map"].hidden.decision.payload, b"include")
            self.assertIsInstance(children[b".hidden-map"].dispatch, FileWork)
            self.assertEqual(children[b"link-to-directory"].classification.kind.payload, b"link")
            self.assertIsInstance(children[b"link-to-directory"].dispatch, NoDispatch)
            self.assertEqual(children[b"link-to-directory"].dispatch.reason.payload, b"symlink-recorded-never-followed")
            self.assertIn(b"chapter-03", state.receipt.serialized.payload)
            self.assertIn(b"molt IS the phoenix mechanic", state.receipt.serialized.payload)
            self.assertIn(b"implementation-witness", state.receipt.serialized.payload)
            self.assertEqual(state.readback.verdict.payload, b"accepted")

    def test_entry_bound_fails_closed_instead_of_sealing_partial_observation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "a").write_bytes(b"a")
            (root / "b").write_bytes(b"b")
            state, _ = run_directory(directory_request(root, OBSERVED, maximum_entries=1))
            self.assertIsInstance(state, DirectoryFailed)
            self.assertEqual(state.issue.code.payload, b"unstable-directory-frame")
            self.assertEqual(state.issue.detail.payload, b"entry-bound-exceeded")


if __name__ == "__main__":
    unittest.main()
