---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Electromagnetic Field Tensor"
  - "Def - The Exterior Derivative"
  - "Thm - Properties of the Exterior Derivative"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The electromagnetic field is the antisymmetric $2$-form $F$ with components $F_{\mu\nu}$. The **four-potential** is the $1$-form $A$ with components $A_\mu$; its metric-dual vector is $\vec A$, $A^\mu = \eta^{\mu\nu}A_\nu$. A scalar field $\chi$ generates a gauge transformation. Relative to an observer of four-velocity $U_0$, the potential splits into the electric scalar potential $V$ and the magnetic vector potential $\boldsymbol{\mathcal A}$; $\mathbf E$ and $\mathbf B$ are the electric and magnetic fields measured by that observer. The exterior derivative is $d$; $\partial_\mu = \partial/\partial x^\mu$. Full registry on [[Special Relativity XXII — Maxwell's Equations]].

This is a compound page: it defines two interlocking notions — the **four-potential** $A$ with $F = dA$, and the **gauge freedom** $A \to A + d\chi$ that makes it non-unique — together with the observer-relative split into the scalar and vector potentials, because the gauge freedom is inseparable from the potential's definition and the split is how the potential connects to elementary electromagnetism.

---

# Axiom Motivation

The four-potential is invented to exploit a free gift. The homogeneous [[Thm - Maxwell Equations|Maxwell equation]] is $dF = 0$: the field $2$-form is **closed**. Now there is a theorem of the exterior calculus — the **Poincaré lemma** — that says a closed form is, at least locally, **exact**: if $dF = 0$ then there exists a $1$-form $A$ with $F = dA$. The desideratum is simply to take advantage of this. Why work with the six-component field $F$, subject to the constraint $dF = 0$, when one can work with the four-component potential $A$, with no constraint at all, and recover $F$ by differentiation?

The payoff is that the constraint disappears. If we posit $F = dA$ from the start, then $dF = d(dA) = 0$ holds **automatically**, by the [[Thm - Properties of the Exterior Derivative|nilpotence of the exterior derivative]], $d^2 = 0$. The entire homogeneous half of Maxwell's equations — Faraday's law and the absence of magnetic monopoles — becomes an identity, true by the mere existence of the potential, not a law to be imposed. This is the whole reason the potential exists: it trades a constrained six-component object for an unconstrained four-component one and makes half of electromagnetism free.

But the trade has a cost, and understanding the cost is the heart of the definition. The potential is **not unique**. If $A$ gives $F = dA$, then so does $A' = A + d\chi$ for any scalar field $\chi$, because $F' = dA' = dA + d(d\chi) = dA + 0 = F$ — again by $d^2 = 0$. Two potentials differing by an exact form $d\chi$ describe the identical physical field. This redundancy is called **gauge freedom**, and it is not a defect: it is a feature that can be exploited to simplify the equations (by choosing $\chi$ to impose a convenient condition like $\nabla\cdot A = 0$), and it is the seed of the gauge principle that organises all of modern physics. The price of the potential's convenience is that $A$ itself is not a measurable quantity — only $F$ is — and any physical question must have a gauge-invariant answer.

Why a $1$-form, and not some other object? Because $F$ is a $2$-form, and the exterior derivative raises form degree by one, so to have $F = dA$ the potential must be a $1$-form. The $1$-form structure also has exactly four components $A_\mu = (-V, \boldsymbol{\mathcal A})$ (relative to an observer), which is the right count: one scalar potential and one vector potential, the two objects elementary electromagnetism already uses. The relation $F = dA$ in components, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, is precisely the curl-like combination that produces the antisymmetric $F$ from $A$, and it reproduces the familiar $\mathbf E = -\nabla V - \partial_t\boldsymbol{\mathcal A}$ and $\mathbf B = \nabla\times\boldsymbol{\mathcal A}$ when projected onto an observer.

One might ask whether the gauge freedom could be eliminated by some natural condition, making $A$ unique. It cannot be eliminated covariantly: any condition that fully fixes $A$ either breaks Lorentz invariance (like the Coulomb gauge) or fails to fix it completely (the Lorenz gauge leaves a residual $A \to A + d\chi$ with $\Box\chi = 0$). The non-uniqueness is intrinsic, a genuine redundancy in the description of the world, and learning to live with it — choosing gauges for convenience while computing only gauge-invariant quantities — is the central skill the potential teaches.

---

# The Definition

Since the electromagnetic field satisfies the homogeneous [[Thm - Maxwell Equations|Maxwell equation]] $dF = 0$, the Poincaré lemma guarantees the existence (at least locally) of a $1$-form $A$ such that
$$
F \;=\; dA.
$$
The $1$-form $A$ is the **electromagnetic four-potential**. In a coordinate system $(x^\mu)$ its relation to the field is
$$
F_{\mu\nu} \;=\; \partial_\mu A_\nu - \partial_\nu A_\mu \;=\; \nabla_\mu A_\nu - \nabla_\nu A_\mu.
$$

The four-potential is determined by $F$ only up to a **gauge transformation**: for any scalar field $\chi$, the $1$-form
$$
A' \;:=\; A + d\chi
$$
gives the same field, $dA' = dA = F$, because $d(d\chi) = 0$. The freedom to choose $\chi$ is the **gauge freedom**; a specific choice of $A$ within its equivalence class is a **gauge choice**. Different gauge choices describe the same physics, since the physical field is entirely captured by $F$, and $A$ is not a directly measurable quantity.

Given an observer $O$ of four-velocity $U_0$, the orthogonal decomposition of $A$ with respect to $U_0$ defines the **electric (scalar) potential** $V$ and the **magnetic (vector) potential** $\boldsymbol{\mathcal A}$:
$$
A \;=\; V\,\underline{U_0} + \boldsymbol{\mathcal A}, \qquad \langle\boldsymbol{\mathcal A}, U_0\rangle = 0,
$$
where $\underline{U_0}$ is the metric-dual $1$-form of $U_0$. In the inertial coordinates adapted to $O$, the components are
$$
A_\mu = (-V,\, \boldsymbol{\mathcal A}), \qquad A^\mu = (V,\, \boldsymbol{\mathcal A})
$$
(with $c$: $A_\mu = (-V, c\boldsymbol{\mathcal A})$). Substituting $A = V\underline{U_0} + \boldsymbol{\mathcal A}$ into $F = dA$ and projecting onto $O$'s rest space recovers the elementary expressions
$$
\mathbf E = -\nabla V - \frac{\partial\boldsymbol{\mathcal A}}{\partial t}, \qquad \mathbf B = \nabla\times\boldsymbol{\mathcal A},
$$
which justify the names: in a static regime $\mathbf E = -\nabla V$, and $\boldsymbol{\mathcal A}$ is the vector potential of the magnetic field.

---

# Categorical / Structural Definition

The four-potential is a **connection $1$-form on a principal $\mathrm{U}(1)$-bundle** over spacetime, and the field $F = dA$ is its **curvature** $2$-form. This is the structural identity that places electromagnetism inside [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|gauge theory]], and it is the cleanest way to understand the gauge freedom.

A principal $\mathrm{U}(1)$-bundle is a space that attaches a copy of the circle group $\mathrm{U}(1) = \{e^{i\theta}\}$ to each event of spacetime, in a smoothly twisting way. A **connection** on it is a rule for parallel-transporting the $\mathrm{U}(1)$ phase along curves, encoded by a $1$-form $A$; its **curvature** $F = dA$ measures the failure of parallel transport around small loops to return to the identity. A **gauge transformation** is a position-dependent change of the phase reference, $\psi(x) = e^{i\chi(x)}$, and under it the connection changes by $A \to A + d\chi$ — exactly the gauge freedom of the potential. The curvature $F = dA$ is gauge-invariant because $d(A + d\chi) = dA$, which is why $F$ is the measurable field while $A$ is not.

In this language the two facts of the definition become two facts of bundle geometry. The existence of $A$ with $F = dA$ is the statement that the curvature is exact, possible locally on any bundle; globally it requires the bundle to be trivial (no topological twisting), which holds on contractible spacetime but can fail in the presence of magnetic monopoles, where $F$ is closed but not exact. The Bianchi identity $dF = ddA = 0$ that every curvature satisfies is precisely the homogeneous Maxwell equation. The gauge-covariant derivative on a charged matter field of charge $q$ is $D_\mu = \nabla_\mu - iqA_\mu$, the connection acting on the associated line bundle, and the interaction term $\int A_\mu J^\mu$ is the canonical pairing of the connection with the current it transports. Electromagnetism is the abelian ($\mathrm{U}(1)$) special case; replacing $\mathrm{U}(1)$ by a nonabelian group gives Yang–Mills, where $F = dA + A\wedge A$ acquires a self-interaction.

---

# Relate to Other Fields / Compression

The four-potential is the electromagnetic instance of a **connection on a bundle** — the same object as the Levi-Civita connection of [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative|covariant differentiation]] (a connection on the tangent bundle, with curvature the Riemann tensor) and the Yang–Mills potential (a connection on a nonabelian bundle, with curvature the gluon or weak field strength). In each case "connection" means a rule for parallel transport, and "curvature $= d(\text{connection}) + \text{quadratic}$" measures its loop-holonomy; for the abelian electromagnetic case the quadratic term vanishes and $F = dA$ is linear.

**True name:** the four-potential is "the $1$-form whose exterior derivative is the field", $F = dA$, defined up to $A \to A + d\chi$. This is the operational characterisation: $A$ is a bookkeeping device that makes $dF = 0$ automatic and reduces solving Maxwell to a wave equation. The crucial rider, always attached, is "up to a gauge transformation" — you never compute a value of $A$, only gauge-invariant combinations of it (or, quantum-mechanically, the holonomy $\oint A$).

The compression with the scalar potential of electrostatics is exact and grounding. Elementary electrostatics has $\mathbf E = -\nabla V$ for a scalar $V$, and the freedom $V \to V + \text{const}$ (the zero of potential is arbitrary); this is the static, spatial shadow of $A \to A + d\chi$. Magnetostatics has $\mathbf B = \nabla\times\boldsymbol{\mathcal A}$ with $\boldsymbol{\mathcal A} \to \boldsymbol{\mathcal A} + \nabla\lambda$ (the curl kills the gradient); this is the spatial shadow of the same gauge freedom. The four-potential unifies $V$ and $\boldsymbol{\mathcal A}$ into one $1$-form and the two separate gauge freedoms into the single covariant freedom $A \to A + d\chi$.

---

# Examples / Corollaries

**Is an instance — the Coulomb potential of a point charge.** A static point charge $q$ at the origin has $A = V\underline{U_0}$ with $V = \frac{q}{4\pi\varepsilon_0 r}$ and $\boldsymbol{\mathcal A} = 0$. Then $\mathbf E = -\nabla V = \frac{q}{4\pi\varepsilon_0 r^2}\hat{\mathbf r}$ (Coulomb's law) and $\mathbf B = 0$. This is the simplest nontrivial potential, and it shows the scalar potential doing exactly the job of elementary electrostatics.

**Is an instance — the plane-wave potential.** A monochromatic plane wave has $A_\mu = a_\mu\cos(k\cdot x)$ with constant amplitude $a_\mu$ and null wave-vector $k$ ($k\cdot k = 0$); then $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = -(k_\mu a_\nu - k_\nu a_\mu)\sin(k\cdot x)$, an oscillating field transverse to $k$. In Lorenz gauge $k\cdot a = 0$, and a residual gauge transformation can further set $a_0 = 0$ (radiation gauge), leaving two physical polarisations — the two helicity states of the photon.

**Is NOT an instance — a potential that "is" the field.** It is tempting to think of $A$ as just another name for $\mathbf E$ and $\mathbf B$ assembled, but $A$ carries strictly more (gauge) information than $F$: distinct potentials $A$ and $A + d\chi$ give the *same* $\mathbf E$ and $\mathbf B$. So $A$ is not recoverable from $F$ — the map $A \mapsto F = dA$ has a kernel (the closed $1$-forms, locally the exact ones $d\chi$). The potential is more than the field, and the excess is pure gauge.

**Is NOT an instance — two potentials differing by a non-exact closed form, on a topologically nontrivial region.** On spacetime with a hole (say, the exterior of an infinite solenoid), there exist $1$-forms $A$ with $dA = 0$ that are *not* of the form $d\chi$ for any single-valued $\chi$ — closed but not exact. Such an $A$ gives $F = dA = 0$ everywhere yet has nonzero holonomy $\oint A \ne 0$ around the hole. This is *not* an example of trivial gauge equivalence: the two potentials $A$ and $A - (\text{closed non-exact})$ are physically distinguishable quantum-mechanically (the Aharonov–Bohm effect), even though both give $F = 0$. The Poincaré lemma's "locally exact" cannot be upgraded to "globally exact" when the topology is nontrivial.

**Corollary — the homogeneous Maxwell equation is automatic.** From $F = dA$, $dF = d(dA) = 0$ identically, so Faraday's law $\nabla\times\mathbf E = -\partial_t\mathbf B$ and the no-monopole law $\nabla\cdot\mathbf B = 0$ hold without being imposed — the moment a potential is introduced. This is the calibration that the potential is doing its job.

**Corollary — gauge transformations shift only the longitudinal part.** Under $A \to A + d\chi$, the field $F = dA$ is unchanged, so all six components of $\mathbf E$ and $\mathbf B$ are gauge-invariant; what changes is the "longitudinal" content of $A$ (its divergence, $\nabla\cdot A \to \nabla\cdot A + \Box\chi$). This is why a gauge condition is always a condition on $\nabla\cdot A$ or on $A_0$ — it fixes the unphysical longitudinal freedom while leaving the physical transverse field alone.

**Calibration check.** If you have understood the four-potential you can: (i) verify $dF = 0$ directly from $F = dA$ using $d^2 = 0$; (ii) show that $A$ and $A + d\chi$ give the same $F$ for any $\chi$, and explain why this means $A_0$ has no observer-independent value; and (iii) write the Coulomb potential as a four-potential and recover $\mathbf E = \frac{q}{4\pi\varepsilon_0 r^2}\hat{\mathbf r}$.

---

# Unlocked by This

> [!tip] The Lorenz Gauge and the Wave Equation *(from §22.2)*
> The gauge freedom $A \to A + d\chi$ is what makes the [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] $\nabla\cdot A = 0$ attainable, and in that gauge the inhomogeneous Maxwell equation reduces to the wave equation $\Box A = \mu_0 J$ — four uncoupled scalar wave equations, the gateway to [[Thm - Electromagnetic Waves|electromagnetic waves]] and the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert potential]].

> [!tip] The Gauge Principle *(from Gauge Theory and the Standard Model)*
> The redundancy $A \to A + d\chi$ is the first example of a **local gauge symmetry**, and the demand that physics be invariant under *local* phase changes of charged matter is what *forces* the existence of the potential and fixes its coupling. This **gauge principle**, applied to the nonabelian groups $\mathrm{SU}(2)$ and $\mathrm{SU}(3)$, produces the weak and strong interactions; electromagnetism is the abelian $\mathrm{U}(1)$ case, and $A$ is the prototype gauge field — a [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|connection on a U(1) bundle]] (see [[Def - U(1) Gauge Field and Electromagnetic Connection]]).

> [!tip] The Aharonov–Bohm Effect and Holonomy *(from Quantum Mechanics)*
> Quantum mechanically, a charged particle's phase shifts by $\exp(\tfrac{iq}{\hbar}\oint A)$ around a closed loop, and this **holonomy** is gauge-invariant and physically observable — even where $F = 0$ along the path. The **Aharonov–Bohm effect** demonstrates that the potential carries real physical information (the line integral $\oint A$) inaccessible to $F$ alone, overturning the classical view that only $F$ matters. The gauge-invariant content of $A$ is its holonomy, the parallel-transport phase of the $\mathrm{U}(1)$ connection.
