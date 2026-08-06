MORPHISM_ONTOLOGY_VALIDATION_SOURCE_ROOT := $(CURDIR)/src
MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT := $(CURDIR)/build/morphism/ontology/validation
MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT := $(abspath $(CURDIR)/../../..)
MORPHISM_ONTOLOGY_VALIDATION_CONSOLIDATED := $(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)/ontology/silmaril-consolidated.ttl
MORPHISM_ONTOLOGY_VALIDATION_SHAPES := $(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)/ontology/shapes.ttl

.PHONY: morphism-ontology-validation

morphism-ontology-validation: $(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/document-parse.out $(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/shapes-conformance.out $(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/queries-parse.out $(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/queries-execution.out
	@cat $^

$(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/document-parse.out: $(MORPHISM_ONTOLOGY_VALIDATION_CONSOLIDATED)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_ONTOLOGY_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.ontology.document.parse.process <"$(MORPHISM_ONTOLOGY_VALIDATION_CONSOLIDATED)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/shapes-conformance.out: $(MORPHISM_ONTOLOGY_VALIDATION_CONSOLIDATED) $(MORPHISM_ONTOLOGY_VALIDATION_SHAPES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_ONTOLOGY_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.ontology.shapes.conformance.process "$(MORPHISM_ONTOLOGY_VALIDATION_SHAPES)" <"$(MORPHISM_ONTOLOGY_VALIDATION_CONSOLIDATED)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.pending" >&2; cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/queries-parse.out: $(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)/ontology/queries.sparql $(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)/ontology/geosparql.sparql
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_ONTOLOGY_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.ontology.queries.parse.process "$(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_ONTOLOGY_VALIDATION_ARTIFACT_ROOT)/queries-execution.out: $(MORPHISM_ONTOLOGY_VALIDATION_CONSOLIDATED) $(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)/ontology/queries.sparql
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_ONTOLOGY_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.ontology.queries.execution.process "$(MORPHISM_ONTOLOGY_VALIDATION_REPOSITORY_ROOT)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
