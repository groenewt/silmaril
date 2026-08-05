from config.constants.morphism.codebase.volume.verification.import_probe.column.coordinate.value import VALUE as COORDINATE_COLUMN
from config.constants.morphism.codebase.volume.verification.import_probe.column.module.value import VALUE as MODULE_COLUMN

BODY_ORIGIN = 1
HEADER_ORIGIN = 0
VIOLATION = "import_probe_registry_column_absent="


def REGISTRATIONS(rows: list) -> list:
    if not rows:
        raise ValueError(VIOLATION + COORDINATE_COLUMN)
    header = rows[HEADER_ORIGIN]
    for column in (COORDINATE_COLUMN, MODULE_COLUMN):
        if column not in header:
            raise ValueError(VIOLATION + column)
    coordinate = header.index(COORDINATE_COLUMN)
    module = header.index(MODULE_COLUMN)
    return sorted({(row[coordinate], row[module]) for row in rows[BODY_ORIGIN:]})
