MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT ?= $(CURDIR)/src
MORPHISM_CODEBASE_VOLUME_TABLE_ARTIFACT_ROOT ?= $(CURDIR)/.artifacts/morphism/codebase/volume/table

define MORPHISM_CODEBASE_VOLUME_TABLE_EDGE
$1: $2 $(MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT)/$(subst .,/,$3).py
	@mkdir -p "$$(@D)"
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $3 <"$2" >"$$@.pending" 2>"$$@.stderr"; STATUS=$$$$?; printf '%s\n' "$$$$STATUS" >"$$@.status"; set -e; if [ "$$$$STATUS" -ne 0 ]; then cat "$$@.stderr" >&2; exit "$$$$STATUS"; fi; mv "$$@.pending" "$$@"
endef

define MORPHISM_CODEBASE_VOLUME_TABLE_NAMED_INPUT_EDGE
$1: $(MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT)/$(subst .,/,$2).py $3
	@mkdir -p "$$(@D)"
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CODEBASE_VOLUME_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m $2 $3 >"$$@.pending" 2>"$$@.stderr"; STATUS=$$$$?; printf '%s\n' "$$$$STATUS" >"$$@.status"; set -e; if [ "$$$$STATUS" -ne 0 ]; then cat "$$@.stderr" >&2; exit "$$$$STATUS"; fi; mv "$$@.pending" "$$@"
endef
