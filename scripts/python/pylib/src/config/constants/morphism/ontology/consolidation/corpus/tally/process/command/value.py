VALUE = (
    "python3",
    "-c",
    r'''import sys

count = 0
for path in sys.stdin.read().splitlines():
    if open(path, encoding="utf-8").read().lstrip():
        count = count + 1
sys.stdout.write(str(count) + "\n")
''',
)
