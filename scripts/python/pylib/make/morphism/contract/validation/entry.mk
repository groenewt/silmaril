.PHONY: morphism-contract-validation-entry-self-test
morphism-contract-validation-entry-self-test: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/expected.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/self/test/expected/frame/process.py $(MCV_ENTRY_SELF_EXPECTED)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.self.test.expected.frame.process <"$(MCV_ENTRY_SELF_EXPECTED)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/observed.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/self/test/observed/frame/process.py $(MCV_ENTRY_SELF_OBSERVED)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.self.test.observed.frame.process <"$(MCV_ENTRY_SELF_OBSERVED)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/self/test/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/expected.frame $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/observed.frame
	@mkdir -p "$(@D)"
	@set +e; cat "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/expected.frame" "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/observed.frame" | PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.self.test.output.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/self/test/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/self/test/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.self.test.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-entry-twin-readback
morphism-contract-validation-entry-twin-readback: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/source.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/twin/readback/source/frame/process.py $(MCV_ENTRY_TWIN_SOURCE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.twin.readback.source.frame.process <"$(MCV_ENTRY_TWIN_SOURCE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/twin.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/twin/readback/twin/frame/process.py $(MCV_ENTRY_TWIN_TWIN)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.twin.readback.twin.frame.process <"$(MCV_ENTRY_TWIN_TWIN)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/twin/readback/output/process.py $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/source.frame $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/twin.frame
	@mkdir -p "$(@D)"
	@set +e; cat "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/source.frame" "$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/twin.frame" | PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.twin.readback.output.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/entry/twin/readback/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/entry/twin/readback/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.entry.twin.readback.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
