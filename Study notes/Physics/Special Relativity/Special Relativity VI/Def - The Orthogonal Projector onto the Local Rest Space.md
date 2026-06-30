---
type: definition
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Metric Duality and Index Manipulation"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$; the observer's [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ satisfies $U_0\cdot U_0 = +1$. The [[Def - Observer and Local Rest Space|local rest space]] is $E_{U_0} = U_0^\perp$. The projector is $\Pi$ (Gourgoulhon writes $\perp_u$); $\underline{U_0} = g(U_0,\cdot)$ is the metric dual (lowered) of $U_0$, with $\langle\underline{U_0}, X\rangle = U_0\cdot X$. Greek indices run $0$–$3$; $\Pi^\mu{}_\nu$ are the components of $\Pi$. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention — the projector sign is the trap of this chapter
> The orthogonal projector onto the rest space is $\Pi = \mathrm{Id} - \langle\underline{U_0},\cdot\rangle\,U_0$ in **our** mostly-minus signature (sign $-$), but Gourgoulhon writes $\perp_u = \mathrm{Id} + \langle\underline{\vec u},\cdot\rangle\,\vec u$ (sign $+$) in his mostly-plus signature. The discrepancy is entirely due to the normalisation of the four-velocity: $U_0\cdot U_0 = +1$ here versus $\vec u\cdot\vec u = -1$ there. The correct coefficient is always $-\dfrac{1}{U_0\cdot U_0}$, which is $-1$ for us and $+1$ for Gourgoulhon. Our $-$ sign happily coincides with the familiar Euclidean projector $\mathrm{Id} - \langle u,\cdot\rangle u$, because our $U_0$ has positive norm just like a Euclidean unit vector. Copying Gourgoulhon's $+$ into our convention gives a map with $\Pi(U_0) = 2U_0\neq 0$ — not a projector at all.

---

# Axiom Motivation

The previous page split the displacement space as $E = E_{U_0}\overset{\perp}{\oplus}\mathrm{Span}(U_0)$: every vector is uniquely a spatial part (in the rest space) plus a part along the four-velocity. This page builds the operator that *performs* that split — the map that extracts "the spatial part of $X$ for observer $\mathcal{O}$". It is the single most-used object in the chapter, because "what does $\mathcal{O}$ measure as the spatial part of this vector?" is the question behind relative velocity, relative acceleration, electric and magnetic fields, and every projected quantity to come.

What must such an operator do? It must (i) be **linear**, so it splits sums and scalar multiples consistently; (ii) **annihilate $U_0$**, since the four-velocity is purely temporal and has no spatial part; and (iii) **fix every rest-space vector**, since a vector already spatial should be returned unchanged. Properties (ii) and (iii) say $\Pi$ acts as $0$ on $\mathrm{Span}(U_0)$ and as the identity on $E_{U_0}$ — and since these two subspaces span everything, *they determine $\Pi$ uniquely*. So the projector is not a free choice; it is forced by the direct-sum decomposition. The only work is to write it in closed form.

The closed form is dictated by the decomposition $X = \Pi(X) + \alpha U_0$. To find $\alpha$, take the inner product of both sides with $U_0$: since $\Pi(X)\in U_0^\perp$ kills the first term, $X\cdot U_0 = \alpha\,(U_0\cdot U_0)$. Here the signature enters decisively. With $U_0\cdot U_0 = +1$ (our convention), $\alpha = X\cdot U_0$, and therefore
$$
\Pi(X) \;=\; X - \alpha U_0 \;=\; X - (X\cdot U_0)\,U_0.
$$
The sign in front is $-$. Had we used Gourgoulhon's normalisation $U_0\cdot U_0 = -1$, the same computation would give $\alpha = -X\cdot U_0$ and $\Pi(X) = X + (X\cdot U_0)U_0$, sign $+$. The general statement — valid in any signature — is $\Pi(X) = X - \dfrac{X\cdot U_0}{U_0\cdot U_0}\,U_0$. This is the one formula in the chapter where signature mistakes are most common and most fatal, because copying the wrong sign produces an operator that is not even idempotent.

Why this *specific* operator and not a nearby variant? Suppose one dropped the requirement that $\Pi(U_0) = 0$ and instead used $\Pi'(X) = X - \lambda(X\cdot U_0)U_0$ with $\lambda\neq 1$. Then $\Pi'(U_0) = (1-\lambda)U_0\neq 0$, so $\Pi'$ leaves a spurious time component, and it is not idempotent: $\Pi'\circ\Pi'\neq\Pi'$. Idempotence — $\Pi\circ\Pi = \Pi$, the defining property of any projector — holds *only* at $\lambda = 1$, i.e. for the metric-correct coefficient. So the demand "be a genuine projector onto the rest space" pins the operator exactly, and the test of having got it right is idempotence together with $\Pi(U_0) = 0$.

A subtle point worth stressing: this is an **orthogonal** projector (it projects along the metric-orthogonal direction), and orthogonal projectors are self-adjoint with respect to the metric, $g(\Pi X, Y) = g(X, \Pi Y)$. Self-adjointness is what distinguishes an *orthogonal* projection from a skew (oblique) one — projecting onto the rest space but along some non-orthogonal direction would give a different, non-self-adjoint operator. The Einstein–Poincaré choice of simultaneity is exactly what makes the projection orthogonal; a Reichenbach $\varepsilon\neq\tfrac12$ slicing would give an oblique, non-self-adjoint projector with no clean metric meaning.

---

# The Definition

Let $\mathcal{O}$ be an observer with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$) and [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0} = U_0^\perp$.

**Orthogonal decomposition.** Every vector $X\in E$ decomposes uniquely as a part in the rest space plus a part along the four-velocity:
$$
\boxed{\,X \;=\; \Pi(X) + (X\cdot U_0)\,U_0, \qquad \Pi(X)\in E_{U_0}\,}.
$$

**Orthogonal projector.** The **orthogonal projector onto the local rest space** is the endomorphism
$$
\boxed{\,\Pi(X) \;=\; X - (X\cdot U_0)\,U_0\,} \qquad\Longleftrightarrow\qquad \Pi \;=\; \mathrm{Id} - \langle\underline{U_0},\,\cdot\,\rangle\,U_0,
$$
where $\underline{U_0} = g(U_0,\cdot)$ is the lowered four-velocity. In components,
$$
\Pi^\mu{}_\nu \;=\; \delta^\mu{}_\nu - U_0^\mu\,(U_0)_\nu, \qquad (U_0)_\nu = \eta_{\nu\rho}U_0^\rho.
$$
(The signature-general form is $\Pi(X) = X - \dfrac{X\cdot U_0}{U_0\cdot U_0}\,U_0$; with $U_0\cdot U_0 = +1$ this is the boxed formula.)

**Defining properties.** The projector satisfies, immediately from the formula:
$$
\Pi(U_0) = 0, \qquad \Pi(X) = X \ \text{ for } X\in E_{U_0}, \qquad \Pi\circ\Pi = \Pi \ \ (\text{idempotence}),
$$
and it is **self-adjoint** with respect to the metric, $g(\Pi X, Y) = g(X, \Pi Y)$. The decomposition of $E$ it implements is the orthogonal direct sum $E = E_{U_0}\overset{\perp}{\oplus}\mathrm{Span}(U_0)$.

> [!note]- Derivation of the three properties
> **$\Pi(U_0) = 0$:** $\Pi(U_0) = U_0 - (U_0\cdot U_0)U_0 = U_0 - (+1)U_0 = 0$.
>
> **$\Pi$ fixes $E_{U_0}$:** if $X\cdot U_0 = 0$ then $\Pi(X) = X - 0 = X$.
>
> **$\Pi(X)\in E_{U_0}$:** $\Pi(X)\cdot U_0 = X\cdot U_0 - (X\cdot U_0)(U_0\cdot U_0) = X\cdot U_0 - (X\cdot U_0) = 0$.
>
> **Idempotence:** since $\Pi(X)\in E_{U_0}$ and $\Pi$ fixes $E_{U_0}$, $\Pi(\Pi(X)) = \Pi(X)$. Directly: $\Pi(\Pi(X)) = \Pi(X) - (\Pi(X)\cdot U_0)U_0 = \Pi(X) - 0 = \Pi(X)$.
>
> **Self-adjointness:** $g(\Pi X, Y) = g(X - (X\cdot U_0)U_0,\,Y) = X\cdot Y - (X\cdot U_0)(U_0\cdot Y)$, which is symmetric in $X\leftrightarrow Y$, hence equals $g(X, \Pi Y)$. $\blacksquare$

---

# Categorical / Structural Definition

A **projector** (idempotent endomorphism) on a vector space $E$ is precisely a choice of direct-sum decomposition $E = \mathrm{im}\,\Pi\oplus\ker\Pi$: the image is fixed, the kernel is killed, and idempotence $\Pi^2 = \Pi$ is the algebraic statement that $E$ is the internal direct sum of these two subspaces. Conversely, every direct-sum decomposition $E = F\oplus G$ determines a unique projector with image $F$ and kernel $G$. Here $\mathrm{im}\,\Pi = E_{U_0}$ and $\ker\Pi = \mathrm{Span}(U_0)$, so $\Pi$ *is* the decomposition $E = E_{U_0}\oplus\mathrm{Span}(U_0)$ packaged as an operator.

What makes it the **orthogonal** projector — as opposed to one of the many projectors with the same image but different kernel — is that its kernel is the *metric-orthogonal* complement of its image, $\ker\Pi = (\mathrm{im}\,\Pi)^\perp$. In an inner-product space this is equivalent to self-adjointness, $\Pi^\dagger = \Pi$: orthogonal projectors are exactly the self-adjoint idempotents. This is the same characterisation as for orthogonal projections in any Hilbert space; the only twist here is that the inner product is *indefinite*, so "orthogonal" is taken with respect to $\eta$, and the projection is onto a *negative*-definite subspace (the spacelike rest space) along a *positive*-norm direction (the timelike $U_0$). The construction $\Pi = \mathrm{Id} - \underline{U_0}\otimes U_0/(U_0\cdot U_0)$ is the indefinite-metric analogue of the rank-one update $\mathrm{Id} - uu^\top$ that projects off a Euclidean unit vector.

In tensor language, $\Pi^\mu{}_\nu = \delta^\mu{}_\nu - U_0^\mu(U_0)_\nu$ is the mixed-index form of the **spatial metric**: lowering the upper index gives $\Pi_{\mu\nu} = \eta_{\mu\nu} - (U_0)_\mu(U_0)_\nu$, which is exactly $g$ restricted to the rest space, the object that becomes the induced three-metric of the $3+1$ split in general relativity.

---

# Relate to Other Fields / Compression

This is the indefinite-signature cousin of the **rank-one orthogonal projection** $P = \mathrm{Id} - uu^\top$ of Euclidean linear algebra (projection off a unit vector $u$), and of the projection $\mathrm{Id} - |u\rangle\langle u|$ that removes a normalised state in quantum mechanics. In the $3+1$ formulation of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]] the very same operator, built from the unit normal to a spacelike slice, is the **projection tensor** onto the slice, and its action on the spacetime metric produces the induced spatial metric; the way it fails to commute with the covariant derivative encodes the extrinsic curvature. In fluid mechanics, projecting the [[Def - The Energy-Momentum Tensor|energy–momentum tensor]] with $\Pi$ relative to the fluid four-velocity is how one reads off the energy density, momentum density, and stress measured in the local rest frame.

**True name:** $\Pi$ is *the self-adjoint idempotent with image $U_0^\perp$ and kernel $\mathrm{Span}(U_0)$* — operationally, *"subtract off the $U_0$-component"*. The formula $\Pi(X) = X - (X\cdot U_0)U_0$ is the whole of it; memorise the sign by the slogan "in mostly-minus, the timelike $U_0$ behaves like a Euclidean unit vector, so the projector is $\mathrm{Id} - (\cdot\, U_0)U_0$, the Euclidean form".

---

# Examples / Corollaries

**Is an instance — projecting a generic four-vector for a rest observer.** For $U_0 = (1,0,0,0)$, $\Pi(X) = X - X^0 U_0 = (0, X^1, X^2, X^3)$: the projector simply deletes the time component, returning the ordinary spatial part. This is the sanity case the general formula must reduce to.

**Is an instance — the relative velocity of a particle.** Given a particle of four-velocity $U$, its relative velocity for $\mathcal{O}$ is built by projecting $U$ onto the rest space and rescaling: $V = \Pi(U)/(U\cdot U_0)$, with $V\in U_0^\perp$. The projector is exactly the operator that strips the temporal part of $U$ to leave the spatial motion $\mathcal{O}$ sees — the foundation of relative kinematics.

**Is NOT an instance — the oblique (Reichenbach) projector.** The map $\Pi'(X) = X - \lambda(X\cdot U_0)U_0$ with $\lambda\neq 1$ projects onto a hyperplane but is *not* the orthogonal projector: $\Pi'(U_0) = (1-\lambda)U_0\neq 0$, it is not idempotent, and it is not self-adjoint. It corresponds to a non-orthogonal simultaneity convention and has no clean metric meaning. This is the calibration that the *coefficient* matters: only $\lambda = 1$ (with $U_0\cdot U_0 = +1$) gives a genuine orthogonal projector.

**Is NOT an instance — a projector built with the wrong sign.** The map $X\mapsto X + (X\cdot U_0)U_0$ (Gourgoulhon's sign, mis-imported into mostly-minus) sends $U_0\mapsto 2U_0$ and squares to $X + 3(X\cdot U_0)U_0\neq\Pi'$ — it is neither idempotent nor a projection onto anything sensible. This is the concrete failure the convention warning guards against.

**Corollary — the metric splits as $g = (\text{time part}) + (\text{spatial part})$.** Lowering indices, $\eta_{\mu\nu} = (U_0)_\mu(U_0)_\nu + \Pi_{\mu\nu}$, where $\Pi_{\mu\nu} = \eta_{\mu\nu} - (U_0)_\mu(U_0)_\nu$ is the (negative-definite) spatial metric. Thus $X\cdot Y = (X\cdot U_0)(Y\cdot U_0) + \Pi(X)\cdot\Pi(Y)$, separating any inner product into a temporal product and a spatial product for $\mathcal{O}$.

**Calibration check.** You should be able to: (1) verify $\Pi(U_0) = 0$ and $\Pi^2 = \Pi$ directly from the formula, getting the sign right via $U_0\cdot U_0 = +1$; (2) state why $\Pi$ is self-adjoint and what would change for an oblique projector; and (3) write the metric decomposition $\eta_{\mu\nu} = (U_0)_\mu(U_0)_\nu + \Pi_{\mu\nu}$ and identify $\Pi_{\mu\nu}$ as the spatial metric.

---

# Unlocked by This

> [!tip] The Euclidean Spatial Metric *(from §6.1)*
> Lowering an index on $\Pi$ gives the spatial metric $h_{\mu\nu} = -\Pi_{\mu\nu} = -(\eta_{\mu\nu} - (U_0)_\mu(U_0)_\nu)$, positive definite on the rest space; this is the metric under which the rest space is the ordinary Euclidean three-space of [[Thm - Euclidean Character of the Local Rest Space]].

> [!tip] Relative Velocity, Acceleration and the Decomposition of Fields *(from Kinematics and Electromagnetism)*
> Projecting four-vectors and tensors with $\Pi$ relative to an observer is the universal recipe for "what this observer measures": the relative velocity and acceleration of [[Special Relativity VII — Kinematics I, Motion Relative to an Observer]], and the electric and magnetic fields an observer reads off the [[Def - The Electromagnetic Field Tensor|electromagnetic field tensor]] via $E_\mu = F_{\mu\nu}U_0^\nu$, are all built from $\Pi$.

> [!tip] The Projection Tensor of the 3+1 Split *(from General Relativity)*
> Built from the unit normal to a spacelike slice, this same operator is the **projection tensor** of the $3+1$ (ADM) decomposition of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]]; its action on the spacetime metric yields the induced three-metric, and its failure to commute with the covariant derivative is the extrinsic curvature — the dynamical variables of the Hamiltonian formulation of gravity.
