include make/morphism/codebase/volume/table/aggregate/file.mk
include make/morphism/codebase/volume/table/aggregate/source_files.mk
include make/morphism/codebase/volume/table/aggregate/gdb_evidence.mk
include make/morphism/codebase/volume/table/aggregate/ring_families.mk
include make/morphism/codebase/volume/table/aggregate/shared_components.mk
include make/morphism/codebase/volume/table/aggregate/shared_anchors.mk

.PHONY: morphism-codebase-volume-table-aggregates
morphism-codebase-volume-table-aggregates: \
	morphism-codebase-volume-table-source-files-aggregate \
	morphism-codebase-volume-table-gdb-evidence-aggregate \
	morphism-codebase-volume-table-ring-families-aggregate \
	morphism-codebase-volume-table-shared-components-aggregate \
	morphism-codebase-volume-table-shared-anchors-aggregate
