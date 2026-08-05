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
    "*.c",
    "--glob",
    "*.cc",
    "--glob",
    "*.cpp",
    "--glob",
    "*.cxx",
    "--glob",
    "*.h",
    "--glob",
    "*.hpp",
    "--glob",
    "*.rs",
    "^",
    ".",
)
