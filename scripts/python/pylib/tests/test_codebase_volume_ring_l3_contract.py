from config.constants.morphism.codebase.volume.ring.family.l3.token.value import VALUE as L3


def test_ring_l3_contract() -> None:
    assert L3 == ("l3", "duckdb", "parquet")
