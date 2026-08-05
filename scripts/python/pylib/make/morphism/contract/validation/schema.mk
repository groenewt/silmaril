.PHONY: morphism-contract-validation-schema-canonicalize
morphism-contract-validation-schema-canonicalize: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/canonicalize/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/canonicalize/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/canonicalize/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/canonicalize/output/process.py $(MCV_CANONICALIZE_FRAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.canonicalize.output.process <"$(MCV_CANONICALIZE_FRAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/canonicalize/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/canonicalize/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.canonicalize.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-schema-diagnostic
morphism-contract-validation-schema-diagnostic: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/diagnostic/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/diagnostic/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/diagnostic/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/diagnostic/output/process.py $(MCV_DIAGNOSTIC_FRAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.diagnostic.output.process <"$(MCV_DIAGNOSTIC_FRAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/diagnostic/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/diagnostic/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.diagnostic.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-schema-digest
morphism-contract-validation-schema-digest: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/digest/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/digest/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/digest/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/digest/output/process.py $(MCV_DIGEST_FRAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.digest.output.process <"$(MCV_DIGEST_FRAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/digest/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/digest/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.digest.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-schema-equality
morphism-contract-validation-schema-equality: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/left.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/equality/left/frame/process.py $(MCV_EQUALITY_LEFT)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.equality.left.frame.process <"$(MCV_EQUALITY_LEFT)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/right.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/equality/right/frame/process.py $(MCV_EQUALITY_RIGHT)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.equality.right.frame.process <"$(MCV_EQUALITY_RIGHT)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/equality/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/left.frame $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/right.frame
	@mkdir -p "$(@D)"
	@set +e; cat "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/left.frame" "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/right.frame" | PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.equality.output.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/equality/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/equality/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.equality.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-schema-format-date-time
morphism-contract-validation-schema-format-date-time: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification/accepted.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/date/time/classification/accepted/process.py $(MCV_DATE_TIME_VALUE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.date.time.classification.accepted.process <"$(MCV_DATE_TIME_VALUE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification/decode_failure.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/date/time/classification/decode_failure/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification/accepted.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.date.time.classification.decode_failure.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification/accepted.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/date/time/classification/rejected/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification/decode_failure.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.date.time.classification.rejected.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification/decode_failure.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/date/time/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.date.time.output.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/date/time/effect/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.date.time.effect.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/date/time/classification.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-schema-format-uri
morphism-contract-validation-schema-format-uri: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification/accepted.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/classification/accepted/process.py $(MCV_URI_VALUE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.classification.accepted.process <"$(MCV_URI_VALUE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification/decode_failure.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/classification/decode_failure/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification/accepted.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.classification.decode_failure.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification/accepted.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/classification/rejected/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification/decode_failure.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.classification.rejected.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification/decode_failure.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.output.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/effect/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.effect.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/classification.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-schema-format-uri-reference
morphism-contract-validation-schema-format-uri-reference: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification/accepted.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/reference/classification/accepted/process.py $(MCV_URI_REFERENCE_VALUE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.classification.accepted.process <"$(MCV_URI_REFERENCE_VALUE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification/decode_failure.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/reference/classification/decode_failure/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification/accepted.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.classification.decode_failure.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification/accepted.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/reference/classification/rejected/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification/decode_failure.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.classification.rejected.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification/decode_failure.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/reference/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.output.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/schema/format/uri/reference/effect/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification.bin
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.schema.format.uri.reference.effect.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/schema/format/uri/reference/classification.bin" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
