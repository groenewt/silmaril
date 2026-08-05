from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-c",
    """
-- Project the catalog contract columns with explicit provenance.
CREATE OR REPLACE TABLE projected_relation AS
SELECT
  g.gap_id AS gap_id,
  g.doc_id AS doc_id,
  g.category AS category,
  g.severity AS severity,
  g.gap_text AS gap_text,
  g.source_locator AS source_locator,
  g.matched_terms AS matched_terms
FROM source_relation AS g;
""",
)
