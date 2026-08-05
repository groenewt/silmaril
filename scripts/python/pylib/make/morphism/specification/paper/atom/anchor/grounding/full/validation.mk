.DELETE_ON_ERROR:

ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON ?= /home/tristan/anaconda3/envs/silmaril/bin/python
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SOURCE_ROOT ?= $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../../../../../../../../src)
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PAPERS_DIRECTORY ?= src/silmaril_specs/data/papers
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT ?= build/morphism/specification/paper/atom/anchor/grounding/full/validation
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PRESENCE := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/00-papers-directory-presence.frame
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_DISCOVERY := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/01-specification-source-discovery.frame
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_ORDERED_SOURCES := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/02-specification-source-canonical-order.frame
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_INSTANCE_RELATION := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/03-document-instance-relation.frame
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_GROUNDING_RELATION := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/04-instance-grounding-classification.frame
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SLUG_AGGREGATE := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/05-paper-slug-aggregate.frame
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_JSON ?= $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/06-summary.json
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_TEXT ?= $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/07-summary.txt
ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_RESULT := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)/08-completeness.valid

export PYTHONDONTWRITEBYTECODE := 1
export PYTHONPATH := $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SOURCE_ROOT)

.PHONY: atom-anchor-grounding-full-json atom-anchor-grounding-full-text atom-anchor-grounding-full-force
atom-anchor-grounding-full-json: $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_RESULT)

atom-anchor-grounding-full-text: $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_TEXT) $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_RESULT)

atom-anchor-grounding-full-force:

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT):
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.stage.directory.construction.process "$@"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PRESENCE): atom-anchor-grounding-full-force | $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_STAGE_ROOT)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.papers.directory.presence.validation.process "$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PAPERS_DIRECTORY)" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_DISCOVERY): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PRESENCE)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.specification.source.discovery.process "$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PAPERS_DIRECTORY)" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_ORDERED_SOURCES): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_DISCOVERY)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.specification.source.canonical.order.projection.process <"$<" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_INSTANCE_RELATION): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_ORDERED_SOURCES)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.specification.document.instance.relation.parsing.process "$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PAPERS_DIRECTORY)" <"$<" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_GROUNDING_RELATION): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_INSTANCE_RELATION)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.instance.grounding.classification.process <"$<" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SLUG_AGGREGATE): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_GROUNDING_RELATION)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.paper.slug.aggregation.process <"$<" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_JSON): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SLUG_AGGREGATE)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.json.construction.process "$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PAPERS_DIRECTORY)" <"$<" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_TEXT): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_JSON)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.text.projection.process <"$<" >"$@" 2>"$@.stderr"

$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_RESULT): $(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_SUMMARY_JSON)
	$(ATOM_ANCHOR_GROUNDING_FULL_VALIDATION_PYTHON) -m silmaril.sparky.morphism.specification.paper.atom.anchor.grounding.full.validation.summary.completeness.validation.process <"$<" >"$@" 2>"$@.stderr"
