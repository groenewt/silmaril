from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB
from config.constants.morphism.codebase.volume.inventory.catalog.null_value.value import VALUE as NULL_VALUE


VALUE = (
    DUCKDB,
    "-readonly",
    "-csv",
    "-header",
    "-nullvalue",
    NULL_VALUE,
    "-c",
    """
-- Encode the ordered native relation as canonical CSV.
FROM ordered_relation;
""",
)
