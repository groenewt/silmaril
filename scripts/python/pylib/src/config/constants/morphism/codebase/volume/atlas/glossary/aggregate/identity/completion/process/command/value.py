from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE identity_completed_cell_relation AS
SELECT term_name, column_index, cell_value, multiple_value
FROM inverse_aggregated_cell_relation
UNION ALL
SELECT target.term_name, identity.column_index, target.term_name, identity.multiple_value
FROM (
  SELECT DISTINCT term_name
  FROM inverse_aggregated_cell_relation
  EXCEPT
  SELECT DISTINCT column_01
  FROM normalized_row_relation
) AS target
CROSS JOIN (VALUES (0, false), (1, false)) AS identity(column_index, multiple_value);
""",
)

