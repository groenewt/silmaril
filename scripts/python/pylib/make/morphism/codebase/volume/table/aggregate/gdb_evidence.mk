VOLUME_GDB_EVIDENCE_ROW_FILES ?=
VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT := $(MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT)/gdb_evidence/aggregate
VOLUME_GDB_EVIDENCE_PARSE := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/parse.carrier
VOLUME_GDB_EVIDENCE_SOURCE_ANNOTATION := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/source-annotation.carrier
VOLUME_GDB_EVIDENCE_GROUP_AGGREGATE := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/group-aggregate.carrier
VOLUME_GDB_EVIDENCE_SHAPE_VALIDATION := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/shape-validation.carrier
VOLUME_GDB_EVIDENCE_REQUIRED_KEY := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/required-key.carrier
VOLUME_GDB_EVIDENCE_REQUIRED_SET_UNIQUENESS := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/required-set-uniqueness.carrier
VOLUME_GDB_EVIDENCE_REQUIRED_SET_ORDER := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/required-set-order.carrier
VOLUME_GDB_EVIDENCE_REQUIRED_REFERENCE_ORDER := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/required-reference-order.carrier
VOLUME_GDB_EVIDENCE_REQUIRED_SET_VALIDATION := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/required-set-validation.carrier
VOLUME_GDB_EVIDENCE_REQUIRED_RESULT := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/required-result.carrier
VOLUME_GDB_EVIDENCE_UNIQUENESS_IDENTITY := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/uniqueness-identity.carrier
VOLUME_GDB_EVIDENCE_UNIQUENESS_VALIDATION := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/uniqueness-validation.carrier
VOLUME_GDB_EVIDENCE_UNIQUENESS_RESULT := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/uniqueness-result.carrier
VOLUME_GDB_EVIDENCE_ROW_PROJECTION := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/row-projection.carrier
VOLUME_GDB_EVIDENCE_ORDER_NUMERIC_NORMALIZATION := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/order-numeric-normalization.carrier
VOLUME_GDB_EVIDENCE_ORDER_KEY := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/order-key.carrier
VOLUME_GDB_EVIDENCE_ORDER := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/order.carrier
VOLUME_GDB_EVIDENCE_ORDER_RESULT := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/order-result.carrier
VOLUME_GDB_EVIDENCE_HEADER := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/header.carrier
VOLUME_GDB_EVIDENCE_CSV := $(VOLUME_GDB_EVIDENCE_AGGREGATE_ROOT)/gdb_evidence.csv

.PHONY: morphism-codebase-volume-table-gdb-evidence-aggregate
morphism-codebase-volume-table-gdb-evidence-aggregate: $(VOLUME_GDB_EVIDENCE_CSV)

$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_NAMED_INPUT_EDGE,$(VOLUME_GDB_EVIDENCE_PARSE),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.parse.process,$(VOLUME_GDB_EVIDENCE_ROW_FILES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_SOURCE_ANNOTATION),$(VOLUME_GDB_EVIDENCE_PARSE),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.source.annotation.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_GROUP_AGGREGATE),$(VOLUME_GDB_EVIDENCE_SOURCE_ANNOTATION),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.group.aggregate.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_SHAPE_VALIDATION),$(VOLUME_GDB_EVIDENCE_GROUP_AGGREGATE),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.shape.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_REQUIRED_KEY),$(VOLUME_GDB_EVIDENCE_SHAPE_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.required.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_REQUIRED_SET_UNIQUENESS),$(VOLUME_GDB_EVIDENCE_REQUIRED_KEY),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.required.set.uniqueness.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_REQUIRED_SET_ORDER),$(VOLUME_GDB_EVIDENCE_REQUIRED_SET_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.required.set.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_REQUIRED_REFERENCE_ORDER),$(VOLUME_GDB_EVIDENCE_REQUIRED_SET_ORDER),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.required.reference.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_REQUIRED_SET_VALIDATION),$(VOLUME_GDB_EVIDENCE_REQUIRED_REFERENCE_ORDER),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.required.set.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_REQUIRED_RESULT),$(VOLUME_GDB_EVIDENCE_REQUIRED_SET_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.required.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_UNIQUENESS_IDENTITY),$(VOLUME_GDB_EVIDENCE_REQUIRED_RESULT),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.uniqueness.identity.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_UNIQUENESS_VALIDATION),$(VOLUME_GDB_EVIDENCE_UNIQUENESS_IDENTITY),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_UNIQUENESS_RESULT),$(VOLUME_GDB_EVIDENCE_UNIQUENESS_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.uniqueness.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_ROW_PROJECTION),$(VOLUME_GDB_EVIDENCE_UNIQUENESS_RESULT),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.row.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_ORDER_NUMERIC_NORMALIZATION),$(VOLUME_GDB_EVIDENCE_ROW_PROJECTION),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.order.numeric.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_ORDER_KEY),$(VOLUME_GDB_EVIDENCE_ORDER_NUMERIC_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_ORDER),$(VOLUME_GDB_EVIDENCE_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_ORDER_RESULT),$(VOLUME_GDB_EVIDENCE_ORDER),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_HEADER),$(VOLUME_GDB_EVIDENCE_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.header.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_TABLE_EDGE,$(VOLUME_GDB_EVIDENCE_CSV),$(VOLUME_GDB_EVIDENCE_HEADER),silmaril.sparky.morphism.codebase.volume.table.gdb_evidence.aggregate.csv.encode.process))
