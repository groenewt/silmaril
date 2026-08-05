VOLUME_SOURCE_FILES_ROW_FILES ?=
VOLUME_SOURCE_FILES_AGGREGATE_ROOT := $(MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT)/source_files/aggregate
VOLUME_SOURCE_FILES_PARSE := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/parse.carrier
VOLUME_SOURCE_FILES_SOURCE_ANNOTATION := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/source-annotation.carrier
VOLUME_SOURCE_FILES_GROUP_AGGREGATE := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/group-aggregate.carrier
VOLUME_SOURCE_FILES_SHAPE_VALIDATION := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/shape-validation.carrier
VOLUME_SOURCE_FILES_UNIQUENESS_IDENTITY := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/uniqueness-identity.carrier
VOLUME_SOURCE_FILES_UNIQUENESS_VALIDATION := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/uniqueness-validation.carrier
VOLUME_SOURCE_FILES_UNIQUENESS_RESULT := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/uniqueness-result.carrier
VOLUME_SOURCE_FILES_ROW_PROJECTION := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/row-projection.carrier
VOLUME_SOURCE_FILES_ORDER_KEY := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/order-key.carrier
VOLUME_SOURCE_FILES_ORDER := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/order.carrier
VOLUME_SOURCE_FILES_ORDER_RESULT := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/order-result.carrier
VOLUME_SOURCE_FILES_HEADER := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/header.carrier
VOLUME_SOURCE_FILES_CSV := $(VOLUME_SOURCE_FILES_AGGREGATE_ROOT)/source_files.csv

.PHONY: morphism-codebase-volume-table-source-files-aggregate
morphism-codebase-volume-table-source-files-aggregate: $(VOLUME_SOURCE_FILES_CSV)

$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_NAMED_INPUT_EDGE,$(VOLUME_SOURCE_FILES_PARSE),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.parse.process,$(VOLUME_SOURCE_FILES_ROW_FILES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_SOURCE_ANNOTATION),$(VOLUME_SOURCE_FILES_PARSE),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.source.annotation.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_GROUP_AGGREGATE),$(VOLUME_SOURCE_FILES_SOURCE_ANNOTATION),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.group.aggregate.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_SHAPE_VALIDATION),$(VOLUME_SOURCE_FILES_GROUP_AGGREGATE),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.shape.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_UNIQUENESS_IDENTITY),$(VOLUME_SOURCE_FILES_SHAPE_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.uniqueness.identity.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_UNIQUENESS_VALIDATION),$(VOLUME_SOURCE_FILES_UNIQUENESS_IDENTITY),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_UNIQUENESS_RESULT),$(VOLUME_SOURCE_FILES_UNIQUENESS_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.uniqueness.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_ROW_PROJECTION),$(VOLUME_SOURCE_FILES_UNIQUENESS_RESULT),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.row.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_ORDER_KEY),$(VOLUME_SOURCE_FILES_ROW_PROJECTION),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_ORDER),$(VOLUME_SOURCE_FILES_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_ORDER_RESULT),$(VOLUME_SOURCE_FILES_ORDER),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_HEADER),$(VOLUME_SOURCE_FILES_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.header.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SOURCE_FILES_CSV),$(VOLUME_SOURCE_FILES_HEADER),silmaril.sparky.morphism.codebase.volume.table.source_files.aggregate.csv.encode.process))
