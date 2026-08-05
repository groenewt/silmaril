from config.constants.morphism.codebase.volume.phase14.error.dimension.unknown.value import VALUE as DIMENSION_UNKNOWN
from config.constants.morphism.codebase.volume.phase14.matrix.detail.marker.value import VALUE as DETAIL_MARKERS
from config.constants.morphism.codebase.volume.phase14.matrix.dimension.name.value import VALUE as DIMENSIONS
from config.constants.morphism.codebase.volume.phase14.matrix.record.detail.field.value import VALUE as DETAIL_FIELD
from config.constants.morphism.codebase.volume.phase14.matrix.status.name.value import VALUE as STATUS_NAMES

PASSED_MARKER, FAILED_MARKER, EMPTY_TRACE_MARKER, SCHEMA_MARKER, QUERY_UNAVAILABLE_MARKER = DETAIL_MARKERS
PASS, PROFILE, TRACE, DRIFT = DIMENSIONS
PENDING, OK, FAIL, MALFORMED, EMPTY_TRACE, DRIFTED, ERROR = STATUS_NAMES
SEPARATOR = "="


def STATUS(dimension: str, record: dict) -> str:
    if record is None:
        return PENDING
    if dimension == PROFILE:
        return OK
    detail = record.get(DETAIL_FIELD)
    if not isinstance(detail, str):
        return MALFORMED
    if dimension == PASS:
        if PASSED_MARKER in detail:
            return OK
        if FAILED_MARKER in detail:
            return FAIL
        return MALFORMED
    if dimension == TRACE:
        if EMPTY_TRACE_MARKER in detail:
            return EMPTY_TRACE
        return OK if detail else MALFORMED
    if dimension == DRIFT:
        if SCHEMA_MARKER in detail:
            return DRIFTED
        if QUERY_UNAVAILABLE_MARKER in detail:
            return ERROR
        return OK if detail else MALFORMED
    raise ValueError(f"{DIMENSION_UNKNOWN}{SEPARATOR}{dimension}")
