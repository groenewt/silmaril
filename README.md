# Silmaril

Computational economics laboratory — GraphAtlas / Silmaril.

## Repository Structure

```
.
├── docs/           # GitHub Pages site (Jekyll)
│   ├── index.html
│   ├── _config.yml
│   ├── _layouts/
│   ├── assets/
│   └── README.md
├── basicttl/       # RDF/TTL ontology files — Silmaril encyclopedia substrate
│   └── _verb/      # Categorical verb definitions and translations
├── ontology/       # Consolidated ontology + shapes + query libraries (generated)
├── keys/           # Committed signing public keys + generated trust manifest
├── hooks/          # Registered git bridge hooks (install: scripts/install-git-hook.sh)
├── scripts/        # Build, validation, and deployment scripts
│   ├── python/     # Python tooling and test suites
│   ├── scala/      # Scala CLI and Spark integrations
│   └── source/     # Source discipline scripts
└── README.md       # This file
```

## GitHub Pages

Site served from `docs/` on the `master` branch.

**URL:** https://groenewt.github.io/silmaril/

## Commit Signing & Verification

Trusted signing keys are declared in the ontology
(`basicttl/commit_signing_trust.ttl`), committed under `keys/`, and enforced by
the typed provenance pipeline in `scripts/python/pylib` (unary byte-frame law:
`docs/unary-byte-frame-law.md`):

| Fingerprint | Identity | Policy |
|-------------|----------|--------|
| `77481DD960B9CBE52BEC60CFC998590FAEA8530A` | Herodotus <herodotus@silmaril.internal> (openclaw agent) | `release` |
| `968479A1AFF927E37D1A566BB5690EEEBB952194` | GitHub <noreply@github.com> (web-flow) | `web-flow` |
| `27044DC503CD3A5EE470CE4E15B79D364040C858` | Claude <claude@silmaril.internal> (session agent) | `agent` |

```bash
export SILMARIL_PYTHON=$(command -v python3)
make -C scripts/python/pylib morphism-provenance-commit-policy-default   # verify history
make -C scripts/python/pylib morphism-provenance-trust-manifest-check    # manifest <- trust model
bash scripts/install-git-hook.sh                                         # bridge hooks
```

The default policy hard-fails tampered signatures and keys outside the trust
manifest; `morphism-provenance-commit-policy-strict` accepts GOOD only. CI runs
the policy, the trust-manifest drift gate, the ontology consolidation sync gate,
and the semantic validation gates on pushes to `master`/`main` and pull
requests. See `keys/README.md` for custody and rotation.

## License

See individual subdirectories for licensing.
