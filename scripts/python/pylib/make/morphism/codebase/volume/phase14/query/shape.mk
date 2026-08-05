VOLUME_PHASE14_QUERY_OBJECT_SHAPE := $(VOLUME_PHASE14_OUTPUT)/query-object.valid
VOLUME_PHASE14_QUERY_FIELD_PRESENCE := $(VOLUME_PHASE14_OUTPUT)/query-field-presence.valid
VOLUME_PHASE14_QUERY_RECORDS_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-records-type.valid
VOLUME_PHASE14_QUERY_COUNT_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-count-type.valid
VOLUME_PHASE14_QUERY_COUNT_EQUALITY := $(VOLUME_PHASE14_OUTPUT)/query-count-equality.valid
VOLUME_PHASE14_QUERY_SELECTED_TIER_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-selected-tier-type.valid
VOLUME_PHASE14_QUERY_SELECTED_TIER_NONEMPTY := $(VOLUME_PHASE14_OUTPUT)/query-selected-tier-nonempty.valid
VOLUME_PHASE14_QUERY_TIERS_CONSULTED_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-tiers-consulted-type.valid
VOLUME_PHASE14_QUERY_TIERS_CONSULTED_MEMBERSHIP := $(VOLUME_PHASE14_OUTPUT)/query-tiers-consulted-membership.valid
VOLUME_PHASE14_QUERY_TIERS_AVAILABLE_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-tiers-available-type.valid
VOLUME_PHASE14_QUERY_TIERS_AVAILABLE_MEMBERSHIP := $(VOLUME_PHASE14_OUTPUT)/query-tiers-available-membership.valid
VOLUME_PHASE14_QUERY_ROUTE_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-route-type.valid
VOLUME_PHASE14_QUERY_ROUTE_NONEMPTY := $(VOLUME_PHASE14_OUTPUT)/query-route-nonempty.valid
VOLUME_PHASE14_QUERY_COMPLETENESS_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-completeness-type.valid
VOLUME_PHASE14_QUERY_COMPLETENESS_NONEMPTY := $(VOLUME_PHASE14_OUTPUT)/query-completeness-nonempty.valid
VOLUME_PHASE14_QUERY_RECORD_TYPE := $(VOLUME_PHASE14_OUTPUT)/query-record-type.valid
VOLUME_PHASE14_QUERY_SHAPE := $(VOLUME_PHASE14_OUTPUT)/query-record-event-type.valid

$(VOLUME_PHASE14_QUERY_OBJECT_SHAPE): $(VOLUME_PHASE14_QUERY_OBJECT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.shape.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_FIELD_PRESENCE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_OBJECT_SHAPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.field.presence.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_RECORDS_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_FIELD_PRESENCE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.records.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_COUNT_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_RECORDS_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.count.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_COUNT_EQUALITY): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_COUNT_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.count.equality.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_SELECTED_TIER_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_COUNT_EQUALITY)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.selected_tier.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_SELECTED_TIER_NONEMPTY): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_SELECTED_TIER_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.selected_tier.nonempty.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_TIERS_CONSULTED_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_SELECTED_TIER_NONEMPTY)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.tiers_consulted.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_TIERS_CONSULTED_MEMBERSHIP): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_TIERS_CONSULTED_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.tiers_consulted.membership.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_TIERS_AVAILABLE_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_TIERS_CONSULTED_MEMBERSHIP)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.tiers_available.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_TIERS_AVAILABLE_MEMBERSHIP): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_TIERS_AVAILABLE_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.tiers_available.membership.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_ROUTE_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_TIERS_AVAILABLE_MEMBERSHIP)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.route.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_ROUTE_NONEMPTY): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_ROUTE_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.route.nonempty.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_COMPLETENESS_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_ROUTE_NONEMPTY)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.completeness.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_COMPLETENESS_NONEMPTY): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_COMPLETENESS_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.completeness.nonempty.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_RECORD_TYPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_COMPLETENESS_NONEMPTY)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.record.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_SHAPE): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_RECORD_TYPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.record.event.type.validation.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"
