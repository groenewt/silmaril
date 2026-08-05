# Read the publication seam back from disk.  Byte comparison, exact path-set
# comparison, hash verification, coverage checks, and source-body proof are
# distinct Make-visible process coordinates.

VOLUME_40_READBACK_COMPARISON_ROOT := $(VOLUME_40_READBACK_ROOT)/comparison
VOLUME_40_READBACK_COVERAGE_ROOT := $(VOLUME_40_READBACK_ROOT)/coverage
VOLUME_40_READBACK_PATH_ROOT := $(VOLUME_40_READBACK_ROOT)/paths
VOLUME_40_READBACK_PATH_RAW := $(VOLUME_40_READBACK_PATH_ROOT)/observed.raw
VOLUME_40_READBACK_PATH_SORTED := $(VOLUME_40_READBACK_PATH_ROOT)/observed.paths
VOLUME_40_READBACK_PATH_RECEIPT := $(VOLUME_40_READBACK_PATH_ROOT)/exact-set.validated
VOLUME_40_READBACK_HASH_RECEIPT := $(VOLUME_40_READBACK_ROOT)/hashes.validated
VOLUME_40_READBACK_STRICT_RECEIPT := $(VOLUME_40_READBACK_ROOT)/source-body.validated

VOLUME_40_MANIFEST_COVERAGE_RELATIVE := $(sort $(VOLUME_40_PRODUCTION_INVENTORY_RELATIVE) $(VOLUME_40_TABLE_RELATIVE) $(VOLUME_40_FRAGMENT_RELATIVE))
VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RELATIVE := $(sort $(VOLUME_40_PRODUCTION_INVENTORY_RELATIVE) $(VOLUME_40_TABLE_RELATIVE) $(filter-out body.tex,$(VOLUME_40_FRAGMENT_RELATIVE)))

$(VOLUME_40_READBACK_ROOT) \
$(VOLUME_40_READBACK_COMPARISON_ROOT) \
$(VOLUME_40_READBACK_COVERAGE_ROOT) \
$(VOLUME_40_READBACK_PATH_ROOT):
	mkdir -p "$@"

.PHONY: volume-40-strict-source-body volume-40-readback
volume-40-strict-source-body: morphism-codebase-volume-source-body-verify | $(VOLUME_40_READBACK_ROOT)
	@test -s "$(VOLUME_40_STRICT_SOURCE_BODY_RECEIPT)" || { printf 'strict source-body receipt missing or empty: %s\n' "$(VOLUME_40_STRICT_SOURCE_BODY_RECEIPT)" >&2; exit 66; }
	@rg -q -F "$(VOLUME_40_STRICT_SOURCE_BODY_TOKEN)" "$(VOLUME_40_STRICT_SOURCE_BODY_RECEIPT)" || { printf 'strict source-body receipt omits token: %s\n' "$(VOLUME_40_STRICT_SOURCE_BODY_TOKEN)" >&2; exit 65; }
	@printf '%s\n' "$(VOLUME_40_STRICT_SOURCE_BODY_TOKEN)" >"$(VOLUME_40_READBACK_STRICT_RECEIPT)"

define VOLUME_40_COMPARISON_RULE
VOLUME_40_COMPARISON_$(subst /,__,$(1)) := $(VOLUME_40_READBACK_COMPARISON_ROOT)/$(subst /,__,$(1)).validated
$$(VOLUME_40_COMPARISON_$(subst /,__,$(1))): $(VOLUME_40_PRODUCTION_ROOT)/$(1) $(VOLUME_40_FINAL_GENERATED_ROOT)/$(1) | $(VOLUME_40_READBACK_COMPARISON_ROOT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.comparison.process "$(VOLUME_40_PRODUCTION_ROOT)/$(1)" "$(VOLUME_40_FINAL_GENERATED_ROOT)/$(1)" >"$$@.stdout" 2>"$$@.stderr"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.stderr" >&2; exit "$$$$status"; fi; \
	printf 'byte_identity,%s\n' "$(1)" >"$$@"
endef

$(foreach path,$(VOLUME_40_INSTALL_RELATIVE),$(eval $(call VOLUME_40_COMPARISON_RULE,$(path))))
VOLUME_40_COMPARISON_RECEIPTS := $(foreach path,$(VOLUME_40_INSTALL_RELATIVE),$(VOLUME_40_COMPARISON_$(subst /,__,$(path))))

$(VOLUME_40_READBACK_PATH_RAW): $(VOLUME_40_FINAL_GENERATED_ROOT) | $(VOLUME_40_READBACK_PATH_ROOT)
	@find "$(VOLUME_40_FINAL_GENERATED_ROOT)" -type f -printf '%P\n' >"$@.tmp"
	@mv "$@.tmp" "$@"

$(VOLUME_40_READBACK_PATH_SORTED): $(VOLUME_40_READBACK_PATH_RAW)
	@sort "$<" >"$@.tmp"
	@mv "$@.tmp" "$@"

$(VOLUME_40_READBACK_PATH_RECEIPT): $(VOLUME_40_INSTALL_PATH_CONTRACT) $(VOLUME_40_READBACK_PATH_SORTED) | $(VOLUME_40_READBACK_PATH_ROOT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.comparison.process "$<" "$(VOLUME_40_READBACK_PATH_SORTED)" >"$@.stdout" 2>"$@.stderr"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.stderr" >&2; exit "$$status"; fi; \
	printf 'exact_install_path_set,34\n' >"$@"

$(VOLUME_40_READBACK_HASH_RECEIPT): $(VOLUME_40_FINAL_GENERATED_ROOT)/sha256sums.txt $(VOLUME_40_FINAL_GENERATED_ROOT) | $(VOLUME_40_READBACK_ROOT)
	@cd "$(VOLUME_40_FINAL_GENERATED_ROOT)" && sha256sum --check sha256sums.txt >"$@.tmp" 2>"$@.stderr"
	@mv "$@.tmp" "$@"

define VOLUME_40_COVERAGE_RULE
VOLUME_40_MANIFEST_COVERAGE_$(subst /,__,$(1)) := $(VOLUME_40_READBACK_COVERAGE_ROOT)/manifest__$(subst /,__,$(1)).validated
$$(VOLUME_40_MANIFEST_COVERAGE_$(subst /,__,$(1))): $(VOLUME_40_FINAL_GENERATED_ROOT)/manifest.json | $(VOLUME_40_READBACK_COVERAGE_ROOT)
	@rg -F "$(1)" "$$<" >"$$@.tmp"
	@mv "$$@.tmp" "$$@"

VOLUME_40_HASH_COVERAGE_$(subst /,__,$(1)) := $(VOLUME_40_READBACK_COVERAGE_ROOT)/hash__$(subst /,__,$(1)).validated
$$(VOLUME_40_HASH_COVERAGE_$(subst /,__,$(1))): $(VOLUME_40_FINAL_GENERATED_ROOT)/sha256sums.txt | $(VOLUME_40_READBACK_COVERAGE_ROOT)
	@rg -F "$(1)" "$$<" >"$$@.tmp"
	@mv "$$@.tmp" "$$@"
endef

$(foreach path,$(VOLUME_40_MANIFEST_COVERAGE_RELATIVE),$(eval $(call VOLUME_40_COVERAGE_RULE,$(path))))
VOLUME_40_MANIFEST_COVERAGE_RECEIPTS := $(foreach path,$(VOLUME_40_MANIFEST_COVERAGE_RELATIVE),$(VOLUME_40_MANIFEST_COVERAGE_$(subst /,__,$(path))))
VOLUME_40_HASH_COVERAGE_RECEIPTS := $(foreach path,$(VOLUME_40_PREHASH_RELATIVE),$(VOLUME_40_HASH_COVERAGE_$(subst /,__,$(path))))

define VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RULE
VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_$(subst /,__,$(1)) := $(VOLUME_40_READBACK_COVERAGE_ROOT)/source-to-fragment__$(subst /,__,$(1)).validated
$$(VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_$(subst /,__,$(1))): $(VOLUME_40_FINAL_GENERATED_ROOT)/source_to_fragment.csv | $(VOLUME_40_READBACK_COVERAGE_ROOT)
	@rg -F "$(1)" "$$<" >"$$@.tmp"
	@mv "$$@.tmp" "$$@"
endef

$(foreach path,$(VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RELATIVE),$(eval $(call VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RULE,$(path))))
VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RECEIPTS := $(foreach path,$(VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RELATIVE),$(VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_$(subst /,__,$(path))))

volume-40-readback: \
	volume-40-bindings \
	volume-40-strict-source-body \
	$(VOLUME_40_FINAL_GENERATED_ROOT) \
	$(VOLUME_40_COMPARISON_RECEIPTS) \
	$(VOLUME_40_READBACK_PATH_RECEIPT) \
	$(VOLUME_40_READBACK_HASH_RECEIPT) \
	$(VOLUME_40_MANIFEST_COVERAGE_RECEIPTS) \
	$(VOLUME_40_SOURCE_TO_FRAGMENT_COVERAGE_RECEIPTS) \
	$(VOLUME_40_HASH_COVERAGE_RECEIPTS)
	@printf 'Volume 40 install/readback contract: GREEN\n'
