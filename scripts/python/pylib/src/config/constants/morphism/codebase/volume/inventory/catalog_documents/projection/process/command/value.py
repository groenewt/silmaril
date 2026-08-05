from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-c",
    """
-- Project the catalog contract columns with explicit provenance.
CREATE OR REPLACE TABLE projected_relation AS
SELECT
  d.doc_id AS doc_id,
  d.abs_path AS abs_path,
  d.rel_path AS rel_path,
  d.filename AS filename,
  d.dir1 AS dir1,
  d.dir2 AS dir2,
  d.extension AS extension,
  d.size_bytes AS size_bytes,
  d.mtime_ns AS mtime_ns,
  d.sha256 AS sha256,
  d.hash_status AS hash_status,
  d.source_label AS source_label,
  d.canonical_status AS canonical_status,
  d.ingest_status AS ingest_status,
  d.text_cache_path AS text_cache_path,
  d.title AS title,
  d.detected_title AS detected_title,
  d.pdf_pages AS pdf_pages,
  d.word_count AS word_count,
  d.line_count AS line_count,
  d.file_kind AS file_kind,
  d.parse_status AS parse_status,
  d.parse_error AS parse_error
FROM source_relation AS d;
""",
)
