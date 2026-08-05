#!/usr/bin/env python3
"""
Silmaril Ontology Consolidator

Merges the distributed TTL encyclopedia (30K+ files) into a single,
queryable ontology with SHACL shapes and SPARQL/GeoSPARQL query sets.

Usage:
    python3 scripts/consolidate-ontology.py [--output-dir ontology/]
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


def extract_prefixes(content: str) -> dict[str, str]:
    """Extract @prefix declarations from TTL content."""
    prefixes = {}
    for match in re.finditer(r'@prefix\s+(\w+):\s+<([^>]+)>\s+\.', content):
        prefixes[match.group(1)] = match.group(2)
    return prefixes


def strip_prefixes(content: str) -> str:
    """Remove @prefix declarations, return just triples."""
    lines = []
    for line in content.split('\n'):
        stripped = line.strip()
        if not stripped.startswith('@prefix') and not stripped.startswith('#'):
            lines.append(line)
    return '\n'.join(lines)


def consolidate_ttl(basicttl_dir: Path) -> tuple[str, dict[str, str], int]:
    """
    Walk all .ttl files and merge into a single ontology document.
    Returns (merged_content, unified_prefixes, file_count).
    """
    all_prefixes: dict[str, str] = {
        'silm': 'urn:silmaril:entity#',
        'cco': 'https://www.commoncoreontologies.org/',
        'cceo': 'https://www.commoncoreontologies.org/cpo#',
        'owl': 'http://www.w3.org/2002/07/owl#',
        'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
        'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
        'xsd': 'http://www.w3.org/2001/XMLSchema#',
        'sh': 'http://www.w3.org/ns/shacl#',
        'geo': 'http://www.opengis.net/ont/geosparql#',
        'sf': 'http://www.opengis.net/ont/sf#',
    }
    triple_blocks = []
    file_count = 0

    for ttl_file in sorted(basicttl_dir.rglob('*.ttl')):
        content = ttl_file.read_text(encoding='utf-8')
        if not content.strip():
            continue
        file_count += 1

        # Extract and merge prefixes
        file_prefixes = extract_prefixes(content)
        for prefix, uri in file_prefixes.items():
            if prefix not in all_prefixes:
                all_prefixes[prefix] = uri

        # Strip prefix declarations and keep triples
        triples = strip_prefixes(content)
        if triples.strip():
            triple_blocks.append(f"\n# Source: {ttl_file.relative_to(basicttl_dir)}\n{triples}")

    # Build header with unified prefixes
    header_lines = [
        "# Silmaril Consolidated Ontology",
        f"# Generated from {file_count} TTL files",
        "# This file is machine-generated; edit the source files in basicttl/",
        "",
    ]
    for prefix, uri in sorted(all_prefixes.items(), key=lambda x: x[0]):
        header_lines.append(f'@prefix {prefix}: <{uri}> .')
    header_lines.append("")

    merged = '\n'.join(header_lines) + '\n'.join(triple_blocks)
    return merged, all_prefixes, file_count


def generate_shacl_shapes() -> str:
    """Generate SHACL shapes for Silmaril ontology validation."""
    return '''
# Silmaril SHACL Shapes

silm:ConcreteAnchorShape a sh:NodeShape ;
    sh:targetClass silm:concreteanchor ;
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
        sh:severity sh:Violation ;
    ] ;
    sh:property [
        sh:path rdfs:comment ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
        sh:severity sh:Warning ;
    ] .

silm:CheeseTrapImmunityShape a sh:NodeShape ;
    sh:targetClass silm:cheesetrapimmunity ;
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
    ] ;
    sh:property [
        sh:path rdfs:comment ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
    ] .

silm:NamedIndividualShape a sh:NodeShape ;
    sh:targetClass owl:NamedIndividual ;
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
    ] ;
    sh:property [
        sh:path silm:hasAdditionalAttribute ;
        sh:minCount 0 ;
        sh:datatype xsd:string ;
    ] .

silm:PaperReferenceShape a sh:NodeShape ;
    sh:targetSubjectsOf silm:hasLongDescription ;
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:maxCount 5 ;
        sh:datatype xsd:string ;
    ] .

silm:DecompositionStepShape a sh:NodeShape ;
    sh:targetClass silm:decompositionstep ;
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:datatype xsd:string ;
    ] .
'''


def generate_sparql_queries() -> str:
    """Generate useful SPARQL queries for the Silmaril ontology."""
    return '''
# Silmaril SPARQL Query Library

# Q1: List all papers with their concrete anchors
# PREFIX silm: <urn:silmaril:entity#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?paper ?anchor ?label WHERE {
    ?paper a owl:NamedIndividual .
    ?paper rdfs:label ?label .
    FILTER (strstarts(str(?paper), str(silm:instances_papers_)))
} ORDER BY ?paper

# Q2: Find all cheese-trap immunity mechanisms
# PREFIX silm: <urn:silmaril:entity#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?immunity ?label ?comment WHERE {
    ?immunity a silm:cheesetrapimmunity .
    OPTIONAL { ?immunity rdfs:label ?label }
    OPTIONAL { ?immunity rdfs:comment ?comment }
}

# Q3: Count entities per paper
# PREFIX silm: <urn:silmaril:entity#>
SELECT ?paper (COUNT(?entity) AS ?count) WHERE {
    ?entity a owl:NamedIndividual .
    FILTER (strstarts(str(?entity), str(silm:instances_papers_)))
    BIND (strbefore(strafter(str(?entity), str(silm:instances_papers_)), ".chapters") AS ?paper)
} GROUP BY ?paper ORDER BY DESC(?count)

# Q4: Find all decomposition steps without examples
# PREFIX silm: <urn:silmaril:entity#>
SELECT ?step ?label WHERE {
    ?step a silm:decompositionstep .
    ?step rdfs:label ?label .
    FILTER NOT EXISTS { ?step silm:hasExample ?ex }
}

# Q5: Full-text search across long descriptions
# PREFIX silm: <urn:silmaril:entity#>
SELECT ?entity ?desc WHERE {
    ?entity silm:hasLongDescription ?desc .
    FILTER (contains(lcase(str(?desc)), "mittens"))
}
'''


def generate_geosparql_queries() -> str:
    """Generate GeoSPARQL queries (if geospatial data is present)."""
    return '''
# Silmaril GeoSPARQL Query Library
# NOTE: The current Silmaril substrate does not contain explicit geospatial
# data, but these queries are ready for when location-aware concrete anchors
# are added (e.g., Tartu Animal Clinic coordinates).

# GQ1: Find all entities within a bounding box (when geo data is added)
# PREFIX geo: <http://www.opengis.net/ont/geosparql#>
# PREFIX sf: <http://www.opengis.net/ont/sf#>
SELECT ?entity ?wkt WHERE {
    ?entity geo:hasGeometry ?geom .
    ?geom geo:asWKT ?wkt .
    FILTER (geof:sfWithin(?wkt,
        "POLYGON((24.7 58.3, 24.8 58.3, 24.8 58.4, 24.7 58.4, 24.7 58.3))"^^geo:wktLiteral))
}

# GQ2: Find entities near a point (buffer search)
# PREFIX geo: <http://www.opengis.net/ont/geosparql#>
SELECT ?entity ?wkt WHERE {
    ?entity geo:hasGeometry ?geom .
    ?geom geo:asWKT ?wkt .
    FILTER (geof:sfWithin(?wkt,
        geof:buffer("POINT(24.745 58.378)"^^geo:wktLiteral, 0.01)))
}
'''


def main() -> int:
    parser = argparse.ArgumentParser(description='Consolidate Silmaril TTL files')
    parser.add_argument('--output-dir', default='ontology', help='Output directory')
    parser.add_argument('--basicttl', default='basicttl', help='Source TTL directory')
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    basicttl_dir = Path(args.basicttl)
    if not basicttl_dir.exists():
        print(f"ERROR: {basicttl_dir} not found", file=sys.stderr)
        return 1

    print(f"Consolidating TTL files from {basicttl_dir}...")
    merged, prefixes, count = consolidate_ttl(basicttl_dir)

    consolidated_path = out_dir / 'silmaril-consolidated.ttl'
    consolidated_path.write_text(merged, encoding='utf-8')
    print(f"  Wrote {consolidated_path} ({count} files merged)")

    shapes_path = out_dir / 'shapes.ttl'
    # Prepend prefixes to shapes
    prefix_block = '\n'.join(f'@prefix {p}: <{u}> .' for p, u in sorted(prefixes.items(), key=lambda x: x[0]))
    shapes_path.write_text(prefix_block + '\n' + generate_shacl_shapes(), encoding='utf-8')
    print(f"  Wrote {shapes_path}")

    sparql_path = out_dir / 'queries.sparql'
    sparql_path.write_text(generate_sparql_queries(), encoding='utf-8')
    print(f"  Wrote {sparql_path}")

    geosparql_path = out_dir / 'geosparql.sparql'
    geosparql_path.write_text(generate_geosparql_queries(), encoding='utf-8')
    print(f"  Wrote {geosparql_path}")

    # Write a manifest
    manifest = f"""# Silmaril Ontology Manifest
# Generated by consolidate-ontology.py

@prefix silm: <urn:silmaril:entity#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

silm:OntologyManifest a owl:Ontology ;
    rdfs:label "Silmaril Consolidated Ontology" ;
    rdfs:comment "Consolidated from {{count}} source TTL files" ;
    owl:versionInfo "1.0.0" .

silm:ConsolidatedGraph a void:Dataset ;
    rdfs:label "Silmaril Knowledge Graph" ;
    void:triples "{{triples_estimate}}" ;
    void:entities "{{entities_estimate}}" .
"""
    manifest_path = out_dir / 'manifest.ttl'
    manifest_path.write_text(manifest, encoding='utf-8')
    print(f"  Wrote {manifest_path}")

    print(f"\nConsolidation complete. Output in {out_dir}/")
    return 0


if __name__ == '__main__':
    sys.exit(main())
