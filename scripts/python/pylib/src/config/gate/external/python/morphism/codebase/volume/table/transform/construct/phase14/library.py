from config.constants.morphism.codebase.volume.phase14.dimension.count.value import VALUE as DIMENSION_COUNT
from config.constants.morphism.codebase.volume.phase14.matrix.dimension.name.value import VALUE as DIMENSIONS
from config.constants.morphism.codebase.volume.phase14.matrix.event.name.value import VALUE as EVENT_NAMES
from config.constants.morphism.codebase.volume.phase14.matrix.gate.identity.value import VALUE as GATE_IDENTITIES
from config.constants.morphism.codebase.volume.table.phase14.header.value import VALUE as HEADER
from config.gate.external.python.morphism.codebase.volume.table.phase14.matrix.evidence.library import EVIDENCE
from config.gate.external.python.morphism.codebase.volume.table.phase14.matrix.index.library import INDEX
from config.gate.external.python.morphism.codebase.volume.table.phase14.matrix.status.library import STATUS

ORDER_ORIGIN = 1


def RENDER(records: tuple) -> list:
    index = INDEX(records)
    rows = [list(HEADER)]
    for position, event in enumerate(EVENT_NAMES):
        gate_position, dimension_position = divmod(position, DIMENSION_COUNT)
        dimension = DIMENSIONS[dimension_position]
        record = index.get(event)
        rows.append(
            [
                gate_position + ORDER_ORIGIN,
                GATE_IDENTITIES[gate_position],
                dimension_position + ORDER_ORIGIN,
                dimension,
                STATUS(dimension, record),
                EVIDENCE(record),
            ]
        )
    return rows
