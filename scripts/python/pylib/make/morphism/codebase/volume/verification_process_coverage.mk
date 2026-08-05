SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/process-coverage
VOLUME_PROCESS_COVERAGE_00_FRAME := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/00-input-frame.carrier
VOLUME_PROCESS_COVERAGE_01_ACCEPTED_EXISTS := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/01-accepted-exists.carrier
VOLUME_PROCESS_COVERAGE_02_MATERIALIZED_EXISTS := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/02-materialized-exists.carrier
VOLUME_PROCESS_COVERAGE_03_ACCEPTED_PARSED := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/03-accepted-parsed.carrier
VOLUME_PROCESS_COVERAGE_04_MATERIALIZED_PARSED := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/04-materialized-parsed.carrier
VOLUME_PROCESS_COVERAGE_05_ACCEPTED_INDEX := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/05-accepted-coordinate-index.carrier
VOLUME_PROCESS_COVERAGE_06_ACCEPTED_HEADER := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/06-accepted-coordinate-header.carrier
VOLUME_PROCESS_COVERAGE_07_ACCEPTED_COORDINATES := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/07-accepted-coordinates.carrier
VOLUME_PROCESS_COVERAGE_08_MATERIALIZED_INDEX := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/08-materialized-coordinate-index.carrier
VOLUME_PROCESS_COVERAGE_09_MATERIALIZED_HEADER := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/09-materialized-coordinate-header.carrier
VOLUME_PROCESS_COVERAGE_10_MATERIALIZED_COORDINATES := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/10-materialized-coordinates.carrier
VOLUME_PROCESS_COVERAGE_11_ACCEPTED_UNIQUE_PROJECTION := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/11-accepted-unique-projection.carrier
VOLUME_PROCESS_COVERAGE_12_ACCEPTED_UNIQUE_VALIDATION := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/12-accepted-unique-validation.carrier
VOLUME_PROCESS_COVERAGE_13_MATERIALIZED_UNIQUE_PROJECTION := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/13-materialized-unique-projection.carrier
VOLUME_PROCESS_COVERAGE_14_MATERIALIZED_UNIQUE_VALIDATION := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/14-materialized-unique-validation.carrier
VOLUME_PROCESS_COVERAGE_15_ACCEPTED_ORDERED := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/15-accepted-ordered.carrier
VOLUME_PROCESS_COVERAGE_16_MATERIALIZED_ORDERED := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/16-materialized-ordered.carrier
VOLUME_PROCESS_COVERAGE_17_MATCHED := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/17-matched.carrier
VOLUME_PROCESS_COVERAGE_18_ACCEPTED_CARDINALITY := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/18-accepted-cardinality.carrier
VOLUME_PROCESS_COVERAGE_19_RESULT := $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/19-result.carrier
VOLUME_PROCESS_COVERAGE ?= $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)/process_coverage.csv

.PHONY: volume-process-coverage volume-process-coverage-force
volume-process-coverage: $(VOLUME_PROCESS_COVERAGE)

volume-process-coverage-force:

$(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT):
	mkdir -p "$@"

$(VOLUME_PROCESS_COVERAGE_00_FRAME): volume-process-coverage-force | $(VOLUME_PROCESS_COVERAGE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$(VOLUME_ACCEPTED_PROCESS_INVENTORY)" || { printf '%s\n' 'VOLUME_ACCEPTED_PROCESS_INVENTORY is required' >&2; exit 64; }
	@test -n "$(VOLUME_MATERIALIZED_PROCESS_COORDINATES)" || { printf '%s\n' 'VOLUME_MATERIALIZED_PROCESS_COORDINATES is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.verification.process_coverage.input.frame.process "$(abspath $(VOLUME_ACCEPTED_PROCESS_INVENTORY))" "$(abspath $(VOLUME_MATERIALIZED_PROCESS_COORDINATES))" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

define VOLUME_PROCESS_COVERAGE_STAGE
$(1): $(2)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m $(3) <"$$<" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; \
	rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_01_ACCEPTED_EXISTS),$(VOLUME_PROCESS_COVERAGE_00_FRAME),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.existence.validation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_02_MATERIALIZED_EXISTS),$(VOLUME_PROCESS_COVERAGE_01_ACCEPTED_EXISTS),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.existence.validation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_03_ACCEPTED_PARSED),$(VOLUME_PROCESS_COVERAGE_02_MATERIALIZED_EXISTS),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.parse.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_04_MATERIALIZED_PARSED),$(VOLUME_PROCESS_COVERAGE_03_ACCEPTED_PARSED),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.parse.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_05_ACCEPTED_INDEX),$(VOLUME_PROCESS_COVERAGE_04_MATERIALIZED_PARSED),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.coordinate.index.lookup.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_06_ACCEPTED_HEADER),$(VOLUME_PROCESS_COVERAGE_05_ACCEPTED_INDEX),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.coordinate.index.existence.validation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_07_ACCEPTED_COORDINATES),$(VOLUME_PROCESS_COVERAGE_06_ACCEPTED_HEADER),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.coordinate.projection.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_08_MATERIALIZED_INDEX),$(VOLUME_PROCESS_COVERAGE_07_ACCEPTED_COORDINATES),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.coordinate.index.lookup.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_09_MATERIALIZED_HEADER),$(VOLUME_PROCESS_COVERAGE_08_MATERIALIZED_INDEX),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.coordinate.index.existence.validation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_10_MATERIALIZED_COORDINATES),$(VOLUME_PROCESS_COVERAGE_09_MATERIALIZED_HEADER),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.coordinate.projection.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_11_ACCEPTED_UNIQUE_PROJECTION),$(VOLUME_PROCESS_COVERAGE_10_MATERIALIZED_COORDINATES),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.unique.projection.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_12_ACCEPTED_UNIQUE_VALIDATION),$(VOLUME_PROCESS_COVERAGE_11_ACCEPTED_UNIQUE_PROJECTION),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.uniqueness.validation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_13_MATERIALIZED_UNIQUE_PROJECTION),$(VOLUME_PROCESS_COVERAGE_12_ACCEPTED_UNIQUE_VALIDATION),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.unique.projection.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_14_MATERIALIZED_UNIQUE_VALIDATION),$(VOLUME_PROCESS_COVERAGE_13_MATERIALIZED_UNIQUE_PROJECTION),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.uniqueness.validation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_15_ACCEPTED_ORDERED),$(VOLUME_PROCESS_COVERAGE_14_MATERIALIZED_UNIQUE_VALIDATION),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.canonical_order.projection.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_16_MATERIALIZED_ORDERED),$(VOLUME_PROCESS_COVERAGE_15_ACCEPTED_ORDERED),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.materialized.canonical_order.projection.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_17_MATCHED),$(VOLUME_PROCESS_COVERAGE_16_MATERIALIZED_ORDERED),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_18_ACCEPTED_CARDINALITY),$(VOLUME_PROCESS_COVERAGE_17_MATCHED),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.accepted.cardinality.observation.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE_19_RESULT),$(VOLUME_PROCESS_COVERAGE_18_ACCEPTED_CARDINALITY),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.result.construction.process))
$(eval $(call VOLUME_PROCESS_COVERAGE_STAGE,$(VOLUME_PROCESS_COVERAGE),$(VOLUME_PROCESS_COVERAGE_19_RESULT),silmaril.sparky.morphism.codebase.volume.verification.process_coverage.encode.process))
