from config.constants.morphism.codebase.volume.ring.family.l1.token.value import VALUE as L1


def test_ring_l1_contract() -> None:
    assert L1 == ("l1", "avro", "commit receipt", "frame head")
