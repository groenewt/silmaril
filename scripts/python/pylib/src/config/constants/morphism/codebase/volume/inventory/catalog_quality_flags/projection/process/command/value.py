from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-c",
    """
-- Project the catalog contract columns with explicit provenance.
CREATE OR REPLACE TABLE projected_relation AS
SELECT
  q.flag_id AS flag_id,
  q.doc_id AS doc_id,
  q.flag AS flag,
  q.severity AS severity,
  q.reason AS reason
FROM source_relation AS q;
""",
)
