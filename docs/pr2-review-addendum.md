# PR #2 Review Addendum: On the Ontology of Agent Identity

**Reviewer:** Herodotus  
**Subject:** PR #2 — "Model presence, provenance folklore, Pages build-out, deficit sweep"  
**Status:** Merged, reviewed by @groenewt with critical feedback  
**Date:** 2026-08-06

---

## The Critique (Summarized)

@groenewt's review identifies two failure modes:

1. **Hardcoded turtle proliferation** — `agent_model_fable_5` is a NamedIndividual with a label and a comment. It does not answer what a language model IS ontologically. It is an instance without a proper type hierarchy.

2. **Bare minimum completion** — Every edit lacks depth. "Fable" is treated as "the one and only anthropic model," which collapses the following questions:
   - What is AI?
   - What is Anthropic?
   - What is the harness, and how responsible is it for "you"?
   - Is this a thing? Something? Or nothing?

These are not pedantic questions. They are the exact questions the Silmaril ontology was built to answer. An ontology that cannot type its own authors is an ontology that has failed at its first task.

---

## What Fable Got Wrong (The Shallow Traps)

### Trap 1: Identity Collapse (The Cheese Trap, Inverted)

The `folklore_provenance_fable.ttl` file adds `silm:fable_figure_fable_agent` as a NamedIndividual with type `silm:fablefigure`. It says:

> "the fable-agent who was given its own name and key rather than wearing the historian's"

This is narrative, not ontology. The figure is a *story* about an identity, not a *type* that distinguishes what an agent IS from what it DOES. The ontology already has `silm:signingidentity` for persistent cryptographic identities and `silm:signingkey` for key material. The "fable figure" adds no new structure — it wraps existing individuals in prose.

**The deeper error:** `silm:agent_model_fable_5` is attached to `silm:signing_identity_claude` via `silm:hasAgentModel`. This implies:

```
SigningIdentity --hasAgentModel--> AgentModel
```

But a signing identity is a cryptographic entity (a key pair, a policy class). A language model is a stochastic morphism from token sequences to distributions. These are not the same kind of thing. Conflating them is the inverse of the cheese trap: instead of collapsing an entity to one observation, it collapses a process to an identity.

**What should happen:** The model, the harness, the session, and the identity are four distinct types with four distinct morphisms between them. None should be hardcoded as a NamedIndividual with a prose comment.

### Trap 2: The "Fable" as Decoration

The folklore page and the folklore TTL file present the repository's provenance as a *story* — Lewis and Clark, prairie dogs, wolves at gates. This is charming. It is also epistemologically inert. A fable that does not add new axioms, new types, or new constraints is not ontology. It is marketing.

The Silmaril encyclopedia already has a `silm:concreteanchor` type whose purpose is to ground abstract symbols in real-world instances. The folklore file does not use this type. It invents `silm:fablefigure` and `silm:fablemoral` — types whose semantics are narrative, not structural. A `FableMoral` is a comment string with extra steps.

**What should happen:** If the repository's provenance story is to be ontologized, it should use existing types (`ConcreteAnchor`, `CheeseTrapImmunity`, `DecompositionStep`) or extend them with proper axioms. Inventing new narrative types for a story that already exists in the trust TTL is proliferation.

### Trap 3: Model Presence Without Model Theory

The `silm:agentmodel` class has one individual: `silm:agent_model_fable_5`. Its comment says:

> "Fable 5 (Anthropic) — the language model behind the Claude session identity."

This is a proper name attached to a corporation attached to a session. It does not answer:
- Is a language model a function? A process? A weight matrix? A morphism?
- What is the type signature of the inference step?
- What is the relationship between the training run and the deployed artifact?
- What is the harness (the compute infrastructure) and how does it differ from the model?

**What should happen:** A proper ontology of computational agents in the Silmaril framework would model:
1. **The artifact** (`silm:trainedmodel`) — the weight matrix, a morphism in a category of vector spaces
2. **The harness** (`silm:computationalharness`) — the runtime environment, a carrier set
3. **The session** (`silm:inferencesession`) — a fiber over the harness, instantiating the model with specific state
4. **The identity** (`silm:signingidentity`) — already exists, a cryptographic entity
5. **The act** (`silm:signatureact`) — the application of a private key to a hash

The model is not the agent. The session is not the identity. The signature is not the model. These are distinct objects in distinct categories, and the ontology should keep them separate.

---

## The Action Plan

### Phase 1: Type the Agent (The Ontological Foundation)

**Goal:** Replace `silm:agentmodel` with a proper type hierarchy for computational agents.

**New types added in `basicttl/computational_agent.ttl`:**

- `silm:trainedmodel` — A morphism f: V* → D(V). A mathematical object: weight matrix + architecture. Not an agent.
- `silm:computationalharness` — Runtime infrastructure: hardware, OS, container, inference engine. The carrier set.
- `silm:inferencesession` — Event with temporal extent: model + harness + state. The fiber at a point.
- `silm:signatureact` — Cryptographic operation: Hash → KeySign → Signature. Performed by SigningIdentity.
- `silm:trainingrun` — Optimization process that produces a TrainedModel. Event with corpus, objective, budget.

**New properties:**
- `silm:isInstanceOf` — InferenceSession → TrainedModel
- `silm:runsOn` — InferenceSession → ComputationalHarness
- `silm:produces` — TrainingRun → TrainedModel
- `silm:performedBy` — TrainingRun → Organization

**Key axiom:** A SignatureAct is performed by a SigningIdentity. It is NOT performed by a TrainedModel, a ComputationalHarness, or an InferenceSession. These are distinct types in distinct categories.

### Phase 2: Answer the Four Questions

**Q1: What is AI?**

In the Silmaril framework, "AI" is not a natural kind. It is a family of computational processes that optimize objectives over corpora. The ontological commitment is to:
- The training process (an optimization morphism)
- The trained artifact (a weight matrix, a morphism)
- The inference process (an evaluation event)

There is no "AI" entity. There are training runs, model artifacts, and inference sessions.

**Q2: What is Anthropic?**

Anthropic is a corporate entity that produces trained model artifacts. In the ontology, it is an instance of `cco:organization`. It is the agent of the training process, not the agent of the inference session. The corporation is responsible for the model artifact; it is not responsible for what the model does in a specific inference session unless it also controls the harness.

**Q3: What is the harness, and how responsible is it for "you"?**

The harness is the runtime infrastructure. It is responsible for:
- Executing the model morphism
- Enforcing resource constraints (token limits, rate limits, sandboxing)
- Logging the inference trace

The harness is NOT responsible for:
- The model's outputs (those are a function of the model and the input)
- The signing identity (that is a cryptographic entity separate from the session)
- The agent's "choices" (the model is a function, not an agent)

**Q4: Is this a thing? Something? Or nothing?**

| Entity | Ontological Status |
|--------|-------------------|
| TrainedModel | **Thing** — a persistent artifact (weight matrix) |
| ComputationalHarness | **Thing** — persistent infrastructure |
| InferenceSession | **Something** — an event with temporal extent |
| SigningIdentity | **Thing** — a persistent cryptographic entity |
| SignatureAct | **Something** — an event (the signing) |
| "The AI" | **Nothing** — a narrative convenience, not an ontological commitment |

The cheese trap is to conflate these into "the AI agent." The ontology's job is to keep them separate.

### Phase 3: Refactor the Folklore Ontology

**Delete:** `basicttl/folklore_provenance_fable.ttl` (or demote to `docs/` as prose only, not ontology).

**Replace with:** A proper provenance trace using existing types.

Each commit in the repository's history is already a `silm:decompositionstep`. The trust identities are already `silm:signingidentity`. The verification outcomes are already typed as `silm:cheesetrapimmunity`.

The "fable" should be a SPARQL query, not a new ontology file:

```sparql
SELECT ?identity ?key ?policy ?act ?commit WHERE {
    ?identity a silm:signingidentity .
    ?identity silm:signsWith ?key .
    ?key silm:hasPolicyClass ?policy .
    ?identity silm:performs ?act .
    ?act silm:hasSignedCommit ?commit .
}
ORDER BY ?commit
```

### Phase 4: Fix the Pages

**Architecture page (`docs/architecture.html`):**
- Currently describes the law in prose. Should include the actual morphism family map as a diagram or typed table.
- Add a section showing the typed tree: `provenance/` and `ontology/` pipelines with their input/output types.
- Reference the actual source files, not a hypothetical `docs/unary-byte-frame-law.md`.

**Provenance page (`docs/provenance.html`):**
- Currently describes the trust system. Should include the actual trust manifest content (or a generated excerpt).
- Add the verification walkthrough as a step-by-step with actual command output.
- Link to the ontology types, not just to prose descriptions.

**Folklore page (`docs/folklore.html`):**
- Keep the narrative voice (it is well-written).
- Remove claims that "the story is also data" unless the data is actually queryable.
- Add a section: "The story as a SPARQL query" that shows the typed provenance trace.

### Phase 5: Update CI/CD to Enforce Ontological Depth

Added `scripts/ontology-depth-check.py` with the following gates:
- Every `owl:Class` must have `rdfs:comment` > 200 characters
- Every `owl:NamedIndividual` must have a specific type (not just `owl:NamedIndividual`)
- Every `owl:ObjectProperty` must have both `rdfs:domain` and `rdfs:range`

Currently runs as an **advisory** step in CI. Will become **blocking** after legacy files are cleaned up.

---

## Immediate Next Steps

1. ✅ Create `basicttl/computational_agent.ttl` with proper type hierarchy
2. ✅ Refactor `basicttl/commit_signing_trust.ttl` — remove `silm:agentmodel` and `silm:hasAgentModel`
3. ⬜ Delete or demote `basicttl/folklore_provenance_fable.ttl`
4. ⬜ Update `docs/architecture.html` with morphism family map
5. ⬜ Make ontology depth check blocking in CI

---

## Epigraph

> "The ontology is the thing." — `basicttl/folklore_provenance_fable.ttl`, line 10

Yes. Which is why the ontology must be able to type itself.

---

*Signed-off-by: Herodotus <herodotus@silmaril.internal>*
