from config.constants.morphism.codebase.volume.projection.chapter.name.value import VALUE as CHAPTERS


def test_projection_chapter_contract() -> None:
    assert CHAPTERS == (
        ("00_architecture", ("source_files", "modules", "public_apis", "dependencies")),
        ("01_build_configuration_tasks", ("configuration", "mix_tasks", "project_tasks", "make_targets")),
        ("02_telephone_rings", ("telephone_topology", "ring_families")),
        ("03_native_gdb_verification", ("native_tree", "gdb_evidence")),
        ("04_operations_documentation", ("scripts", "tests", "documentation", "shared_components", "shared_anchors")),
        ("05_provenance_relations_gaps", ("catalog_documents", "catalog_claims", "catalog_gaps", "catalog_quality_flags", "provenance")),
        ("06_phase14_26x4", ("phase14",)),
    )
