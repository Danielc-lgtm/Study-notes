# Recall and Reference Callouts

The paper-notes callouts that carry point-of-use recalls (Rule 2), imported external results (Rule 5), and flagged uncertainties (Rule 6). All are Obsidian callouts; syntax and nesting rules are in `obsidian-patterns.md`. `[!cite]` is a native Obsidian type (an alias of `quote`, rendered with a quote icon) and `[!warning]` is native. `[!recall]` is a custom label: Obsidian renders an unrecognised callout label with a default (pencil) icon and neutral styling, and the collapse marker (`-`/`+`) still works, so it is safe to use — if a guaranteed-styled type is ever wanted, `[!note]-` is the native fallback for a recall.

---

## The recall callout — `> [!recall]-`

The core device of the skill. Whenever a term or notation above the undergraduate floor is used, insert a recall **at the point of use**. It is collapsed (`-`) so a reader who knows the term is not slowed, and it must be **self-sufficient**: a reader who never clicks the wikilink still gets the formal content, a jargon-free paraphrase, *and* a concrete mental model.

**Three fields are mandatory:**

- **Formally:** the precise definition, fully typed (domain/codomain, ambient space, what a measure is over, quantifiers). This is the statement the reader can *use* in a proof.
- **In words:** what the term *means* or *does*, in plain language. **No above-floor jargon is allowed in this field.** If the paraphrase needs another above-floor term, either replace it with a floor-level phrase or nest a `> > [!recall]-` for it inside the current recall. This is what lets the reader *recognise* when the term applies.
- **Concretely:** a specific mental model the reader can hold in working memory — a small example (the $n=2$ case, the smallest non-trivial instance), a physical picture (a rubber sheet, a cylinder, a random walk on $\mathbb{Z}$), a computation the reader can do on paper, or a picture-in-words with explicit coordinates. This field must not be empty and must not consist solely of "See [[Def - X]]" — the wikilink is a supplement, not a substitute.

```markdown
> [!recall]- Absolutely continuous (μ ≪ ν)
> **Formally:** for measures $\mu, \nu$ on a measurable space $(X, \mathcal{F})$, $\mu \ll \nu$ means every $\nu$-null set is $\mu$-null: for all $A \in \mathcal{F}$, $\nu(A) = 0 \Rightarrow \mu(A) = 0$.
> **In words:** $\nu$ sees at least everything $\mu$ sees. Wherever $\mu$ puts positive mass, $\nu$ already put some.
> **Concretely:** on the real line, the standard normal probability measure $\gamma$ (bell curve) is absolutely continuous with respect to Lebesgue length $\lambda$: any set of length zero also has probability zero, because $\gamma$ has the density $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ against $\lambda$. But Lebesgue length is *not* absolutely continuous with respect to the point mass $\delta_0$ at zero: the set $\{0\}$ has $\delta_0(\{0\})=1\ne0$ yet length $0$. See [[Def - Absolute Continuity of Measures]].
```

Rules for recalls:

- **Title = the term, as it appears in the text**, with its notation in parentheses if it has a symbol. Use Unicode inside the title, never LaTeX: math in a callout *title* (fold line) renders inconsistently across Obsidian versions and themes — some show `$\sigma$` literally — so Unicode is the portable choice, exactly as for wikilink display text. The *body* renders LaTeX reliably and must use it. So `> [!recall]- σ-algebra`, not `> [!recall]- $\sigma$-algebra`; the body then uses `$\sigma$-algebra` freely.
- **Put the wikilink to the atomic note at the end of the Concretely field.** The recall is the just-in-time reminder; the atomic note is the full treatment.
- **Duplicate freely across sections.** Repeat the recall the first time a term is used in each new section. A collapsed recall is cheaper to re-read than to hunt down.
- **Length is not a virtue and not a vice.** A one-sentence recall (for a floor-adjacent term) is fine; an eight-line recall (for a genuinely alien object) is fine. What matters is that a floor reader closes the recall with a picture. Rule 7 (prose over compression) governs — err on the long side.
- **Nest freely.** When the "In words" field must use another above-floor term, nest a recall for it: `> > [!recall]- [nested term]` inside the outer recall. Two levels of nesting is the practical maximum; beyond that, restructure so each layer is its own top-level recall.
- **The three fields are non-negotiable.** Skipping "Concretely" because "the definition is basically the picture" is a bug — the *reader* does not have your familiarity. Empty fields, or fields containing only "See [[Def - X]]", fail the recall.
- **A recall is not a proof dependency you can wave at.** If the argument *uses a property* of the term (not just its definition), that property is a separate recall or an external-input callout — the recall states what the term *is*, not every theorem about it.
- **For a term the paper itself defines** (not a prerequisite), you still recall it at re-use across sections, but the primary treatment is the item's own atomic subpage.

### The jargon-in-plain-language failure — an anti-example and its fix

**Anti-example (from an early draft of this vault's Brownian-loops notes — do not do this):**

```markdown
> [!recall]- Free homotopy classes ↔ conjugacy classes; closed geodesics; fundamental strip
> **Formally:** free homotopy classes of oriented closed curves on X correspond bijectively to
>   conjugacy classes in Γ; a non-trivial non-peripheral class corresponds to a primitive
>   hyperbolic τ, conjugated to standard form τ:z↦e^ℓz with axis the imaginary half-line and
>   translation length ℓ; the class contains the unique closed geodesic γ of length ℓ. The class
>   winding m times is C_X(γ^m)↔[τ^m]_conj. The centraliser is C_Γ(τ^m)=⟨τ⟩, so
>   [τ^m]_conj = ⊔_{r∈Γ/⟨τ⟩} {rτ^m r^{-1}} (one conjugate per coset). Since Im(τz)=e^ℓ Im z,
>   the fundamental strip F_τ = {z : 1 ≤ Im z < e^ℓ} is a fundamental region for ⟨τ⟩.
> **In words:** "which hole, how many times" is recorded by a conjugacy class; each class has one
>   taut geodesic representative of a definite length; the strip is one period of the cylinder
>   that ⟨τ⟩ wraps up.
```

Why this fails: the "In words" field uses *another* pile of above-floor terms — "conjugacy class", "taut geodesic representative", "period of the cylinder that $\langle\tau\rangle$ wraps up". A floor reader cannot draw a picture, cannot name what the strip *is* as a set, cannot say what "primitive hyperbolic" excludes. There is no concrete instance the reader can compute on. The recall *looks* comprehensive because every symbol is typed and every term named — but it fails the actual test, which is *can the reader hold this in working memory*.

**Fix (the pattern to imitate):**

```markdown
> [!recall]- Free homotopy classes on X ↔ conjugacy classes in Γ
> **Formally:** two oriented closed curves on X are *freely homotopic* if one can be continuously
>   deformed into the other in X — no basepoint fixed. The set of free homotopy classes is in
>   bijection with the set of conjugacy classes of Γ (two group elements h, h' are conjugate if
>   h' = q h q^{-1} for some q ∈ Γ).
> **In words:** each loop on the surface "goes around some holes in some pattern"; two loops that
>   go around the same holes in the same pattern (allowing you to slide the starting point) are
>   in one class. On the algebraic side, Γ is the group of deck moves of the covering
>   ℍ^2 → X, and moving the starting point of a loop *by* a group element q changes its
>   recorded deck move from h to qhq^{-1} — that is exactly conjugation. So free homotopy
>   classes (basepoint-free geometry) ↔ conjugacy classes (basepoint-free algebra).
> **Concretely:** think of a torus T² = ℝ²/ℤ². Its deck group is Γ = ℤ² (translations by
>   integer vectors). A loop that goes once around the horizontal circle records the deck move
>   (1, 0); once around the vertical, (0, 1). Because ℤ² is abelian, its conjugacy classes are
>   singletons, so free homotopy classes are in bijection with ℤ² itself — every integer pair
>   (a, b) is one class, indexed by "a times around horizontally, b times around vertically". In
>   the hyperbolic case Γ is *not* abelian, so a conjugacy class is a genuine equivalence class
>   of many group elements — but the picture is the same: one class per topological type of loop.
> See [[Def - Closed Geodesics, Conjugacy Classes, and Translation Length]].
```

This recall passes: the "In words" field uses only "closed curve", "continuously deformed", "group element", "conjugation", "covering", "deck move" — all either floor-level or nested into their own recalls or given a picture. The "Concretely" field puts a *specific compact object* (the torus, $\mathbb{Z}^2$, the pair $(a, b)$) in the reader's head. A floor reader closes this recall able to answer "what is a free homotopy class?" without needing to click through.

**When a term genuinely needs its own space — the anti-example continues.** "Primitive hyperbolic $\tau$", "translation length", "fundamental strip" each carry as much content as the recall above; do *not* pack them into one recall. Give them separate top-level recalls (or one atomic subpage that treats them together), each with its own three fields. Cross-recall as needed.

---

## The external-input callout — `> [!cite]-`

For a result the paper **invokes but does not prove** (Rule 5). State it, type it, give its intuition, cite the source — and **prove it in full** on its own atomic `Thm -`/`Lemma -` page in the paper's `Subpages/` folder (or wikilink an existing vault page whose Formal Proof is complete), linked from the callout. The callout is the point-of-use record of *how the paper uses* the result; the proof lives on the atomic page, at the vault's proof floor (`prose-and-proof-standard.md` §6). The reader is never asked to take a result on faith: the vault-wide Proof Standard — every theorem mentioned is proved — applies to paper notes without exception.

```markdown
> [!cite]- External input — Radon–Nikodym theorem
> **Statement (typed):** if $\mu, \nu$ are $\sigma$-finite measures on $(X, \mathcal{F})$ with $\mu \ll \nu$, then there is a $\nu$-almost-everywhere-unique measurable $f : X \to [0, \infty)$ with $\mu(A) = \int_A f \, d\nu$ for all $A \in \mathcal{F}$. The function $f$ is written $\frac{d\mu}{d\nu}$.
> **Why it's true (intuition):** absolute continuity forbids $\mu$ from putting mass where $\nu$ has none, so "how much $\mu$ per unit $\nu$" is well-defined pointwise; $f$ is that local exchange rate.
> **Where the paper uses it:** to define the density of the loop measure against Lebesgue measure in §3.2.
> **Proof:** in full on [[Thm - Radon–Nikodym Theorem]] (via the Hahn decomposition; every step written out). **Source of the statement:** Folland, *Real Analysis*, Theorem 3.8.
```

Rules for external-input callouts:

- **The `Statement (typed)` line is fully symbolic.** Both its precondition and its conclusion carry no bare jargon — every term in them is either floor-level or recalled/typed nearby.
- **The `Proof` line always points at a complete proof.** Either an atomic page in `Subpages/` written for this paper, or an existing vault page whose `# Formal Proof` is complete. A callout whose proof line says "take on faith", "standard", or "see [source]" without a proved page behind it is a Proof Standard violation, not a shortcut.
- **The one exception — a genuinely book-length result** (of the order of fifty pages or more even in the most efficient textbook treatment). Such a result is used only in the `> [!warning] Imported without proof: …` callout form of `prose-and-proof-standard.md` §5 — exact statement, published source by section or page, one paragraph on the architecture of the proof, the reason it is imported — and is listed in the index page's Verification log. This is a last resort for a handful of results, never a category for anything long.
- **Mark a genuine gap as a gap.** If the paper cites something you could not fully verify, or whose proof you had to supply from your own knowledge, say so in a one-line Status and, if it matters, flag it with the uncertainty marker below.
- **Promote to an atomic `Thm -`/`Lemma -` note is not optional** — it is where the proof lives; the callout and the note link each other.

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
