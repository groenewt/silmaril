VOLUME_SOURCE_FILES_LOCUS_INPUT ?=
VOLUME_SOURCE_FILES_LOCUS_ROOT ?= $(MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT)/source_files/locus
VOLUME_SOURCE_FILES_LOCUS_ROOT_PATHNAME := $(VOLUME_SOURCE_FILES_LOCUS_ROOT)/root-pathname.carrier
VOLUME_SOURCE_FILES_LOCUS_PATH_PATHNAME := $(VOLUME_SOURCE_FILES_LOCUS_ROOT)/path-pathname.carrier
VOLUME_SOURCE_FILES_LOCUS_JOIN := $(VOLUME_SOURCE_FILES_LOCUS_ROOT)/locus-projection.carrier
VOLUME_SOURCE_FILES_LOCUS_NORMALIZATION := $(VOLUME_SOURCE_FILES_LOCUS_ROOT)/locus-normalization.carrier
VOLUME_SOURCE_FILES_LOCUS_STRING := $(VOLUME_SOURCE_FILES_LOCUS_ROOT)/locus-string-projection.carrier

.PHONY: morphism-codebase-volume-table-source-files-locus
morphism-codebase-volume-table-source-files-locus: $(VOLUME_SOURCE_FILES_LOCUS_STRING)

$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_SOURCE_FILES_LOCUS_ROOT_PATHNAME),$(VOLUME_SOURCE_FILES_LOCUS_INPUT),silmaril.sparky.morphism.codebase.volume.table.source_files.root.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_SOURCE_FILES_LOCUS_PATH_PATHNAME),$(VOLUME_SOURCE_FILES_LOCUS_ROOT_PATHNAME),silmaril.sparky.morphism.codebase.volume.table.source_files.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_SOURCE_FILES_LOCUS_JOIN),$(VOLUME_SOURCE_FILES_LOCUS_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.table.source_files.locus.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_SOURCE_FILES_LOCUS_NORMALIZATION),$(VOLUME_SOURCE_FILES_LOCUS_JOIN),silmaril.sparky.morphism.codebase.volume.table.source_files.locus.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_SOURCE_FILES_LOCUS_STRING),$(VOLUME_SOURCE_FILES_LOCUS_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.source_files.locus.string.projection.process))
