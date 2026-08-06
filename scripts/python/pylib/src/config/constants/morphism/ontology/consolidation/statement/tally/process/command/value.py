VALUE = (
    "python3",
    "-c",
    r'''import sys

count = 0
for line in sys.stdin.read().splitlines():
    if line.rstrip().endswith((".", ";")) and not line.lstrip().startswith(("#", "@prefix")):
        count = count + 1
sys.stdout.write(str(count) + "\n")
''',
)
