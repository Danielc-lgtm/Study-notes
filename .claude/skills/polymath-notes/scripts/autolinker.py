#!/usr/bin/env python3
"""
Auto-linker for the polymath-notes vault.

For each Def-/Thm- subpage in the vault, this script extracts a canonical
"term" (the part after the prefix, e.g. "Group" from "Def - Group.md"),
generates lowercase + plural variants, and scans every other .md page in
the vault for the FIRST unlinked occurrence of that term in body text,
wrapping it in a wikilink to the source page.

It carefully skips:
- YAML frontmatter
- Math regions: $...$, $$...$$
- Code regions: `...`, ```...```
- Existing wikilinks [[...]] and transclusions ![[...]]
- Markdown headers (lines starting with #)
- Section bodies titled "Unlocked by This", "Sources and Targets",
  "Bridges", "Insights" where the page intentionally uses bold plain text
  for forward references
- Words inside other words (boundary check)

It only inserts a wikilink at the FIRST body-text occurrence per file
(to avoid clutter); subsequent occurrences are left alone.

The script is run with --dry-run to produce a report first, then with
--apply to write changes. Pass --limit N to apply at most N changes for
testing.
"""
import os, re, sys, argparse
from collections import defaultdict

VAULT = "/home/user/Study-notes/Study notes"

# Phrases that are too generic to safely link
BLOCKLIST_TERMS = {
    "the definition", "definition", "theorem", "exercise", "example",
    "examples", "section", "chapter", "lemma", "corollary", "remark",
    "proof", "field", "set", "function", "map", "space", "form",
    "norm", "constant", "value", "point", "line", "plane", "curve",
    "circle", "sphere", "edge", "vertex", "face", "graph",
    "the differential", "exterior", "interior", "support",
    "kernel", "image", "rank", "trace", "traces", "determinant",
    "tensor", "vector", "scalar", "object", "morphism", "category",
    "identity", "inverse", "composition", "order", "degree",
    "frame", "basis", "coordinate", "coordinates", "chart",
    "atlas", "neighborhood", "neighbourhood",
    "operation", "element", "group action",
    "isomorphism", "homomorphism",
    "one", "two", "three", "first", "second", "third",
    "integer", "integers", "natural", "natural number",
    "rational", "real", "complex", "number",
    "open", "closed", "compact", "complete", "smooth", "continuous",
    "differentiable", "bounded", "convex",
    # Common verbs/short nouns that double as math terms
    "normaliser", "normalisers", "normalizer", "normalizers",
    "center", "centre", "centres", "centers",
    "stabiliser", "stabilizer", "stabilisers", "stabilizers",
    "centralizer", "centraliser",
    "the integral", "the integrals", "integral", "integrals",  # too generic
    "the trace", "the traces",
    # Single very-common short technical words
    "torus", "torsion", "the", "and", "but", "with",
    "sequence", "sequences", "series", "limit", "limits",
    "convergence", "convergent", "divergent",
    # Likely English-word collisions
    "induction", "deduction", "structure", "structures",
    "transform", "transforms", "transformation", "transformations",
    "system", "systems", "boundary", "boundaries",
    "section", "sections", "extension", "extensions",
    "the closure", "closure", "closures",
    "the derivative", "derivative", "derivatives",
    "tangent", "tangents", "the differential",
    # Highly ambiguous English/math collisions
    "field", "fields",  # "vector field", "gauge field" dominate over the algebraic Field
    "independence",  # "coordinate-independence", "path-independence" dominate
    "primitive", "primitives",  # primitive root / ideal / element / permutation dominate
}

# Def filenames whose target is dangerous to auto-link (too many false positives
# across the vault — link these manually only)
BLOCKLIST_TARGETS = {
    "Def - Field",
    "Def - Independence",
    "Def - Primitive (Antiderivative)",
}


# Section headers under which we should not insert new links
# (these intentionally use bold plain text or are reference-only)
SKIP_SECTIONS = {
    "notation", "notation registry", "unlocked by this", "unlocked",
    "sources and targets", "bridges", "insights", "calibration check",
    "true name", "relate to other fields",
}

def extract_term_from_filename(fname):
    """Extract the natural-language term from a Def-/Thm- filename."""
    name = fname[:-3]  # strip .md
    for prefix in ("Def - ", "Thm - "):
        if name.startswith(prefix):
            term = name[len(prefix):]
            # Skip terms with parenthetical disambiguators for matching
            # (we still want to link to them but use the core part for matching)
            core = re.sub(r"\s*\([^)]*\)\s*", " ", term).strip()
            return name, term, core
    return None

def generate_variants(core_term):
    """Generate matching variants for a term."""
    variants = set()
    t = core_term.strip()
    if not t:
        return variants
    variants.add(t)
    # Lowercase first letter
    if t[0].isupper():
        variants.add(t[0].lower() + t[1:])
    # Strip leading "The "
    if t.startswith("The "):
        variants.add(t[4:])
        if t[4].isupper():
            variants.add(t[4].lower() + t[5:])
    elif t.startswith("the "):
        variants.add(t[4:])
    # Simple plural: add 's' if doesn't end in s
    base_variants = list(variants)
    for v in base_variants:
        if v.endswith("y") and len(v) > 1 and v[-2] not in "aeiou":
            variants.add(v[:-1] + "ies")
        elif not v.endswith(("s", "x", "z", "ch", "sh")):
            variants.add(v + "s")
        elif v.endswith("us") and len(v) > 2:
            variants.add(v[:-2] + "i")
        elif v.endswith("ex"):
            variants.add(v[:-2] + "ices")
    # Filter out blocklisted
    variants = {v for v in variants
                if v.lower() not in BLOCKLIST_TERMS and len(v) >= 4}
    return variants

def strip_protected_regions(text):
    """Return text with protected regions replaced by spaces (preserving length).

    Protected: YAML frontmatter, $...$, $$...$$, `...`, ```...```, [[...]], ![[...]], #-headers.
    """
    out = list(text)
    n = len(text)

    def blank(start, end):
        for i in range(start, min(end, n)):
            if out[i] != '\n':
                out[i] = ' '

    # YAML frontmatter (--- at start)
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            blank(0, end + 5)

    # $$...$$ display math
    for m in re.finditer(r"\$\$[\s\S]*?\$\$", text):
        blank(m.start(), m.end())

    # $...$ inline math
    for m in re.finditer(r"\$[^\$\n]*\$", text):
        blank(m.start(), m.end())

    # ``` code blocks
    for m in re.finditer(r"```[\s\S]*?```", text):
        blank(m.start(), m.end())

    # `code` inline
    for m in re.finditer(r"`[^`\n]*`", text):
        blank(m.start(), m.end())

    # Existing wikilinks and transclusions
    for m in re.finditer(r"!?\[\[[^\]\[]+\]\]", text):
        blank(m.start(), m.end())

    # Headers (entire line)
    for m in re.finditer(r"^#+[^\n]*$", text, re.MULTILINE):
        blank(m.start(), m.end())

    return "".join(out)

def find_skip_section_ranges(text):
    """Find character ranges inside sections we should not edit."""
    ranges = []
    header_re = re.compile(r"^(#+)\s+([^\n]+)$", re.MULTILINE)
    headers = [(m.start(), m.end(), len(m.group(1)), m.group(2).strip().lower())
               for m in header_re.finditer(text)]
    for i, (s, e, lvl, title) in enumerate(headers):
        title_clean = re.sub(r'[^a-z ]', '', title).strip()
        # Match "# Unlocked by This", "# Bridges", etc.
        if any(skip in title_clean for skip in SKIP_SECTIONS):
            # Find next header at same or higher level
            section_end = len(text)
            for s2, e2, lvl2, _ in headers[i+1:]:
                if lvl2 <= lvl:
                    section_end = s2
                    break
            ranges.append((e, section_end))
    return ranges

def find_first_match(masked_text, raw_text, variants, skip_ranges, self_term):
    """Find the first non-overlapping body-text match of any variant."""
    best = None
    for v in variants:
        # Use word-boundary regex; case-sensitive for capitalized terms
        # to avoid false positives (don't link "field" in random English)
        if v[0].isupper():
            pat = re.compile(r"\b" + re.escape(v) + r"\b")
        else:
            # Lowercase variants: skip - too risky
            continue
        for m in pat.finditer(masked_text):
            s, e = m.span()
            # Verify the masked text actually has the term (not blanked out)
            if masked_text[s:e] != v:
                continue
            # Skip if in a skip-section
            if any(sr_s <= s < sr_e for sr_s, sr_e in skip_ranges):
                continue
            # Skip if matched text equals self_term
            if v == self_term:
                continue
            if best is None or s < best[0]:
                best = (s, e, v)
                break
    return best

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--report", default="/tmp/autolink-report.txt")
    parser.add_argument("--max-per-file", type=int, default=15,
                        help="Max links to add per file")
    args = parser.parse_args()

    # Index all subpages
    all_pages = []
    target_index = {}  # variant -> (filename_stem, term)
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not f.endswith(".md"):
                continue
            all_pages.append(os.path.join(root, f))
            ext = extract_term_from_filename(f)
            if ext is None:
                continue
            stem, term, core = ext
            if stem in BLOCKLIST_TARGETS:
                continue
            variants = generate_variants(core)
            for v in variants:
                # Prefer longer (more specific) targets when conflict
                if v in target_index:
                    existing_term = target_index[v][1]
                    if len(core) <= len(existing_term):
                        continue
                target_index[v] = (stem, core)

    print(f"Indexed {len(target_index)} unique variants pointing to {len({t[0] for t in target_index.values()})} targets")
    print(f"Scanning {len(all_pages)} pages...")

    # Sort variants longest-first so multi-word matches win
    sorted_variants = sorted(target_index.keys(), key=lambda v: -len(v))

    total_changes = 0
    pages_changed = 0
    report = []

    for fp in all_pages:
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception:
            continue

        # Determine this file's self-term (don't link to self)
        bn = os.path.basename(fp)
        ext = extract_term_from_filename(bn)
        self_term = ext[1] if ext else None
        self_core = ext[2] if ext else None

        masked = strip_protected_regions(text)
        skip_ranges = find_skip_section_ranges(text)

        # Find all candidate matches (longest-first), greedy first-match per target
        used_targets = set()
        replacements = []  # (start, end, replacement_text)
        used_positions = []  # spans already taken

        for v in sorted_variants:
            target_stem, target_core = target_index[v]
            if target_stem in used_targets:
                continue
            # Skip self-linking
            if self_core and target_core == self_core:
                continue
            pat = re.compile(r"\b" + re.escape(v) + r"\b")
            for m in pat.finditer(masked):
                s, e = m.span()
                if masked[s:e] != v:
                    continue
                if any(sr_s <= s < sr_e for sr_s, sr_e in skip_ranges):
                    continue
                # Check overlap with prior replacements
                if any(not (e <= ps or s >= pe) for ps, pe in used_positions):
                    continue
                # Add a wikilink at this position
                original_word = text[s:e]
                if original_word == target_stem.split(' - ', 1)[-1].split(' (')[0]:
                    # Display can just be the target
                    new_link = f"[[{target_stem}|{original_word}]]"
                else:
                    new_link = f"[[{target_stem}|{original_word}]]"
                replacements.append((s, e, new_link))
                used_positions.append((s, e))
                used_targets.add(target_stem)
                break  # one match per target per file

            if len(replacements) >= args.max_per_file:
                break

        if not replacements:
            continue

        # Apply replacements in reverse order
        replacements.sort(key=lambda r: -r[0])
        new_text = text
        for s, e, new in replacements:
            new_text = new_text[:s] + new + new_text[e:]

        rel = fp.replace(VAULT + "/", "")
        report.append(f"\n=== {rel} ({len(replacements)} links) ===")
        for s, e, new in sorted(replacements, key=lambda r: r[0]):
            orig = text[s:e]
            ctx_s = max(0, s - 40)
            ctx_e = min(len(text), e + 40)
            ctx = text[ctx_s:ctx_e].replace("\n", " ")
            report.append(f"  '{orig}' -> {new}")
            report.append(f"     ctx: ...{ctx}...")

        total_changes += len(replacements)
        pages_changed += 1

        if args.apply:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_text)

        if args.limit and total_changes >= args.limit:
            break

    with open(args.report, 'w', encoding='utf-8') as f:
        f.write(f"Total links proposed: {total_changes} across {pages_changed} pages\n")
        f.write("\n".join(report))

    print(f"\n{'APPLIED' if args.apply else 'DRY RUN'}: {total_changes} links across {pages_changed} pages")
    print(f"Report: {args.report}")

if __name__ == "__main__":
    main()
