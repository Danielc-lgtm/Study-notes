---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Homotopy of Paths"
  - "Def - Group"
  - "Def - Path-Connected Space"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$I = [0,1]$. A path $\gamma : I \to X$ has start $\gamma(0)$ and end $\gamma(1)$; a loop based at $x_0$ has $\gamma(0) = \gamma(1) = x_0$. The constant loop at $x_0$ is $c_{x_0}$. The reverse of $\gamma$ is $\gamma^{-1}(t) = \gamma(1-t)$. Path-homotopy rel endpoints is $\simeq$; the class of $\gamma$ is $[\gamma]$. We write $\pi_1(X, x_0)$ for the fundamental group. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

This is a compound page: it defines **two interlocking notions** — the path-product operation $\cdot$ and the fundamental group $\pi_1(X, x_0)$ — because they are introduced together and neither is fully usable without the other (the product is the operation on the group; the group is the set of equivalence classes the product acts on).

---

# Axiom Motivation

We want a group out of loops. A loop is a continuous map of the interval whose start and end coincide; the most natural thing to do with two loops based at the same point is **concatenate them**: do the first loop, then the second. To package both into a single map of $[0,1]$, we have to traverse each at double speed — the first on $[0, \tfrac12]$, the second on $[\tfrac12, 1]$. This is the **path-product** $\gamma_1 \cdot \gamma_2$, and it is the only natural way to combine two paths into one map of the unit interval.

But the path-product on raw paths is *not* associative: the loop $(\alpha \cdot \beta) \cdot \gamma$ spends time $\tfrac14, \tfrac14, \tfrac12$ on its three pieces, while $\alpha \cdot (\beta \cdot \gamma)$ spends $\tfrac12, \tfrac14, \tfrac14$. The two are reparameterisations of each other, but they are not equal as maps. Similarly $c_{x_0} \cdot \gamma$ traverses $c_{x_0}$ for the first half (waiting at $x_0$) and $\gamma$ at double speed for the second half — not the same map as $\gamma$. And $\gamma \cdot \gamma^{-1}$ goes out and back, not the constant.

The right resolution: **pass to homotopy classes**. Reparameterisations are path-homotopic (the homotopy is the straight-line interpolation in parameter space), so $(\alpha \cdot \beta) \cdot \gamma \simeq \alpha \cdot (\beta \cdot \gamma)$, recovering associativity *modulo homotopy*. The "wait then run" loop $c_{x_0} \cdot \gamma$ is reparameterisation-equivalent to $\gamma$, recovering the identity law. And $\gamma \cdot \gamma^{-1}$ admits the "fold" homotopy back to the constant loop, recovering inverses. So path-homotopy is *precisely* the equivalence relation that makes the concatenation product into a group operation.

This is the entire motivation. There is no choice in the construction: we want a group of loops, the only natural product is concatenation, and concatenation fails the group axioms strictly but satisfies them up to path-homotopy. So we quotient by path-homotopy and the result is a group. Any weaker quotient (e.g., free homotopy, without rel endpoints) makes the relation too coarse — loops at different base points would become identified — and any stronger one (e.g., equality on the nose) leaves us with a non-group structure.

The base-point dependence is forced by the rel-endpoints constraint. Without a base point, we have no notion of "loop" to begin with — a loop *is* a path whose endpoints coincide at a specified point, and concatenation only makes sense when the chosen endpoint matches. The base point is a feature, not a bug; for path-connected spaces, the fundamental groups at different base points are isomorphic (via the change-of-basepoint isomorphism, see Examples), but not *canonically* so — the isomorphism depends on a choice of path between the base points.

Why not take homotopy classes of *maps $S^1 \to X$* instead of loops? You can, and you get the set $[S^1, X]$ of **free homotopy classes** of maps, which is the same as $\pi_1(X, x_0) / \mathrm{conj}$ — conjugacy classes in $\pi_1$. It loses the group structure (you cannot concatenate free loops at no base point) and loses the distinction between elements of $\pi_1$ that are conjugate. So free homotopy is a coarser invariant; based homotopy with concatenation is the rich one.

---

# The Definition

**Path-product.** Let $\gamma_1, \gamma_2 : I \to X$ be paths with $\gamma_1(1) = \gamma_2(0)$. Their **path-product** $\gamma_1 \cdot \gamma_2 : I \to X$ is defined by
$$
(\gamma_1 \cdot \gamma_2)(s) = \begin{cases} \gamma_1(2s) & 0 \leq s \leq \tfrac12 \\ \gamma_2(2s-1) & \tfrac12 \leq s \leq 1. \end{cases}
$$
This is continuous (the two pieces agree at $s = \tfrac12$ on the value $\gamma_1(1) = \gamma_2(0)$), and is itself a path from $\gamma_1(0)$ to $\gamma_2(1)$.

**Fundamental group.** Let $X$ be a topological space and $x_0 \in X$ a chosen **base point**. Let $\Omega(X, x_0)$ denote the set of loops at $x_0$ — continuous maps $\gamma : I \to X$ with $\gamma(0) = \gamma(1) = x_0$. The path-product restricts to loops at $x_0$ (since $\gamma_1(1) = x_0 = \gamma_2(0)$), and descends to homotopy classes (if $\gamma_i \simeq \gamma_i'$ then $\gamma_1 \cdot \gamma_2 \simeq \gamma_1' \cdot \gamma_2'$).

The **fundamental group of $X$ at base point $x_0$** is
$$
\pi_1(X, x_0) := \Omega(X, x_0) / \simeq,
$$
the set of path-homotopy classes of loops at $x_0$, with group operation $[\gamma_1] \cdot [\gamma_2] := [\gamma_1 \cdot \gamma_2]$, identity $[c_{x_0}]$, and inverse $[\gamma]^{-1} := [\gamma^{-1}]$ where $\gamma^{-1}(t) = \gamma(1-t)$.

That this is a [[Def - Group|group]] is the content of [[Thm - The Fundamental Group is a Group]].

**Functoriality.** A continuous map $f : X \to Y$ with $f(x_0) = y_0$ induces a **homomorphism**
$$
f_* : \pi_1(X, x_0) \to \pi_1(Y, y_0), \qquad f_*[\gamma] := [f \circ \gamma].
$$
This is well-defined (homotopies of loops in $X$ push forward to homotopies of loops in $Y$), preserves the group operation ($f \circ (\gamma_1 \cdot \gamma_2) = (f\circ\gamma_1) \cdot (f\circ\gamma_2)$), and satisfies $(g \circ f)_* = g_* \circ f_*$ and $(\mathrm{id}_X)_* = \mathrm{id}_{\pi_1(X, x_0)}$. So $\pi_1$ is a **functor** from $\mathbf{Top}_*$ (pointed spaces) to $\mathbf{Grp}$.

**Change of basepoint.** If $X$ is path-connected and $\alpha$ is a path from $x_0$ to $x_1$, the map $\beta_\alpha : \pi_1(X, x_1) \to \pi_1(X, x_0)$ defined by $[\gamma] \mapsto [\alpha \cdot \gamma \cdot \alpha^{-1}]$ is an isomorphism. Different paths $\alpha, \alpha'$ give isomorphisms differing by an inner automorphism of $\pi_1(X, x_0)$. In particular, for path-connected $X$ the group $\pi_1(X, x_0)$ is well-defined up to (non-canonical) isomorphism, and we write $\pi_1(X)$.

---

# Categorical / Structural Definition

$\pi_1 : \mathbf{Top}_* \to \mathbf{Grp}$ is a functor from the category of pointed topological spaces (continuous base-point-preserving maps as morphisms) to the category of groups. It is the lowest non-trivial example of the **homotopy group functors** $\pi_n : \mathbf{Top}_* \to \mathbf{Grp}$, with $\pi_n(X, x_0) = [S^n, X]_*$, pointed homotopy classes of pointed maps from the $n$-sphere. For $n \geq 2$ the group is abelian (Eckmann-Hilton — see [[Ex - Pi_1 of a Topological Group is Abelian]] for the same argument in a different guise).

Equivalently, $\pi_1(X, x_0) = \pi_0(\Omega_{x_0} X, c_{x_0})$ — the set of path-components of the **loop space** $\Omega_{x_0} X = \mathrm{Map}_*(S^1, X)$, with group structure inherited from the natural $H$-space structure on the loop space (concatenation of loops, up to homotopy). This is the conceptual starting point: the fundamental group is the lowest homotopy invariant of an $A_\infty$-space (the loop space), and the higher homotopy invariants give $\pi_n$.

---

# Relate to Other Fields / Compression

The fundamental group is the **1-skeleton homotopy invariant** of a space. For a **CW complex** (a space built by attaching cells of increasing dimension), $\pi_1$ depends only on the 2-skeleton: 1-cells generate, 2-cells impose relations. So computing $\pi_1$ for a CW complex reduces to writing down a presentation $\langle$generators $\mid$ relations$\rangle$.

In the language of [[Group Theory I — §1.1–1.2|group theory]], $\pi_1$ converts a topological-space question into a group-theoretic question, with continuous maps becoming homomorphisms. The covering-space theory makes this dictionary even tighter: connected covers of $X$ ↔ subgroups of $\pi_1(X)$ (see [[Thm - Galois Correspondence for Covering Spaces]]). So the fundamental group is the *complete invariant* of the covering-space theory of $X$.

**True name:** the fundamental group is the **automorphism group of a point in the universal cover**. That is, $\pi_1(X, x_0)$ acts on the fibre $p^{-1}(x_0)$ of the universal cover $\widetilde X \to X$, and this action is free and transitive — so $\pi_1(X, x_0) \cong p^{-1}(x_0)$ as a $\pi_1$-set, and the group structure is the deck-transformation structure. When you want to *compute* with $\pi_1$, think loops and concatenation; when you want to *understand* what it is, think deck transformations of the universal cover.

---

# Examples / Corollaries

**Is an instance: $\pi_1(\mathbb{R}^n, 0) = \{1\}$.** Every loop in $\mathbb{R}^n$ at $0$ is null-homotopic via the straight-line homotopy $H(s,t) = (1-t)\gamma(s)$. So $\pi_1$ of any convex set, any star-shaped set, any contractible space is trivial.

**Is an instance: $\pi_1(S^1, 1) = \mathbb{Z}$.** Loops in $S^1$ are classified by **winding number**, an integer assigning to each loop how many times it goes around. The standard generator is $\theta \mapsto e^{2\pi i \theta}$. See [[Thm - Pi_1 of S^1 is Z]].

**Is an instance: $\pi_1(T^n) = \mathbb{Z}^n$.** The torus $T^n = (S^1)^n$ has $\pi_1$ the product of $n$ copies of $\mathbb{Z}$, generated by the $n$ "circles around the holes". See [[Ex - Pi_1 of the Torus is Z Squared]].

**Is an instance: $\pi_1(S^n) = \{1\}$ for $n \geq 2$.** The $n$-sphere is simply connected once $n \geq 2$ — any loop can be perturbed off any single point (by general position) and the complement of a point is homeomorphic to $\mathbb{R}^n$, hence contractible. So the loop contracts in the complement, hence in $S^n$. See [[Def - Simply Connected Space]].

**Is an instance: $\pi_1(S^1 \vee S^1) = F_2$, the free group on two generators.** The figure-eight has two independent loops $a, b$, and any reduced word in $a, b, a^{-1}, b^{-1}$ corresponds to a different homotopy class. See [[Def - Free Group and Free Product]] and [[Ex - The Universal Cover of the Figure-Eight is the Cayley Graph of F_2]].

**Is NOT an instance: free homotopy classes of maps $S^1 \to X$ are not a group.** Without a chosen base point, you cannot concatenate two free loops — they may not meet. The set $[S^1, X]$ of free homotopy classes is a *set*, equal to the set of conjugacy classes in $\pi_1(X, x_0)$ (for any choice of $x_0$). It loses both the group structure and the distinction between conjugate elements.

**Is NOT an instance: path-product without homotopy quotient is not associative.** As computed above, $(\alpha \cdot \beta) \cdot \gamma$ and $\alpha \cdot (\beta \cdot \gamma)$ are different maps, and the constant loop is not a strict identity. So the raw set $\Omega(X, x_0)$ is *not* a group — only the quotient by path-homotopy is. The quotient is essential.

**Corollary (functoriality applied to homeomorphisms).** A homeomorphism $f : X \to Y$ induces an isomorphism $f_* : \pi_1(X, x_0) \to \pi_1(Y, f(x_0))$. So $\pi_1$ is a topological invariant: two spaces with different $\pi_1$ cannot be homeomorphic. This is the obstruction tool: $\pi_1(\mathbb{R}^2 \setminus \{0\}) = \mathbb{Z}$ but $\pi_1(\mathbb{R}^3 \setminus \{0\}) = 0$, so the two are not homeomorphic.

**Corollary (functoriality applied to homotopy equivalences).** $\pi_1$ is invariant under homotopy equivalence (a stronger statement: $\pi_1$ depends only on homotopy type). So $\pi_1$ of the annulus equals $\pi_1(S^1) = \mathbb{Z}$, since the annulus deformation-retracts to $S^1$.

**Calibration check.** If you can (a) write down the path-product formula explicitly, (b) explain in one sentence why associativity fails strictly and is restored on classes, and (c) state the change-of-basepoint isomorphism along with its inner-automorphism ambiguity, you have understood the definition. Bonus: prove the claim that change-of-basepoint isomorphisms differ by an inner automorphism (hint: $\beta_{\alpha'} \beta_\alpha^{-1}$ is conjugation by $[\alpha' \cdot \alpha^{-1}]$).

---

# Unlocked by This

> [!tip] Higher Homotopy Groups *(from Algebraic Topology III)*
> Replace loops $S^1 \to X$ with **higher-dimensional spheres** $S^n \to X$ (still pointed) and pass to homotopy classes: you get $\pi_n(X, x_0)$, the $n$-th homotopy group. For $n \geq 2$ this group is *automatically abelian* (by the Eckmann-Hilton argument applied to two compatible products on $\pi_n$). The higher homotopy groups carry vastly more information than $\pi_1$ — they detect the difference between $S^2$ and $S^3$, between Lie groups of different ranks — and are notoriously hard to compute. The whole subject of [[Algebraic Topology III — Higher Homotopy and Chern Forms|higher homotopy theory]] grows out of this generalisation.

> [!tip] The Hurewicz Theorem *(from Algebraic Topology I)*
> The first **singular homology** group $H_1(X; \mathbb{Z})$ is the abelianisation of $\pi_1(X)$: $H_1(X; \mathbb{Z}) \cong \pi_1(X)^{\mathrm{ab}} = \pi_1(X) / [\pi_1(X), \pi_1(X)]$. So $H_1$ is "$\pi_1$ with all commutators killed." This is the **Hurewicz theorem in degree 1**, and it gives a clean computational route: compute $\pi_1$ (geometrically), abelianise (algebraically), recover $H_1$. The higher Hurewicz theorem says the lowest-degree non-trivial homotopy and homology groups agree, with the map $\pi_n(X) \to H_n(X)$ being an isomorphism in that degree.
