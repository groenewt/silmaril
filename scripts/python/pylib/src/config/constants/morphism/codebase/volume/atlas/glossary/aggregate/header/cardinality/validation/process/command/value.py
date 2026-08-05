from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-c",
    """
CREATE OR REPLACE TABLE header_cardinality_validation AS
SELECT CASE
  WHEN count(*) = 21 THEN true
  ELSE error('atlas glossary header cardinality must equal 21')
END AS accepted
FROM pragma_table_info('header_source_relation');
""",
)

