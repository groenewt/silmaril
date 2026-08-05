from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE inverse_projected_cell_relation AS
SELECT term_name, column_index, cell_value, multiple_value
FROM aggregated_cell_relation
UNION ALL
SELECT
  direct.cell_value AS term_name,
  CASE direct.column_index
    WHEN 11 THEN 13
    WHEN 9 THEN 12
    WHEN 19 THEN 20
    WHEN 16 THEN 18
  END AS column_index,
  direct.term_name AS cell_value,
  true AS multiple_value
FROM expanded_cell_relation AS direct
WHERE direct.column_index IN (9, 11, 16, 19)
  AND direct.cell_value <> direct.term_name;
""",
)

