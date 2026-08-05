from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE expanded_cell_relation AS
SELECT
  source.term_name,
  cast(right(source.column_name, 2) AS INTEGER) AS column_index,
  CASE WHEN source.multiple_value THEN trim(piece.value) ELSE piece.value END AS cell_value,
  source.multiple_value,
  source.filename,
  source.occurrence_order
FROM (
  SELECT
    unpivoted.*,
    column_name IN (
      'column_04', 'column_07', 'column_08', 'column_09', 'column_10',
      'column_11', 'column_12', 'column_13', 'column_14', 'column_17',
      'column_18', 'column_19', 'column_20'
    ) AS multiple_value
  FROM (
    UNPIVOT normalized_row_relation
    ON column_00, column_01, column_02, column_03, column_04, column_05,
       column_06, column_07, column_08, column_09, column_10, column_11,
       column_12, column_13, column_14, column_15, column_16, column_17,
       column_18, column_19, column_20
    INTO NAME column_name VALUE raw_value
  ) AS unpivoted
) AS source
CROSS JOIN LATERAL unnest(
  CASE
    WHEN source.multiple_value THEN string_split(source.raw_value, ';')
    ELSE [source.raw_value]
  END
) AS piece(value)
WHERE CASE WHEN source.multiple_value THEN trim(piece.value) ELSE piece.value END <> '';
""",
)

