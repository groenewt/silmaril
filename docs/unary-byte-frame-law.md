# Universal Unary Byte-Frame Law

Observed: `2026-07-14`

Status: **active red migration; the law is specified, but the enforcement
implementation does not yet satisfy the law it enforces**

## Document topology

This file is the authoritative index and law. Its focused continuations preserve
the same active-red status without exemptions:

- [Enforcement proof, semantic atomicity, findings, and fixtures](unary-byte-frame-law-enforcement-proof.md)
- [Censuses, self-host receipt, owned files, verification, and open dependencies](unary-byte-frame-law-receipts.md)

The three documents form one campaign record. A continuation may refine
evidence, but it cannot weaken, waive, or reinterpret this law.

## Law

Every exposed callable, independent of language, file type, path, declaration
spelling, or generated status, is inventoried as a typed arrow with one
explicit input and one explicit physical frame result. The current syntax
inventory includes Scala `def`, extension methods, callable-valued `val`
bindings and lambdas plus Java methods, explicit constructors, and Java
lambda/SAM bodies; those examples do not bound the law:

```text
T -> Frame(output: X, error|effect: Y)
```

This is the typed product required to construct a frame around a byte stream.
It is not a tuple, `Either`, `Try`, `Future`, raw `Result`, implicit exception,
or success/error sum substituted for the product. The input, output, and
error/effect are separately navigable coordinates. The frame is the Yoneda
point at which the callable's one observed input maps to its output and typed
effect.

This arrow law does **not** redefine the functional-programming triad. The FP
triad is exactly **Haskell, Elixir, Scala**. `T`, `X`, and `Y` name the three
separately normalized carrier positions of one callable frame; they are not
language identities and must never be described, generated, or queried as the
FP triad.

The callable positions also do not flatten the graph coordinate. `S`, `O`, and
`P` are independently typed, nth-dimensional vector/tower coordinates. Their
URN-addressed composition supplies the geometry used by frames, plans,
execution, and micro-partitioning. A scalar triple, raw tuple, or three unrelated
URN strings is not an admissible substitute for those towers.

## Semantic ancestry amendment

Observed: `2026-07-16`

Generic capability ancestry is not semantic ancestry. A semantic node, carrier,
frame coordinate, relation occurrence, or taxonomy value that directly extends
`highway.config.Sorted.Value` is rejected. `Sorted.Value` supplies only a
sorting/type capability; it does not define the value's immediate semantic
parent, subtype tower, components, lineage, or relationships. Adding direct
`highway.config.Projection.Byte.Substrate.Value` descent beside it does not
repair that loss.

Every admitted semantic carrier must physically descend through its exact
drilled parent carrier or parent component chain. That chain must itself reach
the canonical Lambda/bit-vector/byte substrate, retain a distinct physical URN
identity at each semantic coordinate, and expose independent subject, object,
and predicate tower evidence for each relationship. A binary `Lineage.of`
declaration, a parent URN passed to a constructor, a directory prefix, or a
shared generic base is evidence of debt only; none is a substitute for the
physical subtype and three-coordinate relation proof.

This rule applies equally to roots and leaves, including language, machine,
build, versioning, ontology, graph-schema, launcher, Input, Output,
Error-or-Effect, and Frame carriers. A bounded identity census cannot be green
while its semantic values use the direct-`Sorted.Value` shortcut.

## Full lexical identity amendment

Observed: `2026-07-16`

Every internal abbreviation, acronym, initialism, title-cased abbreviation,
lower-cased abbreviation, and fused expansion is rejected. Internal topology
contains the full lexical words as separately navigable physical, package,
type, and identity coordinates. The abbreviated spelling may remain only as
typed immutable source evidence on the external side of a registered bridge.
It never becomes an internal namespace, compatibility alias, field name, type
identity, or dispatch shortcut.

The first binding examples are:

```text
RDF -> Resource / Description / Framework
CPG -> Type / Graph / Instance / Instruction / Code / Property
URN -> Resource / Uniform / Name
URI -> Resource / Uniform / Identifier
JVM -> Language / Machine / Virtual / Java
BEAM -> Language / Machine / Virtual / Erlang / Abstract
SDK -> Language / Development / Kit / Software
JDK -> Language / Development / Kit / Software / Java
LLVM -> Language / Development / Compilation / Infrastructure / Low / Level / Virtual / Machine
JMX -> Language / Development / Extension / Management / Java
JNI -> Language / Development / Interface / Native / Java
JAR -> Language / Development / Build / Artifact / Archive / Java
NIF -> Language / Development / Interface / Native / Implemented / Function / Erlang
C++ -> Language / C / Operator / Plus / Plus
OWL -> Web / Ontology / Language
S/O/P -> Subject / Object / Predicate
SHA -> Secure / Hash / Algorithm
UTF -> Unicode / Transformation / Format
RGB -> Red / Green / Blue
IPC -> Communication / Client / Process / Inter
RPC -> Communication / Client / Client / Protocol / Procedure / Remote
MCP -> Communication / Client / Client / Protocol / Model / Context
LSP -> Communication / Client / Client / Protocol / Language / Server
HTTP -> Communication / Client / Client / Protocol / Hypertext / Transfer
mTLS -> Communication / Client / Client / Protocol / Transport / Layer / Security / Mutual
```

Every `Language/...` coordinate displayed above expands physically from
`Type/Graph/Instance/Instruction/Code/Property/Language/...`. The shortened
form is prose notation only; no top-level `Language` facade, forwarding
package, or compatibility type is admitted.

`Language` is the universal linguistic substrate for these coordinates, not a
folder whose meaning is restricted to programming languages. Lexical form,
syntax, sentence, context, semantics, and polysemy remain independently
navigable language coordinates. Source code, assembly, instruction sets,
machine code, and serialized binary are projections and relations within that
same substrate.
`Language/Development` is its shared development subtree, not an
abbreviation-expansion bucket. `Kit`, `Transpilation`, `Compilation`, `Build`,
and `Assembly` are independently navigable descendants.
`Language/Development/Kit/Software/Java` specializes the
software-development-kit branch; it does not place `Development/Kit` beneath
`Java`. Compiler infrastructure such as the externally spelled `LLVM` is
drilled through
`Language/Development/Compilation/Infrastructure/Low/Level/Virtual/Machine`.
Assembler and disassembler identities descend independently through
`Language/Development/Assembly`; neither is flattened into a compiler label.
Build-system identities descend through `Language/Development/Build/Tool`;
external command spellings such as `mvn` are bridge evidence for Maven, never
internal aliases. Make, CMake, and Nix retain distinct product identities,
with every initial or fused component lexically normalized before admission.
The external `jar` command is a Java development-tool operation; a Java archive
is a `Language/Development/Build/Artifact/Archive/Java` value. They are
distinct nodes joined by an explicit production or inspection relation. Java
management extensions, the Java native interface, and Erlang native
implemented functions likewise occupy distinct `Extension`, `Interface`, and
language/runtime bridge coordinates. Elixir access to an Erlang native
implemented function is a typed projection across that bridge, not a second
`NIF` identity.

The initial representation and translation topology is:

```text
Type / Graph / Instance / Instruction / Code / Property / Language
  / Representation / Serialized / Binary
  / Machine / Code
  / Instruction / Set / Architecture
  / Assembly
  / Development / Compilation / Compiler
  / C
  / Rust
```

`ISA` and `ASM` are external evidence spellings for the independently
navigable instruction-set-architecture and assembly coordinates. C and Rust
source, compiler invocation, assembly, instruction-set selection, machine
code, and serialized binary are distinct nodes. Their direction is expressed
only by typed unary transformation frames with explicit output and effect
coordinates; it is not inferred from directory ancestry or compressed into a
single compiler callable.

The corresponding operator reference is maintained at
`docs/reference/Resource/Uniform/Name/Dictionary.md`. The operator evidence
label `URANARY` does not authorize an abbreviated internal coordinate.

The abbreviated communication spellings are external protocol evidence, not
internal definitions. Ingress, egress, send, receive, port, and payload continue
as independently typed descendants of the exact protocol family, for example
`Communication/Client/Client/Protocol/Model/Context/Port`. An external field
spelled `value` must be mapped to the typed `Payload` coordinate by a lawful
bridge; it does not authorize a `Value` package alias. Remote procedure call
uses the external protocol branch, while inter-process communication uses the
internal process branch. `Thrift` remains a proper product/protocol name
rather than being decomposed as an acronym. The doubled `Client/Client`
coordinate intentionally marks an external-facing client surface. Internal
communication remains on the single-`Client` branch; the two coordinates must
not be collapsed as lexical duplication.

Accordingly, new identity terminals use the shared Resource-first coordinate
`Type/Resource/Uniform/Name/Value.scala`, not
`Type/Uniform/Resource/Name/Value.scala` or `Type/Urn/Value.scala`. Related
resource identities drill distinct branches below the same prefix:

```text
Type / Resource / Description / Framework
Type / Resource / Uniform / Name
Type / Resource / Uniform / Identifier
```

Unicode transformation formats and secure hash algorithms are not flat
acronym-derived type families. Their internal carriers descend physically
through the bit, octet, and octet-pair substrate; spellings such as `UTF-8` and
`SHA-256` remain immutable external evidence observed through registered
bridges.

Camel-case substitutions such as `uniformResourceName` still reject because
they fuse three semantic coordinates into one identifier. A one-word field may
reference a carrier whose drilled type supplies the complete meaning.

The current `highway.config.Urn`, `Type/Urn`, and `dtype` spellings are
inherited red migration dependencies. Their appearance elsewhere in this
historical receipt describes the observed implementation; it is not a
canonical spelling, exemption, or template for new work. The
functional-programming triad remains exactly Haskell, Elixir, and Scala; this
amendment does not reinterpret that triad.

## Build bootstrap boundary

Observed: `2026-07-16`

The SBT bootstrap trust root authorizes the external toolchain boundary only.
It does not exempt build-source declarations from the unary byte-frame law,
full lexical identity, physical byte descent, explicit lineage, atomic body,
or bridge-handler requirements. Internally, `Sbt` is the red abbreviated
spelling of the drilled `Simple/Build/Tool` coordinate.

The operator-named entrances
`project/highway/build/Source/Layout/Identity/Read.scala` and
`project/highway/build/Source/Admission/Apply.scala` expose one explicit input
and delegate to a declared frame, but that surface shape is not closure proof.

The earlier same-day snapshot named their delegated topology
`Sbt/Compatibility/Settings/{Input,Output,Frame,Effect}` and observed raw SBT
values, absent physical byte descent, absent identity lineage, and multi-stage
settings programs inside output constructors. That paragraph is retained as
historical red evidence. It is stale as a description of the current physical
topology and is not an accepted compatibility coordinate.

At the `2026-07-16T17:15:22-0500` checkpoint:

- the internal topology is drilled through `Simple/Build/Tool`; no
  `Sbt/Compatibility`, `Scala/Build/Tool`, `sbtProjection`, or
  `scalaBuildToolProjection` coordinate remains in the scoped source set;
- unmanaged and generated managed sources have distinct root, ownership,
  provenance, identity, and verification coordinates; the managed root is not
  admitted as a module base or accepted escape path;
- PathFinder construction, direct selection, descendant selection, and
  materialization are separate operation-specific external adapter leaves;
- the offline SBT `reload` entrance exits zero, and the source-set entrance
  reaches the compiler with the full observed tree rather than the earlier
  empty unmanaged set;
- the fresh compiler entrance observes `19,481` Scala sources and `4` Java
  sources, including `72` generated managed Scala sources, then reports `846`
  application errors;
- after compiler diagnostics, both `(config / Compile / admission)` and
  `(config / Compile / verifyUnmanaged)` still reject with
  `Opened descriptor cannot be associated with its source coordinate`.

The build boundary therefore remains red. Its `691` scoped Scala files contain
`166` `def` declarations, `10` declared Frame results, `124` explicit returns,
`2` explicit throws, and zero canonical physical descents from
`highway.config.Projection.Byte.Substrate.Value`. All `166` declarations remain
uncertified by the complete law. The build-local
`Bootstrap/Carrier/Unverified` root records debt; it is not a byte-substrate
proof. Zero wildcard imports and zero import declarations outside scoped
`External/Adapter` leaves do not compensate for `140` direct fully qualified
host-reference lines still outside those leaves. A trust-root import does not
turn an external package value into a primordial carrier, and a one-line outer
delegation does not make the delegated multi-stage constructor subatomic.

The exact command, logs, error categories, census digest, and historical
`19,456`-source checkpoint are recorded in
`docs/campaigns/build-bootstrap-unary-law-red-receipt-2026-07-16.md`.

## Normative boundary law

Owned modules remain audited after encapsulation; modular boundaries grant no exception.
Isolation is permitted only for immutable upstream provenance or typed host effects; it
never exempts an owned callable, validator, lineage, parity obligation, node, edge, or property.

Physical byte descent in the callable checks below is necessary but not
sufficient. The input, Frame, output, and error-or-effect carriers must also
satisfy the semantic ancestry amendment above; direct generic sorting ancestry
rejects even when the byte-substrate and URN spellings are present.

For each callable, the Source Discipline audit now requires:

1. exactly one parameter clause containing exactly one parameter;
2. an explicit, non-`using`, non-`implicit`, non-`given`, non-`erased`,
   non-default input;
3. physical transitive descent of the input carrier from
   `highway.config.Projection.Byte.Substrate.Value`;
4. explicit URN identity evidence on that physical primordial carrier;
5. an explicit result type whose physical terminal path is
   `Frame/Value.scala`, with the same byte-descent and URN-identity proof;
6. exactly two explicitly typed frame coordinates: one `val output: X` and
   exactly one `val error: Y` or `val effect: Y`;
7. physical byte descent and URN identity for both `X` and `Y`;
8. exactly one physical body line containing exactly one top-level expression;
   an absent body, local declaration sequence, multiline expression,
   multi-statement block, or explicit `return` in Scala rejects;
9. that expression performs exactly one atomic semantic operation or one typed
   delegation. Compressing several comparisons, calls, decision matches,
   planner stages, or state transitions onto one physical line still rejects;
10. no overload identity and no explicit `throw` or Java `throws` effect.

## Explicit binding and observation law

### Python process form

The process-form correction in `STRICTNESS_RULES.md`, rule 2, replaces the
former nullary terminal trailer with `MAIN(input: Input) -> Frame`. MAIN has
exactly one explicit, typed, non-default input and returns the declared physical
Frame. Importing its `process.py` module performs no invocation. A process does
not read implicit environment or command-line input, raise SystemExit, or
substitute an integer exit status for its Frame.

Host input observation and host termination occupy separately typed registered
boundaries. Completion must preserve the output and effect coordinates and
their evidence before the host consumes an admitted termination instruction.
The host's termination is an observed external effect, not a returning owned
callable or an exception-based replacement for the Frame. This correction
settles the process syntax; it does not admit an implementation, waive physical
carrier closure, or make a previously unobserved launcher executable.

The callable law is language-neutral. Scala and Java name the current scanner
surface; they are not a scope ceiling or an ontology. Each Haskell, Elixir,
Scala, Java, BEAM, native, script, generated, or later language frontend must
project its syntax through a registered ContractGate observation into the same
typed physical evidence. A language that lacks a current frontend remains
unobserved and red; it is never silently outside the law.

The same audit root enforces three additional rules without a file, path,
adapter, language, generated-source, launcher, test, or build exemption:

11. no glob or wildcard import is admissible. Scala/Java `*`, legacy Scala `_`,
    wildcard selectors, and equivalent language forms reject. Every imported
    coordinate is named explicitly or the binding does not exist;
12. explicit spelling alone is not external-dependency admission. Every host,
    JDK, runtime, native, filesystem, descriptor, process, network, clock,
    digest, compiler, or library symbol must cross its registered typed
    ContractGate boundary. Placement below `adapters/jvm` or an exact
    `java.nio.file.Files`-style import grants nothing;
13. file extension, file type, path prefix, language identity, declaration
    kind, annotation, generated status, and naming convention are observations,
    not definitions. A rule such as “this file type in this language with this
    declaration means X” rejects unless a physical typed identity and behavior
    contract independently proves X;
14. Python campaign/runtime code is not executable merely because it has a
    `.py` suffix or sits below `scripts/python`. Its physical implementation,
    config carriers, registered external bindings, unary launcher, and typed
    readback must first be integrated in the registered recursive physical tree
    rooted at the exact directory `scripts/python/pylib`. A Python helper
    outside that tree, a reference-only tree, a missing package/config
    dependency, or an unregistered direct interpreter entrance remains red and
    must not be executed.

A Markov chain may model ordered process state and transition probability. A
gateway, bridge, tunnel, frontend, adapter, or parser may transport and observe
that process. Neither defines the carrier, identity, callable effect, or
semantic operation it observes. Those remain separately URN-addressed physical
coordinates with exact lineage and byte-frame evidence.

The required terminal finding families are drilled, not fused:

- `Import.Binding.Wildcard.Present.Value`;
- `Import.Binding.Explicit.Absent.Value`;
- `External.Binding.Contract.Gate.Absent.Value`;
- `Definition.Authority.Inferred.Value`, whose evidence retains separate
  File, candidate File-Type or Suffix, Declaration, and Path observations plus
  an explicit absent Authority coordinate. A Language coordinate is present
  only when a registered typed frontend independently proves it; none of those
  observations may derive one;
- `Shell.Definition.Cardinality.Value`;
- `Shell.Callable.Contract.Absent.Value`;
- `Shell.Expansion.Wildcard.Present.Value`.

`Import.Binding.Wildcard.Present.Value` and
`Import.Binding.Explicit.Absent.Value`,
`External.Binding.Contract.Gate.Absent.Value`, and
`Definition.Authority.Inferred.Value` now exist with their own Type/URN
identities and direct lineage to the normalized Finding.Code parent. Wildcard
and unbounded-given imports now emit explicit-binding absence; a hidden alias
creates no binding. Primordial declaration authority now joins the current
source identity, terminal `Value.scala` shape, physical carrier catalog,
Byte-descendant closure, and identified-carrier catalog instead of inferring
authority from a path, suffix, language, or declaration spelling.
The three Shell families likewise have distinct Type/URN identities and direct
lineage to the normalized Finding.Code parent; the `Shell` and `Expansion`
words are independent segment carriers.
Language-neutral frontend evidence and positive typed external
admission/readback remain absent. Those gaps are enforcement failures, not
exemptions or reasons to weaken the law.

The `2026-07-16` physical Python census is likewise red. `scripts/python`
contains `1,191` Python files: `1,141` below `pylib` and `50` outside it.
The production-shaped `pylib/src` frontier contains only `59` files, while
`1,082` files remain under `pylib/reference`. All `59` production-shaped files
import a `config` package that is absent from `pylib/src`; there is no
`pyproject.toml`. The combined pylib tree contains `342` `def` declarations,
including `236` raw `Bytes -> Bytes` arrows. Its `382` external-gate import
lines are spelling evidence only until their physical registrations, launcher,
and readback are proven. Zero Python wildcard-import lines were observed, but
that does not cure the missing package and callable-law evidence. No Python
file in this census is claimed as executed or admitted.

The frozen Lambda Blotto red receipt is `68` files and `771` physical lines,
with `9` unary Frame arrows and `9` exact output-plus-effect Frames. Its parser
and static checks pass. The current chain is:

```text
Heat unavailable
 -> Subject
 -> Object
 -> Predicate
 -> Delta
 -> Sigma
 -> Pi
 -> Hybrid
 -> independence unavailable
 -> Barrier
 -> Wingtip refusal
 -> Continue(original heat input)
```

This does not make that engine green. The modes are relays. Accepted
role-vector input, current heat, independence, Narrow, Wide, allocation,
Complete, proof, receipt, root input, and tests remain absent.

The `2026-07-16` Bash frontier is also active and red. Full-audit traverses
the registered `scripts` and generated `captures` roots, while focused-file
inspection accepts any repository-relative `.sh` or `.bash` surface and any
extensionless file with a registered Bash or shell shebang. The suffix and
shebang select a shell syntax observer only; neither supplies type, identity,
ownership, operation, or effect authority. Every shebang/top-level script
entrance is inventoried as `script`, and every declared shell function is
inventoried independently. Generated capture status grants no exemption.

One shell file has exactly one callable definition. A shebang/top-level
launcher therefore contains no function declaration, while a
declaration-only shell library may contain one function and no top-level
operation. Zero or plural definitions emit
`Shell.Definition.Cardinality.Value`; line count is evidence only and never
substitutes for physical definition cardinality.

Each admitted shell callable declares exactly these four immutable bindings:

```text
readonly <callable>__input_type='<identified byte-descendant Value>'
readonly <callable>__frame_type='<identified byte-descendant Frame.Value>'
readonly <callable>__operation_type='<identified byte-descendant Value>'
readonly <callable>__binding_type='<identified byte-descendant Contract.Gate Binding.Admission.Accepted.Value>'
```

The input body observes position `$1` and no other numeric, `$@`, `$*`, `$#`,
or `shift` input surface. The declared Frame resolves through the same
physical primordial catalog as Scala and Java and still has exactly one
`output` plus one `error|effect`, all identified byte descendants. The body
contains one non-declaration physical command and no command chain, pipeline,
subshell/command substitution, local declaration, assignment, explicit
`return`, `exit`, or `trap`. Glob expansion, array-wide expansion, `$@`, and
`$*` emit `Shell.Expansion.Wildcard.Present.Value`. A dynamic or wildcard
`source`/dot binding also emits the existing explicit/wildcard import
findings, and every source binding remains rejected by
`External.Binding.Contract.Gate.Absent.Value` until its exact typed
ContractGate admission exists.

The current repository census is exact: `15` Bash files, `702` physical
lines, `12` declared functions, `27` independently inventoried callable
entrances, `4` shell contract-coordinate declarations, and `3` source/dot
bindings. The four coordinates belong to the new physical
`scripts/source/discipline/gate/shell/launcher/value.sh` entrance. The other
`26` callables remain without the complete shell contract and therefore emit
`Shell.Callable.Contract.Absent.Value`; every preexisting file containing a
function also has plural script/function definitions. Exactly `5` current
files therefore emit `Shell.Definition.Cardinality.Value`.

The new launcher is one physical script definition with no function
declaration. It observes only `$1`, executes one `printf` projection, and
declares identified input, Frame, operation, and accepted ContractGate binding
coordinates. Its operation identity is the drilled
`highway.config.gates.Source.Discipline.Shell.Launcher.Operation.Value`;
its input and Frame are the existing physical Text/Read carriers. It is a
Sparky-era shell entrance, not a predecessor alias or compatibility launcher.

`scripts/ci.sh` is not exempt. It has four definitions: its top-level script
entrance plus `ci_finish`, `wire`, and `fail`. `ci_finish` observes zero input
positions, `wire` observes positions one and two, `fail` observes exactly
position one, and the top-level entrance observes positions one and two plus
dynamic array/shift surfaces. Consequently `ci_finish`, `wire`, and the
top-level entrance emit input-cardinality findings. Unary `fail` still rejects
because its typed input/Frame/operation/binding coordinates are absent and its
explicit `exit` is an untyped effect. All four bodies are multi-stage rather
than one-command arrows.

The exact `2026-07-16` implementation now inventories Scala `.*`, legacy
Scala `._`, multiline selector wildcards, equivalent Scala export bindings,
Java `.*`, and Java static `.*`. Wildcard bindings are excluded from import
resolution, wildcard fallback is removed from use resolution, intrinsic
ownership rejects them, and legacy boundary registration cannot authorize
`*` or `_`. Alias hiding such as `None as _` is not a wildcard binding because
it creates no imported local binding.

The Gate also emits `External.Binding.Contract.Gate.Absent.Value` for external
imports, qualified external references, and external declaration references
before and independently of legacy boundary-spelling permission. An adapter
path plus exact old registration can suppress only the predecessor
outside-adapter finding; it cannot suppress typed ContractGate absence. The
positive typed admission path remains red: Gate has no admitted-registration
catalog/readback input, and `Registration.Admission.Apply` still returns
Rejected. Exact spelling does not cure admission. Neither self-hosting nor
bootstrap status grants an exception.

Physical line count is therefore necessary but not sufficient. A long nested
expression is not a subatomic callable merely because formatting places it on
one line. Multi-stage work is represented by typed stage state and a unary
scheduler step whose output is `Continue(nextState)` or `Complete(result)`;
each scheduler invocation performs one transition only.

Carrier initialization is not a behavior loophole. A Frame, Output, Effect,
State, or other primordial carrier may retain and project typed coordinates,
but it may not execute a comparison, conjunction, parser, planner transition,
adapter call, or other semantic operation in a constructor argument default,
field initializer, companion initializer, or inheritance expression. That
operation belongs in its own lawful unary behavior arrow.

There is no callable constructor exemption and no constructor-method fixed
point. Primary data-constructor syntax is a separate syntax category. It is
admitted only within a lexically drilled config behavior whose innermost
callable already satisfies the complete law above. The callable's declared
physical Frame result derives the only construction closure:

```text
{ declared Frame, Frame.output carrier, Frame.error|effect carrier }
```

The closure is resolved from physical primordial types and has exactly three
identified byte-descendant carrier coordinates. A fourth carrier, a malformed
Frame, a non-Frame result, a non-lawful enclosing callable, or construction
outside config behavior rejects. Scala and Java use the same derivation.
Neither a path spelling nor a `Construct/Apply.scala` suffix authorizes a
callable or carrier.

This is not a prefix rule, name list, adapter privilege, compatibility alias,
ignore, greylist, baseline, or waiver. `audit(root)` and `files(root, files)`
always apply the callable law. The focused-file entrance also computes global
case-fold namespace collisions, so it cannot hide a conflict with an
unchanged path.

## Sealed Self-Hosting Closure

The terminal acceptance boundary is a sealed graph-and-build loop, not the
existence of a source catalog. The loop has five separately receipted states:

1. pinned Spark and Joern source bytes, syntax occurrences, build
   declarations, and graph relations;
2. their owned, lexically normalized code-property graph with exact
   source-to-owned mappings;
3. the owned Scala and build-language twin compiling or transpiling the
   repository;
4. that successor using the same owned twin to compile or transpile itself;
5. deterministic owned-to-readback mappings whose topology, content, and
   relation digests equal the planned successor.

No state is inferred from the next state. Every transition names its input
schema, output schema, preserved invariants, typed effect, and certificate.
The sealed result requires stable repeated digests, a verified byte-complete
inverse, and a drift-free predecessor recapture immediately before commit.

Lexical normalization, exact semantic-family subtype closure, independent
subject/object/predicate towers, the Universal Unary Byte-Frame law, explicit
external ContractGate bindings, and the wildcard prohibitions gate every
state. A successful upstream replay, parser pass, compiler pass, or build pass
cannot waive a failed coordinate gate. Spark and Joern names remain immutable
provenance; their syntax, declarations, calls, control/data flow, build
relations, and schemas become owned navigable evidence rather than forwarding
packages.

## Split and Consolidated Render Seal

The terminal render is a reversible pair over the complete owned syntax tree
and physical file-tree graph. Both physical projections are required:

1. the split projection drills the entire graph into a normal form with exactly
   one precise semantic thing per file; and
2. the consolidated projection emits the entire codebase as exactly one
   physical Scala source file containing one root class and recursively nested
   inner classes. It uses Scala inner-class path dependence, not singleton or
   inner objects, to make the complete namespace and syntax tree turtle inside
   that one root instance.

A semantic thing is one independently identified carrier, identity, relation
occurrence, input, output, error-or-effect, Frame, algebraic alternative,
state, stage, or unary operation. A split file cannot become a bag of adjacent
definitions merely because they share a package, family, generator, or host
language. The consolidated Scala file is one aggregate render, but it does not
fuse its nested children into one semantic identity or authorize one
monolithic callable. Its generation and traversal remain compositions of
subatomic unary Frame arrows, one observed transition per scheduler invocation.

The single-file render is a structural proof witness, not a packaging or
distribution optimization. Its inner-class containment must reproduce the
exact semantic ancestry, lexical drill-down, chain order, scheduler-stage
boundaries, byte-stream attachments, and independent subject/object/predicate
relationship topology of the owned graph. The physical split may disappear
inside the one compilation unit; none of that semantic structure may disappear.
The resulting source must expose the required topology directly to Scala's
type system. A raw lookup map, string-key dispatch table, reflection layer,
forwarding alias, generated compatibility facade, or generator-only side table
cannot supply the proof.

Every nested class is bound to the exact outer render instance. A child of one
consolidated snapshot is therefore a different path-dependent type from the
same lexical child of another snapshot. Widening those children to a
cross-instance type projection rejects unless a separately identified unary
bridge declares the conversion, output, and effect. This instance boundary is
part of the render seal, not a host-language implementation detail.

Split and consolidate are inverse render operations, not two hand-maintained
authorities. They preserve every source byte and byte schema, lexical locator,
file and declaration boundary, child order, identity, exact semantic
progenitor, and independent subject/object/predicate relationship occurrence.
The one-file projection carries the original physical file coordinates as
typed render evidence so its inverse can recreate the exact split tree.
Comments, whitespace, external spellings, generated status, and physical
account evidence remain typed syntax or provenance coordinates rather than
discarded trivia.

Acceptance requires separately identified unary input, output, effect, and
Frame carriers for both directions plus deterministic certificates for:

```text
consolidate(split(graph)) == graph
split(consolidate(graph)) == split(graph)
```

Equality includes topology, ordered content, byte revision, identities, and
relationship digests after a drift-free recapture. A lossy syntax tree, a
pretty-print approximation, a manually divergent one-file projection, a
forwarding file, or a split that drops physical entries remains red. The Atlas
and Graph views may colimit each other through this pair, but neither
projection may invent, erase, or silently rename a coordinate.

Compiling the one-file projection is necessary but insufficient. The proof
closes only when the compiler-observed nested type graph equals the planned
semantic topology and both inverse renders reproduce the complete physical and
relationship accounts. This is how the consolidated projection proves that
the repository's topology and chains have the required structure rather than
merely a preferred visual style.

The path-dependent mechanism is the one documented by the Scala language tour
at `https://docs.scala-lang.org/tour/inner-classes.html`: member classes belong
to an outer instance. The seal retains that per-instance distinction; it does
not substitute a singleton-object namespace.

## Complete Component Account

The seal also requires a content-addressed predecessor/successor account for
every in-scope physical entry and declaration, including tracked, untracked,
ignored, generated, cached, and control-plane surfaces. Each account row keeps
these coordinates distinct:

- lexical locator;
- physical device, inode or file-node, generation, and opened-handle
  observation where the host exposes them;
- byte revision and observation completeness;
- semantic identity and exact semantic-family progenitor;
- consumers and independently typed subject/object/predicate relationships;
- disposition: reuse, migrate, split, merge, retire, conflict, or provisional;
- successor identity and inverse evidence.

No label such as `duplicate`, `neglected`, or `unnecessary` authorizes deletion.
A duplicate requires identity and denotation evidence; a retirement requires
consumer closure plus a byte-complete inverse; an unresolved meaning remains
provisional. Locator equality, case-fold equality, inode equality, content
equality, and semantic equality are separate observations and never substitute
for one another.

Semantic family membership is likewise physical, not lexical. Every compiler
must descend through the canonical compiler progenitor, every machine through
the canonical machine progenitor and its exact branch, and the same rule
applies to build, assembly, versioning, and every later family. Package or path
prefixes and binary `Lineage.of` records do not establish that closure.
Independent content-addressed relationship occurrences weave the proven
family anchors into the lineage yarn consumed by Lambda-Blotto combinators.

## Byte-Stream Carrier Closure

The physical carrier is fundamental. Inputs, outputs, effects, identities,
graph occurrences, plans, receipts, and inverse evidence are not arbitrary
host values awaiting later serialization. Each physically descends from an
identified Lambda byte-vector, byte-set, or ordered byte-stream carrier and
declares the schema needed to interpret its bits.

`Byte` is not an alias for `Octet`. Bit width, bit order, byte order, encoding,
and registered width bounds are independent coordinates; the schema family
admits registered byte widths through `128` bits. An Octet Sequence is the
eight-bit projection only and cannot serve as an unproved universal byte root.
A host `String`, collection, path, Java or Scala object, shell word, or Python
object may be observed only through its exact typed ContractGate frontier and
the resulting byte carrier. It never becomes an implicit fourth callable
coordinate.

The Frame remains the physical Yoneda point for one such input stream. Its one
output and one error/effect coordinate separately descend through the same
identified byte-carrier system. Subject, object, and predicate towers retain
their independent semantic geometry while each tower's physical evidence is
encoded by an explicit byte-stream schema; semantic independence does not
authorize an untyped physical representation.

Byte-vector and byte-set construction is closed algebraic admission, not a
public host constructor. The ordered vector family has separately identified
schema-qualified `Empty` and `Link` alternatives; a Link carries one admitted
bit-vector head and one tail with the same byte schema. The unordered set
family has its own separately identified alternatives and never supplies
sequence order by convention. Every alternative, progenitor, admission state,
and identity occupies its own physical file and URN coordinate.

The attachment from bytes to an abstract value keeps four layers distinct. A
stream is an ordered sequence of schema-qualified byte occurrences. A block is
a bounded, complete or explicitly incomplete span over one stable stream
revision; an offset, locator, or host slice is not its identity. A container is
an admitted organization of one or more blocks with explicit schema and
boundary evidence. A value is the typed algebraic interpretation of that
container with its own Type/URN and independent subject/object/predicate
relationships. The attachment between layers is itself a typed, receipted
arrow; inheritance or a matching path spelling is insufficient.

Byte width and stream extent are different cardinalities. The `1..128` bound
governs the number of bits in one byte occurrence. Stream ordinal, block start,
block end, and block length count byte occurrences and use their own validated
non-negative, generation-sized carriers; they cannot reuse the width carrier
or a raw fixed-width host integer. This distinction remains valid at
Avogadro-scale partition counts.

The shared recursive positive Count authority is nevertheless realized through
`256`: `Unit` denotes one and each `Successor(previous)` denotes exactly the
next positive count. Width admission consumes only its `1..128` refinement.
The separately typed eight-bit byte and color-channel code space has cardinality
`256`, while its value ordinal is a distinct non-negative carrier ranging from
`0` through `255`. Count `256`, ordinal `255`, and bit width `128` are therefore
three navigable coordinates; none may be reused as, inferred from, or collapsed
into another.

The bit/schema bootstrap is an explicit initial algebra, not a hidden ancestry
cycle. The separately identified bit alternatives and schema grammar are
constructor-free definitions at the eigenvalue trust root; they expose no
callable motion and do not borrow a host Boolean or integer as authority. A
typed closure certificate records how that grammar constructs the first
admitted byte vector and proves schema-to-bits-to-schema readback. After that
closure, every exposed operation still consumes one admitted byte carrier and
returns a physical Frame whose output and error/effect are admitted byte
carriers. Calling the bootstrap an exemption, or making Bit and Byte inherit
from one another, rejects.

That first closure is concrete rather than a generic claim about emptiness.
Its registered initial schema separately identifies a one-bit positive width,
most-significant-first bit order, single-byte order, and unsigned-binary
encoding with exhaustive `0 <-> Zero` and `1 <-> One` inverse evidence. The
`Byte.Vector.Empty` alternative's Type identity and the first empty occurrence
identity are different coordinates. The occurrence explicitly attaches the
registered schema and an ordered empty-stream revision; a closure certificate
binds both identities and proves exact schema readback without inferring a
schema from the absence of payload bits. The first non-empty Link then enters
through ordinary unary admission from that already admitted occurrence.

An admission gate remains a unary Frame arrow. Its output coordinate may be a
closed admission-state algebraic data type, but `Accepted|Rejected` never
replaces the Frame product: the output state and typed error/effect evidence
are both present, separately navigable, independently identified byte
descendants. A raw array, tuple, collection, constructor call, or pattern match
cannot bypass this gate.

Matrices, surfaces, polygons, and shapes are distinct higher-dimensional
Lambda-vector algebraic families above the admitted physical byte carrier.
Each declares its own rank or dimension, coordinate towers, boundary and
incidence evidence, topology or geometry invariants, and Type/URN lineage.
They are not aliases for nested host arrays, scalar triples, or byte vectors;
the byte stream supplies their physical evidence while the independent Lambda
vectors retain their semantic geometry.
