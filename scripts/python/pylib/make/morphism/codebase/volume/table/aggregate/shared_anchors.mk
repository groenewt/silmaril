VOLUME_SHARED_ANCHORS_ROW_FILES ?=
VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT := $(MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT)/shared_anchors/aggregate
VOLUME_SHARED_ANCHORS_PARSE := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/parse.carrier
VOLUME_SHARED_ANCHORS_SOURCE_ANNOTATION := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/source-annotation.carrier
VOLUME_SHARED_ANCHORS_GROUP_AGGREGATE := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/group-aggregate.carrier
VOLUME_SHARED_ANCHORS_SHAPE_VALIDATION := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/shape-validation.carrier
VOLUME_SHARED_ANCHORS_REQUIRED_KEY := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/required-key.carrier
VOLUME_SHARED_ANCHORS_REQUIRED_SET_UNIQUENESS := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/required-set-uniqueness.carrier
VOLUME_SHARED_ANCHORS_REQUIRED_SET_ORDER := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/required-set-order.carrier
VOLUME_SHARED_ANCHORS_REQUIRED_REFERENCE_ORDER := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/required-reference-order.carrier
VOLUME_SHARED_ANCHORS_REQUIRED_SET_VALIDATION := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/required-set-validation.carrier
VOLUME_SHARED_ANCHORS_REQUIRED_RESULT := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/required-result.carrier
VOLUME_SHARED_ANCHORS_UNIQUENESS_IDENTITY := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/uniqueness-identity.carrier
VOLUME_SHARED_ANCHORS_UNIQUENESS_VALIDATION := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/uniqueness-validation.carrier
VOLUME_SHARED_ANCHORS_UNIQUENESS_RESULT := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/uniqueness-result.carrier
VOLUME_SHARED_ANCHORS_ROW_PROJECTION := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/row-projection.carrier
VOLUME_SHARED_ANCHORS_ORDER_NUMERIC_NORMALIZATION := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/order-numeric-normalization.carrier
VOLUME_SHARED_ANCHORS_ORDER_KEY := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/order-key.carrier
VOLUME_SHARED_ANCHORS_ORDER := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/order.carrier
VOLUME_SHARED_ANCHORS_ORDER_RESULT := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/order-result.carrier
VOLUME_SHARED_ANCHORS_HEADER := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/header.carrier
VOLUME_SHARED_ANCHORS_CSV := $(VOLUME_SHARED_ANCHORS_AGGREGATE_ROOT)/shared_anchors.csv

.PHONY: morphism-codebase-volume-table-shared-anchors-aggregate
morphism-codebase-volume-table-shared-anchors-aggregate: $(VOLUME_SHARED_ANCHORS_CSV)

$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_NAMED_INPUT_EDGE,$(VOLUME_SHARED_ANCHORS_PARSE),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.parse.process,$(VOLUME_SHARED_ANCHORS_ROW_FILES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_SOURCE_ANNOTATION),$(VOLUME_SHARED_ANCHORS_PARSE),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.source.annotation.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_GROUP_AGGREGATE),$(VOLUME_SHARED_ANCHORS_SOURCE_ANNOTATION),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.group.aggregate.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_SHAPE_VALIDATION),$(VOLUME_SHARED_ANCHORS_GROUP_AGGREGATE),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.shape.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_REQUIRED_KEY),$(VOLUME_SHARED_ANCHORS_SHAPE_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.required.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_REQUIRED_SET_UNIQUENESS),$(VOLUME_SHARED_ANCHORS_REQUIRED_KEY),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.required.set.uniqueness.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_REQUIRED_SET_ORDER),$(VOLUME_SHARED_ANCHORS_REQUIRED_SET_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.required.set.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_REQUIRED_REFERENCE_ORDER),$(VOLUME_SHARED_ANCHORS_REQUIRED_SET_ORDER),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.required.reference.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_REQUIRED_SET_VALIDATION),$(VOLUME_SHARED_ANCHORS_REQUIRED_REFERENCE_ORDER),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.required.set.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_REQUIRED_RESULT),$(VOLUME_SHARED_ANCHORS_REQUIRED_SET_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.required.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_UNIQUENESS_IDENTITY),$(VOLUME_SHARED_ANCHORS_REQUIRED_RESULT),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.uniqueness.identity.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_UNIQUENESS_VALIDATION),$(VOLUME_SHARED_ANCHORS_UNIQUENESS_IDENTITY),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_UNIQUENESS_RESULT),$(VOLUME_SHARED_ANCHORS_UNIQUENESS_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.uniqueness.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_ROW_PROJECTION),$(VOLUME_SHARED_ANCHORS_UNIQUENESS_RESULT),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.row.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_ORDER_NUMERIC_NORMALIZATION),$(VOLUME_SHARED_ANCHORS_ROW_PROJECTION),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.order.numeric.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_ORDER_KEY),$(VOLUME_SHARED_ANCHORS_ORDER_NUMERIC_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_ORDER),$(VOLUME_SHARED_ANCHORS_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_ORDER_RESULT),$(VOLUME_SHARED_ANCHORS_ORDER),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_HEADER),$(VOLUME_SHARED_ANCHORS_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.header.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_SHARED_ANCHORS_CSV),$(VOLUME_SHARED_ANCHORS_HEADER),silmaril.sparky.morphism.codebase.volume.table.shared_anchors.aggregate.csv.encode.process))
