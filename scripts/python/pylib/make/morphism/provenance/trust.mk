MORPHISM_PROVENANCE_TRUST_SOURCE_ROOT := $(CURDIR)/src
MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT := $(CURDIR)/build/morphism/provenance/trust
MORPHISM_PROVENANCE_TRUST_REPOSITORY_ROOT := $(abspath $(CURDIR)/../../..)
MORPHISM_PROVENANCE_TRUST_MODEL := $(MORPHISM_PROVENANCE_TRUST_REPOSITORY_ROOT)/basicttl/commit_signing_trust.ttl
MORPHISM_PROVENANCE_TRUST_COMMITTED_MANIFEST := $(MORPHISM_PROVENANCE_TRUST_REPOSITORY_ROOT)/keys/trust-manifest.txt

.PHONY: morphism-provenance-trust-manifest morphism-provenance-trust-manifest-check

morphism-provenance-trust-manifest: $(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/render.out

$(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/extraction.out: $(MORPHISM_PROVENANCE_TRUST_SOURCE_ROOT)/silmaril/sparky/morphism/provenance/trust/manifest/extraction/process.py $(MORPHISM_PROVENANCE_TRUST_MODEL)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_TRUST_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.trust.manifest.extraction.process <"$(MORPHISM_PROVENANCE_TRUST_MODEL)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/render.out: $(MORPHISM_PROVENANCE_TRUST_SOURCE_ROOT)/silmaril/sparky/morphism/provenance/trust/manifest/render/process.py $(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/extraction.out
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_TRUST_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.trust.manifest.render.process <"$(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/extraction.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

morphism-provenance-trust-manifest-check: $(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/render.out
	@cmp "$(MORPHISM_PROVENANCE_TRUST_ARTIFACT_ROOT)/manifest/render.out" "$(MORPHISM_PROVENANCE_TRUST_COMMITTED_MANIFEST)" || { printf '%s\n' 'trust-manifest drift: keys/trust-manifest.txt does not match basicttl/commit_signing_trust.ttl' >&2; exit 1; }
	@printf '%s\n' 'trust-manifest in sync with the trust model'
