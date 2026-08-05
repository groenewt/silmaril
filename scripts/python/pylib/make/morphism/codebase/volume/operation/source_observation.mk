MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT := $(MORPHISM_CODEBASE_VOLUME_OPERATION_ROOT)/source/observation
MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT ?= $(CURDIR)

VOLUME_OBSERVATION_PATH_DISCOVERY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/discovery.txt
VOLUME_OBSERVATION_PATH_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/input-parse.carrier
VOLUME_OBSERVATION_PATH_LINE_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/line-normalization.carrier
VOLUME_OBSERVATION_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/path-normalization.carrier
VOLUME_OBSERVATION_PATH_SEGMENTS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/segments.carrier
VOLUME_OBSERVATION_PATH_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/exclusion-filter.carrier
VOLUME_OBSERVATION_PATH_ORDER_KEY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/order-key.carrier
VOLUME_OBSERVATION_PATH_SORT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/order.carrier
VOLUME_OBSERVATION_PATH_ORDER_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/order-result.carrier
VOLUME_OBSERVATION_PATH_ORDER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/path/lines.txt
VOLUME_OBSERVATION_LINE_DISCOVERY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/discovery.txt
VOLUME_OBSERVATION_LINE_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/input-parse.carrier
VOLUME_OBSERVATION_LINE_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/path-normalization.carrier
VOLUME_OBSERVATION_LINE_SEGMENTS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/segments.carrier
VOLUME_OBSERVATION_LINE_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/exclusion-filter.carrier
VOLUME_OBSERVATION_LINE_NUMERIC_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/numeric-normalization.carrier
VOLUME_OBSERVATION_LINE_ORDER_KEY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/order-key.carrier
VOLUME_OBSERVATION_LINE_SORT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/order.carrier
VOLUME_OBSERVATION_LINE_ORDER_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/order-result.carrier
VOLUME_OBSERVATION_LINE_CONSTRUCTION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/line-construction.carrier
VOLUME_OBSERVATION_LINE_ORDER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/line/lines.txt
VOLUME_OBSERVATION_SYMLINK_DISCOVERY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/discovery.txt
VOLUME_OBSERVATION_SYMLINK_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/input-parse.carrier
VOLUME_OBSERVATION_SYMLINK_LINE_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/line-normalization.carrier
VOLUME_OBSERVATION_SYMLINK_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/path-normalization.carrier
VOLUME_OBSERVATION_SYMLINK_SEGMENTS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/segments.carrier
VOLUME_OBSERVATION_SYMLINK_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/exclusion-filter.carrier
VOLUME_OBSERVATION_SYMLINK_SELECTION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/selection.carrier
VOLUME_OBSERVATION_SYMLINK_ORDER_KEY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/order-key.carrier
VOLUME_OBSERVATION_SYMLINK_SORT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/order.carrier
VOLUME_OBSERVATION_SYMLINK_ORDER_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/order-result.carrier
VOLUME_OBSERVATION_SYMLINK_ORDER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/symlink/lines.txt

.PHONY: morphism-codebase-volume-source-observation-path morphism-codebase-volume-source-observation-line morphism-codebase-volume-source-observation-symlink morphism-codebase-volume-inventory-source-files
morphism-codebase-volume-source-observation-path: $(VOLUME_OBSERVATION_PATH_ORDER)
morphism-codebase-volume-source-observation-line: $(VOLUME_OBSERVATION_LINE_ORDER)
morphism-codebase-volume-source-observation-symlink: $(VOLUME_OBSERVATION_SYMLINK_ORDER)
morphism-codebase-volume-inventory-source-files: $(VOLUME_OBSERVATION_PATH_ORDER)

$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_SOURCE,$(VOLUME_OBSERVATION_PATH_DISCOVERY),silmaril.sparky.morphism.codebase.volume.source.observation.path.discovery.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT),))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_PARSE),$(VOLUME_OBSERVATION_PATH_DISCOVERY),silmaril.sparky.morphism.codebase.volume.source.observation.path.input.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_LINE_NORMALIZATION),$(VOLUME_OBSERVATION_PATH_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.path.line.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_NORMALIZATION),$(VOLUME_OBSERVATION_PATH_LINE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_SEGMENTS),$(VOLUME_OBSERVATION_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.path.segment.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_FILTER),$(VOLUME_OBSERVATION_PATH_SEGMENTS),silmaril.sparky.morphism.codebase.volume.source.observation.path.exclusion.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_ORDER_KEY),$(VOLUME_OBSERVATION_PATH_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.path.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_SORT),$(VOLUME_OBSERVATION_PATH_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.source.observation.path.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_ORDER_RESULT),$(VOLUME_OBSERVATION_PATH_SORT),silmaril.sparky.morphism.codebase.volume.source.observation.path.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_PATH_ORDER),$(VOLUME_OBSERVATION_PATH_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.path.line.encode.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_SOURCE,$(VOLUME_OBSERVATION_LINE_DISCOVERY),silmaril.sparky.morphism.codebase.volume.source.observation.line.discovery.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT),))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_PARSE),$(VOLUME_OBSERVATION_LINE_DISCOVERY),silmaril.sparky.morphism.codebase.volume.source.observation.line.input.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_PATH_NORMALIZATION),$(VOLUME_OBSERVATION_LINE_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.line.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_SEGMENTS),$(VOLUME_OBSERVATION_LINE_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.line.segment.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_FILTER),$(VOLUME_OBSERVATION_LINE_SEGMENTS),silmaril.sparky.morphism.codebase.volume.source.observation.line.exclusion.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_NUMERIC_NORMALIZATION),$(VOLUME_OBSERVATION_LINE_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.line.numeric.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_ORDER_KEY),$(VOLUME_OBSERVATION_LINE_NUMERIC_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.line.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_SORT),$(VOLUME_OBSERVATION_LINE_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.source.observation.line.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_ORDER_RESULT),$(VOLUME_OBSERVATION_LINE_SORT),silmaril.sparky.morphism.codebase.volume.source.observation.line.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_CONSTRUCTION),$(VOLUME_OBSERVATION_LINE_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.line.line.construction.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_LINE_ORDER),$(VOLUME_OBSERVATION_LINE_CONSTRUCTION),silmaril.sparky.morphism.codebase.volume.source.observation.line.line.encode.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_SOURCE,$(VOLUME_OBSERVATION_SYMLINK_DISCOVERY),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.discovery.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT),))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_PARSE),$(VOLUME_OBSERVATION_SYMLINK_DISCOVERY),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.input.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_LINE_NORMALIZATION),$(VOLUME_OBSERVATION_SYMLINK_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.line.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_PATH_NORMALIZATION),$(VOLUME_OBSERVATION_SYMLINK_LINE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_SEGMENTS),$(VOLUME_OBSERVATION_SYMLINK_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.segment.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_FILTER),$(VOLUME_OBSERVATION_SYMLINK_SEGMENTS),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.exclusion.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$(VOLUME_OBSERVATION_SYMLINK_SELECTION),$(VOLUME_OBSERVATION_SYMLINK_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.selection.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_ORDER_KEY),$(VOLUME_OBSERVATION_SYMLINK_SELECTION),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_SORT),$(VOLUME_OBSERVATION_SYMLINK_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_ORDER_RESULT),$(VOLUME_OBSERVATION_SYMLINK_SORT),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_SYMLINK_ORDER),$(VOLUME_OBSERVATION_SYMLINK_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.symlink.line.encode.process))

VOLUME_OBSERVATION_UNREADABLE_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/input-parse.carrier
VOLUME_OBSERVATION_UNREADABLE_LINE_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/line-normalization.carrier
VOLUME_OBSERVATION_UNREADABLE_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/path-normalization.carrier
VOLUME_OBSERVATION_UNREADABLE_ROOT_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/root-pathname.carrier
VOLUME_OBSERVATION_UNREADABLE_ROOT_ABSOLUTE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/root-absolute.carrier
VOLUME_OBSERVATION_UNREADABLE_ROOT_DIRECTORY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/root-directory.carrier
VOLUME_OBSERVATION_UNREADABLE_PATH_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/path-presence.carrier
VOLUME_OBSERVATION_UNREADABLE_PATH_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/path-pathname.carrier
VOLUME_OBSERVATION_UNREADABLE_PATH_RELATIVE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/path-relative.carrier
VOLUME_OBSERVATION_UNREADABLE_PATH_PARENT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/path-parent.carrier
VOLUME_OBSERVATION_UNREADABLE_LOCUS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/locus.carrier
VOLUME_OBSERVATION_UNREADABLE_LOCUS_STRING := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/locus-string.carrier
VOLUME_OBSERVATION_UNREADABLE_EXISTENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/path-existence.carrier
VOLUME_OBSERVATION_UNREADABLE_SYMLINK_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/symlink-filter.carrier
VOLUME_OBSERVATION_UNREADABLE_FILE_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/file-filter.carrier
VOLUME_OBSERVATION_UNREADABLE_READABILITY_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/readability-filter.carrier
VOLUME_OBSERVATION_UNREADABLE_UNIQUENESS_KEY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/uniqueness-key.carrier
VOLUME_OBSERVATION_UNREADABLE_UNIQUENESS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/uniqueness.carrier
VOLUME_OBSERVATION_UNREADABLE_ORDER_KEY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/order-key.carrier
VOLUME_OBSERVATION_UNREADABLE_SORT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/order.carrier
VOLUME_OBSERVATION_UNREADABLE_ORDER_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/order-result.carrier
VOLUME_OBSERVATION_UNREADABLE_LINES := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/unreadable/lines.txt

.PHONY: morphism-codebase-volume-source-observation-unreadable
morphism-codebase-volume-source-observation-unreadable: $(VOLUME_OBSERVATION_UNREADABLE_LINES)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_PARSE),$(VOLUME_OBSERVATION_PATH_ORDER),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.input.parse.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_LINE_NORMALIZATION),$(VOLUME_OBSERVATION_UNREADABLE_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.line.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_PATH_NORMALIZATION),$(VOLUME_OBSERVATION_UNREADABLE_LINE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_ROOT_PATHNAME),$(VOLUME_OBSERVATION_UNREADABLE_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.root.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_ROOT_ABSOLUTE),$(VOLUME_OBSERVATION_UNREADABLE_ROOT_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.root.absolute.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_ROOT_DIRECTORY),$(VOLUME_OBSERVATION_UNREADABLE_ROOT_ABSOLUTE),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.root.directory.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_PATH_PRESENCE),$(VOLUME_OBSERVATION_UNREADABLE_ROOT_DIRECTORY),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.path.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_PATH_PATHNAME),$(VOLUME_OBSERVATION_UNREADABLE_PATH_PRESENCE),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_PATH_RELATIVE),$(VOLUME_OBSERVATION_UNREADABLE_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.path.relative.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_PATH_PARENT),$(VOLUME_OBSERVATION_UNREADABLE_PATH_RELATIVE),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.path.parent.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_LOCUS),$(VOLUME_OBSERVATION_UNREADABLE_PATH_PARENT),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.locus.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_LOCUS_STRING),$(VOLUME_OBSERVATION_UNREADABLE_LOCUS),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.locus.string.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_EXISTENCE),$(VOLUME_OBSERVATION_UNREADABLE_LOCUS_STRING),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.path.existence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_SYMLINK_FILTER),$(VOLUME_OBSERVATION_UNREADABLE_EXISTENCE),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.symlink.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_FILE_FILTER),$(VOLUME_OBSERVATION_UNREADABLE_SYMLINK_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.file.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_READABILITY_FILTER),$(VOLUME_OBSERVATION_UNREADABLE_FILE_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.readability.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_UNIQUENESS_KEY),$(VOLUME_OBSERVATION_UNREADABLE_READABILITY_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.uniqueness.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_UNIQUENESS),$(VOLUME_OBSERVATION_UNREADABLE_UNIQUENESS_KEY),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_ORDER_KEY),$(VOLUME_OBSERVATION_UNREADABLE_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.order.key.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_SORT),$(VOLUME_OBSERVATION_UNREADABLE_ORDER_KEY),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_ORDER_RESULT),$(VOLUME_OBSERVATION_UNREADABLE_SORT),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.order.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_UNREADABLE_LINES),$(VOLUME_OBSERVATION_UNREADABLE_ORDER_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.unreadable.line.encode.process))

VOLUME_OBSERVATION_EXCLUDED_PREFIXES ?=
VOLUME_OBSERVATION_EXCLUDED_NAMES ?=

VOLUME_OBSERVATION_EXCLUDED_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/input-parse.carrier
VOLUME_OBSERVATION_EXCLUDED_LINE_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/line-normalization.carrier
VOLUME_OBSERVATION_EXCLUDED_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/path-normalization.carrier
VOLUME_OBSERVATION_EXCLUDED_ROOT_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/root-pathname.carrier
VOLUME_OBSERVATION_EXCLUDED_ROOT_ABSOLUTE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/root-absolute.carrier
VOLUME_OBSERVATION_EXCLUDED_ROOT_DIRECTORY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/root-directory.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-presence.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_UNIQUENESS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-uniqueness.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-pathname.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_RELATIVE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-relative.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_PARENT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-parent.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-normalization.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_STRING := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-string.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_LEADING := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-leading.carrier
VOLUME_OBSERVATION_EXCLUDED_PREFIX_TRAILING := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/prefix-trailing.carrier
VOLUME_OBSERVATION_EXCLUDED_PATH_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/path-presence.carrier
VOLUME_OBSERVATION_EXCLUDED_PATH_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/path-pathname.carrier
VOLUME_OBSERVATION_EXCLUDED_PATH_RELATIVE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/path-relative.carrier
VOLUME_OBSERVATION_EXCLUDED_PATH_PARENT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/path-parent.carrier
VOLUME_OBSERVATION_EXCLUDED_LOCUS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/locus.carrier
VOLUME_OBSERVATION_EXCLUDED_EXISTENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/existence.carrier
VOLUME_OBSERVATION_EXCLUDED_LOCUS_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/locus-result.carrier
VOLUME_OBSERVATION_EXCLUDED_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/filter.carrier
VOLUME_OBSERVATION_EXCLUDED_UNIQUENESS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/uniqueness.carrier
VOLUME_OBSERVATION_EXCLUDED_ORDER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/order.carrier
VOLUME_OBSERVATION_EXCLUDED_LINES := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/excluded/lines.txt

.PHONY: morphism-codebase-volume-source-observation-excluded
morphism-codebase-volume-source-observation-excluded: $(VOLUME_OBSERVATION_EXCLUDED_LINES)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PARSE),$(VOLUME_OBSERVATION_PATH_ORDER),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.input.parse.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT) $(VOLUME_OBSERVATION_EXCLUDED_PREFIXES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_LINE_NORMALIZATION),$(VOLUME_OBSERVATION_EXCLUDED_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.line.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PATH_NORMALIZATION),$(VOLUME_OBSERVATION_EXCLUDED_LINE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_ROOT_PATHNAME),$(VOLUME_OBSERVATION_EXCLUDED_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.root.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_ROOT_ABSOLUTE),$(VOLUME_OBSERVATION_EXCLUDED_ROOT_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.root.absolute.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_ROOT_DIRECTORY),$(VOLUME_OBSERVATION_EXCLUDED_ROOT_ABSOLUTE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.root.directory.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_PRESENCE),$(VOLUME_OBSERVATION_EXCLUDED_ROOT_DIRECTORY),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_UNIQUENESS),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_PRESENCE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_PATHNAME),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_RELATIVE),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.relative.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_PARENT),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_RELATIVE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.parent.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_NORMALIZATION),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_PARENT),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_STRING),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.string.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_LEADING),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_STRING),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.leading.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_TRAILING),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_LEADING),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.trailing.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PATH_PRESENCE),$(VOLUME_OBSERVATION_EXCLUDED_PREFIX_TRAILING),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.path.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PATH_PATHNAME),$(VOLUME_OBSERVATION_EXCLUDED_PATH_PRESENCE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PATH_RELATIVE),$(VOLUME_OBSERVATION_EXCLUDED_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.path.relative.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_PATH_PARENT),$(VOLUME_OBSERVATION_EXCLUDED_PATH_RELATIVE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.path.parent.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_LOCUS),$(VOLUME_OBSERVATION_EXCLUDED_PATH_PARENT),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.locus.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_EXISTENCE),$(VOLUME_OBSERVATION_EXCLUDED_LOCUS),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.path.existence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_LOCUS_RESULT),$(VOLUME_OBSERVATION_EXCLUDED_EXISTENCE),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.locus.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_FILTER),$(VOLUME_OBSERVATION_EXCLUDED_LOCUS_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.prefix.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_UNIQUENESS),$(VOLUME_OBSERVATION_EXCLUDED_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_ORDER),$(VOLUME_OBSERVATION_EXCLUDED_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_EXCLUDED_LINES),$(VOLUME_OBSERVATION_EXCLUDED_ORDER),silmaril.sparky.morphism.codebase.volume.source.observation.excluded.line.encode.process))

VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/input-parse.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LINE_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/line-normalization.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_NORMALIZATION := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/path-normalization.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/root-pathname.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_ABSOLUTE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/root-absolute.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_DIRECTORY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/root-directory.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/name-presence.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_UNIQUENESS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/name-uniqueness.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_ELEMENT_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/name-element-presence.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_IDENTITY := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/name-identity.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_SEPARATOR := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/name-separator.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PRESENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/path-presence.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PATHNAME := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/path-pathname.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_RELATIVE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/path-relative.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PARENT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/path-parent.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LOCUS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/locus.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_EXISTENCE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/existence.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LOCUS_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/locus-result.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_SEGMENT_PARSE := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/segment-parse.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_FILTER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/filter.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_FILTER_RESULT := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/filter-result.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_UNIQUENESS := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/uniqueness.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ORDER := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/order.carrier
VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LINES := $(MORPHISM_CODEBASE_VOLUME_OBSERVATION_ROOT)/name-segment-excluded/lines.txt

.PHONY: morphism-codebase-volume-source-observation-name-segment-excluded
morphism-codebase-volume-source-observation-name-segment-excluded: $(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LINES)
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_ARGV_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PARSE),$(VOLUME_OBSERVATION_PATH_ORDER),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.input.parse.process,$(MORPHISM_CODEBASE_VOLUME_OBSERVATION_SOURCE_ROOT) $(VOLUME_OBSERVATION_EXCLUDED_NAMES)))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LINE_NORMALIZATION),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.line.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_NORMALIZATION),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LINE_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.path.normalization.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_PATHNAME),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_NORMALIZATION),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.root.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_ABSOLUTE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.root.absolute.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_DIRECTORY),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_ABSOLUTE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.root.directory.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_PRESENCE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ROOT_DIRECTORY),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.name.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_UNIQUENESS),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_PRESENCE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.name.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_ELEMENT_PRESENCE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.name.element.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_IDENTITY),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_ELEMENT_PRESENCE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.name.identity.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_SEPARATOR),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_IDENTITY),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.name.separator.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PRESENCE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_NAME_SEPARATOR),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.path.presence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PATHNAME),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PRESENCE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.path.pathname.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_RELATIVE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PATHNAME),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.path.relative.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PARENT),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_RELATIVE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.path.parent.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LOCUS),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_PATH_PARENT),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.locus.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_EXISTENCE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LOCUS),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.path.existence.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LOCUS_RESULT),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_EXISTENCE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.locus.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_SEGMENT_PARSE),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LOCUS_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.segment.parse.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_FILTER),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_SEGMENT_PARSE),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.segment.filter.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_FILTER_RESULT),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_FILTER),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.segment.result.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_UNIQUENESS),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_FILTER_RESULT),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.uniqueness.validation.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ORDER),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_UNIQUENESS),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.order.projection.process))
$(eval $(call MORPHISM_CODEBASE_VOLUME_OPERATION_EDGE,$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_LINES),$(VOLUME_OBSERVATION_NAME_SEGMENT_EXCLUDED_ORDER),silmaril.sparky.morphism.codebase.volume.source.observation.name_segment_excluded.line.encode.process))
