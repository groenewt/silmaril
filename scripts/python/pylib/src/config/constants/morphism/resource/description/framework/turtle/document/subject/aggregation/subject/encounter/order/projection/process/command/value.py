VALUE = (
    "awk",
    "-F",
    "\t",
    r'BEGIN { OFS="\t"; count=0 } { subject=$1; if (!(subject in ordinal)) { ordinal[subject]=count; count++ } print ordinal[subject], $0 }',
)

