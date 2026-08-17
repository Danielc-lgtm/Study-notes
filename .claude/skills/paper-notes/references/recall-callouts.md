# Recall and Reference Callouts

The paper-notes callouts that carry point-of-use recalls (Rule 2), imported external results (Rule 5), and flagged uncertainties (Rule 6). All are Obsidian callouts; syntax and nesting rules are in `obsidian-patterns.md`. `[!cite]` is a native Obsidian type (an alias of `quote`, rendered with a quote icon) and `[!warning]` is native. `[!recall]` is a custom label: Obsidian renders an unrecognised callout label with a default (pencil) icon and neutral styling, and the collapse marker (`-`/`+`) still works, so it is safe to use — if a guaranteed-styled type is ever wanted, `[!note]-` is the native fallback for a recall.

---

## The recall callout — `> [!recall]-`

The core device of the skill. Whenever a term or notation above the undergraduate floor is used, insert a recall **at the point of use**. It is collapsed (`-`) so a reader who knows the term is not slowed, and it must be **self-sufficient**: a reader who never clicks the wikilink still gets both the formal content and the plain-language meaning.

**Both halves are mandatory:**

- **Formally:** the precise definition, fully typed (domain/codomain, ambient space, what a measure is over, quantifiers). This is the statement the reader can *use* in a proof.
- **In words:** what the term *means* or *does* — the intuition, the picture, the role it plays. This is what lets the reader *recognise* when the term applies.

```markdown
> [!recall]- Absolutely continuous (μ ≪ ν)
> **Formally:** for measures $\mu, \nu$ on a measurable space $(X, \mathcal{F})$, $\mu \ll \nu$ means every $\nu$-null set is $\mu$-null: for all $A \in \mathcal{F}$, $\nu(A) = 0 \Rightarrow \mu(A) = 0$.
> **In words:** $\nu$ cannot be blind to anything $\mu$ sees — wherever $\mu$ puts mass, $\nu$ already puts some. This is exactly the condition under which $\mu$ has a density with respect to $\nu$. See [[Def - Absolute Continuity of Measures]].
```

Rules for recalls:

- **Title = the term, as it appears in the text**, with its notation in parentheses if it has a symbol. Use Unicode inside the title, never LaTeX: math in a callout *title* (fold line) renders inconsistently across Obsidian versions and themes — some show `$\sigma$` literally — so Unicode is the portable choice, exactly as for wikilink display text. The *body* renders LaTeX reliably and must use it. So `> [!recall]- σ-algebra`, not `> [!recall]- $\sigma$-algebra`; the body then uses `$\sigma$-algebra` freely. (This is a deliberate carve-out from `obsidian-patterns.md`, which says markdown renders in titles — see SKILL.md's precedence note.)
- **Put the wikilink to the atomic note inside the recall**, after the plain-language half. The recall is the just-in-time reminder; the atomic note is the full treatment.
- **Duplicate freely.** Repeat the recall the first time a term is used in each new section. A collapsed one-liner is cheaper to re-read than to hunt down. Do not make later sections depend on a recall the reader saw sections ago.
- **A recall is not a proof dependency you can wave at.** If the argument *uses a property* of the term (not just its definition), that property is a separate recall or an external-input callout — the recall states what the term *is*, not every theorem about it.
- **For a term the paper itself defines** (not a prerequisite), you still recall it at re-use across sections, but the primary treatment is the definition walk-through in the companion section plus its stub note — not a `[!recall]`.

---

## The external-input callout — `> [!cite]-`

For a result the paper **invokes but does not prove** (Rule 5). State it, type it, give its intuition, cite the source, and include the proof only when it is short or genuinely illuminating. The reader may then take it on faith with its precondition and conclusion stated exactly.

```markdown
> [!cite]- External input — Radon–Nikodym theorem
> **Statement (typed):** if $\mu, \nu$ are $\sigma$-finite measures on $(X, \mathcal{F})$ with $\mu \ll \nu$, then there is a $\nu$-almost-everywhere-unique measurable $f : X \to [0, \infty)$ with $\mu(A) = \int_A f \, d\nu$ for all $A \in \mathcal{F}$. The function $f$ is written $\frac{d\mu}{d\nu}$.
> **Why it's true (intuition):** absolute continuity forbids $\mu$ from putting mass where $\nu$ has none, so "how much $\mu$ per unit $\nu$" is well-defined pointwise; $f$ is that local exchange rate.
> **Source:** Folland, *Real Analysis*, Theorem 3.8. Take on faith with the precondition ($\sigma$-finite, $\mu \ll \nu$) and conclusion above; the proof (via the Hahn decomposition) is not needed here.
```

Rules for external-input callouts:

- **The `Statement (typed)` line is fully symbolic.** Both its precondition and its conclusion carry no bare jargon — every term in them is either floor-level or recalled/typed nearby.
- **Mark a genuine gap as a gap.** If the paper cites something you could not fully verify, or which is itself non-trivial and unproven in the notes, say so in a one-line Status and, if it matters, flag it with the uncertainty marker below.
- **Promote to an atomic `Thm -`/`Lemma -` note** when the reader will reuse the result — the callout is the point-of-use reminder, the atomic note is the reusable asset. Link them.
- **If the imported result's proof is short or illuminating, include it** in a nested `> > [!note]- Proof` inside the callout, or write it out as a `Lemma -` atomic note. Judgement call: illuminating means the proof teaches the reader something about the object, not merely that it is true.

---

## The uncertainty marker (Rule 6)

Flag anything you remain unsure of with a **visible** marker — never bury a doubt in smooth prose. Two forms:

**Inline**, for a local doubt (a constant, a hypothesis you suspect is stated loosely, a step you filled but could not fully verify):

```markdown
The normalising constant is $\frac{1}{2\pi}$ ⚠️ [unverified: the paper writes $\frac{1}{\pi}$ at eq. (4.2) but the $2\pi$ is needed for the density to integrate to 1; I could not reconcile this — flagged for the reader].
```

**Callout**, for a doubt worth separating from the flow:

```markdown
> [!warning] Verification note
> The paper states Lemma 4.3 with hypothesis "$P$ is faithful"; the proof appears to use only the weaker "$P$ has no extra independences among $\{X, Y, Z\}$". I have written the proof under the weaker hypothesis and flagged it; a specialist should confirm which the authors intend.
```

Rules for the uncertainty marker:

- **Use it whenever verification (Rule 6) did not fully close.** Supplying a fact you could not confirm, or filling a proof step you are not certain of, requires a flag. A wrong-but-confident statement is the worst outcome; a flagged uncertainty is an honest one.
- **Gather every flag into the Verification log** at the foot of the companion page, so the reader has one place to see everything outstanding.
- **The marker is `⚠️`** (a single emoji) inline, or a `> [!warning] Verification note` callout — both are visually loud in Obsidian and greppable. Do not use a plain parenthetical; it disappears.
