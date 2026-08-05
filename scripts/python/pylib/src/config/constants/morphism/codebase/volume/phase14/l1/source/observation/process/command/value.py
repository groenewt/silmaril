from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB


VALUE = (
    DUCKDB,
    "-json",
    "-c",
    """
SELECT
  source.event AS event,
  source.detail AS detail,
  source.correlation_id AS correlation_id,
  source.run_id AS run_id,
  source.sequence AS sequence,
  source.time_iso AS time_iso
FROM read_avro([
  getenv('VOLUME_PHASE14_L1_OK_GLOB'),
  getenv('VOLUME_PHASE14_L1_ERROR_GLOB')
]) AS source;
""",
)
