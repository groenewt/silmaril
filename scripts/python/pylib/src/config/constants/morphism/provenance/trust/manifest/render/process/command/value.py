VALUE = (
    "python3",
    "-c",
    r'''import json
import sys

rows = [json.loads(line) for line in sys.stdin.buffer.read().decode("utf-8").splitlines() if line]
header = [
    "# Silmaril signing-key trust manifest.",
    "# GENERATED from basicttl/commit_signing_trust.ttl by scripts/generate-trust-manifest.py — regenerate, do not hand-edit.",
    "#",
    "# Columns: FINGERPRINT(40 hex, no spaces)  POLICY  KEYFILE(relative to this dir)  COMMENT...",
    "# POLICY classes: release (maintainer/openclaw agent) | web-flow (GitHub web UI) | agent (session agents).",
    '# A listed fingerprint whose KEYFILE is absent is "attested": commits by it are',
    "# acknowledged but cryptographically unverifiable until the key file lands.",
]
fingerprint_width = max(len(row[0]) for row in rows)
policy_width = max(len(row[1]) for row in rows)
key_file_width = max(len(row[2]) for row in rows)
lines = header + [
    row[0].ljust(fingerprint_width) + "  "
    + row[1].ljust(policy_width) + "  "
    + row[2].ljust(key_file_width) + "  "
    + row[3] + " <" + row[4] + ">"
    for row in rows
]
sys.stdout.buffer.write("\n".join(lines).encode("utf-8") + b"\n")
''',
)
