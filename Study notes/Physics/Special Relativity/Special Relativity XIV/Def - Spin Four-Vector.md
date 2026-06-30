---
type: definition
subject: special-relativity
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Casimir Invariants of the Poincaré Group"
  - "Def - The Levi-Civita Tensor"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, so a timelike vector has positive norm-squared and a spacelike vector negative. An isolated system $\mathscr{S}$ has total [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$, rest mass $m$ with $P\cdot P = m^2$, and four-velocity $U = P/m$. The [[Def - Angular Momentum Four-Tensor|angular momentum tensor]] about an event $C$ is $J^{\alpha\beta} = x^\alpha p^\beta - x^\beta p^\alpha$, with two-form $J_C$. The Levi-Civita tensor is $\epsilon$, with $\epsilon_{0123} = +1$ (so $\epsilon^{0123} = -1$ in mostly-minus); $\times$ or $\times_u$ is the rest-space cross product it induces. The [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] is $W^\mu$. Full registry on [[Special Relativity XIV — Angular Momentum and Spin]].

> [!warning] Convention
> In Gourgoulhon's mostly-plus signature the spin four-vector $\vec s$ is spacelike with $\vec s\cdot\vec s > 0$ and $\vec u\cdot\vec u = -c^2$; in our mostly-minus convention the same physical vector has $\vec s\cdot\vec s < 0$ and $\vec u\cdot\vec u = c^2$. The orthogonality $S\cdot U = 0$ and the magnitude $\|\vec s\| = |\vec\sigma|$ are convention-independent statements; only the sign of the norm-squared and the placement of factors of $c$ change.

This is a compound page: it defines three interlocking notions — the **spin vector** $\vec\sigma$, the **spin two-form** $S$, and the **spin four-vector** $S^\mu$ — because they are three packagings of one object (intrinsic angular momentum) and none is fully usable without the others.

---

# Axiom Motivation

We have built the [[Def - Angular Momentum Four-Tensor|angular momentum tensor]] $J_C$, but it has a flaw as a measure of a body's *intrinsic* rotation: it depends on the reference event $C$. A spinning top has the same internal spin whether you take moments about its centre, about a point a metre away, or about a point in another galaxy — yet $J_C$ changes when you move $C$, by the orbital term $\overrightarrow{C'C}^\flat\wedge P$. We want to extract the part of the angular momentum that does *not* change, the part that is genuinely a property of the system rather than of the observer's choice of origin. That part is the spin.

The first desideratum, then, is **point-independence**. The change-of-origin rule $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$ shows the obstruction: the orbital term is built from the total momentum $P$. If we could find a frame in which $P$ has no spatial part — the barycentric, or centre-of-momentum, frame — then the orbital term would only shift the *time-space* components, and the *space-space* angular momentum vector $\vec\sigma_C$ would be the same for every $C$. This is exactly what happens. For an isolated system measured by an observer comoving with it, $\vec\sigma_C$ turns out to be independent of $C$, and that common value is what we *call* the spin vector $\vec\sigma$. The definition is engineered to deliver point-independence.

The second desideratum is to **package $\vec\sigma$ covariantly**, so that it has meaning independent of the comoving observer who happened to measure it. The angular momentum vector $\vec\sigma$ lives in the rest space $E_u$, a three-dimensional space; to lift it to a four-dimensional object we need to encode "which rest space" — that is, we need the four-velocity $U$. The natural covariant object is the two-form $S := \epsilon(\vec u,\vec\sigma,\cdot,\cdot)$, the angular momentum about the centre of inertia, or equivalently its Hodge dual contracted with $U$, the **spin four-vector** $S^\mu$. The four-velocity is built in because spin is the *rotation in the rest frame*, and there is no rest frame without a four-velocity.

Why must the spin four-vector be **orthogonal to $U$**? Because $\vec\sigma$ lives in the rest space $E_u = U^\perp$ by construction — it is a spatial vector in the comoving frame, with no time component there. Orthogonality $S\cdot U = 0$ is the covariant statement of "purely spatial in the rest frame", and it is what cuts the four components of $S^\mu$ down to the three physical spin components. Drop the orthogonality and you reintroduce a spurious fourth component with no physical meaning — and, worse, you lose the link to the reference worldline: $S\cdot U = 0$ is equivalent to the **spin supplementary condition** $S(p,\cdot)=0$, which is precisely the statement that the spin is referred to the centre of inertia (the Tulczyjew/Synge condition $J_G(p,\cdot)=0$). Without it, "the spin" is referred to no particular worldline and is ambiguous.

The third desideratum, the one that justifies the name, is that this classical object should be the **classical limit of quantum spin**. Wigner's classification labels a relativistic particle by the two Casimir invariants $P^2 = m^2$ and $W^2$, where $W^\mu$ is the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]]. The Pauli–Lubanski vector is built from exactly the contraction $\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$, and it satisfies $W\cdot P = 0$ identically. Defining $S^\mu = W^\mu/(mc)$ makes the classical spin four-vector *equal* to the Pauli–Lubanski vector up to the mass, inherits the orthogonality $S\cdot U = 0$ from $W\cdot P = 0$, and has magnitude that becomes $\sqrt{s(s+1)}\,\hbar$ upon quantisation. The classical definition is chosen so that quantisation is a one-line replacement.

---

# The Definition

Let $\mathscr{S}$ be an **isolated system** of nonvanishing rest mass $m$, with total [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$ and four-velocity $U = P/m$. For an observer comoving with $\mathscr{S}$ (a **barycentric observer**, four-velocity $U$), the [[Def - Angular Momentum Four-Tensor|angular momentum vector]] $\vec\sigma_C$ is **independent of the reference event** $C$. This common value $\vec\sigma\in E_u$ is the **spin vector** of $\mathscr{S}$.

The **spin two-form** is
$$
S \;:=\; \epsilon(\vec u, \vec\sigma, \cdot, \cdot),
$$
the angular momentum of $\mathscr{S}$ about its centre of inertia $G$: by the [[Thm - König Theorem (Relativistic)|König theorem]], $J_G = S$. It satisfies
$$
S(P, \cdot) = 0,
$$
the **spin supplementary condition** (equivalently $S(p,\cdot)=0$, the statement that $S$ is "magnetic" with respect to $P$).

The **spin four-vector** $S^\mu$ is the metric-dual of $\vec\sigma$ lifted covariantly, equal to the [[Def - Casimir Invariants of the Poincaré Group|Pauli–Lubanski vector]] divided by the mass:
$$
S^\mu \;=\; \frac{W^\mu}{mc},
\qquad
W^\mu \;=\; -\tfrac12\,\epsilon^{\mu\nu\rho\sigma} J_{\nu\rho} P_\sigma .
$$
It satisfies the **orthogonality** (spin supplementary) condition
$$
S\cdot U = 0,
$$
inherited from $W\cdot P = 0$, and is therefore a **spacelike** vector lying in the rest space $E_u$. Its norm-squared encodes the magnitude of the spin: $S\cdot S = -\|\vec\sigma\|^2$ (mostly-minus), and the Lorentz-invariant $W^2 = m^2\,S\cdot S = -m^2\|\vec\sigma\|^2$ is the second Casimir of the Poincaré group. The spin two-form and the spin four-vector are related by Hodge duality, $S = \epsilon(\vec u, \vec s, \cdot,\cdot)$ where $\vec s$ is the vector with components $S^\mu$; the two-form $S$ is recovered from $\vec s$ and conversely, so $\vec s$ alone fully determines the spin.

For a **single particle with spin** (treated as a model rather than a derived quantity, since a structureless point particle has $S=0$), the spin is defined directly: a particle with spin carries, in addition to its worldline and four-momentum, a two-form $S$ along the worldline with $S(p,\cdot)=0$, equivalently a spin four-vector $\vec s\in E_u$ with $\vec u\cdot\vec s = 0$, and the spin two-form is $S = \epsilon(\vec u,\vec s,\cdot,\cdot)$.

---

# Categorical / Structural Definition

The spin four-vector is the image of the angular momentum two-form $J$ and the four-momentum $P$ under the natural map
$$
\Lambda^2 V^* \times V \longrightarrow V,
\qquad (J, P) \longmapsto {\star}(J\wedge P^\flat)/m
$$
where $\star$ is the [[Def - The Hodge Star|Hodge star]] on Minkowski space. Concretely $W_\mu = -\tfrac12\epsilon_{\mu\nu\rho\sigma}J^{\nu\rho}P^\sigma$ is the Hodge dual of the three-form $J\wedge P^\flat$, and the spin is $S = W/m$. This is the canonical way to extract a *vector* from the *two-form* $J$ once a preferred direction $P$ is supplied: the Hodge star trades the two unused indices for two used ones, and contraction with $P$ selects the rest-space part.

Structurally, this is the same operation that, in three dimensions, turns the antisymmetric matrix $L_{ij} = \epsilon_{ijk}L^k$ back into the axial vector $L^k$ — except that in four dimensions one antisymmetric pair of indices is dualised and the remaining freedom is fixed by contracting with the four-velocity. The orthogonality $S\cdot U = 0$ is automatic from the antisymmetry of $\epsilon$: $S^\mu U_\mu \propto \epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu = 0$ because $P_\sigma P_\mu$ is symmetric while $\epsilon$ is antisymmetric in $\sigma\mu$.

In the language of the Poincaré group, $W^\mu$ is the unique (up to scale) vector operator built from the generators $J^{\mu\nu}$ and $P^\mu$ that commutes with all translations, and $W^2$ together with $P^2$ generate the centre of the universal enveloping algebra — the two **Casimir invariants**. The spin four-vector is thus the classical avatar of the operator whose eigenvalue labels the spin of a quantum particle.

---

# Relate to Other Fields / Compression

This is, in representation theory, the **Pauli–Lubanski vector** of the Poincaré group, the second of the two Casimir-generating operators (the first being $P^\mu$ itself). In the [[Def - Casimir Invariants of the Poincaré Group|Wigner classification]] the eigenvalue of $W^2$ is what distinguishes a spin-$0$ from a spin-$\tfrac12$ from a spin-$1$ particle of the same mass. The classical spin four-vector is the $\hbar\to 0$ shadow of this operator.

In the geometry of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian mechanics]] the spin is a point of a **coadjoint orbit** of the Poincaré group: the orbits are labelled by mass and spin, and the symplectic structure on the orbit is the natural arena for the classical dynamics of a spinning particle. The spin supplementary condition $S\cdot U = 0$ is the constraint that picks out the physical orbit.

**True name:** the spin is *the part of the angular momentum that is independent of the reference point*. The Pauli–Lubanski formula and the Hodge-dual machinery are the covariant packaging, but the operational content — the thing to reach for in a problem — is far simpler: change the point you take moments about, watch the orbital part $\overrightarrow{C'C}^\flat\wedge P$ change, and the spin is what is left invariant. Equivalently, the spin is the angular momentum measured about the centre of inertia, in the rest frame, where there is no orbital motion to contaminate it.

---

# Examples / Corollaries

**Is an instance — the spin of a rotating disk.** A disk of mass $m$ spinning about its symmetry axis at angular velocity $\omega$ has, in its rest frame, angular momentum vector $\vec\sigma = I\boldsymbol{\omega}$ with $I$ the moment of inertia, a spacelike vector along the axis. Lifted covariantly, $S^\mu = (0, I\boldsymbol{\omega})$ in the rest frame, orthogonal to $U = (1,\mathbf{0})$, with $S\cdot S = -(I\omega)^2$. Boosting the disk does not change $S\cdot S$ — the spin magnitude is a Lorentz invariant — but it tilts $S^\mu$ to acquire a time component in the new frame, always staying orthogonal to the boosted $U$.

**Is an instance — the photon's helicity (as a limiting case).** For a massless particle $m=0$ and $S^\mu = W^\mu/(mc)$ is singular, but $W^\mu$ itself remains finite and turns out to be proportional to $P^\mu$: $W^\mu = h P^\mu$ with $h$ the **helicity**, the projection of spin onto the direction of motion. The massless case degenerates because there is no rest frame; the spin collapses from a three-component vector to a single number, the helicity, which is why a photon has only two polarisation states ($\pm 1$) rather than three.

**Is NOT an instance — the orbital angular momentum.** The orbital part $\overrightarrow{CG}^\flat\wedge P$ of the [[Thm - König Theorem (Relativistic)|König decomposition]] is *not* spin: it depends on the reference event $C$ and vanishes when $C = G$. Spin is by definition the $C$-independent remainder. A planet orbiting a star has large orbital angular momentum about the star but its *spin* is only its own axial rotation.

**Is NOT an instance — a four-vector violating $S\cdot U = 0$.** A vector with a nonzero rest-frame time component, $S^\mu = (S^0, \vec s)$ with $S^0 \ne 0$ in the rest frame, is not a spin four-vector: it fails the supplementary condition, carries an unphysical fourth degree of freedom, and is referred to no definite worldline. The condition $S\cdot U = 0$ is not optional bookkeeping — it is part of the definition.

**Corollary — the spin magnitude is a Lorentz invariant.** Since $S\cdot S = -\|\vec\sigma\|^2$ and the inner product is Lorentz invariant, $\|\vec\sigma\|$ is the same in every frame. This is what makes "the spin of the system" a well-defined number independent of the observer, and it is the classical precursor of the quantised eigenvalue $\sqrt{s(s+1)}\,\hbar$.

**Corollary — orthogonality from antisymmetry.** $S\cdot U \propto W\cdot P \propto \epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma P_\mu = 0$, because the symmetric $P_\sigma P_\mu$ contracts to zero against the antisymmetric $\epsilon$. The supplementary condition is therefore an identity, not an extra assumption, once the spin is defined through the Pauli–Lubanski vector.

**Calibration check.** You should be able to: (1) verify $S\cdot U = 0$ directly from $W^\mu = -\tfrac12\epsilon^{\mu\nu\rho\sigma}J_{\nu\rho}P_\sigma$ using the antisymmetry of $\epsilon$; (2) state, for a system at rest with angular momentum vector $\vec\sigma$, the four components of $S^\mu$ (answer: $(0,\vec\sigma)$); and (3) explain why a massless particle's spin reduces to a single helicity number rather than a three-vector (answer: no rest frame, so $W^\mu \propto P^\mu$).

---

# Unlocked by This

> [!tip] Wigner's Classification and the Meaning of "Particle" *(from Quantum Field Theory)*
> The two Lorentz invariants of an isolated system, $P^2 = m^2$ and $S\cdot S = -\|\vec\sigma\|^2$ (equivalently $W^2 = -m^2\|\vec\sigma\|^2$), are the two [[Def - Casimir Invariants of the Poincaré Group|Casimir invariants]] of the Poincaré group. Wigner's theorem promotes them to a *definition*: an elementary particle is an irreducible unitary representation of the Poincaré group, and such representations are classified by mass $m$ and spin $s$, where $\|\vec\sigma\|^2$ quantises to $s(s+1)\hbar^2$. The classical spin four-vector of this page is the bridge: it is the classical observable whose quantisation yields the spin quantum number, and its orthogonality $S\cdot U = 0$ is the classical form of the constraint that selects the $2s+1$ physical polarisation states. The whole subject of "what an elementary particle is" rests on this object.

> [!tip] The Dirac and Weyl Spinor Fields *(from Quantum Field Theory)*
> A spin-$\tfrac12$ system has $\|\vec\sigma\|^2 = \tfrac34\hbar^2$, and its quantum description is not a four-vector but a **spinor** — an object transforming under the double cover $SL(2,\mathbb{C})$ of the Lorentz group, built in [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]]. The classical spin four-vector $S^\mu$ reappears in spinor language as the bilinear $\bar\psi\gamma^\mu\gamma^5\psi$, the axial current, whose expectation value is the spin direction. The classical kinematics of this page — the supplementary condition, the BMT precession — survive into the spinor theory as the semiclassical limit of the Dirac equation in an external field.

> [!tip] Spin–Statistics and the Structure of Matter *(from Quantum Field Theory)*
> The invariant $S\cdot S$ classified here, once quantised to integer or half-integer $s$, is the input to the **spin–statistics theorem**: integer spin forces Bose statistics, half-integer spin forces Fermi statistics. That the electron has $s = \tfrac12$ — a fact encoded classically in its spin four-vector and measured through the BMT precession of this chapter — is, via spin–statistics and the Pauli exclusion principle, the reason matter is stable and the periodic table has its structure. The humble classical spin vector is the first link in that chain.
