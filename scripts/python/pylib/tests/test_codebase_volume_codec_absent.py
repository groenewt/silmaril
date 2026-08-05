from pathlib import Path


GATE_ROOT = (
    Path(__file__).parents[1]
    / "src/config/gate/external/python/morphism/codebase/volume"
)


def test_codec_aggregator_is_absent() -> None:
    assert not (GATE_ROOT / "codec/library.py").exists()
    assert not (GATE_ROOT / "source/observation/path/library.py").exists()
