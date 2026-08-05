SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/inventory/catalog-gaps
VOLUME_INVENTORY_CATALOG_GAPS_CARRIER := $(VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT)/relation.duckdb
VOLUME_INVENTORY_CATALOG_GAPS_PROJECTED := $(VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT)/projection.receipt
VOLUME_INVENTORY_CATALOG_GAPS_ORDERED := $(VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT)/canonical-order.receipt
VOLUME_INVENTORY_CATALOG_GAPS_CSV ?= $(VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT)/catalog_gaps.csv

.PHONY: volume-inventory-catalog-gaps volume-inventory-catalog-gaps-force
volume-inventory-catalog-gaps: $(VOLUME_INVENTORY_CATALOG_GAPS_CSV)

volume-inventory-catalog-gaps-force:

$(VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT):
	mkdir -p "$@"

$(VOLUME_INVENTORY_CATALOG_GAPS_CARRIER): volume-inventory-catalog-gaps-force | $(VOLUME_INVENTORY_CATALOG_GAPS_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$(VOLUME_REPOSITORY)" || { printf '%s\n' 'VOLUME_REPOSITORY is required' >&2; exit 64; }
	@rm -f "$@.tmp" "$@.stdout" "$@.error"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_gaps.source.parse.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $@).tmp" >"$@.stdout" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.stdout" "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_INVENTORY_CATALOG_GAPS_PROJECTED): $(VOLUME_INVENTORY_CATALOG_GAPS_CARRIER)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_gaps.projection.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $<)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_INVENTORY_CATALOG_GAPS_ORDERED): $(VOLUME_INVENTORY_CATALOG_GAPS_PROJECTED)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_gaps.canonical_order.projection.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $(VOLUME_INVENTORY_CATALOG_GAPS_CARRIER))" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_INVENTORY_CATALOG_GAPS_CSV): $(VOLUME_INVENTORY_CATALOG_GAPS_ORDERED)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_gaps.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $(VOLUME_INVENTORY_CATALOG_GAPS_CARRIER))" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"
