MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCE_ROOT := $(CURDIR)/src
MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT := $(CURDIR)/build/morphism/user/interface/constructor
MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT := $(abspath $(CURDIR)/../../..)
MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/basicttl/ui_constructor.ttl
MORPHISM_USER_INTERFACE_CONSTRUCTOR_CASCADING_STYLE_SHEET_COMMITTED := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/docs/assets/css/generated.css
MORPHISM_USER_INTERFACE_CONSTRUCTOR_HYPERTEXT_MARKUP_LANGUAGE_COMMITTED := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/docs/_includes/build-status.html

define MORPHISM_USER_INTERFACE_CONSTRUCTOR_STEP
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; SILMARIL_ONTOLOGY_PATH="$(2)" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.user.interface.constructor.$(1).process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
endef

.PHONY: morphism-user-interface-constructor morphism-user-interface-constructor-check morphism-user-interface-constructor-force
morphism-user-interface-constructor-force:

morphism-user-interface-constructor: $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/generated.css $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/build-status.html

$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/generated.css: $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY) morphism-user-interface-constructor-force
	$(call MORPHISM_USER_INTERFACE_CONSTRUCTOR_STEP,cascading.style.sheet.render,"$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY)")

$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/build-status.html: $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY) morphism-user-interface-constructor-force
	$(call MORPHISM_USER_INTERFACE_CONSTRUCTOR_STEP,hypertext.markup.language.render,"$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY)")

morphism-user-interface-constructor-check: morphism-user-interface-constructor
	@STATUS=0; for f in generated.css build-status.html; do cmp "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/$$f" "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/docs/$$(echo $$f | sed 's/^generated/css\/generated/; s/^build-status/_includes\/build-status/')" || { printf 'user interface constructor drift: docs/%s does not match regeneration from basicttl/ui_constructor.ttl\n' "$$f" >&2; STATUS=1; }; done; exit $$STATUS
	@printf '%s\n' 'user interface constructor artifacts in sync with ontology'
