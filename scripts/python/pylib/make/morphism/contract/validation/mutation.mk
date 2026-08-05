.PHONY: morphism-contract-validation-mutation-append-copy
morphism-contract-validation-mutation-append-copy: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/target.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/append/copy/target/frame/process.py $(MCV_APPEND_TARGET)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.append.copy.target.frame.process <"$(MCV_APPEND_TARGET)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/copy.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/append/copy/copy/frame/process.py $(MCV_APPEND_COPY)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.append.copy.copy.frame.process <"$(MCV_APPEND_COPY)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/append/copy/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/target.frame $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/copy.frame
	@mkdir -p "$(@D)"
	@set +e; cat "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/target.frame" "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/copy.frame" | PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.append.copy.output.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/append/copy/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/append/copy/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.append.copy.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-mutation-fill-preserving-length
morphism-contract-validation-mutation-fill-preserving-length: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/fill/preserving/length/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/fill/preserving/length/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/fill/preserving/length/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/fill/preserving/length/output/process.py $(MCV_FILL_TARGET)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.output.process <"$(MCV_FILL_TARGET)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/fill/preserving/length/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/fill/preserving/length/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.fill.preserving.length.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-mutation-remove-matching
morphism-contract-validation-mutation-remove-matching: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/target.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/remove/matching/target/frame/process.py $(MCV_REMOVE_TARGET)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.remove.matching.target.frame.process <"$(MCV_REMOVE_TARGET)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/matching.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/remove/matching/matching/frame/process.py $(MCV_REMOVE_MATCHING)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.remove.matching.matching.frame.process <"$(MCV_REMOVE_MATCHING)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/remove/matching/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/target.frame $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/matching.frame
	@mkdir -p "$(@D)"
	@set +e; cat "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/target.frame" "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/matching.frame" | PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.remove.matching.output.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/remove/matching/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/remove/matching/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.remove.matching.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-mutation-set
morphism-contract-validation-mutation-set: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/target.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/set/target/frame/process.py $(MCV_SET_TARGET)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.set.target.frame.process <"$(MCV_SET_TARGET)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/replacement.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/set/replacement/frame/process.py $(MCV_SET_REPLACEMENT)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.set.replacement.frame.process <"$(MCV_SET_REPLACEMENT)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/set/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/target.frame $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/replacement.frame
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.set.output.process <"$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/replacement.frame" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mutation/set/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mutation/set/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mutation.set.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
