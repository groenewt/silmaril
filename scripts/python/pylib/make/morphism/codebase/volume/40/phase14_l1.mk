VOLUME_40_PHASE14_L1_OUTPUT := $(VOLUME_40_BUILD_ROOT)/phase14/l1-snapshot
VOLUME_40_PHASE14_L1_SOURCE_JSON := $(VOLUME_40_PHASE14_L1_OUTPUT)/source.json
VOLUME_40_PHASE14_L1_SOURCE_OBJECT := $(VOLUME_40_PHASE14_L1_OUTPUT)/source.carrier
VOLUME_40_PHASE14_L1_CANONICAL := $(VOLUME_40_PHASE14_L1_OUTPUT)/canonical.carrier
VOLUME_40_PHASE14_L1_SEQUENCES := $(VOLUME_40_PHASE14_L1_OUTPUT)/sequences.carrier
VOLUME_40_PHASE14_L1_KEYS := $(VOLUME_40_PHASE14_L1_OUTPUT)/keys.carrier
VOLUME_40_PHASE14_L1_ORDER := $(VOLUME_40_PHASE14_L1_OUTPUT)/order.carrier
VOLUME_40_PHASE14_L1_ORDERED := $(VOLUME_40_PHASE14_L1_OUTPUT)/ordered.carrier
VOLUME_40_PHASE14_L1_LATEST := $(VOLUME_40_PHASE14_L1_OUTPUT)/latest.carrier
VOLUME_40_PHASE14_L1_ENVELOPE_OBJECT := $(VOLUME_40_PHASE14_L1_OUTPUT)/evidence-envelope.carrier
VOLUME_40_PHASE14_L1_ENVELOPE := $(VOLUME_40_PHASE14_L1_OUTPUT)/evidence-envelope.json

ifeq ($(VOLUME_40_PHASE14_SOURCE),l1_snapshot)
VOLUME_PHASE14_TABLE_INPUT := $(VOLUME_40_PHASE14_L1_ENVELOPE)
endif

.PHONY: volume-40-phase14-l1-snapshot
volume-40-phase14-l1-snapshot: $(VOLUME_40_PHASE14_L1_ENVELOPE)

$(VOLUME_40_PHASE14_L1_OUTPUT):
	mkdir -p "$@"

$(VOLUME_40_PHASE14_L1_SOURCE_JSON): FORCE | $(VOLUME_40_PHASE14_L1_OUTPUT)
	@test -n "$(VOLUME_40_PHASE14_L1_OK_GLOB)" || { printf '%s\n' 'VOLUME_40_PHASE14_L1_OK_GLOB is required' >&2; exit 64; }
	@test -n "$(VOLUME_40_PHASE14_L1_ERROR_GLOB)" || { printf '%s\n' 'VOLUME_40_PHASE14_L1_ERROR_GLOB is required' >&2; exit 64; }
	@set +e; VOLUME_PHASE14_L1_OK_GLOB="$(VOLUME_40_PHASE14_L1_OK_GLOB)" VOLUME_PHASE14_L1_ERROR_GLOB="$(VOLUME_40_PHASE14_L1_ERROR_GLOB)" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.l1.source.observation.process >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_SOURCE_OBJECT): $(VOLUME_40_PHASE14_L1_SOURCE_JSON)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.json.parse.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_CANONICAL): $(VOLUME_40_PHASE14_L1_SOURCE_OBJECT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.table.phase14.record.canonical.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_SEQUENCES): $(VOLUME_40_PHASE14_L1_CANONICAL)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.l1.record.sequence.numeric.normalization.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_KEYS): $(VOLUME_40_PHASE14_L1_SEQUENCES)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.l1.record.order.key.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_ORDER): $(VOLUME_40_PHASE14_L1_KEYS)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.l1.record.order.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_ORDERED): $(VOLUME_40_PHASE14_L1_ORDER)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.l1.record.order.result.projection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_LATEST): $(VOLUME_40_PHASE14_L1_ORDERED)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.l1.record.event.latest.selection.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_ENVELOPE_OBJECT): $(VOLUME_40_PHASE14_L1_LATEST)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.query.envelope.construction.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"

$(VOLUME_40_PHASE14_L1_ENVELOPE): $(VOLUME_40_PHASE14_L1_ENVELOPE_OBJECT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.phase14.json.encode.process <"$<" >"$@.tmp" 2>"$@.error"; status=$$?; set -e; if test "$$status" -ne 0; then cat "$@.error" >&2; exit "$$status"; fi; rm -f "$@.error"; mv "$@.tmp" "$@"
