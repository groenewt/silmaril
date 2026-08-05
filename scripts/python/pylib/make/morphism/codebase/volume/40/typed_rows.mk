# Dynamic, source-derived row streams for the five aggregate table families.
# Every semantic edge is an external runtime coordinate; Make alone composes
# raw stdout into the next process stdin and retains original stderr/status.

VOLUME_40_TYPED_ROW_ROOT := $(VOLUME_40_BUILD_ROOT)/typed-rows
VOLUME_40_SOURCE_FILES_ROWS_ROOT := $(VOLUME_40_TYPED_ROW_ROOT)/source_files/observed
VOLUME_40_SOURCE_FILES_ROWS_FRAME := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/input-frame.carrier
VOLUME_40_SOURCE_FILES_ROWS_ROOT_ID := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/root-id-validation.carrier
VOLUME_40_SOURCE_FILES_ROWS_ROOT_INPUT_PATHNAME := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/root-input-pathname.carrier
VOLUME_40_SOURCE_FILES_ROWS_ROOT_ABSOLUTE := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/root-absolute-validation.carrier
VOLUME_40_SOURCE_FILES_ROWS_ROOT_REAL := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/root-real.carrier
VOLUME_40_SOURCE_FILES_ROWS_ROOT_PATHNAME := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/root-pathname.carrier
VOLUME_40_SOURCE_FILES_ROWS_PATH_NORMALIZATION := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/path-normalization.carrier
VOLUME_40_SOURCE_FILES_ROWS_PATH_PATHNAME := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/path-pathname.carrier
VOLUME_40_SOURCE_FILES_ROWS_PATH_SAFETY := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/path-safety-validation.carrier
VOLUME_40_SOURCE_FILES_ROWS_LOCUS := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/locus-projection.carrier
VOLUME_40_SOURCE_FILES_ROWS_LOCUS_NORMALIZATION := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/locus-normalization.carrier
VOLUME_40_SOURCE_FILES_ROWS_LOCUS_STRING := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/locus-string.carrier
VOLUME_40_SOURCE_FILES_ROWS_PATHNAME_RELEASE := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/pathname-carrier-release.carrier
VOLUME_40_SOURCE_FILES_ROWS_REGULAR := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/regular-selection.carrier
VOLUME_40_SOURCE_FILES_ROWS_READABLE := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/readable-selection.carrier
VOLUME_40_SOURCE_FILES_ROWS_ROW := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/row-projection.carrier
VOLUME_40_SOURCE_FILES_ROWS_CSV := $(VOLUME_40_SOURCE_FILES_ROWS_ROOT)/rows.csv

VOLUME_40_FINAL_OBSERVATION_OPERATION_ROOT := $(VOLUME_40_BUILD_ROOT)/observation/final-working/operation
VOLUME_40_FINAL_OBSERVATION_LINE := $(VOLUME_40_FINAL_OBSERVATION_OPERATION_ROOT)/source/observation/line/lines.txt
VOLUME_40_NATIVE_OBSERVATION_OPERATION_ROOT := $(VOLUME_40_BUILD_ROOT)/observation/native-evidence/operation
VOLUME_40_NATIVE_OBSERVATION_LINE := $(VOLUME_40_NATIVE_OBSERVATION_OPERATION_ROOT)/source/observation/line/lines.txt
VOLUME_40_NATIVE_EVIDENCE_ROOT ?= $(VOLUME_40_SOURCE_ROOT)/logs/native

.PHONY: volume-40-typed-row-producers

$(VOLUME_40_FINAL_OBSERVATION_LINE):
	$(MAKE) --no-print-directory -B \
		-f make/morphism/codebase/volume/operation/file.mk \
		-f make/morphism/codebase/volume/operation/source_observation.mk \
		"$@" \
		SILMARIL_PYTHON="$(SILMARIL_PYTHON)" \
		MORPHISM_CODEBASE_VOLUME_OPERATION_ROOT="$(VOLUME_40_FINAL_OBSERVATION_OPERATION_ROOT)" \
		MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT="$(VOLUME_40_FINAL_WORKING_ROOT)"

$(VOLUME_40_NATIVE_OBSERVATION_LINE):
	@test -d "$(VOLUME_40_NATIVE_EVIDENCE_ROOT)" || { printf 'native evidence root is not a directory: %s\n' "$(VOLUME_40_NATIVE_EVIDENCE_ROOT)" >&2; exit 66; }
	$(MAKE) --no-print-directory -B \
		-f make/morphism/codebase/volume/operation/file.mk \
		-f make/morphism/codebase/volume/operation/source_observation.mk \
		"$@" \
		SILMARIL_PYTHON="$(SILMARIL_PYTHON)" \
		MORPHISM_CODEBASE_VOLUME_OPERATION_ROOT="$(VOLUME_40_NATIVE_OBSERVATION_OPERATION_ROOT)" \
		MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT="$(VOLUME_40_NATIVE_EVIDENCE_ROOT)"

$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_FRAME),$(VOLUME_OBSERVATION_PATH_ORDER),silmaril.sparky.morphism.codebase.volume.table.source_files.observed.input.frame.process,"codebase" "$(VOLUME_40_SOURCE_ROOT)"))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_ID),$(VOLUME_40_SOURCE_FILES_ROWS_FRAME),silmaril.sparky.morphism.codebase.volume.table.source_files.root.id.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_INPUT_PATHNAME),$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_ID),silmaril.sparky.morphism.codebase.volume.table.source_files.root.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_ABSOLUTE),$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_INPUT_PATHNAME),silmaril.sparky.morphism.codebase.volume.table.source_files.root.pathname.absolute.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_REAL),$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_ABSOLUTE),silmaril.sparky.morphism.codebase.volume.table.source_files.root.real.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_PATHNAME),$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_REAL),silmaril.sparky.morphism.codebase.volume.table.source_files.root.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_PATH_NORMALIZATION),$(VOLUME_40_SOURCE_FILES_ROWS_ROOT_PATHNAME),silmaril.sparky.morphism.codebase.volume.table.source_files.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_PATH_PATHNAME),$(VOLUME_40_SOURCE_FILES_ROWS_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.source_files.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_PATH_SAFETY),$(VOLUME_40_SOURCE_FILES_ROWS_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.table.source_files.path.pathname.safety.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_LOCUS),$(VOLUME_40_SOURCE_FILES_ROWS_PATH_SAFETY),silmaril.sparky.morphism.codebase.volume.table.source_files.locus.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_LOCUS_NORMALIZATION),$(VOLUME_40_SOURCE_FILES_ROWS_LOCUS),silmaril.sparky.morphism.codebase.volume.table.source_files.locus.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_LOCUS_STRING),$(VOLUME_40_SOURCE_FILES_ROWS_LOCUS_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.table.source_files.locus.string.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_PATHNAME_RELEASE),$(VOLUME_40_SOURCE_FILES_ROWS_LOCUS_STRING),silmaril.sparky.morphism.codebase.volume.table.source_files.pathname.carrier.release.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_REGULAR),$(VOLUME_40_SOURCE_FILES_ROWS_PATHNAME_RELEASE),silmaril.sparky.morphism.codebase.volume.table.source_files.observed.regular.selection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_READABLE),$(VOLUME_40_SOURCE_FILES_ROWS_REGULAR),silmaril.sparky.morphism.codebase.volume.table.source_files.observed.readable.selection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_ROW),$(VOLUME_40_SOURCE_FILES_ROWS_READABLE),silmaril.sparky.morphism.codebase.volume.table.source_files.observed.row.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_40_SOURCE_FILES_ROWS_CSV),$(VOLUME_40_SOURCE_FILES_ROWS_ROW),silmaril.sparky.morphism.codebase.volume.table.source_files.csv.encode.process))

define VOLUME_40_EVIDENCE_ROW_PIPELINE
VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT := $$(VOLUME_40_TYPED_ROW_ROOT)/$(1)/$(2)
VOLUME_40_TYPED_ROW_$(1)_$(2)_FILTER := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/filter.txt
VOLUME_40_TYPED_ROW_$(1)_$(2)_FRAME := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/input-frame.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_NEWLINE := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/source-newline.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_PATTERN := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/source-pattern.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_VALIDATION := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/source-validation.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_ROW := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/row-projection.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_CSV := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/rows.csv
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FILTER),$(5),$(6)))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FRAME),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FILTER),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.input.parse.process,"$(1)" "$(3)" "$(4)"))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_NEWLINE),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FRAME),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.source.newline.normalization.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_PATTERN),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_NEWLINE),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.source.pattern.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_VALIDATION),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_PATTERN),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.source.pattern.validation.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROW),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_VALIDATION),$(7)))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_CSV),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROW),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.csv.encode.process))
endef

define VOLUME_40_GDB_EVIDENCE_ROW_PIPELINE
VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT := $$(VOLUME_40_TYPED_ROW_ROOT)/$(1)/$(2)
VOLUME_40_TYPED_ROW_$(1)_$(2)_FILTER := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/filter.txt
VOLUME_40_TYPED_ROW_$(1)_$(2)_FRAME := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/input-frame.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_NEWLINE := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/source-newline.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_PATTERN := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/source-pattern.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_VALIDATION := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/source-validation.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_DIGEST := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/digest-projection.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_ROW := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/row-projection.carrier
VOLUME_40_TYPED_ROW_$(1)_$(2)_CSV := $$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROOT)/rows.csv
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FILTER),$(5),$(6)))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FRAME),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FILTER),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.input.parse.process,"$(1)" "$(3)" "$(4)"))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_NEWLINE),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_FRAME),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.source.newline.normalization.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_PATTERN),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_NEWLINE),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.source.pattern.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_VALIDATION),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_PATTERN),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.source.pattern.validation.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_DIGEST),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_VALIDATION),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.digest.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROW),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_DIGEST),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.gdb_evidence.projection.process))
$$(eval $$(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_CSV),$$(VOLUME_40_TYPED_ROW_$(1)_$(2)_ROW),silmaril.sparky.morphism.codebase.volume.table.evidence_rows.csv.encode.process))
endef

$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,dunbar_inner_5,0,dunbar_inner_5,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_inner_5.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,dunbar_15,1,dunbar_15,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_15.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,dunbar_50,2,dunbar_50,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_50.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,dunbar_150,3,dunbar_150,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_150.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,l0,4,l0,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.l0.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,l1,5,l1,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.l1.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,l2,6,l2,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.l2.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,l3,7,l3,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.l3.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,l3_5,8,l3_5,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.l3_5.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,native_pool,9,native_pool,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.native_pool.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,ring_families,trust_protection,10,trust_protection,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.ring.family.trust_protection.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.ring_families.projection.process))

$(eval $(call VOLUME_40_GDB_EVIDENCE_ROW_PIPELINE,gdb_evidence,hash,hash,,$(VOLUME_40_NATIVE_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.native.gdb.hash.process))
$(eval $(call VOLUME_40_GDB_EVIDENCE_ROW_PIPELINE,gdb_evidence,readback,readback,,$(VOLUME_40_NATIVE_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.native.gdb.readback.process))
$(eval $(call VOLUME_40_GDB_EVIDENCE_ROW_PIPELINE,gdb_evidence,source_frame,source_frame,,$(VOLUME_40_NATIVE_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.native.gdb.source_frame.process))
$(eval $(call VOLUME_40_GDB_EVIDENCE_ROW_PIPELINE,gdb_evidence,transcript,transcript,,$(VOLUME_40_NATIVE_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.native.gdb.transcript.process))
$(eval $(call VOLUME_40_GDB_EVIDENCE_ROW_PIPELINE,gdb_evidence,verifier,verifier,,$(VOLUME_OBSERVATION_LINE_ORDER),silmaril.sparky.morphism.codebase.volume.native.gdb.verifier.process))

$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,bibliography,bibliography,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.bibliography.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,build_wrapper,build_wrapper,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.build_wrapper.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,diagram,diagram,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.diagram.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,glossary,glossary,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.glossary.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,index,index,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.index.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,macro,macro,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.macro.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,preamble,preamble,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.preamble.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,projection_wrapper,projection_wrapper,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.projection_wrapper.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,table,table,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.table.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_components,title_metadata,title_metadata,,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.component.title_metadata.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_components.projection.process))

$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,cross_volume,cross_volume,cross_volume,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.cross_volume.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,global_architecture,global_architecture,global_architecture,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.global_architecture.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,label,label,latex_label,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.label.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,validation_build,validation_build,validation_build,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.build.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,validation_include,validation_include,validation_include,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.include.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,validation_label,validation_label,validation_label,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.label.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))
$(eval $(call VOLUME_40_EVIDENCE_ROW_PIPELINE,shared_anchors,validation_projection,validation_projection,validation_projection,$(VOLUME_40_FINAL_OBSERVATION_LINE),silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.projection.process,silmaril.sparky.morphism.codebase.volume.table.evidence_rows.row.shared_anchors.projection.process))

VOLUME_40_RING_FAMILIES_ROW_FILES_GENERATED := $(foreach name,dunbar_inner_5 dunbar_15 dunbar_50 dunbar_150 l0 l1 l2 l3 l3_5 native_pool trust_protection,$(VOLUME_40_TYPED_ROW_ring_families_$(name)_CSV))
VOLUME_40_GDB_EVIDENCE_ROW_FILES_GENERATED := $(foreach name,hash readback source_frame transcript verifier,$(VOLUME_40_TYPED_ROW_gdb_evidence_$(name)_CSV))
VOLUME_40_SHARED_COMPONENTS_ROW_FILES_GENERATED := $(foreach name,bibliography build_wrapper diagram glossary index macro preamble projection_wrapper table title_metadata,$(VOLUME_40_TYPED_ROW_shared_components_$(name)_CSV))
VOLUME_40_SHARED_ANCHORS_ROW_FILES_GENERATED := $(foreach name,cross_volume global_architecture label validation_build validation_include validation_label validation_projection,$(VOLUME_40_TYPED_ROW_shared_anchors_$(name)_CSV))

VOLUME_40_SOURCE_FILES_ROW_FILES := $(VOLUME_40_SOURCE_FILES_ROWS_CSV)
VOLUME_40_RING_FAMILIES_ROW_FILES := $(VOLUME_40_RING_FAMILIES_ROW_FILES_GENERATED)
VOLUME_40_GDB_EVIDENCE_ROW_FILES := $(VOLUME_40_GDB_EVIDENCE_ROW_FILES_GENERATED)
VOLUME_40_SHARED_COMPONENTS_ROW_FILES := $(VOLUME_40_SHARED_COMPONENTS_ROW_FILES_GENERATED)
VOLUME_40_SHARED_ANCHORS_ROW_FILES := $(VOLUME_40_SHARED_ANCHORS_ROW_FILES_GENERATED)

volume-40-typed-row-producers: \
	$(VOLUME_40_SOURCE_FILES_ROW_FILES) \
	$(VOLUME_40_RING_FAMILIES_ROW_FILES) \
	$(VOLUME_40_GDB_EVIDENCE_ROW_FILES) \
	$(VOLUME_40_SHARED_COMPONENTS_ROW_FILES) \
	$(VOLUME_40_SHARED_ANCHORS_ROW_FILES)
