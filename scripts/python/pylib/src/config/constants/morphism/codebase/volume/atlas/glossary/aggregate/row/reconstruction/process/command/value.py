from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE reconstructed_row_relation AS
SELECT
  term_name,
  coalesce(max(cell_value) FILTER (column_index = 0), '') AS column_00,
  coalesce(max(cell_value) FILTER (column_index = 1), '') AS column_01,
  coalesce(max(cell_value) FILTER (column_index = 2), '') AS column_02,
  coalesce(max(cell_value) FILTER (column_index = 3), '') AS column_03,
  coalesce(max(cell_value) FILTER (column_index = 4), '') AS column_04,
  coalesce(max(cell_value) FILTER (column_index = 5), '') AS column_05,
  coalesce(max(cell_value) FILTER (column_index = 6), '') AS column_06,
  coalesce(max(cell_value) FILTER (column_index = 7), '') AS column_07,
  coalesce(max(cell_value) FILTER (column_index = 8), '') AS column_08,
  coalesce(max(cell_value) FILTER (column_index = 9), '') AS column_09,
  coalesce(max(cell_value) FILTER (column_index = 10), '') AS column_10,
  coalesce(max(cell_value) FILTER (column_index = 11), '') AS column_11,
  coalesce(max(cell_value) FILTER (column_index = 12), '') AS column_12,
  coalesce(max(cell_value) FILTER (column_index = 13), '') AS column_13,
  coalesce(max(cell_value) FILTER (column_index = 14), '') AS column_14,
  coalesce(max(cell_value) FILTER (column_index = 15), '') AS column_15,
  coalesce(max(cell_value) FILTER (column_index = 16), '') AS column_16,
  coalesce(max(cell_value) FILTER (column_index = 17), '') AS column_17,
  coalesce(max(cell_value) FILTER (column_index = 18), '') AS column_18,
  coalesce(max(cell_value) FILTER (column_index = 19), '') AS column_19,
  coalesce(max(cell_value) FILTER (column_index = 20), '') AS column_20
FROM identity_completed_cell_relation
GROUP BY term_name;
""",
)

