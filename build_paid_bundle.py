#!/usr/bin/env python3
"""Build the private AI Money Stack delivery ZIP."""

from __future__ import annotations

import shutil
import textwrap
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BUNDLE_DIR = ROOT / "paid_bundle"
ZIP_PATH = ROOT / "paid_bundle.zip"


PR_REVIEW_AGENT = r'''#!/usr/bin/env python3
"""Generate a deterministic PR review brief from a local git diff."""

from __future__ import annotations

import argparse
import subprocess


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, text=True, capture_output=True, check=True).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="HEAD~1")
    parser.add_argument("--head", default="HEAD")
    args = parser.parse_args()

    diff = run(["git", "diff", "--stat", f"{args.base}..{args.head}"])
    names = run(["git", "diff", "--name-only", f"{args.base}..{args.head}"])
    print("# PR Review Agent Lite")
    print()
    print("## Changed Files")
    for name in names.splitlines():
        print(f"- {name}")
    print()
    print("## Diff Stat")
    print("```")
    print(diff)
    print("```")
    print()
    print("## Deterministic Review Checklist")
    print("- Verify tests cover the changed behavior.")
    print("- Check public API, docs, and migration impact.")
    print("- Look for secret leakage, destructive commands, and unrelated churn.")
    print("- Confirm generated files are intentional.")


if __name__ == "__main__":
    main()
'''


IDEA_FORGE_HTML = r'''<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Idea Forge Local</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;margin:40px;max-width:860px;line-height:1.5}
textarea,input{width:100%;padding:10px;margin:8px 0;font:inherit}
button{padding:12px 18px;font-weight:700}
pre{background:#111;color:#eee;padding:16px;white-space:pre-wrap}
</style>
<h1>Idea Forge Local</h1>
<p>Paste a trend, a personal asset, and a constraint. Everything runs in this browser tab.</p>
<label>Trend pattern</label><textarea id="trend">AI agents fail at account-gated revenue, but can create local artifacts.</textarea>
<label>Your asset</label><textarea id="asset">Large Obsidian vault, GitHub account, local Python skills.</textarea>
<label>Constraint</label><textarea id="constraint">No cold outreach, no paid APIs, no new accounts.</textarea>
<button onclick="forge()">Generate hypotheses</button>
<pre id="out"></pre>
<script>
function forge(){
  const trend = document.getElementById('trend').value.trim();
  const asset = document.getElementById('asset').value.trim();
  const constraint = document.getElementById('constraint').value.trim();
  const routes = ['template pack','local CLI','paid checklist','micro-course','audit report'];
  document.getElementById('out').textContent = routes.map((route, i) =>
    `${i+1}. ${route}: Use "${asset}" to serve people facing "${trend}". Constraint: ${constraint}. First artifact: README + demo + checkout link.`
  ).join('\n\n');
}
forge();
</script>
</html>
'''


ENDPOINT_PACKET = """# Obsidian-to-Money Endpoint Packet

## Pattern Map

| Note Pattern | Product Endpoint | First Artifact |
|---|---|---|
| Repeated blocker notes | Checklist or audit report | Markdown report + examples |
| Working local scripts | CLI bundle | README + demo + sample output |
| Research sweeps | Paid brief | Ranked list + source links |
| Prompt workflows | Template pack | 5 templates + before/after examples |

## Rule

Do not count possible revenue as revenue. A path is live only after a buyer,
maintainer, or platform creates a real payment event.
"""


BOUNTY_CHECKLIST = """# Paid OSS Bounty Quality Checklist

Use this before writing code.

- Confirm the bounty is funded or escrowed on the platform.
- Confirm the upstream issue is open and maintainers are accepting work.
- Search for duplicate active PRs.
- Check the repo had a merge in the last 60 days.
- Avoid tasks requiring KYC, OAuth, hardware, private credentials, or social proof.
- Prefer small tests, docs, examples, reproducible bug fixes, and maintainer-friendly PRs.
- Submit one clear claim with validation evidence. Do not spam.
"""


LOCAL_LLM_QUICKSTART = """# Local LLM Quickstart

This is a written starter guide for running the bundle in a local-first setup.

## Minimal Setup

1. Install Python 3.10+.
2. Install GitHub CLI if you want to use `pr_review_agent_lite.py`.
3. Install Ollama only if you want to extend these tools with local LLM calls.

## Recommended Local Models

- Qwen2.5 7B/14B for Korean and English mixed documents.
- Llama 3.1 8B for general English notes.
- Gemma small models for quick local classification.

## Data Rule

Keep private company documents on the local machine. Do not paste confidential
documents into hosted SaaS tools unless your company has approved that workflow.

## First Demo

```bash
python3 tools/obsidian_revenue_scout.py --vault examples/fixture_vault --out examples/sample-output
```
"""


README = """# AI Money Stack Paid Bundle

Included:

- `tools/obsidian_revenue_scout.py` - local Obsidian revenue scoring CLI.
- `tools/pr_review_agent_lite.py` - deterministic PR review brief generator.
- `idea_forge_pwa/index.html` - browser-only idea remix tool.
- `docs/obsidian_to_money_endpoint_packet.md` - endpoint mapping reference.
- `docs/paid_oss_bounty_quality_checklist.md` - bounty filter checklist.
- `docs/local_llm_quickstart.md` - written local setup guide.
- `examples/` - fixture vault and generated sample outputs.
- `case-study/` - field notes from failed and live revenue attempts.

Personal use only. Do not resell or redistribute this ZIP.
"""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def copy_tree(src: Path, dest: Path) -> None:
    if src.exists():
        shutil.copytree(src, dest, dirs_exist_ok=True)


def build() -> None:
    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir()

    write_text(BUNDLE_DIR / "README.md", README)
    (BUNDLE_DIR / "tools").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "obsidian_revenue_scout.py", BUNDLE_DIR / "tools" / "obsidian_revenue_scout.py")
    write_text(BUNDLE_DIR / "tools" / "pr_review_agent_lite.py", PR_REVIEW_AGENT)
    write_text(BUNDLE_DIR / "idea_forge_pwa" / "index.html", IDEA_FORGE_HTML)
    write_text(BUNDLE_DIR / "docs" / "obsidian_to_money_endpoint_packet.md", ENDPOINT_PACKET)
    write_text(BUNDLE_DIR / "docs" / "paid_oss_bounty_quality_checklist.md", BOUNTY_CHECKLIST)
    write_text(BUNDLE_DIR / "docs" / "local_llm_quickstart.md", LOCAL_LLM_QUICKSTART)
    copy_tree(ROOT / "examples", BUNDLE_DIR / "examples")
    copy_tree(ROOT / "case-study", BUNDLE_DIR / "case-study")
    shutil.copy2(ROOT / "LICENSE", BUNDLE_DIR / "LICENSE")

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(BUNDLE_DIR.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(BUNDLE_DIR.parent))

    print(f"Bundle: {ZIP_PATH}")
    print(f"ZIP bytes: {ZIP_PATH.stat().st_size}")
    print(f"Files: {sum(1 for p in BUNDLE_DIR.rglob('*') if p.is_file())}")


if __name__ == "__main__":
    build()
