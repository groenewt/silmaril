SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/source-to-fragment
VOLUME_SOURCE_TO_FRAGMENT_00_FRAME := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/00-input-frame.carrier
VOLUME_SOURCE_TO_FRAGMENT_01_CONTRACT_EXISTS := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/01-contract-exists.carrier
VOLUME_SOURCE_TO_FRAGMENT_02_ROOT_EXISTS := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/02-root-exists.carrier
VOLUME_SOURCE_TO_FRAGMENT_03_CONTRACT_PARSED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/03-contract-parsed.carrier
VOLUME_SOURCE_TO_FRAGMENT_04_CONTRACT_CARDINALITY_OBSERVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/04-contract-cardinality-observed.carrier
VOLUME_SOURCE_TO_FRAGMENT_05_CONTRACT_CARDINALITY_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/05-contract-cardinality-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_06_INVENTORY_INDEX := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/06-inventory-index.carrier
VOLUME_SOURCE_TO_FRAGMENT_07_INVENTORY_INDEX_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/07-inventory-index-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_08_INVENTORY_IDENTITIES := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/08-inventory-identities.carrier
VOLUME_SOURCE_TO_FRAGMENT_09_UNIQUE_INVENTORY_IDENTITIES := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/09-unique-inventory-identities.carrier
VOLUME_SOURCE_TO_FRAGMENT_10_INVENTORY_UNIQUENESS_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/10-inventory-uniqueness-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_11_SOURCE_ARTIFACT_INDEX := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/11-source-artifact-index.carrier
VOLUME_SOURCE_TO_FRAGMENT_12_SOURCE_ARTIFACT_INDEX_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/12-source-artifact-index-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_13_FRAGMENT_ARTIFACT_INDEX := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/13-fragment-artifact-index.carrier
VOLUME_SOURCE_TO_FRAGMENT_14_FRAGMENT_ARTIFACT_INDEX_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/14-fragment-artifact-index-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_15_CONTRACT_ORDERED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/15-contract-ordered.carrier
VOLUME_SOURCE_TO_FRAGMENT_16_RECORDS_PROJECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/16-records-projected.carrier
VOLUME_SOURCE_TO_FRAGMENT_17_PROJECTION_ARTIFACTS_DERIVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/17-projection-artifacts-derived.carrier
VOLUME_SOURCE_TO_FRAGMENT_18_SOURCE_PATHS_DERIVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/18-source-paths-derived.carrier
VOLUME_SOURCE_TO_FRAGMENT_19_PROJECTION_PATHS_DERIVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/19-projection-paths-derived.carrier
VOLUME_SOURCE_TO_FRAGMENT_20_FRAGMENT_PATHS_DERIVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/20-fragment-paths-derived.carrier
VOLUME_SOURCE_TO_FRAGMENT_21_MISSING_SOURCE_SELECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/21-missing-source-selected.carrier
VOLUME_SOURCE_TO_FRAGMENT_22_SOURCE_EXISTENCE_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/22-source-existence-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_23_EMPTY_SOURCE_SELECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/23-empty-source-selected.carrier
VOLUME_SOURCE_TO_FRAGMENT_24_SOURCE_NONEMPTY_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/24-source-nonempty-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_25_MISSING_PROJECTION_SELECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/25-missing-projection-selected.carrier
VOLUME_SOURCE_TO_FRAGMENT_26_PROJECTION_EXISTENCE_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/26-projection-existence-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_27_EMPTY_PROJECTION_SELECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/27-empty-projection-selected.carrier
VOLUME_SOURCE_TO_FRAGMENT_28_PROJECTION_NONEMPTY_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/28-projection-nonempty-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_29_MISSING_FRAGMENT_SELECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/29-missing-fragment-selected.carrier
VOLUME_SOURCE_TO_FRAGMENT_30_FRAGMENT_EXISTENCE_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/30-fragment-existence-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_31_EMPTY_FRAGMENT_SELECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/31-empty-fragment-selected.carrier
VOLUME_SOURCE_TO_FRAGMENT_32_FRAGMENT_NONEMPTY_VALIDATED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/32-fragment-nonempty-validated.carrier
VOLUME_SOURCE_TO_FRAGMENT_33_SOURCE_DOCUMENTS_PARSED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/33-source-documents-parsed.carrier
VOLUME_SOURCE_TO_FRAGMENT_34_SOURCE_DOCUMENTS_ATTACHED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/34-source-documents-attached.carrier
VOLUME_SOURCE_TO_FRAGMENT_35_ROW_COUNTS_OBSERVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/35-row-counts-observed.carrier
VOLUME_SOURCE_TO_FRAGMENT_36_DIGESTS_OBSERVED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/36-digests-observed.carrier
VOLUME_SOURCE_TO_FRAGMENT_37_DOCUMENT_CARRIER_RELEASED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/37-document-carrier-released.carrier
VOLUME_SOURCE_TO_FRAGMENT_38_OUTPUT_ROWS_PROJECTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/38-output-rows-projected.carrier
VOLUME_SOURCE_TO_FRAGMENT_39_HEADER_CONSTRUCTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/39-header-constructed.carrier
VOLUME_SOURCE_TO_FRAGMENT_40_ENVELOPE_CONSTRUCTED := $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/40-envelope-constructed.carrier
VOLUME_SOURCE_TO_FRAGMENT ?= $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)/source_to_fragment.csv

.PHONY: volume-source-to-fragment volume-source-to-fragment-force
volume-source-to-fragment: $(VOLUME_SOURCE_TO_FRAGMENT)

volume-source-to-fragment-force:

$(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT):
	mkdir -p "$@"

$(VOLUME_SOURCE_TO_FRAGMENT_00_FRAME): volume-source-to-fragment-force | $(VOLUME_SOURCE_TO_FRAGMENT_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$(VOLUME_INVENTORY_CONTRACT)" || { printf '%s\n' 'VOLUME_INVENTORY_CONTRACT is required' >&2; exit 64; }
	@test -n "$(VOLUME_SOURCE_TO_FRAGMENT_GENERATED_ROOT)" || { printf '%s\n' 'VOLUME_SOURCE_TO_FRAGMENT_GENERATED_ROOT is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.input.frame.process "$(abspath $(VOLUME_INVENTORY_CONTRACT))" "$(abspath $(VOLUME_SOURCE_TO_FRAGMENT_GENERATED_ROOT))" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

define VOLUME_SOURCE_TO_FRAGMENT_STAGE
$(1): $(2)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m $(3) <"$$<" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; \
	rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_01_CONTRACT_EXISTS),$(VOLUME_SOURCE_TO_FRAGMENT_00_FRAME),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.contract.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_02_ROOT_EXISTS),$(VOLUME_SOURCE_TO_FRAGMENT_01_CONTRACT_EXISTS),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.root.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_03_CONTRACT_PARSED),$(VOLUME_SOURCE_TO_FRAGMENT_02_ROOT_EXISTS),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.parse.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_04_CONTRACT_CARDINALITY_OBSERVED),$(VOLUME_SOURCE_TO_FRAGMENT_03_CONTRACT_PARSED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.contract.cardinality.observation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_05_CONTRACT_CARDINALITY_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_04_CONTRACT_CARDINALITY_OBSERVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.contract.cardinality.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_06_INVENTORY_INDEX),$(VOLUME_SOURCE_TO_FRAGMENT_05_CONTRACT_CARDINALITY_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.inventory.identity.index.lookup.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_07_INVENTORY_INDEX_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_06_INVENTORY_INDEX),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.inventory.identity.index.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_08_INVENTORY_IDENTITIES),$(VOLUME_SOURCE_TO_FRAGMENT_07_INVENTORY_INDEX_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.inventory.identity.projection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_09_UNIQUE_INVENTORY_IDENTITIES),$(VOLUME_SOURCE_TO_FRAGMENT_08_INVENTORY_IDENTITIES),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.inventory.unique.projection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_10_INVENTORY_UNIQUENESS_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_09_UNIQUE_INVENTORY_IDENTITIES),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.inventory.uniqueness.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_11_SOURCE_ARTIFACT_INDEX),$(VOLUME_SOURCE_TO_FRAGMENT_10_INVENTORY_UNIQUENESS_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.artifact.index.lookup.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_12_SOURCE_ARTIFACT_INDEX_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_11_SOURCE_ARTIFACT_INDEX),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.artifact.index.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_13_FRAGMENT_ARTIFACT_INDEX),$(VOLUME_SOURCE_TO_FRAGMENT_12_SOURCE_ARTIFACT_INDEX_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.artifact.index.lookup.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_14_FRAGMENT_ARTIFACT_INDEX_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_13_FRAGMENT_ARTIFACT_INDEX),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.artifact.index.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_15_CONTRACT_ORDERED),$(VOLUME_SOURCE_TO_FRAGMENT_14_FRAGMENT_ARTIFACT_INDEX_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.contract.canonical_order.projection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_16_RECORDS_PROJECTED),$(VOLUME_SOURCE_TO_FRAGMENT_15_CONTRACT_ORDERED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.record.projection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_17_PROJECTION_ARTIFACTS_DERIVED),$(VOLUME_SOURCE_TO_FRAGMENT_16_RECORDS_PROJECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.projection.artifact.derivation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_18_SOURCE_PATHS_DERIVED),$(VOLUME_SOURCE_TO_FRAGMENT_17_PROJECTION_ARTIFACTS_DERIVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.path.derivation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_19_PROJECTION_PATHS_DERIVED),$(VOLUME_SOURCE_TO_FRAGMENT_18_SOURCE_PATHS_DERIVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.projection.path.derivation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_20_FRAGMENT_PATHS_DERIVED),$(VOLUME_SOURCE_TO_FRAGMENT_19_PROJECTION_PATHS_DERIVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.path.derivation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_21_MISSING_SOURCE_SELECTED),$(VOLUME_SOURCE_TO_FRAGMENT_20_FRAGMENT_PATHS_DERIVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.missing.selection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_22_SOURCE_EXISTENCE_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_21_MISSING_SOURCE_SELECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_23_EMPTY_SOURCE_SELECTED),$(VOLUME_SOURCE_TO_FRAGMENT_22_SOURCE_EXISTENCE_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.empty.selection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_24_SOURCE_NONEMPTY_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_23_EMPTY_SOURCE_SELECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.nonempty.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_25_MISSING_PROJECTION_SELECTED),$(VOLUME_SOURCE_TO_FRAGMENT_24_SOURCE_NONEMPTY_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.projection.missing.selection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_26_PROJECTION_EXISTENCE_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_25_MISSING_PROJECTION_SELECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.projection.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_27_EMPTY_PROJECTION_SELECTED),$(VOLUME_SOURCE_TO_FRAGMENT_26_PROJECTION_EXISTENCE_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.projection.empty.selection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_28_PROJECTION_NONEMPTY_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_27_EMPTY_PROJECTION_SELECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.projection.nonempty.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_29_MISSING_FRAGMENT_SELECTED),$(VOLUME_SOURCE_TO_FRAGMENT_28_PROJECTION_NONEMPTY_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.missing.selection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_30_FRAGMENT_EXISTENCE_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_29_MISSING_FRAGMENT_SELECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.existence.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_31_EMPTY_FRAGMENT_SELECTED),$(VOLUME_SOURCE_TO_FRAGMENT_30_FRAGMENT_EXISTENCE_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.empty.selection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_32_FRAGMENT_NONEMPTY_VALIDATED),$(VOLUME_SOURCE_TO_FRAGMENT_31_EMPTY_FRAGMENT_SELECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.fragment.nonempty.validation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_33_SOURCE_DOCUMENTS_PARSED),$(VOLUME_SOURCE_TO_FRAGMENT_32_FRAGMENT_NONEMPTY_VALIDATED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.parse.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_34_SOURCE_DOCUMENTS_ATTACHED),$(VOLUME_SOURCE_TO_FRAGMENT_33_SOURCE_DOCUMENTS_PARSED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.document.attachment.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_35_ROW_COUNTS_OBSERVED),$(VOLUME_SOURCE_TO_FRAGMENT_34_SOURCE_DOCUMENTS_ATTACHED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.row_count.observation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_36_DIGESTS_OBSERVED),$(VOLUME_SOURCE_TO_FRAGMENT_35_ROW_COUNTS_OBSERVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.digest.observation.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_37_DOCUMENT_CARRIER_RELEASED),$(VOLUME_SOURCE_TO_FRAGMENT_36_DIGESTS_OBSERVED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.source.document.carrier.release.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_38_OUTPUT_ROWS_PROJECTED),$(VOLUME_SOURCE_TO_FRAGMENT_37_DOCUMENT_CARRIER_RELEASED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.output.row.projection.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_39_HEADER_CONSTRUCTED),$(VOLUME_SOURCE_TO_FRAGMENT_38_OUTPUT_ROWS_PROJECTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.header.construction.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT_40_ENVELOPE_CONSTRUCTED),$(VOLUME_SOURCE_TO_FRAGMENT_39_HEADER_CONSTRUCTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.construct.process))
$(eval $(call VOLUME_SOURCE_TO_FRAGMENT_STAGE,$(VOLUME_SOURCE_TO_FRAGMENT),$(VOLUME_SOURCE_TO_FRAGMENT_40_ENVELOPE_CONSTRUCTED),silmaril.sparky.morphism.codebase.volume.provenance.source_to_fragment.encode.process))
