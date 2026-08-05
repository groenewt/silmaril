$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/closed-enumeration.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/closed/enumeration/frame/process.py $(MCV_ARTIFACT_CLOSED_ENUMERATION)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.closed.enumeration.frame.process <"$(MCV_ARTIFACT_CLOSED_ENUMERATION)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/registration-kind.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/registration/kind/frame/process.py $(MCV_ARTIFACT_REGISTRATION_KIND)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.registration.kind.frame.process <"$(MCV_ARTIFACT_REGISTRATION_KIND)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/registration-identity.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/registration/identity/frame/process.py $(MCV_ARTIFACT_REGISTRATION_IDENTITY)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.registration.identity.frame.process <"$(MCV_ARTIFACT_REGISTRATION_IDENTITY)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/registration-path.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/registration/path/frame/process.py $(MCV_ARTIFACT_REGISTRATION_PATH)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.registration.path.frame.process <"$(MCV_ARTIFACT_REGISTRATION_PATH)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/registration-schema.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/registration/schema/frame/process.py $(MCV_ARTIFACT_REGISTRATION_SCHEMA)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.registration.schema.frame.process <"$(MCV_ARTIFACT_REGISTRATION_SCHEMA)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/registration-status.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/registration/status/frame/process.py $(MCV_ARTIFACT_REGISTRATION_STATUS)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.registration.status.frame.process <"$(MCV_ARTIFACT_REGISTRATION_STATUS)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/registration-source-evidence.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/registration/source/evidence/frame/process.py $(MCV_ARTIFACT_REGISTRATION_SOURCE_EVIDENCE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.registration.source.evidence.frame.process <"$(MCV_ARTIFACT_REGISTRATION_SOURCE_EVIDENCE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/document-schema.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/document/schema/frame/process.py $(MCV_ARTIFACT_DOCUMENT_SCHEMA)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.document.schema.frame.process <"$(MCV_ARTIFACT_DOCUMENT_SCHEMA)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/artifact/kind/schema-document-schema.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/artifact/kind/schema/document/schema/frame/process.py $(MCV_ARTIFACT_SCHEMA_DOCUMENT_SCHEMA)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.artifact.kind.schema.document.schema.frame.process <"$(MCV_ARTIFACT_SCHEMA_DOCUMENT_SCHEMA)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/digest/support/coordinate.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/digest/support/coordinate/frame/process.py $(MCV_DIGEST_SUPPORT_COORDINATE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.digest.support.coordinate.frame.process <"$(MCV_DIGEST_SUPPORT_COORDINATE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/digest/support/value.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/digest/support/value/frame/process.py $(MCV_DIGEST_SUPPORT_VALUE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.digest.support.value.frame.process <"$(MCV_DIGEST_SUPPORT_VALUE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/format/name.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/format/name/frame/process.py $(MCV_FORMAT_NAME)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.format.name.frame.process <"$(MCV_FORMAT_NAME)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"

$(MORPHISM_CONTRACT_VALIDATION_ARTIFACT_ROOT)/mechanic/format/value.frame: $(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)/silmaril/sparky/morphism/contract/validation/mechanic/format/value/frame/process.py $(MCV_FORMAT_VALUE)
	@mkdir -p "$(@D)"
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_CONTRACT_VALIDATION_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.contract.validation.mechanic.format.value.frame.process <"$(MCV_FORMAT_VALUE)" >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
