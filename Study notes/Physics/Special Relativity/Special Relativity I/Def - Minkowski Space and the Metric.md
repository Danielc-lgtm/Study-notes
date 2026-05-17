---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spacetime Interval"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Points of Minkowski space are **events**; in an inertial frame an event has coordinates $x^\mu = (t,x,y,z)$, $\mu = 0,1,2,3$, with $x^0 = t$. The **Minkowski metric** is $\eta$, with components $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$. We use the **Einstein summation convention**: a repeated index, once up once down, is summed over $0,1,2,3$. The space is written $\mathbb{M}$ or $\mathbb{R}^{1,3}$. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

By the end of §1.1 and §1.2 there is a body of facts — the [[Def - The Lorentz Transformation|Lorentz transformation]], the [[Thm - Invariance of the Spacetime Interval|invariant interval]], the [[Def - The Lorentz Group|Lorentz group]] — but no single object holding them together. Minkowski's contribution was to supply that object: a geometry. The desideratum is to package "space and time" into one mathematical structure on which the Lorentz group acts as the natural symmetry, just as the Euclidean group acts on Euclidean space.

The naive package is wrong, and seeing why is the whole motivation. The obvious move is to take $\mathbb{R}^4$ with its standard Euclidean structure: a four-dimensional space with the distance $\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$. But the Euclidean distance on $\mathbb{R}^4$ is *not* Lorentz invariant — a boost changes it — so the Euclidean structure is the wrong structure. What §1.1 established is that the invariant quantity is the [[Def - The Spacetime Interval|interval]] $\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$, with three minus signs. So the geometry we want is $\mathbb{R}^4$ equipped not with the Euclidean metric but with this *indefinite* one.

The clean way to encode "a quadratic notion of distance" on a vector space is a **symmetric bilinear form** — a map $\eta(\cdot,\cdot)$ taking two vectors to a number, linear in each and symmetric. Its diagonal $\eta(X,X)$ is the quadratic form, and we want $\eta(X,X)$ to be the interval. The bilinear form whose quadratic form is $t^2 - x^2 - y^2 - z^2$ is $\eta = \mathrm{diag}(1,-1,-1,-1)$. Two requirements pin it down. It must be **non-degenerate**: if some nonzero vector were "invisible" to $\eta$ — orthogonal to everything — the geometry would be defective, and the Lorentz group would not be its full isometry group. And it must have **signature $(1,3)$** — one plus, three minuses — because that is what makes the interval invariant and what distinguishes the one time direction from the three space directions. By Sylvester's law of inertia the signature is a coordinate-independent invariant of the form, so "signature $(1,3)$" is a genuine, frame-free specification.

What it must *not* be is **positive definite**. A positive-definite $\eta$ would give honest four-dimensional Euclidean geometry — no light cone, no causal structure, no distinction between time and space, nothing relativistic. The indefiniteness, the fact that $\eta(X,X)$ can be negative or zero for nonzero $X$, is not a defect to be tolerated; it is the entire physical content. It is what produces null vectors, the light cone, and the [[Def - Classification of Four-Vectors|timelike/spacelike/null trichotomy]]. The single design decision of the topic is: keep $\mathbb{R}^4$, but replace the positive-definite metric with the indefinite $\eta$ of signature $(1,3)$.

One more choice: is the structure on *points* or on *vectors*? Events are points; there is no distinguished "origin event". So Minkowski space is properly an **affine space** — a space of points with no preferred origin — and the metric lives on the associated vector space of *displacements between events*. This is why the coordinate tuple of a single event is not a [[Def - Four-Vector|four-vector]] but a difference of two such tuples is.

---

# The Definition

**Minkowski space** $\mathbb{M}$ is the four-dimensional real **affine space** modelled on $\mathbb{R}^4$ — its points are **events** — together with the **Minkowski metric** on the associated vector space of displacements: the symmetric, non-degenerate, indefinite bilinear form
$$
\eta(X, Y) \;=\; \eta_{\mu\nu}\, X^\mu Y^\nu \;=\; X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3,
\qquad
\eta_{\mu\nu} = \begin{pmatrix} 1 & & & \\ & -1 & & \\ & & -1 & \\ & & & -1 \end{pmatrix}.
$$
The form has **signature** $(1,3)$ — one positive and three negative eigenvalues — and by Sylvester's law of inertia this signature is independent of the (inertial) coordinates chosen. The associated **quadratic form** is $\eta(X,X) = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2$; for $X$ the displacement between two events it is the [[Def - The Spacetime Interval|spacetime interval]] $\Delta s^2$.

The metric is **indefinite**: $\eta(X,X)$ may be positive, negative, or zero, and a nonzero vector $X$ can satisfy $\eta(X,X) = 0$. The metric is **non-degenerate**: $\eta(X,Y) = 0$ for all $Y$ implies $X = 0$.

An **inertial coordinate system** is a choice of origin event and a **pseudo-orthonormal basis** $(e_0, e_1, e_2, e_3)$ — one vector with $\eta(e_0,e_0) = +1$, three with $\eta(e_i,e_i) = -1$, all mutually $\eta$-orthogonal. The transformations between inertial coordinate systems are exactly the [[Def - The Lorentz Group|Lorentz transformations]] (allowing also a shift of origin gives the Poincaré transformations); the Lorentz group $O(1,3)$ is the **isometry group** of $(\mathbb{M},\eta)$.

> Sign-convention warning: many field-theory texts (and Carroll's notes) use the opposite signature $\eta = \mathrm{diag}(-1,+1,+1,+1)$, the "mostly plus" convention. The two differ by an overall sign of $\eta$; every interval and norm flips sign, and timelike/spacelike swap which is positive. We use "mostly minus", $\mathrm{diag}(1,-1,-1,-1)$, throughout, so a timelike vector has $\eta(X,X) > 0$.

---

# Categorical / Structural Definition

Minkowski space is an object of the category of **pseudo-Riemannian inner-product spaces** (in the flat, constant-metric case): a real vector space equipped with a non-degenerate symmetric bilinear form, with morphisms the linear isometries. Two such spaces are isomorphic exactly when their forms have the same signature (Sylvester), so the isomorphism class of $(\mathbb{M},\eta)$ is the single datum "signature $(1,3)$, dimension $4$". The automorphism group of the object is its isometry group — here the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$.

This places Minkowski space one rung above Euclidean space in a uniform hierarchy. Euclidean space $\mathbb{E}^n$ is the inner-product space of signature $(n,0)$, with automorphism group $O(n)$. Minkowski space is signature $(1,3)$, with automorphism group $O(1,3)$. Both are *flat* — the metric is constant, the same bilinear form at every point — which is what makes them affine spaces rather than genuine curved manifolds. General relativity drops flatness: it replaces the constant $\eta$ by a position-dependent metric $g_{\mu\nu}(x)$ on a manifold, and the object becomes a genuine pseudo-Riemannian manifold whose automorphisms are general diffeomorphisms.

---

# Examples / Corollaries

**Is an instance — the displacement between two events.** If $P$ and $Q$ are events with coordinates $p^\mu$ and $q^\mu$, the displacement $X^\mu = q^\mu - p^\mu$ is a vector in the model space of $\mathbb{M}$, and $\eta(X,X) = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ is the interval between them. Displacements are the prototypical vectors of Minkowski space.

**Is an instance — a pseudo-orthonormal basis.** In any inertial frame the coordinate basis $e_0 = (1,0,0,0)$, $e_1 = (0,1,0,0)$, $e_2 = (0,0,1,0)$, $e_3 = (0,0,0,1)$ is pseudo-orthonormal: $\eta(e_0,e_0) = 1$, $\eta(e_i,e_i) = -1$ for $i=1,2,3$, and all cross products vanish. A Lorentz transformation carries one such basis to another.

**Is NOT an instance — $\mathbb{R}^4$ with the Euclidean metric.** The space $\mathbb{R}^4$ with $\eta(X,Y) = X^0Y^0 + X^1Y^1 + X^2Y^2 + X^3Y^3$ (all plus signs, signature $(4,0)$) is four-dimensional Euclidean space, *not* Minkowski space. Its isometry group is $O(4)$, not $O(1,3)$; it has no light cone and no causal structure. The topological space is the same — both are $\mathbb{R}^4$ — but the geometry is entirely different. Minkowski space *is* the metric, not the underlying point set.

**Is NOT an instance — a degenerate form.** The "Galilean metric", which measures only time difference ($\eta(X,X) = (X^0)^2$, ignoring space), is degenerate: every purely spatial vector is $\eta$-orthogonal to everything. This degenerate structure is what underlies Newtonian spacetime, and its degeneracy is exactly why Newtonian physics has *separate* absolute time and absolute space rather than a single fused geometry.

**Corollary — there exist nonzero vectors of zero norm.** Take $X = (1,1,0,0)$: $\eta(X,X) = 1 - 1 = 0$, yet $X \ne 0$. Such **null vectors** exist precisely because $\eta$ is indefinite; they form the light cone. In a Euclidean space, zero norm forces the zero vector — the calibration check that one has understood indefiniteness.

**Corollary — the metric raises and lowers indices.** Non-degeneracy means $\eta$ gives an isomorphism between vectors and dual vectors (linear functionals): to a vector $X^\mu$ it associates the dual vector $X_\mu = \eta_{\mu\nu}X^\nu$, with $X_0 = X^0$, $X_i = -X^i$. The inner product is then $\eta(X,Y) = X_\mu Y^\mu$. This is the index gymnastics that organises every relativistic computation.

---

# Unlocked by This

> [!tip] Four-Vectors and Their Classification *(from §1.3)*
> With the metric in hand, a [[Def - Four-Vector|four-vector]] is an object transforming under the Lorentz group, and the sign of its norm $\eta(X,X)$ gives the Lorentz-invariant [[Def - Classification of Four-Vectors|classification]] into timelike, spacelike, and null — the causal structure of spacetime.

> [!tip] Tensors on Spacetime *(from QFT and General Relativity)*
> Once a vector space with a metric is fixed, **tensors** — multilinear maps on copies of the space and its dual — are the immediate generalisation, transforming with one factor of $\Lambda$ per index. The metric $\eta_{\mu\nu}$ is itself a tensor, the **energy–momentum tensor** $T^{\mu\nu}$ another, and tensor equations are the manifestly Lorentz-invariant laws of relativistic physics.

> [!tip] The Curved Metric of General Relativity *(from General Relativity)*
> Replacing the constant $\eta_{\mu\nu}$ by a position-dependent $g_{\mu\nu}(x)$ turns the flat affine Minkowski space into a curved **pseudo-Riemannian manifold**; the deviation of $g$ from $\eta$ is the gravitational field, and Minkowski space is the local model every curved spacetime resembles at each point.
