#!/usr/bin/env bash
# coverage.sh TREE_ROOT MANIFEST
# Exit 0 iff MANIFEST covers exactly the file set of TREE_ROOT (excluding .git
# plumbing) AND every manifest line's sha256 (col1) and byte count (col2) match
# the file on disk. A corrupted hash or size now FAILS instead of printing
# COVERAGE EXACT (closes the P.3 "path-coverage, not content-integrity" gap).
# Manifest format: sha256<TAB>bytes<TAB>path (paths relative to repo root).
#
# The two manifested roots are symlink-FREE (verified 2026-08-07):
#     find forge/base_templates -type l | wc -l  ->  0
#     find forge/base           -type l | wc -l  ->  0
# so '-type f' loses no in-scope entry HERE and is kept deliberately. The
# symlink-bearing trees are bound to disk by tree-disk-check.sh, not this file.
set -euo pipefail
root=$1; manifest=$2

# (1) PATH-SET coverage: on-disk regular-file set == manifest path column (col3).
diff <(find "$root" -type f -not -path "*/.git/*" | sort) \
     <(cut -f3 "$manifest" | sort)

# (2) CONTENT integrity — sha256 (col1): re-hash every file and compare in bulk.
#     --quiet prints only failures; --strict rejects any malformed manifest line.
if ! hashout=$(awk -F'\t' '{printf "%s  %s\n", $1, $3}' "$manifest" \
               | sha256sum -c --quiet --strict 2>&1); then
  echo "SHA256 MISMATCH ($manifest):"; echo "$hashout"; exit 1
fi

# (3) CONTENT integrity — bytes (col2): re-measure every file and compare the
#     recorded byte count. This catches a mutated size column independently of
#     the hash column. Every path is known to exist (guaranteed by step 1).
bytefail=$(while IFS=$'\t' read -r h b p; do
             disk=$(stat -c %s -- "$p")
             [ "$disk" = "$b" ] || printf '%s recorded=%s disk=%s\n' "$p" "$b" "$disk"
           done < "$manifest")
test -z "$bytefail" || { echo "BYTES MISMATCH ($manifest):"; echo "$bytefail"; exit 1; }

echo "COVERAGE EXACT: $root == $manifest ($(wc -l < "$manifest" | tr -d ' ') files; sha256+bytes verified)"
