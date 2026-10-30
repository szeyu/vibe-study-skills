#!/usr/bin/env python3
"""Check Obsidian study notes in a folder. Standard library only.

Checks: frontmatter, wikilinks and embeds (resolved like Obsidian: relative,
vault-root, or unique basename), folded question/answer callouts, paragraphs
longer than N sentences, Mermaid reserved-word names, and Mermaid rendering
through `mmdc` when it is installed.

Usage:
    python3 check_notes.py <folder> [--no-mermaid] [--max-sentences 3]
Env:
    MMDC_PUPPETEER_CONFIG  optional puppeteer config file passed to mmdc (-p)
Exit code 1 when any issue is found.
"""
import argparse
import collections
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FENCE = re.compile(r"^[ \t>]*```.*?^[ \t>]*```", re.S | re.M)
MERMAID = re.compile(r"^([ \t>]*)```mermaid\n(.*?)^[ \t>]*```", re.S | re.M)
LINK = re.compile(r"!?\[\[([^\]|#^]+)")
RESERVED = re.compile(r"^\s*(participant|actor)\s+(end|opt|alt|loop|par|off)\b", re.I | re.M)


def vault_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / ".obsidian").is_dir() or (p / ".git").exists():
            return p
    return start


def index_names(vault: Path):
    names = collections.defaultdict(list)
    for p in vault.rglob("*"):
        if any(part.startswith(".") for part in p.relative_to(vault).parts):
            continue
        names[p.name].append(p)
        if p.suffix == ".md":
            names[p.stem].append(p)
    return names


def resolves(target: str, note: Path, vault: Path, names) -> bool:
    for base in (note.parent, vault):
        if (base / target).exists() or (base / (target + ".md")).exists():
            return True
    return len(names.get(Path(target).name, [])) == 1  # Obsidian's unique-basename lookup


def check_note(f: Path, root: Path, vault: Path, names, max_sent: int):
    text = f.read_text(encoding="utf-8")
    rel = f.relative_to(root)
    issues = []
    if not text.startswith("---\n"):
        issues.append(f"{rel}: no frontmatter")
    body = FENCE.sub("", text)
    no_code = re.sub(r"`[^`\n]+`", "", body)  # skip example syntax in inline code
    for raw in LINK.findall(no_code):
        target = raw.strip().rstrip("\\")
        if target and not resolves(target, f, vault, names):
            issues.append(f"{rel}: broken link [[{raw}]]")
    if re.search(r"\[!(question|success|answer)\][+-]", FENCE.sub("", no_code), re.I):
        issues.append(f"{rel}: folded question/answer callout (answers should be visible)")
    for para in re.split(r"\n\s*\n", body):
        s = para.lstrip()
        if not s or s.startswith(("|", "-", "*", ">", "#", "!", "$", "<", "```")) or re.match(r"\d+\.", s):
            continue
        n = len(re.findall(r"[.!?](?:\s|$)", s))
        if n > max_sent:
            issues.append(f"{rel}: paragraph has {n} sentences: {s[:60]!r}")
    for i, (_, block) in enumerate(MERMAID.findall(text)):
        m = RESERVED.search(block)
        if m:
            issues.append(f"{rel}: mermaid #{i} uses reserved word as a name: {m.group(0).strip()!r}")
    return issues, text


def render_mermaid(rel, text, mmdc, cfg):
    issues = []
    for i, (prefix, block) in enumerate(MERMAID.findall(text)):
        if prefix.strip():  # inside a callout: strip the "> " prefixes
            block = "\n".join(re.sub(r"^[ \t]*(>[ \t]?)+", "", ln) for ln in block.splitlines())
        with tempfile.TemporaryDirectory() as d:
            src, out = Path(d, "a.mmd"), Path(d, "a.svg")
            src.write_text(block, encoding="utf-8")
            cmd = [mmdc, "-i", str(src), "-o", str(out), "-q"] + (["-p", cfg] if cfg else [])
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode and re.search(r"Could not find (Chrome|browser)|Failed to launch", r.stderr + r.stdout):
                raise RuntimeError("mmdc could not start a browser; set MMDC_PUPPETEER_CONFIG to a config with executablePath")
            if r.returncode:
                first = (r.stderr or r.stdout).strip().splitlines()[:2]
                issues.append(f"{rel}: mermaid #{i} failed to render: {' | '.join(first)}")
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--no-mermaid", action="store_true", help="skip Mermaid rendering")
    ap.add_argument("--max-sentences", type=int, default=3)
    a = ap.parse_args()

    root = Path(a.folder).resolve()
    vault = vault_root(root)
    names = index_names(vault)
    mmdc = None if a.no_mermaid else shutil.which("mmdc")
    cfg = os.environ.get("MMDC_PUPPETEER_CONFIG")

    notes = sorted(root.rglob("*.md")) if root.is_dir() else [root]
    root = root if root.is_dir() else root.parent
    issues, blocks, no_browser = [], 0, ""
    for f in notes:
        found, text = check_note(f, root, vault, names, a.max_sentences)
        issues += found
        blocks += len(MERMAID.findall(text))
        if mmdc:
            try:
                issues += render_mermaid(f.relative_to(root), text, mmdc, cfg)
            except RuntimeError as e:
                mmdc, no_browser = None, str(e)

    print("\n".join(issues))
    if a.no_mermaid:
        mm = "Mermaid rendering skipped (--no-mermaid)"
    elif no_browser:
        mm = f"Mermaid: NOT rendered - {no_browser}"
    elif mmdc:
        mm = f"Mermaid: {blocks} blocks rendered with mmdc"
    else:
        mm = f"Mermaid: NOT rendered ({blocks} blocks) - install @mermaid-js/mermaid-cli for mmdc"
    print(f"{len(notes)} notes, vault root {vault}\n{mm}\nissues: {len(issues)}")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
