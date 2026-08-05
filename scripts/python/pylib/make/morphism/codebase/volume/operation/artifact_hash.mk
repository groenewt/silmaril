MORPHISM_CODEBASE_VOLUME_HASH_ROOT := $(MORPHISM_CODEBASE_VOLUME_OPERATION_ROOT)/artifact/hash
VOLUME_HASH_LINE_ARTIFACT ?=
VOLUME_HASH_LINE_RELATIVE_PATH ?=
VOLUME_HASH_MANIFEST_LINES ?=

VOLUME_HASH_LINE_PARSE := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/input-parse.carrier
VOLUME_HASH_LINE_ARTIFACT_VALIDATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/artifact-validation.carrier
VOLUME_HASH_LINE_PATH_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/path-presence.carrier
VOLUME_HASH_LINE_PATH_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/path-pathname.carrier
VOLUME_HASH_LINE_PATH_ABSOLUTE := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/path-absolute.carrier
VOLUME_HASH_LINE_PATH_PARENT := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/path-parent.carrier
VOLUME_HASH_LINE_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/path-normalization.carrier
VOLUME_HASH_LINE_PATH_STRING := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/path-string.carrier
VOLUME_HASH_LINE_SHA256 := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/sha256.carrier
VOLUME_HASH_LINE_CONSTRUCTION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/construction.carrier
VOLUME_HASH_LINE := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/line/hash-line.txt

.PHONY: morphism-codebase-volume-artifact-hash-line
morphism-codebase-volume-artifact-hash-line: $(VOLUME_HASH_LINE)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_SOURCE,$(VOLUME_HASH_LINE_PARSE),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.input.parse.process,$(VOLUME_HASH_LINE_ARTIFACT) $(VOLUME_HASH_LINE_RELATIVE_PATH),$(VOLUME_HASH_LINE_ARTIFACT)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_ARTIFACT_VALIDATION),$(VOLUME_HASH_LINE_PARSE),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.artifact.existence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_PATH_PRESENCE),$(VOLUME_HASH_LINE_ARTIFACT_VALIDATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.path.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_PATH_PATHNAME),$(VOLUME_HASH_LINE_PATH_PRESENCE),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_PATH_ABSOLUTE),$(VOLUME_HASH_LINE_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.path.absolute.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_PATH_PARENT),$(VOLUME_HASH_LINE_PATH_ABSOLUTE),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.path.parent.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_PATH_NORMALIZATION),$(VOLUME_HASH_LINE_PATH_PARENT),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_PATH_STRING),$(VOLUME_HASH_LINE_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.path.string.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_SHA256),$(VOLUME_HASH_LINE_PATH_STRING),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.sha256.observation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE_CONSTRUCTION),$(VOLUME_HASH_LINE_SHA256),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.line.construction.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_LINE),$(VOLUME_HASH_LINE_CONSTRUCTION),silmaril.sparky.morphism.codebase.volume.artifact.hash_line.construct.line.encode.process))

VOLUME_HASH_MANIFEST_PARSE := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/input-parse.carrier
VOLUME_HASH_MANIFEST_ARTIFACT_VALIDATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/artifact-validation.carrier
VOLUME_HASH_MANIFEST_LINE_OBSERVATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-observation.carrier
VOLUME_HASH_MANIFEST_LINE_COUNT_PROJECTION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-count-projection.carrier
VOLUME_HASH_MANIFEST_LINE_COUNT_VALIDATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-count-validation.carrier
VOLUME_HASH_MANIFEST_LINE_ONLY_PROJECTION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-only-projection.carrier
VOLUME_HASH_MANIFEST_LINE_PATTERN_PROJECTION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-pattern-projection.carrier
VOLUME_HASH_MANIFEST_LINE_PATTERN_VALIDATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-pattern-validation.carrier
VOLUME_HASH_MANIFEST_LINE_ENTRY_CONSTRUCTION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/line-entry-construction.carrier
VOLUME_HASH_MANIFEST_PATH_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/path-pathname.carrier
VOLUME_HASH_MANIFEST_PATH_ABSOLUTE := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/path-absolute.carrier
VOLUME_HASH_MANIFEST_PATH_PARENT := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/path-parent.carrier
VOLUME_HASH_MANIFEST_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/path-normalization.carrier
VOLUME_HASH_MANIFEST_PATH_STRING := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/path-string.carrier
VOLUME_HASH_MANIFEST_ENTRY_RECONSTRUCTION := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/entry-reconstruction.carrier
VOLUME_HASH_MANIFEST_IDENTITY := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/identity.carrier
VOLUME_HASH_MANIFEST_UNIQUENESS := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/uniqueness.carrier
VOLUME_HASH_MANIFEST_ORDER := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/order.carrier
VOLUME_HASH_MANIFEST := $(MORPHISM_CODEBASE_VOLUME_HASH_ROOT)/manifest/manifest.txt

.PHONY: morphism-codebase-volume-artifact-hash-manifest
morphism-codebase-volume-artifact-hash-manifest: $(VOLUME_HASH_MANIFEST)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_SOURCE,$(VOLUME_HASH_MANIFEST_PARSE),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.input.parse.process,$(VOLUME_HASH_MANIFEST_LINES),$(VOLUME_HASH_MANIFEST_LINES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_ARTIFACT_VALIDATION),$(VOLUME_HASH_MANIFEST_PARSE),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.artifact.existence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_OBSERVATION),$(VOLUME_HASH_MANIFEST_ARTIFACT_VALIDATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.observation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_COUNT_PROJECTION),$(VOLUME_HASH_MANIFEST_LINE_OBSERVATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.count.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_COUNT_VALIDATION),$(VOLUME_HASH_MANIFEST_LINE_COUNT_PROJECTION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.count.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_ONLY_PROJECTION),$(VOLUME_HASH_MANIFEST_LINE_COUNT_VALIDATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.only.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_PATTERN_PROJECTION),$(VOLUME_HASH_MANIFEST_LINE_ONLY_PROJECTION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.pattern.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_PATTERN_VALIDATION),$(VOLUME_HASH_MANIFEST_LINE_PATTERN_PROJECTION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.pattern.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_LINE_ENTRY_CONSTRUCTION),$(VOLUME_HASH_MANIFEST_LINE_PATTERN_VALIDATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.entry.construction.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_PATH_PATHNAME),$(VOLUME_HASH_MANIFEST_LINE_ENTRY_CONSTRUCTION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_PATH_ABSOLUTE),$(VOLUME_HASH_MANIFEST_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.path.absolute.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_PATH_PARENT),$(VOLUME_HASH_MANIFEST_PATH_ABSOLUTE),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.path.parent.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_PATH_NORMALIZATION),$(VOLUME_HASH_MANIFEST_PATH_PARENT),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_PATH_STRING),$(VOLUME_HASH_MANIFEST_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.path.string.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_ENTRY_RECONSTRUCTION),$(VOLUME_HASH_MANIFEST_PATH_STRING),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.entry.reconstruction.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_IDENTITY),$(VOLUME_HASH_MANIFEST_ENTRY_RECONSTRUCTION),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.identity.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_UNIQUENESS),$(VOLUME_HASH_MANIFEST_IDENTITY),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST_ORDER),$(VOLUME_HASH_MANIFEST_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_HASH_MANIFEST),$(VOLUME_HASH_MANIFEST_ORDER),silmaril.sparky.morphism.codebase.volume.artifact.hash_manifest.construct.line.encode.process))
