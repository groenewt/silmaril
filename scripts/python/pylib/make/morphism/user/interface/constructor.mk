include make/morphism/user/interface/admission.mk

MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCE_ROOT := $(CURDIR)/src
MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT := $(CURDIR)/build/morphism/user/interface/constructor
MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT := $(abspath $(CURDIR)/../../..)
MORPHISM_USER_INTERFACE_CONSTRUCTOR_SPECIFICATION_ROOT := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/basicttl/user/interface
# The same validation graph covers the status bar, portal elements, and reading templates.
MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCES := $(addprefix $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SPECIFICATION_ROOT)/,schema.ttl components.ttl styles.ttl queries.ttl shapes.ttl portal.ttl documentation.ttl)
MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/specification.ttl
MORPHISM_USER_INTERFACE_CONSTRUCTOR_CASCADING_STYLE_SHEET := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/docs/assets/css/generated.css
MORPHISM_USER_INTERFACE_CONSTRUCTOR_HYPERTEXT_MARKUP_LANGUAGE := $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/docs/_includes/build-status.html

define MORPHISM_USER_INTERFACE_CONSTRUCTOR_STEP
	@test -n "$(SILMARIL_PYTHON)" || { printf '%s\n' 'SILMARIL_PYTHON is required' >&2; exit 64; }
	@mkdir -p "$(@D)"
	@set +e; SILMARIL_ONTOLOGY_PATH="$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY)" PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.user.interface.constructor.$(1).process >"$@.pending" 2>"$@.stderr"; STATUS=$$?; printf '%s\n' "$$STATUS" >"$@.status"; set -e; if [ "$$STATUS" -ne 0 ]; then cat "$@.stderr" >&2; exit "$$STATUS"; fi; mv "$@.pending" "$@"
endef

.PHONY: morphism-user-interface-constructor morphism-user-interface-constructor-check morphism-user-interface-constructor-install morphism-user-interface-constructor-force
morphism-user-interface-constructor-force:

$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY): $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCES) morphism-user-interface-constructor-force
	@mkdir -p "$(@D)"
	@cat $(foreach SOURCE,$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCES),"$(SOURCE)") >"$@.pending"
	@mv "$@.pending" "$@"

morphism-user-interface-constructor: $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/generated.css $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/build-status.html

$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/generated.css: $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY)
	$(call MORPHISM_USER_INTERFACE_CONSTRUCTOR_STEP,cascading.style.sheet.render)

$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/build-status.html: $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ONTOLOGY)
	$(call MORPHISM_USER_INTERFACE_CONSTRUCTOR_STEP,hypertext.markup.language.render)

morphism-user-interface-constructor-check: morphism-user-interface-constructor
	@PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m pytest -q tests/test_user_interface_constructor.py ../../../scripts/site/test_projection.py

morphism-user-interface-constructor-install: morphism-user-interface-constructor
	@mkdir -p "$(dir $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_CASCADING_STYLE_SHEET))" "$(dir $(MORPHISM_USER_INTERFACE_CONSTRUCTOR_HYPERTEXT_MARKUP_LANGUAGE))"
	@cp "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/generated.css" "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_CASCADING_STYLE_SHEET).pending"
	@cp "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_ARTIFACT_ROOT)/build-status.html" "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_HYPERTEXT_MARKUP_LANGUAGE).pending"
	@mv "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_CASCADING_STYLE_SHEET).pending" "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_CASCADING_STYLE_SHEET)"
	@mv "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_HYPERTEXT_MARKUP_LANGUAGE).pending" "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_HYPERTEXT_MARKUP_LANGUAGE)"

.PHONY: morphism-user-interface-documentation
morphism-user-interface-documentation:
	@SILMARIL_REPOSITORY_ROOT="$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)" PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_SOURCE_ROOT)" "$(SILMARIL_PYTHON)" -m silmaril.sparky.morphism.user.interface.documentation.render.engine

morphism-user-interface-constructor-install: morphism-user-interface-documentation

.PHONY: morphism-user-interface-portal
morphism-user-interface-portal:
	@PYTHONDONTWRITEBYTECODE=1 "$(SILMARIL_PYTHON)" "$(MORPHISM_USER_INTERFACE_CONSTRUCTOR_REPOSITORY_ROOT)/scripts/site/project.py"

morphism-user-interface-constructor-install: morphism-user-interface-portal
