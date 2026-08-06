MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT := $(CURDIR)/src
MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT := $(CURDIR)/build/morphism/provenance/commit
MORPHISM_PROVENANCE_COMMIT_REPOSITORY_ROOT := $(abspath $(CURDIR)/../../..)
MORPHISM_PROVENANCE_COMMIT_KEYRING_HOME ?= $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/gnupg
MORPHISM_PROVENANCE_COMMIT_MANIFEST := $(MORPHISM_PROVENANCE_COMMIT_REPOSITORY_ROOT)/keys/trust-manifest.txt
MORPHISM_PROVENANCE_COMMIT_KEYS := $(wildcard $(MORPHISM_PROVENANCE_COMMIT_REPOSITORY_ROOT)/keys/*.asc)
PROVENANCE_COMMIT_REVISIONS ?= HEAD
# The observed git repository defaults to the working tree this pylib sits in;
# the server-side update bridge overrides it with the bare repository while the
# trust material resolves from the extracted trusted-revision tree.
PROVENANCE_COMMIT_GIT_REPOSITORY ?= $(MORPHISM_PROVENANCE_COMMIT_REPOSITORY_ROOT)

define MORPHISM_PROVENANCE_COMMIT_ENVELOPE
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
endef

.PHONY: morphism-provenance-commit-force morphism-provenance-commit-policy-default morphism-provenance-commit-policy-strict morphism-provenance-commit-policy-report
morphism-provenance-commit-force:

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/keyring.done: $(MORPHISM_PROVENANCE_COMMIT_KEYS)
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@mkdir -p "$(MORPHISM_PROVENANCE_COMMIT_KEYRING_HOME)"; chmod 700 "$(MORPHISM_PROVENANCE_COMMIT_KEYRING_HOME)"
	@set +e; GNUPGHOME="$(MORPHISM_PROVENANCE_COMMIT_KEYRING_HOME)" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.keyring.construction.process $(MORPHISM_PROVENANCE_COMMIT_KEYS) >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/verification.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/keyring.done morphism-provenance-commit-force
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; GNUPGHOME="$(MORPHISM_PROVENANCE_COMMIT_KEYRING_HOME)" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.observation.verification.process "$(PROVENANCE_COMMIT_GIT_REPOSITORY)" $(PROVENANCE_COMMIT_REVISIONS) >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/header.out: morphism-provenance-commit-force
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.observation.header.process "$(PROVENANCE_COMMIT_GIT_REPOSITORY)" $(PROVENANCE_COMMIT_REVISIONS) >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/signature-type.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/header.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.signature.type.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/header.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/record.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/signature-type.out $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/verification.out $(MORPHISM_PROVENANCE_COMMIT_MANIFEST)
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.record.merge.process "$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/signature-type.out" "$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/verification.out" "$(MORPHISM_PROVENANCE_COMMIT_MANIFEST)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-good.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/record.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.good.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/record.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-attested.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-good.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.attested.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-good.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-bad-signature.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-attested.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.bad.signature.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-attested.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-secure-shell.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-bad-signature.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.secure.shell.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-bad-signature.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-unsigned.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-secure-shell.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.unsigned.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-secure-shell.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classes.out: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-unsigned.out
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.classification.unknown.process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classified-unsigned.out" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

define MORPHISM_PROVENANCE_COMMIT_POLICY
	$(MORPHISM_PROVENANCE_COMMIT_ENVELOPE)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_PROVENANCE_COMMIT_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.provenance.commit.policy.$(1).process <"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classes.out" >"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/policy-$(1).out" 2>"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/policy-$(1).stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/policy-$(1).status"; set -e; cat "$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/policy-$(1).out"; if [ "$$STATUS" -ne 0 ]; then cat "$(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/policy-$(1).stderr" >&2; exit "$$STATUS"; fi
endef

morphism-provenance-commit-policy-default: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classes.out
	$(call MORPHISM_PROVENANCE_COMMIT_POLICY,default)

morphism-provenance-commit-policy-strict: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classes.out
	$(call MORPHISM_PROVENANCE_COMMIT_POLICY,strict)

morphism-provenance-commit-policy-report: $(MORPHISM_PROVENANCE_COMMIT_ARTIFACT_ROOT)/classes.out
	$(call MORPHISM_PROVENANCE_COMMIT_POLICY,report)
