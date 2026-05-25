#!/usr/bin/env python3
"""
Scan the vault for inline-math regions that KaTeX/Obsidian commonly mis-renders.

Patterns checked:
1. $...$ where $-toggle appears INSIDE \text{...} — opens nested math
   region in text mode, often renders broken. Always fixable to
   \text{...}\sigma\text{...} (split the text around the math command).
2. Mismatched braces inside $...$ — count of { vs } unbalanced.
3. \\ (LaTeX line break) inside inline math $...$ — only legal in
   display math or environments.
4. \left( without matching \right) within the same math region (rough
   check; some legitimate cases use \right. or span lines).
5. Display math $$ with no closing $$ in the document.

Reports file:line with one line of context.
"""
import os, re, sys

VAULT = "/home/user/Study-notes/Study notes"

def scan_file(text):
    bugs = []
    lines = text.split("\n")
    # 5. Display $$ pairing — count $$ tokens; an odd count means a
    # missing delimiter. We exclude inline contexts where `$X$$Y$` would
    # produce a phantom $$ by walking with a state machine.
    in_inline = False
    n_display = 0
    i = 0
    while i < len(text):
        if text[i:i+2] == "$$":
            if not in_inline:
                n_display += 1
                i += 2
                continue
            else:
                # `$$` inside inline math closes inline immediately then opens
                # again? Treat as two separate $ delimiters. Rare; skip.
                i += 1
                continue
        if text[i] == "$" and (i == 0 or text[i-1] != "\\"):
            in_inline = not in_inline
            i += 1
            continue
        if text[i] == "\n":
            in_inline = False  # inline math is line-bound
        i += 1
    if n_display % 2 != 0:
        bugs.append((0, "unpaired-display",
                     f"file has {n_display} '$$' tokens"))
    # Per-line inline math scan
    in_display = False
    for ln, line in enumerate(lines, start=1):
        # Track display state
        i = 0
        # Walk inline math regions outside display
        # Simple state machine
        math_start = None
        depth = 0  # depth of \text{...} braces while inside math
        while i < len(line):
            two = line[i:i+2]
            if two == "$$":
                in_display = not in_display
                i += 2
                continue
            if in_display:
                i += 1
                continue
            # Track \text{ braces inside math mode
            if math_start is not None:
                if line[i:i+6] == "\\text{" or line[i:i+8] == "\\mathrm{":
                    depth += 1
                    i += (6 if line[i:i+6] == "\\text{" else 8)
                    continue
                if line[i] == "}" and depth > 0 and (i == 0 or line[i-1] != "\\"):
                    depth -= 1
                    i += 1
                    continue
            if line[i] == "$" and (i == 0 or line[i-1] != "\\"):
                # If we encounter $ inside an open \text{...} brace (depth > 0),
                # this is a re-entry into math mode from text mode. KaTeX
                # supports it; do not flip the math_start state, just skip.
                if depth > 0:
                    # Find the closing $ of this nested math (within the same line)
                    j = line.find("$", i+1)
                    if j != -1:
                        # Skip the nested math
                        i = j + 1
                        continue
                if math_start is None:
                    math_start = i
                else:
                    # Closing $; inspect [math_start+1, i)
                    content = line[math_start+1:i]
                    # 1. $ inside \text{...} content? KaTeX supports
                    # \text{prefix $X$ suffix} (math re-entry), but only
                    # when the $...$ has whitespace separating it from the
                    # surrounding text. The bug pattern is \text{X$Y$} or
                    # \text{$Y$Z} or \text{X$Y$Z} where letters/digits abut
                    # the dollar with no space.
                    for tm in re.finditer(r"\\text\{([^{}]*)\}", content):
                        inner = tm.group(1)
                        # Find $...$ pairs and check spacing
                        for dm in re.finditer(r"\$[^$]+\$", inner):
                            s, e = dm.span()
                            before = inner[s-1] if s > 0 else " "
                            after = inner[e] if e < len(inner) else " "
                            if before not in " \t" or after not in " \t":
                                bugs.append((ln, "dollar-in-text-no-space",
                                             line[max(0, math_start-5):min(len(line), i+5)]))
                                break
                    # 2. Brace balance in content (ignoring escaped \{ \})
                    stripped = re.sub(r"\\[\{\}]", "", content)
                    if stripped.count("{") != stripped.count("}"):
                        bugs.append((ln, "unbalanced-braces",
                                     line[max(0, math_start-5):min(len(line), i+5)]))
                    # 3. \\ inside inline math is a bug ONLY when it occurs
                    # outside a \begin{...}...\end{...} environment. Inside
                    # matrix/array/cases environments \\ is the row separator.
                    content_no_env = re.sub(r"\\begin\{[^}]+\}[\s\S]*?\\end\{[^}]+\}", " ", content)
                    if re.search(r"(?<!\\)\\\\(?!\\)", content_no_env):
                        bugs.append((ln, "line-break-in-inline",
                                     line[max(0, math_start-5):min(len(line), i+5)]))
                    # 4. \left without \right
                    n_left = len(re.findall(r"\\left[\(\[\{\|.]", content))
                    n_right = len(re.findall(r"\\right[\)\]\}\|.]", content))
                    if n_left != n_right:
                        bugs.append((ln, "left-right-mismatch",
                                     line[max(0, math_start-5):min(len(line), i+5)]))
                    math_start = None
                i += 1
            else:
                i += 1
    return bugs

def main():
    total = 0
    by_kind = {}
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as fd:
                text = fd.read()
            # Skip protected regions: YAML frontmatter, fenced code
            if text.startswith("---\n"):
                end = text.find("\n---\n", 4)
                if end != -1:
                    # We'll just scan after frontmatter; replace with newlines
                    text = "\n" * text[:end+5].count("\n") + text[end+5:]
            text = re.sub(r"```[\s\S]*?```", lambda m: "\n" * m.group(0).count("\n"), text)
            bugs = scan_file(text)
            for ln, kind, ctx in bugs:
                by_kind.setdefault(kind, []).append((fp.replace(VAULT + "/", ""), ln, ctx))
                total += 1
    print(f"Total: {total} math-region bugs\n")
    for kind, items in sorted(by_kind.items()):
        print(f"=== {kind}: {len(items)} ===")
        for fp, ln, ctx in items[:30]:
            print(f"  {fp}:{ln}  ...{ctx.strip()}...")
        if len(items) > 30:
            print(f"  ... and {len(items)-30} more")
        print()

if __name__ == "__main__":
    main()
