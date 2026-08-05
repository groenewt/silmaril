VALUE = (
    "awk",
    r'BEGIN { identifier["silm"]="urn:silmaril:entity#"; identifier["cco"]="https://www.commoncoreontologies.org/"; identifier["cceo"]="https://www.commoncoreontologies.org/cpo#"; identifier["owl"]="http://www.w3.org/2002/07/owl#"; identifier["rdf"]="http://www.w3.org/1999/02/22-rdf-syntax-ns#"; identifier["rdfs"]="http://www.w3.org/2000/01/rdf-schema#"; identifier["sh"]="http://www.w3.org/ns/shacl#"; identifier["xsd"]="http://www.w3.org/2001/XMLSchema#" } { print "@prefix " $0 ": <" identifier[$0] "> ." } END { print "" }',
)

