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
    "*.md",
    "--glob",
    "*.tex",
    "--glob",
    "*.rst",
    "--glob",
    "*.adoc",
    "^(#{1,6}[[:space:]]+|[.][.][[:space:]]+_[^:]+:|\\\\(part|chapter|section|subsection|subsubsection)[{])",
    ".",
)
