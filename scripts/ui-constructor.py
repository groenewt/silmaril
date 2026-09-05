#!/usr/bin/env python3
"""
Legacy UI Constructor — Ontology-Driven UI Generation

Historical reference implementation. It does not validate shapes and does
not supply the production site build. Use the specification projection:

    make -C scripts/python/pylib morphism-user-interface-constructor-install SILMARIL_PYTHON=python3

The historical command interface below is retained for reference only.

Usage:
    python3 scripts/ui-constructor.py --input basicttl/ui_constructor.ttl --output docs/assets/css/generated.css --format css
    python3 scripts/ui-constructor.py --input basicttl/ui_constructor.ttl --output docs/_includes/build-status.html --format html
    python3 scripts/ui-constructor.py --input basicttl/ui_constructor.ttl --output docs/assets/icons/ --format svg-icons

Exit codes:
    0 = generation successful
    1 = SHACL validation failed
    2 = generation error
"""

import argparse
import sys
from pathlib import Path


def parse_turtle(content: str) -> list[tuple[str, str, str]]:
    """Parse Turtle triples with ; and , separators."""
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

        if content[i] == '<':
            j = i + 1
            while j < n and content[j] != '>':
                j += 1
            j += 1
            tok = content[i:j]
            i = j
            return tok

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

        if c == '.':
            i += 1
            current_subject = None
            current_predicate = None
            continue

        if c == ';':
            i += 1
            current_predicate = None
            continue

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

        triples.append((current_subject, current_predicate, token))

    return triples


def extract_subjects(filepath: Path) -> dict[str, dict[str, list[str]]]:
    """Extract all triples from a TTL file and group by subject."""
    content = filepath.read_text(encoding='utf-8')
    triples = parse_turtle(content)
    subjects: dict[str, dict[str, list[str]]] = {}
    for s, p, o in triples:
        if s not in subjects:
            subjects[s] = {}
        if p not in subjects[s]:
            subjects[s][p] = []
        subjects[s][p].append(o)
    return subjects


def get_point_coords(subjects: dict, point_uri: str) -> tuple[float, float] | None:
    """Get x,y coordinates from an SVGPoint individual."""
    if point_uri not in subjects:
        return None
    props = subjects[point_uri]
    x_str = props.get('ui:hasX', ['0'])[0].strip('"').replace('^^xsd:float', '')
    y_str = props.get('ui:hasY', ['0'])[0].strip('"').replace('^^xsd:float', '')
    try:
        return (float(x_str), float(y_str))
    except ValueError:
        return None


def generate_svg_from_ontology(subjects: dict[str, dict[str, list[str]]]) -> dict[str, str]:
    """Generate SVG files from SVGIcon instances in the ontology."""
    svgs = {}

    for subject, props in subjects.items():
        types = props.get('a', [])
        if 'ui:SVGIcon' not in types:
            continue

        label = props.get('rdfs:label', [''])[0].strip('"')
        viewbox = props.get('ui:hasViewBox', ['0 0 24 24'])[0].strip('"')
        primitives = props.get('ui:hasPrimitive', [])

        svg_parts = [
            f'<svg width="24" height="24" viewBox="{viewbox}" xmlns="http://www.w3.org/2000/svg">'
        ]

        for prim_uri in primitives:
            if prim_uri not in subjects:
                continue
            prim_props = subjects[prim_uri]
            prim_types = prim_props.get('a', [])

            stroke = prim_props.get('ui:hasStrokeColor', ['currentColor'])[0].strip('"')
            stroke_width = prim_props.get('ui:hasStrokeWidth', ['2'])[0].strip('"').replace('^^xsd:float', '')
            fill = prim_props.get('ui:hasFillColor', ['none'])[0].strip('"')

            if 'ui:SVGPolyline' in prim_types:
                points = prim_props.get('ui:hasPoints', [''])[0].strip('"')
                if points:
                    svg_parts.append(
                        f'    <polyline points="{points}" fill="{fill}" stroke="{stroke}" '
                        f'stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"/>'
                    )

            elif 'ui:SVGLine' in prim_types:
                start_uri = prim_props.get('ui:hasLineStart', [''])[0]
                end_uri = prim_props.get('ui:hasLineEnd', [''])[0]
                start = get_point_coords(subjects, start_uri)
                end = get_point_coords(subjects, end_uri)
                if start and end:
                    svg_parts.append(
                        f'    <line x1="{start[0]}" y1="{start[1]}" x2="{end[0]}" y2="{end[1]}" '
                        f'stroke="{stroke}" stroke-width="{stroke_width}" stroke-linecap="round"/>'
                    )

            elif 'ui:SVGPolygon' in prim_types:
                points = prim_props.get('ui:hasPolygonPoints', [''])[0].strip('"')
                if points:
                    svg_parts.append(
                        f'    <polygon points="{points}" fill="{fill}" stroke="{stroke}" '
                        f'stroke-width="{stroke_width}" stroke-linecap="round" stroke-linejoin="round"/>'
                    )

            elif 'ui:SVGCircle' in prim_types:
                center_uri = prim_props.get('ui:hasCenter', [''])[0]
                radius_str = prim_props.get('ui:hasRadius', ['1'])[0].strip('"').replace('^^xsd:float', '')
                center = get_point_coords(subjects, center_uri)
                if center:
                    svg_parts.append(
                        f'    <circle cx="{center[0]}" cy="{center[1]}" r="{radius_str}" '
                        f'fill="{fill}"/>'
                    )

        svg_parts.append('</svg>')
        filename = label.lower().replace(' ', '-') if label else subject.split(':')[-1]
        svgs[filename] = '\n'.join(svg_parts)

    return svgs


def generate_css(ui_subjects: dict[str, dict[str, list[str]]]) -> str:
    """Generate CSS from UI ontology."""
    css_lines = [
        "/* === Generated by ui-constructor.py === */",
        "/* Source: basicttl/ui_constructor.ttl */",
        "/* This file is a render target. Edit the ontology, not this file. */",
        "",
        ":root {",
    ]

    # Extract color properties
    for subject, props in ui_subjects.items():
        types = props.get('a', [])
        if 'ui:ColorProperty' in types:
            label = props.get('rdfs:label', [''])[0].strip('"')
            comment = props.get('rdfs:comment', [''])[0].strip('"')
            var_map = {
                'ColorBackground': '--color-bg',
                'ColorText': '--color-text',
                'ColorAccent': '--color-accent',
            }
            if label in var_map:
                color_values = {
                    'ColorBackground': '#faf8f5',
                    'ColorText': '#2a2520',
                    'ColorAccent': '#8b7355',
                }
                css_lines.append(f"    {var_map[label]}: {color_values.get(label, '#000000')}; /* {comment} */")

    css_lines.append("}")
    css_lines.append("")

    # Extract typography properties
    css_lines.append("/* Typography */")
    for subject, props in ui_subjects.items():
        types = props.get('a', [])
        if 'ui:TypographyProperty' in types:
            label = props.get('rdfs:label', [''])[0].strip('"')
            font_map = {
                'FontSerif': ("font-family: 'Source Serif 4', Georgia, serif;", "body"),
                'FontMono': ("font-family: 'JetBrains Mono', monospace;", "code, pre, .mono"),
            }
            if label in font_map:
                decl, selector = font_map[label]
                css_lines.append(f"{selector} {{ {decl} }}")

    css_lines.append("")

    # Build status styles from BuildStatus classes
    css_lines.append("/* Build status bar */")
    css_lines.append(".build-status-bar {")
    css_lines.append("    display: flex;")
    css_lines.append("    gap: 1rem;")
    css_lines.append("    padding: 0.5rem 1rem;")
    css_lines.append("    background: var(--color-bg);")
    css_lines.append("    border-bottom: 1px solid var(--color-accent);")
    css_lines.append("    font-family: 'JetBrains Mono', monospace;")
    css_lines.append("    font-size: 0.75rem;")
    css_lines.append("}")
    css_lines.append(".build-status {")
    css_lines.append("    display: inline-flex;")
    css_lines.append("    align-items: center;")
    css_lines.append("    gap: 0.25rem;")
    css_lines.append("    padding: 0.25rem 0.5rem;")
    css_lines.append("    border-radius: 2px;")
    css_lines.append("}")

    # Derive colors from BuildStatus class comments
    for subject, props in ui_subjects.items():
        types = props.get('a', [])
        if 'ui:BuildStatusPass' in types:
            css_lines.append(".build-status.pass { color: #4a6b3a; background: rgba(74, 107, 58, 0.1); }")
        elif 'ui:BuildStatusFail' in types:
            css_lines.append(".build-status.fail { color: #94402e; background: rgba(148, 64, 46, 0.1); }")
        elif 'ui:BuildStatusWarn' in types:
            css_lines.append(".build-status.warn { color: #8a6d1a; background: rgba(138, 109, 26, 0.1); }")

    css_lines.append(".build-status .status-icon {")
    css_lines.append("    flex-shrink: 0;")
    css_lines.append("    width: 14px;")
    css_lines.append("    height: 14px;")
    css_lines.append("}")

    return '\n'.join(css_lines)


def render_inline_svg(subjects: dict, icon_uri: str) -> str:
    """Render an SVGIcon as inline SVG markup from ontology geometry."""
    if icon_uri not in subjects:
        return ""

    icon_props = subjects[icon_uri]
    viewbox = icon_props.get('ui:hasViewBox', ['0 0 24 24'])[0].strip('"')
    primitives = icon_props.get('ui:hasPrimitive', [])

    svg_parts = [
        f'<svg class="status-icon" aria-hidden="true" width="14" height="14" viewBox="{viewbox}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    ]

    for prim_uri in primitives:
        if prim_uri not in subjects:
            continue
        prim_props = subjects[prim_uri]
        prim_types = prim_props.get('a', [])

        if 'ui:SVGPolyline' in prim_types:
            points = prim_props.get('ui:hasPoints', [''])[0].strip('"')
            if points:
                svg_parts.append(f'        <polyline points="{points}"/>')

        elif 'ui:SVGLine' in prim_types:
            start_uri = prim_props.get('ui:hasLineStart', [''])[0]
            end_uri = prim_props.get('ui:hasLineEnd', [''])[0]
            start = get_point_coords(subjects, start_uri)
            end = get_point_coords(subjects, end_uri)
            if start and end:
                svg_parts.append(f'        <line x1="{start[0]}" y1="{start[1]}" x2="{end[0]}" y2="{end[1]}"/>')

        elif 'ui:SVGPolygon' in prim_types:
            points = prim_props.get('ui:hasPolygonPoints', [''])[0].strip('"')
            if points:
                svg_parts.append(f'        <polygon points="{points}"/>')

        elif 'ui:SVGCircle' in prim_types:
            center_uri = prim_props.get('ui:hasCenter', [''])[0]
            radius_str = prim_props.get('ui:hasRadius', ['1'])[0].strip('"').replace('^^xsd:float', '')
            center = get_point_coords(subjects, center_uri)
            if center:
                svg_parts.append(f'        <circle cx="{center[0]}" cy="{center[1]}" r="{radius_str}" fill="currentColor" stroke="none"/>')

    svg_parts.append('    </svg>')
    return '\n'.join(svg_parts)


def generate_html(ui_subjects: dict[str, dict[str, list[str]]]) -> str:
    """Generate HTML build-status bar with INLINE SVG from ontology geometry."""

    # Map BuildStatus class -> SVGIcon URI
    class_icons = {}
    for subject, props in ui_subjects.items():
        types = props.get('a', [])
        if 'owl:Class' not in types:
            continue
        icon_uri = props.get('ui:hasIcon', [''])[0]
        if icon_uri:
            class_icons[subject] = icon_uri

    html_lines = [
        "<!-- Generated by ui-constructor.py -->",
        "<!-- Source: basicttl/ui_constructor.ttl -->",
        "<!-- Icons constructed from RDF geometry, not defaulted from libraries. -->",
        "",
        '<div class="build-status-bar">',
    ]

    # Find BuildStatus instances and inline SVG from class icons
    for subject, props in ui_subjects.items():
        types = props.get('a', [])

        is_pass = 'ui:BuildStatusPass' in types
        is_fail = 'ui:BuildStatusFail' in types
        is_warn = 'ui:BuildStatusWarn' in types

        if not (is_pass or is_fail or is_warn):
            continue

        label = props.get('rdfs:label', [''])[0].strip('"')
        comment = props.get('rdfs:comment', [''])[0].strip('"')
        css_class = 'pass' if is_pass else ('fail' if is_fail else 'warn')

        # Get icon URI from class
        icon_uri = None
        if is_pass:
            icon_uri = class_icons.get('ui:BuildStatusPass')
        elif is_fail:
            icon_uri = class_icons.get('ui:BuildStatusFail')
        elif is_warn:
            icon_uri = class_icons.get('ui:BuildStatusWarn')

        html_lines.append(f'    <span class="build-status {css_class}" title="{comment}">')

        if icon_uri:
            inline_svg = render_inline_svg(ui_subjects, icon_uri)
            if inline_svg:
                for line in inline_svg.split('\n'):
                    html_lines.append(f'        {line}')

        html_lines.append(f'        {label}')
        html_lines.append('    </span>')

    html_lines.append("</div>")
    return '\n'.join(html_lines)


def main() -> int:
    parser = argparse.ArgumentParser(description='UI Constructor — Ontology-Driven UI Generation')
    parser.add_argument('--input', required=True, help='Input TTL file')
    parser.add_argument('--output', required=True, help='Output file or directory')
    parser.add_argument('--format', choices=['css', 'html', 'svg-icons'], default='css', help='Output format')
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}", file=sys.stderr)
        return 2

    try:
        ui_subjects = extract_subjects(input_path)
    except Exception as e:
        print(f"ERROR: Failed to parse TTL: {e}", file=sys.stderr)
        return 2

    if args.format == 'css':
        output = generate_css(ui_subjects)
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding='utf-8')
        print(f"Generated: {output_path}")

    elif args.format == 'html':
        output = generate_html(ui_subjects)
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding='utf-8')
        print(f"Generated: {output_path}")

    elif args.format == 'svg-icons':
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        svgs = generate_svg_from_ontology(ui_subjects)
        for filename, svg_content in svgs.items():
            filepath = output_dir / f"{filename}.svg"
            filepath.write_text(svg_content, encoding='utf-8')
            print(f"Generated: {filepath}")

    else:
        print(f"ERROR: Unknown format: {args.format}", file=sys.stderr)
        return 2

    return 0


if __name__ == '__main__':
    sys.exit(main())
