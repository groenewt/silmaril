# Generate the complete Volume 40 producer tree.  This file contains no
# semantic implementation: every transformation is a named external runtime
# process and every composition edge is visible to Make.

VOLUME_40_INVENTORY_NAMES := \
	source_files \
	modules \
	public_apis \
	dependencies \
	configuration \
	mix_tasks \
	project_tasks \
	make_targets \
	telephone_topology \
	ring_families \
	native_tree \
	gdb_evidence \
	scripts \
	tests \
	documentation \
	shared_components \
	shared_anchors \
	catalog_documents \
	catalog_claims \
	catalog_gaps \
	catalog_quality_flags \
	provenance \
	phase14

VOLUME_40_INVENTORY_SOURCE_source_files = $(VOLUME_SOURCE_FILES_CSV)
VOLUME_40_INVENTORY_SOURCE_modules = $(VOLUME_TABLE_MODULES_CSV)
VOLUME_40_INVENTORY_SOURCE_public_apis = $(VOLUME_TABLE_PUBLIC_APIS_CSV)
VOLUME_40_INVENTORY_SOURCE_dependencies = $(VOLUME_TABLE_DEPENDENCIES_CSV)
VOLUME_40_INVENTORY_SOURCE_configuration = $(VOLUME_TABLE_CONFIGURATION_CSV)
VOLUME_40_INVENTORY_SOURCE_mix_tasks = $(VOLUME_TABLE_MIX_TASKS_CSV)
VOLUME_40_INVENTORY_SOURCE_project_tasks = $(VOLUME_TABLE_PROJECT_TASKS_CSV)
VOLUME_40_INVENTORY_SOURCE_make_targets = $(VOLUME_TABLE_MAKE_TARGETS_CSV)
VOLUME_40_INVENTORY_SOURCE_telephone_topology = $(VOLUME_TABLE_TELEPHONE_TOPOLOGY_CSV)
VOLUME_40_INVENTORY_SOURCE_ring_families = $(VOLUME_RING_FAMILIES_CSV)
VOLUME_40_INVENTORY_SOURCE_native_tree = $(VOLUME_TABLE_NATIVE_TREE_CSV)
VOLUME_40_INVENTORY_SOURCE_gdb_evidence = $(VOLUME_GDB_EVIDENCE_CSV)
VOLUME_40_INVENTORY_SOURCE_scripts = $(VOLUME_TABLE_SCRIPTS_CSV)
VOLUME_40_INVENTORY_SOURCE_tests = $(VOLUME_TABLE_TESTS_CSV)
VOLUME_40_INVENTORY_SOURCE_documentation = $(VOLUME_TABLE_DOCUMENTATION_CSV)
VOLUME_40_INVENTORY_SOURCE_shared_components = $(VOLUME_SHARED_COMPONENTS_CSV)
VOLUME_40_INVENTORY_SOURCE_shared_anchors = $(VOLUME_SHARED_ANCHORS_CSV)
VOLUME_40_INVENTORY_SOURCE_catalog_documents = $(VOLUME_INVENTORY_CATALOG_DOCUMENTS_CSV)
VOLUME_40_INVENTORY_SOURCE_catalog_claims = $(VOLUME_INVENTORY_CATALOG_CLAIMS_CSV)
VOLUME_40_INVENTORY_SOURCE_catalog_gaps = $(VOLUME_INVENTORY_CATALOG_GAPS_CSV)
VOLUME_40_INVENTORY_SOURCE_catalog_quality_flags = $(VOLUME_INVENTORY_CATALOG_QUALITY_FLAGS_CSV)
VOLUME_40_INVENTORY_SOURCE_provenance = $(VOLUME_TABLE_PROVENANCE_CSV)
VOLUME_40_INVENTORY_SOURCE_phase14 = $(VOLUME_PHASE14_TABLE_CSV)

VOLUME_40_INVENTORY_TITLE_source_files := Source files
VOLUME_40_INVENTORY_TITLE_modules := Modules
VOLUME_40_INVENTORY_TITLE_public_apis := Public APIs
VOLUME_40_INVENTORY_TITLE_dependencies := Dependencies
VOLUME_40_INVENTORY_TITLE_configuration := Configuration
VOLUME_40_INVENTORY_TITLE_mix_tasks := Mix tasks
VOLUME_40_INVENTORY_TITLE_project_tasks := Project tasks
VOLUME_40_INVENTORY_TITLE_make_targets := Make targets
VOLUME_40_INVENTORY_TITLE_telephone_topology := Telephone topology
VOLUME_40_INVENTORY_TITLE_ring_families := Ring families
VOLUME_40_INVENTORY_TITLE_native_tree := Native tree
VOLUME_40_INVENTORY_TITLE_gdb_evidence := GDB evidence
VOLUME_40_INVENTORY_TITLE_scripts := Scripts
VOLUME_40_INVENTORY_TITLE_tests := Tests
VOLUME_40_INVENTORY_TITLE_documentation := Documentation
VOLUME_40_INVENTORY_TITLE_shared_components := Shared components
VOLUME_40_INVENTORY_TITLE_shared_anchors := Shared anchors
VOLUME_40_INVENTORY_TITLE_catalog_documents := Catalog documents
VOLUME_40_INVENTORY_TITLE_catalog_claims := Catalog claims
VOLUME_40_INVENTORY_TITLE_catalog_gaps := Catalog gaps
VOLUME_40_INVENTORY_TITLE_catalog_quality_flags := Catalog quality flags
VOLUME_40_INVENTORY_TITLE_provenance := Provenance
VOLUME_40_INVENTORY_TITLE_phase14 := Phase 14 certification matrix

VOLUME_40_INVENTORY_SOURCE_PATHS = $(foreach name,$(VOLUME_40_INVENTORY_NAMES),$(VOLUME_40_INVENTORY_SOURCE_$(name)))
VOLUME_40_PRODUCTION_INVENTORY_RELATIVE := $(addprefix inventories/,$(addsuffix .csv,$(VOLUME_40_INVENTORY_NAMES)))
VOLUME_40_PRODUCTION_INVENTORIES := $(addprefix $(VOLUME_40_PRODUCTION_ROOT)/,$(VOLUME_40_PRODUCTION_INVENTORY_RELATIVE))
VOLUME_40_TABLE_RELATIVE := $(addprefix tables/,$(addsuffix .tex,$(VOLUME_40_INVENTORY_NAMES)))
VOLUME_40_TABLES := $(addprefix $(VOLUME_40_PRODUCTION_ROOT)/,$(VOLUME_40_TABLE_RELATIVE))
VOLUME_40_FRAGMENT_RELATIVE := \
	00_architecture.tex \
	01_build_configuration_tasks.tex \
	02_telephone_rings.tex \
	03_native_gdb_verification.tex \
	04_operations_documentation.tex \
	05_provenance_relations_gaps.tex \
	06_phase14_26x4.tex \
	body.tex
VOLUME_40_FRAGMENTS := $(addprefix $(VOLUME_40_PRODUCTION_ROOT)/,$(VOLUME_40_FRAGMENT_RELATIVE))
VOLUME_40_READBACK_RELATIVE := manifest.json source_to_fragment.csv sha256sums.txt
VOLUME_40_READBACKS := $(addprefix $(VOLUME_40_PRODUCTION_ROOT)/,$(VOLUME_40_READBACK_RELATIVE))
VOLUME_40_INSTALL_RELATIVE := $(sort $(VOLUME_40_TABLE_RELATIVE) $(VOLUME_40_FRAGMENT_RELATIVE) $(VOLUME_40_READBACK_RELATIVE))
VOLUME_40_INSTALL_SOURCES := $(addprefix $(VOLUME_40_PRODUCTION_ROOT)/,$(VOLUME_40_INSTALL_RELATIVE))
VOLUME_40_PREHASH_RELATIVE := $(filter-out sha256sums.txt,$(VOLUME_40_INSTALL_RELATIVE))
VOLUME_40_PREHASH_ARTIFACTS := $(addprefix $(VOLUME_40_PRODUCTION_ROOT)/,$(VOLUME_40_PREHASH_RELATIVE))

VOLUME_MANIFEST_CSV_ARTIFACTS = $(VOLUME_40_PRODUCTION_INVENTORY_RELATIVE)
VOLUME_MANIFEST_ARTIFACTS = $(VOLUME_40_PRODUCTION_INVENTORY_RELATIVE) $(VOLUME_40_TABLE_RELATIVE) $(VOLUME_40_FRAGMENT_RELATIVE)

VOLUME_40_INVENTORY_TARGETS := \
	morphism-codebase-volume-source-observation-line \
	morphism-codebase-volume-table-source-files-aggregate \
	morphism-codebase-volume-table-modules \
	morphism-codebase-volume-table-public-apis \
	morphism-codebase-volume-table-dependencies \
	morphism-codebase-volume-table-configuration \
	morphism-codebase-volume-table-scripts \
	morphism-codebase-volume-table-tests \
	morphism-codebase-volume-table-documentation \
	morphism-codebase-volume-table-mix-tasks \
	morphism-codebase-volume-table-project-tasks \
	morphism-codebase-volume-table-make-targets \
	morphism-codebase-volume-table-native-tree \
	morphism-codebase-volume-table-telephone-topology \
	morphism-codebase-volume-table-provenance \
	morphism-codebase-volume-table-ring-families-aggregate \
	morphism-codebase-volume-table-gdb-evidence-aggregate \
	morphism-codebase-volume-table-shared-components-aggregate \
	morphism-codebase-volume-table-shared-anchors-aggregate \
	volume-inventory-catalogs \
	volume-phase14-table

.PHONY: volume-40-inventories volume-40-generate
volume-40-inventories: volume-40-bindings $(VOLUME_40_INVENTORY_TARGETS)

volume-40-generate: volume-40-bindings $(VOLUME_40_INSTALL_SOURCES)
	@printf 'Volume 40 producer root materialized: %s\n' "$(VOLUME_40_PRODUCTION_ROOT)"

$(VOLUME_40_PRODUCTION_ROOT)/inventories \
$(VOLUME_40_PRODUCTION_ROOT)/tables \
$(VOLUME_40_RECEIPT_ROOT) \
$(VOLUME_40_HASH_ROOT) \
$(VOLUME_40_HASH_ROOT)/lines:
	mkdir -p "$@"

define VOLUME_40_INVENTORY_RULE
$(VOLUME_40_PRODUCTION_ROOT)/inventories/$(1).csv: $$(VOLUME_40_INVENTORY_SOURCE_$(1)) | $(VOLUME_40_PRODUCTION_ROOT)/inventories $(VOLUME_40_RECEIPT_ROOT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.install.process "$$<" "$$@" >"$(VOLUME_40_RECEIPT_ROOT)/inventory-$(1).stdout" 2>"$(VOLUME_40_RECEIPT_ROOT)/inventory-$(1).stderr"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$(VOLUME_40_RECEIPT_ROOT)/inventory-$(1).stderr" >&2; exit "$$$$status"; fi; \
	printf '%s\n' "$$$$status" >"$(VOLUME_40_RECEIPT_ROOT)/inventory-$(1).status"

$(VOLUME_40_PRODUCTION_ROOT)/tables/$(1).tex: $(VOLUME_40_PRODUCTION_ROOT)/inventories/$(1).csv | $(VOLUME_40_PRODUCTION_ROOT)/tables
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.projection.inventory.process "$$(VOLUME_40_INVENTORY_TITLE_$(1))" <"$$<" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; \
	rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

$(foreach name,$(VOLUME_40_INVENTORY_NAMES),$(eval $(call VOLUME_40_INVENTORY_RULE,$(name))))

$(VOLUME_40_PRODUCTION_ROOT)/00_architecture.tex: \
	$(addprefix $(VOLUME_40_PRODUCTION_ROOT)/tables/,source_files.tex modules.tex public_apis.tex dependencies.tex)
$(VOLUME_40_PRODUCTION_ROOT)/01_build_configuration_tasks.tex: \
	$(addprefix $(VOLUME_40_PRODUCTION_ROOT)/tables/,configuration.tex mix_tasks.tex project_tasks.tex make_targets.tex)
$(VOLUME_40_PRODUCTION_ROOT)/02_telephone_rings.tex: \
	$(addprefix $(VOLUME_40_PRODUCTION_ROOT)/tables/,telephone_topology.tex ring_families.tex)
$(VOLUME_40_PRODUCTION_ROOT)/03_native_gdb_verification.tex: \
	$(addprefix $(VOLUME_40_PRODUCTION_ROOT)/tables/,native_tree.tex gdb_evidence.tex)
$(VOLUME_40_PRODUCTION_ROOT)/04_operations_documentation.tex: \
	$(addprefix $(VOLUME_40_PRODUCTION_ROOT)/tables/,scripts.tex tests.tex documentation.tex shared_components.tex shared_anchors.tex)
$(VOLUME_40_PRODUCTION_ROOT)/05_provenance_relations_gaps.tex: \
	$(addprefix $(VOLUME_40_PRODUCTION_ROOT)/tables/,catalog_documents.tex catalog_claims.tex catalog_gaps.tex catalog_quality_flags.tex provenance.tex)
$(VOLUME_40_PRODUCTION_ROOT)/06_phase14_26x4.tex: $(VOLUME_40_PRODUCTION_ROOT)/tables/phase14.tex
$(VOLUME_40_PRODUCTION_ROOT)/body.tex: $(filter-out $(VOLUME_40_PRODUCTION_ROOT)/body.tex,$(VOLUME_40_FRAGMENTS))

$(VOLUME_ARTIFACT_MANIFEST_00_FRAME): $(VOLUME_40_PRODUCTION_INVENTORIES) $(VOLUME_40_TABLES) $(VOLUME_40_FRAGMENTS)
$(VOLUME_SOURCE_TO_FRAGMENT_00_FRAME): $(VOLUME_40_PRODUCTION_INVENTORIES) $(VOLUME_40_TABLES) $(VOLUME_40_FRAGMENTS)

define VOLUME_40_HASH_LINE_RULE
VOLUME_40_HASH_LINE_$(subst /,__,$(1)) := $(VOLUME_40_HASH_ROOT)/edge/$(subst /,__,$(1))/line/hash-line.txt
$$(VOLUME_40_HASH_LINE_$(subst /,__,$(1))): $(VOLUME_40_PRODUCTION_ROOT)/$(1) | $(VOLUME_40_HASH_ROOT)/lines
	$$(MAKE) --no-print-directory \
		-f make/morphism/codebase/volume/operation/file.mk \
		-f make/morphism/codebase/volume/operation/artifact_hash.mk \
		morphism-codebase-volume-artifact-hash-line \
		SILMARIL_PYTHON="$(SILMARIL_PYTHON)" \
		MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT="$(SILMARIL_PYLIB_SOURCE_ROOT)" \
		MORPHISM_CODEBASE_VOLUME_HASH_ROOT="$(VOLUME_40_HASH_ROOT)/edge/$(subst /,__,$(1))" \
		VOLUME_HASH_LINE_ARTIFACT="$$<" \
		VOLUME_HASH_LINE_RELATIVE_PATH="$(1)"
endef

$(foreach path,$(VOLUME_40_PREHASH_RELATIVE),$(eval $(call VOLUME_40_HASH_LINE_RULE,$(path))))
VOLUME_40_HASH_LINES := $(foreach path,$(VOLUME_40_PREHASH_RELATIVE),$(VOLUME_40_HASH_LINE_$(subst /,__,$(path))))
VOLUME_40_HASH_MANIFEST_SOURCE := $(VOLUME_40_HASH_ROOT)/manifest/manifest/manifest.txt

$(VOLUME_40_HASH_MANIFEST_SOURCE): $(VOLUME_40_HASH_LINES)
	$(MAKE) --no-print-directory \
		-f make/morphism/codebase/volume/operation/file.mk \
		-f make/morphism/codebase/volume/operation/artifact_hash.mk \
		morphism-codebase-volume-artifact-hash-manifest \
		SILMARIL_PYTHON="$(SILMARIL_PYTHON)" \
		MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT="$(SILMARIL_PYLIB_SOURCE_ROOT)" \
		MORPHISM_CODEBASE_VOLUME_HASH_ROOT="$(VOLUME_40_HASH_ROOT)/manifest" \
		VOLUME_HASH_MANIFEST_LINES="$(VOLUME_40_HASH_LINES)"

$(VOLUME_40_PRODUCTION_ROOT)/sha256sums.txt: $(VOLUME_40_HASH_MANIFEST_SOURCE) | $(VOLUME_40_PRODUCTION_ROOT) $(VOLUME_40_RECEIPT_ROOT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.install.process "$<" "$@" >"$(VOLUME_40_RECEIPT_ROOT)/sha256sums.stdout" 2>"$(VOLUME_40_RECEIPT_ROOT)/sha256sums.stderr"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$(VOLUME_40_RECEIPT_ROOT)/sha256sums.stderr" >&2; exit "$$status"; fi; \
	printf '%s\n' "$$status" >"$(VOLUME_40_RECEIPT_ROOT)/sha256sums.status"
