VALUE = (
    "python3",
    "-c",
    r'''import sys

count = open(sys.argv[1], encoding="utf-8").read().rstrip("\n")
declarations = open(sys.argv[2], encoding="utf-8").read()
sys.stdout.write("# Silmaril Consolidated Ontology\n")
sys.stdout.write("# Generated from " + count + " TTL files\n")
sys.stdout.write("# This file is machine-generated; edit the source files in basicttl/\n")
sys.stdout.write("\n")
sys.stdout.write(declarations)
sys.stdout.write(sys.stdin.read())
''',
)
