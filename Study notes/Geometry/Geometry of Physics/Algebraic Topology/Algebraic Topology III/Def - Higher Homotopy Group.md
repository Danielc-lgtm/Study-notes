---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Fundamental Group"
  - "Def - Topological Space"
  - "Def - Continuous Map"
tags: [geometry, algebraic-topology, homotopy]
---

# Notation

$X$ is a topological space (almost always path-connected) with chosen base point $x_0$. $S^k$ is the unit $k$-sphere in $\mathbb{R}^{k+1}$ with a chosen base point (the "north pole"). $I^k = [0,1]^k$ is the unit $k$-cube; its boundary $\dot I^k$ is the union of all faces. A based map $f : (S^k, \mathrm{pt}) \to (X, x_0)$ is equivalent to a map $f : I^k \to X$ with $f(\dot I^k) = x_0$ (collapsing the boundary of the cube to the base point). Two based maps $f_0, f_1$ are **based-homotopic**, written $f_0 \simeq f_1$, if there is a homotopy $F : I^k \times I \to X$ with $F(\cdot, 0) = f_0$, $F(\cdot, 1) = f_1$, and $F(\dot I^k \times I) = x_0$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The motivating question is: *how can we measure the existence of $k$-dimensional holes in a space?* The first homotopy group $\pi_1(X)$ measures the failure of loops to contract — equivalently, the presence of 1-dimensional holes such as the hole in a circle or a torus. For a 2-sphere, $\pi_1(S^2) = 0$ because every loop on the sphere can be contracted to a point; yet there is clearly a "2-dimensional hole" in $S^2$ — the interior of the sphere is missing, and a 2-sphere mapped non-trivially onto another 2-sphere detects this. We need a homotopy invariant that detects this kind of hole — and more generally, that detects $k$-dimensional holes for every $k \geq 1$. The construction generalises $\pi_1$ in the most direct way possible: replace the circle $S^1$ with the higher sphere $S^k$, replace loop homotopy with $k$-dimensional homotopy, and assemble homotopy classes into a group.

The first question of design is: *what is the set of objects, and what is the equivalence relation?* The set must be **based homotopy classes of based maps** $S^k \to X$. The basepoint constraint is technical but necessary: without it, the would-be group operation does not have a unit (a "constant map" in path-connected spaces is unambiguous only up to choice of constant value), and the would-be associativity does not hold up to homotopy without further work. The basepoint is the algebraic anchor. For path-connected $X$, changing the basepoint changes $\pi_k(X, x_0)$ only up to canonical isomorphism (via path conjugation), so the basepoint dependence is mild — but it cannot be removed.

The second question is: *what is the group operation?* For $\pi_1$ the operation is concatenation of loops: travel along $f$ then along $g$. The natural generalisation for $\pi_k$ uses *one* of the $k$ coordinates of $S^k$ to play the role of the loop coordinate, and concatenates along that coordinate while leaving the others as parameters. Concretely, identifying $S^k$ with $I^k / \dot I^k$, we set

$$(f + g)(t_1, t_2, \ldots, t_k) = \begin{cases} f(2t_1, t_2, \ldots, t_k) & 0 \leq t_1 \leq 1/2 \\ g(2t_1 - 1, t_2, \ldots, t_k) & 1/2 \leq t_1 \leq 1. \end{cases}$$

The first coordinate $t_1$ is the "concatenation direction"; the remaining coordinates are passive parameters. The identity is the constant map at $x_0$; the inverse $-f$ is $f$ with the first coordinate reversed, $(-f)(t_1, t_2, \ldots) = f(1 - t_1, t_2, \ldots)$. The verification that this gives a well-defined group on homotopy classes is the same routine that proves $\pi_1$ is a group, with the extra coordinates playing no role.

The third question — and this is the deeper one — is: *why is the group abelian for $k \geq 2$?* For $\pi_1$, concatenation $f \cdot g$ and $g \cdot f$ are generally distinct in homotopy: the loops do not commute because there is no room to slide them past each other on the one-dimensional interval. For $\pi_2$, with two coordinate dimensions available, there *is* room: we can slide $g$ down and $f$ up within the square, then back along the other diagonal, producing a homotopy from $f + g$ to $g + f$. This is the **Eckmann–Hilton argument**, and it explains why higher homotopy groups are forced abelian. The lesson — and this is one of the most important conceptual points in algebraic topology — is that **dimension is what makes addition commutative**. With one dimension, you have only an ordered concatenation; with two or more, you have a genuine sum.

The functoriality requirement determines everything else. A based continuous map $\varphi : (X, x_0) \to (Y, y_0)$ induces a group homomorphism $\varphi_* : \pi_k(X, x_0) \to \pi_k(Y, y_0)$ by post-composition: $[f] \mapsto [\varphi \circ f]$. Based-homotopic maps induce the same homomorphism, so $\pi_k$ is a functor from the homotopy category of pointed spaces to groups (abelian for $k \geq 2$). The composition rule $(\varphi \circ \psi)_* = \varphi_* \circ \psi_*$ holds tautologically. This functoriality is what makes $\pi_k$ a true *invariant* of pointed homotopy type, and it is what allows the long exact sequence of a fibration to exist.

What if we tried a different definition? We could try **unbased** maps modulo unbased homotopy, the **free homotopy classes** $[S^k, X]$. For $k = 0$ this gives the set of path-components $\pi_0(X)$, which is a set with a distinguished element but not a group. For $k \geq 1$ on a path-connected space, $[S^k, X] = \pi_k(X)/\pi_1(X)$, the quotient of based homotopy classes by the action of $\pi_1$ on $\pi_k$ (via change-of-basepoint conjugation). For simply connected spaces these agree. But the based version is what supports the group operation cleanly. Alternatively, we could try **stable** maps (suspension-stabilised), giving the **stable homotopy groups** $\pi_k^s(X)$ — these are easier to compute but discard information. The unstable based version is the universal choice from which all variants are derived.

---

# The Definition

Let $(X, x_0)$ be a pointed topological space and let $k \geq 1$ be an integer. The **$k$-th homotopy group of $X$ at $x_0$** is

$$\pi_k(X, x_0) = \{\text{based continuous maps } (S^k, \mathrm{pt}) \to (X, x_0)\} / (\text{based homotopy}),$$

with group operation $[f] + [g] = [f + g]$ defined by concatenation along the first coordinate:

$$(f + g)(t_1, t_2, \ldots, t_k) = \begin{cases} f(2t_1, t_2, \ldots, t_k) & 0 \leq t_1 \leq 1/2 \\ g(2t_1 - 1, t_2, \ldots, t_k) & 1/2 \leq t_1 \leq 1, \end{cases}$$

where we identify $S^k$ with $I^k / \dot I^k$. The identity is the homotopy class of the constant map at $x_0$, and the inverse of $[f]$ is $[-f]$ with $(-f)(t_1, t_2, \ldots) = f(1 - t_1, t_2, \ldots)$.

When $k = 1$, this is the **fundamental group** $\pi_1(X, x_0)$ (see [[Algebraic Topology II — Fundamental Group and Covering Spaces]]).

For $k \geq 2$, $\pi_k(X, x_0)$ is an **abelian group** (proved by [[Thm - Higher Homotopy Groups are Abelian|the Eckmann–Hilton argument]]).

For $k = 0$, $\pi_0(X, x_0)$ is the **set of path-components** of $X$, with $x_0$ distinguished but no group structure in general.

A continuous based map $\varphi : (X, x_0) \to (Y, y_0)$ induces a group homomorphism $\varphi_* : \pi_k(X, x_0) \to \pi_k(Y, y_0)$ by $[f] \mapsto [\varphi \circ f]$.

---

# Categorical / Structural Definition

In categorical language, $\pi_k$ is a **functor** from the category of pointed topological spaces (with based continuous maps modulo based homotopy) to the category of groups (abelian for $k \geq 2$):

$$\pi_k : \mathrm{hTop}_* \to \mathrm{Grp} \quad (k = 1), \qquad \pi_k : \mathrm{hTop}_* \to \mathrm{Ab} \quad (k \geq 2).$$

Equivalently, $\pi_k(X, x_0) = [S^k, X]_*$, the based homotopy classes of based maps from the pointed sphere $S^k$ to the pointed space $(X, x_0)$. The functoriality is by post-composition.

A more refined structural definition uses **loop spaces**. The loop space $\Omega X$ is the space of based maps $S^1 \to X$ (with the compact-open topology, base point the constant loop); it has a natural concatenation that makes it an **$H$-space** (associative up to homotopy). Then $\pi_k(X) = \pi_{k-1}(\Omega X)$, and iterating $\pi_k(X) = \pi_0(\Omega^k X)$. The Eckmann–Hilton structure of higher homotopy is then a consequence of the **double loop space** $\Omega^2 X$ having two compatible $H$-space structures.

In modern language, $\pi_k$ is an invariant of the **$(n, 0)$-truncation** in the homotopy hypothesis: $\pi_k(X)$ records the "$k$-dimensional part" of the $\infty$-groupoid that $X$ represents.

---

# Relate to Other Fields / Compression

**True name:** $\pi_k(X)$ is the **abelian group of homotopy classes of $k$-dimensional spheres in $X$** (with concatenation as group operation). The operational picture is "what are all the genuinely-different ways to draw a $k$-sphere in $X$?" Two are the same if and only if one can be deformed continuously into the other; concatenation is the obvious "do one then the other along a chosen coordinate"; the addition is automatically abelian for $k \geq 2$ because of the extra room.

In the language of [[Algebraic Topology II — Fundamental Group and Covering Spaces|the fundamental group]], $\pi_k$ generalises $\pi_1$ in exactly the most direct way: replace "loop $S^1 \to X$" with "$k$-spherical loop $S^k \to X$". The constructions of base point dependence, functoriality, and homotopy invariance all proceed identically. The new content at higher $k$ is the abelianness, which the fundamental group lacks.

From the perspective of [[Algebraic Topology I — Singular Homology and the de Rham Theorem|singular homology]], $\pi_k(X)$ is a **finer invariant** than $H_k(X; \mathbb{Z})$ — it sees more. The Hurewicz map $\pi_k(X) \to H_k(X; \mathbb{Z})$ (see [[Def - Hurewicz Map]]) is the comparison; it is an isomorphism in the first nonzero degree (by [[Thm - Hurewicz Theorem (Statement)|Hurewicz]]) but in general loses information. The class of the Hopf map in $\pi_3(S^2) = \mathbb{Z}$ maps to zero in $H_3(S^2) = 0$, exhibiting the discrepancy.

---

# Examples / Corollaries

**Is an instance: $\pi_k(\mathbb{R}^n) = 0$ for all $k \geq 1$.** Every continuous map $S^k \to \mathbb{R}^n$ is null-homotopic via the straight-line homotopy $F(x, t) = (1 - t) f(x)$ to the constant map at $0$. So $\pi_k(\mathbb{R}^n) = 0$ for every $k$. This shows that contractible spaces have trivial homotopy in all degrees.

**Is an instance: $\pi_k(S^n) = 0$ for $1 \leq k < n$.** A continuous map $f : S^k \to S^n$ with $k < n$ is homotopic to a smooth map (by smoothing), and by [[Thm - Sard's Theorem|Sard's theorem]] a smooth map cannot cover all of $S^n$ — there is some point $p \in S^n$ missed by $f$. Then $f$ factors through $S^n \setminus \{p\} \cong \mathbb{R}^n$, which is contractible, so $f$ is null-homotopic. So $\pi_k(S^n) = 0$ for $k < n$. This is "low-dimensional spheres detect no high-dimensional features".

**Is an instance: $\pi_n(S^n) = \mathbb{Z}$.** Generated by the identity map, with the integer attached to $f : S^n \to S^n$ being its **Brouwer degree** (see [[Ex - Pi_n of S^n is Z]]). This is the prototype of every Chern number and every integer-valued topological invariant in the chapter.

**Is an instance: $\pi_3(S^2) = \mathbb{Z}$.** Generated by the Hopf map $\eta : S^3 \to S^2$ (see [[Def - The Hopf Map]] and [[Ex - Pi_3 of S^2 is Z via the Hopf Map]]). This is the *spectacular* example: a 3-sphere maps non-trivially onto a 2-sphere, contradicting the naive intuition that lower-dimensional targets can only host lower-dimensional homotopy. The computation goes through the long exact sequence of the Hopf fibration.

**Is an instance: $\pi_k(\mathbb{T}^n) = 0$ for $k \geq 2$.** The torus $\mathbb{T}^n$ has universal cover $\mathbb{R}^n$, which is contractible. By [[Thm - Long Exact Sequence of a Fibration|the long exact sequence]] of the covering $\mathbb{Z}^n \to \mathbb{R}^n \to \mathbb{T}^n$, $\pi_k(\mathbb{T}^n) = \pi_k(\mathbb{R}^n) = 0$ for $k \geq 2$ (the discrete fibre contributes nothing to higher $\pi_k$). The torus has $\pi_1 = \mathbb{Z}^n$ but all higher homotopy is trivial — it is an **aspherical** space, or **Eilenberg–MacLane space** $K(\mathbb{Z}^n, 1)$.

**Is an instance: $\pi_k(\mathbb{RP}^n) = \pi_k(S^n)$ for $k \geq 2$.** $\mathbb{RP}^n$ has $S^n$ as its double cover. By the long exact sequence of the covering $\mathbb{Z}/2 \to S^n \to \mathbb{RP}^n$, the higher homotopy agrees with that of $S^n$; only $\pi_1$ differs ($\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$). This is a general fact: covering spaces share all higher homotopy with their bases.

**Is NOT an instance: a free group structure.** The fundamental group $\pi_1$ can be free, non-abelian, or have any presentation; for instance $\pi_1(\text{figure-eight}) = F_2$ (free on two generators). The higher homotopy group $\pi_k$ for $k \geq 2$ is *always abelian*, so it can never be a free non-abelian group. It can, however, be a free abelian group or any abelian group whatsoever — and constructing a space with prescribed $\pi_k$ is possible via Eilenberg–MacLane spaces.

**Corollary (functoriality).** A homotopy equivalence $f : X \to Y$ induces isomorphisms $f_* : \pi_k(X) \to \pi_k(Y)$ for all $k$. Conversely, **Whitehead's theorem** says that a map between CW complexes inducing isomorphisms on all $\pi_k$ is a homotopy equivalence. So homotopy groups are a complete invariant of homotopy type for CW complexes.

**Corollary (long exact sequence).** Every fibration $F \to E \to B$ produces a long exact sequence $\cdots \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \to \pi_{k-1}(F) \to \cdots$ (see [[Thm - Long Exact Sequence of a Fibration]]). This is the dominant computational tool for higher homotopy.

**Calibration check.** If you understand the definition you should be able to: (i) verify directly that $\pi_k$ is a group (associativity, identity, inverses up to homotopy); (ii) explain why the constant map serves as the identity and why $-f$ defined by reversing the first coordinate is an inverse; (iii) explain why $\pi_0(X)$ is a set rather than a group; (iv) compute $\pi_k(\mathrm{pt}) = 0$ for all $k$.

---

# Unlocked by This

> [!tip] Whitehead's Theorem *(from Algebraic Topology)*
> A based continuous map $f : X \to Y$ between CW complexes that induces isomorphisms $f_* : \pi_k(X) \to \pi_k(Y)$ for all $k \geq 0$ is a **homotopy equivalence**. This is the foundational theorem of CW homotopy theory: the entire homotopy type of a CW complex is determined by its homotopy groups (together with the action of $\pi_1$ on higher $\pi_k$ and the **Postnikov $k$-invariants** that record gluing data). Whitehead is what licences us to call $\pi_k$ "the" invariants of homotopy type.

> [!tip] Eilenberg–MacLane Spaces and Cohomology Operations *(from Homotopy Theory)*
> A space $K(\pi, n)$ with $\pi_n = \pi$ and $\pi_k = 0$ for $k \neq n$ is an **Eilenberg–MacLane space**. It exists and is unique up to homotopy equivalence for every abelian group $\pi$ and every $n \geq 1$. The defining property is the **representability of cohomology**: $H^n(X; \pi) \cong [X, K(\pi, n)]$, so cohomology classes are literally homotopy classes of maps to Eilenberg–MacLane spaces. The space $\mathbb{CP}^\infty = K(\mathbb{Z}, 2)$ is the classifying space $BU(1)$, and the bijection $[X, \mathbb{CP}^\infty] = H^2(X; \mathbb{Z})$ is the statement that line bundles are classified by $c_1$. This is the higher-degree generalisation of the loop-space picture: $\pi_n(X) = [S^n, X] = H^n(X; \pi)^*$ via dualisation, when $X$ is a $K(\pi, n)$.

> [!tip] Stable Homotopy Groups of Spheres *(from Stable Homotopy Theory)*
> The groups $\pi_{n+k}(S^n)$ stabilise as $n \to \infty$ (Freudenthal's suspension theorem): the suspension homomorphism $\Sigma : \pi_{n+k}(S^n) \to \pi_{n+k+1}(S^{n+1})$ is an isomorphism for $n > k + 1$. The limit $\pi_k^s = \lim_n \pi_{n+k}(S^n)$ is the **$k$-th stable homotopy group of spheres**. Computing $\pi_k^s$ is one of the central problems of **stable homotopy theory**: $\pi_0^s = \mathbb{Z}$, $\pi_1^s = \mathbb{Z}/2$ (Hopf), $\pi_2^s = \mathbb{Z}/2$, $\pi_3^s = \mathbb{Z}/24$, and the pattern becomes very intricate. The **Adams spectral sequence** and the **chromatic** filtration are the modern tools for these computations.
