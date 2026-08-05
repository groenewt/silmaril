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
    "config/**",
    "--glob",
    "*.exs",
    "--glob",
    ".codex/**",
    "--glob",
    "scripts/env/**",
    "^",
    ".",
)
