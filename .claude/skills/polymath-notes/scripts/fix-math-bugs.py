#!/usr/bin/env python3
"""
Fix $...$ math regions whose closing $ is preceded by whitespace.

The fix is to remove the trailing whitespace inside math: change `$X = $` to
`$X =$`. This is valid math (the trailing `=` is rendered fine) and lets the
following prose proceed. The same applies to other operator-then-whitespace
endings like `$X + $`, `$X \mapsto $`, etc.

Also fixes opening-dollar followed by whitespace: `$ X$` -> `$X$` (move the
content's leading whitespace out of math).

Skips: YAML frontmatter, $$...$$ display math, code fences, inline code.

Run with --apply to write changes.
"""
import os, re, sys, argparse

VAULT = "/home/user/Study-notes/Study notes"

def find_protected_regions(text):
    """Return list of (start, end) tuples of regions to skip."""
    protected = []
    # YAML frontmatter
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            protected.append((0, end + 5))
    # $$...$$ display math (paired)
    i = 0
    while i < len(text):
        j = text.find("$$", i)
        if j == -1:
            break
        k = text.find("$$", j + 2)
        if k == -1:
            break
        protected.append((j, k + 2))
        i = k + 2
    # ```...``` fenced code
    for m in re.finditer(r"```[\s\S]*?```", text):
        protected.append((m.start(), m.end()))
    # `inline code`
    for m in re.finditer(r"`[^`\n]*`", text):
        protected.append((m.start(), m.end()))
    protected.sort()
    return protected

def in_protected(pos, regions):
    for s, e in regions:
        if s <= pos < e:
            return True
        if s > pos:
            return False
    return False

def fix_text(text):
    """Return (new_text, num_fixes)."""
    protected = find_protected_regions(text)
    # Walk character by character, tracking math state per line.
    new_chars = []
    fixes = 0
    line_start = 0
    in_math = False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\n":
            # Reset math state at line breaks (we model line-bound math)
            in_math = False
            new_chars.append(ch)
            i += 1
            continue
        if in_protected(i, protected):
            new_chars.append(ch)
            i += 1
            continue
        if ch == "$":
            # Escaped?
            if i > 0 and text[i-1] == "\\":
                new_chars.append(ch)
                i += 1
                continue
            if not in_math:
                # Opening $. Eat following whitespace inside math?
                # Look at next char.
                j = i + 1
                if j < len(text) and text[j] in " \t":
                    # Find next $ on the line to confirm it's a math region
                    nl = text.find("\n", j)
                    if nl == -1:
                        nl = len(text)
                    close = text.find("$", j + 1)
                    if close != -1 and close < nl:
                        # This is broken open-ws math. Skip the leading whitespace.
                        new_chars.append("$")
                        # advance past leading whitespace
                        k = j
                        while k < len(text) and text[k] in " \t":
                            k += 1
                        i = k
                        in_math = True
                        fixes += 1
                        continue
                in_math = True
                new_chars.append(ch)
                i += 1
            else:
                # Closing $. If previous emitted char was whitespace inside math,
                # remove that whitespace.
                # Pop trailing whitespace from new_chars (only on the same logical
                # math region — but since math is line-bound, this is safe).
                popped = 0
                while new_chars and new_chars[-1] in " \t":
                    new_chars.pop()
                    popped += 1
                if popped > 0:
                    fixes += 1
                new_chars.append("$")
                in_math = False
                i += 1
        else:
            new_chars.append(ch)
            i += 1
    return "".join(new_chars), fixes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    total_fixes = 0
    files_changed = 0
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as fd:
                text = fd.read()
            new_text, fixes = fix_text(text)
            if fixes > 0:
                files_changed += 1
                total_fixes += fixes
                if args.apply and new_text != text:
                    with open(fp, "w", encoding="utf-8") as fd:
                        fd.write(new_text)
                print(f"  {fp.replace(VAULT + '/', '')}: {fixes} fixes")
    print(f"\n{'APPLIED' if args.apply else 'DRY RUN'}: {total_fixes} fixes across {files_changed} files")

if __name__ == "__main__":
    main()
