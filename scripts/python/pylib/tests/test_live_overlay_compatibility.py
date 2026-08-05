import ast
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGE_SRC = ROOT / "src"
LIVE_ROOT = Path("/data/src/scripts/pylib")
LIVE_SRC = LIVE_ROOT / "src"


def owned_python_paths() -> tuple[Path, ...]:
    manifest = json.loads((ROOT / "file-capture-manifest.json").read_text())
    rooted = tuple(
        path
        for relative in manifest["owned_source_roots"]
        for path in (STAGE_SRC / relative).rglob("*.py")
    )
    exact = tuple(STAGE_SRC / relative for relative in manifest["owned_source_files"])
    return tuple(sorted(set(rooted + exact)))


def module_candidates(root: Path, module: str) -> tuple[Path, Path]:
    relative = Path(*module.split("."))
    return root / relative.with_suffix(".py"), root / relative / "__init__.py"


def project_imports(path: Path) -> tuple[str, ...]:
    tree = ast.parse(path.read_bytes(), filename=str(path))
    return tuple(
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
        and node.level == 0
        and node.module is not None
        and node.module.split(".", 1)[0] in ("config", "silmaril")
    )


class LiveOverlayCompatibilityTest(unittest.TestCase):
    def test_stage_has_no_exact_live_path_collision(self):
        if (ROOT / "reference").exists():
            self.skipTest("collision is certified on the isolated stage before overlay")
        stage = {path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_file()}
        live = {path.relative_to(LIVE_ROOT) for path in LIVE_ROOT.rglob("*") if path.is_file()}
        self.assertEqual(stage & live, set())

    def test_every_project_import_resolves_in_stage_or_live_dependency_surface(self):
        unresolved = []
        for path in owned_python_paths():
            for module in project_imports(path):
                stage_candidates = module_candidates(STAGE_SRC, module)
                live_candidates = module_candidates(LIVE_SRC, module)
                if not any(candidate.is_file() for candidate in stage_candidates + live_candidates):
                    unresolved.append(f"{path.relative_to(ROOT)} -> {module}")
        self.assertEqual(unresolved, [])

    def test_isolated_stage_manifest_owns_every_python_source(self):
        if (ROOT / "reference").exists():
            self.skipTest("owned-source completeness is certified before overlay")
        self.assertEqual(set(owned_python_paths()), set(STAGE_SRC.rglob("*.py")))

    def test_shared_byte_vector_uses_telephone_project_gate(self):
        direct = []
        expected = "config.gate.external.project.sparky.substrate.byte.vector.library"
        for path in owned_python_paths():
            imports = project_imports(path)
            if "silmaril.sparky.lambda.substrate.byte.vector.value" in imports:
                direct.append(str(path.relative_to(ROOT)))
        self.assertEqual(direct, [])
        self.assertTrue(any(expected in path.read_text() for path in STAGE_SRC.rglob("*.py")))


if __name__ == "__main__":
    unittest.main()
