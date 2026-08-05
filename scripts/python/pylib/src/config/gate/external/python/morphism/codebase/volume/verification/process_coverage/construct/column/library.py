from config.constants.morphism.codebase.volume.verification.process_coverage.column.coordinate.value import VALUE as COORDINATE_COLUMN

BODY_ORIGIN = 1
HEADER_ORIGIN = 0
VIOLATION = "process_coverage_coordinate_column_absent="


def COORDINATES(rows: list) -> list:
    if not rows:
        raise ValueError(VIOLATION + COORDINATE_COLUMN)
    header = rows[HEADER_ORIGIN]
    if COORDINATE_COLUMN not in header:
        raise ValueError(VIOLATION + COORDINATE_COLUMN)
    origin = header.index(COORDINATE_COLUMN)
    return sorted({row[origin] for row in rows[BODY_ORIGIN:]})
