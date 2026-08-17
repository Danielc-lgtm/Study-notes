# Paper-Note Page Templates — Self-Contained Edition

Page skeletons for the `paper-notes` skill. The reading surface is a **Map** plus one **section page** per paper section; two **reference pages** sit under the Map, optional. There are no per-result subpages.

Low-level Obsidian syntax is **not** repeated here — see `../../polymath-notes/references/obsidian-patterns.md` (source of truth). Two reminders:

- Math is `$...$` inline, `$$...$$` display. Nothing else. Never `$...$` inside `[[ ]]` — link text uses Unicode.
- Callout folds: `> [!def]+` (expanded), `> [!recall]-` (collapsed), `> [!import]-`, `> [!note]-` (collapsed proof/commentary), `> [!warning]`.

**The governing invariant is the scissor test:** delete every wikilink on a section page and every statement and proof still typechecks from what remains rendered. Wikilinks appear only in the foot's Climb line.

---

## The four expansion tiers (used everywhere on a section page)

Every non-anchor token in a statement is expanded on the page in one of these, chosen by length and first-vs-later use. Each T1/T2/T3 callout is preceded by a one-line **"Used here —"** consequence, *outside* the fold.

- **T0 inline gloss** (≤1 line, in prose): **bold term** — em-dash — symbolic clause bottoming at anchors — em-dash — plain parenthetical.
  > $\Gamma$ acts **freely** — $\forall h\in\Gamma\setminus\{1\}\,\forall z:\ hz\neq z$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^2:\ \#\{h:hK\cap K\neq\varnothing\}<\infty$ (each compact set meets finitely many translates).
- **T1 expanded core callout** (2–12 lines, first use):
  ```markdown
  **Used here —** only that it yields a well-defined $I_\phi$; no other property of $\phi$ is used.
  > [!def]+ $\phi$ a Bernstein function satisfying Assumption 2.3
  > $\phi:(0,\infty)\to[0,\infty)$ is **Bernstein** if $C^\infty$ with $(-1)^{n-1}\phi^{(n)}\ge0$; equivalently (Lévy–Khintchine) $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda u})\nu(\mathrm du)$ … **Assumption 2.3:** $b>0$ or $\nu(0,\infty)=\infty$.
  ```
- **T2 collapsed recall chip** (expanded earlier, or an earlier-section object used through its end-formula): `> [!recall]- $I_\phi$, the weighted heat-kernel integral` with the shorter core inside.
- **T3 import box** (external result, no proof):
  ```markdown
  > [!import]- (WX) Wang–Xue strip identity — Says / Needs / Gives  [the one genuine gap of §3]
  > **Says.** $\int_{F_\tau}p_{\mathbb H^2}(u,w,e^Lw)\,\mathrm d\mathrm{vol}=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-u/4}e^{-L^2/4u}}{2\sqrt{\pi u}}$.
  > **Needs.** $u>0$; $L=m\ell_\gamma$; $\tau$ in standard form; speed-$2$ $\mathbb H^2$ heat kernel.
  > **Gives.** the spatial integral, factorised (geometric)×(analytic in $u,L$). Assume freely; nothing here re-proves it. **Status:** [WX25, Lem 3.2]; the $\mathbb H^2$ kernel has no elementary form.
  ```

---

## Section page

Filename `§N <Section Title>.md` (the paper's own numbering; the `§` glyph is fine).

````markdown
---
type: paper-section
paper: "<CiteKey>"
subject: <slug>
section: "<N>"
tags: [paper, section, self-contained]
---

> [!info] Part of [[Map - <paper>]]. Self-contained: every symbol, predicate and imported result used below is written out on this page. Grey callouts are folds on THIS page — opening one is a scroll, not a jump. You can typecheck §N front-to-back without opening anything else.

**What §N buys you.** <one–three sentences, in type-language: the section's deliverable.>

# A. Standing setup

<Inline, as literal text bottoming at anchors, every standing/geometric object §N uses — so an anchor-jump straight into §N is covered.>

**Notation for §N.**

| symbol | type |
|---|---|
| ... | ... |

**Standing conventions.** <the locked block, verbatim: Δ-sign, speed, the distinct time-like glyphs, κ=s(s-1) with κ≥−¼, total-mass = non-trivial non-peripheral.>

<Then, for each object built in an earlier section that §N uses only through an end-formula: a "Used here —" line, then a T2 `> [!recall]-` chip carrying the inlined core.>

# B. Spine of §N (skim layer)

<A numbered list, one line per result IN ORDER, each a *Given* … ⊢ *Produces* … type card. Reading only this list gives §N's logical content.>

# C. The results

## §N.1  <name>

<new symbols delta from the table; then, for every unfamiliar token in the coming statement, its T0/T1/T2/T3 expansion, each with its "Used here —" line outside any fold.>

> **Result N.1 (<name>).** Assume **(H1)** … **(Hn)** …. Then
> $$\dots\tag{N}$$

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | <import/recall/hypothesis> | <what> | <result> |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> **Step 1.** … (each step cites a labelled hypothesis, an import's *Gives*, or an explicit computation.)

> [!note]- Verification of <the worked number> (skippable)
> … (every number reproducible from the page's own cores.)

> [!warning] Why <hypothesis> has exactly this form
> <when the exact shape of a hypothesis is the whole content.>

## §N.2  <name>
…

# D. Exports, climb, commentary

**Exports (what later sections consume from §N).**
- **(E1)** <numbered typed statement>. → §<k>, §<l>.

**Climb (optional — none is needed to typecheck §N).** Sibling sections: [[§<k> …]] · [[§<l> …]]. Import sources and gap-depth: [[External Inputs and Gaps]]. Backchain to anchors: [[Anchors and Prerequisites]]. <Deletable with zero loss. NEVER link to a per-result atom page — none exist.>

> [!note]- Commentary (skippable)
> <Tong-register motivation, the one-line mechanism, what breaks without each hypothesis. The only place Tong register is allowed. Held to the statement-level faithfulness bar.>
````

**Standing-setup is the coverage fix.** Inlining *every* standing object — not only the fashionable jargon — is what lets a reader jump straight into §N. If a symbol appears in a statement but not in the setup or an expansion, that is the coverage bug this section prevents.

---

## Map page

Filename `Map - <Paper Short Title>.md`. The reader's entry point and one-screen overview; links here are convenience.

````markdown
---
type: paper-map
paper: "<CiteKey>"
subject: <slug>
title: "<Full Title> — <Authors>"
tags: [paper, map, self-contained]
---

> [!info] This note-set is a self-contained rewrite. To read the whole paper you open only this Map and the section pages, in order — never a subpage. The two reference pages at the foot are optional.

# What the paper does
<one paragraph, plain.>  **Source.** `paper_source/<file>` — <citation>.

# The one identity (the spine)
$$\dots$$
<the logical chain as a numbered list, each link tagged with the section that proves it.>

# Global signature
<every symbol used anywhere, typed; a Conventions & collisions line.>

# Section-level dependency table
| section | consumes | produces | page |
|---|---|---|---|
<one row per section, linking the section page. Then: the shortest chain to the headline result.>

# Reading orders
<cover-to-cover; just-the-main-theorem; per-audience; what is skippable with what cost.>

# The honest floor
<two sentences pointing to [[External Inputs and Gaps]] and [[Anchors and Prerequisites]], naming the deepest gaps.>

# Open questions
<the paper's stated open questions and anything the notes noticed, each a precise question.>
````

---

## Reference page — External Inputs and Gaps

Filename `External Inputs and Gaps.md`. The consolidated ledger; optional reading (each import is already stated on its section page).

````markdown
---
type: paper-imports
paper: "<CiteKey>"
subject: <slug>
tags: [paper, imports, gaps, self-contained]
---

> [!info] Optional reference. Every result below is already stated in full, at point of use, on its section page. This is the consolidated ledger + source + gap-depth. Part of [[Map - <paper>]].

# What "gap" means here
<an import is not a gap if a reader with the anchor set could reconstruct it (anchor-level); it is a gap if it needs machinery above the anchor set. Both are usable on faith.>

# Genuine gaps, ranked by how much rests on them
| # | import | Says (conclusion) | source | used at | closes with |
|---|---|---|---|---|---|

# Imports that are NOT gaps (anchor-level)
| import | Says | why not a gap |
|---|---|---|

# The pattern
<where the gaps cluster, and which single DAG node would close several at once.>
````

---

## Reference page — Anchors and Prerequisites

Filename `Anchors and Prerequisites.md`. The anchor set named, the backchain, the repair order; optional reading.

````markdown
---
type: prereq-dag
paper: "<CiteKey>"
subject: <slug>
tags: [paper, prereqs, anchors, self-contained]
---

> [!info] Optional reference. The section pages expand every term down to the anchor set below, on the page. This names that set (so it can be sanity-checked) and gives the backchain and a repair order. Part of [[Map - <paper>]].

# The anchor set — what the section pages assume you own
| anchor | what it covers here |
|---|---|

> [!warning] Calibration calls, stated not hidden
> <any 🔵 node treated as an anchor, and the anchor most worth double-checking. A wrongly-assumed anchor is the failure this design exists to prevent.>

# Backchain — every non-anchor term, and where it bottoms out
<per section, terse: term → reduction → 🟢 anchor or **gap**.>

# Suggested repair order (to close gaps rather than assume them)
<ordered list; the highest-leverage node first.>

# What this paper unlocks downstream
| DAG node | what §-content feeds it |
|---|---|
````
