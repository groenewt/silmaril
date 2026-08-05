from config.constants.morphism.codebase.volume.executable.rg.value import VALUE as RG


VALUE = (
    RG,
    "--sort",
    "path",
    "--files",
    "--hidden",
    "--glob",
    "!.git/**",
    "--glob",
    "*.sh",
    "--glob",
    "bin/**",
    "--glob",
    "scripts/**",
    ".",
)
