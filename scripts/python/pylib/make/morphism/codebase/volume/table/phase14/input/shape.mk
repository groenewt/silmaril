VOLUME_PHASE14_TABLE_INPUT_OBJECT_SHAPE := $(VOLUME_PHASE14_TABLE_OUTPUT)/input-object.valid
VOLUME_PHASE14_TABLE_INPUT_RECORDS_PRESENCE := $(VOLUME_PHASE14_TABLE_OUTPUT)/input-records-presence.valid
VOLUME_PHASE14_TABLE_INPUT_RECORDS_TYPE := $(VOLUME_PHASE14_TABLE_OUTPUT)/input-records-type.valid
VOLUME_PHASE14_TABLE_INPUT_SHAPE := $(VOLUME_PHASE14_TABLE_OUTPUT)/input-record-type.valid

$(VOLUME_PHASE14_TABLE_INPUT_OBJECT_SHAPE): $(VOLUME_PHASE14_TABLE_INPUT_OBJECT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.input.shape.validation.process <"$(VOLUME_PHASE14_TABLE_INPUT_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_INPUT_RECORDS_PRESENCE): $(VOLUME_PHASE14_TABLE_INPUT_OBJECT) $(VOLUME_PHASE14_TABLE_INPUT_OBJECT_SHAPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.input.records.presence.validation.process <"$(VOLUME_PHASE14_TABLE_INPUT_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_INPUT_RECORDS_TYPE): $(VOLUME_PHASE14_TABLE_INPUT_OBJECT) $(VOLUME_PHASE14_TABLE_INPUT_RECORDS_PRESENCE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.input.records.type.validation.process <"$(VOLUME_PHASE14_TABLE_INPUT_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_INPUT_SHAPE): $(VOLUME_PHASE14_TABLE_INPUT_OBJECT) $(VOLUME_PHASE14_TABLE_INPUT_RECORDS_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.input.record.type.validation.process <"$(VOLUME_PHASE14_TABLE_INPUT_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"
