from config.constants.morphism.codebase.volume.ring.family.trust_protection.token.value import VALUE as TRUST_PROTECTION


def test_ring_trust_protection_contract() -> None:
    assert TRUST_PROTECTION == ("trust ring", "protection ring", "default-deny", "trustgate")
