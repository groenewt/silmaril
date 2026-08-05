SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_PROJECTION_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/projection
VOLUME_PROJECTION_ARTIFACT_PREFIX ?=

VOLUME_PROJECTION_ARCHITECTURE_INPUT ?=
VOLUME_PROJECTION_BUILD_CONFIGURATION_TASKS_INPUT ?=
VOLUME_PROJECTION_TELEPHONE_RINGS_INPUT ?=
VOLUME_PROJECTION_NATIVE_GDB_VERIFICATION_INPUT ?=
VOLUME_PROJECTION_OPERATIONS_DOCUMENTATION_INPUT ?=
VOLUME_PROJECTION_PROVENANCE_RELATIONS_GAPS_INPUT ?=
VOLUME_PROJECTION_PHASE14_26X4_INPUT ?=
VOLUME_PROJECTION_VOLUME_BODY_INPUT ?=

.PHONY: volume-projection
volume-projection: \
	volume-projection-chapter-architecture \
	volume-projection-chapter-build-configuration-tasks \
	volume-projection-chapter-telephone-rings \
	volume-projection-chapter-native-gdb-verification \
	volume-projection-chapter-operations-documentation \
	volume-projection-chapter-provenance-relations-gaps \
	volume-projection-chapter-phase14-26x4 \
	volume-projection-volume-body

$(VOLUME_PROJECTION_OUTPUT_ROOT):
	mkdir -p "$@"

define VOLUME_PROJECTION_DOCUMENT
.PHONY: $(1)
$(1): $(6)

$(3): $(2) | $(VOLUME_PROJECTION_OUTPUT_ROOT)
	@test -n "$(2)" || { printf '%s\n' '$(1) input is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(9) <"$(2)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"

$(4): $(3)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(10) <"$$<" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"

$(5): $(4)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(11) $(7) <"$$<" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"

$(6): $(4) $(5)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(8) <"$(4)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-architecture,$(VOLUME_PROJECTION_ARCHITECTURE_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/architecture-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/architecture-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/architecture-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/00_architecture.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/source_files.tex tables/modules.tex tables/public_apis.tex tables/dependencies.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.architecture.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.architecture.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.architecture.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.architecture.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-build-configuration-tasks,$(VOLUME_PROJECTION_BUILD_CONFIGURATION_TASKS_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/build-configuration-tasks-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/build-configuration-tasks-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/build-configuration-tasks-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/01_build_configuration_tasks.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/configuration.tex tables/mix_tasks.tex tables/project_tasks.tex tables/make_targets.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.build_configuration_tasks.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.build_configuration_tasks.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.build_configuration_tasks.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.build_configuration_tasks.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-telephone-rings,$(VOLUME_PROJECTION_TELEPHONE_RINGS_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/telephone-rings-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/telephone-rings-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/telephone-rings-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/02_telephone_rings.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/telephone_topology.tex tables/ring_families.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.telephone_rings.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.telephone_rings.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.telephone_rings.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.telephone_rings.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-native-gdb-verification,$(VOLUME_PROJECTION_NATIVE_GDB_VERIFICATION_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/native-gdb-verification-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/native-gdb-verification-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/native-gdb-verification-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/03_native_gdb_verification.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/native_tree.tex tables/gdb_evidence.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.native_gdb_verification.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.native_gdb_verification.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.native_gdb_verification.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.native_gdb_verification.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-operations-documentation,$(VOLUME_PROJECTION_OPERATIONS_DOCUMENTATION_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/operations-documentation-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/operations-documentation-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/operations-documentation-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/04_operations_documentation.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/scripts.tex tables/tests.tex tables/documentation.tex tables/shared_components.tex tables/shared_anchors.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.operations_documentation.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.operations_documentation.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.operations_documentation.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.operations_documentation.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-provenance-relations-gaps,$(VOLUME_PROJECTION_PROVENANCE_RELATIONS_GAPS_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/provenance-relations-gaps-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/provenance-relations-gaps-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/provenance-relations-gaps-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/05_provenance_relations_gaps.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/catalog_documents.tex tables/catalog_claims.tex tables/catalog_gaps.tex tables/catalog_quality_flags.tex tables/provenance.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.provenance_relations_gaps.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.provenance_relations_gaps.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.provenance_relations_gaps.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.provenance_relations_gaps.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-chapter-phase14-26x4,$(VOLUME_PROJECTION_PHASE14_26X4_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/phase14-26x4-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/phase14-26x4-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/phase14-26x4-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/06_phase14_26x4.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),tables/phase14.tex),silmaril.sparky.morphism.codebase.volume.projection.chapter.phase14_26x4.construct.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.phase14_26x4.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.phase14_26x4.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.chapter.phase14_26x4.path.expected.validation.process))
$(eval $(call VOLUME_PROJECTION_DOCUMENT,volume-projection-volume-body,$(VOLUME_PROJECTION_VOLUME_BODY_INPUT),$(VOLUME_PROJECTION_OUTPUT_ROOT)/volume-body-path-lines.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/volume-body-paths.carrier,$(VOLUME_PROJECTION_OUTPUT_ROOT)/volume-body-paths.valid,$(VOLUME_PROJECTION_OUTPUT_ROOT)/body.tex,$(addprefix $(VOLUME_PROJECTION_ARTIFACT_PREFIX),00_architecture.tex 01_build_configuration_tasks.tex 02_telephone_rings.tex 03_native_gdb_verification.tex 04_operations_documentation.tex 05_provenance_relations_gaps.tex 06_phase14_26x4.tex),silmaril.sparky.morphism.codebase.volume.projection.volume_body.construct.process,silmaril.sparky.morphism.codebase.volume.projection.volume_body.path.line.parse.process,silmaril.sparky.morphism.codebase.volume.projection.volume_body.path.newline.normalization.process,silmaril.sparky.morphism.codebase.volume.projection.volume_body.path.expected.validation.process))
