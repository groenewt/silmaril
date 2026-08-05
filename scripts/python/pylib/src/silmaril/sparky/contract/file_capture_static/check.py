import json
from pathlib import Path

OPERATION_FILES = ("input/value.py", "output/value.py", "effect/value.py", "frame/value.py", "apply.py")
EXACT_GATES = (
    "config/gate/external/python/stdlib/os/stat/value.py",
    "config/gate/external/python/stdlib/os/fstat/value.py",
    "config/gate/external/python/stdlib/os/open/value.py",
    "config/gate/external/python/stdlib/os/read/value.py",
    "config/gate/external/python/stdlib/os/close/value.py",
    "config/gate/external/python/stdlib/os/lseek/value.py",
    "config/gate/external/python/stdlib/os/listdir/value.py",
    "config/gate/external/python/stdlib/fcntl/status/flags/value.py",
    "config/gate/external/python/stdlib/stat/classifiers/value.py",
    "config/gate/external/python/stdlib/hashlib/sha256/value.py",
)
FORBIDDEN_CAPTURE_TEXT = ("import os", "from os", "import hashlib", "from hashlib", "import fcntl", "from fcntl", "import stat", "from stat", "print(", "logging.", "_ATTEMPT_SEQUENCE", "uuid", "time.time")

def _check_operations(root, operations, operation_root, external_root, constant_root, failures):
    for operation in operations:
        for suffix in OPERATION_FILES:
            candidate = operation_root / operation / suffix
            if not candidate.is_file():
                failures.append(f"missing operation contract: {candidate.relative_to(root)}")
        project = external_root / operation / "library.py"
        identity = constant_root / operation / "request/operation/identity/value.py"
        if not project.is_file():
            failures.append(f"missing PROJECT leaf: {project.relative_to(root)}")
        if not identity.is_file():
            failures.append(f"missing operation identity: {identity.relative_to(root)}")
        for role in ("input", "output", "effect", "frame"):
            candidate = operation_root / operation / role / "value.py"
            if candidate.is_file():
                text = candidate.read_text()
                if "@DATACLASSES.dataclass(frozen=True, slots=True)" not in text:
                    failures.append(f"mutable or untyped role carrier: {candidate.relative_to(root)}")
                if role == "effect" and "evidence_class: ByteVector" not in text:
                    failures.append(f"frame evidence lineage is absent: {candidate.relative_to(root)}")
                if role == "effect" and "ByteVector(OBSERVED)" in text:
                    failures.append(f"operation effect defaults to observed evidence: {candidate.relative_to(root)}")
                if "schema_identity = SCHEMA_IDENTITY" not in text or "lineage_identity = LINEAGE_IDENTITY" not in text:
                    failures.append(f"schema or lineage identity is absent: {candidate.relative_to(root)}")
            for identity_kind in ("schema", "lineage"):
                identity = constant_root / operation / role / identity_kind / "identity/value.py"
                if not identity.is_file():
                    failures.append(f"missing role identity: {identity.relative_to(root)}")
        apply_path = operation_root / operation / "apply.py"
        if apply_path.is_file() and ("def apply(value: Input) -> Frame" not in apply_path.read_text() or "PROJECT(value)" not in apply_path.read_text()):
            failures.append(f"non-unary apply: {apply_path.relative_to(root)}")

def check(root: Path) -> tuple[str, ...]:
    failures = []
    manifest = json.loads((root / "file-capture-manifest.json").read_text())
    routing_manifests = tuple(
        json.loads((root / name).read_text())
        for name in ("phoenix-disintegration-routing.json", "federated-computing-substrate-routing.json")
    )
    source = root / manifest["root"]
    operation_root = source / "silmaril/sparky/lambda_blotto/invocation/process/file/capture"
    external_root = source / "config/gate/external/python/lambda_blotto/invocation/process/file/capture"
    constant_root = source / "config/constants/lambda_blotto/invocation/process/file/capture"
    directory_operation_root = source / "silmaril/sparky/lambda_blotto/invocation/process/directory/crawl"
    directory_external_root = source / "config/gate/external/python/lambda_blotto/invocation/process/directory/crawl"
    directory_constant_root = source / "config/constants/lambda_blotto/invocation/process/directory/crawl"
    _check_operations(root, manifest["operations"], operation_root, external_root, constant_root, failures)
    _check_operations(root, manifest["directory_operations"], directory_operation_root, directory_external_root, directory_constant_root, failures)
    for gate in EXACT_GATES:
        if not (source / gate).is_file():
            failures.append(f"missing exact external gate: {gate}")
    for candidate in tuple(operation_root.rglob("*.py")) + tuple(directory_operation_root.rglob("*.py")):
        text = candidate.read_text()
        for forbidden in FORBIDDEN_CAPTURE_TEXT:
            if forbidden in text:
                failures.append(f"forbidden capture dependency {forbidden!r}: {candidate.relative_to(root)}")
    for candidate in tuple(operation_root.glob("state/**/value.py")) + tuple(directory_operation_root.glob("state/**/value.py")):
        if candidate.name == "value.py" and candidate.parent.name != "state" and "@DATACLASSES.dataclass(frozen=True, slots=True)" not in candidate.read_text():
            failures.append(f"non-immutable algebraic state: {candidate.relative_to(root)}")
    collision = source / "silmaril/sparky/lambda_blotto/invocation/process/file/apply.py"
    if collision.exists():
        failures.append("staging overwrites existing process/file/apply.py collision path")
    scheduler = (external_root / "scheduler/transition/library.py").read_text()
    if "while " in scheduler or "for " in scheduler:
        failures.append("scheduler contains a loop instead of one transition")
    if "same-descriptor-pre-post-and-whole-payload" not in (external_root / "stability/decide/library.py").read_text():
        failures.append("same-descriptor stability evidence is absent")
    if "value.evidence_class" not in scheduler or "scheduler-evidence-class-mismatch" not in scheduler:
        failures.append("file scheduler does not preserve explicit evidence class")
    directory_scheduler = (directory_external_root / "scheduler/transition/library.py").read_text()
    if "while " in directory_scheduler or "for " in directory_scheduler:
        failures.append("directory scheduler contains a loop instead of one transition")
    if "value.scan_identity" not in directory_scheduler or "value.attempt" not in directory_scheduler:
        failures.append("directory progress receipt omits scan or attempt identity")
    if "scheduler-progress-identity-mismatch" not in directory_scheduler or "scheduler-evidence-class-mismatch" not in directory_scheduler:
        failures.append("directory scheduler does not check progress and evidence lineage")
    child_metadata = (directory_external_root / "child/metadata/observe/library.py").read_text()
    child_dispatch = (directory_external_root / "child/dispatch/library.py").read_text()
    hidden = (directory_external_root / "hidden/policy/decide/library.py").read_text()
    if "follow_symlinks=False" not in child_metadata or "symlink-recorded-never-followed" not in child_dispatch:
        failures.append("no-symlink-follow law is absent")
    if "include-all" not in hidden or "hidden-included-explicitly" not in hidden:
        failures.append("explicit hidden inclusion law is absent")
    if "maximum_entries" not in directory_scheduler or "maximum_depth" not in directory_scheduler:
        failures.append("directory traversal bounds are absent")
    if "Lambda Blotto is discrete Colonel Blotto" not in manifest["semantics"]:
        failures.append("integrated Lambda Blotto semantic statement is absent")
    if "spectral coordinates" not in manifest["lambda_role"] or "lambda-calculus motion" not in manifest["lambda_role"]:
        failures.append("Lambda spectral/motion role is absent")
    seal = (external_root / "receipt/seal/library.py").read_text()
    if "non-observed-seal-rejected" not in seal or "provenance.evidence_class" not in seal:
        failures.append("Predicted/Counterfactual sealing guard is absent")
    request = (operation_root / "request/value.py").read_text()
    if "provenance: Provenance" not in request:
        failures.append("artifact provenance is absent from capture request")
    provenance = (operation_root / "artifact/provenance/value.py").read_text()
    file_seal = (external_root / "receipt/seal/library.py").read_text()
    directory_serialize = (directory_operation_root / "frame/serialize/project.py").read_text()
    routing_serialize = (operation_root / "publication/routing/serialize/project.py").read_text()
    occurrence = (operation_root / "publication/routing/occurrence/value.py").read_text()
    occurrence_serialize = (operation_root / "publication/routing/occurrence/serialize/project.py").read_text()
    for field in ("drilldown_chain", "source_diversity", "publication_routing"):
        if field not in provenance:
            failures.append(f"artifact provenance omits {field}")
    for field in ("source_kind", "source_family", "source_identity"):
        if field not in file_seal or field not in directory_serialize:
            failures.append(f"sealed source diversity omits {field}")
    if "ROUTING(routing)" not in file_seal or "ROUTING(routing)" not in directory_serialize:
        failures.append("file or directory receipt omits the publication-routing projection")
    for field in ("claim_key", "volume_route", "chapter_route", "appendix_route", "occurrences"):
        if field not in routing_serialize:
            failures.append(f"sealed publication routing omits {field}")
    for field in ("occurrence_key", "source_kind", "authority_role", "route_relation", "exact_text", "source_path", "source_locus", "source_revision", "frame_time", "authority_scope", "resolution_status", "non_exclusivity", "evidence_class", "claim_classification", "support_boundary", "target_volume_route", "target_chapter_route", "target_subsection_route", "semantic_drilldown_route", "diagram_route", "citation_key", "publication_header", "publication_footer", "readback_artifact"):
        if field not in occurrence:
            failures.append(f"corpus route occurrence omits {field}")
        if field not in occurrence_serialize:
            failures.append(f"corpus route occurrence serializer omits {field}")
    occurrence_fields = ("occurrence_key", "source_kind", "authority_role", "route_relation", "exact_text", "source_path", "source_locus", "source_revision", "frame_time", "authority_scope", "resolution_status", "non_exclusivity", "evidence_class", "claim_classification", "support_boundary", "target_volume_route", "target_chapter_route")
    occurrence_keys = []
    for routing_manifest in routing_manifests:
        if "source locus" not in routing_manifest.get("publication_validation_law", "").lower():
            failures.append(f"routing manifest publication law omits source locus: {routing_manifest.get('identity', '<missing-identity>')}")
        coordinate_fields = ("coordinate_key", "applies_to_occurrence_keys", "volume_route", "chapter_route", "subsection_route", "semantic_drilldown_route", "diagram_route", "citation_key", "source_locus_field", "header_artifact", "footer_artifact", "readback_artifact")
        coordinate_owners = {}
        for coordinate in routing_manifest.get("publication_coordinates", ()):
            for field in coordinate_fields:
                if not coordinate.get(field):
                    failures.append(f"publication coordinate omits {field}: {coordinate.get('coordinate_key', '<missing-key>')}")
            if coordinate.get("source_locus_field") != "occurrence.source_locus":
                failures.append(f"publication coordinate does not bind occurrence source locus: {coordinate.get('coordinate_key', '<missing-key>')}")
            for occurrence_key in coordinate.get("applies_to_occurrence_keys", ()):
                coordinate_owners.setdefault(occurrence_key, []).append(coordinate)
        for routed_occurrence in routing_manifest["occurrences"]:
            occurrence_keys.append(routed_occurrence.get("occurrence_key"))
            for field in occurrence_fields:
                if not routed_occurrence.get(field):
                    failures.append(f"routing manifest occurrence omits {field}: {routed_occurrence.get('occurrence_key', '<missing-key>')}")
            owners = coordinate_owners.get(routed_occurrence.get("occurrence_key"), ())
            if len(owners) != 1:
                failures.append(f"routing occurrence requires exactly one publication coordinate: {routed_occurrence.get('occurrence_key', '<missing-key>')}")
            elif owners[0].get("volume_route") != routed_occurrence.get("target_volume_route") or owners[0].get("chapter_route") != routed_occurrence.get("target_chapter_route"):
                failures.append(f"publication coordinate route mismatch: {routed_occurrence.get('occurrence_key', '<missing-key>')}")
        routed_keys = {routed_occurrence.get("occurrence_key") for routed_occurrence in routing_manifest["occurrences"]}
        unknown_coordinate_keys = set(coordinate_owners) - routed_keys
        if unknown_coordinate_keys:
            failures.append(f"publication coordinates name unknown occurrences: {sorted(unknown_coordinate_keys)}")
    if len(occurrence_keys) != len(set(occurrence_keys)):
        failures.append("routing manifest occurrence keys are not globally unique")
    for candidate in source.rglob("*.py"):
        try:
            compile(candidate.read_bytes(), str(candidate), "exec")
        except SyntaxError as issue:
            failures.append(f"Python syntax failure: {candidate.relative_to(root)}:{issue.lineno}")
        import_lines = tuple(line for line in candidate.read_text().splitlines() if line.startswith(("from ", "import ")))
        if any(".lambda." in line or ".evidence.class." in line or ".issue.from." in line for line in import_lines):
            failures.append(f"reserved-keyword package import remains: {candidate.relative_to(root)}")
    return tuple(failures)
