VOLUME_RING_FAMILIES_ROW_FILES ?=
VOLUME_RING_FAMILIES_AGGREGATE_ROOT := $(MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT)/ring_families/aggregate
VOLUME_RING_FAMILIES_PARSE := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/parse.carrier
VOLUME_RING_FAMILIES_SOURCE_ANNOTATION := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/source-annotation.carrier
VOLUME_RING_FAMILIES_GROUP_AGGREGATE := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/group-aggregate.carrier
VOLUME_RING_FAMILIES_SHAPE_VALIDATION := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/shape-validation.carrier
VOLUME_RING_FAMILIES_UNIQUENESS_IDENTITY := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/uniqueness-identity.carrier
VOLUME_RING_FAMILIES_UNIQUENESS_VALIDATION := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/uniqueness-validation.carrier
VOLUME_RING_FAMILIES_UNIQUENESS_RESULT := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/uniqueness-result.carrier
VOLUME_RING_FAMILIES_REQUIRED_KEY := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/required-key.carrier
VOLUME_RING_FAMILIES_REQUIRED_SET_UNIQUENESS := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/required-set-uniqueness.carrier
VOLUME_RING_FAMILIES_REQUIRED_SET_ORDER := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/required-set-order.carrier
VOLUME_RING_FAMILIES_REQUIRED_REFERENCE_ORDER := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/required-reference-order.carrier
VOLUME_RING_FAMILIES_REQUIRED_SET_VALIDATION := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/required-set-validation.carrier
VOLUME_RING_FAMILIES_REQUIRED_RESULT := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/required-result.carrier
VOLUME_RING_FAMILIES_ROW_PROJECTION := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/row-projection.carrier
VOLUME_RING_FAMILIES_ORDER_NUMERIC_NORMALIZATION := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/order-numeric-normalization.carrier
VOLUME_RING_FAMILIES_ORDER_KEY := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/order-key.carrier
VOLUME_RING_FAMILIES_ORDER := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/order.carrier
VOLUME_RING_FAMILIES_ORDER_RESULT := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/order-result.carrier
VOLUME_RING_FAMILIES_HEADER := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/header.carrier
VOLUME_RING_FAMILIES_CSV := $(VOLUME_RING_FAMILIES_AGGREGATE_ROOT)/ring_families.csv

.PHONY: morphism-codebase-volume-table-ring-families-aggregate
morphism-codebase-volume-table-ring-families-aggregate: $(VOLUME_RING_FAMILIES_CSV)

$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_NAMED_INPUT_EDGE,$(VOLUME_RING_FAMILIES_PARSE),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.parse.process,$(VOLUME_RING_FAMILIES_ROW_FILES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_SOURCE_ANNOTATION),$(VOLUME_RING_FAMILIES_PARSE),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.source.annotation.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_GROUP_AGGREGATE),$(VOLUME_RING_FAMILIES_SOURCE_ANNOTATION),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.group.aggregate.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_SHAPE_VALIDATION),$(VOLUME_RING_FAMILIES_GROUP_AGGREGATE),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.shape.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_UNIQUENESS_IDENTITY),$(VOLUME_RING_FAMILIES_SHAPE_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.uniqueness.identity.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_UNIQUENESS_VALIDATION),$(VOLUME_RING_FAMILIES_UNIQUENESS_IDENTITY),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_UNIQUENESS_RESULT),$(VOLUME_RING_FAMILIES_UNIQUENESS_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.uniqueness.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_REQUIRED_KEY),$(VOLUME_RING_FAMILIES_UNIQUENESS_RESULT),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.required.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_REQUIRED_SET_UNIQUENESS),$(VOLUME_RING_FAMILIES_REQUIRED_KEY),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.required.set.uniqueness.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_REQUIRED_SET_ORDER),$(VOLUME_RING_FAMILIES_REQUIRED_SET_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.required.set.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_REQUIRED_REFERENCE_ORDER),$(VOLUME_RING_FAMILIES_REQUIRED_SET_ORDER),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.required.reference.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_REQUIRED_SET_VALIDATION),$(VOLUME_RING_FAMILIES_REQUIRED_REFERENCE_ORDER),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.required.set.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_REQUIRED_RESULT),$(VOLUME_RING_FAMILIES_REQUIRED_SET_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.required.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_ROW_PROJECTION),$(VOLUME_RING_FAMILIES_REQUIRED_RESULT),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.row.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_ORDER_NUMERIC_NORMALIZATION),$(VOLUME_RING_FAMILIES_ROW_PROJECTION),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.order.numeric.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_ORDER_KEY),$(VOLUME_RING_FAMILIES_ORDER_NUMERIC_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_ORDER),$(VOLUME_RING_FAMILIES_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_ORDER_RESULT),$(VOLUME_RING_FAMILIES_ORDER),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_HEADER),$(VOLUME_RING_FAMILIES_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.header.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_RING_FAMILIES_CSV),$(VOLUME_RING_FAMILIES_HEADER),silmaril.sparky.morphism.codebase.volume.table.ring_families.aggregate.csv.encode.process))
