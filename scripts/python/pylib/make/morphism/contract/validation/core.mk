.PHONY: morphism-contract-validation-application
morphism-contract-validation-application: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/application/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/application/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/application/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/application/output/process.py $(MCV_APPLICATION_FRAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.application.output.process <"$(MCV_APPLICATION_FRAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/application/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/application/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.application.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-configuration-capture
morphism-contract-validation-configuration-capture: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/configuration/capture/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/configuration/capture/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/configuration/capture/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/configuration/capture/output/process.py $(MCV_CONFIGURATION_CAPTURE_FRAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.configuration.capture.output.process <"$(MCV_CONFIGURATION_CAPTURE_FRAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/configuration/capture/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/configuration/capture/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.configuration.capture.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-contract-bundle-capture
morphism-contract-validation-contract-bundle-capture: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/contract/bundle/capture/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/contract/bundle/capture/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/contract/bundle/capture/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/contract/bundle/capture/output/process.py $(MCV_CONTRACT_BUNDLE_CAPTURE_FRAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.contract.bundle.capture.output.process <"$(MCV_CONTRACT_BUNDLE_CAPTURE_FRAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/contract/bundle/capture/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/contract/bundle/capture/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.contract.bundle.capture.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"


.PHONY: morphism-contract-validation-determinism-reverse
morphism-contract-validation-determinism-reverse: $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/determinism/reverse/output.bin $(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/determinism/reverse/effect.bin

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/determinism/reverse/output.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/determinism/reverse/output/process.py $(MCV_DETERMINISM_REVERSE_TARGET)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.determinism.reverse.output.process <"$(MCV_DETERMINISM_REVERSE_TARGET)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/determinism/reverse/effect.bin: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/determinism/reverse/effect/process.py
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.determinism.reverse.effect.process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
