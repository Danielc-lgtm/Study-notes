#!/usr/bin/env python3
"""
For every theorem subpage (Thm - X.md), find single-letter math variables
used in the Statement section that are not introduced in the Notation
section. Reports likely missing-notation cases.

A "variable" here is:
- a single ASCII letter A-Z, a-z, optionally subscripted ($X_n$, $x_i$)
- a Greek letter via \alpha, \beta, ..., \omega, \varphi, etc.
- a few common mathcal/mathbb names ($\mathcal{F}$, $\mathbb{R}$ etc.)

Filters out conventional symbols that don't need definition:
- ℕ, ℤ, ℚ, ℝ, ℂ, $\mathbb{R}$, $\mathbb{Z}$, etc.
- Loop indices i, j, k, l, m, n (when used as subscripts only)
- Standard quantifiers and operators

Reports file:line with the missing variable and one line of context.
"""
import os, re, sys

VAULT = "/home/user/Study-notes/Study notes"

# Symbols that never need definition (universal mathematical objects)
UNIVERSAL = {
    r"\mathbb{R}", r"\mathbb{Z}", r"\mathbb{N}", r"\mathbb{Q}",
    r"\mathbb{C}", r"\mathbb{P}", r"\mathbb{F}", r"\mathbb{H}",
    r"\R", r"\Z", r"\N", r"\Q", r"\C",
    r"\emptyset", r"\infty", r"\cdot", r"\dots", r"\ldots", r"\cdots",
    r"\to", r"\mapsto", r"\implies", r"\iff",
    r"\leq", r"\geq", r"\le", r"\ge", r"\neq", r"\ne",
    r"\subset", r"\subseteq", r"\supset", r"\supseteq",
    r"\in", r"\notin", r"\ni",
    r"\cup", r"\cap", r"\setminus",
    r"\forall", r"\exists", r"\partial", r"\nabla",
    r"\sum", r"\prod", r"\int", r"\oint",
    r"\sqrt", r"\frac", r"\binom",
    r"\sin", r"\cos", r"\tan", r"\log", r"\ln", r"\exp",
    r"\mathrm{id}", r"\text", r"\mathrm",
    r"\lim", r"\sup", r"\inf", r"\max", r"\min",
    r"\det", r"\tr", r"\ker", r"\operatorname",
    r"\Delta", r"\nabla",
}

# Conventional loop / placeholder indices
INDEX_LETTERS = {"i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t",
                 "x", "y", "z", "a", "b", "c", "d", "e",
                 "I", "J", "K", "M", "N", "P", "Q", "R", "S", "T",
                 "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "U", "V", "W", "L",
                 # Greek lowercase letters commonly conventional
                 r"\alpha", r"\beta", r"\gamma", r"\delta", r"\epsilon",
                 r"\varepsilon", r"\zeta", r"\eta", r"\theta", r"\vartheta",
                 r"\iota", r"\kappa", r"\lambda", r"\mu", r"\nu", r"\xi",
                 r"\pi", r"\rho", r"\sigma", r"\tau", r"\upsilon", r"\varphi",
                 r"\phi", r"\chi", r"\psi", r"\omega",
                 r"\Gamma", r"\Delta", r"\Theta", r"\Lambda", r"\Xi", r"\Pi",
                 r"\Sigma", r"\Phi", r"\Psi", r"\Omega"}

# Regex for variables. We capture LaTeX commands (\word) and single letters.
TOKEN = re.compile(r"\\[a-zA-Z]+|[A-Za-z]")

def section_text(content, header_pattern):
    """Return text of the section whose header matches the pattern."""
    lines = content.split("\n")
    out = []
    in_section = False
    section_level = 0
    for line in lines:
        m = re.match(r"^(#+)\s+(.*?)\s*$", line)
        if m:
            lvl = len(m.group(1))
            title = m.group(2).strip()
            if in_section and lvl <= section_level:
                break
            if header_pattern.search(title):
                in_section = True
                section_level = lvl
                continue
        if in_section:
            out.append(line)
    return "\n".join(out)

def strip_command_args(math):
    """Strip arguments of typesetting commands so their inner letters don't
    appear as bare variables. Removes:
      \\mathcal{X}, \\mathbf{X}, \\mathbb{X}, \\mathrm{X}, \\operatorname{X},
      \\text{...}, \\textbf{...}, \\textit{...}, \\mathfrak{X}, \\mathscr{X}
    Also strips subscript/superscript single-token args ({i}, {n}, etc.)
    after _ and ^ so loop indices don't leak in.
    """
    typesetting = r"(?:mathcal|mathbf|mathbb|mathrm|mathfrak|mathscr|"\
                  r"operatorname|text|textbf|textit|textrm|textsf|"\
                  r"boldsymbol|underline|overline|widetilde|widehat|"\
                  r"vec|hat|tilde|bar|dot|ddot)"
    math = re.sub(r"\\" + typesetting + r"\s*\{[^{}]*\}", " ", math)
    # Strip subscript/superscript braced args
    math = re.sub(r"[_^]\s*\{[^{}]*\}", " ", math)
    # Strip single-character subscript/superscript: _i, ^k
    math = re.sub(r"[_^]\s*[A-Za-z0-9]", " ", math)
    return math

def extract_math_tokens(text):
    """Find all math regions and extract tokens."""
    tokens = []
    # $$...$$ display
    for m in re.finditer(r"\$\$([\s\S]*?)\$\$", text):
        tokens.extend(TOKEN.findall(strip_command_args(m.group(1))))
    # $...$ inline (rough)
    cleaned = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    for m in re.finditer(r"\$([^\$\n]+)\$", cleaned):
        tokens.extend(TOKEN.findall(strip_command_args(m.group(1))))
    return tokens

def text_introduces(content_up_to_pos, var):
    """Check if `var` appears anywhere in `content_up_to_pos` inside math —
    i.e., it has been seen at least once before the current display math.
    If yes, we treat it as introduced (the author at least mentioned it).
    """
    # Strip protected regions to avoid matching inside code or wikilinks
    # but keep math.
    text = content_up_to_pos
    # Collect tokens from all math regions
    earlier_tokens = set()
    for m in re.finditer(r"\$\$[\s\S]*?\$\$", text):
        earlier_tokens.update(TOKEN.findall(strip_command_args(m.group(0))))
    no_display = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    for m in re.finditer(r"\$[^\$\n]+\$", no_display):
        earlier_tokens.update(TOKEN.findall(strip_command_args(m.group(0))))
    return var in earlier_tokens

def main():
    notation_re = re.compile(r"^Notation(\s+Registry)?$", re.IGNORECASE)
    statement_re = re.compile(r"^Statement$|^The Definition$", re.IGNORECASE)

    # Only flag tokens that are likely to be PIVOTAL variables:
    # single uppercase Latin letters, or specific Greek lowercase commands
    # commonly used as maps (\varphi, \pi, \sigma, \tau, \rho — but only when
    # used as morphisms, hard to detect, so we err on the side of reporting).
    PIVOTAL_LATIN_UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    PIVOTAL_GREEK = {r"\varphi", r"\phi", r"\psi", r"\pi", r"\sigma",
                     r"\tau", r"\rho", r"\theta", r"\Phi", r"\Psi",
                     r"\Sigma", r"\Pi", r"\Lambda", r"\Gamma", r"\Theta",
                     r"\Omega", r"\Xi"}

    issues = []
    for root, dirs, files in os.walk(VAULT):
        for f in files:
            if not (f.startswith("Thm - ") or f.startswith("Def - ")) or not f.endswith(".md"):
                continue
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8") as fd:
                content = fd.read()
            notation = section_text(content, notation_re)
            statement = section_text(content, statement_re)
            if not statement or not notation:
                continue
            # For each $$...$$ display math in Statement, extract pivotal tokens
            # and check whether each was introduced anywhere up to the display
            # math (in Notation or earlier in Statement).
            statement_start_in_content = content.find(statement)
            for m in re.finditer(r"\$\$([\s\S]*?)\$\$", statement):
                tokens = TOKEN.findall(strip_command_args(m.group(1)))
                pos_in_content = statement_start_in_content + m.start()
                preceding = content[:pos_in_content]
                for tok in set(tokens):
                    if tok not in PIVOTAL_LATIN_UPPER and tok not in PIVOTAL_GREEK:
                        continue
                    if text_introduces(preceding, tok):
                        continue
                    issues.append((fp.replace(VAULT + "/", ""), tok))

    # Group by file
    from collections import defaultdict
    by_file = defaultdict(list)
    for fp, tok in issues:
        by_file[fp].append(tok)
    print(f"Files with possibly-missing notation: {len(by_file)}")
    for fp, toks in sorted(by_file.items())[:80]:
        print(f"  {fp}")
        print(f"     missing: {sorted(set(toks))}")

if __name__ == "__main__":
    main()
