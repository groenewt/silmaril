from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE inverse_aggregated_cell_relation AS
SELECT
  term_name,
  column_index,
  CASE
    WHEN bool_or(multiple_value)
      THEN string_agg(DISTINCT cell_value, ';' ORDER BY cell_value)
    ELSE first(cell_value)
  END AS cell_value,
  bool_or(multiple_value) AS multiple_value
FROM inverse_projected_cell_relation
GROUP BY term_name, column_index;
""",
)

