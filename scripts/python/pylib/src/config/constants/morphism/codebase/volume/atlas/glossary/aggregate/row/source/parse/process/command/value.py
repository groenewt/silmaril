from config.constants.morphism.codebase.volume.atlas.glossary.aggregate.environment.row_source_glob.value import VALUE as ROW_SOURCE_GLOB
from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    f"""
CREATE OR REPLACE TABLE row_source_relation AS
SELECT row_number() OVER () AS occurrence_order, *
FROM read_csv(
  getenv('{ROW_SOURCE_GLOB}'),
  header = false,
  auto_detect = false,
  delim = ',',
  quote = '"',
  escape = '"',
  columns = {{
    'column_00':'VARCHAR','column_01':'VARCHAR','column_02':'VARCHAR',
    'column_03':'VARCHAR','column_04':'VARCHAR','column_05':'VARCHAR',
    'column_06':'VARCHAR','column_07':'VARCHAR','column_08':'VARCHAR',
    'column_09':'VARCHAR','column_10':'VARCHAR','column_11':'VARCHAR',
    'column_12':'VARCHAR','column_13':'VARCHAR','column_14':'VARCHAR',
    'column_15':'VARCHAR','column_16':'VARCHAR','column_17':'VARCHAR',
    'column_18':'VARCHAR','column_19':'VARCHAR','column_20':'VARCHAR'
  }},
  filename = true,
  null_padding = true
);
""",
)

