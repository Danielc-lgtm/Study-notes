---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Transfinite Composition and Smallness"
  - "Def - Relative Cell Complex"
  - "Def - Topological Space"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $A$ be a **compact** topological space. Show that $A$ is [[Def - Transfinite Composition and Smallness|small]] relative to the relative cell complexes built from the set $I = \{S^{n-1}\hookrightarrow D^n : n\geq 0\}$ in $\mathbf{Top}$. Concretely, prove that for any $\lambda$-sequence $X_0\to X_1\to\cdots$ in which each map $X_\beta\to X_{\beta+1}$ is an $I$-cell map (an attachment of disks along their boundary spheres), every continuous map $g : A\to \mathrm{colim}_{\beta<\lambda} X_\beta$ factors through some bounded stage $X_\beta$, and the factorization is essentially unique. Identify which property of the cell attachments (besides compactness of $A$) the argument relies on.

**Recall:**

![[Def - Transfinite Composition and Smallness#The Definition]]

A [[Def - Relative Cell Complex|relative I-cell complex]] is a transfinite composite of pushouts of coproducts of the boundary inclusions $S^{n-1}\hookrightarrow D^n$; geometrically, each stage attaches a collection of disks $D^n$ to the previous space along attaching maps $S^{n-1}\to X_\beta$. A space $A$ is **compact** if every open cover has a finite subcover; equivalently every net has a convergent subnet.

---

# Convergent Strategy

**Problem class:** This is a smallness-certification problem — the third recurring target of the chapter, establishing the termination hypothesis that the [[Thm - The Small Object Argument|small object argument]] requires. It is the topological prototype: the route is always to convert a topological finiteness property (compactness) into the categorical bounded-factorization property (smallness).

**Assumption pattern:** The decisive assumptions are (a) compactness of $A$ and (b) that the cell attachments are *closed* inclusions, so that the colimit is built by attaching closed cells and a compact subset can only meet finitely many of them. Compactness alone is not enough; you need the colimit topology to be the right one — the weak (colimit) topology in which a set is closed iff its preimage at every stage is closed — which is exactly what makes "compact image meets finitely many cells" true.

**Theorem routing:** The route is: a continuous image of a compact space is compact (so $g(A)$ is compact); a compact subset of a transfinite cell complex (with the colimit topology) is contained in a finite subcomplex, hence lands in a bounded stage; therefore $g$ factors through that stage. Essential uniqueness follows because two stage-factorizations agreeing in the colimit must agree at a common later stage, again by compactness of $A$.

**Key decision point:** The non-obvious step is recognizing that the relevant finiteness is "$g(A)$ meets only finitely many *cells*," not "$g(A)$ lands in finitely many *stages*." Each stage may attach infinitely many cells, but the compact image still meets only finitely many of them (across all stages), and finitely many cells live in a bounded stage. Misreading this as "finitely many stages" loses the argument when stages are infinite-dimensional.

---

# Legal Operations Used

1. **Operation 5 from the topic page (certify smallness by compactness).** This exercise *is* the certification: it shows compactness of $A$ implies smallness relative to the cell complexes, by the compact-image-meets-finitely-many-cells argument.

2. **Operation 1 from the topic page (form the closures of a set).** The class against which smallness is checked is $I\text{-cell}$, the relative cell complexes of $I = \{S^{n-1}\hookrightarrow D^n\}$.

---

# Hints

> [!note]- Hint 1
> A continuous map sends compact sets to compact sets. So $g(A)$ is a compact subspace of the colimit $X_\infty = \mathrm{colim}_\beta X_\beta$. The whole problem reduces to: where can a compact subset of $X_\infty$ live?

> [!note]- Hint 2
> The colimit $X_\infty$ carries the weak topology: a set is closed iff it is closed at every finite stage. Each attached cell $D^n$ is a closed subset, and its image meets a compact set in a closed (hence compact) set. Argue that a compact subset can intersect the interiors of only finitely many cells, or it would contain an infinite closed discrete subset.

> [!note]- Hint 3
> Pick one point from each cell whose interior $g(A)$ meets. If there were infinitely many such cells, this set of points would be closed (its intersection with every stage is finite, hence closed) and discrete, contradicting compactness of the subset of $g(A)$ containing them. So $g(A)$ meets finitely many cells.

> [!note]- Hint 4
> Finitely many cells are all attached by some bounded stage $X_\beta$ (each cell appears at a successor ordinal; the max of finitely many ordinals is an ordinal $<\lambda$). So $g(A)\subseteq X_\beta$, and since $X_\beta\to X_\infty$ is the colimit inclusion, $g$ factors through $X_\beta$. For uniqueness, two factorizations through stages $\beta, \beta'$ agreeing in $X_\infty$ agree on the compact $A$ at the stage $\max(\beta,\beta')$ by the same boundedness.

---

# Solution

The proof converts compactness into bounded factorization in three moves: the image $g(A)$ is compact (Step 1); a compact subset of the cell complex meets finitely many cells, hence lies in a bounded stage (Step 2); so $g$ factors boundedly, essentially uniquely (Step 3). The decisive lemma is the finitely-many-cells fact, which uses the colimit topology.

**Step 1: The image $g(A)$ is compact.**

> [!note]- Derivation
> The map $g : A\to X_\infty$ is continuous and $A$ is compact, so $g(A)$ is a compact subspace of $X_\infty$ (continuous images of compact spaces are compact: an open cover of $g(A)$ pulls back to an open cover of $A$, which has a finite subcover, whose image covers $g(A)$). This is the only place compactness of $A$ is used directly.

**Step 2: A compact subset of $X_\infty$ meets only finitely many cells and hence lies in a bounded stage.**

> [!note]- Derivation
> Write $X_\infty$ as $X_0$ with cells $\{e_t\}_{t\in T}$ attached, each $e_t$ a copy of (the interior of) a disk $D^{n_t}$ attached at some stage $\sigma(t)+1$. The colimit topology declares a set closed iff its preimage in every $X_\beta$ is closed.
>
> Suppose for contradiction that $g(A)$ met the interiors of infinitely many cells $e_{t_1}, e_{t_2}, \dots$. Choose a point $x_k\in g(A)\cap \mathrm{int}(e_{t_k})$ for each $k$. The set $P = \{x_1, x_2, \dots\}$ has the property that its intersection with each $X_\beta$ is finite (only finitely many of the chosen cells are attached by stage $\beta$), hence closed; so $P$ is closed in $X_\infty$, and by the same argument every subset of $P$ is closed, i.e. $P$ is discrete. But $P\subseteq g(A)$ is then an infinite closed discrete subset of the compact space $g(A)$ — impossible. So $g(A)$ meets only finitely many cell interiors.
>
> Finitely many cells $e_{t_1},\dots,e_{t_m}$ are attached by stage $\beta := \max_i(\sigma(t_i)+1) < \lambda$ (a finite max of ordinals below the regular $\lambda$ is below $\lambda$). Hence $g(A)\subseteq X_\beta$.

**Step 3: $g$ factors through $X_\beta$, essentially uniquely.**

> [!note]- Derivation
> Since $g(A)\subseteq X_\beta$ and $X_\beta\hookrightarrow X_\infty$ is (a subspace inclusion realizing) the colimit map, $g$ corestricts to a continuous map $g_\beta : A\to X_\beta$ with $g = (X_\beta\to X_\infty)\circ g_\beta$. This is the surjectivity half of the smallness map.
>
> For uniqueness (injectivity), suppose $g_\beta : A\to X_\beta$ and $g_{\beta'} : A\to X_{\beta'}$ both represent $g$ in the colimit, i.e. become equal after mapping to $X_\infty$. For each $a\in A$, the points $g_\beta(a)$ and $g_{\beta'}(a)$ have the same image in $X_\infty$, so they are identified at some stage $\geq\max(\beta,\beta')$; since $A$ is compact, one bounded stage $\gamma<\lambda$ identifies them for all $a$ at once (the same compact-image argument applied to the pair). Thus $g_\beta$ and $g_{\beta'}$ agree in $X_\gamma$. This is the injectivity half. Together, the canonical map $\mathrm{colim}_\beta\,\mathbf{Top}(A, X_\beta)\to\mathbf{Top}(A, X_\infty)$ is a bijection: $A$ is small relative to $I\text{-cell}$.

> [!note]- Complete formal solution
> Let $X_\infty = \mathrm{colim}_{\beta<\lambda} X_\beta$ for a $\lambda$-sequence of $I$-cell maps, $\lambda$ regular, and $g : A\to X_\infty$ continuous with $A$ compact.
>
> $g(A)$ is compact (continuous image of a compact space). Realize $X_\infty$ as $X_0$ with cells $\{e_t\}_{t\in T}$ attached, cell $e_t$ at stage $\sigma(t)+1$, with the colimit (weak) topology. If $g(A)$ met infinitely many cell interiors, choosing one point per cell yields an infinite subset of $g(A)$ whose intersection with each $X_\beta$ is finite, hence a closed discrete infinite subset of the compact $g(A)$ — a contradiction. So $g(A)$ meets finitely many cells, all attached by $\beta = \max_i(\sigma(t_i)+1)<\lambda$, whence $g(A)\subseteq X_\beta$ and $g$ factors as $A\xrightarrow{g_\beta} X_\beta\to X_\infty$.
>
> If two stage-maps represent $g$, the compactness argument again forces them to agree at a bounded stage. Hence $\mathrm{colim}_\beta\,\mathbf{Top}(A,X_\beta)\to\mathbf{Top}(A,X_\infty)$ is a bijection, so $A$ is small relative to $I\text{-cell}$. The argument used compactness of $A$ and the *closedness of the cell attachments* (giving the weak colimit topology in which finite-per-stage sets are closed). $\blacksquare$

---

# Key Takeaways

**Compactness is smallness, and the bridge is "compact image meets finitely many cells."** The single most transferable idea here is that the analytic finiteness property — compactness — translates directly into the categorical bounded-factorization property — smallness — through the geometric fact that a compact set cannot be spread across infinitely many closed cells. This is the exact mechanism by which the [[Thm - The Small Object Argument|small object argument]] terminates in $\mathbf{Top}$: the domains $S^{n-1}, D^n$ of the generators are compact, so every lifting problem appears at a bounded stage. Whenever you must certify smallness in a topological or geometric category, this is the argument; whenever you see "compact domain," expect "small," and expect the small object argument to run.

**The colimit topology is load-bearing: the argument fails for the wrong topology.** The proof rests on $X_\infty$ carrying the weak topology, in which a set is closed iff it is closed at every stage. This is what makes "one point per cell" a closed discrete set and delivers the contradiction with compactness. If $X_\infty$ carried a coarser topology, a compact set could meet infinitely many cells. The general lesson — that a transfinite colimit must be formed in the right category with the right (colimit) topology for smallness arguments to work — recurs throughout the subject, and is why one works in $\mathbf{Top}$ (or compactly generated spaces) rather than in some convenient but ill-behaved subcategory.

**Smallness has two halves, and both are compactness arguments.** It is easy to focus only on surjectivity ("the map factors through a stage") and forget injectivity ("two stage-factorizations agreeing at infinity already agree at a stage"). Both are needed for the hom-functor to commute with the colimit, and both follow from the same compact-image-is-bounded principle applied once to $g$ and once to the pair of representatives. Recognizing that smallness is a *bijection* statement, not merely a factorization statement, is what lets it be used as the clean hypothesis "the hom-functor commutes with these colimits" in the small object argument and the recognition theorem.
