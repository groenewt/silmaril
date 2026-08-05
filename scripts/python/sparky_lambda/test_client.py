"""Artifact-boundary laws for Python invocation of registered Scala Lambda."""
#```python
#EXAMPLE OF OUR FUNCTIONAL RESTRICTION. LITERAL AND STRICT "ONE INPUT,One output"-> IF IT Cannot meet this criterion (this applies to any function anywhere where it receives ONE DEFINED TYPE PER iNPUT, THEN OUTPUT)< IF THIS CANNOT BE ACHIEVED WE CANNOT "CONSTRUCT A FRAME" AROUND OUR BYTE STREAM NOR CAN WE EVEN CLAIM "SUCCESS". PLEASE BE MINDFUL I HAVE FULL OVERVIEW OF THE CODEBASE AND ITS RATHER DISAPPOINT HOW MUCH LEXICAL, SEMANTIC AND TOPOLOGICAL RICHNESS WE LOSE BC THIS RULE IS NOT STRICTLY (and LIKE OUR CONFIG/{CONSTANTS,GATE *THERE ARE SO MANY JAVE VIOLATIONS!* } enforced. BAD RULE ENFORCE MENT IS WHAT GETS US KILLED
#T=Typevar('ANormalizedTypeUrn')
#X=Typevar('BNormalizedTypeUrn')
#Y=Typevar('CNormalizedTypeUrn')
#DEF somefunction(sometypekindbytestream:T)-> (someoutputsometypekindbytestream:X, someerroroutputsometypekindbytestream:Y):
#return SOMECALLABLE(sometypekindbytestream)
#T->(X,Y) IS A EXTREMELY STRICT HYGEINE RULE FOR IDK MAYBE 1) TO ACCOMPLISH MY FUCKING GOAL 2) TO FUCKING ENSURE PROPER SUBATOMIC MODELING 3) TO AVOID ANY AND ALL "BULLSHJT" bc like it has one parameter in, or it doesnt ;;;  It has only an effect (and implictly _error)( or it doesnt we are nto returning/workign with underfine sets. ARE URN TYPE DRIVE SWALLOWS ALL TO CREATE YONEDA POINTS (AGAIN SOMETHIGN YOU CAN SEARCH!)
#MORE AT /home/tristan/site_stage/cpg-highway/docs/campaigns/unary-byte-frame-law.md
#```

from __future__ import annotations

import unittest

from . import artifact, jvm
from .artifact import Request, Response
from .client import Client
from .contract import Contract
from .contract_gate.host.octet import (
    DecodingAccepted,
    EncodingEqual,
    EncodingUnequal,
    Projection,
    decode,
    equivalent,
    observe_encoding,
)
from .contract_gate.test_support import repository, responses, symbolic_link
from .kind import Provisional, PythonSemanticsAbsent, Registered, TimestampStale


class ClientSpecification(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repository = repository(__file__)
        cls.contract = Contract.discover(cls.repository)
        cls.projection = Projection.registered(cls.contract)

    def test_contract_names_scala_as_the_only_evaluation_authority(self) -> None:
        self.assertEqual(
            self.contract.implementation.evaluator,
            "semantic.Lambda.Evaluator.evaluate",
        )
        self.assertEqual(
            self.contract.laws.evaluation_authority,
            "canonical-scala-evaluator",
        )
        self.assertIsInstance(
            self.contract.laws.python_semantics,
            PythonSemanticsAbsent,
        )
        self.assertTrue(self.contract.laws.python_semantics.identity.startswith("urn:"))
        self.assertTrue(
            self.contract.laws.python_semantics.lineage_identity.startswith("urn:")
        )

    def test_readback_exposes_typed_artifacts_and_physical_lineage(self) -> None:
        readback = Client.readback(self.repository)

        self.assertIsInstance(readback.state, Registered)
        self.assertIsInstance(readback.request, Request)
        self.assertIsInstance(readback.response, Response)
        self.assertEqual(readback.request.framing_identity, readback.response.framing_identity)
        self.assertTrue(readback.request.locator.canonical.value.startswith("file://"))
        self.assertNotEqual(
            readback.request.locator.canonical.value,
            readback.request.locator.host_path.lexical,
        )
        self.assertGreater(readback.request_observation.pre.changed_ns, 0)
        self.assertGreater(readback.request_observation.pre.link_count, 0)
        self.assertEqual(
            readback.request_observation.pre.inode,
            readback.request_observation.opened_description_inode.inode,
        )

    def test_host_octet_projection_is_named_and_remains_provisional(self) -> None:
        readback = Client.readback(self.repository)
        request_encoding = observe_encoding(readback.request, self.projection)
        request_decoding = decode(readback.request, self.projection)
        response_decoding = decode(readback.response, self.projection)
        registration = self.contract.process_file

        self.assertEqual(self.projection.bit_width, 8)
        self.assertIsInstance(self.projection.state, Provisional)
        self.assertEqual(self.projection.schema_revision_state, self.projection.state)
        self.assertEqual(self.projection.provenance_state, self.projection.state)
        self.assertEqual(self.projection.runtime_shoe, registration.runtime_shoe)
        self.assertIn(self.projection.gap_identity, registration.gap_identities)
        self.assertGreater(request_encoding.host_octet_count, 0)
        self.assertGreater(response_decoding.host_octet_count, 0)
        self.assertIsInstance(request_decoding, DecodingAccepted)
        self.assertIsInstance(response_decoding, DecodingAccepted)
        self.assertEqual(request_encoding.digest, self.projection.digest)
        self.assertNotEqual(
            self.projection.digest.algorithm_identity,
            self.projection.digest.host_spelling,
        )

    def test_descriptor_open_description_inode_edges_remain_distinct(self) -> None:
        readback = Client.readback(self.repository)
        observation = observe_encoding(readback.request, self.projection).observation
        capture = self.contract.contract_gate.capture

        self.assertEqual(
            observation.descriptor_opened_description.relation_identity,
            capture.descriptor_opened_description_relation_identity,
        )
        self.assertEqual(
            observation.opened_description_inode.relation_identity,
            capture.opened_description_inode_relation_identity,
        )
        self.assertEqual(
            observation.descriptor_opened_description.descriptor,
            observation.descriptor,
        )
        self.assertEqual(
            observation.opened_description_inode.inode,
            observation.pre.inode,
        )
        self.assertEqual(observation.opened_description.offset_pre, 0)
        self.assertEqual(
            observation.opened_description.offset_post,
            observation.host_octet_count,
        )
        self.assertIsInstance(
            observation.opened_description.context.evidence_state,
            Provisional,
        )
        self.assertEqual(
            observation.opened_description.identity_evidence.gap_identity,
            capture.opened_description_kernel_identity_gap_identity,
        )
        self.assertNotEqual(
            observation.descriptor.capture_attempt,
            readback.request_observation.descriptor.capture_attempt,
        )

    def test_final_symbolic_link_is_not_collapsed_into_its_target(self) -> None:
        readback = Client.readback(self.repository)
        with symbolic_link(self.repository, readback.response.locator) as link:
            linked = artifact.response(self.contract, link)
            self.assertEqual(linked.locator.canonical, link.canonical)
            with self.assertRaises(OSError):
                observe_encoding(linked, self.projection)

    def test_mcp_is_a_typed_provisional_registration_not_a_python_handler(self) -> None:
        observed = Client.mcp(self.repository)
        registered = self.contract.mcp_tool

        self.assertEqual(observed.capability, registered.capability)
        self.assertEqual(observed.state, registered.state)
        self.assertIsInstance(observed.state, Provisional)
        self.assertEqual(observed.tool, registered.tool)
        self.assertEqual(observed.argument_field, registered.argument_field)

    def test_jvm_shoe_is_derived_from_registered_bsp_and_sbt_evidence(self) -> None:
        process = jvm.discover(self.repository, self.contract)
        self.assertIsInstance(process, jvm.Process)
        assert isinstance(process, jvm.Process)
        registration = self.contract.process_file

        self.assertEqual(process.capability, registration.capability)
        self.assertEqual(process.runtime_shoe, registration.runtime_shoe)
        self.assertEqual(process.main_class, self.contract.implementation.main_class)
        self.assertTrue(process.bsp_registrations)
        self.assertTrue(process.sources)
        self.assertTrue(process.dependencies)
        self.assertEqual(process.evidence.state, registration.operation_state)
        self.assertEqual(process.evidence.gap_identities, registration.gap_identities)
        self.assertEqual(process.evidence.bsp.digest, self.projection.digest)
        self.assertTrue(
            any(
                isinstance(dependency.state, TimestampStale)
                for dependency in process.evidence.owned_dependencies
            )
        )
        directory_revisions = tuple(
            revision
            for dependency in process.evidence.owned_dependencies
            for revision in (dependency.source, dependency.product)
            if revision.directories
        )
        self.assertTrue(directory_revisions)
        self.assertTrue(
            all(
                any(
                    gap.identity
                    == self.contract.contract_gate.capture.non_atomic_snapshot_gap_identity
                    for gap in revision.gaps
                )
                for revision in directory_revisions
            )
        )

    def test_python_launches_registered_scala_with_exact_artifact_locators(self) -> None:
        readback = Client.readback(self.repository)
        expected = decode(readback.response, self.projection)
        process = Client.jvm(self.repository)

        with responses(self.repository, "sparky-lambda-") as locators:
            first_response = process.response(locators.first)
            second_response = process.response(locators.second)
            first_execution = process.invoke(readback.request, first_response)
            second_execution = process.invoke(readback.request, second_response)
            first = decode(first_response, self.projection)
            second = decode(second_response, self.projection)
            repeated = equivalent(first_response, second_response, self.projection)
            fixture = equivalent(first_response, readback.response, self.projection)

        self.assertEqual(first_execution.exit_code, 0)
        self.assertEqual(second_execution.exit_code, 0)
        self.assertIsInstance(first, DecodingAccepted)
        self.assertIsInstance(second, DecodingAccepted)
        self.assertIsInstance(expected, DecodingAccepted)
        self.assertIsInstance(repeated, EncodingEqual)
        self.assertIsInstance(fixture, EncodingUnequal)
        self.assertEqual(first.payload_digest, second.payload_digest)
        self.assertNotEqual(first.payload_digest, expected.payload_digest)
        self.assertEqual(first.host_octet_count, second.host_octet_count)
        self.assertNotEqual(first.host_octet_count, expected.host_octet_count)
        self.assertEqual(first_execution.evidence, second_execution.evidence)


if __name__ == "__main__":
    unittest.main()
