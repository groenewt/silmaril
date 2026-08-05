from config.constants.morphism.codebase.volume.artifact.generated.table.name.value import VALUE as TABLES


def test_generated_table_contract() -> None:
    assert TABLES == (
        "source_files",
        "modules",
        "public_apis",
        "dependencies",
        "configuration",
        "scripts",
        "tests",
        "documentation",
        "catalog_documents",
        "catalog_claims",
        "catalog_gaps",
        "catalog_quality_flags",
        "mix_tasks",
        "project_tasks",
        "make_targets",
        "native_tree",
        "telephone_topology",
        "ring_families",
        "provenance",
        "phase14",
        "gdb_evidence",
        "shared_components",
        "shared_anchors",
    )
