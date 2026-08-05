# Stage exactly the declared 34 artifacts, then publish them with one atomic
# directory rename.  Per-file copies and the final rename are independent
# external-process coordinates.

VOLUME_40_INSTALL_STAGE_FILES := $(addprefix $(VOLUME_40_INSTALL_STAGE_ROOT)/,$(VOLUME_40_INSTALL_RELATIVE))

.PHONY: volume-40-install-stage volume-40-install
volume-40-install-stage: volume-40-bindings volume-40-strict-source-body volume-40-generate $(VOLUME_40_INSTALL_STAGE_FILES)
	@printf 'Volume 40 install stage materialized: %s\n' "$(VOLUME_40_INSTALL_STAGE_ROOT)"

$(VOLUME_40_INSTALL_STAGE_ROOT) \
$(VOLUME_40_INSTALL_STAGE_ROOT)/tables \
$(VOLUME_40_INSTALL_RECEIPT_ROOT):
	mkdir -p "$@"

define VOLUME_40_INSTALL_RULE
$(VOLUME_40_INSTALL_STAGE_ROOT)/$(1): $(VOLUME_40_PRODUCTION_ROOT)/$(1) | $(VOLUME_40_INSTALL_STAGE_ROOT) $(VOLUME_40_INSTALL_STAGE_ROOT)/tables $(VOLUME_40_INSTALL_RECEIPT_ROOT)
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.install.process "$$<" "$$@" >"$(VOLUME_40_INSTALL_RECEIPT_ROOT)/$(subst /,__,$(1)).stdout" 2>"$(VOLUME_40_INSTALL_RECEIPT_ROOT)/$(subst /,__,$(1)).stderr"; status=$$$$?; set -e; \
	if test "$$$$status" -ne 0; then cat "$(VOLUME_40_INSTALL_RECEIPT_ROOT)/$(subst /,__,$(1)).stderr" >&2; exit "$$$$status"; fi; \
	printf '%s\n' "$$$$status" >"$(VOLUME_40_INSTALL_RECEIPT_ROOT)/$(subst /,__,$(1)).status"
endef

$(foreach path,$(VOLUME_40_INSTALL_RELATIVE),$(eval $(call VOLUME_40_INSTALL_RULE,$(path))))

$(VOLUME_40_FINAL_GENERATED_ROOT): $(VOLUME_40_INSTALL_STAGE_FILES) | volume-40-bindings $(VOLUME_40_INSTALL_RECEIPT_ROOT)
	@test ! -e "$@" && test ! -L "$@" || { printf 'atomic install destination already exists: %s\n' "$@" >&2; exit 73; }
	@set +e; PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(SILMARIL_PYLIB_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.codebase.volume.artifact.atomic_delivery.process "$(VOLUME_40_INSTALL_STAGE_ROOT)" "$@" >"$(VOLUME_40_INSTALL_RECEIPT_ROOT)/atomic-delivery.stdout" 2>"$(VOLUME_40_INSTALL_RECEIPT_ROOT)/atomic-delivery.stderr"; status=$$?; set -e; \
	if test "$$status" -ne 0; then cat "$(VOLUME_40_INSTALL_RECEIPT_ROOT)/atomic-delivery.stderr" >&2; exit "$$status"; fi; \
	printf '%s\n' "$$status" >"$(VOLUME_40_INSTALL_RECEIPT_ROOT)/atomic-delivery.status"

ifeq ($(wildcard $(VOLUME_40_FINAL_GENERATED_ROOT)),)
volume-40-install: $(VOLUME_40_FINAL_GENERATED_ROOT)
	@printf 'Volume 40 atomically installed: %s\n' "$(VOLUME_40_FINAL_GENERATED_ROOT)"
else
volume-40-install: volume-40-readback
	@printf 'Volume 40 install already present and byte-verified: %s\n' "$(VOLUME_40_FINAL_GENERATED_ROOT)"
endif
