---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
  - "Def - Relativistic Action of a Free Particle"
  - "Def - The Legendre Transform"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

Starting from the inertial-observer free Lagrangian $L = -m\sqrt{1 - \mathbf{v}^2}$ (with $c = 1$, $\mathbf{v}$ the three-velocity), construct the Hamiltonian by Legendre transform.

1. Compute the conjugate three-momentum $\mathbf{p} = \partial L/\partial\mathbf{v}$ and invert it to express $\mathbf{v}$ in terms of $\mathbf{p}$.
2. Form $H = \mathbf{p}\cdot\mathbf{v} - L$ and show $H = \sqrt{\mathbf{p}^2 + m^2}$.
3. Verify Hamilton's equations $\dot{\mathbf{x}} = \partial H/\partial\mathbf{p}$ and $\dot{\mathbf{p}} = -\partial H/\partial\mathbf{x}$ reproduce the free equation of motion, and confirm $H = E = m\gamma$ is the energy.
4. Add a scalar potential $V(\mathbf{x})$ and a vector potential to obtain the charged-particle Hamiltonian $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} + q\phi$. Take the non-relativistic limit and recover the Newtonian Hamiltonian.

**Recall:**

![[Def - Generalized Four-Momentum and the Relativistic Hamiltonian#The Definition]]

The [[Def - The Legendre Transform|Legendre transform]] of a Lagrangian $L(\mathbf{x}, \mathbf{v})$ is $H(\mathbf{x}, \mathbf{p}) = \mathbf{p}\cdot\mathbf{v} - L$ with $\mathbf{p} = \partial L/\partial\mathbf{v}$, *provided* this relation is invertible for $\mathbf{v}$. The inertial-observer Lagrangian $-m\sqrt{1 - \mathbf{v}^2}$ is non-degenerate in $\mathbf{v}$ (unlike the covariant $-m\sqrt{\eta\dot x\dot x}$, whose Legendre transform fails), so the ordinary recipe applies. The relativistic energy is $E = m\gamma$ and momentum $\mathbf{p} = m\gamma\mathbf{v}$ ([[Def - Four-Momentum and Rest Mass]]).

---

# Convergent Strategy

**Problem class.** A *Legendre-transform-to-a-Hamiltonian* problem, the standard passage from the Lagrangian to the Hamiltonian picture (operation 6 of the [[Special Relativity XV — The Principle of Least Action#Legal Operations|topic]]). The key is that the inertial-observer Lagrangian is non-degenerate, so the transform succeeds — unlike the covariant case.

**Assumption pattern.** The Lagrangian is in the inertial-observer form $-m\sqrt{1 - \mathbf{v}^2}$, a function of the three-velocity $\mathbf{v}$ that is *not* homogeneous of degree one (it equals $-m \neq 0$ at $\mathbf{v} = 0$), so its Hessian in $\mathbf{v}$ is invertible and the Legendre map $\mathbf{v} \mapsto \mathbf{p}$ can be inverted.

**Theorem routing.** Differentiate [[Def - Relativistic Action of a Free Particle|the inertial-observer Lagrangian]] to get $\mathbf{p} = m\gamma\mathbf{v}$; invert for $\mathbf{v}(\mathbf{p})$; form the [[Def - The Legendre Transform|Legendre transform]] $H = \mathbf{p}\cdot\mathbf{v} - L$; simplify to $\sqrt{\mathbf{p}^2 + m^2}$ ([[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]); verify Hamilton's equations; and add potentials for the charged case.

**Key decision point.** The crux is the inversion $\mathbf{p} = m\gamma\mathbf{v} \Rightarrow \mathbf{v} = \mathbf{p}/\sqrt{\mathbf{p}^2 + m^2}$, which requires solving for $\gamma$ in terms of $\mathbf{p}$. The trick is to compute $\mathbf{p}^2 = m^2\gamma^2\mathbf{v}^2 = m^2(\gamma^2 - 1)$ (using $\gamma^2\mathbf{v}^2 = \gamma^2 - 1$), giving $\gamma = \sqrt{1 + \mathbf{p}^2/m^2} = \sqrt{\mathbf{p}^2 + m^2}/m$, so $H = m\gamma = \sqrt{\mathbf{p}^2 + m^2}$ directly. Recognising $\gamma^2\mathbf{v}^2 = \gamma^2 - 1$ is the algebraic shortcut.

---

# Legal Operations Used

1. **Switch to the inertial-observer Lagrangian for explicit computation** (operation 8 from the topic page). The non-covariant form $-m\sqrt{1 - \mathbf{v}^2}$ admits an honest Legendre transform.

2. **Perform the Legendre transform** (operation 6). Since this Lagrangian is non-degenerate, $H = \mathbf{p}\cdot\mathbf{v} - L$ with $\mathbf{p} = \partial L/\partial\mathbf{v}$ gives a genuine Hamiltonian.

3. **Compute the generalized momentum** (operation 5). Here $\mathbf{p} = m\gamma\mathbf{v}$, the relativistic three-momentum.

---

# Hints

> [!note]- Hint 1
> $\mathbf{p} = \partial L/\partial\mathbf{v} = -m\cdot\tfrac{-\mathbf{v}}{\sqrt{1-\mathbf{v}^2}} = \tfrac{m\mathbf{v}}{\sqrt{1-\mathbf{v}^2}} = m\gamma\mathbf{v}$. To invert: $\mathbf{p}^2 = m^2\gamma^2\mathbf{v}^2$, and $\gamma^2\mathbf{v}^2 = \gamma^2(1 - 1/\gamma^2) = \gamma^2 - 1$, so $\mathbf{p}^2 = m^2(\gamma^2 - 1)$, giving $\gamma = \sqrt{1 + \mathbf{p}^2/m^2}$.

> [!note]- Hint 2
> $H = \mathbf{p}\cdot\mathbf{v} - L = m\gamma\mathbf{v}^2 + m\sqrt{1-\mathbf{v}^2} = m\gamma\mathbf{v}^2 + m/\gamma$. Use $\mathbf{v}^2 = 1 - 1/\gamma^2$: $H = m\gamma(1 - 1/\gamma^2) + m/\gamma = m\gamma - m/\gamma + m/\gamma = m\gamma = \sqrt{\mathbf{p}^2 + m^2}$.

> [!note]- Hint 3
> $\partial H/\partial\mathbf{p} = \mathbf{p}/\sqrt{\mathbf{p}^2 + m^2} = \mathbf{p}/(m\gamma) = \mathbf{v}$ ✓ (recovers $\mathbf{p} = m\gamma\mathbf{v}$). For a free particle $\partial H/\partial\mathbf{x} = 0$, so $\dot{\mathbf{p}} = 0$, momentum conservation. And $H = m\gamma = E$, the energy.

> [!note]- Hint 4
> Minimal substitution $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$ in the kinetic part and add $q\phi$: $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} + q\phi$. Non-relativistic limit: $\sqrt{(\mathbf{p}-q\mathbf{A})^2 + m^2} \approx m + (\mathbf{p}-q\mathbf{A})^2/(2m)$, giving $H \approx m + (\mathbf{p}-q\mathbf{A})^2/(2m) + q\phi$, the Newtonian Hamiltonian (plus rest energy $m$).

---

# Solution

The solution is a clean four-step Legendre transform. Step 1 computes and inverts the momentum. Step 2 forms the Hamiltonian and simplifies to $\sqrt{\mathbf{p}^2 + m^2}$. Step 3 checks Hamilton's equations and identifies $H$ as the energy. Step 4 adds potentials and takes the non-relativistic limit. The recurring algebraic tool is $\gamma^2\mathbf{v}^2 = \gamma^2 - 1$, which untangles the inversion.

**Step 1: The momentum and its inversion.**

> [!note]- Derivation
> Differentiate $L = -m\sqrt{1 - \mathbf{v}^2} = -m(1 - \mathbf{v}^2)^{1/2}$:
> $$\mathbf{p} = \frac{\partial L}{\partial\mathbf{v}} = -m\cdot\frac12(1 - \mathbf{v}^2)^{-1/2}\cdot(-2\mathbf{v}) = \frac{m\mathbf{v}}{\sqrt{1 - \mathbf{v}^2}} = m\gamma\mathbf{v}.$$
> To invert for $\mathbf{v}(\mathbf{p})$, square: $\mathbf{p}^2 = m^2\gamma^2\mathbf{v}^2$. Using the identity $\gamma^2\mathbf{v}^2 = \gamma^2(1 - 1/\gamma^2) = \gamma^2 - 1$ (since $1/\gamma^2 = 1 - \mathbf{v}^2$),
> $$\mathbf{p}^2 = m^2(\gamma^2 - 1) \quad\Longrightarrow\quad \gamma^2 = 1 + \frac{\mathbf{p}^2}{m^2} \quad\Longrightarrow\quad \gamma = \frac{\sqrt{\mathbf{p}^2 + m^2}}{m}.$$
> Then $\mathbf{v} = \mathbf{p}/(m\gamma) = \mathbf{p}/\sqrt{\mathbf{p}^2 + m^2}$, the inverted relation. (Note $|\mathbf{v}| < 1$ for all finite $\mathbf{p}$, and $|\mathbf{v}| \to 1$ as $|\mathbf{p}| \to \infty$ — the speed approaches $c$ but never reaches it.)

**Step 2: The Hamiltonian is $\sqrt{\mathbf{p}^2 + m^2}$.**

> [!note]- Derivation
> Form the Legendre transform $H = \mathbf{p}\cdot\mathbf{v} - L$:
> $$H = m\gamma\mathbf{v}\cdot\mathbf{v} - \big(-m\sqrt{1 - \mathbf{v}^2}\big) = m\gamma\mathbf{v}^2 + m\sqrt{1 - \mathbf{v}^2} = m\gamma\mathbf{v}^2 + \frac{m}{\gamma}.$$
> Use $\mathbf{v}^2 = 1 - 1/\gamma^2$:
> $$H = m\gamma\Big(1 - \frac{1}{\gamma^2}\Big) + \frac{m}{\gamma} = m\gamma - \frac{m}{\gamma} + \frac{m}{\gamma} = m\gamma.$$
> Substituting $\gamma = \sqrt{\mathbf{p}^2 + m^2}/m$ from Step 1,
> $$\boxed{H = m\gamma = \sqrt{\mathbf{p}^2 + m^2}}\qquad(\text{with } c:\ H = \sqrt{\mathbf{p}^2c^2 + m^2c^4}).$$
> This is the relativistic **energy-momentum relation**, now read as the Hamiltonian — the energy expressed as a function of the three-momentum. It satisfies the mass-shell constraint $H^2 - \mathbf{p}^2 = m^2$, the statement $E^2 = \mathbf{p}^2 + m^2$.

**Step 3: Hamilton's equations and $H = E$.**

> [!note]- Derivation
> Check the first canonical equation:
> $$\dot{\mathbf{x}} = \frac{\partial H}{\partial\mathbf{p}} = \frac{\mathbf{p}}{\sqrt{\mathbf{p}^2 + m^2}} = \frac{\mathbf{p}}{m\gamma} = \mathbf{v},$$
> which recovers $\mathbf{p} = m\gamma\mathbf{v}$ — consistent. For a free particle $H$ has no $\mathbf{x}$-dependence, so the second canonical equation gives
> $$\dot{\mathbf{p}} = -\frac{\partial H}{\partial\mathbf{x}} = 0,$$
> conservation of three-momentum, hence (since $H = \sqrt{\mathbf{p}^2 + m^2}$ depends only on the conserved $\mathbf{p}$) conservation of energy. Finally, $H = m\gamma$ is exactly the **energy** $E$ of the particle relative to the observer ([[Def - Four-Momentum and Rest Mass]]): the Hamiltonian *is* the energy, as it should be for a time-independent system. The four-momentum is $P = (E, \mathbf{p}) = (H, \mathbf{p})$, with $H$ the time component.

**Step 4: The charged-particle Hamiltonian and the non-relativistic limit.**

> [!note]- Derivation
> For a particle in a vector field, the canonical momentum is $\mathbf{p} = m\gamma\mathbf{v} + q\mathbf{A}$, so the *kinetic* momentum is $\mathbf{p} - q\mathbf{A} = m\gamma\mathbf{v}$, which satisfies $(\mathbf{p} - q\mathbf{A})^2 = m^2(\gamma^2 - 1)$. Repeating the Legendre transform (and adding the scalar potential energy $q\phi$, with $\phi = A_0$),
> $$\boxed{H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} + q\phi}.$$
> This is obtained from the free Hamiltonian by the **minimal substitution** $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$ plus the addition of $q\phi$. *Non-relativistic limit*, $|\mathbf{p} - q\mathbf{A}| \ll m$:
> $$\sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} = m\sqrt{1 + \frac{(\mathbf{p}-q\mathbf{A})^2}{m^2}} \approx m + \frac{(\mathbf{p} - q\mathbf{A})^2}{2m},$$
> so
> $$H \approx m + \frac{(\mathbf{p} - q\mathbf{A})^2}{2m} + q\phi.$$
> Dropping the rest-energy constant $m$, this is exactly the **Newtonian Hamiltonian** of a charged particle in an electromagnetic field. The relativistic Hamiltonian thus contains the Newtonian one as its low-momentum limit, with the rest energy $m$ as an additive constant and the relativistic corrections in the higher-order terms of the expansion.

> [!note]- Complete formal solution
> From $L = -m\sqrt{1 - \mathbf{v}^2}$, the momentum is $\mathbf{p} = \partial L/\partial\mathbf{v} = m\gamma\mathbf{v}$. Inverting via $\mathbf{p}^2 = m^2\gamma^2\mathbf{v}^2 = m^2(\gamma^2 - 1)$ gives $\gamma = \sqrt{\mathbf{p}^2 + m^2}/m$ and $\mathbf{v} = \mathbf{p}/\sqrt{\mathbf{p}^2 + m^2}$. The Legendre transform $H = \mathbf{p}\cdot\mathbf{v} - L = m\gamma\mathbf{v}^2 + m/\gamma = m\gamma = \sqrt{\mathbf{p}^2 + m^2}$. Hamilton's equations: $\dot{\mathbf{x}} = \partial H/\partial\mathbf{p} = \mathbf{p}/\sqrt{\mathbf{p}^2+m^2} = \mathbf{v}$ ✓, and $\dot{\mathbf{p}} = -\partial H/\partial\mathbf{x} = 0$ for a free particle, with $H = m\gamma = E$ the energy. Charged case: minimal substitution $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$ and add $q\phi$ gives $H = \sqrt{(\mathbf{p}-q\mathbf{A})^2 + m^2} + q\phi$, whose non-relativistic limit $m + (\mathbf{p}-q\mathbf{A})^2/(2m) + q\phi$ is the Newtonian Hamiltonian (plus rest energy). $\blacksquare$

---

# Key Takeaways

**The relativistic Hamiltonian is the energy-momentum relation, and the Legendre transform works only because the parametrisation is non-covariant.** The Hamiltonian $H = \sqrt{\mathbf{p}^2 + m^2}$ is nothing but the relativistic dispersion relation $E = \sqrt{\mathbf{p}^2c^2 + m^2c^4}$ read as a function on phase space — the energy expressed through the three-momentum. The reason this clean construction is available *here* but not for the manifestly covariant Lagrangian is that the inertial-observer Lagrangian $-m\sqrt{1 - \mathbf{v}^2}$ is *non-degenerate* in $\mathbf{v}$ (it is not homogeneous of degree one), so its Legendre transform is honest; the covariant $-m\sqrt{\eta\dot x\dot x}$ is degenerate and its naive Legendre transform vanishes. The reusable principle: to get the physical Hamiltonian $\sqrt{\mathbf{p}^2 + m^2}$, break Lorentz covariance by parametrising with an observer's time, which removes the reparametrisation degeneracy; to keep covariance, use the Dirac constraint Hamiltonian instead. The trade-off — covariance versus a non-degenerate Legendre transform — is the central choice in setting up the relativistic Hamiltonian.

**The identity $\gamma^2\mathbf{v}^2 = \gamma^2 - 1$ is the algebraic key to every relativistic momentum inversion.** Inverting $\mathbf{p} = m\gamma\mathbf{v}$ to get $\mathbf{v}(\mathbf{p})$ or $\gamma(\mathbf{p})$ looks circular — $\gamma$ depends on $\mathbf{v}$, which is what you are solving for — until you use $\gamma^2\mathbf{v}^2 = \gamma^2 - 1$, which expresses $\mathbf{p}^2 = m^2(\gamma^2 - 1)$ in terms of $\gamma$ alone, breaking the circularity. This identity, a direct consequence of $1/\gamma^2 = 1 - \mathbf{v}^2$, recurs throughout relativistic kinematics whenever one must trade velocity variables for momentum variables, and it is worth committing to memory. The same manoeuvre gives $E^2 = \mathbf{p}^2 + m^2$ from $E = m\gamma$, $\mathbf{p} = m\gamma\mathbf{v}$, and it is the reason the mass shell $E^2 - \mathbf{p}^2 = m^2$ is the natural constraint surface. Whenever a relativistic problem mixes $\gamma$, $\mathbf{v}$, and $\mathbf{p}$, reach for $\gamma^2\mathbf{v}^2 = \gamma^2 - 1$ to decouple them.

**Minimal substitution $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$ couples the Hamiltonian to electromagnetism, and contains the Newtonian limit.** The charged-particle Hamiltonian $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} + q\phi$ is obtained from the free one by the minimal substitution $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$ (replacing canonical by kinetic momentum) plus the scalar potential energy $q\phi$. This is the same gauge-covariant substitution that, promoted to operators, couples the Klein–Gordon and Dirac equations to electromagnetism, and its appearance here in the classical Hamiltonian is its origin. Expanding for small momenta recovers the Newtonian Hamiltonian $m + (\mathbf{p} - q\mathbf{A})^2/(2m) + q\phi$, confirming that the relativistic theory contains the non-relativistic one with the rest energy $m$ as an additive constant. The reusable insight is that the entire electromagnetic interaction of a charged particle — classical or quantum — is encoded in the single substitution $\mathbf{p} \to \mathbf{p} - q\mathbf{A}$, which replaces the canonical momentum by the gauge-invariant kinetic momentum. For the covariant Dirac Hamiltonian and the primary constraint that the energy Hamiltonian sidesteps, see [[Ex - The Dirac Hamiltonian and the primary constraint]].
