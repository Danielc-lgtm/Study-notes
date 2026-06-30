---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Def - Minkowski Space and the Metric"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus signature** $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X\cdot X > 0$. $\Phi$ is the gravitational potential (a scalar field on Minkowski spacetime); $G$ is Newton's constant; $\rho$, $\varepsilon$, $p$ are the rest-mass density, energy density, and pressure of matter. $T^{\mu\nu}$ is the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]] and $T = T^\mu{}_\mu = \eta^{\mu\nu}T_{\mu\nu}$ its **trace**. $\Box = \partial_\mu\partial^\mu = \eta^{\mu\nu}\partial_\mu\partial_\nu$ is the **d'Alembertian**; in mostly-minus, $\Box = \partial_t^2 - \nabla^2$ (with $c$: $\Box = c^{-2}\partial_t^2 - \nabla^2$), and $\nabla^2 = \Delta$ is the spatial Laplacian. $m_a$, $q_a$ are the inertial and gravitational masses of particle $a$; $\vec u_a$ its four-velocity, $\vec a_a$ its four-acceleration, $\bot_{u_a}$ the orthogonal projector onto its local rest space. Full registry on [[Special Relativity XXV — Toward Relativistic Gravitation]].

> [!warning] Convention: signature and the sign of the d'Alembertian
> Gourgoulhon, the source, uses mostly-plus $\mathrm{diag}(-1,+1,+1,+1)$, in which $\Box = -c^{-2}\partial_t^2 + \nabla^2$ and the field equation reads $\Box\Phi = -4\pi G\,T/c^2$. In our mostly-minus convention the operator flips overall sign, $\Box = +c^{-2}\partial_t^2 - \nabla^2$, and the trace $T = T^\mu{}_\mu$ also flips sign with the metric. The two conventions describe identical physics: the slowly-varying limit recovers Poisson's equation $\Delta\Phi = 4\pi G\rho$ either way. To avoid sign confusion this page states the equation in the form whose nonrelativistic limit is manifestly Poisson, and flags the source term explicitly. The one fact that is convention-independent is that the **source is the trace of the energy-momentum tensor, not the energy density**.

This is a compound page: it defines two interlocking notions — Nordström's **field equation** for the scalar potential and Nordström's **equation of motion** for a particle in the field — because they are introduced together as a single least-action theory and neither is usable without the other.

---

# Axiom Motivation

The problem is sharp: Newtonian gravity is the Poisson equation $\Delta\Phi = 4\pi G\rho$ together with the equation of motion $\ddot{\vec r} = -\vec\nabla\Phi$, and neither survives unchanged in special relativity. The Laplacian $\Delta$ is not a Lorentz-invariant operator — it picks out an observer's spatial slices — and the mass density $\rho$ is not a Lorentz scalar — it is a component of a tensor. A relativistic theory must replace both with invariant objects, and the most economical guess is that gravity, like the Newtonian potential, is described by a single scalar field $\Phi$ on Minkowski spacetime. The entire design problem is then: which invariant equation does $\Phi$ obey, and how does a particle move in it?

The left-hand side is the easy half. There is a unique natural Lorentz-invariant second-order operator on Minkowski spacetime that reduces to $\Delta$ for slowly-varying fields: the **d'Alembertian** $\Box = \partial_\mu\partial^\mu$, the wave operator. It is built from the metric, so it is invariant, and when the time derivatives are negligible compared to the spatial ones — the condition $|\partial_t^2\Phi| \ll c^2|\nabla^2\Phi|$, which holds for static and slowly-changing fields — it collapses to $-\nabla^2$ (mostly-minus) and reproduces the Laplacian. So the field equation must be of the form $\Box\Phi = (\text{source})$, the wave equation with a source. This is the same operator that governs electromagnetic waves in [[Special Relativity XXII — Maxwell's Equations|XXII]], and the choice is forced if one wants the simplest invariant generalisation of Poisson.

The right-hand side is where the subtlety lives, and getting it wrong is the most instructive mistake in the subject. The naive move is to invoke $E = mc^2$ and replace the mass density $\rho$ by the energy density $\varepsilon$. But energy density is **not a Lorentz scalar**: it is the $T^{00}$ component of the energy-momentum tensor, and it transforms under a boost both because energy itself changes and because the volume element Lorentz-contracts — so $\varepsilon$ depends on the observer in two ways. A scalar field equation must have a *scalar* source, and the only scalar one can build from the matter's energy-momentum tensor is its **trace** $T = T^\mu{}_\mu$. This is the decisive axiom: the source of scalar gravity is the trace of the energy-momentum tensor, the quantity Einstein called "Laue's scalar". One must check it reduces correctly: for ordinary matter the nonrelativistic limit of $-T/c^2$ is exactly $\rho$ (for a perfect fluid, $-T/c^2 = \rho + (\varepsilon_{\mathrm{int}} - 3p)/c^2 \to \rho$ when pressures and internal energies are small compared to rest energy), so Poisson is recovered. If we had used $\varepsilon$ the limit would also have given $\rho$ — the two agree nonrelativistically — but they differ for relativistic matter, and that difference is not academic: it is exactly why light, which has $T^{\mathrm{em}} = 0$ but nonzero energy density, exerts and feels *no* scalar gravity.

For the equation of motion, the right tool is the **principle of least action**, which has two virtues here: it determines the source self-consistently (rather than being postulated), and it gives the relativistic generalisation of $\ddot{\vec r} = -\vec\nabla\Phi$ as a by-product. The free particle already has its action, $S_{\mathrm{free}} = -\sum_a m_a\int d\tau$ from [[Special Relativity XV — The Principle of Least Action|XV]]; gravity is added through an interaction term in which the particle couples to $\Phi$ with a **gravitational charge** $q_a$. The crucial axiom — the one that singles gravity out from electromagnetism — is to set the gravitational charge equal to the inertial mass, $q_a = m_a$. This hardwires the **equality of gravitational and inertial mass** into the theory from the start: because the coupling is the mass itself, the acceleration a particle suffers is independent of its mass, so all bodies fall the same way. Were $q_a$ an independent charge (as the electric charge is in electromagnetism), different particles would fall differently, contradicting the universality of free fall. The whole physical character of gravity is encoded in the single substitution $q_a = m_a$.

What if one weakened or altered each piece? If the operator were not the full d'Alembertian but, say, $\partial_t^2 + \nabla^2$ (Euclidean), the equation would not be hyperbolic and would have no causal wave propagation — gravity would act instantaneously, as in Newton, violating relativity. If the source were $\varepsilon$ instead of $T$, the equation would not be Lorentz-covariant (its right-hand side would not be a scalar), so it would hold in only one frame. If the gravitational charge were independent of the mass, the equivalence principle would fail and the theory would predict composition-dependent free fall, ruled out by Eötvös to $3\times 10^{-13}$. Each axiom is forced by a non-negotiable requirement: covariance forces the d'Alembertian, scalarity forces the trace, and universality forces $q = m$.

---

# The Definition

**Nordström's scalar theory of gravity** describes gravitation by a single scalar field $\Phi$ on Minkowski spacetime, governed by two equations derived from the action $S = S_{\mathrm{field}} + S_{\mathrm{inter}} + S_{\mathrm{free}}$.

The **field action** is the massless Klein-Gordon (scalar kinetic) action with a gravitational coupling constant,
$$
S_{\mathrm{field}} = -\frac{1}{8\pi G c}\int_{\mathscr{U}} \eta^{\mu\nu}\,\frac{\partial\Phi}{\partial x^\mu}\frac{\partial\Phi}{\partial x^\nu}\,dU,
$$
where $\mathscr{U}$ is a four-dimensional region of spacetime and $dU$ the invariant volume element; the constant $4\pi G c$ is the coupling between field and matter. The **interaction action**, for a system of particles with the gravitational charge set equal to the inertial mass ($q_a = m_a$), is
$$
S_{\mathrm{inter}} = -\frac{1}{c}\sum_a m_a\int_{\lambda_1}^{\lambda_2} \Phi\big(x_a^\alpha(\lambda)\big)\,\sqrt{\eta_{\alpha\beta}\,\dot x_a^\alpha\,\dot x_a^\beta}\;d\lambda,
$$
and the **free action** is $S_{\mathrm{free}} = -\sum_a m_a c\int\sqrt{\eta_{\alpha\beta}\dot x_a^\alpha\dot x_a^\beta}\,d\lambda$.

Varying $S$ with respect to $\Phi$ gives the **field equation**
$$
\boxed{\;\Box\Phi = -\frac{4\pi G}{c^2}\,T\;}
\qquad\Longleftrightarrow\qquad
\Box\Phi = 4\pi G\,\mathcal{S},\quad \mathcal{S} := -\frac{T}{c^2},
$$
where $T = T^\mu{}_\mu$ is the trace of the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]] of all matter and non-gravitational fields. In the weak-field, slowly-varying limit $\Box\to -\nabla^2$ and $-T/c^2 \to \rho$, recovering **Poisson's equation** $\Delta\Phi = 4\pi G\rho$.

Varying $S$ with respect to the worldline $x_a^\alpha$ gives the **equation of motion**
$$
\boxed{\;(c^2 + \Phi)\,\vec a_a = -\vec\nabla\Phi\circ\bot_{u_a}\;}
$$
or, in components with respect to inertial coordinates and with $\tau_a$ the proper time of particle $a$,
$$
\left(1 + \frac{\Phi}{c^2}\right)\frac{d^2 x_a^\alpha}{d\tau_a^2} = -\left(\eta^{\alpha\beta} + \frac{1}{c^2}\frac{dx_a^\alpha}{d\tau_a}\frac{dx_a^\beta}{d\tau_a}\right)\frac{\partial\Phi}{\partial x^\beta},
$$
where $\vec a_a$ is the four-acceleration and $\bot_{u_a}$ the orthogonal projector onto the local rest space. The spatial components ($\alpha = i$) reduce, in the nonrelativistic limit $|\Phi|/c^2 \ll 1$ and $|d x_a^i/d\tau_a| \ll c$, to Newton's law $\ddot{\vec r} = -\vec\nabla\Phi$.

The theory is equivalently written in the **nonlinear Nordström form**: defining the matter stress tensor as it enters the conserved total tensor, the field equation becomes
$$
\left(1 + \frac{\Phi}{c^2}\right)\Box\Phi = -\frac{4\pi G}{c^2}\,T_{\mathrm{mat}},
$$
which is manifestly nonlinear in $\Phi$, and is the form Nordström published in 1913.

Finally, Einstein and Fokker showed the theory is a **metric** theory: particles follow geodesics of the conformally rescaled metric
$$
\tilde g = \left(1 + \frac{\Phi}{c^2}\right)^2 \eta,
$$
which has the same light cones as $\eta$ (so light is unbent) but rescaled proper times (so clocks are redshifted). In this form $\Phi$ disappears and only $\tilde g$ remains as the physical metric.

---

# Categorical / Structural Definition

Structurally, Nordström's theory is the **spin-0** entry in the classification of relativistic gravity theories by the spin (Lorentz-representation type) of the mediating field: scalar (spin-0, this theory), vector (spin-1, [[Def - Vector and Tensor Theories of Gravity|the vector theory]]), tensor (spin-2, the precursor of general relativity). A relativistic field theory is specified by the representation of the [[Def - The Lorentz Group|Lorentz group]] under which its field transforms and by a Lorentz-scalar Lagrangian; the scalar choice is the trivial representation, the field $\Phi$ being invariant under Lorentz transformations. The coupling to matter is then necessarily through the unique Lorentz scalar built from the matter, namely the trace $T = T^\mu{}_\mu$ of the energy-momentum tensor — there is no other invariant a scalar field can couple to. This structural fact, that *a scalar field couples only to the trace*, is what determines the theory's entire observational profile: matter with traceless stress (radiation) is invisible to it.

In the Einstein-Fokker reformulation the theory acquires a second structural identity: it is the **conformally flat** metric theory. Its physical metric $\tilde g = \Omega^2\eta$ with $\Omega = 1 + \Phi/c^2$ is conformal to Minkowski space, meaning it lies in the conformal equivalence class of the flat metric. Conformal metrics form an object of independent interest — they share null geodesics (light cones) but not timelike geodesics — and Nordström's theory is precisely the gravity theory in which spacetime is conformally flat. General relativity's metrics are *not* in general conformally flat (the Weyl tensor, the conformally-invariant part of curvature, is nonzero), and that is the invariant geometric statement of why general relativity bends light where Nordström's theory does not.

---

# Relate to Other Fields / Compression

Nordström's field equation is the **sourced wave equation** of mathematical physics, $\Box\Phi = \rho_{\mathrm{source}}$, the same equation that governs the electromagnetic potential in Lorenz gauge ([[Special Relativity XXII — Maxwell's Equations|XXII]]) and the Klein-Gordon field in quantum field theory. What distinguishes the gravitational case is purely the source: the trace of the stress tensor rather than a charge-current. The solution methods — retarded Green's functions, multipole expansions — are identical, which is why Nordström's theory, like electromagnetism, predicts gravitational waves (propagating at $c$) and a $1/r$ static potential.

**True name:** Nordström's theory is *"general relativity restricted to conformally-flat metrics"*. Its physical content is entirely captured by the statement that the spacetime metric is $\tilde g = (1+\Phi/c^2)^2\eta$, a conformal rescaling of Minkowski space. Everything else — the field equation, the equation of motion, the redshift, the absence of light bending — follows from this single geometric fact. This is the most operational way to hold the theory: it is the gravity you get if you are allowed to rescale clocks but not to tilt light cones.

In the language of general relativity, Nordström's theory is the statement $R = \tfrac{24\pi G}{c^4}T$, where $R$ is the scalar curvature and $T$ the trace of the stress tensor — a *single scalar equation* relating the trace of the curvature to the trace of the source. Einstein's theory replaces this by ten equations, $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \tfrac{8\pi G}{c^4}T_{\mu\nu}$, relating the full Ricci tensor to the full stress tensor. Nordström's is the "trace part" of Einstein's; the nine remaining equations, which Nordström's theory sets trivially to the conformal condition, are exactly what bend light and give the correct perihelion advance.

---

# Examples / Corollaries

**Is an instance — the static field of a point mass.** For a point mass $M$ at rest, the matter is dust with $T = \rho c^2$ (the dust trace equals its rest-energy density), and the field equation in the static limit is $\nabla^2\Phi = 4\pi G\rho$ with solution $\Phi = -GM/r$ — exactly the Newtonian potential. So Nordström's theory reproduces Newtonian gravity for static, slow, pressureless matter, as any acceptable theory must.

**Is an instance — the perfect-fluid source.** For a [[Def - Perfect Fluid|perfect fluid]] with energy density $\varepsilon$ and pressure $p$, the trace is $T = \varepsilon - 3p$ (computed from $T^\mu{}_\mu = (\varepsilon + p)u^\mu u_\mu - 4p = (\varepsilon+p) - 4p$ using $u^\mu u_\mu = 1$), so the source is $-T/c^2 = (3p - \varepsilon)/c^2$. Splitting $\varepsilon = \rho c^2 + \varepsilon_{\mathrm{int}}$ gives $-T/c^2 = \rho + (\varepsilon_{\mathrm{int}} - 3p)/c^2$, which tends to the mass density $\rho$ when internal energy and pressure are small compared to rest energy. The pressure thus gravitates in this theory — with a relative sign ($+3p$) that is a genuine relativistic correction to the Newtonian source.

**Is NOT an instance — the electromagnetic field as a source.** The electromagnetic field has a **traceless** energy-momentum tensor, $T^{\mathrm{em}} = \varepsilon_0(F_{\mu\alpha}F^{\mu\alpha} - \tfrac14 F_{\mu\nu}F^{\mu\nu}\cdot 4) = 0$ identically, because the two terms cancel. Therefore the electromagnetic field is *not* a source of scalar gravity: an electromagnetic wave, or the light from a star, produces no Nordström field and feels none. This is not a peculiarity to be patched but the theory's fatal flaw — it means light does not bend in a gravitational field, contradicting observation.

**Is NOT an instance — a theory with an independent gravitational charge.** If one set $q_a \neq m_a$ — an independent "gravitational charge" — the resulting theory would still be a well-posed scalar field theory, but it would *not* be Nordström's theory of *gravity*, because the acceleration $\vec a_a \approx -(q_a/m_a)\vec\nabla\Phi/c^2$ would depend on the charge-to-mass ratio, so different bodies would fall differently. Such a theory describes a long-range scalar force (a "fifth force"), not gravity; the equality $q_a = m_a$ is precisely what makes it gravity.

**Corollary — the theory predicts a gravitational redshift.** Because the Einstein-Fokker metric $\tilde g = (1+\Phi/c^2)^2\eta$ rescales proper time by the conformal factor, a clock at potential $\Phi$ runs at rate $(1+\Phi/c^2)$ relative to a clock at $\Phi = 0$. Two clocks at different potentials therefore disagree, by $\Delta\nu/\nu = \Delta\Phi/c^2$ — the gravitational redshift. So Nordström's theory *does* predict the redshift (this is generic to any metric theory, see [[Thm - Gravitational Redshift]]); it is the *deflection of light* it fails to predict.

**Calibration check.** The reader should be able to verify, after reading: (i) that the source of the field equation is $-T/c^2$ and reduces to $\rho$ for slow pressureless matter; (ii) that the electromagnetic trace $T^{\mathrm{em}} = 0$ vanishes because $\varepsilon_0(F_{\mu\alpha}F^{\mu\alpha} - F_{\mu\nu}F^{\mu\nu}) = 0$, so light does not couple; and (iii) that setting $q_a = m_a$ in the interaction action is what makes the free-fall acceleration mass-independent.

---

# Unlocked by This

> [!tip] The Einstein-Fokker Conformal Reformulation *(from the History of General Relativity)*
> Recognising Nordström's theory as the conformal metric theory $\tilde g = (1+\Phi/c^2)^2\eta$ was the **first time a gravity theory was written as pure geometry**, with the gravitational field absorbed entirely into a spacetime metric and particles moving on its geodesics. This was the conceptual template Einstein generalised: drop the restriction to conformally-flat metrics, let the metric be an arbitrary Lorentzian field $g_{\mu\nu}(x)$, and one has general relativity. Nordström's theory is the dress rehearsal for the metric idea — see [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Scalar-Tensor Theories and the Brans-Dicke Field *(from Modern Gravity)*
> A scalar gravitational field did not die with Nordström. Modern **scalar-tensor theories** keep general relativity's tensor metric but add a scalar field alongside it — the **Brans-Dicke** field is the prototype — to encode a position-dependent gravitational "constant". These theories are tightly constrained by exactly the observations that killed pure scalar gravity (light deflection, perihelion advance), and the residual scalar is now a leading candidate for **dark energy** (quintessence) and appears as the **dilaton** in string theory. Nordström's lesson — that a scalar couples to the trace of the stress tensor — is the organising principle of all of them.
