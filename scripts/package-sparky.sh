#!/usr/bin/env bash
# Package the sparky CLI as an installable, sbt-free binary distribution:
#
#   dist/sparky/lib/*.jar       module jars + Scala runtime jars
#   dist/sparky/bin/sparky      launcher (plain `java -cp`)
#
#   scripts/package-sparky.sh [--symlink [DIR]]
#
# --symlink installs a PATH symlink (default ~/.local/bin/sparky), mirroring
# the host's single-dir-symlink install convention.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v sbt >/dev/null 2>&1; then
  # shellcheck disable=SC1091
  [ -s "$HOME/.sdkman/bin/sdkman-init.sh" ] && . "$HOME/.sdkman/bin/sdkman-init.sh" >/dev/null 2>&1 || true
fi

DIST=dist/sparky
rm -rf "$DIST"
mkdir -p "$DIST/lib" "$DIST/bin"

echo "packaging module jars + resolving runtime classpath..."
CP_FILE=$(mktemp)
sbt -batch --no-colors package "export cli/Runtime/fullClasspath" \
  | grep -E '^[^\[].*(classes|\.jar)' | tail -1 > "$CP_FILE"

# classpath entries: external jars copy verbatim; module classes dirs map to
# the jar `sbt package` just built next to them
tr ':' '\n' < "$CP_FILE" | while read -r entry; do
  [ -n "$entry" ] || continue
  if [[ "$entry" == *.jar ]]; then
    cp "$entry" "$DIST/lib/"
  elif [[ "$entry" == */classes ]]; then
    jar=$(find "$(dirname "$entry")" -maxdepth 1 -name '*.jar' | head -1)
    [ -n "$jar" ] && cp "$jar" "$DIST/lib/"
  fi
done
rm -f "$CP_FILE"

cat > "$DIST/bin/sparky" <<'LAUNCHER'
#!/usr/bin/env bash
# sparky — installable CLI launcher (no sbt; plain JVM over packaged jars).
set -euo pipefail
HERE=$(cd "$(dirname "$(readlink -f "$0")")" && pwd)
exec java -Xmx6g -Xss64m -cp "$HERE/../lib/*" graphatlas.sparky.cli.Main "$@"
LAUNCHER
chmod +x "$DIST/bin/sparky"

echo "packaged: $DIST/lib ($(ls "$DIST/lib" | wc -l) jars)"
echo "launcher: $DIST/bin/sparky"

if [ "${1:-}" = "--symlink" ]; then
  TARGET_DIR="${2:-$HOME/.local/bin}"
  mkdir -p "$TARGET_DIR"
  ln -sf "$(pwd)/$DIST/bin/sparky" "$TARGET_DIR/sparky"
  echo "symlinked: $TARGET_DIR/sparky"
fi
