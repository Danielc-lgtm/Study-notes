---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - The Lorentz Group"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. A four-vector is written with a capital letter, $X, Y, U, V$ — *no* arrow, which is reserved for spatial three-vectors $\mathbf{v}$. Its components in an inertial frame are $X^\mu$, $\mu = 0,1,2,3$, with $X^0$ the time component. A Lorentz transformation is $\Lambda$ with components $\Lambda^\mu{}_\nu$. The Einstein summation convention is in force. The metric is $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$, and $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu$. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Axiom Motivation

[[Def - Minkowski Space and the Metric|Minkowski space]] is in place. We now want the relativistic analogue of a "vector" — the kind of object out of which relativistic physics is built: velocity, momentum, force, the electromagnetic potential. The naive definition is "a four-tuple of numbers", but that is exactly the trap, and avoiding it is the whole motivation.

Consider the coordinate tuple $(t,x,y,z)$ of a single event. It is a four-tuple of numbers — but it is *not* a good geometric object, for a simple reason: it depends on where you put the origin. Shift the origin (a Poincaré translation) and every component changes by a constant, *inhomogeneously*. A genuine vector should not care about the origin; its transformation law should be *linear and homogeneous*. So "four-tuple of numbers" is too permissive — it admits the coordinate tuple, which is not a vector.

The fix is to define a four-vector not by what it *is* (a list) but by how it *transforms*. The model is the displacement between two events, $X^\mu = q^\mu - p^\mu$. Under a change of inertial frame both $p^\mu$ and $q^\mu$ acquire the same inhomogeneous shift, which cancels in the difference; what is left is the homogeneous, linear law $X^\mu \to \Lambda^\mu{}_\nu X^\nu$. So the desideratum is exactly this: a four-vector is anything whose four components transform, between inertial frames, by the Lorentz matrix $\Lambda$ — homogeneously, with no additive piece.

Why is the transformation law the right thing to enshrine, rather than the components? Because it is the transformation law that guarantees the *physics* is frame-independent. If $X^\mu$ and $Y^\mu$ both transform with $\Lambda$, then their inner product $\eta_{\mu\nu}X^\mu Y^\nu$ is automatically the *same number* in every frame — the defining property $\Lambda^{\mathsf T}\eta\Lambda = \eta$ of the [[Def - The Lorentz Group|Lorentz group]] makes the two factors of $\Lambda$ cancel against $\eta$. Invariants are built by contracting four-vectors, and a quantity is invariant *because* its ingredients are four-vectors. If you allowed objects with the wrong transformation law into the toolkit, their inner products would be frame-dependent and useless. The transformation law is the membership criterion precisely because it is the passport to invariance.

What breaks with a nearby definition? Define a four-vector as "any four numbers" and you admit the coordinate tuple, whose "inner product with itself" $t^2 - x^2 - \cdots$ depends on the origin — not invariant. Define it as "four numbers invariant under $\Lambda$" and you admit only multiples of zero — too restrictive; genuine four-vectors *do* change components, they just change them lawfully. The Goldilocks definition is "transforms by $\Lambda$": components change, but in the one specific way that keeps contractions invariant.

This is the platonic-versus-representation distinction in its sharpest form. The four-vector is an abstract arrow in [[Def - Minkowski Space and the Metric|Minkowski space]] — a genuine geometric object, existing prior to any frame. Its components $X^\mu$ are merely its shadow in one particular pseudo-orthonormal basis. Different frames see different shadows, related by $\Lambda$; the arrow itself is what is real.

---

# The Definition

A **four-vector** $X$ is an element of the vector space of displacements of [[Def - Minkowski Space and the Metric|Minkowski space]] — equivalently, an object that assigns to each inertial frame an ordered list of four **components** $X^\mu = (X^0, X^1, X^2, X^3)$, such that the components in two inertial frames related by a [[Def - The Lorentz Transformation|Lorentz transformation]] $\Lambda$ satisfy the **transformation law**
$$
\boxed{\quad X^\mu \;=\; \Lambda^\mu{}_\nu\, X'^\nu \quad}
$$
(summation over $\nu$). The law is **linear and homogeneous** — no additive term — which is what distinguishes a four-vector from the coordinate tuple of an event.

Four-vectors form a four-dimensional real vector space: they may be added, $\,(X+Y)^\mu = X^\mu + Y^\mu$, and scaled, $\,(aX)^\mu = aX^\mu$, and both operations respect the transformation law.

The **Minkowski inner product** of two four-vectors is
$$X \cdot Y \;=\; \eta_{\mu\nu}\, X^\mu Y^\nu \;=\; X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3,$$
and the **norm-squared** (or **Minkowski norm**) of $X$ is $X\cdot X = \eta_{\mu\nu}X^\mu X^\nu$. Both are **Lorentz invariant**: they take the same value in every inertial frame. (Proof: $X\cdot Y = X^{\mathsf T}\eta Y = (\Lambda X')^{\mathsf T}\eta(\Lambda Y') = X'^{\mathsf T}(\Lambda^{\mathsf T}\eta\Lambda)Y' = X'^{\mathsf T}\eta Y' = X'\cdot Y'$, using $\Lambda^{\mathsf T}\eta\Lambda = \eta$.)

The **dual** of a four-vector $X^\mu$ is the **covector** (one-form) with **lowered-index components** $X_\mu = \eta_{\mu\nu}X^\nu$, so $X_0 = X^0$, $X_i = -X^i$; covector components transform by the *inverse* matrix, $X_\mu = (\Lambda^{-1})^\nu{}_\mu X'_\nu$, and the inner product is then $X\cdot Y = X_\mu Y^\mu$.

---

# Categorical / Structural Definition

A four-vector is an element of the **tangent space** of Minkowski space at an event — the abstract vector space $T_p\mathbb{M}$ of displacements based at $p$. Carroll's framing makes the point: a vector does not "stretch from one point to another"; it lives at a single point, in the tangent space there. Because Minkowski space is flat (affine), all the tangent spaces are canonically identified, so one often speaks loosely of "the" space of four-vectors — but the careful statement, which survives the passage to curved spacetime, is that a four-vector field assigns a vector in $T_p\mathbb{M}$ to each event $p$.

The **dual** vector space $T^*_p\mathbb{M}$ — the **cotangent space** — is the space of linear maps from four-vectors to $\mathbb{R}$; its elements are covectors or one-forms. The metric $\eta$, being non-degenerate, supplies a canonical isomorphism $T_p\mathbb{M} \xrightarrow{\sim} T^*_p\mathbb{M}$, $X^\mu \mapsto X_\mu = \eta_{\mu\nu}X^\nu$ — "lowering the index". This is the same construction as the musical isomorphism of Riemannian geometry. The distinction between vectors (upper indices, transforming by $\Lambda$) and covectors (lower indices, transforming by $\Lambda^{-1}$) is the **contravariant/covariant** distinction; it is exactly the [[Multivariate Analysis I — Differentiation in Several Variables|multivariate-analysis]] distinction between a tangent vector and a gradient, and it becomes unavoidable here because the metric is indefinite and no basis is canonical.

A **tensor** of type $(k,\ell)$ is then a multilinear map taking $k$ covectors and $\ell$ vectors to $\mathbb{R}$; vectors are type $(1,0)$, covectors type $(0,1)$, the metric type $(0,2)$, and tensor components carry one factor of $\Lambda$ per upper index and one of $\Lambda^{-1}$ per lower index.

---

# Relate to Other Fields / Compression

The transformation law $X^\mu = \Lambda^\mu{}_\nu X'^\nu$ is the [[Thm - The Chain Rule|chain rule]] for a linear coordinate change. In [[Multivariate Analysis I — Differentiation in Several Variables]], a tangent vector to a curve has components $V^\mu = dx^\mu/d\lambda$; under a coordinate change $x^\mu = x^\mu(x')$ these transform by the [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian]] $\partial x^\mu/\partial x'^\nu$. For a Lorentz transformation the coordinate change is *linear*, so the Jacobian is the constant matrix $\Lambda^\mu{}_\nu = \partial x^\mu/\partial x'^\nu$, the same at every event — and the four-vector transformation law is precisely this Jacobian acting on tangent-vector components. The covector law, with $\Lambda^{-1}$, is the chain rule for *gradients*: $\partial/\partial x'^\mu = (\partial x^\nu/\partial x'^\mu)\,\partial/\partial x^\nu$. So the four-vector / covector pair is the tangent-vector / gradient pair of multivariate analysis, specialised to a flat space with constant linear transition maps. The distinction is "pedantic in $\mathbb{R}^n$" (as that note puts it) only because the Euclidean metric identifies the two; in Minkowski space the indefinite metric makes the identification non-trivial — lowering an index flips three signs — and the distinction is structural.

The gradient of a scalar function, $\partial_\mu\phi$, is the canonical example of a covector: under a coordinate change it transforms by the inverse Jacobian, exactly as a one-form must.

---

# Examples / Corollaries

**Is an instance — the displacement between two events.** $X^\mu = q^\mu - p^\mu$ transforms by $\Lambda$ (the inhomogeneous origin-shifts in $p$ and $q$ cancel), so it is a four-vector. It is the prototype, the object the definition is modelled on.

**Is an instance — the four-velocity (preview).** The tangent to a particle's worldline, differentiated with respect to [[Def - Proper Time|proper time]], is the [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $V^\mu = dx^\mu/d\tau$. Because $d\tau$ is a Lorentz invariant and $dx^\mu$ transforms by $\Lambda$, the quotient transforms by $\Lambda$ — a four-vector. (Differentiating instead by coordinate time $t$, which is *not* invariant, would *not* give a four-vector — this is the subtlety **Special Relativity II** opens with.)

**Is an instance — the gradient of a scalar, as a covector.** If $\phi$ is a Lorentz-scalar field, $\partial_\mu\phi$ is a covector — its components transform by $\Lambda^{-1}$. Raising the index, $\partial^\mu\phi = \eta^{\mu\nu}\partial_\nu\phi$, gives the four-vector gradient. The covector is the natural object; the vector requires the metric.

**Is NOT an instance — the coordinate tuple of an event.** $x^\mu = (t,x,y,z)$ is *not* a four-vector: under a Poincaré transformation $x^\mu = \Lambda^\mu{}_\nu x'^\nu + a^\mu$, the constant $a^\mu$ makes the law inhomogeneous. The position of a single event is frame-dependent in a way no genuine vector is. Only *differences* of coordinate tuples are four-vectors.

**Is NOT an instance — the spatial velocity $\mathbf{v} = d\mathbf{x}/dt$.** The ordinary three-velocity, differentiated with respect to coordinate time, does not transform as (the spatial part of) a four-vector: $t$ is not invariant, so $d\mathbf{x}/dt$ obeys the messy [[Thm - Relativistic Velocity Addition|velocity-addition law]] rather than a linear $\Lambda$. This is precisely why relativistic kinematics replaces it with the four-velocity.

**Corollary — inner products of four-vectors are invariants.** For any four-vectors $X, Y$, the number $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu$ is the same in every frame. This is the workhorse: to compute a frame-independent quantity, recognise it as a four-vector inner product and evaluate it in the most convenient frame.

**Corollary — a four-vector that vanishes in one frame vanishes in all.** If $X^\mu = 0$ in some frame, then $X^\mu = \Lambda^\mu{}_\nu\cdot 0 = 0$ in every frame. This is why a conservation law (total four-momentum unchanged) valid in one frame holds in all — the difference "before minus after" is a four-vector, zero in one frame, hence zero everywhere.

---

# Unlocked by This

> [!tip] Classification of Four-Vectors *(from §1.3)*
> The norm-squared $X\cdot X$ is a Lorentz invariant, so its *sign* is frame-independent; this partitions four-vectors into [[Def - Classification of Four-Vectors|timelike, spacelike, and null]], the causal classification of spacetime.

> [!tip] Four-Velocity and Four-Momentum *(from Relativistic Kinematics)*
> Differentiating the worldline by the invariant proper time gives the [[Def - Four-Velocity and Four-Acceleration|four-velocity]]; multiplying by rest mass gives the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P^\mu = (E,\mathbf{p})$, whose conservation and whose invariant norm $P\cdot P = m^2$ are the foundation of relativistic dynamics.

> [!tip] Tensor Fields and the Stress–Energy Tensor *(from QFT and General Relativity)*
> Iterating the construction gives **tensors** — multilinear maps transforming with one $\Lambda$ per index. The **electromagnetic field tensor** $F^{\mu\nu}$ and the **stress–energy tensor** $T^{\mu\nu}$ package the laws of field theory into manifestly Lorentz-invariant equations.
