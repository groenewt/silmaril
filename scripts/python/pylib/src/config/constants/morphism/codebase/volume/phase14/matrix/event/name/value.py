from config.constants.morphism.codebase.volume.phase14.gate.count.value import VALUE as GATE_COUNT
from config.constants.morphism.codebase.volume.phase14.matrix.event.suffix.value import VALUE as EVENT_SUFFIXES


VALUE = tuple(
    f"gate_{gate}_{suffix}"
    for gate in range(1, GATE_COUNT + 1)
    for suffix in EVENT_SUFFIXES
)
