---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Four-Potential"
  - "Def - The Covariant Derivative"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - The Four-Potential|four-potential]] is the $1$-form $A$, with metric-dual vector $\vec A$ and components $A^\mu$; the gauge freedom is $A \to A + d\chi$ for a scalar $\chi$. The covariant divergence is $\nabla\cdot A = \nabla_\mu A^\mu$. The **d'Alembertian** (wave operator) is $\Box := \nabla_\mu\nabla^\mu$; in inertial coordinates with $c = 1$ and signature $(+{-}{-}{-})$, $\Box = \partial_t^2 - \partial_x^2 - \partial_y^2 - \partial_z^2$. The four-current is $J$, the field $F$. An observer of four-velocity $U_0$ splits $A = V\underline{U_0} + \boldsymbol{\mathcal A}$ into scalar and vector potentials. Full registry on [[Special Relativity XXII — Maxwell's Equations]].

This is a compound page: it defines two interlocking notions — the general concept of a **gauge choice** (a condition that fixes the potential within its equivalence class), and the specific **Lorenz gauge** $\nabla\cdot A = 0$ — because the Lorenz gauge is the canonical instance and is unusable without understanding what a gauge choice is and does.

---

# Axiom Motivation

A gauge choice exists to remove a redundancy. The [[Def - The Four-Potential|four-potential]] $A$ is defined only up to $A \to A + d\chi$, so it carries one scalar field's worth of unphysical freedom; this freedom makes $A$ non-unique and clutters the equations with terms that have no physical content. The desideratum is to spend this freedom usefully — to impose a condition that fixes $\chi$ (entirely or partly) and that simplifies the equation we must solve. A gauge choice is exactly such a condition.

Which condition? The equation we want to simplify is the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] written for the potential. Inserting $F = dA$ into $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ gives
$$
\Box A^\nu - \nabla^\nu(\nabla\cdot A) = \mu_0 J^\nu,
$$
a coupled system: the four components of $A$ are tangled together by the term $\nabla^\nu(\nabla\cdot A)$. This term is the obstruction to solving the system component-by-component, and it depends only on the divergence $\nabla\cdot A$. The strategy writes itself: choose the gauge so that $\nabla\cdot A = 0$, and the offending term vanishes, leaving the clean uncoupled wave equation $\Box A^\nu = \mu_0 J^\nu$. This is the **Lorenz gauge**, and it is chosen precisely because $\nabla\cdot A$ is the thing in the way.

Is the Lorenz gauge attainable? This is the crux, and the answer is yes, always — because of how the divergence transforms under a gauge change. If $A$ does not satisfy $\nabla\cdot A = 0$, shift to $A' = A + d\chi$; then $\nabla\cdot A' = \nabla\cdot A + \nabla\cdot(d\chi) = \nabla\cdot A + \Box\chi$. So to make $\nabla\cdot A' = 0$ we need $\Box\chi = -\nabla\cdot A$, a scalar wave equation for $\chi$ with a known source. This equation always has a solution (the d'Alembertian is invertible via its Green function), so the Lorenz gauge can always be reached. The gauge freedom is exactly enough to kill the divergence: one scalar of freedom ($\chi$) removes one scalar constraint ($\nabla\cdot A = 0$).

Why this gauge and not another? The decisive virtue is **Lorentz invariance**. The condition $\nabla\cdot A = 0$ is a scalar equation — the divergence is a scalar — so it holds in every inertial frame at once: a Lorentz transformation maps a Lorenz-gauge potential to another Lorenz-gauge potential. Contrast the **Coulomb gauge** $\nabla\cdot\boldsymbol{\mathcal A} = 0$, which involves only the spatial divergence in a particular observer's rest space; a boost spoils it, because it singles out a frame. For relativistic problems — radiation, the field of a moving charge, anything where covariance matters — the Lorenz gauge is the only natural choice. The Coulomb gauge is reserved for problems inside a fixed frame (atomic physics, statics) where its own simplification (instantaneous Coulomb potential, transverse radiation field) outweighs the loss of covariance.

One subtlety completes the picture: the Lorenz gauge does **not** fix $A$ uniquely. After imposing $\nabla\cdot A = 0$, a further gauge transformation $A \to A + d\chi$ preserves the gauge provided $\Box\chi = 0$ — any solution of the homogeneous wave equation. So a *residual* gauge freedom survives, parametrised by harmonic $\chi$, and it can be spent on a second condition (for instance setting $A_0 = 0$ in vacuum, the radiation gauge). A gauge choice need not be a complete fixing; it is whatever condition makes the problem tractable, and partial fixings are common and useful.

---

# The Definition

A **gauge choice** is a condition imposed on the [[Def - The Four-Potential|four-potential]] $A$ that selects a representative (or a smaller class of representatives) within its gauge-equivalence class $\{A + d\chi : \chi \text{ scalar}\}$, used to simplify the field equations. Two potentials related by $A \to A + d\chi$ describe the same physics; a gauge choice removes some or all of this redundancy.

The **Lorenz gauge** is the choice
$$
\nabla\cdot A \;=\; \nabla_\mu A^\mu \;=\; 0.
$$
It is always attainable: given any $A$ with $\nabla\cdot A \ne 0$, the gauge transformation $A \to A + d\chi$ with $\chi$ a solution of the scalar wave equation
$$
\Box\chi \;=\; -\nabla\cdot A
$$
yields a potential satisfying $\nabla\cdot A = 0$, since $\nabla\cdot(A + d\chi) = \nabla\cdot A + \Box\chi$.

In the Lorenz gauge, the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]], which in general reads
$$
\Box A^\nu - \nabla^\nu(\nabla\cdot A) = \mu_0 J^\nu,
$$
reduces to the **wave equation** for the potential:
$$
\boxed{\;\Box A^\nu = \mu_0 J^\nu\;} \qquad (\text{Lorenz gauge}),
$$
four uncoupled scalar wave equations, one for each component of $A$ (in inertial coordinates).

The Lorenz gauge is **Lorentz-invariant**: $\nabla\cdot A$ is a scalar, so the condition holds in every inertial frame simultaneously. It does **not** fix $A$ uniquely; a **residual gauge freedom** remains, namely $A \to A + d\chi$ with $\Box\chi = 0$ (harmonic $\chi$), which preserves $\nabla\cdot A = 0$.

For comparison, the **Coulomb gauge** $\nabla\cdot\boldsymbol{\mathcal A} = 0$ imposes the vanishing of only the spatial divergence of the vector potential in a particular observer's rest space; it is not Lorentz-invariant, but it is convenient for static and bound-state problems, where it makes the scalar potential the instantaneous Coulomb potential and the vector potential purely transverse.

> Naming note: the gauge is **Lorenz** (after the Danish physicist Ludvig Lorenz, 1867), not **Lorentz** (the Dutch physicist Hendrik Lorentz of the transformation, group, factor, and force). The spelling is a genuine distinction, frequently miswritten; only the gauge is Lorenz.

---

# Relate to Other Fields / Compression

A gauge choice is the electromagnetic instance of **fixing a section of a principal bundle** — choosing, at each event, a reference for the $\mathrm{U}(1)$ phase, the bundle-theoretic content of [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|gauge theory]]. The same notion recurs whenever a theory has a redundancy: coordinate gauges in general relativity (harmonic coordinates, the analogue of Lorenz gauge), the unitary and $R_\xi$ gauges of the electroweak theory, and the conformal gauge of string theory are all conditions that fix a redundancy to make the dynamics tractable.

**True name:** the Lorenz gauge is "the divergence-free, Lorentz-invariant gauge that decouples the wave equation". This is what you reach for: it is always available, it respects boosts, and it turns $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ into $\Box A = \mu_0 J$. The defining operational fact is the reduction to four uncoupled scalar wave equations — that is the entire reason to impose it.

The compression with harmonic coordinates in general relativity is exact. There, the metric's coordinate freedom (diffeomorphisms) is the analogue of the gauge freedom, and the **harmonic** (or de Donder) gauge $\Box x^\mu = 0$, equivalently $\partial_\nu(\sqrt{-g}\,g^{\mu\nu}) = 0$, plays exactly the role of the Lorenz gauge: it decouples the linearised Einstein equations into wave equations $\Box\bar h_{\mu\nu} = -16\pi G\,T_{\mu\nu}$, the gravitational counterpart of $\Box A = \mu_0 J$, from which gravitational waves and their retarded solutions follow just as electromagnetic waves do here.

---

# Examples / Corollaries

**Is an instance — the Lorenz gauge for a static charge.** A static point charge has $A = V\underline{U_0}$ with $V = \frac{q}{4\pi\varepsilon_0 r}$ and $\boldsymbol{\mathcal A} = 0$, so $\nabla\cdot A = \nabla_\mu A^\mu = \partial_t V = 0$ (the potential is time-independent): the static Coulomb potential already satisfies the Lorenz gauge. Here the Lorenz and Coulomb gauges coincide, because nothing is time-dependent and the vector potential vanishes.

**Is an instance — the radiation gauge for a vacuum wave.** A plane wave in vacuum can be put in Lorenz gauge ($k\cdot a = 0$), and the residual freedom $A \to A + d\chi$ with $\Box\chi = 0$ can then be used to set $A_0 = 0$, the **radiation (or temporal) gauge**. This leaves $A_\mu = (0, \boldsymbol{\mathcal A})$ with $\nabla\cdot\boldsymbol{\mathcal A} = 0$, exhibiting the two transverse polarisations directly. This shows a gauge choice exploiting residual freedom on top of an earlier one.

**Is NOT an instance of a complete gauge fixing — the Lorenz condition alone.** The Lorenz gauge does *not* uniquely determine $A$: any harmonic $\chi$ (with $\Box\chi = 0$) generates a further allowed transformation. So "impose Lorenz gauge" is not a complete fixing, and a calculation that assumes $A$ is unique after Lorenz gauge is in error. To fix $A$ completely one must impose a second condition using the residual freedom.

**Is NOT an instance of a Lorentz-invariant gauge — the Coulomb gauge.** The condition $\nabla\cdot\boldsymbol{\mathcal A} = 0$ holds in one observer's frame but not after a boost: it is *not* a scalar equation, since it involves the spatial divergence in a chosen rest space. A manifestly covariant calculation must not silently use the Coulomb gauge, on pain of mixing frames. The Coulomb gauge is legitimate only inside a single fixed frame.

**Corollary — the gauge function for any target divergence is computable.** To impose any condition of the form $\nabla\cdot A = f$ for a prescribed scalar $f$, solve $\Box\chi = f - \nabla\cdot A$ for the gauge function; a solution always exists by the invertibility of $\Box$. The Lorenz gauge is the case $f = 0$. This shows the gauge freedom is "large enough" to set the divergence to anything.

**Corollary — in Lorenz gauge the potential and current satisfy the same operator equation.** Both obey $\Box(\cdot) = \mu_0 J$ versus $\nabla\cdot J = 0$: the potential satisfies the inhomogeneous wave equation with source $\mu_0 J$, and consistency requires $\nabla\cdot J = 0$ (apply $\nabla_\nu$ to $\Box A^\nu = \mu_0 J^\nu$ and use $\nabla_\nu\Box A^\nu = \Box(\nabla\cdot A) = 0$ in Lorenz gauge). So the Lorenz gauge is consistent with the wave equation *only if* charge is conserved — a built-in check.

**Calibration check.** If you have understood gauge choice and the Lorenz gauge you can: (i) show that $\nabla\cdot A \to \nabla\cdot A + \Box\chi$ under $A \to A + d\chi$, hence that solving $\Box\chi = -\nabla\cdot A$ achieves the Lorenz gauge; (ii) verify that the Lorenz gauge reduces $\Box A^\nu - \nabla^\nu(\nabla\cdot A) = \mu_0 J^\nu$ to $\Box A^\nu = \mu_0 J^\nu$; and (iii) explain why the Coulomb gauge is not Lorentz-invariant while the Lorenz gauge is, by comparing $\nabla\cdot\boldsymbol{\mathcal A}$ (a frame-dependent spatial divergence) with $\nabla\cdot A$ (a scalar).

---

# Unlocked by This

> [!tip] The Retarded Potential and Liénard–Wiechert *(from §22.2–22.3)*
> Once the Lorenz gauge reduces Maxwell to $\Box A = \mu_0 J$, the retarded Green function of the d'Alembertian solves it, giving the retarded potential and, for a single charge, the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert potential]]. The Lorenz gauge is the gauge in which this solution is transparent, and the Liénard–Wiechert potential can be checked to satisfy $\nabla\cdot A = 0$ directly.

> [!tip] Harmonic Coordinates and Gravitational Waves *(from General Relativity)*
> The Lorenz gauge has an exact counterpart in gravitation: the **harmonic (de Donder) gauge** $\partial_\nu(\sqrt{-g}\,g^{\mu\nu}) = 0$ decouples the linearised Einstein equations into wave equations $\Box\bar h_{\mu\nu} = -16\pi G\,T_{\mu\nu}$, from which **gravitational waves** propagating at $c$ and their retarded (quadrupole) solutions follow exactly as electromagnetic waves do here. The metric's gauge freedom is diffeomorphism invariance; the analogue of $\Box\chi = -\nabla\cdot A$ is the coordinate condition that achieves the harmonic gauge. See [[General Relativity I — Einstein's Equations and Schwarzschild|General Relativity I]].
