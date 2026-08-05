SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/artifact-manifest
VOLUME_ARTIFACT_MANIFEST_GENERATED_ROOT ?= $(CURDIR)
VOLUME_ARTIFACT_MANIFEST_00_FRAME := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/00-input-frame.carrier
VOLUME_ARTIFACT_MANIFEST_01_CONTRACT_EXISTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/01-contract-exists.carrier
VOLUME_ARTIFACT_MANIFEST_02_CONTRACT_PARSED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/02-contract-parsed.carrier
VOLUME_ARTIFACT_MANIFEST_03_CONTRACT_CARDINALITY_OBSERVED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/03-contract-cardinality-observed.carrier
VOLUME_ARTIFACT_MANIFEST_04_CONTRACT_CARDINALITY_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/04-contract-cardinality-validated.carrier
VOLUME_ARTIFACT_MANIFEST_05_INVENTORY_IDENTITY_INDEX := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/05-inventory-identity-index.carrier
VOLUME_ARTIFACT_MANIFEST_06_INVENTORY_IDENTITY_INDEX_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/06-inventory-identity-index-validated.carrier
VOLUME_ARTIFACT_MANIFEST_07_INVENTORY_IDENTITIES := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/07-inventory-identities.carrier
VOLUME_ARTIFACT_MANIFEST_08_UNIQUE_INVENTORY_IDENTITIES := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/08-unique-inventory-identities.carrier
VOLUME_ARTIFACT_MANIFEST_09_INVENTORY_UNIQUENESS_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/09-inventory-uniqueness-validated.carrier
VOLUME_ARTIFACT_MANIFEST_10_CSV_ARTIFACT_INDEX := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/10-csv-artifact-index.carrier
VOLUME_ARTIFACT_MANIFEST_11_CSV_ARTIFACT_INDEX_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/11-csv-artifact-index-validated.carrier
VOLUME_ARTIFACT_MANIFEST_12_EXPECTED_CSV_ARTIFACTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/12-expected-csv-artifacts.carrier
VOLUME_ARTIFACT_MANIFEST_13_EXPECTED_CSV_ARTIFACTS_ORDERED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/13-expected-csv-artifacts-ordered.carrier
VOLUME_ARTIFACT_MANIFEST_14_OBSERVED_CSV_ARTIFACTS_ORDERED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/14-observed-csv-artifacts-ordered.carrier
VOLUME_ARTIFACT_MANIFEST_15_CSV_ARTIFACT_SET_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/15-csv-artifact-set-validated.carrier
VOLUME_ARTIFACT_MANIFEST_16_FRAGMENT_ARTIFACT_INDEX := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/16-fragment-artifact-index.carrier
VOLUME_ARTIFACT_MANIFEST_17_FRAGMENT_ARTIFACT_INDEX_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/17-fragment-artifact-index-validated.carrier
VOLUME_ARTIFACT_MANIFEST_18_EXPECTED_TABLE_ARTIFACTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/18-expected-table-artifacts.carrier
VOLUME_ARTIFACT_MANIFEST_19_EXPECTED_FRAGMENT_ARTIFACTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/19-expected-fragment-artifacts.carrier
VOLUME_ARTIFACT_MANIFEST_20_EXPECTED_BODY_ARTIFACTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/20-expected-body-artifacts.carrier
VOLUME_ARTIFACT_MANIFEST_21_EXPECTED_ARTIFACTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/21-expected-artifacts.carrier
VOLUME_ARTIFACT_MANIFEST_22_EXPECTED_ARTIFACTS_NORMALIZED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/22-expected-artifacts-normalized.carrier
VOLUME_ARTIFACT_MANIFEST_23_EXPECTED_ARTIFACTS_ORDERED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/23-expected-artifacts-ordered.carrier
VOLUME_ARTIFACT_MANIFEST_24_EXPECTED_ARTIFACT_CARDINALITY_OBSERVED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/24-expected-artifact-cardinality-observed.carrier
VOLUME_ARTIFACT_MANIFEST_24A_OBSERVED_ARTIFACT_CARDINALITY_OBSERVED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/24a-observed-artifact-cardinality-observed.carrier
VOLUME_ARTIFACT_MANIFEST_25_ARTIFACT_CARDINALITY_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/25-artifact-cardinality-validated.carrier
VOLUME_ARTIFACT_MANIFEST_26_UNSAFE_ARTIFACT_SELECTED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/26-unsafe-artifact-selected.carrier
VOLUME_ARTIFACT_MANIFEST_27_ARTIFACT_PATH_SAFETY_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/27-artifact-path-safety-validated.carrier
VOLUME_ARTIFACT_MANIFEST_27A_ARTIFACT_PATHNAMES := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/27a-artifact-pathnames.carrier
VOLUME_ARTIFACT_MANIFEST_28_ARTIFACT_PATHS_NORMALIZED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/28-artifact-paths-normalized.carrier
VOLUME_ARTIFACT_MANIFEST_28A_ARTIFACT_PATH_STRINGS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/28a-artifact-path-strings.carrier
VOLUME_ARTIFACT_MANIFEST_29_UNIQUE_ARTIFACT_PATHS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/29-unique-artifact-paths.carrier
VOLUME_ARTIFACT_MANIFEST_30_ARTIFACT_UNIQUENESS_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/30-artifact-uniqueness-validated.carrier
VOLUME_ARTIFACT_MANIFEST_31_ARTIFACT_PATHS_ORDERED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/31-artifact-paths-ordered.carrier
VOLUME_ARTIFACT_MANIFEST_32_ARTIFACT_SET_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/32-artifact-set-validated.carrier
VOLUME_ARTIFACT_MANIFEST_33_MISSING_ARTIFACT_SELECTED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/33-missing-artifact-selected.carrier
VOLUME_ARTIFACT_MANIFEST_34_ARTIFACT_EXISTENCE_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/34-artifact-existence-validated.carrier
VOLUME_ARTIFACT_MANIFEST_35_EMPTY_ARTIFACT_SELECTED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/35-empty-artifact-selected.carrier
VOLUME_ARTIFACT_MANIFEST_36_ARTIFACT_NONEMPTY_VALIDATED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/36-artifact-nonempty-validated.carrier
VOLUME_ARTIFACT_MANIFEST_37_CSV_ARTIFACTS_PARSED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/37-csv-artifacts-parsed.carrier
VOLUME_ARTIFACT_MANIFEST_38_ARTIFACT_BYTES_OBSERVED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/38-artifact-bytes-observed.carrier
VOLUME_ARTIFACT_MANIFEST_39_ARTIFACT_DIGESTS_OBSERVED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/39-artifact-digests-observed.carrier
VOLUME_ARTIFACT_MANIFEST_40_INVENTORY_LOCATORS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/40-inventory-locators.carrier
VOLUME_ARTIFACT_MANIFEST_40A_INVENTORY_TEX_PATHS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/40a-inventory-tex-paths.carrier
VOLUME_ARTIFACT_MANIFEST_41_CSV_DOCUMENTS_ATTACHED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/41-csv-documents-attached.carrier
VOLUME_ARTIFACT_MANIFEST_42_INVENTORY_ROW_COUNTS := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/42-inventory-row-counts.carrier
VOLUME_ARTIFACT_MANIFEST_43_CARRIER_RELEASED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/43-carrier-released.carrier
VOLUME_ARTIFACT_MANIFEST_44_INVENTORIES_ORDERED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/44-inventories-ordered.carrier
VOLUME_ARTIFACT_MANIFEST_45_GAPS_DEFAULTED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/45-gaps-defaulted.carrier
VOLUME_ARTIFACT_MANIFEST_46_MANIFEST_CONSTRUCTED := $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/46-manifest-constructed.carrier
VOLUME_ARTIFACT_MANIFEST ?= $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)/manifest.json

.PHONY: volume-artifact-manifest volume-artifact-manifest-force
volume-artifact-manifest: $(VOLUME_ARTIFACT_MANIFEST)

volume-artifact-manifest-force:

$(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT):
	mkdir -p "$@"

$(VOLUME_ARTIFACT_MANIFEST_00_FRAME): volume-artifact-manifest-force | $(VOLUME_ARTIFACT_MANIFEST_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$(VOLUME_INVENTORY_CONTRACT)" || { printf '%s\n' 'VOLUME_INVENTORY_CONTRACT is required' >&2; exit 64; }
	@test -n "$(VOLUME_MANIFEST_CSV_ARTIFACTS)" || { printf '%s\n' 'VOLUME_MANIFEST_CSV_ARTIFACTS is required' >&2; exit 64; }
	@test -n "$(VOLUME_MANIFEST_ARTIFACTS)" || { printf '%s\n' 'VOLUME_MANIFEST_ARTIFACTS is required' >&2; exit 64; }
	@set +e; cd "$(VOLUME_ARTIFACT_MANIFEST_GENERATED_ROOT)" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.manifest.input.frame.process "$(abspath $(VOLUME_INVENTORY_CONTRACT))" "$(words $(VOLUME_MANIFEST_CSV_ARTIFACTS))" $(VOLUME_MANIFEST_CSV_ARTIFACTS) $(VOLUME_MANIFEST_ARTIFACTS) >"$(abspath $@).tmp" 2>"$(abspath $@).error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$(abspath $@).error" >&2; exit "$$status"; fi; \
	rm -f "$(abspath $@).error"; mv "$(abspath $@).tmp" "$(abspath $@)"

define VOLUME_ARTIFACT_MANIFEST_STAGE
$(1): $(2)
	@set +e; cd "$(VOLUME_ARTIFACT_MANIFEST_GENERATED_ROOT)" && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m $(3) <"$(abspath $(2))" >"$(abspath $(1)).tmp" 2>"$(abspath $(1)).error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$(abspath $(1)).error" >&2; exit "$$$$status"; fi; \
	rm -f "$(abspath $(1)).error"; mv "$(abspath $(1)).tmp" "$(abspath $(1))"
endef

$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_01_CONTRACT_EXISTS),$(VOLUME_ARTIFACT_MANIFEST_00_FRAME),silmaril.sparky.morphism.codebase.volume.artifact.manifest.contract.existence.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_02_CONTRACT_PARSED),$(VOLUME_ARTIFACT_MANIFEST_01_CONTRACT_EXISTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.parse.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_03_CONTRACT_CARDINALITY_OBSERVED),$(VOLUME_ARTIFACT_MANIFEST_02_CONTRACT_PARSED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.contract.cardinality.observation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_04_CONTRACT_CARDINALITY_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_03_CONTRACT_CARDINALITY_OBSERVED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.contract.cardinality.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_05_INVENTORY_IDENTITY_INDEX),$(VOLUME_ARTIFACT_MANIFEST_04_CONTRACT_CARDINALITY_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.identity.index.lookup.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_06_INVENTORY_IDENTITY_INDEX_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_05_INVENTORY_IDENTITY_INDEX),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.identity.index.existence.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_07_INVENTORY_IDENTITIES),$(VOLUME_ARTIFACT_MANIFEST_06_INVENTORY_IDENTITY_INDEX_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.identity.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_08_UNIQUE_INVENTORY_IDENTITIES),$(VOLUME_ARTIFACT_MANIFEST_07_INVENTORY_IDENTITIES),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.unique.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_09_INVENTORY_UNIQUENESS_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_08_UNIQUE_INVENTORY_IDENTITIES),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.uniqueness.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_10_CSV_ARTIFACT_INDEX),$(VOLUME_ARTIFACT_MANIFEST_09_INVENTORY_UNIQUENESS_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.index.lookup.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_11_CSV_ARTIFACT_INDEX_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_10_CSV_ARTIFACT_INDEX),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.index.existence.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_12_EXPECTED_CSV_ARTIFACTS),$(VOLUME_ARTIFACT_MANIFEST_11_CSV_ARTIFACT_INDEX_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.expected.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_13_EXPECTED_CSV_ARTIFACTS_ORDERED),$(VOLUME_ARTIFACT_MANIFEST_12_EXPECTED_CSV_ARTIFACTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.expected.canonical_order.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_14_OBSERVED_CSV_ARTIFACTS_ORDERED),$(VOLUME_ARTIFACT_MANIFEST_13_EXPECTED_CSV_ARTIFACTS_ORDERED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.observed.canonical_order.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_15_CSV_ARTIFACT_SET_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_14_OBSERVED_CSV_ARTIFACTS_ORDERED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.set.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_16_FRAGMENT_ARTIFACT_INDEX),$(VOLUME_ARTIFACT_MANIFEST_15_CSV_ARTIFACT_SET_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.fragment.artifact.index.lookup.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_17_FRAGMENT_ARTIFACT_INDEX_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_16_FRAGMENT_ARTIFACT_INDEX),silmaril.sparky.morphism.codebase.volume.artifact.manifest.fragment.artifact.index.existence.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_18_EXPECTED_TABLE_ARTIFACTS),$(VOLUME_ARTIFACT_MANIFEST_17_FRAGMENT_ARTIFACT_INDEX_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.expected.table.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_19_EXPECTED_FRAGMENT_ARTIFACTS),$(VOLUME_ARTIFACT_MANIFEST_18_EXPECTED_TABLE_ARTIFACTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.expected.fragment.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_20_EXPECTED_BODY_ARTIFACTS),$(VOLUME_ARTIFACT_MANIFEST_19_EXPECTED_FRAGMENT_ARTIFACTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.expected.body.construction.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_21_EXPECTED_ARTIFACTS),$(VOLUME_ARTIFACT_MANIFEST_20_EXPECTED_BODY_ARTIFACTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.expected.artifact.aggregation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_22_EXPECTED_ARTIFACTS_NORMALIZED),$(VOLUME_ARTIFACT_MANIFEST_21_EXPECTED_ARTIFACTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.expected.artifact.normalization.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_23_EXPECTED_ARTIFACTS_ORDERED),$(VOLUME_ARTIFACT_MANIFEST_22_EXPECTED_ARTIFACTS_NORMALIZED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.expected.artifact.canonical_order.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_24_EXPECTED_ARTIFACT_CARDINALITY_OBSERVED),$(VOLUME_ARTIFACT_MANIFEST_23_EXPECTED_ARTIFACTS_ORDERED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.cardinality.expected.observation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_24A_OBSERVED_ARTIFACT_CARDINALITY_OBSERVED),$(VOLUME_ARTIFACT_MANIFEST_24_EXPECTED_ARTIFACT_CARDINALITY_OBSERVED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.cardinality.observed.observation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_25_ARTIFACT_CARDINALITY_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_24A_OBSERVED_ARTIFACT_CARDINALITY_OBSERVED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.cardinality.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_26_UNSAFE_ARTIFACT_SELECTED),$(VOLUME_ARTIFACT_MANIFEST_25_ARTIFACT_CARDINALITY_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.path.unsafe.selection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_27_ARTIFACT_PATH_SAFETY_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_26_UNSAFE_ARTIFACT_SELECTED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.path.safety.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_27A_ARTIFACT_PATHNAMES),$(VOLUME_ARTIFACT_MANIFEST_27_ARTIFACT_PATH_SAFETY_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.path.pathname.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_28_ARTIFACT_PATHS_NORMALIZED),$(VOLUME_ARTIFACT_MANIFEST_27A_ARTIFACT_PATHNAMES),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.path.normalization.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_28A_ARTIFACT_PATH_STRINGS),$(VOLUME_ARTIFACT_MANIFEST_28_ARTIFACT_PATHS_NORMALIZED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.path.string.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_29_UNIQUE_ARTIFACT_PATHS),$(VOLUME_ARTIFACT_MANIFEST_28A_ARTIFACT_PATH_STRINGS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.unique.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_30_ARTIFACT_UNIQUENESS_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_29_UNIQUE_ARTIFACT_PATHS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.uniqueness.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_31_ARTIFACT_PATHS_ORDERED),$(VOLUME_ARTIFACT_MANIFEST_30_ARTIFACT_UNIQUENESS_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.canonical_order.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_32_ARTIFACT_SET_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_31_ARTIFACT_PATHS_ORDERED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.set.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_33_MISSING_ARTIFACT_SELECTED),$(VOLUME_ARTIFACT_MANIFEST_32_ARTIFACT_SET_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.missing.selection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_34_ARTIFACT_EXISTENCE_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_33_MISSING_ARTIFACT_SELECTED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.existence.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_35_EMPTY_ARTIFACT_SELECTED),$(VOLUME_ARTIFACT_MANIFEST_34_ARTIFACT_EXISTENCE_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.empty.selection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_36_ARTIFACT_NONEMPTY_VALIDATED),$(VOLUME_ARTIFACT_MANIFEST_35_EMPTY_ARTIFACT_SELECTED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.nonempty.validation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_37_CSV_ARTIFACTS_PARSED),$(VOLUME_ARTIFACT_MANIFEST_36_ARTIFACT_NONEMPTY_VALIDATED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.csv_artifact.parse.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_38_ARTIFACT_BYTES_OBSERVED),$(VOLUME_ARTIFACT_MANIFEST_37_CSV_ARTIFACTS_PARSED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.bytes.observation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_39_ARTIFACT_DIGESTS_OBSERVED),$(VOLUME_ARTIFACT_MANIFEST_38_ARTIFACT_BYTES_OBSERVED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.artifact.digest.observation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_40_INVENTORY_LOCATORS),$(VOLUME_ARTIFACT_MANIFEST_39_ARTIFACT_DIGESTS_OBSERVED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.locator.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_40A_INVENTORY_TEX_PATHS),$(VOLUME_ARTIFACT_MANIFEST_40_INVENTORY_LOCATORS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.tex_path.derivation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_41_CSV_DOCUMENTS_ATTACHED),$(VOLUME_ARTIFACT_MANIFEST_40A_INVENTORY_TEX_PATHS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.csv_document.attachment.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_42_INVENTORY_ROW_COUNTS),$(VOLUME_ARTIFACT_MANIFEST_41_CSV_DOCUMENTS_ATTACHED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.row_count.observation.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_43_CARRIER_RELEASED),$(VOLUME_ARTIFACT_MANIFEST_42_INVENTORY_ROW_COUNTS),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.carrier.release.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_44_INVENTORIES_ORDERED),$(VOLUME_ARTIFACT_MANIFEST_43_CARRIER_RELEASED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.inventory.canonical_order.projection.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_45_GAPS_DEFAULTED),$(VOLUME_ARTIFACT_MANIFEST_44_INVENTORIES_ORDERED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.gap.default.construction.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST_46_MANIFEST_CONSTRUCTED),$(VOLUME_ARTIFACT_MANIFEST_45_GAPS_DEFAULTED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.construct.process))
$(eval $(call VOLUME_ARTIFACT_MANIFEST_STAGE,$(VOLUME_ARTIFACT_MANIFEST),$(VOLUME_ARTIFACT_MANIFEST_46_MANIFEST_CONSTRUCTED),silmaril.sparky.morphism.codebase.volume.artifact.manifest.encode.process))
