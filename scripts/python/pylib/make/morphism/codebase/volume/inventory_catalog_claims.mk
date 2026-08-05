SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/inventory/catalog-claims
VOLUME_INVENTORY_CATALOG_CLAIMS_CARRIER := $(VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT)/relation.duckdb
VOLUME_INVENTORY_CATALOG_CLAIMS_PROJECTED := $(VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT)/projection.receipt
VOLUME_INVENTORY_CATALOG_CLAIMS_ORDERED := $(VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT)/canonical-order.receipt
VOLUME_INVENTORY_CATALOG_CLAIMS_CSV ?= $(VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT)/catalog_claims.csv

.PHONY: volume-inventory-catalog-claims volume-inventory-catalog-claims-force
volume-inventory-catalog-claims: $(VOLUME_INVENTORY_CATALOG_CLAIMS_CSV)

volume-inventory-catalog-claims-force:

$(VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT):
	mkdir -p "$@"

$(VOLUME_INVENTORY_CATALOG_CLAIMS_CARRIER): volume-inventory-catalog-claims-force | $(VOLUME_INVENTORY_CATALOG_CLAIMS_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$(VOLUME_REPOSITORY)" || { printf '%s\n' 'VOLUME_REPOSITORY is required' >&2; exit 64; }
	@rm -f "$@.tmp" "$@.stdout" "$@.error"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_claims.source.parse.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $@).tmp" >"$@.stdout" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.stdout" "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_INVENTORY_CATALOG_CLAIMS_PROJECTED): $(VOLUME_INVENTORY_CATALOG_CLAIMS_CARRIER)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_claims.projection.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $<)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_INVENTORY_CATALOG_CLAIMS_ORDERED): $(VOLUME_INVENTORY_CATALOG_CLAIMS_PROJECTED)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_claims.canonical_order.projection.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $(VOLUME_INVENTORY_CATALOG_CLAIMS_CARRIER))" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_INVENTORY_CATALOG_CLAIMS_CSV): $(VOLUME_INVENTORY_CATALOG_CLAIMS_ORDERED)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(abspath $(SILMARIL_PYLIB_SOURCE_ROOT))" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.inventory.catalog_claims.process "$(abspath $(VOLUME_REPOSITORY))" "$(abspath $(VOLUME_INVENTORY_CATALOG_CLAIMS_CARRIER))" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"
