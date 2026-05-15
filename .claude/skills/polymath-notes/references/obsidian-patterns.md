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

**Link to a specific section:**
```markdown
[[Thm - Lagrange's Theorem#Why Is It True]]
```

**All definition, theorem, and exercise references throughout the notes should use wikilinks.** The same concept may be linked with different display text in different contexts.

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

## Collapsible Sections (Details/Summary)

Obsidian supports HTML `<details>/<summary>` tags for collapsible content. These implement the hierarchical structure principle.

```markdown
<details>
<summary><strong>Lemma 1: Cosets partition G</strong></summary>

Two cosets $gH$ and $g'H$ are either identical or disjoint...

</details>
```

**Nesting:** Collapsible sections can be nested for multi-level progressive disclosure:

```markdown
<details>
<summary><strong>Step 1: Show the map is well-defined</strong></summary>

The key is that $gH = g'H$ implies $\varphi(g) = \varphi(g')$...

<details>
<summary>Full derivation</summary>

[Detailed computation]

</details>

</details>
```

**Important formatting notes:**
- Leave a blank line after `<summary>...</summary>` before the content.
- Leave a blank line before the closing `</details>` tag.
- Markdown rendering inside `<details>` blocks works in Obsidian, including LaTeX, wikilinks, and further nesting.

## Callouts

Obsidian has a native callout syntax using `>` blocks:

```markdown
> [!note] Exercise Index — §1.1 Basic Concepts
> See [[Exercise Index - §1.1]] for all exercises in this section.
```

```markdown
> [!tip] Unlocked: Affine Variety
> Now that you have ideals and the Zariski topology, you can define affine varieties...
> See [[Def - Affine Variety]] *(from Algebraic Geometry)*.
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
