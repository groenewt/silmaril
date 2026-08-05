VALUE = (
    "python3",
    "-c",
    r'''import json
import re
import sys

text = sys.stdin.read()
blocks = []
buffer = ""
quoted = False
previous = None
for character in text:
    if character == '"' and previous != "\\":
        quoted = not quoted
    if character == "." and not quoted:
        blocks.append(buffer)
        buffer = ""
    else:
        buffer += character
    previous = character
if re.search(r"\S", buffer):
    blocks.append(buffer)
for block in blocks:
    match = re.match(r"\A\s*silm:(\S+)\s+(.*?)\s*\Z", block, re.DOTALL)
    if match is None:
        continue
    subject = match.group(1)
    body = match.group(2)
    properties = []
    property_buffer = ""
    quoted = False
    previous = None
    for character in body:
        if character == '"' and previous != "\\":
            quoted = not quoted
        if character == ";" and not quoted:
            properties.append(property_buffer)
            property_buffer = ""
        else:
            property_buffer += character
        previous = character
    if re.search(r"\S", property_buffer):
        properties.append(property_buffer)
    for entry in properties:
        trimmed = re.match(r"\A\s*(.*?)\s*\Z", entry, re.DOTALL).group(1)
        sys.stdout.write(json.dumps([subject, trimmed], separators=(",", ":")) + "\n")
''',
)
