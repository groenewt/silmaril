# Git Bridge Hooks

Registered external bridges between git's hook protocol and the typed
provenance pipeline (`scripts/python/pylib`). Under the unary byte-frame law
(`docs/unary-byte-frame-law.md`) a git hook cannot be a lawful internal
callable — the protocol supplies multiple arguments and stdin streams — so
each bridge declares the findings it carries in its header, stays thin, and
delegates all policy to the typed tree.

## Bridges

| Bridge | Protocol | Delegates to | Blocks on |
|--------|----------|--------------|-----------|
| `pre-commit` | index observation | staged-blob gates | syntax errors in staged `*.sh`; staged armored secret key material; signing misconfiguration when `silmaril.requiresign` is true |
| `pre-push` | ref stream on stdin | `make morphism-provenance-commit-policy-default` per outgoing range | BADSIG or UNKNOWN classification |
| `remote-update` | server-side (refname, old, new) | policy extracted from the TRUSTED old revision | BADSIG or UNKNOWN in the pushed range; tampered force-pushes are rejected with the ref unmoved |

## Install / uninstall

```bash
bash scripts/install-git-hook.sh              # sets core.hooksPath = hooks
bash scripts/install-git-hook.sh --uninstall  # unsets core.hooksPath
```

`core.hooksPath` shadows everything in `.git/hooks/` while installed. The
`remote-update` bridge is installed into a bare remote as `hooks/update` by
`scripts/init-fake-remote.sh`.

```bash
git config silmaril.requiresign true   # pre-commit signing warnings become failures
```

Do not put policy in a bridge; policy lives in the typed tree and the trust
ontology (`basicttl/commit_signing_trust.ttl`).
