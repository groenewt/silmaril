MORPHISM_CODEBASE_VOLUME_TABLE_CONSTRUCT_ROOT := $(MORPHISM_CODEBASE_VOLUME_OPERATION_ROOT)/table/construct

define VOLUME_TABLE_SINGLE_ORDER_PIPELINE
VOLUME_TABLE_$1_ORDER := $$(VOLUME_TABLE_$1_ROOT)/order-projection.carrier
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_ORDER),$$(VOLUME_TABLE_$1_DISTINCT),silmaril.sparky.morphism.codebase.volume.table.$3.construct.order.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_HEADER),$$(VOLUME_TABLE_$1_ORDER),silmaril.sparky.morphism.codebase.volume.table.$3.construct.header.projection.process))
endef

define VOLUME_TABLE_NUMERIC_ORDER_PIPELINE
VOLUME_TABLE_$1_ORDER_NUMERIC := $$(VOLUME_TABLE_$1_ROOT)/order-numeric-normalization.carrier
VOLUME_TABLE_$1_ORDER_KEY := $$(VOLUME_TABLE_$1_ROOT)/order-key-projection.carrier
VOLUME_TABLE_$1_ORDER := $$(VOLUME_TABLE_$1_ROOT)/order-projection.carrier
VOLUME_TABLE_$1_ORDER_RESULT := $$(VOLUME_TABLE_$1_ROOT)/order-result-projection.carrier
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_ORDER_NUMERIC),$$(VOLUME_TABLE_$1_DISTINCT),silmaril.sparky.morphism.codebase.volume.table.$3.construct.order.numeric.normalization.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_ORDER_KEY),$$(VOLUME_TABLE_$1_ORDER_NUMERIC),silmaril.sparky.morphism.codebase.volume.table.$3.construct.order.key.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_ORDER),$$(VOLUME_TABLE_$1_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.$3.construct.order.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_ORDER_RESULT),$$(VOLUME_TABLE_$1_ORDER),silmaril.sparky.morphism.codebase.volume.table.$3.construct.order.result.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_HEADER),$$(VOLUME_TABLE_$1_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.table.$3.construct.header.projection.process))
endef

define VOLUME_TABLE_COMMON_PIPELINE
VOLUME_TABLE_$1_ROOT := $$(MORPHISM_CODEBASE_VOLUME_TABLE_CONSTRUCT_ROOT)/$2
VOLUME_TABLE_$1_LINE := $$(VOLUME_TABLE_$1_ROOT)/input-line-parse.carrier
VOLUME_TABLE_$1_NEWLINE := $$(VOLUME_TABLE_$1_ROOT)/input-newline-normalization.carrier
VOLUME_TABLE_$1_PARSE := $$(VOLUME_TABLE_$1_ROOT)/input-record-parse.carrier
VOLUME_TABLE_$1_PATH := $$(VOLUME_TABLE_$1_ROOT)/input-path-normalization.carrier
VOLUME_TABLE_$1_MATCH := $$(VOLUME_TABLE_$1_ROOT)/match-parse.carrier
VOLUME_TABLE_$1_SELECTED := $$(VOLUME_TABLE_$1_ROOT)/match-presence-selection.carrier
VOLUME_TABLE_$1_ROW := $$(VOLUME_TABLE_$1_ROOT)/row-projection.carrier
VOLUME_TABLE_$1_DISTINCT := $$(VOLUME_TABLE_$1_ROOT)/distinct-selection.carrier
VOLUME_TABLE_$1_HEADER := $$(VOLUME_TABLE_$1_ROOT)/header-projection.carrier
VOLUME_TABLE_$1_CSV := $$(VOLUME_TABLE_$1_ROOT)/$2.csv
.PHONY: morphism-codebase-volume-table-$2
morphism-codebase-volume-table-$2: $$(VOLUME_TABLE_$1_CSV)
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_LINE),$$($4),silmaril.sparky.morphism.codebase.volume.table.$3.construct.input.line.parse.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_NEWLINE),$$(VOLUME_TABLE_$1_LINE),silmaril.sparky.morphism.codebase.volume.table.$3.construct.input.newline.normalization.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_PARSE),$$(VOLUME_TABLE_$1_NEWLINE),silmaril.sparky.morphism.codebase.volume.table.$3.construct.input.parse.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_PATH),$$(VOLUME_TABLE_$1_PARSE),silmaril.sparky.morphism.codebase.volume.table.$3.construct.input.path.normalization.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_MATCH),$$(VOLUME_TABLE_$1_PATH),silmaril.sparky.morphism.codebase.volume.table.$3.construct.match.parse.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_SELECTED),$$(VOLUME_TABLE_$1_MATCH),silmaril.sparky.morphism.codebase.volume.table.match.presence.selection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_ROW),$$(VOLUME_TABLE_$1_$5),silmaril.sparky.morphism.codebase.volume.table.$3.construct.row.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_DISTINCT),$$(VOLUME_TABLE_$1_$6),silmaril.sparky.morphism.codebase.volume.table.$3.construct.distinct.selection.process))
$(call VOLUME_TABLE_$7_ORDER_PIPELINE,$1,$2,$3)
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_CSV),$$(VOLUME_TABLE_$1_HEADER),silmaril.sparky.morphism.codebase.volume.table.$3.construct.csv.encode.process))
endef

VOLUME_TABLE_TESTS_INPUT ?=
VOLUME_TABLE_MAKE_TARGETS_INPUT ?=
VOLUME_TABLE_DOCUMENTATION_INPUT ?=
VOLUME_TABLE_MODULES_INPUT ?=
$(eval $(call VOLUME_TABLE_COMMON_PIPELINE,TESTS,tests,tests,VOLUME_TABLE_TESTS_INPUT,SELECTED,ROW,NUMERIC))
$(eval $(call VOLUME_TABLE_COMMON_PIPELINE,MAKE_TARGETS,make-targets,make_targets,VOLUME_TABLE_MAKE_TARGETS_INPUT,SELECTED,ROW,NUMERIC))
$(eval $(call VOLUME_TABLE_COMMON_PIPELINE,DOCUMENTATION,documentation,documentation,VOLUME_TABLE_DOCUMENTATION_INPUT,SELECTED,ROW,NUMERIC))
$(eval $(call VOLUME_TABLE_COMMON_PIPELINE,MODULES,modules,modules,VOLUME_TABLE_MODULES_INPUT,SELECTED,ROW,SINGLE))

define VOLUME_TABLE_DEPENDENCY_PIPELINE
VOLUME_TABLE_DEPENDENCIES_CLASSIFIED := $$(MORPHISM_CODEBASE_VOLUME_TABLE_CONSTRUCT_ROOT)/dependencies/ecosystem-classification.carrier
$(call VOLUME_TABLE_COMMON_PIPELINE,DEPENDENCIES,dependencies,dependencies,VOLUME_TABLE_DEPENDENCIES_INPUT,CLASSIFIED,ROW,NUMERIC)
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_DEPENDENCIES_CLASSIFIED),$$(VOLUME_TABLE_DEPENDENCIES_SELECTED),silmaril.sparky.morphism.codebase.volume.table.dependencies.construct.ecosystem.classification.process))
endef

VOLUME_TABLE_DEPENDENCIES_INPUT ?=
$(eval $(call VOLUME_TABLE_DEPENDENCY_PIPELINE))

define VOLUME_TABLE_TASK_PIPELINE
VOLUME_TABLE_$1_NORMALIZED := $$(MORPHISM_CODEBASE_VOLUME_TABLE_CONSTRUCT_ROOT)/$2/task-normalization.carrier
$(call VOLUME_TABLE_COMMON_PIPELINE,$1,$2,$3,$4,SELECTED,NORMALIZED,SINGLE)
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_TABLE_$1_NORMALIZED),$$(VOLUME_TABLE_$1_ROW),silmaril.sparky.morphism.codebase.volume.table.$3.construct.task.normalization.process))
endef

VOLUME_TABLE_PROJECT_TASKS_INPUT ?=
VOLUME_TABLE_MIX_TASKS_INPUT ?=
$(eval $(call VOLUME_TABLE_TASK_PIPELINE,PROJECT_TASKS,project-tasks,project_tasks,VOLUME_TABLE_PROJECT_TASKS_INPUT))
$(eval $(call VOLUME_TABLE_TASK_PIPELINE,MIX_TASKS,mix-tasks,mix_tasks,VOLUME_TABLE_MIX_TASKS_INPUT))

define VOLUME_TABLE_MATCH_FILTER_PIPELINE
$(call VOLUME_TABLE_COMMON_PIPELINE,$1,$2,$3,VOLUME_TABLE_$1_INPUT,SELECTED,ROW,$4)
endef

VOLUME_TABLE_NATIVE_TREE_INPUT ?=
VOLUME_TABLE_CONFIGURATION_INPUT ?=
$(eval $(call VOLUME_TABLE_MATCH_FILTER_PIPELINE,NATIVE_TREE,native-tree,native_tree,NUMERIC))
$(eval $(call VOLUME_TABLE_MATCH_FILTER_PIPELINE,CONFIGURATION,configuration,configuration,NUMERIC))

VOLUME_TABLE_PROVENANCE_INPUT ?=
VOLUME_TABLE_PROVENANCE_ROOT := $(MORPHISM_CODEBASE_VOLUME_TABLE_CONSTRUCT_ROOT)/provenance
VOLUME_TABLE_PROVENANCE_LINE := $(VOLUME_TABLE_PROVENANCE_ROOT)/input-line-parse.carrier
VOLUME_TABLE_PROVENANCE_NEWLINE := $(VOLUME_TABLE_PROVENANCE_ROOT)/input-newline-normalization.carrier
VOLUME_TABLE_PROVENANCE_PARSE := $(VOLUME_TABLE_PROVENANCE_ROOT)/input-record-parse.carrier
VOLUME_TABLE_PROVENANCE_PATH := $(VOLUME_TABLE_PROVENANCE_ROOT)/input-path-normalization.carrier
VOLUME_TABLE_PROVENANCE_DECLARATION := $(VOLUME_TABLE_PROVENANCE_ROOT)/declaration-parse.carrier
VOLUME_TABLE_PROVENANCE_INDEX := $(VOLUME_TABLE_PROVENANCE_ROOT)/subject-index.carrier
VOLUME_TABLE_PROVENANCE_RELATION := $(VOLUME_TABLE_PROVENANCE_ROOT)/relation-parse.carrier
VOLUME_TABLE_PROVENANCE_SELECTED := $(VOLUME_TABLE_PROVENANCE_ROOT)/relation-filter.carrier
VOLUME_TABLE_PROVENANCE_DISTINCT := $(VOLUME_TABLE_PROVENANCE_ROOT)/distinct-selection.carrier
VOLUME_TABLE_PROVENANCE_ORDER_NUMERIC := $(VOLUME_TABLE_PROVENANCE_ROOT)/order-numeric-normalization.carrier
VOLUME_TABLE_PROVENANCE_ORDER_KEY := $(VOLUME_TABLE_PROVENANCE_ROOT)/order-key-projection.carrier
VOLUME_TABLE_PROVENANCE_ORDER := $(VOLUME_TABLE_PROVENANCE_ROOT)/order-projection.carrier
VOLUME_TABLE_PROVENANCE_ORDER_RESULT := $(VOLUME_TABLE_PROVENANCE_ROOT)/order-result-projection.carrier
VOLUME_TABLE_PROVENANCE_HEADER := $(VOLUME_TABLE_PROVENANCE_ROOT)/header-projection.carrier
VOLUME_TABLE_PROVENANCE_CSV := $(VOLUME_TABLE_PROVENANCE_ROOT)/provenance.csv
.PHONY: morphism-codebase-volume-table-provenance
morphism-codebase-volume-table-provenance: $(VOLUME_TABLE_PROVENANCE_CSV)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_LINE),$(VOLUME_TABLE_PROVENANCE_INPUT),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.input.line.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_NEWLINE),$(VOLUME_TABLE_PROVENANCE_LINE),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.input.newline.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_PARSE),$(VOLUME_TABLE_PROVENANCE_NEWLINE),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.input.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_PATH),$(VOLUME_TABLE_PROVENANCE_PARSE),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.input.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_DECLARATION),$(VOLUME_TABLE_PROVENANCE_PATH),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.declaration.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_INDEX),$(VOLUME_TABLE_PROVENANCE_DECLARATION),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.subject.index.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_RELATION),$(VOLUME_TABLE_PROVENANCE_INDEX),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.relation.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_SELECTED),$(VOLUME_TABLE_PROVENANCE_RELATION),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.relation.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_DISTINCT),$(VOLUME_TABLE_PROVENANCE_SELECTED),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.distinct.selection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_ORDER_NUMERIC),$(VOLUME_TABLE_PROVENANCE_DISTINCT),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.order.numeric.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_ORDER_KEY),$(VOLUME_TABLE_PROVENANCE_ORDER_NUMERIC),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_ORDER),$(VOLUME_TABLE_PROVENANCE_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_ORDER_RESULT),$(VOLUME_TABLE_PROVENANCE_ORDER),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_HEADER),$(VOLUME_TABLE_PROVENANCE_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.header.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_PROVENANCE_CSV),$(VOLUME_TABLE_PROVENANCE_HEADER),silmaril.sparky.morphism.codebase.volume.table.provenance.construct.csv.encode.process))

VOLUME_TABLE_SCRIPTS_INPUT ?=
VOLUME_TABLE_SCRIPTS_ROOT := $(MORPHISM_CODEBASE_VOLUME_TABLE_CONSTRUCT_ROOT)/scripts
VOLUME_TABLE_SCRIPTS_LINE := $(VOLUME_TABLE_SCRIPTS_ROOT)/input-line-parse.carrier
VOLUME_TABLE_SCRIPTS_NEWLINE := $(VOLUME_TABLE_SCRIPTS_ROOT)/input-newline-normalization.carrier
VOLUME_TABLE_SCRIPTS_PATH := $(VOLUME_TABLE_SCRIPTS_ROOT)/path-normalization.carrier
VOLUME_TABLE_SCRIPTS_NONEMPTY := $(VOLUME_TABLE_SCRIPTS_ROOT)/nonempty-selection.carrier
VOLUME_TABLE_SCRIPTS_DISTINCT := $(VOLUME_TABLE_SCRIPTS_ROOT)/distinct-selection.carrier
VOLUME_TABLE_SCRIPTS_ROW := $(VOLUME_TABLE_SCRIPTS_ROOT)/row-projection.carrier
VOLUME_TABLE_SCRIPTS_ORDER := $(VOLUME_TABLE_SCRIPTS_ROOT)/order-projection.carrier
VOLUME_TABLE_SCRIPTS_HEADER := $(VOLUME_TABLE_SCRIPTS_ROOT)/header-projection.carrier
VOLUME_TABLE_SCRIPTS_CSV := $(VOLUME_TABLE_SCRIPTS_ROOT)/scripts.csv
.PHONY: morphism-codebase-volume-table-scripts
morphism-codebase-volume-table-scripts: $(VOLUME_TABLE_SCRIPTS_CSV)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_LINE),$(VOLUME_TABLE_SCRIPTS_INPUT),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.input.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_NEWLINE),$(VOLUME_TABLE_SCRIPTS_LINE),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.input.newline.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_PATH),$(VOLUME_TABLE_SCRIPTS_NEWLINE),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_NONEMPTY),$(VOLUME_TABLE_SCRIPTS_PATH),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.nonempty.selection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_DISTINCT),$(VOLUME_TABLE_SCRIPTS_NONEMPTY),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.distinct.selection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_ROW),$(VOLUME_TABLE_SCRIPTS_DISTINCT),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.row.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_ORDER),$(VOLUME_TABLE_SCRIPTS_ROW),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_HEADER),$(VOLUME_TABLE_SCRIPTS_ORDER),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.header.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_TABLE_SCRIPTS_CSV),$(VOLUME_TABLE_SCRIPTS_HEADER),silmaril.sparky.morphism.codebase.volume.table.scripts.construct.csv.encode.process))
