VALUE = (
    "awk",
    "-F",
    "\t",
    r'BEGIN { OFS="\t" } { priority=($3 ~ /^a owl:NamedIndividual/ ? 0 : 1); print $1, $2, priority, $3 }',
)

