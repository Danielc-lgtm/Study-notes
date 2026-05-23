# Obsidian Formatting Patterns

This document describes Obsidian-specific formatting conventions for the polymath-notes skill. All pages are standard markdown files stored in a GitHub-hosted Obsidian vault.

## LaTeX / Math

Obsidian uses MathJax (or KaTeX, depending on user configuration) for math rendering.

**Inline math:** `$...$`
```markdown
A group $G$ acts on a set $X$ via a homomorphism $\varphi : G \to \text{Sym}(X)$.
```

**Display math:** `$$...$$`
```markdown
$$|G| = |G_x| \cdot |G \cdot x|$$
```

**Important:** Every variable name, mathematical symbol, and equation in prose must be in LaTeX. Do not use bare Unicode math symbols (∈, ∇, ∂, ℝ, etc.) in prose — always wrap them in `$...$`. Write `$\in$`, `$\nabla$`, `$\partial$`, `$\mathbb{R}$`.

**Exception — never use `$...$` inside a wikilink.** LaTeX is for prose, formal statements, and callout bodies only. Obsidian renders `$...$` literally inside `[[ ]]`, so wikilink display text (and targets) must use Unicode characters instead — see the Wikilinks section below.

**Use only core MathJax/KaTeX commands — never amsmath/physics-package macros.** Obsidian's math renderer supports the *core* TeX command set, not the full set a LaTeX document with `\usepackage{...}` provides. Commands defined by amsmath or other packages render as raw red error text. The most common offender is `\fint` (the average-integral, `⨍`): it is **not** a core command and does not render. Write the average explicitly instead — `\frac{1}{\lambda(B)}\int_B f` rather than `\fint_B f`. Other non-core commands to avoid: `\xfrac`, `\sfrac`, `\abs`, `\norm`, `\bra`, `\ket`, `\dv`, `\pdv` (physics package), `\eqref`, `\numberwithin`, and custom `\newcommand` macros (Obsidian has no preamble — every note is rendered in isolation, so a macro defined in one note is undefined everywhere). When in doubt, prefer the explicit primitive form: `\frac`, `\int`, `\sum`, `\left|...\right|`, `\lVert...\rVert`, `\langle...\rangle`, `\frac{d}{dx}`, `\frac{\partial}{\partial x}`. If a compact notation is genuinely needed repeatedly, spell it out in full each time rather than relying on a macro.

## Wikilinks

Obsidian uses `[[...]]` wikilinks for internal cross-references. These are the primary linking mechanism in the vault.

**Basic link:**
```markdown
[[Def - Group]]
```

**Display text (pipe syntax):**
```markdown
[[Def - Group|group]]
[[Def - Compactness|compact]]
```

**Never put LaTeX (`$...$`) in wikilink display text — or anywhere inside `[[...]]`.** Obsidian does *not* render math inside a wikilink: `[[Def - Sigma-Algebra|$\sigma$-algebra]]` displays the literal characters `$\sigma$-algebra`, dollar signs and all. The same applies to the target and to section anchors. Inside `[[...]]`, write mathematical symbols as **Unicode characters**, not LaTeX:

```markdown
[[Def - Sigma-Algebra|σ-algebra]]            not  |$\sigma$-algebra]]
[[Thm - Dynkin's π-λ Theorem|π–λ theorem]]   not  |$\pi$–$\lambda$ theorem]]
[[Def - Lp Spaces|Lᵖ space]]                 not  |$L^p$ space]]
[[Thm - ...|σ-subadditivity]]                not  |$\sigma$-subadditivity]]
```

Common substitutions for display text: `\sigma`→σ, `\pi`→π, `\lambda`→λ, `\mu`→μ, `\nu`→ν, `\varphi`→φ, `\mathbb{P}`→ℙ, `\mathbb{R}`→ℝ, `\mathbb{N}`→ℕ, `\mathbb{Q}`→ℚ, `\mathcal{F}`→ℱ; superscripts `^1 ^2 ^p ^k ^n`→¹ ² ᵖ ᵏ ⁿ; subscripts `_n _k`→ₙ ₖ; `\le`→≤, `\ge`→≥, `\to`→→, `\infty`→∞, `\leftrightarrow`→↔. Filenames likewise use the Unicode character (e.g. `Def - σ-Finite Measure.md`), so the link target is a plain Unicode string too. LaTeX `$...$` is *only* for ordinary prose, formal statements, and callout bodies — never within `[[ ]]`.

**Whitespace rule for inline math (mandatory).** KaTeX/Pandoc require that the character immediately AFTER an opening `$` is NOT whitespace, and the character immediately BEFORE a closing `$` is NOT whitespace. Violating either rule makes Obsidian fail to close the math region, silently swallowing following prose into one runaway math block. The classic offender is writing `$X = $ (some prose)` — the closing `$` is preceded by a space, so KaTeX does not treat it as a close; the math region extends through the prose until the next `$`, which then captures the prose as math (rendering it without spaces). Fix patterns:

- **Trailing operator inside math.** Never end math with `= ` (or `+ `, `- `, `\mapsto `, etc.) right before the closing `$`. Either remove the trailing whitespace (`$X =$` is valid and renders fine, with the dangling `=` shown — this is the mechanical fix), or move the operator into prose: `$X$ = (some prose)`. The mechanical fix is what the auto-fixer applies.
- **Leading whitespace inside math.** Never write `$ X$` (space after opening `$`). Just `$X$`.
- **Empty math.** Never write `$$` inline (zero content); write the content or remove the dollars.
- **Escaped dollars near math.** `\$` inside math is a literal dollar that does NOT close the region. If you write `$...X_n\$ for all...$`, KaTeX keeps math open past the `\$`. Fix by removing the spurious backslash: `$...X_n$ for all...`.

The skill ships two scripts to enforce this:
- `.claude/skills/polymath-notes/scripts/find-math-bugs.py` — scans the whole vault, reports every offending math region with file:line. Run it after any batch.
- `.claude/skills/polymath-notes/scripts/fix-math-bugs.py` — applies the mechanical fix (strip whitespace inside math at both ends) across the vault. Run with `--apply` after dry-run review.

**Link to a specific section:**
```markdown
[[Thm - Lagrange's Theorem#Why Is It True]]
```

**Never wrap a wikilink in square brackets.** Writing `[[[Def - Group]]]`, or enclosing a list of wikilinks as `[[[Def - A]], [[Def - B]]]`, places a `[` directly against the `[[` opener — Obsidian reads the resulting `[[[` as a malformed link, and the link breaks. To group a list of wikilinks (for instance the dependency list on an exercise index page), enclose it in parentheses: `([[Def - A]], [[Def - B]])`.

**All definition, theorem, and exercise references throughout the notes should use wikilinks.** The same concept may be linked with different display text in different contexts.

**A wikilink target must resolve.** Only write `[[Page Name]]` when that page already exists or is being created in the same batch of notes. Everything else must be written as **bold plain text**, not a wikilink: an in-scope concept that has no page of its own, a "companion" definition or theorem mentioned in body prose or the Bridges list, and — importantly — a forward reference to a downstream subject in an `[!tip]` "Unlocked" callout. In Obsidian, clicking a wikilink whose target file does not exist *creates* an empty stub page, so a `[[...]]` to a nonexistent page is never harmless. When the downstream page is eventually written, the link can be added then.

## Transclusion (Embedding)

Obsidian can embed the content of another page (or a specific section) inline. This is ideal for Recall sections in exercises and for restating definitions at point of use.

**Embed an entire page:**
```markdown
![[Def - Group]]
```

**Embed a specific section:**
```markdown
![[Def - Group#The Definition]]
![[Thm - First Isomorphism Theorem#Formal Statement]]
```

**When to use transclusion vs. restatement:**
- Use transclusion when the full definition or theorem statement should appear inline and you want automatic updates if the source changes.
- Use a brief restatement in your own words when transclusion would be too bulky, or when you want to highlight a specific aspect of the definition relevant to the current context.
- Always include a wikilink alongside any restatement.

## Collapsible Callouts

Collapsible content — lemma decompositions, formal proofs, progressive hints, worked-solution steps — uses Obsidian's **collapsible callouts**: a `> [!type]` block whose type marker carries a `-` (collapsed by default) or `+` (expanded by default). Study notes use `-`, so the content is hidden until the reader chooses to expand it. Every line of the callout body is prefixed with `> `, and a blank line inside the callout is a line containing just `>`.

```markdown
> [!note]- Lemma 1: Cosets partition G
> **Statement:** Two cosets $gH$ and $g'H$ are either identical or disjoint.
>
> **Hint:** Show that "lying in the same coset" is an equivalence relation.
```

**Nesting:** a callout nests inside another by adding a second `> ` to its lines — the inner callout's body carries `> > `. This is how a full proof is tucked inside a lemma:

```markdown
> [!note]- Lemma 1: [Statement]
> **Statement:** [...]
>
> **Hint:** [...]
>
> > [!note]- Full proof
> > [the complete proof]
```

**Do not use HTML `<details>`/`<summary>` for collapsible content.** Although `<details>` renders in Editing view, it does not collapse reliably in Obsidian's Reading view, and Obsidian does not parse markdown inside HTML tags. Collapsible callouts collapse correctly in *both* views and support the full range of markdown — LaTeX, wikilinks, lists, nested callouts — in both the title and the body.

**Never put a wikilink inside an HTML tag.** A `[[wikilink]]` placed inside `<details>`, `<summary>`, `<strong>`, or any other HTML element is *not* clickable in Obsidian — Obsidian does not parse wikilink syntax inside raw HTML. Keep every wikilink in ordinary Markdown (callout titles and bodies are Markdown, so wikilinks work there).

**Formatting notes:**
- Choose a callout type from the list in the Callouts section below; `note` is the neutral default for proofs, lemmas, hints, and derivations.
- A callout must be preceded by a blank line (or begin the section).
- The title follows the type marker on the same line: `> [!note]- Title here`.

## Foldable Bullets (for the Concept Map)

The concept map needs entries that are both collapsible and carry a clickable wikilink in the visible title. HTML `<details>` cannot do this: a wikilink inside the `<summary>` is dead, and a `<details>` block containing markdown does not collapse reliably in Obsidian's Reading view. Use a nested bullet list instead — a parent bullet holds the wikilinked name, an indented child bullet holds the statement:

```markdown
- **[[Def - Group]]**
	- A group is a set $G$ with an associative binary operation, an identity element, and an inverse for every element. [...continue the 3–5 sentence statement, all on this single line...]

- **[[Thm - Lagrange's Theorem]]**
	- For a finite group $G$ and a subgroup $H \leq G$, $|G| = |H| \cdot |G:H|$, so $|H|$ divides $|G|$. [...3–5 sentences...]
```

Folding the parent bullet collapses the statement, and this works in both Editing view and Reading view (enable "Fold indent" in Settings → Editor; note that some themes hide the fold arrows). The wikilink, being ordinary Markdown, is clickable in both views. Two rules keep folding reliable in Reading view: keep the parent bullet to a single short line, and write the child statement as a single (long) line — Reading view may not show a fold arrow for multi-line list items. Indent the child by one level (a tab, or the indentation Obsidian inserts when you press Tab in a list).

## Callouts

Obsidian has a native callout syntax using `>` blocks:

```markdown
> [!note] Exercise Index — §1.1 Basic Concepts
> See [[Exercise Index - §1.1]] for all exercises in this section.
```

```markdown
> [!tip] Unlocked: Affine Variety
> Now that you have ideals and the Zariski topology, you can define **affine varieties** as zero sets of ideals *(from Algebraic Geometry)*.
```

```markdown
> [!warning] Illegal but tempting
> Exchanging limits without checking uniform convergence...
```

Available callout types: `note`, `tip`, `warning`, `danger`, `example`, `info`, `abstract`, `question`, `quote`, `bug`, `success`, `failure`.

Use callouts for:
- Exercise index links at the end of each concept map section (`[!note]`)
- "Unlocked by this" previews of advanced concepts (`[!tip]`)
- "Illegal but tempting" warnings (`[!warning]`)
- Trigger-reaction patterns that deserve emphasis (`[!example]`)

## YAML Frontmatter

Every page must have YAML frontmatter at the top of the file. This enables Dataview queries, filtering, and the graph view.

**Topic page:**
```yaml
---
type: topic
subject: group-theory
chapter: "1.1-1.2"
title: "Group Theory I — Basics, Quotients, Isomorphisms"
tags: [algebra, group-theory]
---
```

**Definition subpage:**
```yaml
---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
tags: [algebra, group-theory]
---
```

**Theorem subpage:**
```yaml
---
type: theorem
subject: group-theory
prereqs:
  - "Def - Normal Subgroup"
  - "Def - Quotient Group"
  - "Def - Homomorphism"
tags: [algebra, group-theory]
---
```

**Exercise subpage:**
```yaml
---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Normal Subgroup"
  - "Thm - Lagrange's Theorem"
tags: [algebra, group-theory]
---
```

**Exercise index:**
```yaml
---
type: exercise-index
subject: group-theory
section: "1.1"
tags: [algebra, group-theory]
---
```

The `prereqs` field lists the wikilink targets (without `[[]]`) of all definitions and theorems that the page depends on. The `difficulty` field uses ⭐ (routine), ⭐⭐ (combining theorems or non-obvious), ⭐⭐⭐ (competition-level).

## File Naming Conventions

```
Def - [Concept Name].md
Thm - [Theorem Name].md
Ex - [Short Description].md
Exercise Index - §X.Y [Section Title].md
[Topic Name].md
```

Examples:
```
Def - Group.md
Def - Normal Subgroup.md
Thm - First Isomorphism Theorem.md
Thm - Orbit-Stabiliser Theorem.md
Ex - Groups of order pq are not simple.md
Ex - Index-2 subgroups are normal.md
Exercise Index - §1.1 Basic Concepts.md
Group Theory I — §1.1–1.2.md
```

Use descriptive names. The file name IS the wikilink target, so it should be clear and unambiguous.

**Windows-portable filenames (mandatory).** The vault must be cloneable on Windows clients, where the filesystem forbids the characters `< > : " / \ | ? *` in filenames. Never use any of these characters in a filename. Two patterns to watch for:

- **Asterisks in dualization / homology notation.** Filenames like `Def - Lambda^k V*.md` or `Ex - Computing H_* of the Torus.md` will fail `git checkout` on Windows. Spell them out: `Def - Alternating Tensor and Lambda k V Dual.md`, `Ex - Computing the Homology of the Torus.md`.
- **Slashes in fraction notation.** Filenames like `Ex - Spin-1/2 in a Magnetic Field.md` are silently interpreted as a path separator on POSIX (creating a directory) and fail on Windows. Spell out the fraction: `Ex - Spin-Half in a Magnetic Field.md`. Same goes for ratios in titles (`1/2`, `3/4`).

Other characters to spell out when they would otherwise appear in a filename: colons (`:` → ` —` or omit), question marks (`?` → omit), pipes (`|` → ` and `), quotes (`"` → omit). The em-dash (`—`), section sign (`§`), and Unicode math (σ, ℝ, →) are all safe.

## Vault Directory Structure

```
Study notes/
  [Subject Area]/                    # e.g., Algebra/, Analysis/, Geometry/
    [Subtopic]/                      # e.g., Group Theory/, Functional Analysis/
      [Topic Page].md
      [Topic Name]/                  # subfolder for subpages
        Def - [Name].md
        Thm - [Name].md
        Ex - [Name].md
        Exercise Index - §X.Y.md
```

Example:
```
Study notes/
  Algebra/
    Group Theory/
      Group Theory I — §1.1–1.2.md
      Group Theory I/
        Def - Group.md
        Def - Subgroup.md
        Def - Normal Subgroup.md
        Thm - Lagrange's Theorem.md
        Thm - First Isomorphism Theorem.md
        Ex - Element order divides group order.md
        Ex - Index-2 subgroups are normal.md
        Exercise Index - §1.1 Basic Concepts.md
        Exercise Index - §1.2 Quotients and Isomorphisms.md
      Group Theory II — §1.5–1.7.md
      Group Theory II/
        ...
```

Wikilinks work across folders in Obsidian, so `[[Def - Group]]` resolves correctly even from a page in a different subject's folder, as long as the file name is unique. If there is ambiguity (e.g., two subjects define "Def - Convergence"), use the full path: `[[Algebra/Group Theory/Group Theory I/Def - Group]]`.

## Tables

Standard markdown tables:
```markdown
| Assumptions | Target | Theorem | Key condition |
|---|---|---|---|
| Homomorphism $\varphi$ given | Identify quotient | [[Thm - First Isomorphism Theorem]] | Compute $\ker$ and $\text{im}$ |
```

## Tags

Use tags in frontmatter for subject classification. Tags enable filtering in Obsidian's search and graph view:
- Subject tags: `group-theory`, `functional-analysis`, `differential-geometry`
- Area tags: `algebra`, `analysis`, `geometry`, `topology`, `probability`
- Cross-cutting tags: `convergence`, `compactness`, `fixed-point`, `spectral`
