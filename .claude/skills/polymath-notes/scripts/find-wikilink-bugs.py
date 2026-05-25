#!/usr/bin/env python3
"""
Scan the vault for malformed wikilinks:
1. Markdown formatting markers inside display text: [[X|**Y**]], [[X|*Y*]],
   [[X|__Y__]], [[X|_Y_]], [[X|~~Y~~]], [[X|`Y`]]
2. Nested wikilinks: [[...[[...]]...]]
3. LaTeX inside display text: [[X|$Y$]]
4. HTML tags inside display text: [[X|<i>Y</i>]]
"""
import os, re, sys, argparse

VAULT = "/home/user/Study-notes/Study notes"

# Find all wikilinks (both [[X]] and [[X|Y]] and ![[X]] transclusions)
WIKILINK = re.compile(r"!?\[\[([^\]\[]+(?:\[\[[^\]\[]+\]\][^\]\[]*)*)\]\]")
# Simpler: find every [[...]] pair, including nested ones
ALL_BRACKETS = re.compile(r"\[\[([^\n]+?)\]\]")

def find_bugs():
    bugs = []
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as fd:
                text = fd.read()
            # Strip code regions (where `R[[X]]` might be in a code fence)
            # and math regions (where `[[X,Y]]` is a Lie bracket, not a
            # wikilink). LaTeX-in-display-text detection runs SEPARATELY
            # below on the original text — we do not strip math here.
            def blank(s):
                # Replace non-newline chars with spaces; preserve \n so line
                # numbering across stripped/orig stays in sync.
                return "".join(" " if c != "\n" else "\n" for c in s)
            stripped = re.sub(r"```[\s\S]*?```", lambda m: blank(m.group(0)), text)
            stripped = re.sub(r"`[^`\n]*`", lambda m: blank(m.group(0)), stripped)
            stripped = re.sub(r"\$\$[\s\S]*?\$\$", lambda m: blank(m.group(0)), stripped)
            stripped = re.sub(r"\$[^\$\n]+\$", lambda m: blank(m.group(0)), stripped)
            stripped_lines = stripped.split("\n")
            orig_lines = text.split("\n")
            for line_no, line in enumerate(stripped_lines, start=1):
                if "[[" not in line:
                    continue
                orig = orig_lines[line_no - 1]
                # Nested-wikilink detection on the stripped line (math removed)
                for m in re.finditer(r"\[\[(?:(?!\]\]).)*\[\[", line):
                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "nested",
                                 orig[m.start():min(len(orig), m.end()+50)]))
                # Walk genuine [[ ... ]] pairs on the stripped line, then use
                # the original line to inspect display text for LaTeX (which
                # was stripped from the stripped line).
                depth = 0
                start = None
                i = 0
                while i < len(line):
                    if line[i:i+2] == "[[":
                        if depth == 0:
                            start = i
                        depth += 1
                        i += 2
                    elif line[i:i+2] == "]]":
                        depth -= 1
                        if depth == 0 and start is not None:
                            # Use ORIGINAL line slice for display-text check
                            orig_content = orig[start+2:i]
                            if "|" in orig_content:
                                target, display = orig_content.split("|", 1)
                            else:
                                target, display = orig_content, ""
                            if display:
                                if re.search(r"\*\*[^*]+\*\*", display):
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "bold-in-display",
                                                 orig[start:i+2]))
                                elif re.search(r"(?<!\*)\*[^*\s][^*]*[^*\s]\*(?!\*)", display):
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "italic-in-display",
                                                 orig[start:i+2]))
                                if re.search(r"__[^_]+__", display):
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "underscore-bold",
                                                 orig[start:i+2]))
                                if re.search(r"~~[^~]+~~", display):
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "strikethrough",
                                                 orig[start:i+2]))
                                if "`" in display:
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "code-in-display",
                                                 orig[start:i+2]))
                                if "$" in display:
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "latex-in-display",
                                                 orig[start:i+2]))
                                if re.search(r"<[/]?[a-zA-Z]+[^>]*>", display):
                                    bugs.append((fp.replace(VAULT + "/", ""), line_no, "html-in-display",
                                                 orig[start:i+2]))
                            i += 2
                            start = None
                        else:
                            i += 2
                    else:
                        i += 1
    return bugs

def main():
    bugs = find_bugs()
    by_kind = {}
    for b in bugs:
        by_kind.setdefault(b[2], []).append(b)
    print(f"Total: {len(bugs)} bugs across {len({(b[0]) for b in bugs})} files\n")
    for kind, bs in sorted(by_kind.items()):
        print(f"=== {kind}: {len(bs)} ===")
        for fp, ln, _, ctx in bs[:30]:
            print(f"  {fp}:{ln}  {ctx[:120]}")
        if len(bs) > 30:
            print(f"  ... and {len(bs)-30} more")
        print()

if __name__ == "__main__":
    main()
