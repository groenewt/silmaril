from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-c",
    """
-- Reify the projected relation in its canonical row order.
CREATE OR REPLACE TABLE ordered_relation AS
FROM projected_relation AS p
ORDER BY
  p.rel_path ASC,
  p.doc_id ASC;
""",
)
