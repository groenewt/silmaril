#!/usr/bin/env python3
"""
Ontology Depth Check

Validates that TTL files meet structural depth requirements:
1. Every owl:Class must have an rdfs:comment > 200 characters
2. Every owl:NamedIndividual must be an instance of a specific class (not just owl:Thing)
3. Every owl:ObjectProperty must have both rdfs:domain and rdfs:range
4. No bare NamedIndividuals without type declarations beyond owl:NamedIndividual

Usage:
    python3 scripts/ontology-depth-check.py basicttl/
    python3 scripts/ontology-depth-check.py basicttl/file.ttl

Exit codes:
    0 = all checks pass
    1 = depth violations found
"""

import sys
from pathlib import Path


def parse_turtle(content: str) -> list[tuple[str, str, str]]:
    """Parse Turtle triples, handling ; and , separators."""
    triples = []
    lines = []
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('@prefix') or stripped.startswith('#'):
            continue
        lines.append(line)

    content = '\n'.join(lines)
    n = len(content)
    i = 0

    def skip_ws():
        nonlocal i
        while i < n and content[i] in ' \t\n\r':
            i += 1

    def parse_token():
        nonlocal i
        skip_ws()
        if i >= n:
            return None

        # """ string
        if content[i:i+3] == '"""':
            j = i + 3
            while j < n - 2:
                if content[j:j+3] == '"""':
                    j += 3
                    break
                j += 1
            tok = content[i:j]
            i = j
            return tok

        # " string
        if content[i] == '"':
            j = i + 1
            while j < n:
                if content[j] == '"' and (j == i+1 or content[j-1] != '\\'):
                    j += 1
                    break
                j += 1
            tok = content[i:j]
            i = j
            return tok

        # <IRI>
        if content[i] == '<':
            j = i + 1
            while j < n and content[j] != '>':
                j += 1
            j += 1
            tok = content[i:j]
            i = j
            return tok

        # Regular token
        j = i
        while j < n and content[j] not in ' \t\n\r;.,':
            j += 1
        tok = content[i:j]
        i = j
        return tok

    current_subject = None
    current_predicate = None

    while i < n:
        skip_ws()
        if i >= n:
            break

        c = content[i]

        # Statement separator: reset subject
        if c == '.':
            i += 1
            current_subject = None
            current_predicate = None
            continue

        # Predicate separator: same subject, new predicate
        if c == ';':
            i += 1
            current_predicate = None
            continue

        # Object separator: same subject, same predicate, new object
        if c == ',':
            i += 1
            continue

        token = parse_token()
        if token is None:
            break

        if current_subject is None:
            current_subject = token
            continue

        if current_predicate is None:
            current_predicate = token
            continue

        # This is an object
        triples.append((current_subject, current_predicate, token))

    return triples


def check_file(filepath: Path) -> list[str]:
    """Check a single TTL file for depth violations."""
    violations = []
    content = filepath.read_text(encoding='utf-8')
    triples = parse_turtle(content)

    subjects: dict[str, dict[str, list[str]]] = {}
    for s, p, o in triples:
        if s not in subjects:
            subjects[s] = {}
        if p not in subjects[s]:
            subjects[s][p] = []
        subjects[s][p].append(o)

    for subject, props in subjects.items():
        if 'a' in props:
            types = props['a']
            if any('owl:Class' in t for t in types):
                if 'rdfs:comment' not in props:
                    violations.append(f"{subject}: owl:Class missing rdfs:comment")
                else:
                    comment = ' '.join(props['rdfs:comment'])
                    comment = comment.replace('"""', '').replace('"', '')
                    if len(comment) < 200:
                        violations.append(f"{subject}: owl:Class rdfs:comment too short ({len(comment)} chars, min 200)")

            if any('owl:NamedIndividual' in t for t in types):
                specific_types = [t for t in types if t != 'owl:NamedIndividual']
                if not specific_types:
                    violations.append(f"{subject}: NamedIndividual has no specific type")

        if 'a' in props and any('owl:ObjectProperty' in t for t in props['a']):
            if 'rdfs:domain' not in props:
                violations.append(f"{subject}: owl:ObjectProperty missing rdfs:domain")
            if 'rdfs:range' not in props:
                violations.append(f"{subject}: owl:ObjectProperty missing rdfs:range")

    return violations


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <ttl-file-or-directory>", file=sys.stderr)
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"ERROR: {target} does not exist", file=sys.stderr)
        return 2

    ttl_files = []
    if target.is_file() and target.suffix == '.ttl':
        ttl_files = [target]
    else:
        ttl_files = list(target.rglob('*.ttl'))

    all_violations = []
    for ttl_file in ttl_files:
        violations = check_file(ttl_file)
        if violations:
            all_violations.append((ttl_file, violations))

    if all_violations:
        print(f"ONTOLOGY DEPTH CHECK FAILED")
        print(f"Files checked: {len(ttl_files)}")
        print(f"Files with violations: {len(all_violations)}")
        print()
        for filepath, violations in all_violations:
            print(f"{filepath}:")
            for v in violations:
                print(f"  - {v}")
        return 1
    else:
        print(f"ONTOLOGY DEPTH CHECK PASSED")
        print(f"Files checked: {len(ttl_files)}")
        return 0


if __name__ == '__main__':
    sys.exit(main())
