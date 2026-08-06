VALUE = (
    "python3",
    "-c",
    r'''import json
import re
import sys

content = sys.stdin.buffer.read().decode("utf-8")
subjects = {}
for block in re.finditer(r"^(silm:\w+)\s+a\s+[^\n]*;\n(.*?)\s\.$", content, re.M | re.S):
    subject = block.group(1)
    body = block.group(2)
    properties = {}
    for entry in re.finditer(
            r'((?:silm|rdfs):\w+)\s+((?:"[^"]*"|silm:\w+)(?:\s*,\s*(?:"[^"]*"|silm:\w+))*)',
            body):
        predicate = entry.group(1)
        for quoted, reference in re.findall(r'"([^"]*)"|(silm:\w+)', entry.group(2)):
            properties.setdefault(predicate, []).append(quoted if quoted else reference)
    subjects[subject] = properties
keys = {}
identities = {}
for subject in subjects:
    if re.search("^" + re.escape(subject) + r"\s+a\s+[^\n]*silm:signingkey", content, re.M):
        keys[subject] = subjects[subject]
    if re.search("^" + re.escape(subject) + r"\s+a\s+[^\n]*silm:signingidentity", content, re.M):
        identities[subject] = subjects[subject]
if not keys:
    raise ValueError("no silm:signingkey individuals found in the trust model")
signer_of = {}
for identity in identities:
    for key_reference in identities[identity].get("silm:signsWith", []):
        if key_reference in signer_of and signer_of[key_reference] != identity:
            raise ValueError(key_reference + ": claimed by both " + signer_of[key_reference] + " and " + identity)
        signer_of[key_reference] = identity
def single(subject, properties, predicate):
    values = properties.get(predicate, [])
    if len(values) > 1:
        raise ValueError(subject + ": " + predicate + " must have exactly one value, found " + str(len(values)))
    return values[0] if values else ""
for subject in keys:
    properties = keys[subject]
    fingerprint = single(subject, properties, "silm:hasFingerprint")
    key_file = single(subject, properties, "silm:hasKeyFile")
    policy_reference = single(subject, properties, "silm:hasPolicyClass")
    if re.match(r"[0-9A-F]{40}$", fingerprint) is None:
        raise ValueError(subject + ": bad or missing fingerprint " + repr(fingerprint))
    if not key_file:
        raise ValueError(subject + ": missing silm:hasKeyFile")
    if not policy_reference.startswith("silm:trust_policy_"):
        raise ValueError(subject + ": bad or missing silm:hasPolicyClass " + repr(policy_reference))
    policy = policy_reference.removeprefix("silm:trust_policy_").replace("_", "-")
    identity = signer_of.get(subject)
    if identity is None:
        raise ValueError(subject + ": no silm:signingidentity signsWith this key")
    label = single(identity, subjects[identity], "rdfs:label")
    electronic_mail = single(identity, subjects[identity], "silm:hasEmail")
    if not label or not electronic_mail:
        raise ValueError(identity + ": missing rdfs:label or silm:hasEmail")
    row = json.dumps([fingerprint, policy, key_file, label, electronic_mail])
    sys.stdout.buffer.write(row.encode("utf-8") + b"\n")
''',
)
