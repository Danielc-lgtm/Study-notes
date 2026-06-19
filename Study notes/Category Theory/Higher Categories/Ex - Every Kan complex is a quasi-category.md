---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Kan Complex and the Nerve"
  - "Def - Quasi-Category"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that every [[Def - Kan Complex and the Nerve|Kan complex]] is a [[Def - Quasi-Category|quasi-category]]. Conclude that Kan complexes are exactly the **∞-groupoids** — the quasi-categories in which every morphism is invertible — and explain why the converse fails: a quasi-category need not be a Kan complex. Give the example of a [[Def - Kan Complex and the Nerve|nerve]] $N(\mathcal{C})$ for a category $\mathcal{C}$ with a non-invertible morphism.

**Recall:**

A [[Def - Kan Complex and the Nerve|Kan complex]] is a [[Def - Simplicial Set|simplicial set]] with the right lifting property against *all* horn inclusions $\Lambda^n_i\hookrightarrow\Delta^n$ ($0\le i\le n$). A [[Def - Quasi-Category|quasi-category]] requires fillers only for the *inner* horns ($0<i<n$). The horns with $i=0$ or $i=n$ are the **outer** horns; filling an outer horn $\Lambda^2_0$ given $f:x\to y$, $h:x\to z$ amounts to producing an arrow $y\to z$ realising $h$ as $(\cdot)\circ f$, which (for the homotopy category) requires $f$ to be invertible.

---

# Convergent Strategy

**Problem class:** This is a "containment of conditions" problem — the simplest kind of "fill" verification in the topic page's [[Higher Categories — 2-Categories, Enrichment, and Quasi-Categories#Sources and Targets|Sources and Targets]]. The routine is to observe that the quasi-category condition is *weaker* than the Kan condition (fewer horns to fill), so Kan implies quasi-category immediately.

**Assumption pattern:** The recognisable feature is the inner/outer split of horns. The Kan condition demands *all* horns fill; the quasi-category condition demands only the *inner* ones. Since inner horns are a subset of all horns, the implication is set-theoretic containment.

**Theorem routing:** The forward implication is immediate from the definitions. The "∞-groupoid" identification and the converse failure route through the geometric meaning of *outer* horn-filling (invertibility), made precise via the [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] (where outer fillers give inverses) and the [[Thm - The Nerve is Fully Faithful and Characterized by Unique Inner Horn Fillers|nerve characterisation]] (nerves with non-invertible arrows fail outer filling).

**Key decision point:** The non-obvious choice is articulating *why* the converse fails — not merely asserting it. The decision is to exhibit the geometric content of outer horns: they encode inversion, so a quasi-category with a non-invertible morphism (e.g. the nerve of a poset with a strict inequality) fills inner horns but not outer ones, hence is a quasi-category that is not Kan.

---

# Legal Operations Used

1. **Operation 4 (apply the nerve / horn-filling characterisation).** Inner horns ⊆ all horns gives Kan ⟹ quasi-category; the inner/outer distinction gives the ∞-category / ∞-groupoid distinction.

2. **Operation 3 (translate horn-filling into composites/inverses).** Outer-horn filling corresponds to invertibility of morphisms, used to identify Kan complexes with ∞-groupoids and to show the converse fails.

---

# Hints

> [!note]- Hint 1
> Compare the two conditions. The Kan condition quantifies over $0\le i\le n$; the quasi-category condition over $0<i<n$. How are the two sets of horns related?

> [!note]- Hint 2
> Inner horns are a *subset* of all horns. So "fill all horns" trivially implies "fill the inner ones". That is the entire forward implication.

> [!note]- Hint 3
> For the converse: outer-horn filling encodes invertibility. Take $\mathcal{C} = [1] = (0\to 1)$, a poset with one non-identity arrow. Its nerve $\Delta^1$ is a quasi-category (it is a nerve), but the outer horn $\Lambda^2_0$ formed by the arrow $0\to 1$ and $\mathrm{id}_0$ has no filler — there is no arrow $1\to 0$. So $\Delta^1$ is a quasi-category that is not Kan.

---

# Solution

The plan: Step 1 proves Kan ⟹ quasi-category by containment. Step 2 identifies Kan complexes with ∞-groupoids via outer-horn = invertibility. Step 3 exhibits a quasi-category that is not Kan, proving the converse fails.

**Step 1: Kan implies quasi-category.** Inner horns are among all horns, so a simplicial set filling all horns fills the inner ones; every [[Def - Kan Complex and the Nerve|Kan complex]] is a [[Def - Quasi-Category|quasi-category]].

> [!note]- Derivation
> The Kan condition is: for *all* $n\ge 1$ and *all* $0\le i\le n$, every map $\Lambda^n_i\to X$ extends to $\Delta^n\to X$. The quasi-category condition is the same statement restricted to $0<i<n$ (inner horns). The set of inner horns $\{\Lambda^n_i : 0<i<n\}$ is a subset of the set of all horns $\{\Lambda^n_i : 0\le i\le n\}$. Therefore "$X$ fills every horn" implies "$X$ fills every inner horn", i.e. Kan $\Rightarrow$ quasi-category. The implication is pure logic — a universal statement over a larger index set implies the same over a smaller one.

**Step 2: Kan complexes are the ∞-groupoids.** Outer-horn filling is exactly invertibility of morphisms; so a Kan complex is a quasi-category in which every morphism is invertible — an ∞-groupoid.

> [!note]- Derivation
> By Step 1 a Kan complex is a quasi-category, so it has a [[Thm - The Homotopy Category of a Quasi-Category|homotopy category]] $\mathrm{ho}(X)$. The extra content of the Kan condition over the quasi-category condition is precisely the *outer* horns. Filling the outer horn $\Lambda^2_0$ — given $f:x\to y$ and $\mathrm{id}_x:x\to x$ — produces an edge $g:y\to x$ with $[g]\circ[f]=[\mathrm{id}_x]$, a left inverse; the outer horn $\Lambda^2_2$ gives a right inverse. So in a Kan complex every morphism becomes invertible in $\mathrm{ho}(X)$, making $\mathrm{ho}(X)$ a [[Def - Groupoid|groupoid]] and $X$ an **∞-groupoid**. Conversely, an $\infty$-category in which every morphism is invertible (an $\infty$-groupoid) fills outer horns as well, hence is Kan. So Kan complexes $=$ ∞-groupoids.

**Step 3: The converse fails.** A nerve $N(\mathcal{C})$ with a non-invertible arrow is a quasi-category that is not Kan; the simplest example is $\mathcal{C} = [1]$, $N([1]) = \Delta^1$.

> [!note]- Derivation
> Take $\mathcal{C} = [1] = (0\to 1)$, the poset with a single non-identity arrow $u:0\to 1$ that has no inverse. By [[Ex - The nerve of a category is a quasi-category|the previous exercise]], $N([1]) = \Delta^1$ is a quasi-category (all inner horns fill, uniquely). But it is *not* a Kan complex: consider the outer horn $\Lambda^2_0\to\Delta^1$ with $d^2 = u$ (the edge $0\to 1$) and $d^1 = \mathrm{id}_0$ (the degenerate edge $0\to 0$). A filler would be a $2$-simplex of $\Delta^1$ whose remaining face $d^0$ is an edge $1\to 0$; but $\Delta^1 = N([1])$ has *no* edge $1\to 0$, since $[1]$ has no arrow $1\to 0$. So the outer horn cannot be filled, and $\Delta^1$ is a quasi-category that is not Kan. The obstruction is exactly the non-invertibility of $u$.

> [!note]- Complete formal solution
> *Kan $\Rightarrow$ quasi-category:* inner horns ($0<i<n$) are a subset of all horns ($0\le i\le n$), so filling all horns implies filling the inner ones (Step 1).
>
> *Kan $=$ ∞-groupoid:* the extra outer horns encode invertibility; filling $\Lambda^2_0$ and $\Lambda^2_2$ produces left and right inverses, so every morphism of $\mathrm{ho}(X)$ is invertible, making $X$ an ∞-groupoid, and conversely (Step 2).
>
> *Converse fails:* $\Delta^1 = N([1])$ is a quasi-category (inner horns fill) but not Kan — the outer horn $\Lambda^2_0$ given by the non-invertible arrow $0\to 1$ and $\mathrm{id}_0$ has no filler, as there is no arrow $1\to 0$ (Step 3). $\quad\blacksquare$

---

# Key Takeaways

**The inner/outer horn distinction *is* the ∞-category / ∞-groupoid distinction — this is the single most important taxonomy in the chapter.** Filling inner horns gives composition; filling outer horns gives inversion. A quasi-category (inner only) is an ∞-category with possibly non-invertible morphisms; a Kan complex (all horns) is an ∞-groupoid where everything inverts. The reusable recognition: "all horns fill" should immediately read "every morphism is invertible — this is a space / ∞-groupoid", while "only inner horns fill" reads "this is a genuine $\infty$-category with directionality". Nerves of non-groupoids and singular complexes of spaces sit on opposite sides of exactly this line.

**Weakening a lifting condition by restricting the index set is the cheapest kind of implication — and it pervades model-category arguments.** Kan ⟹ quasi-category is nothing but "a universal statement over a bigger set implies it over a smaller set". This pattern — defining classes of objects by lifting against *some* maps, and comparing them by comparing the sets of maps — is the entire mechanism of [[Def - Lifting Property and the Retract Argument|lifting properties]] in model categories. The trigger to carry forward: whenever two structures are defined by lifting against nested sets of maps, the structure with the larger set is the stronger (more special) one, and the implication is immediate.

**The converse failing is not a defect but the whole reason ∞-categories exist.** If every quasi-category were a Kan complex, $\infty$-category theory would collapse to the homotopy theory of spaces and could not model categories with non-invertible morphisms. The example $\Delta^1$ — a quasi-category that is not Kan because its single arrow has no inverse — is the minimal witness that the two notions genuinely differ. This is exactly why we want quasi-categories rather than Kan complexes as the model of $\infty$-*categories*: they retain directionality. The diagnostic: to show a quasi-category is not Kan, exhibit a non-invertible morphism and the outer horn it fails to fill.
