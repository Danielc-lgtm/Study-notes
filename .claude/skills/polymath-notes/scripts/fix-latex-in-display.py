#!/usr/bin/env python3
"""
Fix wikilink display text that contains LaTeX `$...$` by:
1. Substituting common LaTeX commands with Unicode characters
2. Stripping the surrounding `$` markers

`[[Def - σ-Algebra|$\sigma$-algebra]]` -> `[[Def - σ-Algebra|σ-algebra]]`
`[[Thm - X|the proof that $R[X]$ is a UFD]]` -> `[[Thm - X|the proof that R[X] is a UFD]]`

Run with --apply to apply changes.
"""
import os, re, sys, argparse

VAULT = "/home/user/Study-notes/Study notes"

# LaTeX -> Unicode substitutions
SUBS = [
    # Greek lowercase
    (r"\\alpha\b", "α"), (r"\\beta\b", "β"), (r"\\gamma\b", "γ"),
    (r"\\delta\b", "δ"), (r"\\epsilon\b", "ε"), (r"\\varepsilon\b", "ε"),
    (r"\\zeta\b", "ζ"), (r"\\eta\b", "η"), (r"\\theta\b", "θ"),
    (r"\\vartheta\b", "θ"), (r"\\iota\b", "ι"), (r"\\kappa\b", "κ"),
    (r"\\lambda\b", "λ"), (r"\\mu\b", "μ"), (r"\\nu\b", "ν"),
    (r"\\xi\b", "ξ"), (r"\\pi\b", "π"), (r"\\varpi\b", "π"),
    (r"\\rho\b", "ρ"), (r"\\varrho\b", "ρ"), (r"\\sigma\b", "σ"),
    (r"\\varsigma\b", "ς"), (r"\\tau\b", "τ"), (r"\\upsilon\b", "υ"),
    (r"\\varphi\b", "φ"), (r"\\phi\b", "φ"), (r"\\chi\b", "χ"),
    (r"\\psi\b", "ψ"), (r"\\omega\b", "ω"),
    # Greek uppercase
    (r"\\Gamma\b", "Γ"), (r"\\Delta\b", "Δ"), (r"\\Theta\b", "Θ"),
    (r"\\Lambda\b", "Λ"), (r"\\Xi\b", "Ξ"), (r"\\Pi\b", "Π"),
    (r"\\Sigma\b", "Σ"), (r"\\Upsilon\b", "Υ"), (r"\\Phi\b", "Φ"),
    (r"\\Psi\b", "Ψ"), (r"\\Omega\b", "Ω"),
    # Number sets
    (r"\\mathbb\{R\}", "ℝ"), (r"\\mathbb\{Z\}", "ℤ"),
    (r"\\mathbb\{N\}", "ℕ"), (r"\\mathbb\{Q\}", "ℚ"),
    (r"\\mathbb\{C\}", "ℂ"), (r"\\mathbb\{F\}", "𝔽"),
    (r"\\mathbb\{P\}", "ℙ"), (r"\\mathbb\{H\}", "ℍ"),
    (r"\\mathbb\{E\}", "𝔼"),
    # Common arrows
    (r"\\Rightarrow\b", "⇒"), (r"\\Leftarrow\b", "⇐"),
    (r"\\Leftrightarrow\b", "⇔"), (r"\\iff\b", "⟺"),
    (r"\\to\b", "→"), (r"\\rightarrow\b", "→"),
    (r"\\leftarrow\b", "←"), (r"\\mapsto\b", "↦"),
    (r"\\hookrightarrow\b", "↪"),
    # Relations
    (r"\\leq\b", "≤"), (r"\\le\b", "≤"),
    (r"\\geq\b", "≥"), (r"\\ge\b", "≥"),
    (r"\\neq\b", "≠"), (r"\\ne\b", "≠"),
    (r"\\sim\b", "~"), (r"\\approx\b", "≈"),
    (r"\\equiv\b", "≡"), (r"\\propto\b", "∝"),
    (r"\\subset\b", "⊂"), (r"\\subseteq\b", "⊆"),
    (r"\\supset\b", "⊃"), (r"\\supseteq\b", "⊇"),
    (r"\\in\b", "∈"), (r"\\notin\b", "∉"), (r"\\ni\b", "∋"),
    # Operators
    (r"\\cdot\b", "·"), (r"\\times\b", "×"),
    (r"\\otimes\b", "⊗"), (r"\\oplus\b", "⊕"),
    (r"\\cup\b", "∪"), (r"\\cap\b", "∩"),
    (r"\\setminus\b", "∖"), (r"\\circ\b", "∘"),
    (r"\\pm\b", "±"), (r"\\mp\b", "∓"),
    # Calculus
    (r"\\partial\b", "∂"), (r"\\nabla\b", "∇"),
    (r"\\sum\b", "∑"), (r"\\prod\b", "∏"),
    (r"\\int\b", "∫"), (r"\\oint\b", "∮"),
    (r"\\infty\b", "∞"), (r"\\emptyset\b", "∅"),
    (r"\\forall\b", "∀"), (r"\\exists\b", "∃"),
    # Common functions
    (r"\\dim\b", "dim"), (r"\\det\b", "det"), (r"\\ker\b", "ker"),
    (r"\\Im\b", "Im"), (r"\\Re\b", "Re"),
    # Subscripts/superscripts: only single-char ones using Unicode
    (r"\^p\b", "ᵖ"), (r"\^n\b", "ⁿ"), (r"\^k\b", "ᵏ"),
    (r"\^2\b", "²"), (r"\^3\b", "³"), (r"\^{-1}", "⁻¹"),
    (r"_n\b", "ₙ"), (r"_k\b", "ₖ"), (r"_i\b", "ᵢ"),
    (r"_j\b", "ⱼ"), (r"_0\b", "₀"), (r"_1\b", "₁"),
    # Stylized letters
    (r"\\mathcal\{F\}", "ℱ"), (r"\\mathcal\{G\}", "𝒢"),
    (r"\\mathcal\{H\}", "ℋ"), (r"\\mathcal\{L\}", "ℒ"),
    (r"\\mathcal\{M\}", "ℳ"), (r"\\mathcal\{N\}", "𝒩"),
    (r"\\mathcal\{O\}", "𝒪"), (r"\\mathcal\{B\}", "ℬ"),
    (r"\\mathcal\{P\}", "𝒫"), (r"\\mathcal\{A\}", "𝒜"),
    # Specific common patterns
    (r"\\dots\b", "…"), (r"\\ldots\b", "…"), (r"\\cdots\b", "⋯"),
    (r"\\bullet\b", "•"), (r"\\star\b", "⋆"),
    (r"\\square\b", "□"), (r"\\blacksquare\b", "■"),
    # Backslash space (LaTeX) just removed
    (r"\\,", ""), (r"\\;", ""), (r"\\:", ""), (r"\\!", ""),
    (r"\\ ", " "), (r"\\quad\b", " "), (r"\\qquad\b", "  "),
]

SUB_RE = [(re.compile(p), r) for p, r in SUBS]

def sub_latex(text):
    """Apply LaTeX -> Unicode substitutions."""
    for r, u in SUB_RE:
        text = r.sub(u, text)
    return text

def fix_display(display):
    """Inside a display-text string, replace `$X$` regions with Unicode-substituted X."""
    # Match $...$ pairs (no nested $); inside, substitute then strip $
    def replace(m):
        inner = m.group(1)
        return sub_latex(inner)
    return re.sub(r"\$([^\$]+)\$", replace, display)

def fix_text(text):
    """Process all wikilinks in text; for any with $ in display, fix the display."""
    out = []
    i = 0
    n = len(text)
    fixes = 0
    while i < n:
        if text[i:i+2] == "[[":
            # Find matching ]]
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
                content = text[i+2:j]
                if "|" in content:
                    target, display = content.split("|", 1)
                    if "$" in display:
                        new_display = fix_display(display)
                        out.append(f"[[{target}|{new_display}]]")
                        i = j + 2
                        fixes += 1
                        continue
                out.append(text[i:j+2])
                i = j + 2
                continue
            out.append(text[i])
            i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out), fixes

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
