from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG


VALUE = (
    RG,
    "--sort",
    "path",
    "--line-number",
    "--hidden",
    "--glob",
    "!.git/**",
    "--glob",
    "test/**",
    "--glob",
    "tests/**",
    "--glob",
    "*_test.*",
    "--glob",
    "test_*",
    "^[[:space:]]*(test[[:space:]]+\"|def[[:space:]]+test_|it[[:space:]]*\\(|describe[[:space:]]*\\()",
    ".",
)
