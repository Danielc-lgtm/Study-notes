#!/usr/bin/env python3
"""
Fix nested wikilinks `[[Thm - [[Thm - X|Y]]|Z]]` -> `[[Thm - X|Z]]`.

Walks the text, finds the outer `[[`, the inner `[[..]]`, the closing `]]`,
parses the inner target and the outer display, and writes back the
single-bracket-pair form.
"""
import os, re, sys

VAULT = "/home/user/Study-notes/Study notes"

def fix_text(text):
    out = []
    i = 0
    n = len(text)
    fixes = 0
    while i < n:
        if text[i:i+2] == "[[":
            # Find matching ]] (depth-aware)
            depth = 1
            j = i + 2
            while j < n - 1 and depth > 0:
                if text[j:j+2] == "[[":
                    depth += 1
                    j += 2
                elif text[j:j+2] == "]]":
                    depth -= 1
                    if depth == 0:
                        break
                    j += 2
                else:
                    j += 1
            if depth == 0:
                # Found outer wikilink from i to j+2
                content = text[i+2:j]  # what's between [[ and ]]
                # Look for inner [[...]] inside content
                inner_match = re.search(r"\[\[([^\]\[|]+)(?:\|[^\]\[]+)?\]\]", content)
                if inner_match:
                    inner_target = inner_match.group(1)
                    # Find the outer display: text after the inner ]] up to (and excluding)
                    # the final |outer_display
                    after_inner = content[inner_match.end():]
                    if "|" in after_inner:
                        outer_disp = after_inner.split("|", 1)[1]
                    else:
                        # No outer display; use the inner target as display
                        outer_disp = inner_target
                    out.append(f"[[{inner_target}|{outer_disp}]]")
                    i = j + 2
                    fixes += 1
                    continue
            # Otherwise, advance past [[
            out.append(text[i])
            i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out), fixes

def main():
    apply = "--apply" in sys.argv
    total = 0
    files_changed = 0
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as fd:
                text = fd.read()
            new_text, n = fix_text(text)
            if n > 0 and new_text != text:
                files_changed += 1
                total += n
                if apply:
                    with open(fp, "w", encoding="utf-8") as fd:
                        fd.write(new_text)
                print(f"  {fp.replace(VAULT + '/', '')}: {n} fixes")
    print(f"\n{'APPLIED' if apply else 'DRY RUN'}: {total} fixes across {files_changed} files")

if __name__ == "__main__":
    main()
