SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_TABLE_HEADER_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/table-header
VOLUME_TABLE_HEADER_00_FRAME := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/00-input-frame.carrier
VOLUME_TABLE_HEADER_01_PATH_PRESENT := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/01-path-present.carrier
VOLUME_TABLE_HEADER_02_INVENTORY_ID_PRESENT := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/02-inventory-id-present.carrier
VOLUME_TABLE_HEADER_03_EXPECTED_HEADER_PRESENT := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/03-expected-header-present.carrier
VOLUME_TABLE_HEADER_04_FILE_EXISTS := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/04-file-exists.carrier
VOLUME_TABLE_HEADER_05_FIRST_LINE := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/05-first-line.carrier
VOLUME_TABLE_HEADER_06_NORMALIZED := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/06-normalized.carrier
VOLUME_TABLE_HEADER_07_VALIDATED := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/07-validated.carrier
VOLUME_TABLE_HEADER_08_RECEIPT := $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/08-receipt.carrier
VOLUME_TABLE_HEADER_RECEIPT ?= $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)/table_header_receipt.csv

.PHONY: volume-table-header volume-table-header-force
volume-table-header: $(VOLUME_TABLE_HEADER_RECEIPT)

volume-table-header-force:

$(VOLUME_TABLE_HEADER_OUTPUT_ROOT):
	mkdir -p "$@"

$(VOLUME_TABLE_HEADER_00_FRAME): volume-table-header-force | $(VOLUME_TABLE_HEADER_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.verification.table_header.input.frame.process "$(VOLUME_TABLE_HEADER_CSV)" "$(VOLUME_TABLE_HEADER_INVENTORY_ID)" "$(VOLUME_TABLE_HEADER_EXPECTED)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

define VOLUME_TABLE_HEADER_STAGE
$(1): $(2)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m $(3) <"$$<" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; \
	rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_01_PATH_PRESENT),$(VOLUME_TABLE_HEADER_00_FRAME),silmaril.sparky.morphism.codebase.volume.verification.table_header.path.presence.validation.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_02_INVENTORY_ID_PRESENT),$(VOLUME_TABLE_HEADER_01_PATH_PRESENT),silmaril.sparky.morphism.codebase.volume.verification.table_header.inventory_id.presence.validation.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_03_EXPECTED_HEADER_PRESENT),$(VOLUME_TABLE_HEADER_02_INVENTORY_ID_PRESENT),silmaril.sparky.morphism.codebase.volume.verification.table_header.expected_header.presence.validation.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_04_FILE_EXISTS),$(VOLUME_TABLE_HEADER_03_EXPECTED_HEADER_PRESENT),silmaril.sparky.morphism.codebase.volume.verification.table_header.file.existence.validation.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_05_FIRST_LINE),$(VOLUME_TABLE_HEADER_04_FILE_EXISTS),silmaril.sparky.morphism.codebase.volume.verification.table_header.first_line.read.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_06_NORMALIZED),$(VOLUME_TABLE_HEADER_05_FIRST_LINE),silmaril.sparky.morphism.codebase.volume.verification.table_header.newline.normalization.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_07_VALIDATED),$(VOLUME_TABLE_HEADER_06_NORMALIZED),silmaril.sparky.morphism.codebase.volume.verification.table_header.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_08_RECEIPT),$(VOLUME_TABLE_HEADER_07_VALIDATED),silmaril.sparky.morphism.codebase.volume.verification.table_header.receipt.construction.process))
$(eval $(call VOLUME_TABLE_HEADER_STAGE,$(VOLUME_TABLE_HEADER_RECEIPT),$(VOLUME_TABLE_HEADER_08_RECEIPT),silmaril.sparky.morphism.codebase.volume.verification.table_header.encode.process))
