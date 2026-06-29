---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Spacetime Interval"
  - "Def - The Lorentz Group"
  - "Def - Four-Vector"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. Points of Minkowski space are **events**; the space is written $\mathbb{M}$, $\mathbb{R}^{1,3}$, or $\mathcal{E}$, and its associated vector space of displacements is $E$, isomorphic to $\mathbb{R}^4$. In an inertial (affine, orthonormal) coordinate system an event has coordinates $x^\mu = (t,x,y,z)$, $\mu = 0,1,2,3$, with $x^0 = t$. The **Minkowski metric** is the bilinear form $g$; its matrix in an orthonormal basis is $\eta$, with components $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$. The scalar product is $X\cdot Y = g(X,Y) = \eta_{\mu\nu}X^\mu Y^\nu$. We use the **Einstein summation convention**: a repeated index, once up once down, is summed over $0,1,2,3$. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

This is a compound page: it defines two interlocking notions — the **affine space** of events and the **metric** on its displacements — because Minkowski spacetime is precisely the affine space together with the metric, and neither half is the geometry by itself.

> [!warning] Convention: signature
> We use the **"mostly minus"** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a **timelike** vector has $X\cdot X > 0$. Gourgoulhon — the textbook this chapter follows — uses the opposite **"mostly plus"** signature $\mathrm{diag}(-1,+1,+1,+1)$, in which timelike means $g(v,v) < 0$. The two differ by an overall sign of the metric, $\eta_{\text{ours}} = -\eta_{\text{Gourgoulhon}}$; every interval and scalar square flips sign, and the timelike/spacelike conditions swap which is positive. Gourgoulhon's own Remark 1.7 notes that many field-theory texts (and the older general-relativity literature) use exactly our $(+,-,-,-)$; the physics is identical, only the bookkeeping signs change. Throughout, a timelike vector has $X\cdot X > 0$, a spacelike one $X\cdot X < 0$, a null one $X\cdot X = 0$.

---

# Axiom Motivation

By this point in the development there is a body of facts — the [[Def - The Lorentz Transformation|Lorentz transformation]], the [[Thm - Invariance of the Spacetime Interval|invariant interval]], the [[Def - The Lorentz Group|Lorentz group]] — but no single object holding them together. Minkowski's contribution was to supply that object: a geometry. The desideratum is to package "space and time" into one mathematical structure on which the Lorentz group acts as the natural symmetry, just as the Euclidean group acts on Euclidean space.

The first design decision is the *kind* of space. Events are the raw data — a flash here-now, a collision there-then — and the crucial observation is that there is no distinguished "origin event", no canonical zero of spacetime. A vector space has a zero; spacetime does not. The correct structure is therefore an **affine space**: a set of points $\mathcal{E}$ together with a vector space $E$ of *displacements between points*, related by a map sending each ordered pair $(A,B)$ to the displacement $\overrightarrow{AB} \in E$, subject to two axioms. First, fixing any point $O$, the map $M \mapsto \overrightarrow{OM}$ is a bijection $\mathcal{E} \to E$ (so a choice of origin identifies points with vectors, but no origin is preferred). Second, Chasles' relation $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ holds for all triples. Drop the first axiom and you cannot coordinatise; drop Chasles' relation and displacements would not compose, so "going from $A$ to $C$ via $B$" would not equal "going from $A$ to $C$". The payoff is exactly the fact that organises the whole subject: the coordinate tuple $(t,x,y,z)$ of a *single* event is not a [[Def - Four-Vector|four-vector]] — a change of origin shifts it inhomogeneously — but a *difference* of two such tuples is, because the constant shift cancels. Vectors live in $E$, the model space; events live in $\mathcal{E}$.

The second, decisive design decision is the structure that makes this affine space *Minkowski* rather than Newtonian or Euclidean. Newtonian spacetime is the same four-dimensional affine space, distinguished only by a foliation into hyperplanes of absolute simultaneity — a *degenerate* "metric" that measures the time-difference between events and is blind to spatial separation. Relativity replaces this with a *non-degenerate* metric. The naive Euclidean choice is wrong, and seeing why is the whole motivation. Take $\mathbb{R}^4$ with the Euclidean structure: the distance $\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$. But the Euclidean distance is *not* Lorentz invariant — a boost changes it — so the Euclidean structure is the wrong structure. What the earlier chapters established is that the invariant quantity is the [[Def - The Spacetime Interval|interval]] $\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$, with three minus signs. So the geometry we want is $\mathbb{R}^4$ equipped not with the Euclidean metric but with this *indefinite* one.

The clean way to encode "a quadratic notion of distance" on a vector space is a **symmetric bilinear form** — a map $g(\cdot,\cdot)$ taking two vectors to a number, linear in each and symmetric. Its diagonal $g(X,X)$ is the quadratic form, and we want it to be the interval. Three properties pin the form down, and each is load-bearing. It must be **bilinear and symmetric**: bilinearity so that the scalar product of sums and scalar multiples behaves correctly (without it, no "scalar product" in any usable sense); symmetry so that $g(X,Y) = g(Y,X)$ and the form is determined by its quadratic form via polarisation. It must be **non-degenerate**: if some nonzero vector were "invisible" to $g$ — orthogonal to everything — the geometry would be defective, the vector-to-form duality would collapse, and the Lorentz group would not be its full isometry group. Drop non-degeneracy and you are back to the *degenerate* Newtonian "metric", with absolute time and absolute space rather than a single fused geometry; this is precisely the failure that distinguishes Newton from Einstein. And it must have **signature $(1,3)$** — one plus, three minus — because that is what makes the interval invariant and distinguishes the one time direction from the three space directions. By **Sylvester's law of inertia** the signature is a coordinate-independent invariant of a real symmetric form, so "signature $(1,3)$" is a genuine, frame-free specification.

What the form must *not* be is **positive definite**. A positive-definite $g$ would give honest four-dimensional Euclidean geometry — no light cone, no causal structure, no distinction between time and space, nothing relativistic. The indefiniteness, the fact that $g(X,X)$ can be negative or zero for nonzero $X$, is not a defect to be tolerated; it is the entire physical content. It is what produces null vectors, the light cone, and the [[Def - Classification of Four-Vectors|timelike/spacelike/null trichotomy]]. The single design decision of the chapter is: keep $\mathbb{R}^4$, but replace the positive-definite metric with the indefinite $g$ of signature $(1,3)$.

---

# The Definition

**Minkowski space** $\mathbb{M}$ is the four-dimensional real **affine space** modelled on $\mathbb{R}^4$ — a set $\mathcal{E}$ of **events**, with associated vector space $E \cong \mathbb{R}^4$ of displacements, such that fixing any origin $O$ makes $M \mapsto \overrightarrow{OM}$ a bijection $\mathcal{E} \to E$ and Chasles' relation $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ holds — together with the **Minkowski metric** on $E$: the symmetric, non-degenerate, indefinite bilinear form $g$ whose matrix in an orthonormal basis is
$$
\eta_{\mu\nu} = \begin{pmatrix} 1 & & & \\ & -1 & & \\ & & -1 & \\ & & & -1 \end{pmatrix},
\qquad
g(X,Y) \;=\; \eta_{\mu\nu}\, X^\mu Y^\nu \;=\; X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3.
$$
The form has **signature** $(1,3)$ — one positive and three negative eigenvalues — and by Sylvester's law of inertia this signature is independent of the (orthonormal) basis chosen. The associated **quadratic form** is $g(X,X) = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2$; for $X = \overrightarrow{PQ}$ the displacement between two events it is the [[Def - The Spacetime Interval|spacetime interval]] $\Delta s^2$.

The form is:
- **symmetric**: $g(X,Y) = g(Y,X)$;
- **non-degenerate**: $g(X,Y) = 0$ for all $Y$ implies $X = 0$ — equivalently, the matrix $(\eta_{\mu\nu})$ is invertible, with inverse $(\eta^{\mu\nu})$ satisfying $\eta^{\mu\rho}\eta_{\rho\nu} = \delta^\mu{}_\nu$;
- **indefinite**: $g(X,X)$ may be positive, negative, or zero, and a *nonzero* vector $X$ can satisfy $g(X,X) = 0$.

A **pseudo-orthonormal basis** (in this chapter, simply an **orthonormal basis**) of $E$ is a basis $(e_0,e_1,e_2,e_3)$ with
$$
e_0 \cdot e_0 = +1, \qquad e_i \cdot e_i = -1 \ \ (i = 1,2,3), \qquad e_\alpha \cdot e_\beta = 0 \ \ (\alpha \neq \beta),
$$
so that $g(e_\alpha, e_\beta) = \eta_{\alpha\beta}$. An **inertial (affine) coordinate system** is a choice of origin event $O$ and such a basis, giving each event $M$ its affine coordinates $x^\mu$ via $\overrightarrow{OM} = x^\mu e_\mu$. The transformations between inertial coordinate systems are exactly the [[Def - The Lorentz Transformation|Lorentz transformations]] (allowing also a shift of origin gives the Poincaré transformations); the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$ — the matrices $\Lambda$ with $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ — is the **isometry group** of $(E,g)$.

The norm with respect to $g$ is $\|X\| := \sqrt{|g(X,X)|}$, equal to $\sqrt{X\cdot X}$ for timelike $X$ and $\sqrt{-X\cdot X}$ for spacelike $X$; it is *not* a norm in the analyst's sense, since $\|X\| = 0$ for nonzero null $X$ and the triangle inequality fails (Gourgoulhon's Remark 1.11).

---

# Categorical / Structural Definition

Minkowski space is, at the level of its vector space, an object of the category of **inner-product spaces with a possibly-indefinite non-degenerate symmetric bilinear form** (pseudo-Euclidean spaces): a real vector space equipped with such a form, with morphisms the linear isometries. Two such spaces are isomorphic exactly when their forms have the same signature (Sylvester's law of inertia), so the isomorphism class of $(E,g)$ is the single datum "signature $(1,3)$, dimension $4$". The automorphism group of the object is its isometry group — here the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$.

This places Minkowski space one rung above Euclidean space in a uniform hierarchy. Euclidean space $\mathbb{E}^n$ is the inner-product space of signature $(n,0)$, with automorphism group $O(n)$. Minkowski space is signature $(1,3)$, with automorphism group $O(1,3)$. Both are *flat* — the metric is constant, the same bilinear form at every point — which is what makes them affine spaces rather than genuine curved manifolds.

At the level of the full structure, Gourgoulhon's clean formulation is that Minkowski spacetime is a **four-tuple** $(\mathcal{E}, g, \mathcal{I}^+, \epsilon)$: an affine space $\mathcal{E}$ of dimension four, a metric $g$ of signature $(1,3)$ on its vector space, a choice $\mathcal{I}^+$ of [[Def - The Null Cone and the Time Arrow|future null cone]] (a time arrow), and a Levi-Civita form $\epsilon$ ([[Def - Spacetime Orientation|an orientation]]). The affine space and metric are fixed by the geometry; once they are set, there are exactly two choices of time arrow and two of orientation. General relativity drops flatness: it replaces the constant $\eta$ by a position-dependent metric field $g_{\mu\nu}(x)$ on a manifold, and the object becomes a genuine pseudo-Riemannian manifold whose automorphisms are general diffeomorphisms.

---

# Examples / Corollaries

**Is an instance — the displacement between two events.** If $P$ and $Q$ are events with coordinates $p^\mu$ and $q^\mu$, the displacement $X^\mu = q^\mu - p^\mu = \overrightarrow{PQ}$ is a vector in the model space $E$ of $\mathbb{M}$, and $g(X,X) = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ is the interval between them. Displacements are the prototypical vectors of Minkowski space.

**Is an instance — a pseudo-orthonormal basis.** In any inertial frame the coordinate basis $e_0 = (1,0,0,0)$, $e_1 = (0,1,0,0)$, $e_2 = (0,0,1,0)$, $e_3 = (0,0,0,1)$ is orthonormal: $e_0\cdot e_0 = +1$, $e_i\cdot e_i = -1$ for $i = 1,2,3$, and all cross products vanish. A Lorentz transformation carries one such basis to another, which is the geometric meaning of "change of inertial frame".

**Is NOT an instance — $\mathbb{R}^4$ with the Euclidean metric.** The space $\mathbb{R}^4$ with $g(X,Y) = X^0Y^0 + X^1Y^1 + X^2Y^2 + X^3Y^3$ (all plus signs, signature $(4,0)$) is four-dimensional Euclidean space, *not* Minkowski space. Its isometry group is $O(4)$, not $O(1,3)$; it has no light cone and no causal structure. The topological space is the same — both are $\mathbb{R}^4$ — but the geometry is entirely different. Minkowski space *is* the metric, not the underlying point set.

**Is NOT an instance — a degenerate form (Newtonian spacetime).** The "Galilean metric", which measures only time difference, $g(X,X) = (X^0)^2$ ignoring the spatial part, is *degenerate*: every purely spatial vector is $g$-orthogonal to everything, so the non-degeneracy axiom fails. This degenerate structure is exactly what underlies Newtonian spacetime, and its degeneracy is why Newtonian physics has *separate* absolute time and absolute space rather than a single fused geometry. It is the same affine space as $\mathbb{M}$, carrying a different and defective form.

**Is NOT an instance — an event as a vector.** A single event $P$, with coordinates $(t,x,y,z)$ in some frame, is *not* a four-vector: shifting the origin $O \mapsto O'$ changes its coordinates by a constant $a^\mu$, $p^\mu \mapsto p^\mu - a^\mu$, which is not a linear (homogeneous) transformation. Only the *difference* $\overrightarrow{PQ} = q^\mu - p^\mu$ is a four-vector, because the constant $a^\mu$ cancels. This is the affine structure doing its work.

**Corollary — there exist nonzero vectors of zero norm.** Take $X = (1,1,0,0)$: $g(X,X) = 1 - 1 = 0$, yet $X \neq 0$. Such **null vectors** exist precisely because $g$ is indefinite; they form the [[Def - The Null Cone and the Time Arrow|null cone]]. In a Euclidean space, zero norm forces the zero vector — the calibration check that one has understood indefiniteness.

**Corollary — the metric raises and lowers indices.** Non-degeneracy means $g$ gives an isomorphism between vectors and dual vectors (linear functionals): to a vector $X^\mu$ it associates the dual vector $X_\mu = \eta_{\mu\nu}X^\nu$, with $X_0 = X^0$, $X_i = -X^i$. The scalar product is then $g(X,Y) = X_\mu Y^\mu$. This is the [[Def - Metric Duality and Index Manipulation|index gymnastics]] that organises every relativistic computation.

**Calibration check.** If you have understood the definition you can: (i) verify that $X = (2,1,1,0)$ is timelike by computing $g(X,X) = 4 - 1 - 1 = 2 > 0$, and that $X = (1,2,0,0)$ is spacelike with $g(X,X) = 1 - 4 = -3 < 0$; (ii) explain why $(t,x,y,z)$ for a single event is not a four-vector but $q^\mu - p^\mu$ is, by appeal to the affine structure and the inhomogeneity of an origin shift; (iii) state, without computing, why no orthonormal basis can have all four basis vectors of scalar square $+1$ (Sylvester: the signature $(1,3)$ is an invariant, so exactly one is $+1$ and three are $-1$).

---

# Unlocked by This

> [!tip] Four-Vectors and Their Classification *(from §3.2)*
> With the metric in hand, a [[Def - Four-Vector|four-vector]] is an element of $E$ (equivalently, an object transforming under the Lorentz group), and the sign of its scalar square $g(X,X)$ gives the Lorentz-invariant [[Def - Classification of Four-Vectors|classification]] into timelike, spacelike, and null — the causal structure of spacetime, and the engine of the [[Thm - Two Lemmas on Causal Vectors|lemmas on causal vectors]].

> [!tip] Tensors on Spacetime *(from QFT and General Relativity)*
> Once a vector space with a metric is fixed, **tensors** — multilinear maps on copies of the space and its dual — are the immediate generalisation, transforming with one factor of $\Lambda$ per index. The metric $\eta_{\mu\nu}$ is itself a tensor, the **energy-momentum tensor** $T^{\mu\nu}$ another, and tensor equations are the manifestly Lorentz-invariant laws of relativistic physics.

> [!tip] The Curved Metric of General Relativity *(from General Relativity)*
> Replacing the constant $\eta_{\mu\nu}$ by a position-dependent $g_{\mu\nu}(x)$ turns the flat affine Minkowski space into a curved **pseudo-Riemannian manifold**; the deviation of $g$ from $\eta$ is the gravitational field, and Minkowski space is the local model every curved spacetime resembles at each point.

> [!tip] The Equivalence Principle and Locally Inertial Frames *(from General Relativity)*
> The single design decision of this page — keep $\mathbb{R}^4$ but install the indefinite $\eta$ of signature $(1,3)$ — is the seed of all of gravitation once one further step is taken: let the metric *vary from point to point*. The flat metric $\eta_{\mu\nu}$ becomes a metric *field* $g_{\mu\nu}(x)$, a different symmetric bilinear form at each event, and gravity is the statement that this field is not constant. The bridge from the flat case to the curved case is the **equivalence principle**: at any one event one can always choose coordinates — a *locally inertial frame*, the frame of a freely-falling observer — in which $g_{\mu\nu}$ equals $\eta_{\mu\nu}$ and its first derivatives vanish, so that special relativity holds *exactly* at that event. Curvature is precisely the obstruction to doing this *globally*: the second derivatives of $g_{\mu\nu}$ cannot all be removed, and what survives is the Riemann tensor. So $\eta_{\mu\nu}$ is the universal local model — every curved spacetime looks like Minkowski space in the tangent space at each point, the way every smooth surface looks like its tangent plane — and the metric, no longer a fixed background but a dynamical field obeying the Einstein equations, becomes the central object of **general relativity**. Minkowski space is the $g_{\mu\nu} = \eta_{\mu\nu}$ solution: the spacetime with no gravity at all.

> [!tip] The Metric as the Central Object of Physics *(from General Relativity)*
> It is worth isolating the single most consequential idea this page seeds. In special relativity the metric $\eta_{\mu\nu}$ is a fixed *background*: it is the same constant array at every event, it is not affected by anything, and it is not itself a physical variable. General relativity makes one change, and the entire theory of gravitation follows from it — the metric is *promoted* from a fixed background to a dynamical field $g_{\mu\nu}(x)$. The values of $g_{\mu\nu}$ at each event are now genuine degrees of freedom, on the same footing as the position of a particle or the value of a field, and they obey their own equation of motion, the Einstein field equations, with matter and energy as the source. Gravity in this picture is not a force superimposed on a flat background; it *is* the deviation of $g_{\mu\nu}(x)$ from the constant $\eta_{\mu\nu}$, and a freely-falling body simply follows a geodesic of $g$. The bridge from this page is the **equivalence principle**: at every event there is a *locally inertial frame* — the frame of a freely-falling observer — in which $g_{\mu\nu}$ reduces to exactly the $\eta_{\mu\nu}$ defined here and its first derivatives vanish, so special relativity holds exactly at that event. What cannot be removed are the second derivatives of $g_{\mu\nu}$; their irreducible part is the curvature, and curvature is the true, frame-independent signature of a gravitational field. So $\eta_{\mu\nu}$ is the universal local model that every spacetime matches in the tangent space of each point, and the indefinite signature $(1,3)$ fixed on this page is carried over unchanged: $g_{\mu\nu}(x)$ has signature $(1,3)$ everywhere, which is the precise sense in which gravitation never disturbs the local structure of time and space, only their global fitting-together.
