VOLUME_EVIDENCE_ROWS_ORDER_INPUT ?=
VOLUME_EVIDENCE_ROWS_ORDER_ROOT ?= $(MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT)/evidence_rows/order
VOLUME_EVIDENCE_ROWS_RING_ORDER_VALUE_NORMALIZATION := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/ring-value-normalization.carrier
VOLUME_EVIDENCE_ROWS_RING_ORDER_KEY := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/ring-key-projection.carrier
VOLUME_EVIDENCE_ROWS_RING_ORDER_ORDER := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/ring-order-projection.carrier
VOLUME_EVIDENCE_ROWS_RING_ORDER_RESULT := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/ring-result-projection.carrier
VOLUME_EVIDENCE_ROWS_TEXT_ORDER_VALUE_NORMALIZATION := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/text-value-normalization.carrier
VOLUME_EVIDENCE_ROWS_TEXT_ORDER_KEY := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/text-key-projection.carrier
VOLUME_EVIDENCE_ROWS_TEXT_ORDER_ORDER := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/text-order-projection.carrier
VOLUME_EVIDENCE_ROWS_TEXT_ORDER_RESULT := $(VOLUME_EVIDENCE_ROWS_ORDER_ROOT)/text-result-projection.carrier

.PHONY: morphism-codebase-volume-table-evidence-rows-ring-order morphism-codebase-volume-table-evidence-rows-text-order
morphism-codebase-volume-table-evidence-rows-ring-order: $(VOLUME_EVIDENCE_ROWS_RING_ORDER_RESULT)
morphism-codebase-volume-table-evidence-rows-text-order: $(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_RESULT)

$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_RING_ORDER_VALUE_NORMALIZATION),$(VOLUME_EVIDENCE_ROWS_ORDER_INPUT),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.ring.value.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_RING_ORDER_KEY),$(VOLUME_EVIDENCE_ROWS_RING_ORDER_VALUE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.ring.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_RING_ORDER_ORDER),$(VOLUME_EVIDENCE_ROWS_RING_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_RING_ORDER_RESULT),$(VOLUME_EVIDENCE_ROWS_RING_ORDER_ORDER),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_VALUE_NORMALIZATION),$(VOLUME_EVIDENCE_ROWS_ORDER_INPUT),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.text.value.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_KEY),$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_VALUE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.text.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_ORDER),$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_RESULT),$(VOLUME_EVIDENCE_ROWS_TEXT_ORDER_ORDER),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.order.result.projection.process))
