VALUE = (
    "awk",
    r'{ if ($0 !~ /^(silm|cco|cceo|owl|rdf|rdfs|sh|xsd)$/) { print "namespace-identifier-absent:" $0 > "/dev/stderr"; exit 2 } print }',
)

