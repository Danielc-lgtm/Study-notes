---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Homotopy Hypothesis"
  - "Def - Kan Complex and the Nerve"
  - "Def - Simplicial Set"
  - "Def - Topological Space"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T$ be a **[[Def - Topological Space|topological space]]** and $\mathrm{Sing}(T)$ its **singular [[Def - Simplicial Set|simplicial set]]**, with $\mathrm{Sing}(T)_n = \{\text{continuous maps } |\Delta^n| \to T\}$. Prove that $\mathrm{Sing}(T)$ is a **[[Def - Kan Complex and the Nerve|Kan complex]]**: every horn $\Lambda^n_i \to \mathrm{Sing}(T)$, for *all* $0 \le i \le n$ (inner *and* outer), has a filler $\Delta^n \to \mathrm{Sing}(T)$. Explain why this is the geometric fact that makes $\mathrm{Sing}(T)$ an *$\infty$-groupoid*, and hence why it underpins the **[[Thm - The Homotopy Hypothesis|homotopy hypothesis]]** in the simplicial model — and why the *all-horns* (not merely inner-horns) condition is what distinguishes an $\infty$-groupoid from a general $(\infty,1)$-category.

**Recall:**

![[Def - Kan Complex and the Nerve#The Definition]]

The **geometric realisation** of the standard $n$-simplex is $|\Delta^n| = \{(t_0, \dots, t_n) \in \mathbb{R}^{n+1} : t_j \ge 0,\ \sum_j t_j = 1\}$. Its $i$th **face** is the subset $\{t_i = 0\}$. The geometric **horn** $|\Lambda^n_i|$ is the union of all faces except the $i$th. By the realisation–singular **adjunction**, a map of simplicial sets $K \to \mathrm{Sing}(T)$ is the same as a continuous map $|K| \to T$.

---

# Convergent Strategy

**Problem class:** This is an *adjunction-plus-geometry* problem: translate a lifting problem of simplicial sets into a continuous-extension problem of spaces via the realisation–singular adjunction, then solve the extension problem by a deformation retraction. The routine is "adjoint the problem to topology, then retract".

**Assumption pattern:** The only assumption is that $T$ is an arbitrary topological space — no hypotheses needed, which is itself the point: $\mathrm{Sing}(T)$ is a Kan complex *for every* $T$. The lever is purely the geometry of the simplex: $|\Lambda^n_i|$ is a deformation retract of $|\Delta^n|$.

**Theorem routing:** The route is: a horn $\Lambda^n_i \to \mathrm{Sing}(T)$ adjuncts to a continuous map $g : |\Lambda^n_i| \to T$ ([[Thm - The Homotopy Hypothesis|realisation–singular adjunction]]); the geometric horn deformation-retracts onto the solid simplex, giving a retraction $r : |\Delta^n| \to |\Lambda^n_i|$; then $g \circ r : |\Delta^n| \to T$ extends $g$, and its adjunct is the required simplicial filler. The retraction exists for *every* $i$, which is exactly why all horns — inner and outer — fill.

**Key decision point:** The non-obvious recognition is that the *all-horns* condition holds because the retraction $|\Delta^n| \to |\Lambda^n_i|$ exists for *every* face index $i$, with no preference for inner. Contrast this with the [[Def - Quasi-Category|quasi-category]] case, where one only demands inner horns: the difference is not in $\mathrm{Sing}(T)$ (which fills all horns) but in what one *requires* of a general simplicial set. The geometry gives all horns; the choice to demand only inner ones is what builds in non-invertibility for general $\infty$-categories.

---

# Legal Operations Used

1. **Operation 7 from the topic page (build the fundamental $\infty$-groupoid of a space).** $\mathrm{Sing}(T)$ *is* the fundamental $\infty$-groupoid $\Pi_\infty(T)$, and showing it is a Kan complex is showing it is an $\infty$-groupoid.

2. **Operation 2 from the topic page (horn-filling as the simplicial composition condition), in its all-horns form.** Filling all horns, not just inner ones, is the simplicial expression of "all morphisms invert".

3. **Operation 8 from the topic page (recover/identify a known structure).** We identify $\mathrm{Sing}(T)$ as the groupoidal ($(\infty,0)$) case, locating the homotopy hypothesis as the boundary of the inner/outer-horn picture.

---

# Hints

> [!note]- Hint 1
> Do not work with simplicial sets directly. Use the realisation–singular adjunction to turn the lifting problem "$\Lambda^n_i \to \mathrm{Sing}(T)$ extends to $\Delta^n$" into a continuous-extension problem "$|\Lambda^n_i| \to T$ extends to $|\Delta^n|$".

> [!note]- Hint 2
> The geometric horn $|\Lambda^n_i|$ — all faces of the solid simplex except the $i$th — sits inside the solid $|\Delta^n|$. Is it a retract? Project radially from a well-chosen point of the *missing* $i$th face.

> [!note]- Hint 3
> If $r : |\Delta^n| \to |\Lambda^n_i|$ is a retraction (so $r$ restricted to $|\Lambda^n_i|$ is the identity), then for any $g : |\Lambda^n_i| \to T$ the composite $g \circ r : |\Delta^n| \to T$ restricts to $g$ on the horn — that is the extension. Adjoint it back.

> [!note]- Hint 4
> Why "all $i$" and not just inner $i$? Because the radial-projection retraction exists for *every* face index, inner or outer. The inner/outer distinction is a restriction one *imposes* on general simplicial sets to allow non-invertible morphisms; $\mathrm{Sing}(T)$, having topological inverses (run a path backwards), satisfies the stronger all-horns condition automatically.

---

# Solution

The proof is two lines of substance wrapped in an adjunction. Step 1 adjuncts the lifting problem to topology. Step 2 solves it by a deformation retraction. Step 3 reads off the consequence for the homotopy hypothesis.

**Step 1: adjoint the horn-filling problem to a topological extension problem.**

> [!note]- Derivation
> A horn $\Lambda^n_i \to \mathrm{Sing}(T)$ is, by the realisation–singular adjunction $|{-}| \dashv \mathrm{Sing}$, the same datum as a continuous map $g : |\Lambda^n_i| \to T$. A filler $\Delta^n \to \mathrm{Sing}(T)$ extending it is, again by adjunction, the same as a continuous map $\bar g : |\Delta^n| \to T$ with $\bar g|_{|\Lambda^n_i|} = g$. So the entire problem becomes: *every continuous map out of the geometric horn extends continuously over the solid simplex.*

**Step 2: the geometric horn is a deformation retract of the solid simplex.**

> [!note]- Derivation
> Realise $|\Delta^n| = \{(t_0,\dots,t_n) : t_j \ge 0,\ \sum t_j = 1\}$. The $i$th face is $\{t_i = 0\}$; the horn $|\Lambda^n_i|$ is the union of all faces $\{t_j = 0\}$ for $j \ne i$. Pick the point $c$ to be the barycentre of the *missing* $i$th face — the centre of $\{t_i = 0\}$ — pushed slightly toward the vertex $e_i$ opposite that face; concretely take $c = e_i$, the $i$th vertex (where $t_i = 1$, all other coordinates $0$). The vertex $e_i$ lies on every face $\{t_j = 0\}$, $j \ne i$, so $e_i \in |\Lambda^n_i|$. Radial projection *away from $e_i$* onto the union of the other faces defines a continuous retraction $r : |\Delta^n| \to |\Lambda^n_i|$: a point $p \ne e_i$ is sent along the ray from $e_i$ through $p$ to where it first meets $|\Lambda^n_i|$, and points of $|\Lambda^n_i|$ are fixed. (The straight-line homotopy $H(p,s) = (1-s)p + s\,r(p)$ from $\mathrm{id}$ to $\iota\circ r$ shows it is a strong deformation retraction, fixing the horn throughout.) Crucially, this construction works for *every* $i$ — there is nothing special about inner $i$.
>
> Now set $\bar g := g \circ r : |\Delta^n| \to T$. For $p \in |\Lambda^n_i|$, $r(p) = p$, so $\bar g(p) = g(p)$; hence $\bar g$ extends $g$. Adjointing back, we obtain the simplicial filler $\Delta^n \to \mathrm{Sing}(T)$. Since this works for all $n \ge 1$ and all $0 \le i \le n$, $\mathrm{Sing}(T)$ satisfies the full Kan condition.

**Step 3: consequence for the homotopy hypothesis.**

> [!note]- Derivation
> A [[Def - Kan Complex and the Nerve|Kan complex]] is the simplicial model of an *$\infty$-groupoid*: filling *outer* horns ($\Lambda^n_0$, $\Lambda^n_n$) is the simplicial form of *inverting* morphisms, so "all horns fill" means "all morphisms are invertible". Therefore $\mathrm{Sing}(T) = \Pi_\infty(T)$ is an $\infty$-groupoid for every space $T$ — its $1$-cells (paths) invert because paths run backwards, its $2$-cells (homotopies) invert, and so on. This is precisely the content the [[Thm - The Homotopy Hypothesis|homotopy hypothesis]] needs on the topological side: the functor $\mathrm{Sing}$ lands in $\infty$-groupoids, and Milnor's theorem then upgrades $|{-}| \dashv \mathrm{Sing}$ to a Quillen equivalence, identifying $\infty$-groupoids (Kan complexes) with homotopy types. The all-horns condition holding *automatically* for $\mathrm{Sing}(T)$ is exactly why the simplicial homotopy hypothesis is a theorem rather than a conjecture.

> [!note]- Complete formal solution
> Let $T$ be a space and $0 \le i \le n$. A horn $\Lambda^n_i \to \mathrm{Sing}(T)$ corresponds by the adjunction $|{-}|\dashv\mathrm{Sing}$ to a continuous $g : |\Lambda^n_i| \to T$. The vertex $e_i \in |\Delta^n|$ lies in every face $\{t_j=0\}$ with $j\ne i$, hence in $|\Lambda^n_i|$; radial projection away from $e_i$ gives a strong deformation retraction $r:|\Delta^n|\to|\Lambda^n_i|$ (with straight-line homotopy $H(p,s)=(1-s)p+s\,r(p)$). Then $\bar g = g\circ r : |\Delta^n|\to T$ is continuous and restricts to $g$ on the horn; its adjunct is a filler $\Delta^n \to \mathrm{Sing}(T)$. As $n, i$ were arbitrary, $\mathrm{Sing}(T)$ fills all horns and is a Kan complex. Filling all horns (including outer) is the simplicial form of invertibility, so $\mathrm{Sing}(T)$ is an $\infty$-groupoid; this is the topological input to the homotopy hypothesis. $\blacksquare$

---

# Key Takeaways

**Adjoint the lifting problem, then retract.** The reusable technique is the two-move pattern: (1) use the realisation–singular adjunction to convert a simplicial lifting problem into a continuous-extension problem, and (2) solve the extension by exhibiting the sub-object as a retract. This pattern recurs throughout the homotopy theory of simplicial sets — proving $\mathrm{Sing}(T)$ fibrant, proving fibrations are Serre fibrations, computing homotopy groups — because the adjunction is the universal translator between combinatorics and topology, and retractions are the universal source of extensions. The trigger is "extend a map off a sub-simplicial-set", and the reaction is "adjoint to spaces and look for a deformation retraction".

**Outer-horn filling is invertibility; all-horns is groupoidal.** The conceptual payoff is the precise dictionary: inner horns encode *composition* (which any $(\infty,1)$-category has), while outer horns encode *invertibility* (which only $\infty$-groupoids have). $\mathrm{Sing}(T)$ fills *all* horns because a space has inverses for free — paths reverse — so it is groupoidal. A general [[Def - Quasi-Category|quasi-category]] is defined to fill only *inner* horns precisely so that it may have non-invertible morphisms and thereby generalise ordinary categories rather than groupoids. Internalising "outer horn $=$ invert" lets you read off, from a horn-filling condition alone, whether you are looking at an $\infty$-category or an $\infty$-groupoid — and it locates the homotopy hypothesis as the all-horns boundary of the inner-horn world.

**"For every $T$" is the real strength.** It is worth dwelling on the fact that no hypothesis on $T$ was used: $\mathrm{Sing}(T)$ is a Kan complex for *any* topological space, however pathological. This is why the simplicial model of $\infty$-groupoids is so robust and why the homotopy hypothesis is *provable* there: the groupoidal structure is supplied uniformly by the geometry of the simplex, not by any niceness of $T$. The contrast with the algebraic (globular) definitions is exactly here — there, invertibility must be *constructed* cell by cell and *proven* to cohere, with no free geometric retraction to lean on, which is why the algebraic homotopy hypothesis remains open. Recognising that "the geometry gives it for free" versus "you must earn it algebraically" is the key to understanding why one side of the hypothesis is a theorem and the other a conjecture.
