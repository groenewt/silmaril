SILMARIL_PYLIB_SOURCE_ROOT ?= $(CURDIR)/src
VOLUME_BASE_OUTPUT_ROOT ?= $(CURDIR)/build/morphism/codebase/volume/base

.PHONY: volume-base-force morphism-codebase-volume-base
volume-base-force:

$(VOLUME_BASE_OUTPUT_ROOT):
	mkdir -p "$@"

define VOLUME_BASE_STDIN0
$(4)_INPUT ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): $$($(4)_INPUT) | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_INPUT)" || { printf '%s\n' '$(4)_INPUT is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) <"$$($(4)_INPUT)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_STDIN1
$(4)_INPUT ?=
$(4)_ARGUMENT_1 ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): $$($(4)_INPUT) | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_INPUT)" || { printf '%s\n' '$(4)_INPUT is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" <"$$($(4)_INPUT)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_STDIN2
$(4)_INPUT ?=
$(4)_ARGUMENT_1 ?=
$(4)_ARGUMENT_2 ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): $$($(4)_INPUT) | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_INPUT)" || { printf '%s\n' '$(4)_INPUT is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_2)" || { printf '%s\n' '$(4)_ARGUMENT_2 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" "$$($(4)_ARGUMENT_2)" <"$$($(4)_INPUT)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_ARGV1
$(4)_ARGUMENT_1 ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): volume-base-force | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_ARGV2
$(4)_ARGUMENT_1 ?=
$(4)_ARGUMENT_2 ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): volume-base-force | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_2)" || { printf '%s\n' '$(4)_ARGUMENT_2 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" "$$($(4)_ARGUMENT_2)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_ARGV3
$(4)_ARGUMENT_1 ?=
$(4)_ARGUMENT_2 ?=
$(4)_ARGUMENT_3 ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): volume-base-force | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_2)" || { printf '%s\n' '$(4)_ARGUMENT_2 is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_3)" || { printf '%s\n' '$(4)_ARGUMENT_3 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" "$$($(4)_ARGUMENT_2)" "$$($(4)_ARGUMENT_3)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_ARGV1_REST
$(4)_ARGUMENT_1 ?=
$(4)_REST_ARGUMENTS ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): volume-base-force | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" $$($(4)_REST_ARGUMENTS) >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_STDIN1_REST
$(4)_INPUT ?=
$(4)_ARGUMENT_1 ?=
$(4)_REST_ARGUMENTS ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): $$($(4)_INPUT) | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@test -n "$$($(4)_INPUT)" || { printf '%s\n' '$(4)_INPUT is required' >&2; exit 64; }
	@test -n "$$($(4)_ARGUMENT_1)" || { printf '%s\n' '$(4)_ARGUMENT_1 is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) "$$($(4)_ARGUMENT_1)" $$($(4)_REST_ARGUMENTS) <"$$($(4)_INPUT)" >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

define VOLUME_BASE_ARGV_REST
$(4)_ARGUMENTS ?=
$(4)_OUTPUT ?= $(VOLUME_BASE_OUTPUT_ROOT)/$(3).out
.PHONY: $(1)
$(1): $$($(4)_OUTPUT)
$$($(4)_OUTPUT): volume-base-force | $(VOLUME_BASE_OUTPUT_ROOT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $(2) $$($(4)_ARGUMENTS) >"$$@.tmp" 2>"$$@.error"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$$@.error" >&2; exit "$$$$status"; fi; rm -f "$$@.error"; mv "$$@.tmp" "$$@"
endef

VOLUME_BASE_TARGETS := \
	morphism-codebase-volume-base-artifact-atomic-delivery \
	morphism-codebase-volume-base-artifact-comparison \
	morphism-codebase-volume-base-artifact-digest \
	morphism-codebase-volume-base-artifact-install \
	morphism-codebase-volume-base-inventory-configuration \
	morphism-codebase-volume-base-inventory-dependency \
	morphism-codebase-volume-base-inventory-documentation \
	morphism-codebase-volume-base-inventory-make-target \
	morphism-codebase-volume-base-inventory-mix-task \
	morphism-codebase-volume-base-inventory-module \
	morphism-codebase-volume-base-inventory-native \
	morphism-codebase-volume-base-inventory-project-task \
	morphism-codebase-volume-base-inventory-public-api \
	morphism-codebase-volume-base-inventory-relation \
	morphism-codebase-volume-base-inventory-script \
	morphism-codebase-volume-base-inventory-telephone \
	morphism-codebase-volume-base-inventory-test \
	morphism-codebase-volume-base-native-gdb-hash \
	morphism-codebase-volume-base-native-gdb-readback \
	morphism-codebase-volume-base-native-gdb-source-frame \
	morphism-codebase-volume-base-native-gdb-transcript \
	morphism-codebase-volume-base-native-gdb-verifier \
	morphism-codebase-volume-base-projection-chapter \
	morphism-codebase-volume-base-projection-inventory \
	morphism-codebase-volume-base-projection-provenance \
	morphism-codebase-volume-base-projection-render-fragment \
	morphism-codebase-volume-base-projection-section \
	morphism-codebase-volume-base-projection-shared-anchor \
	morphism-codebase-volume-base-projection-shared-component \
	morphism-codebase-volume-base-ring-family-dunbar-15 \
	morphism-codebase-volume-base-ring-family-dunbar-150 \
	morphism-codebase-volume-base-ring-family-dunbar-50 \
	morphism-codebase-volume-base-ring-family-dunbar-inner-5 \
	morphism-codebase-volume-base-ring-family-l0 \
	morphism-codebase-volume-base-ring-family-l1 \
	morphism-codebase-volume-base-ring-family-l2 \
	morphism-codebase-volume-base-ring-family-l3 \
	morphism-codebase-volume-base-ring-family-l3-5 \
	morphism-codebase-volume-base-ring-family-native-pool \
	morphism-codebase-volume-base-ring-family-trust-protection \
	morphism-codebase-volume-base-root-project \
	morphism-codebase-volume-base-shared-anchor-cross-volume \
	morphism-codebase-volume-base-shared-anchor-global-architecture \
	morphism-codebase-volume-base-shared-anchor-label \
	morphism-codebase-volume-base-shared-anchor-validation-build \
	morphism-codebase-volume-base-shared-anchor-validation-include \
	morphism-codebase-volume-base-shared-anchor-validation-label \
	morphism-codebase-volume-base-shared-anchor-validation-projection \
	morphism-codebase-volume-base-shared-component-bibliography \
	morphism-codebase-volume-base-shared-component-build-wrapper \
	morphism-codebase-volume-base-shared-component-diagram \
	morphism-codebase-volume-base-shared-component-glossary \
	morphism-codebase-volume-base-shared-component-index \
	morphism-codebase-volume-base-shared-component-macro \
	morphism-codebase-volume-base-shared-component-preamble \
	morphism-codebase-volume-base-shared-component-projection-wrapper \
	morphism-codebase-volume-base-shared-component-table \
	morphism-codebase-volume-base-shared-component-title-metadata \
	morphism-codebase-volume-base-source-observation-bytes \
	morphism-codebase-volume-base-source-observation-classification \
	morphism-codebase-volume-base-source-observation-digest \
	morphism-codebase-volume-base-source-observation-parse \
	morphism-codebase-volume-base-source-observation-text \
	morphism-codebase-volume-base-verification-absent-anchor \
	morphism-codebase-volume-base-verification-collision \
	morphism-codebase-volume-base-verification-mtime-invariance \
	morphism-codebase-volume-base-verification-reverse-discovery \
	morphism-codebase-volume-base-verification-self-test \
	morphism-codebase-volume-base-verification-symlink-escape \
	morphism-codebase-volume-base-verification-twin-readback \
	morphism-codebase-volume-base-source-observation-text

$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-artifact-atomic-delivery,silmaril.sparky.morphism.codebase.volume.artifact.atomic_delivery.process,artifact__atomic_delivery,VOLUME_BASE_ARTIFACT_ATOMIC_DELIVERY))
$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-artifact-comparison,silmaril.sparky.morphism.codebase.volume.artifact.comparison.process,artifact__comparison,VOLUME_BASE_ARTIFACT_COMPARISON))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-artifact-digest,silmaril.sparky.morphism.codebase.volume.artifact.digest.process,artifact__digest,VOLUME_BASE_ARTIFACT_DIGEST))
$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-artifact-install,silmaril.sparky.morphism.codebase.volume.artifact.install.process,artifact__install,VOLUME_BASE_ARTIFACT_INSTALL))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-configuration,silmaril.sparky.morphism.codebase.volume.inventory.configuration.process,inventory__configuration,VOLUME_BASE_INVENTORY_CONFIGURATION))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-dependency,silmaril.sparky.morphism.codebase.volume.inventory.dependency.process,inventory__dependency,VOLUME_BASE_INVENTORY_DEPENDENCY))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-documentation,silmaril.sparky.morphism.codebase.volume.inventory.documentation.process,inventory__documentation,VOLUME_BASE_INVENTORY_DOCUMENTATION))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-make-target,silmaril.sparky.morphism.codebase.volume.inventory.make_target.process,inventory__make_target,VOLUME_BASE_INVENTORY_MAKE_TARGET))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-mix-task,silmaril.sparky.morphism.codebase.volume.inventory.mix_task.process,inventory__mix_task,VOLUME_BASE_INVENTORY_MIX_TASK))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-module,silmaril.sparky.morphism.codebase.volume.inventory.module.process,inventory__module,VOLUME_BASE_INVENTORY_MODULE))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-native,silmaril.sparky.morphism.codebase.volume.inventory.native.process,inventory__native,VOLUME_BASE_INVENTORY_NATIVE))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-project-task,silmaril.sparky.morphism.codebase.volume.inventory.project_task.process,inventory__project_task,VOLUME_BASE_INVENTORY_PROJECT_TASK))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-public-api,silmaril.sparky.morphism.codebase.volume.inventory.public_api.process,inventory__public_api,VOLUME_BASE_INVENTORY_PUBLIC_API))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-relation,silmaril.sparky.morphism.codebase.volume.inventory.relation.process,inventory__relation,VOLUME_BASE_INVENTORY_RELATION))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-script,silmaril.sparky.morphism.codebase.volume.inventory.script.process,inventory__script,VOLUME_BASE_INVENTORY_SCRIPT))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-telephone,silmaril.sparky.morphism.codebase.volume.inventory.telephone.process,inventory__telephone,VOLUME_BASE_INVENTORY_TELEPHONE))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-inventory-test,silmaril.sparky.morphism.codebase.volume.inventory.test.process,inventory__test,VOLUME_BASE_INVENTORY_TEST))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-native-gdb-hash,silmaril.sparky.morphism.codebase.volume.native.gdb.hash.process,native__gdb__hash,VOLUME_BASE_NATIVE_GDB_HASH))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-native-gdb-readback,silmaril.sparky.morphism.codebase.volume.native.gdb.readback.process,native__gdb__readback,VOLUME_BASE_NATIVE_GDB_READBACK))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-native-gdb-source-frame,silmaril.sparky.morphism.codebase.volume.native.gdb.source_frame.process,native__gdb__source_frame,VOLUME_BASE_NATIVE_GDB_SOURCE_FRAME))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-native-gdb-transcript,silmaril.sparky.morphism.codebase.volume.native.gdb.transcript.process,native__gdb__transcript,VOLUME_BASE_NATIVE_GDB_TRANSCRIPT))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-native-gdb-verifier,silmaril.sparky.morphism.codebase.volume.native.gdb.verifier.process,native__gdb__verifier,VOLUME_BASE_NATIVE_GDB_VERIFIER))
$(eval $(call VOLUME_BASE_STDIN1,morphism-codebase-volume-base-projection-chapter,silmaril.sparky.morphism.codebase.volume.projection.chapter.process,projection__chapter,VOLUME_BASE_PROJECTION_CHAPTER))
$(eval $(call VOLUME_BASE_STDIN1,morphism-codebase-volume-base-projection-inventory,silmaril.sparky.morphism.codebase.volume.projection.inventory.process,projection__inventory,VOLUME_BASE_PROJECTION_INVENTORY))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-projection-provenance,silmaril.sparky.morphism.codebase.volume.projection.provenance.process,projection__provenance,VOLUME_BASE_PROJECTION_PROVENANCE))
$(eval $(call VOLUME_BASE_STDIN1,morphism-codebase-volume-base-projection-render-fragment,silmaril.sparky.morphism.codebase.volume.projection.render.fragment.process,projection__render__fragment,VOLUME_BASE_PROJECTION_RENDER_FRAGMENT))
$(eval $(call VOLUME_BASE_STDIN1,morphism-codebase-volume-base-projection-section,silmaril.sparky.morphism.codebase.volume.projection.section.process,projection__section,VOLUME_BASE_PROJECTION_SECTION))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-projection-shared-anchor,silmaril.sparky.morphism.codebase.volume.projection.shared_anchor.process,projection__shared_anchor,VOLUME_BASE_PROJECTION_SHARED_ANCHOR))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-projection-shared-component,silmaril.sparky.morphism.codebase.volume.projection.shared_component.process,projection__shared_component,VOLUME_BASE_PROJECTION_SHARED_COMPONENT))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-dunbar-15,silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_15.process,ring__family__dunbar_15,VOLUME_BASE_RING_FAMILY_DUNBAR_15))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-dunbar-150,silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_150.process,ring__family__dunbar_150,VOLUME_BASE_RING_FAMILY_DUNBAR_150))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-dunbar-50,silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_50.process,ring__family__dunbar_50,VOLUME_BASE_RING_FAMILY_DUNBAR_50))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-dunbar-inner-5,silmaril.sparky.morphism.codebase.volume.ring.family.dunbar_inner_5.process,ring__family__dunbar_inner_5,VOLUME_BASE_RING_FAMILY_DUNBAR_INNER_5))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-l0,silmaril.sparky.morphism.codebase.volume.ring.family.l0.process,ring__family__l0,VOLUME_BASE_RING_FAMILY_L0))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-l1,silmaril.sparky.morphism.codebase.volume.ring.family.l1.process,ring__family__l1,VOLUME_BASE_RING_FAMILY_L1))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-l2,silmaril.sparky.morphism.codebase.volume.ring.family.l2.process,ring__family__l2,VOLUME_BASE_RING_FAMILY_L2))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-l3,silmaril.sparky.morphism.codebase.volume.ring.family.l3.process,ring__family__l3,VOLUME_BASE_RING_FAMILY_L3))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-l3-5,silmaril.sparky.morphism.codebase.volume.ring.family.l3_5.process,ring__family__l3_5,VOLUME_BASE_RING_FAMILY_L3_5))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-native-pool,silmaril.sparky.morphism.codebase.volume.ring.family.native_pool.process,ring__family__native_pool,VOLUME_BASE_RING_FAMILY_NATIVE_POOL))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-ring-family-trust-protection,silmaril.sparky.morphism.codebase.volume.ring.family.trust_protection.process,ring__family__trust_protection,VOLUME_BASE_RING_FAMILY_TRUST_PROTECTION))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-root-project,silmaril.sparky.morphism.codebase.volume.root.project.process,root__project,VOLUME_BASE_ROOT_PROJECT))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-cross-volume,silmaril.sparky.morphism.codebase.volume.shared.anchor.cross_volume.process,shared__anchor__cross_volume,VOLUME_BASE_SHARED_ANCHOR_CROSS_VOLUME))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-global-architecture,silmaril.sparky.morphism.codebase.volume.shared.anchor.global_architecture.process,shared__anchor__global_architecture,VOLUME_BASE_SHARED_ANCHOR_GLOBAL_ARCHITECTURE))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-label,silmaril.sparky.morphism.codebase.volume.shared.anchor.label.process,shared__anchor__label,VOLUME_BASE_SHARED_ANCHOR_LABEL))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-validation-build,silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.build.process,shared__anchor__validation__build,VOLUME_BASE_SHARED_ANCHOR_VALIDATION_BUILD))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-validation-include,silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.include.process,shared__anchor__validation__include,VOLUME_BASE_SHARED_ANCHOR_VALIDATION_INCLUDE))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-validation-label,silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.label.process,shared__anchor__validation__label,VOLUME_BASE_SHARED_ANCHOR_VALIDATION_LABEL))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-anchor-validation-projection,silmaril.sparky.morphism.codebase.volume.shared.anchor.validation.projection.process,shared__anchor__validation__projection,VOLUME_BASE_SHARED_ANCHOR_VALIDATION_PROJECTION))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-bibliography,silmaril.sparky.morphism.codebase.volume.shared.component.bibliography.process,shared__component__bibliography,VOLUME_BASE_SHARED_COMPONENT_BIBLIOGRAPHY))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-build-wrapper,silmaril.sparky.morphism.codebase.volume.shared.component.build_wrapper.process,shared__component__build_wrapper,VOLUME_BASE_SHARED_COMPONENT_BUILD_WRAPPER))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-diagram,silmaril.sparky.morphism.codebase.volume.shared.component.diagram.process,shared__component__diagram,VOLUME_BASE_SHARED_COMPONENT_DIAGRAM))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-glossary,silmaril.sparky.morphism.codebase.volume.shared.component.glossary.process,shared__component__glossary,VOLUME_BASE_SHARED_COMPONENT_GLOSSARY))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-index,silmaril.sparky.morphism.codebase.volume.shared.component.index.process,shared__component__index,VOLUME_BASE_SHARED_COMPONENT_INDEX))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-macro,silmaril.sparky.morphism.codebase.volume.shared.component.macro.process,shared__component__macro,VOLUME_BASE_SHARED_COMPONENT_MACRO))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-preamble,silmaril.sparky.morphism.codebase.volume.shared.component.preamble.process,shared__component__preamble,VOLUME_BASE_SHARED_COMPONENT_PREAMBLE))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-projection-wrapper,silmaril.sparky.morphism.codebase.volume.shared.component.projection_wrapper.process,shared__component__projection_wrapper,VOLUME_BASE_SHARED_COMPONENT_PROJECTION_WRAPPER))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-table,silmaril.sparky.morphism.codebase.volume.shared.component.table.process,shared__component__table,VOLUME_BASE_SHARED_COMPONENT_TABLE))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-shared-component-title-metadata,silmaril.sparky.morphism.codebase.volume.shared.component.title_metadata.process,shared__component__title_metadata,VOLUME_BASE_SHARED_COMPONENT_TITLE_METADATA))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-source-observation-bytes,silmaril.sparky.morphism.codebase.volume.source.observation.bytes.process,source__observation__bytes,VOLUME_BASE_SOURCE_OBSERVATION_BYTES))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-source-observation-classification,silmaril.sparky.morphism.codebase.volume.source.observation.classification.process,source__observation__classification,VOLUME_BASE_SOURCE_OBSERVATION_CLASSIFICATION))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-source-observation-digest,silmaril.sparky.morphism.codebase.volume.source.observation.digest.process,source__observation__digest,VOLUME_BASE_SOURCE_OBSERVATION_DIGEST))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-source-observation-parse,silmaril.sparky.morphism.codebase.volume.source.observation.parse.process,source__observation__parse,VOLUME_BASE_SOURCE_OBSERVATION_PARSE))
$(eval $(call VOLUME_BASE_STDIN0,morphism-codebase-volume-base-source-observation-text,silmaril.sparky.morphism.codebase.volume.source.observation.text.process,source__observation__text,VOLUME_BASE_SOURCE_OBSERVATION_TEXT))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-verification-absent-anchor,silmaril.sparky.morphism.codebase.volume.verification.absent_anchor.process,verification__absent_anchor,VOLUME_BASE_VERIFICATION_ABSENT_ANCHOR))
$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-verification-collision,silmaril.sparky.morphism.codebase.volume.verification.collision.process,verification__collision,VOLUME_BASE_VERIFICATION_COLLISION))
$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-verification-mtime-invariance,silmaril.sparky.morphism.codebase.volume.verification.mtime_invariance.process,verification__mtime_invariance,VOLUME_BASE_VERIFICATION_MTIME_INVARIANCE))
$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-verification-reverse-discovery,silmaril.sparky.morphism.codebase.volume.verification.reverse_discovery.process,verification__reverse_discovery,VOLUME_BASE_VERIFICATION_REVERSE_DISCOVERY))
$(eval $(call VOLUME_BASE_ARGV1,morphism-codebase-volume-base-verification-self-test,silmaril.sparky.morphism.codebase.volume.verification.self_test.process,verification__self_test,VOLUME_BASE_VERIFICATION_SELF_TEST))
$(eval $(call VOLUME_BASE_ARGV2,morphism-codebase-volume-base-verification-twin-readback,silmaril.sparky.morphism.codebase.volume.verification.twin_readback.process,verification__twin_readback,VOLUME_BASE_VERIFICATION_TWIN_READBACK))

morphism-codebase-volume-base: $(VOLUME_BASE_TARGETS)
