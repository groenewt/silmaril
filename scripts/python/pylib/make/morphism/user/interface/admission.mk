# This is a denial, not an implementation of the unary admission arrow.
# Remove it only with the physical carrier, launcher and readback correction.
# The required evidence is recorded in basicttl/user/interface/runtime/requirements.ttl.
.PHONY: morphism-user-interface-runtime-admission
morphism-user-interface-runtime-admission:
	$(error User interface execution is not admitted. The renderer lacks integrated byte-carrier ADTs, typed dependency effects and a lawful launcher. See basicttl/user/interface/runtime/requirements.ttl)
