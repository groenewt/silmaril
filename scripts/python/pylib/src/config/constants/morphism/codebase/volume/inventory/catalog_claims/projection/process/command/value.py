from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-c",
    """
-- Project the catalog contract columns with explicit provenance.
CREATE OR REPLACE TABLE projected_relation AS
SELECT
  c.claim_id AS claim_id,
  c.doc_id AS doc_id,
  c.claim_text AS claim_text,
  c.source_locator AS source_locator,
  c.trust_state AS trust_state,
  c.claim_type AS claim_type,
  c.evidence_hint AS evidence_hint
FROM source_relation AS c;
""",
)
