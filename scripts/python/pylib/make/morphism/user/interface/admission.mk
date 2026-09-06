# Formal runtime admission is distinct from observing the generated site.
# This target remains unsuccessful until the physical carrier, launcher and
# readback correction exists. A successful site build does not invoke it or
# claim its result. Keep the unresolved requirements independently inspectable.
# The required evidence is recorded in basicttl/user/interface/runtime/requirements.ttl.
.PHONY: morphism-user-interface-runtime-admission
morphism-user-interface-runtime-admission:
	$(error User interface execution is not admitted. The renderer lacks integrated byte-carrier ADTs, typed dependency effects and a lawful launcher. See basicttl/user/interface/runtime/requirements.ttl)
