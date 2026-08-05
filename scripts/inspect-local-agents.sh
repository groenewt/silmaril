#!/usr/bin/env bash
# Enumerate local fork/reference targets under the platform agents tree.
set -uo pipefail
AGENTS="$HOME/Desktop/platform/core/agents"
echo "== native crates/libs =="
ls -1 "$AGENTS/native" 2>/dev/null
echo "== ducklake catalogs =="
ls -1 "$AGENTS"/*.ducklake "$AGENTS"/*.duckdb 2>/dev/null
echo "== kvrocks / ducklake / arrow interface patterns =="
ls -1 "$AGENTS"/scripts/set0_kvrocks_*.exs "$AGENTS"/scripts/verify-ducklake.sh "$AGENTS"/vendor/ex_arrow 2>/dev/null
echo "== provenance =="
git -C "$HOME/Desktop/platform" rev-parse HEAD 2>/dev/null
