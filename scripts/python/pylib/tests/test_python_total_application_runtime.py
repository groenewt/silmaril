import ast
import re
from pathlib import Path


ROOT = Path(__file__).parents[1]
SOURCE_ROOT = ROOT / "src"
PROJECT_PREFIXES = (
    "config.constants.",
    "config.gate.external.project.",
    "config.gate.external.python.morphism.",
    "silmaril.",
)
FORBIDDEN_APPLICATION_NAMES = {"APPLY", "PROJECT", "TRANSFORM", "apply", "project"}
SEMANTIC_CATEGORIES = {
    "digest": re.compile(r"Digest::|\.hexdigest\b"),
    "encoding": re.compile(r"(?:CSV|JSON)\.(?:generate|dump)|YAML\.dump"),
    "file_observation": re.compile(
        r"File\.(?:file\?|directory\?|exist\?|readable\?|symlink\?|read\b|binread\b)"
    ),
    "filtering": re.compile(r"\.(?:select|reject|filter|compact)\b"),
    "grouping": re.compile(r"\.(?:group_by|flat_map|flatten|each_slice|transpose)\b"),
    "normalization": re.compile(
        r"\.(?:strip|sub|gsub|delete_prefix|delete_suffix|downcase|upcase|to_i|to_s|cleanpath)\b|Integer\("
    ),
    "ordering": re.compile(r"\.(?:sort|sort_by)\b"),
    "parsing": re.compile(r"(?:CSV|JSON)\.(?:read|parse)|YAML\.(?:load|safe_load)"),
    "pathname_projection": re.compile(
        r"Pathname\.new|\.relative_path_from\b|\.(?:basename|dirname|extname)\b"
    ),
    "pattern": re.compile(r"\.match\?|=~|\.scan\b|\.split\b|\.each_line\b"),
    "process_dispatch": re.compile(r"Open3\.|IO\.popen|\bsystem\("),
    "uniqueness": re.compile(r"\.uniq\b"),
}


def test_every_python_source_file_is_one_total_application() -> None:
    paths = tuple(sorted(SOURCE_ROOT.rglob("*.py")))
    violations = []

    for path in paths:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        relative_path = path.relative_to(ROOT).as_posix()
        public_symbols = []
        imported_project_symbols = {}
        project_function_imports = set()

        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                if not node.name.startswith("_"):
                    public_symbols.append(node.name)
            elif isinstance(node, ast.Assign):
                public_symbols.extend(
                    target.id
                    for target in node.targets
                    if isinstance(target, ast.Name) and not target.id.startswith("_")
                )
            elif isinstance(node, ast.AnnAssign):
                if isinstance(node.target, ast.Name) and not node.target.id.startswith("_"):
                    public_symbols.append(node.target.id)
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    binding = alias.asname or alias.name.split(".")[0]
                    if (path.name == "library.py" or binding == "VALUE") and not binding.startswith("_"):
                        public_symbols.append(binding)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    binding = alias.asname or alias.name
                    if (path.name == "library.py" or binding == "VALUE") and not binding.startswith("_"):
                        public_symbols.append(binding)
                    if node.level or module.startswith(PROJECT_PREFIXES):
                        imported_project_symbols[binding] = module
                        if alias.name in FORBIDDEN_APPLICATION_NAMES or alias.name == "MAIN":
                            project_function_imports.add(binding)

        if path.name == "value.py":
            expected_symbols = {"VALUE"} if "VALUE" in public_symbols else {"Value"}
        elif path.name == "library.py":
            expected_symbols = {"DEPENDENCY"}
        elif path.name == "process.py":
            expected_symbols = {"MAIN"}
        else:
            expected_symbols = set()
            violations.append((relative_path, "unsupported_source_filename", path.name))

        if set(public_symbols) != expected_symbols or len(public_symbols) != 1:
            violations.append((relative_path, "public_semantic_surface", tuple(public_symbols)))

        functions = tuple(
            node
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        )
        if path.name == "process.py" and tuple(node.name for node in functions) != ("MAIN",):
            violations.append((relative_path, "runtime_function_surface", tuple(node.name for node in functions)))
        if path.name != "process.py" and functions:
            violations.append((relative_path, "non_runtime_function_surface", tuple(node.name for node in functions)))

        called_project_symbols = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in imported_project_symbols
        }
        if called_project_symbols:
            violations.append(
                (relative_path, "invoked_project_local_functions", tuple(sorted(called_project_symbols)))
            )
        if project_function_imports:
            violations.append(
                (relative_path, "project_local_function_imports", tuple(sorted(project_function_imports)))
            )

        if path.name == "process.py" and functions:
            external_applications = tuple(
                node
                for node in ast.walk(functions[0])
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "SUBPROCESS"
                and node.func.attr == "run"
            )
            if len(external_applications) > 1:
                violations.append(
                    (relative_path, "external_application_count", len(external_applications))
                )
            if not external_applications:
                direct_categories = set()
                for node in ast.walk(functions[0]):
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                        if (
                            isinstance(node.func.value, ast.Name)
                            and node.func.value.id == "_PATHLIB"
                            and node.func.attr == "Path"
                        ):
                            direct_categories.add("pathname_projection")
                        if node.func.attr == "read_bytes":
                            direct_categories.add("file_observation")
                        if node.func.attr in {"strip", "translate"}:
                            direct_categories.add("normalization")
                        if node.func.attr == "sub":
                            direct_categories.add("pattern")
                        if node.func.attr == "join":
                            direct_categories.add("grouping")
                        if node.func.attr in {"sha256", "digest"}:
                            direct_categories.add("digest")
                    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                        direct_categories.add("combination")
                    if isinstance(node, ast.Compare):
                        direct_categories.add("predicate")
                    if isinstance(node, ast.IfExp):
                        direct_categories.add("predicate")
                    if (
                        isinstance(node, ast.Subscript)
                        and not isinstance(node.slice, ast.Slice)
                    ):
                        direct_categories.add("selection")
                    if (
                        isinstance(node, ast.Subscript)
                        and isinstance(node.slice, ast.Slice)
                        and isinstance(node.slice.step, ast.UnaryOp)
                    ):
                        direct_categories.add("normalization")
                if len(direct_categories) > 1:
                    violations.append(
                        (
                            relative_path,
                            "multiple_direct_semantic_categories",
                            tuple(sorted(direct_categories)),
                        )
                    )

        forbidden_names = {
            node.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Name) and node.id in FORBIDDEN_APPLICATION_NAMES
        }
        forbidden_names.update(
            node.name
            for node in ast.walk(tree)
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name in FORBIDDEN_APPLICATION_NAMES
        )
        if forbidden_names:
            violations.append((relative_path, "forbidden_application_facade", tuple(sorted(forbidden_names))))

        if any(isinstance(node, (ast.Try, ast.TryStar)) for node in ast.walk(tree)):
            violations.append((relative_path, "caught_or_relabeled_error", "try"))
        if any(isinstance(node, ast.NamedExpr) for node in ast.walk(tree)):
            violations.append((relative_path, "hidden_walrus_pipeline", ":="))
        if any(
            isinstance(node, ast.Tuple)
            and any(isinstance(descendant, ast.Call) for descendant in ast.walk(node))
            for function in functions
            for node in ast.walk(function)
        ):
            violations.append((relative_path, "hidden_tuple_application_pipeline", "tuple_calls"))
        if any(
            isinstance(node, (ast.Import, ast.ImportFrom))
            and any(alias.name == "importlib" or alias.name.startswith("importlib.") for alias in node.names)
            for node in tree.body
        ):
            violations.append((relative_path, "dynamic_dispatch_import", "importlib"))

    command_paths = tuple(
        sorted(SOURCE_ROOT.glob("**/process/command/value.py"))
    )
    for path in command_paths:
        tree = ast.parse(path.read_bytes(), filename=str(path))
        relative_path = path.relative_to(ROOT).as_posix()
        bodies = []
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue
            if not any(isinstance(target, ast.Name) and target.id == "VALUE" for target in node.targets):
                continue
            if not isinstance(node.value, (ast.Tuple, ast.List)):
                continue
            elements = node.value.elts
            for index, element in enumerate(elements[:-1]):
                if not isinstance(element, ast.Constant) or element.value not in {"-c", "-e"}:
                    continue
                body = elements[index + 1]
                if isinstance(body, ast.Constant) and isinstance(body.value, str):
                    bodies.append(body.value)

        for body in bodies:
            categories = tuple(
                name
                for name, pattern in SEMANTIC_CATEGORIES.items()
                if pattern.search(body)
            )
            if "filtering" in categories and "file_observation" in categories:
                categories = tuple(
                    name for name in categories if name != "file_observation"
                )
            if len(categories) > 1:
                violations.append(
                    (relative_path, "multiple_child_semantic_categories", categories)
                )

    assert paths
    assert command_paths
    assert not tuple(SOURCE_ROOT.rglob("apply.py"))
    assert not tuple(SOURCE_ROOT.rglob("project.py"))
    assert not tuple(
        path
        for path in SOURCE_ROOT.rglob("library.py")
        if path.as_posix().endswith("morphism/codebase/volume/codec/library.py")
    )
    assert not violations, "\n" + "\n".join(
        " | ".join((path, kind, repr(detail)))
        for path, kind, detail in violations
    )
