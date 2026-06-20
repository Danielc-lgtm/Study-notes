---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - Baez-Dolan Opetopic Weak n-Categories"
  - "Def - Opetopic Set"
  - "Def - Limit and Colimit"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Explain, with a concrete low-dimensional example, why the opetopic definition of weak $n$-category requires **universal** fillers and not merely the existence of *some* filler for each niche. Exhibit an [[Def - Opetopic Set|opetopic set]] in which every niche has at least one filler but the fillers are not universal, and show that it fails to be a category (composition is not well-defined / not unique). Then identify what goes wrong if a niche has *no* filler at all (composition does not exist), and summarise the three regimes: no filler, non-universal filler, universal filler.

**Recall:**

![[Thm - Baez-Dolan Opetopic Weak n-Categories#Statement]]

A **niche** is a many-in, one-out configuration awaiting a composite. A **filler** is any cell capping the niche; a **universal filler** is one that is initial/terminal among all fillers — characterised by a [[Def - Limit and Colimit|universal property]], hence essentially unique. The opetopic definition of weak $n$-category demands a *universal* filler for every niche, which is the chosen composite.

---

# Convergent Strategy

**Problem class:** This is a *stress-test-the-definition* problem — it probes why a specific hypothesis (universality) cannot be weakened, by exhibiting the failure mode when it is. This is the dual of the validation exercises: instead of confirming the definition reproduces known cases, we confirm that *removing* universality breaks it.

**Assumption pattern:** The setup deliberately *violates* the universality assumption while keeping mere existence. The pattern to recognise is that "a filler exists" gives a composite that is *not pinned down* — multiple non-isomorphic fillers mean multiple candidate composites, so composition is multivalued, exactly the disease universality cures.

**Theorem routing:** We route through the calibration theorem ([[Thm - Baez-Dolan Opetopic Weak n-Categories|Baez–Dolan opetopic weak n-categories]]): its $n = 1$ case shows universal fillers give a *unique* composite. We contrast with the merely-existent case, where Lemma 1's essential uniqueness is unavailable because the filler is not universal. The contrast is with the [[Def - Limit and Colimit|universal-cone]] notion.

**Key decision point:** The non-obvious choice is to build the counterexample by supplying *two distinct, non-isomorphic* fillers for a single niche, neither universal, and to observe that there is then no canonical composite. The tempting error is to think "existence is enough, just pick one" — but a non-canonical choice is not functorial, breaks associativity, and depends on arbitrary selection, which is exactly why universality is required.

---

# Legal Operations Used

1. **Operation 5 (recognise a niche and demand a filler)** from the topic page — here examined critically: we ask what "demand a filler" must mean (universal, not merely existent) for composition to be well-defined.

2. **Operation 6 (identify a universal property in lieu of an equation)** from the topic page. The example shows that *without* the universal property, the would-be composite is not pinned down, so no equation or canonical operation survives.

---

# Hints

> [!note]- Hint 1
> Build a small opetopic set with objects $a, b, c$, arrows $f : a \to b$, $g : b \to c$, and *two distinct* $1$-cells $h_1, h_2 : a \to c$, each with a $2$-cell filling the niche "$g$ after $f$" but with no $2$-cell relating $h_1$ and $h_2$. Both $h_1$ and $h_2$ are fillers; neither is universal.

> [!note]- Hint 2
> A universal filler would be initial among fillers: there would be a (unique) $2$-cell from it to every other filler. With $h_1, h_2$ unrelated, neither has a $2$-cell to the other, so neither is universal. Hence "the composite $g \circ f$" is ambiguous — is it $h_1$ or $h_2$?

> [!note]- Hint 3
> Now consider the opposite extreme: a niche with *no* filler at all. Then the string $f, g$ has no composite whatsoever, so the structure is not even a category. Summarise: no filler = no composite; non-universal filler = ambiguous composite; universal filler = unique canonical composite.

---

# Solution

The route is to build a concrete opetopic set where a niche has two unrelated fillers, show neither is universal and composition is ambiguous, then contrast with the no-filler and universal-filler regimes.

**Step 1: An opetopic set with a niche having two non-universal fillers.**

> [!note]- Derivation
> Take objects $a, b, c$; $1$-cells $f : a \to b$ and $g : b \to c$; and two distinct $1$-cells $h_1, h_2 : a \to c$. Add a $2$-cell $\theta_1$ filling the arity-$2$ niche with source $f, g$ and target $h_1$, and another $2$-cell $\theta_2$ filling the *same* niche (source $f, g$) but with target $h_2$. Include no $3$-cells and no $2$-cells relating $h_1$ to $h_2$. This is a perfectly good [[Def - Opetopic Set|opetopic set]] (a presheaf on $\mathbb{O}$): all boundaries match, all restrictions are defined.
>
> The niche "compose $f$ then $g$" has *two* fillers, $\theta_1$ (giving $h_1$) and $\theta_2$ (giving $h_2$). Existence of a filler holds. But which is the composite $g \circ f$?

**Step 2: Neither filler is universal, so composition is ambiguous.**

> [!note]- Derivation
> A universal filler of the niche would be *initial* among fillers: from it there would be a unique mediating cell (a $2$-cell, since we are testing universality of a $2$-cell) to *every* other filler of the niche. For $\theta_1$ to be universal there must be a mediating cell $\theta_1 \to \theta_2$; for $\theta_2$ to be universal, one $\theta_2 \to \theta_1$. We included no such cells (no $3$-cells, no $2$-cells between $h_1, h_2$), so **neither $\theta_1$ nor $\theta_2$ is universal**.
>
> Consequently there is no canonical composite: the niche "$g$ after $f$" has two equally-valid, non-comparable candidate outputs $h_1, h_2$. Composition is *multivalued*. By the $n = 1$ case of [[Thm - Baez-Dolan Opetopic Weak n-Categories|the calibration theorem]], a category requires a *unique* composite, which comes precisely from a universal filler (Lemma 1 forces uniqueness *only when the filler is universal*). With mere existence, Lemma 1 does not apply — there is nothing to force $h_1 = h_2$ — so $X$ is **not** a category. Choosing one of $h_1, h_2$ arbitrarily is not functorial and breaks associativity, because the choice cannot be made coherently across all niches.

**Step 3: The three regimes.**

> [!note]- Derivation
> - **No filler.** If the niche on $f, g$ has *no* filler, then the string $f, g$ has no composite at all. The structure is not a category (and not a weak $n$-category): composition does not exist. This is the failure of *existence*.
> - **Non-universal filler (Step 1–2).** If the niche has fillers but none universal, the composite *exists but is ambiguous* — multivalued, non-canonical. The structure is still not a category, because there is no well-defined composition. This is the failure of *uniqueness/canonicity*.
> - **Universal filler.** If the niche has a universal filler, the composite is canonical and (at the appropriate truncation) unique. By [[Thm - Baez-Dolan Opetopic Weak n-Categories|the calibration theorem]] this yields a category at $n = 1$ and a bicategory at $n = 2$. This is the correct regime.
>
> The opetopic definition demands the third regime — universal fillers — precisely because the first fails to give composites and the second fails to give *canonical* ones. Universality is the unique condition that supplies a composite *and* pins it down.

> [!note]- Complete formal solution
> Build the [[Def - Opetopic Set|opetopic set]] $X$ with objects $a, b, c$; arrows $f : a \to b$, $g : b \to c$, and $h_1, h_2 : a \to c$ ($h_1 \neq h_2$); $2$-cells $\theta_1 : (f, g) \Rightarrow h_1$ and $\theta_2 : (f, g) \Rightarrow h_2$ filling the *same* arity-$2$ niche; no cells relating $h_1, h_2$. Every niche on $f, g$ has fillers ($\theta_1, \theta_2$), so existence holds. But a universal filler must be initial among fillers (a unique mediating cell to every other filler); since no cell relates $\theta_1$ and $\theta_2$, neither is universal. Hence the composite $g \circ f$ is ambiguous (could be $h_1$ or $h_2$), composition is multivalued, and by the $n=1$ case of [[Thm - Baez-Dolan Opetopic Weak n-Categories|the calibration theorem]] $X$ is not a category. The three regimes: no filler $\Rightarrow$ no composite; non-universal filler $\Rightarrow$ ambiguous composite; universal filler $\Rightarrow$ canonical composite (category at $n=1$, bicategory at $n=2$). $\blacksquare$

---

# Key Takeaways

**Existence gives a composite; universality gives *the* composite.** The crux of the whole opetopic definition is that demanding mere existence of fillers is not enough — it yields a multivalued, non-canonical composition that fails to be a category. Only universality pins the composite down. The reusable insight is that "there exists" and "there exists a universal one" are very different hypotheses: the first allows arbitrary, incoherent choices; the second forces a canonical, essentially-unique answer that composes well. The trigger is any definition phrased with fillers, lifts, or extensions: check whether *existence* or *universal existence* is demanded, because the two give wildly different theories — a Kan fibration (mere lifts) versus a limit (universal cone) is the same distinction.

**Non-canonical choice breaks coherence, not just uniqueness.** It is tempting to repair the non-universal example by simply *choosing* one filler per niche. This fails not only because the choice is arbitrary but because it cannot be made *coherently*: the chosen composites will not satisfy associativity unless the choices are compatible across all niches, and there is no mechanism forcing compatibility without universality. The reusable principle is that arbitrary choices are the enemy of coherence: any structure that depends on un-forced selections will fail higher coherence laws. The trigger is any construction requiring a choice (a section, a representative, a composite); ask whether the choice is forced by a universal property — if not, expect coherence to break downstream. This is why the axiom of choice is so delicate in homotopical settings.

**Stress-testing a hypothesis by removing it is how you understand why it is there.** The methodological lesson is that to understand why a definition demands universality, you remove it and watch the structure break. The trigger is any time a definition includes a strong-looking condition (universal, contractible, unique-up-to-coherent-iso): construct the object that satisfies the weaker condition and exhibit the pathology. Here, mere existence gives multivalued composition; this *explains* universality rather than merely stating it. This dual of validation — confirming a hypothesis is necessary, not just sufficient — is what gives a definition its full meaning, and it generalises across every "filler/lifting condition" definition in higher category theory and homotopy theory. See [[Ex - At n equals 1 the universal filler condition gives a category]] and [[Ex - At n equals 2 the universal fillers reproduce a bicategory]] for the correct (universal) regime in action.
