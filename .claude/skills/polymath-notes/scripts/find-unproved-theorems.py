#!/usr/bin/env python3
"""Find theorem pages that violate the vault's full-proof rule.

The rule (polymath-notes SKILL.md, "The Proof Standard"): every theorem,
lemma, proposition, and corollary that the vault states or invokes carries a
complete, self-contained proof on its own page. A page is a violation when

  1. its filename marks it as statement-only ("(Statement)");
  2. it has no "# Formal Proof" section, or that section is empty / too short
     to be a proof;
  3. its Formal Proof section admits it is not a proof ("sketch", "omitted",
     "beyond the scope", "we do not prove", "left to the reader", ...);
  4. a lemma callout inside the page lacks its nested "Full proof" callout.

It also reports every wikilink, anywhere in the scanned tree, whose target is
a "(Statement)"-only page, because invoking an unproved theorem is the same
violation from the other side.

Usage:
    python3 find-unproved-theorems.py [ROOT ...]     # default: "Study notes"
    python3 find-unproved-theorems.py --strict ...  # exit 1 on any finding

The scanner is conservative in one direction only: it never certifies a proof
as complete. A clean run means "no mechanical evidence of an unproved theorem",
not "every proof is rigorous"; the line-by-line P1 audit still has to be done.
"""

import os
import re
import sys

THEOREM_PREFIXES = ("Thm - ", "Lemma - ", "Prop - ", "Cor - ")
STATEMENT_MARK = "(Statement)"
MIN_PROOF_CHARS = 400

ADMISSION_PATTERNS = [
    r"\bproof sketch\b",
    r"\bsketch of (the )?proof\b",
    r"\bwe (only )?sketch\b",
    r"\bis sketched\b",
    r"\bproof (is )?omitted\b",
    r"\bomit the proof\b",
    r"\bwe do not prove\b",
    r"\bwe will not prove\b",
    r"\bnot proved here\b",
    r"\bbeyond (the )?scope\b",
    r"\bleft to the reader\b",
    r"\bleft as an exercise\b",
    r"\bwithout proof\b",
    r"\bsee \[[^\]]*\] for (a|the) proof\b",
    r"\bproof (can be )?found in\b",
    r"\bstandard result\b",
    r"\bwell[- ]known result\b",
    r"\bit is well known that\b",
]
ADMISSION_RE = re.compile("|".join(ADMISSION_PATTERNS), re.IGNORECASE)

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
LEMMA_CALLOUT_RE = re.compile(r"^> \[!\w+\]-\s*Lemma\b", re.IGNORECASE)
FULL_PROOF_RE = re.compile(r"^> > \[!\w+\]-\s*Full proof", re.IGNORECASE)
HEADER_RE = re.compile(r"^#{1,6}\s+(.*)$")


def strip_math_and_code(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    text = re.sub(r"\$[^$\n]*\$", " ", text)
    return text


def section(text, name):
    """Return the body of the level-1/2 section whose header is `name`."""
    lines = text.splitlines()
    out, inside = [], False
    for line in lines:
        m = HEADER_RE.match(line)
        if m:
            title = m.group(1).strip()
            if inside:
                break
            inside = title.lower() == name.lower()
            continue
        if inside:
            out.append(line)
    return "\n".join(out) if inside or out else None


def scan_theorem_page(path, text):
    findings = []
    base = os.path.basename(path)
    if STATEMENT_MARK in base:
        findings.append("statement-only page (no proof by construction)")
    proof = section(text, "Formal Proof")
    if proof is None:
        findings.append("no '# Formal Proof' section")
    else:
        body = strip_math_and_code(proof)
        if len(re.sub(r"\s+", "", body)) < MIN_PROOF_CHARS and len(re.sub(r"\s+", "", proof)) < 2 * MIN_PROOF_CHARS:
            findings.append("Formal Proof section is empty or far too short to be a proof")
        m = ADMISSION_RE.search(body)
        if m:
            findings.append(f"Formal Proof admits it is not a proof: '{m.group(0)}'")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if LEMMA_CALLOUT_RE.match(line):
            j = i + 1
            found = False
            while j < len(lines) and lines[j].startswith(">"):
                if FULL_PROOF_RE.match(lines[j]):
                    found = True
                    break
                j += 1
            if not found:
                findings.append(f"line {i + 1}: lemma callout without a nested 'Full proof' callout")
    return findings


def main(argv):
    strict = "--strict" in argv
    roots = [a for a in argv if not a.startswith("--")] or ["Study notes"]
    md_files = []
    for root in roots:
        for dirpath, _, files in os.walk(root):
            for f in files:
                if f.endswith(".md"):
                    md_files.append(os.path.join(dirpath, f))
    basenames = {os.path.splitext(os.path.basename(p))[0]: p for p in md_files}
    statement_pages = {b for b in basenames if STATEMENT_MARK in b}

    total = 0
    for path in sorted(md_files):
        base = os.path.basename(path)
        try:
            text = open(path, encoding="utf-8").read()
        except UnicodeDecodeError:
            text = open(path, encoding="utf-8", errors="replace").read()
        if base.startswith(THEOREM_PREFIXES):
            for f in scan_theorem_page(path, text):
                total += 1
                print(f"{path}: {f}")
        for m in WIKILINK_RE.finditer(strip_math_and_code(text)):
            target = m.group(1).strip()
            if target in statement_pages:
                total += 1
                print(f"{path}: links to statement-only page [[{target}]]")
    print(f"\n{total} finding(s) across {len(md_files)} files.")
    return 1 if (strict and total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
