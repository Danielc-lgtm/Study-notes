---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Path-Product and the Fundamental Group"
  - "Def - Path-Connected Space"
  - "Def - Homotopy of Paths"
tags: [geometry, algebraic-topology, topology]
---

# Notation

$X$ is a topological space, $x_0 \in X$ a base point. $\pi_1(X, x_0)$ is the fundamental group (see [[Def - Path-Product and the Fundamental Group]]). $\{1\}$ denotes the trivial group. See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for full notation.

---

# Axiom Motivation

A space is "simply connected" when it has no holes that a loop can wrap around. The first thing to formalise: there should be no big-scale obstruction to contracting a loop. The second: the space should be in one piece. Both are needed — a space could be path-connected but have a hole (the annulus), or be simply-connected in each component but disconnected (two copies of the disc).

The first condition — every loop contracts — is the natural formalisation of "no holes that obstruct loops." Why is the obstruction phrased in terms of loops? Because higher-dimensional holes (cavities the size of an $n$-ball) are detected by higher-dimensional spheres, not loops. So "every loop contracts" is precisely a 1-dimensional obstruction-vanishing statement, and a space without it has a 1-dimensional hole — the circle around the missing puncture.

Why path-connectedness as the second condition? Because $\pi_1$ is *base-point dependent* — without path-connectedness, the trivial $\pi_1$ at one base point tells you nothing about the other components. A disjoint union of a contractible space and a circle has trivial $\pi_1$ at base points in the contractible component, but the circle's $\pi_1 = \mathbb{Z}$ is invisible there. Path-connectedness is what makes "the" fundamental group meaningful.

A common error: thinking simple connectedness implies contractibility. It does not — the sphere $S^n$ for $n \geq 2$ is simply connected (no 1-dimensional obstructions) but not contractible (the higher-dimensional cavity is detected by $\pi_n$, not $\pi_1$). Contractibility implies simple connectedness; the converse is false the moment higher dimensions become relevant.

A stronger condition: "every continuous map from any compact CW complex contracts" — this is essentially contractibility, but in a categorical packaging. A weaker condition: "$\pi_1$ is trivial at *some* base point" — for non-path-connected spaces, this is weaker than the standard definition. The standard "path-connected + $\pi_1 = 0$" is the sharp sweet spot: enough to make $\pi_1$-vanishing meaningful, not so strong as to demand contractibility.

The single-statement reformulation that captures it: **any two paths in $X$ with the same endpoints are path-homotopic.** This is equivalent (when $X$ is path-connected) to $\pi_1 = 0$ (any loop $\gamma$, viewed as a path from $x_0$ to itself, is path-homotopic to the constant path, since both go from $x_0$ to $x_0$). It is often the cleaner working definition because it avoids the base-point bookkeeping.

---

# The Definition

A topological space $X$ is **simply connected** if:

1. $X$ is [[Def - Path-Connected Space|path-connected]];
2. For some (equivalently, every) base point $x_0 \in X$, $\pi_1(X, x_0) = \{1\}$.

Equivalently (and more usefully in practice): any two paths in $X$ with the same start and end are [[Def - Homotopy of Paths|path-homotopic]].

---

# Categorical / Structural Definition

In the homotopy category $\mathbf{hTop}$, simple connectedness is the property that $X$ is path-connected and $[S^1, X] = *$ (a single homotopy class — that of the constant map). Equivalently, $X$ is path-connected and the map $X \to *$ to a point induces an isomorphism on $\pi_0$ and on $\pi_1$. In the language of CW complexes, $X$ is simply connected if it has the same 2-type as a point — its 2-skeleton (more precisely, its Postnikov 1-truncation) is trivial.

For [[Def - Smooth Manifold|smooth manifolds]] this can be tested via the existence of a [[Def - Universal Cover|universal cover]] being equal to $X$ itself: $X$ is simply connected iff the universal cover $\widetilde X = X$.

---

# Relate to Other Fields / Compression

Simple connectedness is the **1-dimensional vanishing of homotopy obstructions**. The hierarchy is:
$$
\text{contractible} \;\Rightarrow\; n\text{-connected for all } n \;\Rightarrow\; \cdots \;\Rightarrow\; 2\text{-connected} \;\Rightarrow\; \text{simply connected} \;\Rightarrow\; \text{path-connected}.
$$
Each link drops one dimension's worth of obstruction. Simple connectedness is the minimal step above path-connectedness, killing only the 1-dimensional homotopy.

**True name:** simply connected = *every loop can be filled by a disc*, equivalently *the universal cover is the space itself*, equivalently *the inclusion of any point is a $\pi_1$-equivalence*. The "every loop bounds a disc" picture is the most operational — when you want to verify simple connectedness, you exhibit, for any loop, a continuous extension to the disc.

In algebraic topology, simple connectedness is the *cleaning hypothesis* for many constructions. The Hurewicz theorem in higher degrees needs $X$ simply connected to identify $\pi_n$ with $H_n$. The Whitehead theorem needs simple connectedness to upgrade a homology equivalence to a homotopy equivalence. The reason: simply-connected spaces have *no fundamental group acting on higher homotopy groups*, so the higher invariants become bare abelian groups instead of $\mathbb{Z}[\pi_1]$-modules.

---

# Examples / Corollaries

**Is an instance: $\mathbb{R}^n$.** Every loop contracts via the straight-line homotopy $H(s,t) = (1-t)\gamma(s)$. So $\pi_1(\mathbb{R}^n) = 0$ for all $n$.

**Is an instance: any convex subset of $\mathbb{R}^n$.** Same straight-line homotopy (lies inside the convex set). So open and closed balls, half-spaces, simplices, polytopes are all simply connected.

**Is an instance: any star-shaped subset of $\mathbb{R}^n$.** If $U$ is star-shaped with respect to $p$, the homotopy $H(s,t) = (1-t)\gamma(s) + tp$ first slides every point on $\gamma$ toward $p$. The line from $\gamma(s)$ to $p$ lies in $U$ by star-shaped-ness.

**Is an instance: $S^n$ for $n \geq 2$.** A loop on $S^n$ ($n \geq 2$) can be perturbed off any given point by general position; the complement of a point in $S^n$ is homeomorphic to $\mathbb{R}^n$, hence contractible. So the loop, lying in the complement, contracts. Formally, this is a Seifert-van Kampen argument with $U$ and $V$ two open hemispheres.

**Is an instance: $\mathrm{SU}(2) \cong S^3$.** Since $S^3$ is simply connected, $\mathrm{SU}(2)$ is too. This is the key fact underlying $\mathrm{SU}(2) \to \mathrm{SO}(3)$ being the universal cover — see [[Ex - SU(2) is the Universal Cover of SO(3)]].

**Is an instance: any contractible space.** If $X$ deformation-retracts to a point, then $\pi_1(X) = \pi_1(\text{point}) = 0$, and $X$ is path-connected by the retraction.

**Is NOT an instance: $S^1$.** $\pi_1(S^1) = \mathbb{Z} \neq 0$ — the once-around loop does not contract. This is the prototype obstruction; see [[Thm - Pi_1 of S^1 is Z]].

**Is NOT an instance: any annulus, cylinder, or punctured plane.** Each has a non-trivial loop wrapping the hole; $\pi_1 = \mathbb{Z}$ in every case (each deformation-retracts to $S^1$).

**Is NOT an instance: the torus $T^n$.** $\pi_1(T^n) = \mathbb{Z}^n$; non-trivial. See [[Ex - Pi_1 of the Torus is Z Squared]].

**Is NOT an instance: $\mathbb{RP}^n$ for $n \geq 1$.** $\pi_1(\mathbb{RP}^n) = \mathbb{Z}/2$ for $n \geq 2$ and $\pi_1(\mathbb{RP}^1) = \mathbb{Z}$ (since $\mathbb{RP}^1 \cong S^1$). See [[Ex - Pi_1 of RP^n is Z over 2 for n at least 2]].

**Is NOT an instance: the disjoint union of two simply-connected spaces.** Two disjoint discs are not path-connected, so they fail the first condition even though each component has trivial $\pi_1$.

**Corollary (closure under products):** if $X$ and $Y$ are simply connected, so is $X \times Y$ — the product formula $\pi_1(X \times Y) = \pi_1(X) \times \pi_1(Y)$ gives $0 \times 0 = 0$, and path-connectedness is preserved.

**Corollary (closure under coverings to simply-connected):** if $\tilde X \to X$ is a covering and $\tilde X$ is simply connected, then $\tilde X$ *is* the universal cover. So simple connectedness is what characterises the top of the cover lattice — see [[Def - Universal Cover]].

**Corollary (every map from a simply-connected space lifts):** if $Y$ is simply connected and $p : \tilde X \to X$ is any covering, then every continuous $f : Y \to X$ admits a lift to $\tilde X$ (uniquely, given a starting fibre point). This is the cleanest case of [[Thm - Lifting Criterion for Continuous Maps]].

**Calibration check.** If you can (a) prove $\pi_1$ of a convex set is trivial in one sentence, (b) explain why $S^2$ is simply connected without invoking Seifert-van Kampen (use the perturb-off-a-point picture), and (c) state why "path-connected" is required separately from "$\pi_1 = 0$ at some point", you have understood the definition. Bonus: explain why being simply connected is *not* the same as being contractible.

---

# Unlocked by This

> [!tip] The Universal Cover *(in this topic)*
> A path-connected space with a universal cover has the universal cover $\widetilde X$ simply connected by definition — and **simple connectedness is the entire content of "universal".** Every other connected cover $\tilde X' \to X$ is intermediately covered by $\widetilde X$, because the lifting criterion lets the simply-connected $\widetilde X$ lift through any cover. See [[Def - Universal Cover]] and [[Thm - Lifting Criterion for Continuous Maps]].

> [!tip] $n$-Connected Spaces *(from Higher Algebraic Topology)*
> A space is **$n$-connected** if $\pi_k(X) = 0$ for $0 \leq k \leq n$. So path-connected = 0-connected, simply connected = 1-connected. Higher connectedness is what enables homotopy-theoretic obstruction arguments: a map $f : X \to Y$ is an $n$-equivalence iff it induces iso on $\pi_k$ for $k \leq n$ and surjection on $\pi_{n+1}$. The **Whitehead theorem** says a weak equivalence (iso on all $\pi_n$) between **CW complexes** is a homotopy equivalence. Each rung of $n$-connectedness peels off one more layer of homotopical obstruction; the limit is contractibility.
