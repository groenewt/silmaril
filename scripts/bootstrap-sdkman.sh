#!/usr/bin/env bash
# Verify the pinned toolchain (.sdkmanrc) plus storage-tier CLIs. No Joern.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ -s "${SDKMAN_DIR:-$HOME/.sdkman}/bin/sdkman-init.sh" ]; then
  # shellcheck disable=SC1091
  source "${SDKMAN_DIR:-$HOME/.sdkman}/bin/sdkman-init.sh"
  sdk env install
fi
for tool in java scala sbt; do
  command -v "$tool" >/dev/null || { echo "missing: $tool" >&2; exit 1; }
done
command -v duckdb >/dev/null || echo "warn: duckdb CLI missing (L1A/L1B/L2B/L3 tiers degrade)" >&2
command -v redis-cli >/dev/null || echo "warn: redis-cli missing (L2A kvrocks tier degrades)" >&2
java -version 2>&1 | head -1
scala --version 2>&1 | tail -1
echo "bootstrap ok"
