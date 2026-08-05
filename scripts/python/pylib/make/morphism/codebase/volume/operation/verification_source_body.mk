VOLUME_SOURCE_BODY_RECEIPT ?= $(CURDIR)/.artifacts/morphism/codebase/volume/verification/source-body-total-application.receipt
VOLUME_SOURCE_BODY_INPUTS := $(shell find $(CURDIR)/src -type f \( -name 'process.py' -o -path '*/process/command/value.py' \) -print | sort)
VOLUME_SOURCE_BODY_TEST := $(CURDIR)/tests/test_python_total_application_runtime.py

.PHONY: morphism-codebase-volume-source-body-verify
morphism-codebase-volume-source-body-verify: $(VOLUME_SOURCE_BODY_RECEIPT)

$(VOLUME_SOURCE_BODY_RECEIPT): $(VOLUME_SOURCE_BODY_INPUTS) $(VOLUME_SOURCE_BODY_TEST)
	@mkdir -p "$(@D)"
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m pytest -q "$(VOLUME_SOURCE_BODY_TEST)" >"$@.stdout.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stdout.pending"; cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.stdout.pending" "$@.stdout"; printf '%s\n' 'source_body_total_application=verified' 'scope=all_pylib_runtime_and_configured_child_bodies' >"$@.pending"; mv "$@.pending" "$@"
