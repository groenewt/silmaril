VALUE = (
    "awk",
    "-F",
    "\t",
    r'BEGIN { current="" } { if (current=="") { print "silm:" $2; current=$2 } else if ($2!=current) { print "    " pending " ."; print ""; print "silm:" $2; current=$2 } else { print "    " pending " ;" } pending=$4 } END { if (current!="") { print "    " pending " ."; print "" } }',
)

