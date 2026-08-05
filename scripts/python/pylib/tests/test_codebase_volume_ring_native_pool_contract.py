from config.constants.morphism.codebase.volume.ring.family.native_pool.token.value import VALUE as NATIVE_POOL


def test_ring_native_pool_contract() -> None:
    assert NATIVE_POOL == ("ring_pool", "ring pool", "capacity 64")
