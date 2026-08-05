# Telephone pylib integration audit

Audit frame: 2026-07-19, staged source compared read-only with `/data/src/scripts/pylib` (the symlinked live tree in `cpg-highway`). Telephone remains the active owner of that live path, so this audit does not promote or overwrite it.

## Snapshot and collision matrix

| Surface | Staged use | Live dependency or owned surface | Exact relative-path collisions | Decision |
|---|---|---|---:|---|
| Executable corpus capture | `src/silmaril/sparky/lambda_blotto/**` | Live `src/silmaril/sparky/lambda/**` remains untouched | 0 | New Python-safe namespace; append-only candidate |
| Constants | `src/config/constants/lambda_blotto/**` | Live constants remain untouched | 0 | New namespace; append-only candidate |
| Effect implementations | `src/config/gate/external/python/lambda_blotto/**` | Live Telephone gates remain untouched | 0 | New namespace; append-only candidate |
| Shared byte carrier | Imported only through `config.gate.external.project.sparky.substrate.byte.vector.library` | Live SHA-256 `dd28b206c8d0e9b4c546fb906000f90506f13ebb733f1c45134930a327827220` | 0 | Reuse; do not duplicate carrier |
| Integer carrier gate | `config.gate.external.python.base.builtins.int.value` | Live SHA-256 `b3a4279223c20461a8b5c4063fdd91d716c98f26d9ef8b79c766f8a287240f0e` | 0 | Reuse |
| Immutable carrier gate | `config.gate.external.python.stdlib.dataclasses.library` | Live SHA-256 `952cb8db1ee305526d8d8e8fe0f31cb8ec982e780050a3f99195bc427bfb1278` | 0 | Reuse |
| Exact observation gates | Stage-only `os`, `fcntl`, `stat`, and SHA-256 leaves under `config/gate/external/python/stdlib/**` | Existing live module-level gates are not modified | 0 | Add leaves; all external imports remain below the dependency gate |
| Live process/file API | No write at `src/silmaril/sparky/lambda/invocation/process/file/*` | Telephone-owned live files | 0 | Preserve unchanged |
| Exact corpus routing | `publication/routing/occurrence/**`, `publication/routing/serialize/**`, `phoenix-disintegration-routing.json`, `federated-computing-substrate-routing.json` | No live counterparts at this frame | 0 | Exact text/locus/revision/time/authority/resolution/non-exclusivity/classification/support-boundary projection; append-only candidate |
| Contract verifier and tests | `src/silmaril/sparky/contract/file_capture_static/**`, `tests/**` | No live counterparts at this frame | 0 | Append-only candidate |

At this frame the stage contains 553 non-`__pycache__` files, including 545 Python source files. The actively changing live tree contained 2,073 files when sampled at Git revision `06c7cb8c02289410dc1434e556a49a6d261697a9`; that count is a time-scoped observation, not a stable size claim. An ignored-aware relative-path comparison reports zero overlaps. AST dependency resolution finds exactly three project imports supplied by the live tree: the shared byte-vector gate, integer carrier gate, and dataclasses gate listed above. Every other project import resolves inside the stage.

## Law and runtime matrix

| Law | Implementation witness | Validation witness | State |
|---|---|---|---|
| Immutable carriers | Frozen, slotted dataclasses for operation roles, states, provenance, frontier, receipt, diversity, and routing | Static role scan plus runtime mutation rejection | GREEN in stage |
| Unary transition | Every operation exposes `apply(value: Input) -> Frame`; file and directory schedulers take one immutable input and advance one algebraic state | Static operation-quartet/arity scan; no scheduler loop | GREEN in stage |
| Explicit effects | Every frame carries an effect; internal fragments default to Provisional, while schedulers propagate the caller's explicit evidence class | Static default-observed rejection; runtime effect-lineage assertions | GREEN in stage |
| Hidden inclusion | `include-all` includes dot-prefixed names; `exclude-hidden` records without dispatch | Runtime `.hidden-map` inclusion | GREEN in stage |
| No symlink follow | Child `stat(..., follow_symlinks=False)` plus `symlink-recorded-never-followed` dispatch | Runtime directory-symlink classification and no-dispatch result | GREEN in stage |
| Explicit bounds | Positive entry/byte bounds, depth bound, and one-transition scheduler | Runtime partial-directory observation fails closed with `entry-bound-exceeded` | GREEN in stage |
| Same-descriptor freshness | File and directory pre/post use `fstat` on one opened descriptor occurrence; metadata/count/payload stability required | Static descriptor-source check plus successful runtime capture | GREEN in stage; cross-invocation descriptor linearity remains GAP |
| SHA seals/readback | Length-framed receipts, file revision digest, directory revision digest, transition digest | Runtime recomputation for file, directory, and every directory transition | GREEN in stage |
| Progress receipt | Directory transition seals scan identity, attempt, transition identity, from/to state, effect, and evidence class | Runtime identity and digest readback across every transition | GREEN in stage; external wire emission remains GAP |
| Lambda Blotto identity | Manifest states Lambda Blotto is discrete Colonel Blotto and delta is its operational semantics | Static semantic contract | GREEN as declared project semantics |
| FIB lineage | Observed, Predicted, Counterfactual, and Admitted are distinct; scheduler effects preserve the input class; only Observed can receive an observed seal | Runtime rejection of Predicted, Counterfactual, and Admitted requests without reclassification | GREEN in stage |
| Drill-down context | Map chain is extended at each child and bound into file and directory receipts | Runtime receipt contains map chain | GREEN in stage |
| Corpus routing | Source kind/family/identity plus claim, volume, chapter, appendix, and an immutable exact-occurrence tuple are typed provenance. Each occurrence binds exact source text, path, locus, revision, frame time, authority role/scope, resolution status, non-exclusivity, relation, evidence class, claim classification, support boundary, and target volume/chapter | Runtime file/directory receipts contain the exact Volume 30 statement, operator topology, Molt map statement, direct implementation witnesses, hardware/ISA/compiler/VM frames, typed discovery obligations, and non-collapse boundaries; static projection checks | GREEN in stage |
| Publication navigability | Every occurrence has exactly one coordinate frame binding volume, chapter, subsection, semantic drill-down, diagram caption/label route, citation key, occurrence-local source locus, header artifact, footer state, and readback artifact | Static total/unique ownership and route agreement checks; runtime receipt contains Phoenix/P34 diagram labels, footer GAP, and citation-resolution readback requirement | GREEN schema/source routing; rendered superscript citation, rendered footer, and P05 chapter-local diagram readbacks remain explicit GAPs |

## Phoenix/Disintegration routing ledger

The canonical staged route is `OUR ecosystem -> PHOENIX RUN [contains Molt D/R] -> Icarus -> Helios/GraphAtlas`. Molt is the disintegration/reassimilation mechanism inside the Phoenix Run. Icarus is the getting-to-the-sun vehicle—the custom VS Code/Protégé ecosystem integration and named reborn integration state, with Daedalus implicated. Helios/GraphAtlas is the mise-en-scène and accessible consolidated stage under construction. These are separate receipt relations, not synonyms.

| Occurrence | Exact locus and revision | Class | Routed use and boundary |
|---|---|---|---|
| Mythic-Phoenix equivalence | `src/papers/30_disintegration_reassimilation/chapters/09_mythic_phoenix_run/chapter.tex:10`, SHA-256 `5c1d2c025314077caad6ebf6f80ba550c90b8c02a7536cc4bd9f6072b42a569c` | Observed wording; declared synthesis | Routes to Volume 30 / Chapter 9. Exact occurrence is observed; equivalence is not mislabeled as proved implementation closure. |
| Canonical route prose | Same file, lines 20–25, same revision | Observed wording; declared synthesis | Preserves Phoenix Run as the middle node, Molt as mechanism, Icarus as vehicle/state, and Helios/GraphAtlas as stage. |
| Project-topology directive | Active 2026-07-19 crawler/routing supersession | Observed direct source | Binds the exact canonical route and the explicit non-collapse of Icarus versus the Helios/GraphAtlas mise-en-scène. |
| Verbatim operator ledger | `/data/src/capture/.maps/_DISCOVERY/LEDGER.md:10`, SHA-256 `72dc9ed477f4c3101795d32a9a07fb7c87fe6a0390044164dd4df3abca7bae3b` | Observed direct source | Names Phoenix across Telephone/Sparky with Icarus carrying Daedalus, making GraphAtlas in the Silmaril ecosystem, and Icarus enabling Helios launch. It does not claim launch occurred. |
| Molt/Phoenix doctrine map | `/data/src/capture/.maps/_DISCOVERY/DOCTRINE_TAG_PLAN9_HISTORY_HUB.md:113`, SHA-256 `d42d4ef2c79261d32e1bfa02524033e37298a2d2c27cb7902f9aca986efc4ed0` | Observed capture map | Preserves exact “molt IS the phoenix mechanic” wording, then drills into the LiveView. It remains a locator/synthesis map, not implementation authority. |
| Molt implementation | `/home/tristan/Desktop/platform/core/agents-phx-real/lib/silmaril_wire_web/live/molt_live.ex:73`, SHA-256 `0d4a41eed03e6cc31b6af34dcc65813a11e7cd20eab2f506718b6d110f3f31fd` | Observed direct source | Implements origin rewrite, namespace reissue, ancestry-hash conservation, and fresh-manifold language. It has no direct reference to the separate Phoenix run spine. |
| Phoenix run spine | `/home/tristan/Desktop/platform/core/agents/lib/research/render/phoenix/rebirth/run/spine.ex:10`, SHA-256 `e6cebd8c89f301e02b4767c8199dd6d93fc406d642d8b7d68fc95ab14678e720` | Observed direct source | Identifies the Phoenix rebirth PageData workflow and explicit-gap boundary. It does not name Molt, Icarus, Daedalus, or Helios. |
| Icarus/Daedalus artifact | `/home/tristan/Downloads/full/fuller/silmaril_kde_phase01_f15_capture_v1/data/src/README.md:12`, SHA-256 `6d3bdc298df91058499533f1c7c08afda875fbbc4c3cfd4d1ce86c740bf200af` | Observed direct source | States that Icarus is the platform and carries Daedalus. The artifact explicitly denies that the vehicle has flown or Helios launched. |
| Icarus→Helios rendition map | `/data/src/capture/.maps/_DISCOVERY/GREMLIN_KDE_INCORPORATION_SPEC.md:11`, SHA-256 `8576326a7e93452b20ace8bfd169e0320c07e6742075c40cb732ef761f6be9be` | Observed capture map | Records “Lite greenfield for ICARUS now → full sauce in HELIOS later” and remains `STAGED, NOT LAUNCHED` at line 50. |

## Open computing-substrate routing ledger

`federated-computing-substrate-routing.json` is an open-world ledger, not a closed hardware enum. Every resolved occurrence has its own frame time, authority scope, resolution status, and non-exclusivity boundary. `hardware_profile.html` is one local frame only, and its identifying serial, UUID, address, and device-identifier fields are excluded from routed text.

| Frame or obligation | Exact locus and revision | Class and authority boundary | State |
|---|---|---|---|
| Local Intel/firmware/AMD-GPU frame | `hardware_profile.html:47-57,237-252,323-336`, SHA-256 `4a59fefa9decf2f49c9cdbc66bc2166981c77ee0c1dad4d231d8c3ed1c343bd2` | Direct local observation only; neither UEFI/ISA authority nor ROCm execution proof | RESOLVED as one non-exclusive host frame |
| RISC-V/HIP/ROCm source-bundle map | `/data/src/capture/.gremlin-maps/r5-sources-a/README.md:7,22-26,40-52`, SHA-256 `c54d0f94d5c3e0e6ee563babec14c13de5e161b1fab6c7f511c8bacd56484a13` | Map authority for identity, provenance, and stated inspection depth; direct documents remain separate | RESOLVED to direct artifacts |
| RISC-V User ISA v2.1 | `.../sources/original/EECS-2016-118.pdf:1`, SHA-256 `2db2e845bbe36ca21141c9cc50ce32d54f1bd3ea8912d34415f6bc1f729d58a2` | Direct versioned ISA document; instruction/ABI/execution claims still require exact loci and receipts | RESOLVED document frame |
| AMD HIP guide | `.../sources/original/AMD_HIP_Programming_Guide.pdf:1`, SHA-256 `13cd0bec23dd6650eecfbb6bf660b254fbe44cead32a56e5bcb670afd0ec1ca0` | AMD vendor document; not local toolchain or kernel-execution proof | RESOLVED document frame |
| Triton MAPL 2019 | `.../compiler/triton/2019-mapl/source.pdf:1`, SHA-256 `7c4d200693c223c4d4c53c98b22c2693bdcf6adf3c902436b070368be097a7c1` | Primary historical compiler-design paper; not authority for current Triton | RESOLVED historical frame |
| Linux KVM | `.../virtualization/linux-kvm/source.pdf:1`, SHA-256 `5bbd6226d5919972e6be2816098c80dec163cf99847c1ed85daffc3d4e8173d9` | Primary historical design paper; not a current VM/deployment readback | RESOLVED historical frame |
| Cross-family lexical map | `/data/src/capture/.maps/scripts-contracts-morphisms-resource/README.md:108-113`, SHA-256 `154072b0c9a888c8803462b350fb3ebdd17a0e825bf830c288674209737fbf07` | Map authority for lexical routes and citation links only | RESOLVED locator frame |
| Intel generations beyond the supplied host | 2026-07-19 project discovery directive | Required scope, not observed artifact evidence | `Admitted` discovery GAP |
| AMD CPU generations | 2026-07-19 project discovery directive | Required scope; the AMD GPU and vendor guides do not substitute | `Admitted` discovery GAP |
| Other ISA systems and RISC-V hardware/psABI/runtime | 2026-07-19 project discovery directive | Required open branch beyond the v2.1 document | `Admitted` discovery GAP |
| Current CUDA/ROCm/Triton and further stacks | 2026-07-19 project discovery directive | Required open accelerator/compiler federation | Partially resolved; remaining rows are `Admitted` GAPs |
| UEFI and further firmware frames | 2026-07-19 project discovery directive | Required normative, implementation, virtual-firmware, and runtime branches | Partially resolved; remaining rows are `Admitted` GAPs |
| KVM/QEMU/Proxmox and further VM/hypervisor frames | 2026-07-19 project discovery directive | Required versioned design plus live configuration/readback branches | Partially resolved; remaining rows are `Admitted` GAPs |
| Networks, storage, operating environments | 2026-07-19 project discovery directive | Required independently observed frames | `Admitted` discovery GAP |
| Single-/multi-machine deployments | 2026-07-19 project discovery directive | Must preserve machine, guest, link, service, shard, storage, network, and observation coordinates | `Admitted` discovery GAP |
| Further computing substrates | 2026-07-19 project discovery directive | Permanent extension point; named seeds never close the enum | OPEN by law |

## Named gaps (not promoted to completion)

- Python does not expose a serializable kernel directory-snapshot token. `os.listdir` materializes a whole fresh name vector before projecting one ordinal. Same-descriptor metadata and count checks detect drift but do not prove an atomic directory snapshot.
- Descriptor occurrence linearity across independently hosted scheduler invocations is not proved by the Python type system.
- File capture is whole-payload bounded; it does not serialize an incremental SHA-256 state.
- Format evidence is request evidence, not content sniffing.
- Progress receipts create typed emission plans; no external Telephone wire emitter is bound here.
- Frontier recursion is deliberately external. The slice produces typed directory/file work and advances one selected work item per call; it has no global recursive cursor.
- Directory-child `lstat` metadata is not rebound as an equality precondition when separately scheduled file frontier work re-admits the child path. A replacement is captured as a fresh occurrence rather than proved identical to the parent-directory observation.
- There is no admitted interpreter launcher. Tests exercise the functions as a live-tree overlay, but promotion and launcher admission are separate gates.
- The multi-generation CPU, remaining ISA/system, current accelerator/compiler, firmware, VM/hypervisor, network/storage/OS, and single-/multi-machine deployment rows above remain required discovery work. Their typed presence is not resolution evidence.
- All seven unique routed citation keys resolve to current bibliography entries and occur in the target chapter sources, but this staged Python slice does not itself render the volumes or inspect a PDF superscript-number/footnote readback. That final rendered-citation artifact remains a GAP.

## Validation results for this frame

- Isolated stage: `python3 -B -m unittest discover -s tests -p 'test_*.py' -v` — 21/21 passed. This includes exact Phoenix and computing-substrate occurrence receipt readback, time/authority/resolution/non-exclusivity checks, publication-coordinate totality/navigation, and the ignored-aware zero-collision assertion against the current live tree.
- Live-tree overlay at `/tmp/lambda-blotto-pylib-routing-iYiAc5qZ`: 19 passed and 2 isolated-stage-only checks skipped intentionally after publication-coordinate v4 projection; zero failures.
- Overlay import sweep: all 29 operation `apply.py` modules imported, and every exported `apply` is callable.
- Scheduler signature readback: file, directory, and frontier-file transitions each expose one `Input` parameter and return one `Frame`.
- Python syntax: all 545 staged source files compiled in memory by the static contract verifier.
- Manifest JSON: `file-capture-manifest.json`, `phoenix-disintegration-routing.json`, and `federated-computing-substrate-routing.json` parsed successfully; every routed occurrence has every required field and globally unique key.
- Staged `__pycache__`: none.
- Real capture-root read: `/data/src/capture` completed with an accepted readback after 51 one-state transition receipts; all seven top-level children were recorded, including `.bsp`, `.gremlin-maps`, `.maps`, `.metals`, `.pdf-maps`, and `.scala-build` under `include-all`.

## Fail-closed promotion recipe

Do not promote while Telephone owns an active write path. Once the owner is quiescent:

1. Re-run the ignored-aware collision test in `tests/test_live_overlay_compatibility.py`; require zero exact relative-path overlaps.
2. Re-run `python3 -B -m unittest discover -s tests -p 'test_*.py' -v` from this staged root against the then-current live dependency surface.
3. Copy the staged root append-only with no-clobber semantics into `/data/src/scripts/pylib`, then verify every staged file exists at the destination with the same SHA-256. Any pre-existing or mismatched target is a hard stop, not a merge hint.
4. Run the same 21-test suite from the live root and import the file scheduler, directory scheduler, and frontier-file transition.
5. Only after those checks, bind a separately reviewed launcher or Telephone emitter. Neither is implicitly authorized by this append-only slice.

The corresponding copy source is exactly `.pylib-staging/scripts/python/pylib/`; no Volume 40 path and no existing Telephone file is part of the candidate set.
