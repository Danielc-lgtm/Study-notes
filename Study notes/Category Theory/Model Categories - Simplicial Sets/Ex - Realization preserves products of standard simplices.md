---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - Geometric Realization is a Quillen Equivalence"
  - "Thm - Geometric Realization is Left Adjoint to the Singular Nerve"
  - "Def - Kan Complex and the Nerve"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Show that geometric realisation preserves the product of two standard simplices: the canonical map
$$|\Delta^m \times \Delta^n| \longrightarrow |\Delta^m| \times |\Delta^n|$$
is a homeomorphism (the right-hand product taken in compactly generated weak Hausdorff spaces). Then explain why this representable case suffices to prove that $|{-}|$ preserves *all* finite products, $|X \times Y| \cong |X| \times |Y|$, and why this is the key lemma behind [[Thm - Geometric Realization is a Quillen Equivalence|the Quillen equivalence]].

**Recall:**

The **geometric realisation** is $|{-}| : \mathbf{sSet} \to \mathbf{Top}$, the colimit-preserving extension of $[n] \mapsto |\Delta^n|$ (the geometric $n$-simplex), left [[Thm - Geometric Realization is Left Adjoint to the Singular Nerve|adjoint]] to $\mathrm{Sing}$. Being a left adjoint, $|{-}|$ preserves all colimits.

The product $\Delta^m \times \Delta^n$ is the [[Def - Kan Complex and the Nerve|nerve]] of the poset $[m] \times [n]$ (the product partial order). Its non-degenerate simplices are the strictly monotone "staircase" paths in the grid $[m] \times [n]$.

In compactly generated weak Hausdorff spaces $\mathbf{Top}$, the product $- \times Z$ preserves colimits (it is a left adjoint, since the category is cartesian closed); the geometric product $|\Delta^m| \times |\Delta^n|$ is the topological prism.

---

# Convergent Strategy

**Problem class:** This is a *comparison* problem of the comparison world (topic-page Problem-Solving Strategy): we verify that a left adjoint preserves a limit (finite product) it has no formal right to preserve. The routine for "a colimit-preserving functor preserves products" is to reduce to representables by density, then check the representable case by an explicit triangulation.

**Assumption pattern:** The recognisable feature is "left adjoint $|{-}|$ versus a product" — a mismatch, since left adjoints preserve colimits, not limits. The resolution is that *both* sides of the comparison map are colimit-preserving in each variable (using that $-\times Z$ is a left adjoint in compactly generated spaces), so density reduces everything to the representable case $\Delta^m \times \Delta^n$, where a hands-on triangulation of the prism settles it.

**Theorem routing:** The route is: both functors $X \mapsto |X\times Y|$ and $X \mapsto |X|\times|Y|$ preserve colimits in $X$ $\to$ a natural map between colimit-preserving functors on a presheaf category is iso iff iso on representables (density / co-Yoneda) $\to$ check on $X = \Delta^m$, $Y = \Delta^n$ $\to$ the staircase triangulation gives $|\Delta^m \times \Delta^n| \cong |\Delta^m|\times|\Delta^n|$. Then symmetry in $Y$ extends to all $X, Y$.

**Key decision point:** The crux is the *triangulation of the prism*: identifying the non-degenerate simplices of $\Delta^m \times \Delta^n$ with the monotone staircase paths, and recognising that these triangulate the geometric prism $|\Delta^m| \times |\Delta^n|$ exactly. The natural error is to assume the homeomorphism "obviously" because both sides are built from simplices; the content is that the *combinatorial* product triangulates the *geometric* product without gaps or overlaps.

---

# Legal Operations Used

1. **Operation 7 from the topic page (pass to / work with realisation).** The whole problem is about the behaviour of $|{-}|$, used as the colimit-preserving extension of its values on representables.

2. **The density (co-Yoneda) reduction (from [[Thm - The Yoneda Lemma]]).** Reducing the general statement to representables is the standard "natural map of colimit-preserving functors is iso iff iso on representables".

3. **The nerve description of $\Delta^m \times \Delta^n$ (from [[Def - Kan Complex and the Nerve]]).** Identifying the product simplicial set as the nerve of $[m]\times[n]$ gives the explicit staircase simplices that triangulate the prism.

---

# Hints

> [!note]- Hint 1
> A left adjoint preserves colimits, not products — so the statement is not formal. The way in is that *both* sides of the comparison preserve colimits in each variable, so you only need the representable case.

> [!note]- Hint 2
> Fix $Y = \Delta^n$. Show both $X \mapsto |X \times \Delta^n|$ and $X \mapsto |X| \times |\Delta^n|$ preserve colimits in $X$ (the first because $|{-}|$ and $-\times\Delta^n$ do; the second because $|{-}|$ and $-\times|\Delta^n|$ do, the product being in compactly generated spaces). A natural map between them is a homeomorphism for all $X$ iff it is for $X = \Delta^m$.

> [!note]- Hint 3
> So reduce to $|\Delta^m \times \Delta^n| \to |\Delta^m| \times |\Delta^n|$. Recall $\Delta^m \times \Delta^n = N([m]\times[n])$, whose non-degenerate simplices are the strictly monotone paths from $(0,0)$ to $(m,n)$ in the integer grid.

> [!note]- Hint 4
> These staircase paths are exactly the maximal simplices of the standard triangulation of the prism $|\Delta^m| \times |\Delta^n|$ (the "Eilenberg–Zilber" or "shuffle" triangulation). Count them: there are $\binom{m+n}{m}$ top-dimensional simplices, the number of monotone lattice paths, matching the shuffle decomposition of the prism.

---

# Solution

The statement is not formal because $|{-}|$ is a left adjoint and products are limits. The resolution: both sides of the comparison map preserve colimits in each variable, so density reduces to the representable case, where the non-degenerate simplices of $\Delta^m \times \Delta^n$ are the monotone staircase paths and these triangulate the geometric prism exactly.

**Step 1: Reduce to representables by density.**

> [!note]- Derivation
> Fix $Y$. Consider the two functors $F(X) = |X \times Y|$ and $G(X) = |X| \times |Y|$ and the canonical natural transformation $\theta_X : F(X) \to G(X)$ (induced by the projections). Both preserve colimits in $X$: $F$ because $-\times Y$ preserves colimits (in cartesian closed $\mathbf{Top}$... after passing through $|{-}|$ which preserves colimits) and $|{-}|$ preserves colimits; $G$ because $|{-}|$ preserves colimits and $-\times|Y|$ preserves colimits in compactly generated spaces (it is a left adjoint there). Every [[Def - Simplicial Set|simplicial set]] $X$ is a colimit of representables $\Delta^m$ ([[Thm - The Yoneda Lemma|density / co-Yoneda]]). A natural transformation between colimit-preserving functors on a presheaf category is an isomorphism iff it is an isomorphism on representables. So it suffices to show $\theta$ is a homeomorphism for $X = \Delta^m$ (and, by symmetry, this then handles all $Y$).

**Step 2: Identify the simplices of $\Delta^m \times \Delta^n$.**

> [!note]- Derivation
> The product simplicial set $\Delta^m \times \Delta^n$ is the [[Def - Kan Complex and the Nerve|nerve]] of the poset $[m] \times [n]$ (with the product order $(a,b) \le (a',b')$ iff $a \le a'$ and $b \le b'$). Its non-degenerate $k$-simplices are the *strictly* increasing chains $(a_0, b_0) < (a_1, b_1) < \dots < (a_k, b_k)$ in $[m]\times[n]$. The top-dimensional ($k = m+n$) non-degenerate simplices are the chains from $(0,0)$ to $(m,n)$ that increase one coordinate at each step — the **monotone staircase paths** in the grid. There are $\binom{m+n}{m}$ of them (choose when to step right versus up).

**Step 3: The staircases triangulate the prism.**

> [!note]- Derivation
> The geometric prism $|\Delta^m| \times |\Delta^n|$ has a standard triangulation — the **shuffle** (Eilenberg–Zilber) triangulation — whose top-dimensional simplices are indexed precisely by the $(m,n)$-shuffles, equivalently the monotone staircase paths of Step 2. Each staircase path $(0,0) \to \dots \to (m,n)$ determines a geometric $(m+n)$-simplex inside the prism (the convex hull of the corresponding grid vertices), these simplices cover the prism, and they meet only along shared faces. Realising $\Delta^m \times \Delta^n$ glues one geometric simplex $|\Delta^k|$ per non-degenerate simplex along faces, producing exactly this triangulated prism. So the canonical map $|\Delta^m \times \Delta^n| \to |\Delta^m| \times |\Delta^n|$ is a continuous bijection that is a homeomorphism (both sides are compact Hausdorff finite CW complexes, and a continuous bijection between them is a homeomorphism).

**Step 4: Extend to all $X, Y$ and state the consequence.**

> [!note]- Derivation
> By Steps 1–3, $\theta_{\Delta^m}$ is a homeomorphism for every $m$; by density (Step 1) $\theta_X$ is a homeomorphism for every $X$ (with $Y = \Delta^n$ fixed). Running the same density argument in the second variable, $\theta_X$ is a homeomorphism for all $X$ and all $Y$: $|X \times Y| \cong |X| \times |Y|$. This is the key lemma for [[Thm - Geometric Realization is a Quillen Equivalence]]: it makes realisation respect the cylinder $X \times \Delta^1$ (so simplicial homotopies realise to topological homotopies) and, combined with [[Def - Minimal Fibration|minimal fibrations]], makes realisation send Kan fibrations to Serre fibrations — which is what forces the derived counit to be a weak equivalence.

> [!note]- Complete formal solution
> Fix $Y$. The functors $X \mapsto |X\times Y|$ and $X \mapsto |X|\times|Y|$ both preserve colimits in $X$ (each is a composite of colimit-preserving functors, using that $|{-}|$ preserves colimits and $-\times|Y|$ is a left adjoint in compactly generated spaces). Since every $X$ is a colimit of representables ([[Thm - The Yoneda Lemma|density]]), the canonical map $\theta_X : |X\times Y| \to |X|\times|Y|$ is a homeomorphism for all $X$ iff for $X = \Delta^m$. Now $\Delta^m\times\Delta^n = N([m]\times[n])$ has non-degenerate top simplices the monotone staircase paths $(0,0)\to\dots\to(m,n)$, which are exactly the simplices of the shuffle triangulation of the prism $|\Delta^m|\times|\Delta^n|$; so $|\Delta^m\times\Delta^n| \to |\Delta^m|\times|\Delta^n|$ is a continuous bijection of compact Hausdorff CW complexes, hence a homeomorphism. By density in each variable, $|X\times Y|\cong|X|\times|Y|$ for all $X, Y$. $\quad\blacksquare$

---

# Key Takeaways

**"Reduce to representables, then triangulate" is the standard route for any realisation computation.** Almost every fact about geometric realisation that is not purely formal is proved this way: use that $|{-}|$ preserves colimits to reduce a statement about all simplicial sets to a statement about the standard simplices $\Delta^n$ (and their products), then verify the representable case by explicit geometry. The trigger is "prove a property of $|X|$ for all $X$"; the reaction is "$X$ is a colimit of $\Delta^n$, $|{-}|$ preserves it, so check $\Delta^n$". The density/co-Yoneda formula is the engine, and it works because $\mathbf{sSet}$ is a presheaf category where representables generate under colimits. This single template handles product-preservation, the CW structure of $|X|$, and the realisation of quotients.

**Product-preservation is special, not formal, and it is why one must work in compactly generated spaces.** The most important conceptual point is that a left adjoint has *no* general right to preserve products — and the only reason $|{-}|$ does is the combination of (i) the reduction to representables and (ii) the fact that in *compactly generated* spaces the product $-\times Z$ is itself a left adjoint, so the right-hand side is also colimit-preserving. In plain $\mathbf{Top}$ the product fails to be a left adjoint, the right-hand side does not commute with the colimit, and the homeomorphism breaks. The transferable lesson: when a left adjoint appears to preserve a limit, look for a *separate* reason (here, cartesian closedness of the ambient category) — and the choice of ambient category is load-bearing, not cosmetic.

**The shuffle triangulation of the prism is the geometric heart of the Eilenberg–Zilber theorem.** The staircase paths that index the top simplices of $\Delta^m \times \Delta^n$ are the $(m,n)$-shuffles, and the same combinatorial gadget governs the Eilenberg–Zilber map relating the chains of a product to the tensor product of chains, hence the Künneth theorem and the cup product. Recognising that "monotone lattice paths = shuffles = simplices of the prism" links this realisation computation to the multiplicative structure of (co)homology. The diagnostic to carry: whenever a product of simplicial objects appears, the combinatorics is shuffles, and the geometry is the prism triangulation — a single picture that recurs from product-preservation here to the Künneth formula in homological algebra.
