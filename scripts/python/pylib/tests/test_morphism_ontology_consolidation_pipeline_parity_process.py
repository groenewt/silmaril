import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]
REPOSITORY = Path(__file__).parents[4]
CORPUS = REPOSITORY / "basicttl"
FAMILY = "silmaril.sparky.morphism.ontology.consolidation"
ENVIRONMENT = {
    **os.environ,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(ROOT / "src"),
}


def _stage(edge: str, arguments: tuple[str, ...], stdin: bytes) -> bytes:
    completed = subprocess.run(
        (sys.executable, "-m", FAMILY + "." + edge + ".process", *arguments),
        capture_output=True,
        check=False,
        env=ENVIRONMENT,
        input=stdin,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stderr == b""
    return completed.stdout


def test_pipeline_reproduces_all_five_committed_ontology_documents(
    tmp_path: Path,
) -> None:
    source_paths = _stage("source.discovery", (str(CORPUS),), b"")
    declarations = _stage("namespace.union.projection", (str(CORPUS),), source_paths)
    corpus_tally = _stage("corpus.tally", (str(CORPUS),), source_paths)
    blocks = _stage("document.normalization", (str(CORPUS),), source_paths)

    corpus_tally_artifact = tmp_path / "corpus-tally"
    corpus_tally_artifact.write_bytes(corpus_tally)
    declarations_artifact = tmp_path / "namespace-declarations"
    declarations_artifact.write_bytes(declarations)

    consolidated = _stage(
        "consolidated.render",
        (str(corpus_tally_artifact), str(declarations_artifact)),
        blocks,
    )
    assert consolidated == (REPOSITORY / "ontology/silmaril-consolidated.ttl").read_bytes()

    shapes = _stage("shapes.constraint.language.document.render", (), declarations)
    assert shapes == (REPOSITORY / "ontology/shapes.ttl").read_bytes()

    queries = _stage("query.protocol.language.document.emission", (), b"")
    assert queries == (REPOSITORY / "ontology/queries.sparql").read_bytes()

    geographic = _stage(
        "geographic.query.protocol.language.document.emission", (), b""
    )
    assert geographic == (REPOSITORY / "ontology/geosparql.sparql").read_bytes()

    statement_tally_artifact = tmp_path / "statement-tally"
    statement_tally_artifact.write_bytes(_stage("statement.tally", (), consolidated))
    entity_tally_artifact = tmp_path / "entity-tally"
    entity_tally_artifact.write_bytes(_stage("entity.tally", (), consolidated))

    manifest = _stage(
        "manifest.render",
        (
            str(corpus_tally_artifact),
            str(statement_tally_artifact),
            str(entity_tally_artifact),
        ),
        b"",
    )
    assert manifest == (REPOSITORY / "ontology/manifest.ttl").read_bytes()
