from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE normalized_row_relation AS
SELECT
  occurrence_order,
  filename,
  coalesce(column_01, '') AS term_name,
  coalesce(column_00, '') AS column_00,
  coalesce(column_01, '') AS column_01,
  coalesce(column_02, '') AS column_02,
  coalesce(column_03, '') AS column_03,
  coalesce(column_04, '') AS column_04,
  coalesce(column_05, '') AS column_05,
  coalesce(column_06, '') AS column_06,
  coalesce(column_07, '') AS column_07,
  coalesce(column_08, '') AS column_08,
  coalesce(column_09, '') AS column_09,
  coalesce(column_10, '') AS column_10,
  coalesce(column_11, '') AS column_11,
  coalesce(column_12, '') AS column_12,
  coalesce(column_13, '') AS column_13,
  coalesce(column_14, '') AS column_14,
  coalesce(column_15, '') AS column_15,
  coalesce(column_16, '') AS column_16,
  coalesce(column_17, '') AS column_17,
  coalesce(column_18, '') AS column_18,
  coalesce(column_19, '') AS column_19,
  coalesce(column_20, '') AS column_20
FROM row_source_relation
WHERE coalesce(column_01, '') <> ''
  AND concat_ws('',
    trim(coalesce(column_00, '')), trim(coalesce(column_01, '')),
    trim(coalesce(column_02, '')), trim(coalesce(column_03, '')),
    trim(coalesce(column_04, '')), trim(coalesce(column_05, '')),
    trim(coalesce(column_06, '')), trim(coalesce(column_07, '')),
    trim(coalesce(column_08, '')), trim(coalesce(column_09, '')),
    trim(coalesce(column_10, '')), trim(coalesce(column_11, '')),
    trim(coalesce(column_12, '')), trim(coalesce(column_13, '')),
    trim(coalesce(column_14, '')), trim(coalesce(column_15, '')),
    trim(coalesce(column_16, '')), trim(coalesce(column_17, '')),
    trim(coalesce(column_18, '')), trim(coalesce(column_19, '')),
    trim(coalesce(column_20, ''))
  ) <> '';
""",
)

