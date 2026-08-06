VALUE = (
    "python3",
    "-c",
    r'''import pathlib
import sys

for path in sorted(pathlib.Path(".").rglob("*.ttl")):
    sys.stdout.write(str(path) + "\n")
''',
)
