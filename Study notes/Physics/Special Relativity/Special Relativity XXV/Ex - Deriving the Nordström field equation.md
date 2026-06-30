---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Nordström's Scalar Theory of Gravity"
  - "Def - The Energy-Momentum Tensor"
  - "Thm - Mass-Energy Equivalence"
tags: [physics, special-relativity]
---

# Problem Statement

Gravity is to be described by a single scalar field $\Phi$ on Minkowski spacetime, coupled to a system of particles through the action $S = S_{\mathrm{field}} + S_{\mathrm{inter}} + S_{\mathrm{free}}$ with (in mostly-minus, $c = 1$)
$$
S_{\mathrm{field}} = -\frac{1}{8\pi G}\int_{\mathscr{U}} \eta^{\mu\nu}\,\partial_\mu\Phi\,\partial_\nu\Phi\,dU, \qquad
S_{\mathrm{inter}} = -\sum_a m_a\int \Phi\big(x_a(\lambda)\big)\sqrt{\eta_{\alpha\beta}\dot x_a^\alpha\dot x_a^\beta}\,d\lambda,
$$
where the gravitational charge has been set equal to the inertial mass $m_a$.

1. By varying $S$ with respect to $\Phi$, show that the field equation is $\Box\Phi = -4\pi G\,T/c^2$, where $T = T^\mu{}_\mu$ is the trace of the energy-momentum tensor, and identify the source as $\mathcal{S} = -T/c^2$.
2. Show that for a slowly-varying weak field this reduces to Poisson's equation $\Delta\Phi = 4\pi G\rho$.
3. Explain why the source is the *trace* $T$ and not the energy density $\varepsilon$, even though $E = mc^2$ would suggest energy density.
4. For a perfect fluid, compute the trace $T = \varepsilon - 3p$ and verify it tends to $\rho c^2$ in the nonrelativistic limit.

**Recall:**

![[Def - Nordström's Scalar Theory of Gravity#The Definition]]

The **energy-momentum tensor** $T^{\mu\nu}$ has trace $T = T^\mu{}_\mu = \eta^{\mu\nu}T_{\mu\nu}$; for a [[Def - Perfect Fluid|perfect fluid]] $T^{\mu\nu} = (\varepsilon + p)u^\mu u^\nu - p\,\eta^{\mu\nu}$ with $u^\mu u_\mu = 1$ (mostly-minus). The d'Alembertian is $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu = c^{-2}\partial_t^2 - \nabla^2$, reducing to $-\nabla^2$ for slowly-varying fields. By [[Thm - Mass-Energy Equivalence|mass-energy equivalence]] the energy density splits as $\varepsilon = \rho c^2 + \varepsilon_{\mathrm{int}}$.

---

# Convergent Strategy

**Problem class.** A *derive-a-field-equation-from-an-action* problem, of the kind solved in [[Special Relativity XXII — Maxwell's Equations|XXII]] for Maxwell and [[Special Relativity XV — The Principle of Least Action|XV]] for the particle: write the action, vary with respect to the field, set the variation to zero, read off the Euler-Lagrange equation. The interaction term must be rewritten as a spacetime integral before it can be varied against a field defined everywhere.

**Assumption pattern.** Two ingredients are present: a Klein-Gordon-type kinetic action (whose variation gives $\Box\Phi$) and a particle-coupling term (whose variation gives the source). The source emerges from rewriting the one-dimensional worldline integral in $S_{\mathrm{inter}}$ as a four-dimensional integral using a Dirac measure, after which the coefficient of $\Phi$ is recognised as the trace of the stress tensor. The condition $q_a = m_a$ is what makes the coupling universal.

**Theorem routing.** The variation of $S_{\mathrm{field}}$ uses integration by parts to move the derivative off $\delta\Phi$, giving $\Box\Phi$; see [[Def - Nordström's Scalar Theory of Gravity]]. The source comes from the trace of the [[Def - The Energy-Momentum Tensor|energy-momentum tensor]], which for particles is $T = -\sum_a m_a\int\delta_{A_a}\,d\tau$ (up to a factor). The Newtonian limit uses the slow-field collapse $\Box \to -\nabla^2$ and the trace's nonrelativistic limit $-T/c^2 \to \rho$.

**Key decision point.** The crux is recognising that the coefficient of $\Phi$ in the rewritten interaction Lagrangian *is* the trace of the energy-momentum tensor — this is not obvious from the action and is the step that determines the source. The natural alternative, guessing the source is the energy density $\varepsilon$, is wrong because $\varepsilon$ is not a Lorentz scalar; only the trace is, and the action forces it.

---

# Legal Operations Used

1. **Take the Newtonian (weak, slow) limit** (operation 1 from the topic page): in part 2, drop the time derivative so $\Box\Phi \to -\nabla^2\Phi$, and identify the nonrelativistic limit of the source $-T/c^2 \to \rho$, recovering Poisson.

2. **Compute the trace of the energy-momentum tensor** (operation 3 from the topic page): in parts 1 and 4, the source is the trace $T = T^\mu{}_\mu$, computed for the particle system (giving $\Box\Phi \propto T$) and for a perfect fluid (giving $T = \varepsilon - 3p$).

3. **Set the gravitational charge equal to the inertial mass** (operation 4 from the topic page): the interaction term uses $q_a = m_a$, which is what makes the trace appear (rather than some independent charge density) and builds in the equivalence principle.

---

# Hints

> [!note]- Hint 1
> Vary $S_{\mathrm{field}}$ first. With $S_{\mathrm{field}} = -\frac{1}{8\pi G}\int\eta^{\mu\nu}\partial_\mu\Phi\,\partial_\nu\Phi\,dU$, the variation $\delta S_{\mathrm{field}} = -\frac{1}{4\pi G}\int\eta^{\mu\nu}\partial_\mu\Phi\,\partial_\nu(\delta\Phi)\,dU$; integrate by parts to get $+\frac{1}{4\pi G}\int(\Box\Phi)\,\delta\Phi\,dU$.

> [!note]- Hint 2
> For $S_{\mathrm{inter}}$, rewrite the worldline integral as a spacetime integral using the Dirac measure: $\int\Phi(x_a(\lambda))\,(\cdots)\,d\lambda = \int_{\mathscr{U}}\Phi(x)\,\big[\int\delta_{A_a}(x)\,(\cdots)\,d\lambda\big]\,dU$. The bracket, summed over particles, is (up to a factor $c^3$) the trace $T$ of the energy-momentum tensor — this is the key identification.

> [!note]- Hint 3
> Setting $\delta S/\delta\Phi = 0$ gives $\frac{1}{4\pi G}\Box\Phi + \frac{1}{c^3}T = 0$ (with $c$ restored appropriately), i.e. $\Box\Phi = -4\pi G\,T/c^2$. The source is $\mathcal{S} = -T/c^2$.

> [!note]- Hint 4
> For the perfect-fluid trace: $T = \eta^{\mu\nu}T_{\mu\nu} = (\varepsilon+p)u^\mu u_\mu - p\,\eta^{\mu\nu}\eta_{\mu\nu} = (\varepsilon+p)(1) - p(4) = \varepsilon - 3p$. Then $-T/c^2 = (3p-\varepsilon)/c^2 = \rho + (\varepsilon_{\mathrm{int}}-3p)/c^2 \to \rho$ when pressure and internal energy are small.

---

# Solution

The derivation breaks into three moves. Step 1 varies the kinetic action to produce $\Box\Phi$. Step 2 rewrites the particle coupling as a spacetime integral and reads off the source as the trace $T$. Step 3 takes the Newtonian limit and computes the fluid trace. The non-obvious move is in Step 2, where the worldline integral becomes a four-dimensional one whose coefficient of $\Phi$ is exactly the trace of the energy-momentum tensor.

**Step 1: Varying $S_{\mathrm{field}}$ gives $\Box\Phi$.**

> [!note]- Derivation
> The field action is $S_{\mathrm{field}} = -\frac{1}{8\pi G}\int_{\mathscr{U}}\eta^{\mu\nu}\partial_\mu\Phi\,\partial_\nu\Phi\,dU$. Vary $\Phi \to \Phi + \delta\Phi$:
> $$\delta S_{\mathrm{field}} = -\frac{1}{8\pi G}\int 2\,\eta^{\mu\nu}\partial_\mu\Phi\,\partial_\nu(\delta\Phi)\,dU = -\frac{1}{4\pi G}\int \eta^{\mu\nu}\partial_\mu\Phi\,\partial_\nu(\delta\Phi)\,dU.$$
> Integrate by parts (the boundary term vanishes for variations supported in the interior of $\mathscr{U}$):
> $$\delta S_{\mathrm{field}} = +\frac{1}{4\pi G}\int \eta^{\mu\nu}\partial_\mu\partial_\nu\Phi\;\delta\Phi\,dU = \frac{1}{4\pi G}\int (\Box\Phi)\,\delta\Phi\,dU,$$
> using $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$. This is the kinetic contribution to the Euler-Lagrange equation.

**Step 2: Varying $S_{\mathrm{inter}}$ gives the source $-T/c^2$.**

> [!note]- Derivation
> The interaction action $S_{\mathrm{inter}} = -\sum_a m_a\int\Phi(x_a(\lambda))\sqrt{\eta_{\alpha\beta}\dot x_a^\alpha\dot x_a^\beta}\,d\lambda$ is a sum of one-dimensional integrals; to vary it against the field $\Phi(x)$ defined on all of spacetime, rewrite each as a four-dimensional integral using the Dirac measure $\delta_{A_a}(x)$ concentrated on the worldline $\mathscr{L}_a$. Choosing proper time $\tau_a$ as the parameter ($\sqrt{\eta_{\alpha\beta}\dot x^\alpha\dot x^\beta}\,d\lambda = c\,d\tau$):
> $$S_{\mathrm{inter}} = -\sum_a m_a c\int \Phi(A_a(\tau))\,d\tau = \int_{\mathscr{U}}\Phi(x)\underbrace{\Big[-\sum_a m_a c\int \delta_{A_a(\tau)}(x)\,d\tau\Big]}_{=\,T/c^3}\,dU.$$
> The bracket is recognised as $T/c^3$, where $T$ is the trace of the energy-momentum tensor of the particle system: using the simple-particle relation $p_a = m_a c\,u_a$ and contracting $\vec T$ with the metric (the $C^1_1$ contraction), $T = T^\mu{}_\mu = -\sum_a m_a c^3\int\delta_{A_a(\tau)}\,d\tau$ (the sign from $u_a^\mu (u_a)_\mu = 1$ in mostly-minus, translated from Gourgoulhon's $-1$). Hence $\mathscr{L}_{\mathrm{inter}} = \frac{1}{c^3}\Phi T$, and
> $$\delta S_{\mathrm{inter}} = \int_{\mathscr{U}}\frac{T}{c^3}\,\delta\Phi\,dU.$$

**Step 3: Assembling the field equation and taking the limit.**

> [!note]- Derivation
> Setting $\delta S = \delta S_{\mathrm{field}} + \delta S_{\mathrm{inter}} = 0$ for all $\delta\Phi$:
> $$\frac{1}{4\pi G}\Box\Phi + \frac{T}{c^3} = 0 \quad\Longrightarrow\quad \boxed{\Box\Phi = -\frac{4\pi G}{c^2}\,T}, \quad \mathcal{S} = -\frac{T}{c^2}.$$
> **Newtonian limit (part 2).** For a slowly-varying field $|c^{-2}\partial_t^2\Phi| \ll |\nabla^2\Phi|$, so $\Box\Phi \to -\nabla^2\Phi$. The source for nonrelativistic matter is $-T/c^2 \to \rho$ (next paragraph). Hence $-\nabla^2\Phi = -4\pi G\rho \cdot(-1)$... carefully: $\Box\Phi = -4\pi G T/c^2$ becomes $-\nabla^2\Phi = -4\pi G\rho$, i.e. $\nabla^2\Phi = 4\pi G\rho$ — Poisson's equation. $\checkmark$
>
> **Perfect-fluid trace (part 4).** With $T^{\mu\nu} = (\varepsilon+p)u^\mu u^\nu - p\eta^{\mu\nu}$,
> $$T = \eta_{\mu\nu}T^{\mu\nu} = (\varepsilon+p)\,u^\mu u_\mu - p\,\delta^\mu_\mu = (\varepsilon+p)(1) - 4p = \varepsilon - 3p,$$
> using $u^\mu u_\mu = 1$ and $\delta^\mu_\mu = 4$. Splitting $\varepsilon = \rho c^2 + \varepsilon_{\mathrm{int}}$:
> $$-\frac{T}{c^2} = \frac{3p - \varepsilon}{c^2} = \rho + \frac{\varepsilon_{\mathrm{int}} - 3p}{c^2} \;\xrightarrow{\ p,\varepsilon_{\mathrm{int}}\,\ll\,\rho c^2\ }\; \rho. \quad\checkmark$$

**Step 4: Why the trace, not the energy density (part 3).**

> [!note]- Derivation
> The naive guess "$\mathcal{S} = \varepsilon/c^2$", motivated by $E = mc^2$, fails because $\varepsilon$ is **not a Lorentz scalar**: it is the $T^{00}$ component of a tensor, and under a boost it changes both because energy transforms and because the volume element Lorentz-contracts. A scalar field equation $\Box\Phi = \mathcal{S}$ must have a scalar right-hand side, or it would hold in only one frame. The only Lorentz scalar one can build from the matter's energy-momentum tensor is its trace $T = T^\mu{}_\mu$, and the action *derives* this rather than leaving it to be guessed — the coefficient of $\Phi$ in the rewritten interaction is forced to be $T$. The two candidates agree nonrelativistically ($-T/c^2$ and $\varepsilon/c^2$ both tend to $\rho$), but they differ for relativistic matter, and the difference is physical: the electromagnetic field has $T^{\mathrm{em}} = 0$ but $\varepsilon^{\mathrm{em}} \neq 0$, so the trace says light does not gravitate while the energy density would say it does. The trace is correct, and the consequence — no light bending in scalar gravity — is what kills the theory.

> [!note]- Complete formal solution
> Varying $S_{\mathrm{field}} = -\frac{1}{8\pi G}\int\eta^{\mu\nu}\partial_\mu\Phi\,\partial_\nu\Phi\,dU$ and integrating by parts gives $\delta S_{\mathrm{field}} = \frac{1}{4\pi G}\int(\Box\Phi)\delta\Phi\,dU$. Rewriting $S_{\mathrm{inter}} = -\sum_a m_a c\int\Phi\,d\tau$ as a spacetime integral via the Dirac measure identifies its integrand's coefficient of $\Phi$ as $T/c^3$, where $T = T^\mu{}_\mu = -\sum_a m_a c^3\int\delta_{A_a}\,d\tau$ is the trace of the energy-momentum tensor, so $\delta S_{\mathrm{inter}} = \int\frac{T}{c^3}\delta\Phi\,dU$. Stationarity $\delta S = 0$ for all $\delta\Phi$ yields $\Box\Phi = -4\pi G\,T/c^2$, with source $\mathcal{S} = -T/c^2$. For slowly-varying weak fields $\Box \to -\nabla^2$ and $-T/c^2 \to \rho$, giving Poisson $\nabla^2\Phi = 4\pi G\rho$. The source is the trace, not $\varepsilon$, because only the trace is a Lorentz scalar; the two agree nonrelativistically but differ for relativistic matter (e.g. the traceless electromagnetic field). For a perfect fluid $T = (\varepsilon+p)u^\mu u_\mu - 4p = \varepsilon - 3p$, and $-T/c^2 = \rho + (\varepsilon_{\mathrm{int}}-3p)/c^2 \to \rho$. $\blacksquare$

---

# Key Takeaways

**A scalar field couples to the trace of the stress tensor — this is the master fact of scalar gravity and the reason it fails.** The single most important thing this exercise teaches is that the source of a scalar field equation must be a Lorentz scalar, and the only scalar built from matter is the trace $T = T^\mu{}_\mu$ of the energy-momentum tensor. The naive replacement of mass density by energy density (motivated by $E = mc^2$) is wrong because energy density is a tensor component, not a scalar. The trigger to recognise this pattern: any time a scalar field must couple to matter, ask for the trace, and remember that conformally invariant matter (radiation, the electromagnetic field) is traceless and therefore decoupled. This one fact propagates through all of scalar gravity, the dilaton, and scale-invariance arguments in field theory — a scalar sees only the trace, so it is blind to anything traceless.

**Rewriting a worldline integral as a spacetime integral via the Dirac measure is the standard bridge between particle and field descriptions.** The technical heart of the derivation — turning $S_{\mathrm{inter}} = -\sum_a m_a\int\Phi\,d\tau$, a sum of one-dimensional integrals, into a four-dimensional integral $\int\Phi\,(T/c^3)\,dU$ — is a move that recurs throughout field theory whenever point particles source a continuous field (it is how the charge-current four-vector arises in electromagnetism, how matter sources gravity, and how the stress tensor of particles is defined). The trigger is a coupling between a localised object (worldline, point charge) and a field defined everywhere: introduce the Dirac measure on the support of the object, and the coefficient of the field in the resulting spacetime integral is the relevant source density. Recognising the trace of the stress tensor in that coefficient is the payoff that determines the physics.

**The Newtonian limit is the universal calibration of any relativistic gravity equation, and it fixes the coupling constant.** Every candidate gravity theory must reduce to $\nabla^2\Phi = 4\pi G\rho$ in the weak, slow limit, and checking this is both a sanity test and the way the numerical coupling ($4\pi G/c^2$ here, $8\pi G/c^4$ in Einstein's equation) is pinned down. The procedure is mechanical: drop the time derivative in the d'Alembertian (so $\Box \to -\nabla^2$) and take the nonrelativistic limit of the source (so $-T/c^2 \to \rho$). The deeper lesson, visible in part 4, is that the relativistic source differs from the Newtonian one by *pressure and internal-energy terms* ($+3p$, $\varepsilon_{\mathrm{int}}$) that vanish nonrelativistically but matter for relativistic matter — pressure gravitates, a genuinely post-Newtonian effect that distinguishes the relativistic theory from Newton's even before one reaches the failures of the scalar theory.
