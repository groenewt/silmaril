from config.constants.morphism.codebase.volume.executable.duckdb.value import VALUE as DUCKDB

VALUE = (
    DUCKDB,
    "-readonly",
    "-csv",
    "-noheader",
    "-c",
    "FROM ordered_row_relation;",
)

