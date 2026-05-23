#!/usr/bin/env python3
"""
Find $...$ math regions that violate the KaTeX/Pandoc rule:
- the character immediately AFTER an opening $ must not be whitespace
- the character immediately BEFORE a closing $ must not be whitespace

Walks each line, alternating open/close state across $ characters.
Skips $$...$$ display math (delimited by paired $$), code fences,
inline code, and YAML frontmatter.
"""
import os, re, sys

VAULT = "/home/user/Study-notes/Study notes"

def blank_region(s, start, end):
    """Replace text between [start, end) with spaces (preserve newlines)."""
    return s[:start] + "".join(' ' if c != '\n' else '\n' for c in s[start:end]) + s[end:]

def preprocess(text):
    """Blank out YAML frontmatter, $$...$$ display math, fenced code, inline code."""
    # YAML frontmatter
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            text = blank_region(text, 0, end + 5)
    # Display math $$...$$ — must come before $...$ scan
    text2 = []
    i = 0
    while i < len(text):
        if text[i:i+2] == "$$":
            close = text.find("$$", i + 2)
            if close == -1:
                text2.append(text[i:])
                break
            for c in text[i:close+2]:
                text2.append(' ' if c != '\n' else '\n')
            i = close + 2
        else:
            text2.append(text[i])
            i += 1
    text = "".join(text2)
    # Fenced code ```...```
    for m in list(re.finditer(r"```[\s\S]*?```", text)):
        text = blank_region(text, m.start(), m.end())
    # Inline code `...`
    for m in list(re.finditer(r"`[^`\n]*`", text)):
        text = blank_region(text, m.start(), m.end())
    return text

def find_dollar_bugs(text):
    """Return list of (line_no, col, kind, context_snippet)."""
    bugs = []
    lines = text.split("\n")
    for ln, line in enumerate(lines, start=1):
        # Walk $ characters, alternating state
        in_math = False
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "$":
                # Check for escaped $: prev char is backslash
                if i > 0 and line[i-1] == "\\":
                    i += 1
                    continue
                if not in_math:
                    # Opening dollar — must be followed by non-whitespace
                    nxt = line[i+1] if i+1 < len(line) else "\n"
                    if nxt in " \t\n":
                        # Could be a stray $ — flag as suspect open
                        # But only if there's a corresponding $ later
                        if "$" in line[i+1:]:
                            ctx = line[max(0, i-30):min(len(line), i+50)]
                            bugs.append((ln, i, "open-ws", ctx))
                    in_math = True
                else:
                    # Closing dollar — must be preceded by non-whitespace
                    prv = line[i-1] if i > 0 else "\n"
                    if prv in " \t":
                        ctx = line[max(0, i-50):min(len(line), i+30)]
                        bugs.append((ln, i, "close-ws", ctx))
                    in_math = False
                i += 1
            else:
                i += 1
    return bugs

def main():
    total = 0
    by_file = {}
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as fd:
                text = fd.read()
            cleaned = preprocess(text)
            bugs = find_dollar_bugs(cleaned)
            if bugs:
                by_file[fp.replace(VAULT + "/", "")] = bugs
                total += len(bugs)
    print(f"Found {total} dollar-sign bugs across {len(by_file)} files")
    for fp, bugs in sorted(by_file.items()):
        print(f"\n=== {fp} ({len(bugs)}) ===")
        for ln, col, kind, ctx in bugs[:5]:
            print(f"  L{ln}:{col} [{kind}]  …{ctx.strip()}…")
        if len(bugs) > 5:
            print(f"  ... and {len(bugs)-5} more")

if __name__ == "__main__":
    main()
