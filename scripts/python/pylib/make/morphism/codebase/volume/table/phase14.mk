VOLUME_PHASE14_TABLE_OUTPUT ?= $(CURDIR)/build/morphism/codebase/volume/table/phase14
VOLUME_PHASE14_TABLE_INPUT ?= $(VOLUME_PHASE14_ENVELOPE)
VOLUME_PHASE14_TABLE_INPUT_OBJECT := $(VOLUME_PHASE14_TABLE_OUTPUT)/input.carrier
VOLUME_PHASE14_TABLE_INPUT_RECORDS := $(VOLUME_PHASE14_TABLE_OUTPUT)/input-records.carrier
VOLUME_PHASE14_TABLE_CANONICAL_RECORDS := $(VOLUME_PHASE14_TABLE_OUTPUT)/canonical-records.carrier
VOLUME_PHASE14_TABLE_CANONICAL_EVENT_NAMES := $(VOLUME_PHASE14_TABLE_OUTPUT)/canonical-event-names.carrier
VOLUME_PHASE14_TABLE_EVENT_COUNTS := $(VOLUME_PHASE14_TABLE_OUTPUT)/event-counts.carrier
VOLUME_PHASE14_TABLE_EVENT_DUPLICATES := $(VOLUME_PHASE14_TABLE_OUTPUT)/event-duplicates.carrier
VOLUME_PHASE14_TABLE_UNIQUENESS := $(VOLUME_PHASE14_TABLE_OUTPUT)/record-uniqueness.valid
VOLUME_PHASE14_TABLE_RECORD_INDEX := $(VOLUME_PHASE14_TABLE_OUTPUT)/record-index.carrier
VOLUME_PHASE14_TABLE_GATES := $(VOLUME_PHASE14_TABLE_OUTPUT)/gates.carrier
VOLUME_PHASE14_TABLE_DIMENSIONS := $(VOLUME_PHASE14_TABLE_OUTPUT)/dimensions.carrier
VOLUME_PHASE14_TABLE_CARTESIAN := $(VOLUME_PHASE14_TABLE_OUTPUT)/cartesian.carrier
VOLUME_PHASE14_TABLE_MATRIX_COORDINATES := $(VOLUME_PHASE14_TABLE_OUTPUT)/matrix-coordinates.carrier
VOLUME_PHASE14_TABLE_EVENT_COORDINATES := $(VOLUME_PHASE14_TABLE_OUTPUT)/event-coordinates.carrier
VOLUME_PHASE14_TABLE_RECORD_LOOKUPS := $(VOLUME_PHASE14_TABLE_OUTPUT)/record-lookups.carrier
VOLUME_PHASE14_TABLE_MATRIX := $(VOLUME_PHASE14_TABLE_OUTPUT)/matrix.carrier
VOLUME_PHASE14_TABLE_CLASSIFIED := $(VOLUME_PHASE14_TABLE_OUTPUT)/classified.carrier
VOLUME_PHASE14_TABLE_STATUS := $(VOLUME_PHASE14_TABLE_OUTPUT)/status.carrier
VOLUME_PHASE14_TABLE_IDENTITY_FIELDS := $(VOLUME_PHASE14_TABLE_OUTPUT)/identity-fields.carrier
VOLUME_PHASE14_TABLE_IDENTITY_PRESENT_FIELDS := $(VOLUME_PHASE14_TABLE_OUTPUT)/identity-present-fields.carrier
VOLUME_PHASE14_TABLE_IDENTITY_CONSTRUCTED := $(VOLUME_PHASE14_TABLE_OUTPUT)/identity-constructed.carrier
VOLUME_PHASE14_TABLE_IDENTITIES := $(VOLUME_PHASE14_TABLE_OUTPUT)/identities.carrier
VOLUME_PHASE14_TABLE_IDENTITY_MISSING := $(VOLUME_PHASE14_TABLE_OUTPUT)/identity-missing.carrier
VOLUME_PHASE14_TABLE_IDENTITY_PRESENCE := $(VOLUME_PHASE14_TABLE_OUTPUT)/identity-presence.valid
VOLUME_PHASE14_TABLE_EVIDENCE_ABSENCE_CLASSIFIED := $(VOLUME_PHASE14_TABLE_OUTPUT)/evidence-absence-classified.carrier
VOLUME_PHASE14_TABLE_EVIDENCE_ABSENCE := $(VOLUME_PHASE14_TABLE_OUTPUT)/evidence-absence-attached.carrier
VOLUME_PHASE14_TABLE_EVIDENCE_ENCODED := $(VOLUME_PHASE14_TABLE_OUTPUT)/evidence-encoded.carrier
VOLUME_PHASE14_TABLE_EVIDENCE := $(VOLUME_PHASE14_TABLE_OUTPUT)/evidence.carrier
VOLUME_PHASE14_TABLE_ROWS := $(VOLUME_PHASE14_TABLE_OUTPUT)/rows.carrier
VOLUME_PHASE14_TABLE_CSV := $(VOLUME_PHASE14_TABLE_OUTPUT)/phase14.csv

include make/morphism/codebase/volume/table/phase14/input/shape.mk

.PHONY: volume-phase14-table
volume-phase14-table: $(VOLUME_PHASE14_TABLE_CSV)

$(VOLUME_PHASE14_TABLE_OUTPUT):
	mkdir -p "$@"

$(VOLUME_PHASE14_TABLE_INPUT_OBJECT): $(VOLUME_PHASE14_TABLE_INPUT) | $(VOLUME_PHASE14_TABLE_OUTPUT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.input.json.parse.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_INPUT_RECORDS): $(VOLUME_PHASE14_TABLE_INPUT_OBJECT) $(VOLUME_PHASE14_TABLE_INPUT_SHAPE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.input.records.projection.process <"$(VOLUME_PHASE14_TABLE_INPUT_OBJECT)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_CANONICAL_RECORDS): $(VOLUME_PHASE14_TABLE_INPUT_RECORDS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.canonical.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_CANONICAL_EVENT_NAMES): $(VOLUME_PHASE14_TABLE_CANONICAL_RECORDS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.event.name.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVENT_COUNTS): $(VOLUME_PHASE14_TABLE_CANONICAL_EVENT_NAMES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.event.count.aggregation.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVENT_DUPLICATES): $(VOLUME_PHASE14_TABLE_EVENT_COUNTS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.event.duplicate.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_UNIQUENESS): $(VOLUME_PHASE14_TABLE_EVENT_DUPLICATES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.uniqueness.validation.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_RECORD_INDEX): $(VOLUME_PHASE14_TABLE_CANONICAL_RECORDS) $(VOLUME_PHASE14_TABLE_UNIQUENESS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.index.projection.process <"$(VOLUME_PHASE14_TABLE_CANONICAL_RECORDS)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_GATES): | $(VOLUME_PHASE14_TABLE_OUTPUT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.matrix.gate.expansion.process </dev/null >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_DIMENSIONS): | $(VOLUME_PHASE14_TABLE_OUTPUT)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.matrix.dimension.index.projection.process </dev/null >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_CARTESIAN): $(VOLUME_PHASE14_TABLE_GATES) $(VOLUME_PHASE14_TABLE_DIMENSIONS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.matrix.cartesian.expansion.process "$(VOLUME_PHASE14_TABLE_DIMENSIONS)" <"$(VOLUME_PHASE14_TABLE_GATES)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_MATRIX_COORDINATES): $(VOLUME_PHASE14_TABLE_CARTESIAN)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.matrix.coordinate.construction.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVENT_COORDINATES): $(VOLUME_PHASE14_TABLE_MATRIX_COORDINATES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.event.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_RECORD_LOOKUPS): $(VOLUME_PHASE14_TABLE_EVENT_COORDINATES) $(VOLUME_PHASE14_TABLE_RECORD_INDEX)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.lookup.process "$(VOLUME_PHASE14_TABLE_RECORD_INDEX)" <"$(VOLUME_PHASE14_TABLE_EVENT_COORDINATES)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_MATRIX): $(VOLUME_PHASE14_TABLE_RECORD_LOOKUPS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.attachment.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_CLASSIFIED): $(VOLUME_PHASE14_TABLE_MATRIX)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.status.classification.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_STATUS): $(VOLUME_PHASE14_TABLE_CLASSIFIED)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.status.attachment.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_IDENTITY_FIELDS): $(VOLUME_PHASE14_TABLE_STATUS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.identity.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_IDENTITY_PRESENT_FIELDS): $(VOLUME_PHASE14_TABLE_IDENTITY_FIELDS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.identity.present.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_IDENTITY_CONSTRUCTED): $(VOLUME_PHASE14_TABLE_IDENTITY_PRESENT_FIELDS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.identity.construction.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_IDENTITIES): $(VOLUME_PHASE14_TABLE_IDENTITY_CONSTRUCTED)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.identity.attachment.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_IDENTITY_MISSING): $(VOLUME_PHASE14_TABLE_IDENTITIES)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.identity.missing.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_IDENTITY_PRESENCE): $(VOLUME_PHASE14_TABLE_IDENTITY_MISSING)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.identity.presence.validation.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVIDENCE_ABSENCE_CLASSIFIED): $(VOLUME_PHASE14_TABLE_IDENTITIES) $(VOLUME_PHASE14_TABLE_IDENTITY_PRESENCE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.absence.projection.process <"$(VOLUME_PHASE14_TABLE_IDENTITIES)" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVIDENCE_ABSENCE): $(VOLUME_PHASE14_TABLE_EVIDENCE_ABSENCE_CLASSIFIED)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.absence.attachment.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVIDENCE_ENCODED): $(VOLUME_PHASE14_TABLE_EVIDENCE_ABSENCE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.json.encode.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_EVIDENCE): $(VOLUME_PHASE14_TABLE_EVIDENCE_ENCODED)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.evidence.reference.attachment.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_ROWS): $(VOLUME_PHASE14_TABLE_EVIDENCE)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.construct.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_PHASE14_TABLE_CSV): $(VOLUME_PHASE14_TABLE_ROWS)
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(CURDIR)/src" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.csv.encode.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"
