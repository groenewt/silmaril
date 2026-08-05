#!/usr/bin/env bash

fail() {
  printf 'situational-awareness migration failed: %s\n' "$1" >&2
  exit 1
}

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || fail "not inside the repository"
cd "$ROOT" || fail "cannot enter repository root"

[ -d audit ] || fail "audit source directory is missing"
[ -d docs ] || fail "docs source directory is missing"
[ ! -e .codex/audit ] || fail ".codex/audit already exists"
[ ! -e .codex/docs ] || fail ".codex/docs already exists"
[ -w .codex ] || fail ".codex is not writable in this session"

mkdir -p .codex || fail "cannot create .codex"
mv audit .codex/audit || fail "cannot move audit"
if ! mv docs .codex/docs; then
  mv .codex/audit audit >/dev/null 2>&1
  fail "cannot move docs; audit rollback attempted"
fi

AUDIT_REFERENCES=(
  .gitignore
  RELEASE_MANIFEST.json
  SHA256SUMS.txt
  build.sbt
  contracts/git-contract.yaml
  contracts/morphisms/README.md
  modules/config/src/main/scala/highway/config/constants/Cli/Values/Assess/Baseline/Fixture/Value.scala
  modules/config/src/main/scala/highway/config/constants/Cli/Values/Assess/Baseline/Self/Value.scala
  modules/config/src/main/scala/highway/config/constants/Cli/Values/Cpg/Exempt/Manifest/Value.scala
  modules/config/src/main/scala/highway/config/constants/Cli/Values/Path/Manifest/Value.scala
  modules/config/src/main/scala/highway/config/constants/ci/Assess.scala
  modules/state/src/main/scala/highway/state/V/22/State.scala
  modules/viewer/src/main/resources/web/ARCHITECTURE.md
  modules/viewer/src/main/resources/web/v12-unified.js
  modules/viewer/src/main/resources/web/v12-universal-state.js
  scripts/ci.sh
  scripts/validate-parity-architecture.py
  .codex/audit/corpus/README.md
  .codex/audit/corpus/corpus_inventory.py
)

for path in "${AUDIT_REFERENCES[@]}"; do
  [ -f "$path" ] || fail "registered audit reference is missing: $path"
  perl -0pi -e 's{(?<!\.codex/)audit/}{.codex/audit/}g' "$path" \
    || fail "cannot rewrite audit reference: $path"
done

DOCS_EXEMPTION=modules/config/src/main/scala/highway/config/constants/Cli/Values/Cpg/Exempt/Docs/Value.scala
[ -f "$DOCS_EXEMPTION" ] || fail "documentation exemption constant is missing"
perl -0pi -e 's{"docs/"}{".codex/docs/"}g' "$DOCS_EXEMPTION" \
  || fail "cannot rewrite documentation exemption"

CI_VALIDATION=scripts/validate-cicd.sh
[ -f "$CI_VALIDATION" ] || fail "CI validation script is missing"
perl -0pi -e 's{mkdir -p docs}{mkdir -p .codex/docs}g; s{docs/ci-heartbeat\.md}{.codex/docs/ci-heartbeat.md}g' "$CI_VALIDATION" \
  || fail "cannot rewrite CI heartbeat path"

if rg -n --hidden --glob '!.git/**' --glob '!.codex/audit/**' --glob '!.codex/docs/**' \
    '(^|[^A-Za-z0-9_.-])audit/' .; then
  fail "operational audit references remain outside the relocated trees"
fi

printf '%s\n' \
  'situational-awareness migration complete' \
  '  audit -> .codex/audit' \
  '  docs  -> .codex/docs'
