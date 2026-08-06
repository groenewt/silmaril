MORPHISM_ONTOLOGY_CONSOLIDATION_SOURCE_ROOT := $(CURDIR)/src
MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT := $(CURDIR)/build/morphism/ontology/consolidation
MORPHISM_ONTOLOGY_CONSOLIDATION_REPOSITORY_ROOT := $(abspath $(CURDIR)/../../..)
MORPHISM_ONTOLOGY_CONSOLIDATION_CORPUS := $(MORPHISM_ONTOLOGY_CONSOLIDATION_REPOSITORY_ROOT)/basicttl
MORPHISM_ONTOLOGY_CONSOLIDATION_COMMITTED := $(MORPHISM_ONTOLOGY_CONSOLIDATION_REPOSITORY_ROOT)/ontology

define MORPHISM_ONTOLOGY_CONSOLIDATION_STEP
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_ONTOLOGY_CONSOLIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.ontology.consolidation.$(1).process $(2) $(3) >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
endef

.PHONY: morphism-ontology-consolidation morphism-ontology-consolidation-check morphism-ontology-consolidation-force
morphism-ontology-consolidation-force:

morphism-ontology-consolidation: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/silmaril-consolidated.ttl $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/shapes.ttl $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/queries.sparql $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/geosparql.sparql $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/manifest.ttl

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out: morphism-ontology-consolidation-force
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,source.discovery,"$(MORPHISM_ONTOLOGY_CONSOLIDATION_CORPUS)",)

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/namespace-union.out: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,namespace.union.projection,"$(MORPHISM_ONTOLOGY_CONSOLIDATION_CORPUS)",<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/corpus-tally.out: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,corpus.tally,"$(MORPHISM_ONTOLOGY_CONSOLIDATION_CORPUS)",<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/normalization.out: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,document.normalization,"$(MORPHISM_ONTOLOGY_CONSOLIDATION_CORPUS)",<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/source-discovery.out")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/silmaril-consolidated.ttl: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/corpus-tally.out $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/namespace-union.out $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/normalization.out
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,consolidated.render,"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/corpus-tally.out" "$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/namespace-union.out",<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/normalization.out")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/shapes.ttl: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/namespace-union.out
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,shapes.constraint.language.document.render,,<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/namespace-union.out")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/queries.sparql: morphism-ontology-consolidation-force
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,query.protocol.language.document.emission,,)

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/geosparql.sparql: morphism-ontology-consolidation-force
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,geographic.query.protocol.language.document.emission,,)

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/statement-tally.out: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/silmaril-consolidated.ttl
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,statement.tally,,<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/silmaril-consolidated.ttl")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/entity-tally.out: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/silmaril-consolidated.ttl
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,entity.tally,,<"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/silmaril-consolidated.ttl")

$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/manifest.ttl: $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/corpus-tally.out $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/statement-tally.out $(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/entity-tally.out
	$(call MORPHISM_ONTOLOGY_CONSOLIDATION_STEP,manifest.render,"$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/corpus-tally.out" "$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/statement-tally.out" "$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/entity-tally.out",)

morphism-ontology-consolidation-check: morphism-ontology-consolidation
	@STATUS=0; for f in silmaril-consolidated.ttl shapes.ttl queries.sparql geosparql.sparql manifest.ttl; do cmp "$(MORPHISM_ONTOLOGY_CONSOLIDATION_ARTIFACT_ROOT)/$$f" "$(MORPHISM_ONTOLOGY_CONSOLIDATION_COMMITTED)/$$f" || { printf 'ontology drift: ontology/%s does not match regeneration from basicttl/\n' "$$f" >&2; STATUS=1; }; done; exit $$STATUS
	@printf '%s\n' 'ontology artifacts in sync with basicttl sources'
