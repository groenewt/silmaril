include make/morphism/codebase/volume/inventory_catalog_documents.mk
include make/morphism/codebase/volume/inventory_catalog_claims.mk
include make/morphism/codebase/volume/inventory_catalog_gaps.mk
include make/morphism/codebase/volume/inventory_catalog_quality_flags.mk

.PHONY: volume-inventory-catalogs
volume-inventory-catalogs: \
	volume-inventory-catalog-documents \
	volume-inventory-catalog-claims \
	volume-inventory-catalog-gaps \
	volume-inventory-catalog-quality-flags
