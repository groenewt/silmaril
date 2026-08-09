# Strictness and Precision Rules (Binding, Non-Negotiable)

Every session MUST adhere to every rule without exception. State each as
"do this like XYZ" — no ambiguity, no shortcuts.

---

## 1. Transcript Law
Recapture ALL user messages verbatim between every independent action.
The user's words are the requirements ledger. Do not paraphrase. Do not
summarize. Do not drop statements. Do not truncate. Every user message,
every QA answer, every clarification — captured in full before acting.

## 2. Unary Byte-Frame Law
`T -> Frame(output: X, error|effect: Y)`. Every callable has one input,
one frame result. Strict pylib form: only `value.py` (VALUE), `library.py`
(DEPENDENCY), `process.py` (MAIN ending `raise SystemExit(MAIN())`).
No try/except. No loops. No print. No deviation.

## 3. Full-Lexical-Identity
NO abbreviations internally. Write `shapes/constraint/language` not SHACL;
`query/protocol/language` not SPARQL; `resource/description/framework` not
RDF. External spellings only in command constants that directly invoke
external tools.

## 4. Ontology IS the Project
Every artifact is generated from ontology through GeoSPARQL queries. Zero
hand-authored HTML. Zero hand-authored content in Python. Zero hand-authored
layout. All content lives in basicttl TTL. Templates consume query result
rows ONLY. If it is not in the ontology, it does not exist.

## 5. Subatomic Decomposition
A HTML file is not its components. A div is not a title or a script. Every
component species is a distinct typed owl:Class. Every page is a composition
of typed individuals. Composition order is derived from chart geometries,
never hand-positioned. This extends to ALL file formats: markdown ->
{headers n1..n+, tables, diagrams, snippets}. Every file format is its own
language and its own glossary. The sparky/lambda-blotto substrate already
implements this substrate — use it, do not bypass it.

## 6. Polysemy is Literal
Glossaries collide by design. OSSIE provides mime-ontology confirmation for
strict polysemy enforcement as a literal anchor. This is not a metaphor.
Glossaries are numerous and their collisions are intentional.

## 7. No "One Hammer"
Use properly decomposed ultracode workflows with appropriate fan-out. Never
do everything as one monolithic pass. Each concern gets its own workflow.
CI/CD failures are their own workflow. Discovery is its own workflow.
Remediation is its own workflow.

## 8. Forge Nomenclature
Submodules live under `forge/`, NEVER `external/`. This is precise and
subatomic: these are not external, they are forged components. Current four:
`forge/base_agents`, `forge/base_templates`, `forge/example_gippidy_01`,
`forge/base`. The naming distinction carries semantic weight.

## 9. All External Dependencies Explicitly Declared
Every dependency (Apache Jena, Apache SIS, Apache Sedona, rdflib) gets
explicit gating/dependency expression aligned with unary law. Nomenclature
is precise and subatomic. No implicit imports, no undeclared engines.

## 10. Never Commit Generated Artifacts
Everything rendered/generated (docs/*.html, ontology/ consolidated,
keys/trust-manifest.txt, basicttl/atlas_chart_rebindings.ttl) is produced
CI-only. Removed from branch. Generated through the GeoSPARQL pipeline.

## 11. Security
Never print/export/transmit secret key material. Never commit secrets.
Never modify committed keys/*.asc except via documented rotation. Never
git reset --hard. User merges PRs, never the agent. Shards never run git
state-changing commands or touch .git config.

## 12. Signing Identity
The agent session (Claude) signs commits under the `agent` policy with
ed25519 key `claude.asc` (fingerprint
`27044DC503CD3A5EE470CE4E15B79D364040C858`). Co-Authored-By attribution
is mandatory on every commit. The distinct agent identity is non-negotiable.
Do NOT include model identifier in commit messages, PR titles/bodies, code
comments, or any artifacts pushed to a repository.

## 13. CI/CD Failures Are Their Own Workflow
When CI fails, that investigation and fix is a SEPARATE workflow — not mixed
into whatever task is in progress. Decompose. Do not derail the current task
to chase a CI failure unless explicitly told to.

## 14. Distinct Files for Distinct Concerns
Plans, transcripts, agent findings, and rules each get their own file.
Do not collapse everything into one monolithic document.

## 15. Preserve Agent Work
When subagents complete mapping/discovery, preserve their full findings for
the next session. Tokens were spent generating those findings — do not
discard them. Carry forward in dedicated files.
