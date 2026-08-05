from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-c",
    """
-- Parse the canonical exported CSV into a native relation carrier.
CREATE OR REPLACE TABLE source_relation AS
FROM read_csv_auto('library_cache/tables/claims.csv');
""",
)
