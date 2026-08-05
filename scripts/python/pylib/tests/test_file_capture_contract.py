import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from silmaril.sparky.contract.file_capture_static.check import check

class FileCaptureContractTest(unittest.TestCase):
    def test_static_contract_is_complete(self):
        self.assertEqual(check(ROOT), ())

    def test_manifest_preserves_provisional_gaps(self):
        manifest = json.loads((ROOT / "file-capture-manifest.json").read_text())
        gaps = " ".join(manifest["provisional_gaps"])
        self.assertIn("linearity", gaps)
        self.assertIn("no admitted Python interpreter entrance", gaps)
        self.assertIn("whole-payload bounded", gaps)
        self.assertIn("emission", gaps)

    def test_scope_includes_bounded_hidden_aware_directory_traversal(self):
        manifest = json.loads((ROOT / "file-capture-manifest.json").read_text())
        self.assertNotIn("directory traversal", manifest["excluded"])
        self.assertIn("scheduler/transition", manifest["directory_operations"])
        self.assertEqual(manifest["directory_contract"]["hidden_policy"].split()[0], "include-all")

    def test_integrated_semantics_is_explicit(self):
        manifest = json.loads((ROOT / "file-capture-manifest.json").read_text())
        self.assertIn("Lambda Blotto is discrete Colonel Blotto", manifest["semantics"])
        self.assertIn("Delta is its operational semantics", manifest["semantics"])
        self.assertIn("spectral coordinates", manifest["lambda_role"])
        self.assertIn("lambda-calculus motion", manifest["lambda_role"])

    def test_provenance_and_evidence_classes_are_non_interchangeable(self):
        manifest = json.loads((ROOT / "file-capture-manifest.json").read_text())
        self.assertIn("source-root", manifest["provenance_contract"])
        seal = (ROOT / "src/config/gate/external/python/lambda_blotto/invocation/process/file/capture/receipt/seal/library.py").read_text()
        self.assertIn("non-observed-seal-rejected", seal)
        self.assertIn("provenance.evidence_class", seal)
        provenance = (ROOT / "src/silmaril/sparky/lambda_blotto/invocation/process/file/capture/artifact/provenance/value.py").read_text()
        self.assertIn("drilldown_chain", provenance)
        self.assertIn("source_diversity", provenance)
        self.assertIn("publication_routing", provenance)

    def test_phoenix_disintegration_routing_is_exact_and_noncollapsed(self):
        routing = json.loads((ROOT / "phoenix-disintegration-routing.json").read_text())
        self.assertEqual(routing["canonical_topology"], "OUR ecosystem -> PHOENIX RUN [contains Molt D/R] -> Icarus -> Helios/GraphAtlas")
        self.assertEqual(routing["mechanism"], "Molt is the disintegration/reassimilation mechanism inside PHOENIX RUN.")
        self.assertIn("getting-to-the-sun vehicle", routing["icarus_role"])
        self.assertIn("Helios/GraphAtlas is the mise-en-scene", routing["mise_en_scene"])
        occurrences = {occurrence["occurrence_key"]: occurrence for occurrence in routing["occurrences"]}
        self.assertEqual(occurrences["volume-30-mythic-phoenix-claim"]["claim_classification"], "declared-synthesis")
        self.assertEqual(occurrences["operator-ledger-phoenix-icarus-helios"]["claim_classification"], "direct-source")
        self.assertEqual(occurrences["molt-is-phoenix-mechanic-map"]["claim_classification"], "capture-map")
        self.assertIn("not implementation authority", occurrences["molt-is-phoenix-mechanic-map"]["support_boundary"])
        self.assertTrue(all(occurrence["target_volume_route"] == "src/papers/30_disintegration_reassimilation" for occurrence in routing["occurrences"]))

    def test_computing_substrate_routing_is_federated_timed_and_open(self):
        routing = json.loads((ROOT / "federated-computing-substrate-routing.json").read_text())
        self.assertIn("open coproduct", routing["federation_law"])
        self.assertIn("not standards authority", routing["profile_boundary"])
        self.assertIn("discovery obligation/GAP", routing["gap_law"])
        occurrences = {occurrence["occurrence_key"]: occurrence for occurrence in routing["occurrences"]}
        required = {
            "local-host-frame-intel-12th-generation",
            "local-host-frame-amd-navi-44",
            "riscv-user-isa-v2-1-direct-artifact",
            "amd-hip-programming-guide-direct-artifact",
            "triton-mapl-2019-direct-artifact",
            "linux-kvm-direct-artifact",
            "gap-intel-generation-federation",
            "gap-amd-cpu-generation-federation",
            "gap-other-isa-system-frames",
            "gap-cuda-rocm-triton-other-stacks",
            "gap-uefi-firmware-federation",
            "gap-vm-hypervisor-federation",
            "gap-network-storage-operating-environment-federation",
            "gap-single-multi-machine-deployment-topologies",
            "gap-extensible-computing-backends",
        }
        self.assertTrue(required.issubset(occurrences))
        self.assertTrue(all(occurrence["frame_time"] for occurrence in occurrences.values()))
        self.assertTrue(all(occurrence["authority_scope"] for occurrence in occurrences.values()))
        self.assertTrue(all(occurrence["resolution_status"] for occurrence in occurrences.values()))
        self.assertTrue(all(occurrence["non_exclusivity"] for occurrence in occurrences.values()))
        gaps = tuple(occurrence for occurrence in occurrences.values() if occurrence["claim_classification"] == "discovery-obligation")
        self.assertTrue(gaps)
        self.assertTrue(all(occurrence["evidence_class"] == "Admitted" for occurrence in gaps))
        self.assertIn("one 12th-generation observation only", occurrences["gap-intel-generation-federation"]["support_boundary"])
        self.assertIn("not a closed backend enumeration", occurrences["gap-cuda-rocm-triton-other-stacks"]["non_exclusivity"])

    def test_publication_coordinates_are_total_navigable_and_readback_bound(self):
        for name in ("phoenix-disintegration-routing.json", "federated-computing-substrate-routing.json"):
            with self.subTest(manifest=name):
                routing = json.loads((ROOT / name).read_text())
                occurrence_keys = {occurrence["occurrence_key"] for occurrence in routing["occurrences"]}
                ownership = {}
                for coordinate in routing["publication_coordinates"]:
                    for key in coordinate["applies_to_occurrence_keys"]:
                        ownership.setdefault(key, []).append(coordinate["coordinate_key"])
                    self.assertTrue(coordinate["volume_route"])
                    self.assertTrue(coordinate["chapter_route"])
                    self.assertTrue(coordinate["subsection_route"])
                    self.assertTrue(coordinate["semantic_drilldown_route"])
                    self.assertTrue(coordinate["diagram_route"])
                    self.assertTrue(coordinate["citation_key"])
                    self.assertEqual(coordinate["source_locus_field"], "occurrence.source_locus")
                    self.assertIn("chapter line 1", coordinate["header_artifact"])
                    self.assertIn("footer artifact", coordinate["footer_artifact"])
                    self.assertIn("readback", coordinate["readback_artifact"])
                self.assertEqual(set(ownership), occurrence_keys)
                self.assertTrue(all(len(owners) == 1 for owners in ownership.values()))
        hardware = json.loads((ROOT / "federated-computing-substrate-routing.json").read_text())
        self.assertIn("superscript numeric citation", hardware["publication_validation_law"])
        diagrams = " ".join(coordinate["diagram_route"] for coordinate in hardware["publication_coordinates"])
        self.assertIn("fig:34-uefi-isa-progressive-boundary", diagrams)
        self.assertIn("no chapter-local diagram", diagrams)

    def test_same_descriptor_freshness_and_close_paths_are_explicit(self):
        external = ROOT / "src/config/gate/external/python/lambda_blotto/invocation/process/file/capture"
        pre = (external / "pre/observe/library.py").read_text()
        post = (external / "post/observe/library.py").read_text()
        scheduler = (external / "scheduler/transition/library.py").read_text()
        self.assertIn("FSTAT(value.opened.descriptor.number.value)", pre)
        self.assertIn("FSTAT(value.opened.descriptor.number.value)", post)
        self.assertIn("AwaitingFailureClose", scheduler)
        self.assertNotIn("while ", scheduler)
        self.assertNotIn("_ATTEMPT_SEQUENCE", scheduler)

    def test_receipt_is_length_framed_hashed_and_read_back(self):
        external = ROOT / "src/config/gate/external/python/lambda_blotto/invocation/process/file/capture"
        seal = (external / "receipt/seal/library.py").read_text()
        readback = (external / "receipt/readback/library.py").read_text()
        self.assertIn("FIELD(field)", seal)
        self.assertIn("SHA256(serialized.payload).digest()", seal)
        self.assertIn("SHA256(value.receipt.serialized.payload).digest()", readback)

    def test_progress_has_explicit_scale_coordinates_without_emission_claim(self):
        progress = (ROOT / "src/config/gate/external/python/lambda_blotto/invocation/process/file/capture/progress/seal/library.py").read_text()
        self.assertIn("value.scan_identity", progress)
        self.assertIn("value.completed", progress)
        self.assertIn("value.total", progress)
        self.assertIn("Plan", progress)
        self.assertNotIn("cheese_call", progress)

    def test_directory_progress_receipt_binds_scan_attempt_and_transition(self):
        scheduler = (ROOT / "src/config/gate/external/python/lambda_blotto/invocation/process/directory/crawl/scheduler/transition/library.py").read_text()
        receipt = (ROOT / "src/silmaril/sparky/lambda_blotto/invocation/process/directory/crawl/transition/receipt/value.py").read_text()
        self.assertIn("value.scan_identity", scheduler)
        self.assertIn("value.attempt", scheduler)
        self.assertIn("scan_identity: ByteVector", receipt)
        self.assertIn("attempt: ByteVector", receipt)

    def test_python_namespace_has_no_reserved_keyword_import(self):
        for path in (ROOT / "src").rglob("*.py"):
            compile(path.read_bytes(), str(path), "exec")
