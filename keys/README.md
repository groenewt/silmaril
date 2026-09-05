# Signing Keys & Trust Manifest

Committed public keys and the trust manifest driving
the typed provenance pipeline. The authoritative trust model lives in the
ontology — `basicttl/commit_signing_trust.ttl` — and this directory's manifest
is generated from it.

## Files

| File | Description |
|------|-------------|
| `herodotus.asc` | Herodotus (openclaw agent) — `77481DD960B9CBE52BEC60CFC998590FAEA8530A`, ed25519, policy `release` |
| `github-web-flow.asc` | GitHub web-flow service key — `968479A1AFF927E37D1A566BB5690EEEBB952194`, rsa4096, policy `web-flow` |
| `claude.asc` | Claude session agent — `27044DC503CD3A5EE470CE4E15B79D364040C858`, ed25519, policy `agent` |
| `aster.asc` | Aster session identity — `1649618A5612CC75132F9336F52E907F309C73B3`, ed25519, proposed policy `agent`; requires maintainer endorsement |
| `trust-manifest.txt` | Generated manifest (fingerprint, policy, keyfile, identity) consumed by the verifier |

## Verifying

```bash
export SILMARIL_PYTHON=$(command -v python3)
make -C scripts/python/pylib morphism-provenance-commit-policy-default  # default policy
make -C scripts/python/pylib morphism-provenance-commit-policy-report   # classify only
make -C scripts/python/pylib morphism-provenance-commit-policy-strict   # GOOD-only gate
```

The verifier imports these keys into an ephemeral keyring — your personal
GnuPG keyring is never read or written.

## Adding or rotating a key

1. Edit `basicttl/commit_signing_trust.ttl`: add the `silm:signingkey`
   individual (fingerprint, algorithm, keyfile, policy class) and link it from
   a `silm:signingidentity` via `silm:signsWith`. Keep superseded keys listed —
   historical commits must keep verifying.
2. Export the armored public key into this directory:

   ```bash
   gpg --armor --export <FINGERPRINT> > keys/<name>.asc
   ```

3. Regenerate the derived artifacts:

   ```bash
   export SILMARIL_PYTHON=$(command -v python3)
   make -C scripts/python/pylib morphism-provenance-trust-manifest
   cp scripts/python/pylib/build/morphism/provenance/trust/manifest/render.out keys/trust-manifest.txt
   make -C scripts/python/pylib morphism-ontology-consolidation
   cp scripts/python/pylib/build/morphism/ontology/consolidation/{silmaril-consolidated.ttl,shapes.ttl,queries.sparql,geosparql.sparql,manifest.ttl} ontology/
   ```

4. Commit the TTL, the key file, the manifest, and the regenerated ontology
   together, signed by an existing trusted key.

## Custody model

- **Herodotus** (`release`) — the openclaw agent's key; the secret half lives
  with that agent's owner.
- **GitHub web-flow** (`web-flow`) — GitHub's service key; signs commits made
  through the web UI. Public knowledge, no custody.
- **Claude** (`agent`) — session-agent keys are deliberately distinct from the
  openclaw identity and their secret halves are session-ephemeral: they die
  with the agent's container and are never exported. A future session without
  the key either ssh-signs (classified `SSH`, a warning under the default
  policy) or mints a successor `agent` key and appends it to the trust model.

Do not hand-edit `trust-manifest.txt` — it is generated, and CI fails on
drift. Never commit secret key material; `.gitignore` guards common export
names, but the guard is not a substitute for care.
