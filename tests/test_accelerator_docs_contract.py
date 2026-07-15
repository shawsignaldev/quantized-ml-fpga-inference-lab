from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_accelerator_depth_docs_exist() -> None:
    for relative in [
        "docs/hardware-architecture.md",
        "docs/throughput-memory-model.md",
        "docs/verification-plan.md",
    ]:
        path = ROOT / relative
        assert path.exists(), f"missing {relative}"
        text = path.read_text(encoding="utf-8")
        assert len(text.split()) >= 130
        assert "##" in text

def test_readme_links_accelerator_depth_docs() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in [
        "docs/hardware-architecture.md",
        "docs/throughput-memory-model.md",
        "docs/verification-plan.md",
    ]:
        assert relative in readme
