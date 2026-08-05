from config.constants.morphism.codebase.volume.phase14.gate.count.value import VALUE as GATE_COUNT


VALUE = tuple(f"gate_{gate}" for gate in range(1, GATE_COUNT + 1))
