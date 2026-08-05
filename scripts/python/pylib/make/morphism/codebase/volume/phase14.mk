VOLUME_PHASE14_OUTPUT ?= $(CURDIR)/build/morphism/codebase/volume/phase14
VOLUME_PHASE14_CELL_COUNT ?= 104
VOLUME_PHASE14_QUERY := $(VOLUME_PHASE14_OUTPUT)/query.json
VOLUME_PHASE14_QUERY_OBJECT := $(VOLUME_PHASE14_OUTPUT)/query.carrier
VOLUME_PHASE14_QUERY_RECORDS := $(VOLUME_PHASE14_OUTPUT)/query-records.carrier
VOLUME_PHASE14_EVENT_NAMES := $(VOLUME_PHASE14_OUTPUT)/event-names.carrier
VOLUME_PHASE14_EVENT_NONCANONICAL := $(VOLUME_PHASE14_OUTPUT)/event-noncanonical.carrier
VOLUME_PHASE14_EVENT_MEMBERSHIP := $(VOLUME_PHASE14_OUTPUT)/event-membership.valid
VOLUME_PHASE14_EVENT_COUNTS := $(VOLUME_PHASE14_OUTPUT)/event-counts.carrier
VOLUME_PHASE14_EVENT_DUPLICATES := $(VOLUME_PHASE14_OUTPUT)/event-duplicates.carrier
VOLUME_PHASE14_EVENT_UNIQUENESS := $(VOLUME_PHASE14_OUTPUT)/event-uniqueness.valid
VOLUME_PHASE14_EVENT_MISSING := $(VOLUME_PHASE14_OUTPUT)/event-missing.carrier
VOLUME_PHASE14_EVENT_COMPLETENESS := $(VOLUME_PHASE14_OUTPUT)/event-completeness.valid
VOLUME_PHASE14_EVENT_INDEX := $(VOLUME_PHASE14_OUTPUT)/event-index.carrier
VOLUME_PHASE14_ORDERED_RECORDS := $(VOLUME_PHASE14_OUTPUT)/ordered-records.carrier
VOLUME_PHASE14_ENVELOPE_OBJECT := $(VOLUME_PHASE14_OUTPUT)/evidence-envelope.carrier
VOLUME_PHASE14_ENVELOPE := $(VOLUME_PHASE14_OUTPUT)/evidence-envelope.json

include make/morphism/codebase/volume/phase14/query/shape.mk
include make/morphism/codebase/volume/phase14/evidence/shape.mk

.PHONY: volume-phase14-evidence FORCE
volume-phase14-evidence: $(VOLUME_PHASE14_ENVELOPE)

FORCE:

$(VOLUME_PHASE14_OUTPUT):
	mkdir -p "$@"

$(VOLUME_PHASE14_QUERY): FORCE | $(VOLUME_PHASE14_OUTPUT)
	@test -n "$(VOLUME_TELEPHONE_QUERY)" || { printf '%s\n' 'VOLUME_TELEPHONE_QUERY is required' >&2; exit 64; }
	@test -n "$(VOLUME_PHASE14_QUERY_TIER)" || { printf '%s\n' 'VOLUME_PHASE14_QUERY_TIER is required' >&2; exit 64; }
	@set -- --tier "$(VOLUME_PHASE14_QUERY_TIER)" --last "$(VOLUME_PHASE14_CELL_COUNT)" --format json; \
	if test -n "$(VOLUME_PHASE14_FRAME_HEAD)"; then set -- "$$@" --frame-head "$(VOLUME_PHASE14_FRAME_HEAD)"; fi; \
	if test -n "$(VOLUME_PHASE14_QUERY_SCOPE)"; then set -- "$$@" --scope "$(VOLUME_PHASE14_QUERY_SCOPE)"; fi; \
	set +e; "$(VOLUME_TELEPHONE_QUERY)" "$$@" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_OBJECT): $(VOLUME_PHASE14_QUERY)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.json.parse.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_QUERY_RECORDS): $(VOLUME_PHASE14_QUERY_OBJECT) $(VOLUME_PHASE14_QUERY_SHAPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.records.projection.process <"$(VOLUME_PHASE14_QUERY_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_NAMES): $(VOLUME_PHASE14_QUERY_RECORDS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.name.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_NONCANONICAL): $(VOLUME_PHASE14_EVENT_NAMES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.noncanonical.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_MEMBERSHIP): $(VOLUME_PHASE14_EVENT_NONCANONICAL)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.membership.validation.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_COUNTS): $(VOLUME_PHASE14_EVENT_NAMES) $(VOLUME_PHASE14_EVENT_MEMBERSHIP)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.count.aggregation.process <"$(VOLUME_PHASE14_EVENT_NAMES)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_DUPLICATES): $(VOLUME_PHASE14_EVENT_COUNTS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.duplicate.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_UNIQUENESS): $(VOLUME_PHASE14_EVENT_DUPLICATES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.uniqueness.validation.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_MISSING): $(VOLUME_PHASE14_EVENT_NAMES) $(VOLUME_PHASE14_EVENT_UNIQUENESS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.missing.projection.process <"$(VOLUME_PHASE14_EVENT_NAMES)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_COMPLETENESS): $(VOLUME_PHASE14_EVENT_MISSING)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.completeness.validation.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_EVENT_INDEX): $(VOLUME_PHASE14_QUERY_RECORDS) $(VOLUME_PHASE14_EVENT_COMPLETENESS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.event.index.projection.process <"$(VOLUME_PHASE14_QUERY_RECORDS)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_ORDERED_RECORDS): $(VOLUME_PHASE14_EVENT_INDEX)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.cell.canonical_order.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_ENVELOPE_OBJECT): $(VOLUME_PHASE14_ORDERED_RECORDS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.envelope.construction.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_ENVELOPE): $(VOLUME_PHASE14_ENVELOPE_OBJECT) $(VOLUME_PHASE14_ENVELOPE_SHAPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.json.encode.process <"$(VOLUME_PHASE14_ENVELOPE_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; \
	rm -f "$@.error"; mv "$@.tmp" "$@"
