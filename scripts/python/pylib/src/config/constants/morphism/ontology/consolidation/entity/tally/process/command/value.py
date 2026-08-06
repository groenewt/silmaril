VALUE = (
    "python3",
    "-c",
    r'''import re
import sys

matches = re.findall(r"\ba owl:NamedIndividual\b", sys.stdin.read())
sys.stdout.write(str(len(matches)) + "\n")
''',
)
