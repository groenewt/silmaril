from config.constants.morphism.codebase.volume.atlas.glossary.aggregate.environment.header_source_path.value import VALUE as HEADER_SOURCE_PATH
from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    f"""
CREATE OR REPLACE TABLE header_source_relation AS
SELECT *
FROM read_csv(
  getenv('{HEADER_SOURCE_PATH}'),
  header = true,
  all_varchar = true,
  sample_size = -1
)
LIMIT 0;
""",
)

