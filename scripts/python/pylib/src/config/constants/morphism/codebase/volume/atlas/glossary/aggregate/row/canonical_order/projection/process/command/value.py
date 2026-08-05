from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE ordered_row_relation AS
SELECT * EXCLUDE (term_name)
FROM reconstructed_row_relation
ORDER BY term_name;
""",
)

