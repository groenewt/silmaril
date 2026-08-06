VALUE = (
    "python3",
    "-c",
    r'''import sys

safe = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.:-")
hexadecimal = set("0123456789abcdefABCDEF")
first = True
for path in sys.stdin.read().splitlines():
    content = open(path, encoding="utf-8").read()
    if not content.lstrip():
        continue
    kept = []
    for line in content.split("\n"):
        head = line.lstrip()
        if not head.startswith("@prefix") and not head.startswith("#"):
            kept.append(line)
    lines = []
    for line in kept:
        result = []
        i = 0
        n = len(line)
        quoted = False
        while i < n:
            character = line[i]
            if quoted:
                if character == "\\" and i + 1 < n:
                    result.append(line[i:i + 2])
                    i = i + 2
                    continue
                if character == '"':
                    quoted = False
                result.append(character)
                i = i + 1
            elif character == '"':
                quoted = True
                result.append(character)
                i = i + 1
            elif line.startswith("silm:", i) and (i == 0 or line[i - 1].isspace() or line[i - 1] in "(^"):
                j = i
                while j < n and not line[j].isspace():
                    j = j + 1
                token = line[i:j]
                encoded = []
                k = 0
                while k < len(token):
                    piece = token[k]
                    if piece == "%" and k + 2 < len(token) and token[k + 1] in hexadecimal and token[k + 2] in hexadecimal:
                        encoded.append(token[k:k + 3])
                        k = k + 3
                    elif piece in safe or ord(piece) > 127:
                        encoded.append(piece)
                        k = k + 1
                    else:
                        for byte in piece.encode("utf-8"):
                            encoded.append("%{:02X}".format(byte))
                        k = k + 1
                result.append("".join(encoded))
                i = j
            else:
                result.append(character)
                i = i + 1
        lines.append("".join(result))
    triples = "\n".join(lines)
    if not triples.lstrip():
        continue
    if not first:
        sys.stdout.write("\n")
    first = False
    sys.stdout.write("\n# Source: " + path + "\n" + triples)
''',
)
