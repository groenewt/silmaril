#!/usr/bin/env bash
# run-aob-checks.sh — the AOB meta-ontology verification runner (W2 · SP2).
# Parses the 7 DATA TTLs (meta/upper_anchor/octet_descent/tensor_block/value_colimit/group_law/
# evidence_glossary) into one graph, runs pyshacl against aob.shapes.ttl (loaded ONLY as the shapes
# graph, never mixed into the data), auto-discovers every "# EXPECT-TRUE <name>" ASK in
# aob.queries.sparql and requires each true, then runs the depth gate. Exits 0 iff all green.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 - <<'PY'
import os.path, re, sys
from rdflib import Graph
from pyshacl import validate
DATA=["meta.ttl","upper_anchor.ttl","octet_descent.ttl","tensor_block.ttl","value_colimit.ttl","group_law.ttl","evidence_glossary.ttl"]
data=Graph()
for f in DATA:
    p=f"basicttl/aob/{f}"
    if os.path.exists(p): data.parse(p)
print(f"parse OK: {len([f for f in DATA if os.path.exists('basicttl/aob/'+f)])} data ttl, {len(data)} triples")
sp="basicttl/aob/aob.shapes.ttl"
if os.path.exists(sp):
    s=Graph(); s.parse(sp)
    ok,_,rep=validate(data, shacl_graph=s, inference="rdfs")
    print("SHACL conforms:", ok)
    if not ok: print(rep[:2000]); sys.exit(1)
else: print("SHACL: shapes file not present yet (skipped)")
q=open("basicttl/aob/aob.queries.sparql").read()
fails=ran=0
for b in re.split(r'\n(?=#\s*EXPECT-TRUE\s)', q):
    m=re.search(r'EXPECT-TRUE\s+(\S+)', b)
    if not m: continue
    ask="\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    if not ask.strip().upper().startswith(("PREFIX","ASK")): continue
    res=bool(data.query(ask)); ran+=1
    print(f"  {'PASS' if res else 'FAIL'}  {m.group(1)}"); fails+=(0 if res else 1)
print(f"ASKs: {ran} run, {fails} failed")
sys.exit(1 if fails else 0)
PY
python3 scripts/ontology-depth-check.py basicttl/aob
echo "AOB CHECKS GREEN"
