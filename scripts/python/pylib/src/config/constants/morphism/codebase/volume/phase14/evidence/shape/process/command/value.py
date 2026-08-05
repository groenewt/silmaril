from config.constants.morphism.codebase.volume.executable.jq.value import VALUE as JQ
from config.constants.morphism.codebase.volume.phase14.gate.count.value import VALUE as GATE_COUNT


VALUE = (
    JQ,
    "--exit-status",
    "(.records | map(.event) | unique | length) == " + str(GATE_COUNT),
)
