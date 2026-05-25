#!/usr/bin/env python3
"""
Fix malformed wikilinks across the vault:

1. Bold in display: [[X|**Y**]] -> **[[X|Y]]**
2. Italic in display: [[X|*Y*]] -> *[[X|Y]]*
3. Underscore bold: [[X|__Y__]] -> __[[X|Y]]__
4. Strikethrough: [[X|~~Y~~]] -> ~~[[X|Y]]~~
5. Nested wikilinks: [[Thm - [[Thm - X|Y]]|Z]] -> [[Thm - X|Z]]
6. Inline code in display: [[X|`Y`]] -> `[[X|Y]]`
7. LaTeX in display: [[X|$Y$]] is reported but only mechanically fixable to
   the Unicode form when we know the substitution — left for manual review.

Run with --apply to apply changes.
"""
import os, re, sys, argparse

VAULT = "/home/user/Study-notes/Study notes"

def fix_text(text):
    n_fixed = 0
    # 1. Nested wikilinks: [[A [[B|C]] D|E]] or [[A [[B|C]] D]] -> [[B|E]] or [[B|D]]
    # Pattern: outer [[ ... [[ inner | inner_text ]] ... | outer_text ]]
    # We extract the inner target as the new target, and the outer display
    # text (after the last |) as the new display.
    nested_pattern = re.compile(
        r"\[\[(?P<pre>[^\]\[]*)"
        r"\[\[(?P<inner_target>[^\]\[|]+)(?:\|(?P<inner_disp>[^\]\[]+))?\]\]"
        r"(?P<post>[^\]\[]*)"
        r"(?:\|(?P<outer_disp>[^\]\[]+))?"
        r"\]\]"
    )

    def replace_nested(m):
        nonlocal n_fixed
        inner_target = m.group("inner_target")
        outer_disp = m.group("outer_disp")
        if outer_disp is not None:
            n_fixed += 1
            return f"[[{inner_target}|{outer_disp}]]"
        # No outer display; use inner display or inner target
        inner_disp = m.group("inner_disp")
        n_fixed += 1
        if inner_disp:
            return f"[[{inner_target}|{inner_disp}]]"
        return f"[[{inner_target}]]"

    # Apply nested fixes iteratively (in case of deeper nesting)
    for _ in range(5):
        new_text = nested_pattern.sub(replace_nested, text)
        if new_text == text:
            break
        text = new_text

    # 2. Formatting markers in display text
    # [[X|**Y**]] -> **[[X|Y]]**
    def fix_bold(m):
        nonlocal n_fixed
        target = m.group(1)
        inner = m.group(2)
        n_fixed += 1
        return f"**[[{target}|{inner}]]**"
    text = re.sub(r"\[\[([^\]\[|]+)\|\*\*([^*\]\[]+)\*\*\]\]", fix_bold, text)

    # [[X|__Y__]] -> __[[X|Y]]__
    def fix_under_bold(m):
        nonlocal n_fixed
        target = m.group(1)
        inner = m.group(2)
        n_fixed += 1
        return f"__[[{target}|{inner}]]__"
    text = re.sub(r"\[\[([^\]\[|]+)\|__([^_\]\[]+)__\]\]", fix_under_bold, text)

    # [[X|*Y*]] -> *[[X|Y]]*  (single asterisks; avoid * at the ends being shared)
    def fix_italic(m):
        nonlocal n_fixed
        target = m.group(1)
        inner = m.group(2)
        n_fixed += 1
        return f"*[[{target}|{inner}]]*"
    text = re.sub(r"\[\[([^\]\[|]+)\|\*([^*\]\[][^*\]\[]*)\*\]\]", fix_italic, text)

    # [[X|~~Y~~]] -> ~~[[X|Y]]~~
    def fix_strike(m):
        nonlocal n_fixed
        target = m.group(1)
        inner = m.group(2)
        n_fixed += 1
        return f"~~[[{target}|{inner}]]~~"
    text = re.sub(r"\[\[([^\]\[|]+)\|~~([^~\]\[]+)~~\]\]", fix_strike, text)

    # [[X|`Y`]] -> `[[X|Y]]`
    def fix_code(m):
        nonlocal n_fixed
        target = m.group(1)
        inner = m.group(2)
        n_fixed += 1
        return f"`[[{target}|{inner}]]`"
    text = re.sub(r"\[\[([^\]\[|]+)\|`([^`\]\[]+)`\]\]", fix_code, text)

    return text, n_fixed

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

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
                if args.apply:
                    with open(fp, "w", encoding="utf-8") as fd:
                        fd.write(new_text)
                print(f"  {fp.replace(VAULT + '/', '')}: {n} fixes")
    print(f"\n{'APPLIED' if args.apply else 'DRY RUN'}: {total} fixes across {files_changed} files")

if __name__ == "__main__":
    main()
