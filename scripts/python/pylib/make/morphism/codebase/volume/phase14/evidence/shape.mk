VOLUME_PHASE14_ENVELOPE_GATE_COUNT := $(VOLUME_PHASE14_OUTPUT)/evidence-gate-count.valid
VOLUME_PHASE14_ENVELOPE_DIMENSION_COUNT := $(VOLUME_PHASE14_OUTPUT)/evidence-dimension-count.valid
VOLUME_PHASE14_ENVELOPE_RECORDS_TYPE := $(VOLUME_PHASE14_OUTPUT)/evidence-records-type.valid
VOLUME_PHASE14_ENVELOPE_SHAPE := $(VOLUME_PHASE14_OUTPUT)/evidence-record-count.valid

$(VOLUME_PHASE14_ENVELOPE_GATE_COUNT): $(VOLUME_PHASE14_ENVELOPE_OBJECT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.evidence.shape.process <"$(VOLUME_PHASE14_ENVELOPE_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_ENVELOPE_DIMENSION_COUNT): $(VOLUME_PHASE14_ENVELOPE_OBJECT) $(VOLUME_PHASE14_ENVELOPE_GATE_COUNT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.evidence.dimension.count.validation.process <"$(VOLUME_PHASE14_ENVELOPE_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_ENVELOPE_RECORDS_TYPE): $(VOLUME_PHASE14_ENVELOPE_OBJECT) $(VOLUME_PHASE14_ENVELOPE_DIMENSION_COUNT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.evidence.records.type.validation.process <"$(VOLUME_PHASE14_ENVELOPE_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_ENVELOPE_SHAPE): $(VOLUME_PHASE14_ENVELOPE_OBJECT) $(VOLUME_PHASE14_ENVELOPE_RECORDS_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.evidence.record.count.validation.process <"$(VOLUME_PHASE14_ENVELOPE_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"
