include make/morphism/contract/validation/file.mk
include make/morphism/contract/validation/core.mk
include make/morphism/contract/validation/entry.mk
include make/morphism/contract/validation/mechanic_frame.mk
include make/morphism/contract/validation/mechanic.mk
include make/morphism/contract/validation/mutation.mk
include make/morphism/contract/validation/schema.mk

.PHONY: morphism-contract-validation
morphism-contract-validation: morphism-contract-validation-application morphism-contract-validation-configuration-capture morphism-contract-validation-contract-bundle-capture morphism-contract-validation-determinism-reverse morphism-contract-validation-entry-self-test morphism-contract-validation-entry-twin-readback morphism-contract-validation-mechanic-artifact-kind morphism-contract-validation-mechanic-digest-support morphism-contract-validation-mechanic-format morphism-contract-validation-mechanic-json morphism-contract-validation-mutation-append-copy morphism-contract-validation-mutation-fill-preserving-length morphism-contract-validation-mutation-remove-matching morphism-contract-validation-mutation-set morphism-contract-validation-schema-canonicalize morphism-contract-validation-schema-diagnostic morphism-contract-validation-schema-digest morphism-contract-validation-schema-equality morphism-contract-validation-schema-format-date-time morphism-contract-validation-schema-format-uri morphism-contract-validation-schema-format-uri-reference
