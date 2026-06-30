---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
  - "Def - Lagrangian for a Particle in a Vector Field"
  - "Thm - Hamiltonian Formulation (Relativistic Particle)"
tags: [physics, special-relativity]
---

# Problem Statement

A particle of mass $m$ and charge $q$ moves in a uniform magnetic field $\mathbf{B} = B\hat{\mathbf{z}}$, described by the vector potential $\mathbf{A} = \tfrac12\mathbf{B}\times\mathbf{x} = \tfrac{B}{2}(-y, x, 0)$ and zero scalar potential. Use the relativistic Hamiltonian and Poisson brackets (with $c = 1$).

1. Write the Hamiltonian $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2}$ and Hamilton's equations.
2. Show that the energy $H$ and the kinetic energy $m\gamma$ are conserved (so $\gamma$, and hence the speed, is constant — the magnetic field does no work).
3. Using the conserved $\gamma$, show the motion is helical: circular in the $xy$-plane at the **relativistic cyclotron frequency** $\omega = qB/(m\gamma)$, with uniform drift along $z$.
4. Compute the Poisson bracket $\{H, p_z\}$ and confirm $p_z$ is conserved; compute $\{\Pi_x, \Pi_y\}$ for the kinetic momentum components $\boldsymbol{\Pi} = \mathbf{p} - q\mathbf{A}$ and interpret.

**Recall:**

![[Def - Generalized Four-Momentum and the Relativistic Hamiltonian#The Definition]]

The relativistic Hamiltonian for a charged particle is $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} + q\phi$ (here $\phi = 0$). The **kinetic momentum** is $\boldsymbol{\Pi} = \mathbf{p} - q\mathbf{A} = m\gamma\mathbf{v}$ ([[Def - Lagrangian for a Particle in a Vector Field]]). The [[Def - Poisson Bracket|Poisson bracket]] is $\{f, g\} = \sum_i(\partial_{x^i}f\,\partial_{p_i}g - \partial_{p_i}f\,\partial_{x^i}g)$, and $df/dt = \{f, H\}$; a quantity is conserved if and only if its Poisson bracket with $H$ vanishes.

---

# Convergent Strategy

**Problem class.** A *solve-the-motion-via-the-Hamiltonian* problem combined with a *conservation-via-Poisson-bracket* check — applying the relativistic energy Hamiltonian to a concrete field and exploiting conserved quantities, in the manner of [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|Hamiltonian mechanics]].

**Assumption pattern.** The field is a uniform magnetic field, encoded in the symmetric-gauge vector potential $\mathbf{A} = \tfrac12\mathbf{B}\times\mathbf{x}$, with no scalar potential. Two symmetries are present: the Hamiltonian has no explicit time dependence (energy conserved) and no explicit $z$-dependence (the canonical $p_z$ conserved). The magnetic field's velocity-perpendicular force does no work, so the speed — and hence $\gamma$ — is constant.

**Theorem routing.** The [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian|relativistic Hamiltonian]] gives Hamilton's equations; the conservation of $\gamma$ (because $\mathbf{B}$ does no work) lets the [[Thm - Hamiltonian Formulation (Relativistic Particle)|relativistic equation of motion]] be linearised into circular motion at $\omega = qB/(m\gamma)$; and the [[Def - Poisson Bracket|Poisson brackets]] confirm the conservation laws and reveal the kinetic-momentum algebra.

**Key decision point.** The crucial realisation is that, because the speed and hence $\gamma$ are constant, the relativistic equation $d(m\gamma\mathbf{v})/dt = q\mathbf{v}\times\mathbf{B}$ becomes $m\gamma\,d\mathbf{v}/dt = q\mathbf{v}\times\mathbf{B}$ — *linear* in $\mathbf{v}$ with the *constant* coefficient $m\gamma$, identical in form to the non-relativistic equation but with $m \to m\gamma$. This is why the relativistic cyclotron frequency is the non-relativistic one with $m$ replaced by $m\gamma$: the constancy of $\gamma$ is what allows the relativistic problem to be solved as easily as the Newtonian one.

---

# Legal Operations Used

1. **Perform the Legendre transform / use the energy Hamiltonian** (operation 6 from the topic page). The Hamiltonian $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2}$ governs the motion.

2. **Couple to a field by minimal coupling** (operation 4). The magnetic field enters via the canonical momentum $\mathbf{p} = \boldsymbol{\Pi} + q\mathbf{A}$.

3. **Apply Noether / cyclic-coordinate conservation** (operation 3). Time-independence conserves $H$; $z$-independence conserves $p_z$, verified by Poisson brackets.

---

# Hints

> [!note]- Hint 1
> $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2}$. Hamilton's equations: $\dot{x}^i = \partial H/\partial p_i = \Pi_i/H$ (where $\boldsymbol{\Pi} = \mathbf{p} - q\mathbf{A}$ and $H = \sqrt{\Pi^2 + m^2} = m\gamma$), and $\dot p_i = -\partial H/\partial x^i = (q/H)\Pi_j\partial_{x^i}A_j$.

> [!note]- Hint 2
> $H$ has no explicit time dependence, so $dH/dt = \{H, H\} = 0$: energy conserved. Since $H = m\gamma$, $\gamma$ is constant, so $|\mathbf{v}|$ is constant. The magnetic force $q\mathbf{v}\times\mathbf{B}$ is perpendicular to $\mathbf{v}$, so it does no work — consistent.

> [!note]- Hint 3
> With $\gamma$ constant, $d(m\gamma\mathbf{v})/dt = q\mathbf{v}\times\mathbf{B}$ becomes $m\gamma\,\dot{\mathbf{v}} = q\mathbf{v}\times\mathbf{B}$. In components: $\dot v_x = -\omega v_y$, $\dot v_y = \omega v_x$, $\dot v_z = 0$, with $\omega = qB/(m\gamma)$. This is circular motion at frequency $\omega$ in the $xy$-plane plus uniform $z$-drift — a helix.

> [!note]- Hint 4
> $\{H, p_z\} = \partial_{x^j}H\,\partial_{p_j}p_z - \dots$; since $A$ has no $z$-component and $H$ has no explicit $z$, this is $-\partial_z H = 0$. For $\{\Pi_x, \Pi_y\}$ with $\Pi_i = p_i - qA_i$ and $\mathbf{A} = \tfrac{B}{2}(-y, x, 0)$: compute directly, getting $\{\Pi_x, \Pi_y\} = qB = q B_z$, the magnetic field — the kinetic momenta do *not* Poisson-commute.

---

# Solution

The solution solves the helical motion and verifies the conservation laws via Poisson brackets. Step 1 sets up the Hamiltonian and Hamilton's equations. Step 2 establishes that $\gamma$ is constant. Step 3 uses this to linearise the equation of motion into circular motion at the relativistic cyclotron frequency. Step 4 computes the relevant Poisson brackets. The key simplification is that the constancy of $\gamma$ turns the relativistic problem into a Newtonian-looking one with $m \to m\gamma$.

**Step 1: The Hamiltonian and Hamilton's equations.**

> [!note]- Derivation
> With $\phi = 0$ and $\mathbf{A} = \tfrac{B}{2}(-y, x, 0)$, the Hamiltonian is
> $$H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2} = \sqrt{\boldsymbol{\Pi}^2 + m^2}, \qquad \boldsymbol{\Pi} := \mathbf{p} - q\mathbf{A}.$$
> Note $H = \sqrt{\boldsymbol{\Pi}^2 + m^2} = m\gamma$ (the energy), since $\boldsymbol{\Pi} = m\gamma\mathbf{v}$ is the kinetic momentum. Hamilton's equations:
> $$\dot{x}^i = \frac{\partial H}{\partial p_i} = \frac{\Pi_i}{\sqrt{\boldsymbol{\Pi}^2 + m^2}} = \frac{\Pi_i}{m\gamma} = v_i,$$
> consistent with $\boldsymbol{\Pi} = m\gamma\mathbf{v}$, and
> $$\dot p_i = -\frac{\partial H}{\partial x^i} = -\frac{1}{m\gamma}\Pi_j\frac{\partial(-qA_j)}{\partial x^i} = \frac{q}{m\gamma}\Pi_j\,\partial_{x^i}A_j.$$

**Step 2: $\gamma$ is constant — the magnetic field does no work.**

> [!note]- Derivation
> The Hamiltonian $H = \sqrt{\boldsymbol{\Pi}^2 + m^2}$ has no explicit time dependence (neither $\mathbf{A}$ nor $\phi$ depends on $t$), so it is conserved:
> $$\frac{dH}{dt} = \frac{\partial H}{\partial t} + \{H, H\} = 0.$$
> Since $H = m\gamma$, the Lorentz factor $\gamma$ is constant, and therefore the speed $|\mathbf{v}| = \sqrt{1 - 1/\gamma^2}$ is constant. This is the statement that the magnetic field does no work: the magnetic force $q\mathbf{v}\times\mathbf{B}$ is always perpendicular to the velocity $\mathbf{v}$, so $\mathbf{F}\cdot\mathbf{v} = q(\mathbf{v}\times\mathbf{B})\cdot\mathbf{v} = 0$, and the kinetic energy $m\gamma$ cannot change. Only the *direction* of $\mathbf{v}$ changes, not its magnitude.

**Step 3: Helical motion at the relativistic cyclotron frequency.**

> [!note]- Derivation
> The relativistic equation of motion is $\tfrac{d\boldsymbol{\Pi}}{dt} = \tfrac{d}{dt}(m\gamma\mathbf{v}) = q\mathbf{v}\times\mathbf{B}$ (the Lorentz force, [[Ex - The Lorentz force from minimal coupling]]). Because $\gamma$ is *constant* (Step 2), it pulls out of the derivative:
> $$m\gamma\frac{d\mathbf{v}}{dt} = q\mathbf{v}\times\mathbf{B}.$$
> This is *linear* in $\mathbf{v}$ with the constant coefficient $m\gamma$ — formally identical to the non-relativistic cyclotron equation, but with $m$ replaced by $m\gamma$. With $\mathbf{B} = B\hat{\mathbf{z}}$, the components are
> $$\dot v_x = -\omega\,v_y, \qquad \dot v_y = +\omega\,v_x, \qquad \dot v_z = 0, \qquad \omega := \frac{qB}{m\gamma}.$$
> The $z$-equation gives uniform drift $v_z = \text{const}$. The $x,y$-equations are the harmonic oscillator $\ddot v_x = -\omega^2 v_x$, solved by $v_x = v_\perp\cos(\omega t + \varphi_0)$, $v_y = v_\perp\sin(\omega t + \varphi_0)$ — circular motion in the $xy$-plane at the **relativistic cyclotron frequency**
> $$\boxed{\omega = \frac{qB}{m\gamma}}\qquad(\text{with } c:\ \omega = \frac{qB}{m\gamma}).$$
> The full trajectory is a **helix**: a circle of radius $r = v_\perp/\omega = m\gamma v_\perp/(qB)$ in the $xy$-plane, drifting uniformly along $z$. The relativistic correction to the Newtonian cyclotron frequency $\omega_0 = qB/m$ is the factor $1/\gamma$: faster particles circulate more slowly (their effective inertia $m\gamma$ is larger), which is why cyclotrons lose synchronisation at relativistic energies and synchrotrons must ramp the field or frequency.

**Step 4: Poisson brackets.**

> [!note]- Derivation
> *Conservation of $p_z$.* The canonical momentum $p_z$ has Poisson bracket with $H$:
> $$\{p_z, H\} = \sum_i\Big(\frac{\partial p_z}{\partial x^i}\frac{\partial H}{\partial p_i} - \frac{\partial p_z}{\partial p_i}\frac{\partial H}{\partial x^i}\Big) = -\frac{\partial H}{\partial z},$$
> since $\partial p_z/\partial x^i = 0$ and $\partial p_z/\partial p_i = \delta_{iz}$. Now $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2}$ with $\mathbf{A} = \tfrac{B}{2}(-y, x, 0)$ has no explicit $z$-dependence, so $\partial H/\partial z = 0$, giving $\{p_z, H\} = 0$: the canonical $p_z$ is conserved (the $z$-translation symmetry). Note $\Pi_z = p_z - qA_z = p_z$ here (since $A_z = 0$), so the *kinetic* $z$-momentum is also conserved — consistent with the uniform $z$-drift.
> *The kinetic-momentum algebra.* Compute $\{\Pi_x, \Pi_y\}$ with $\Pi_i = p_i - qA_i$, $A_x = -\tfrac{B}{2}y$, $A_y = +\tfrac{B}{2}x$:
> $$\{\Pi_x, \Pi_y\} = \{p_x - qA_x,\ p_y - qA_y\} = -q\{p_x, A_y\} - q\{A_x, p_y\} + q^2\{A_x, A_y\}.$$
> Now $\{p_x, A_y\} = -\partial_x A_y = -\tfrac{B}{2}$ (using $\{p_i, f\} = -\partial_{x^i}f$), $\{A_x, p_y\} = \partial_y A_x = -\tfrac{B}{2}$, and $\{A_x, A_y\} = 0$ (both depend only on positions). So
> $$\{\Pi_x, \Pi_y\} = -q\big(-\tfrac{B}{2}\big) - q\big(-\tfrac{B}{2}\big) = qB = qB_z.$$
> The kinetic momenta $\Pi_x, \Pi_y$ do **not** Poisson-commute: $\{\Pi_x, \Pi_y\} = qB_z$, the magnetic field. This non-commutativity is the classical origin of the **Landau-level** structure in the quantum problem — the quantised kinetic momenta behave like position and momentum of a harmonic oscillator, with $qB$ playing the role of $\hbar$, giving the discrete cyclotron energy levels. The Poisson bracket $\{\Pi_x, \Pi_y\} = qB$ is the seed of $[\hat\Pi_x, \hat\Pi_y] = i\hbar qB$.

> [!note]- Complete formal solution
> With $\mathbf{A} = \tfrac{B}{2}(-y, x, 0)$, $\phi = 0$, the Hamiltonian is $H = \sqrt{\boldsymbol{\Pi}^2 + m^2} = m\gamma$, $\boldsymbol{\Pi} = \mathbf{p} - q\mathbf{A} = m\gamma\mathbf{v}$. Since $H$ is time-independent, $\gamma = H/m$ is conserved, so $|\mathbf{v}|$ is constant (the magnetic force does no work). Then $d(m\gamma\mathbf{v})/dt = q\mathbf{v}\times\mathbf{B}$ becomes $m\gamma\,\dot{\mathbf{v}} = q\mathbf{v}\times\mathbf{B}$, i.e. $\dot v_x = -\omega v_y$, $\dot v_y = \omega v_x$, $\dot v_z = 0$ with $\omega = qB/(m\gamma)$ — helical motion: a circle of radius $r = m\gamma v_\perp/(qB)$ at frequency $\omega$, drifting along $z$. Poisson brackets: $\{p_z, H\} = -\partial_z H = 0$ (conserved $p_z$); $\{\Pi_x, \Pi_y\} = qB_z$ (kinetic momenta do not commute, the seed of Landau levels). $\blacksquare$

---

# Key Takeaways

**Constant $\gamma$ turns the relativistic cyclotron problem into the Newtonian one with $m \to m\gamma$.** The single observation that the magnetic field does no work — so $\gamma$ is constant — is what makes this problem tractable. With $\gamma$ constant, the relativistic equation $d(m\gamma\mathbf{v})/dt = q\mathbf{v}\times\mathbf{B}$ collapses to $m\gamma\,d\mathbf{v}/dt = q\mathbf{v}\times\mathbf{B}$, formally identical to the non-relativistic cyclotron equation but with the inertia $m$ replaced by the relativistic inertia $m\gamma$. The cyclotron frequency is thus the Newtonian $qB/m$ scaled by $1/\gamma$: faster particles circulate more slowly because their effective mass is larger. The reusable principle is that whenever a force does no work (is perpendicular to the velocity), the speed and hence $\gamma$ are constant, and the relativistic dynamics reduces to a velocity-direction problem with constant-magnitude velocity — often solvable by the same methods as the non-relativistic case with $m \to m\gamma$. This is exactly why the magnetic deflection of relativistic particles in accelerators and detectors is computed with $m\gamma$ in place of $m$, and why cyclotrons (fixed frequency) fail at relativistic energies while synchrotrons (ramped frequency or field) succeed.

**The relativistic Hamiltonian makes conservation laws Poisson-bracket computations.** Once the energy Hamiltonian $H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 + m^2}$ is in hand, the question "what is conserved?" becomes the mechanical computation "which phase-space functions have vanishing Poisson bracket with $H$?". Time-independence of $H$ gives $\{H, H\} = 0$ (energy conserved); $z$-independence gives $\{p_z, H\} = -\partial_z H = 0$ (canonical $p_z$ conserved). This is the [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|symplectic]] face of Noether's theorem: a symmetry of $H$ is a function that Poisson-commutes with it, and the function *is* the conserved charge and *generates* the symmetry. The reusable diagnostic is that $df/dt = \{f, H\}$, so conservation is equivalent to Poisson-commuting with the Hamiltonian, and one finds conserved quantities by inspecting which coordinates are absent from $H$. This bracket-based bookkeeping is the bridge from the classical relativistic particle to its quantum version, where Poisson brackets become commutators and conserved quantities become symmetry operators.

**Kinetic momenta do not commute in a magnetic field, and this is the classical seed of Landau levels.** The Poisson bracket $\{\Pi_x, \Pi_y\} = qB_z$ shows that the kinetic momentum components — the gauge-invariant, physical momenta $m\gamma\mathbf{v}$ — fail to Poisson-commute when a magnetic field is present, with the bracket equal to the field strength. (The *canonical* momenta $p_i$ do commute, $\{p_i, p_j\} = 0$; it is the gauge-invariant kinetic combination that does not.) This non-commutativity is the classical shadow of the quantum fact that $[\hat\Pi_x, \hat\Pi_y] = i\hbar qB$, which makes $\hat\Pi_x$ and $\hat\Pi_y$ behave like conjugate position and momentum of a harmonic oscillator — producing the quantised **Landau levels** with energy spacing $\hbar\omega = \hbar qB/(m\gamma)$. The reusable insight is that the algebra of the kinetic momenta encodes the field: $\{\Pi_i, \Pi_j\} = qF_{ij}$ (in general, the field-strength tensor), so the non-commutativity of physical momenta is a direct measure of the field, and it is the structure that quantises into the magnetic energy levels. For the variational derivation of the Lorentz force that this Hamiltonian motion realises, see [[Ex - The Lorentz force from minimal coupling]]; for the Legendre transform producing the Hamiltonian, see [[Ex - Legendre transform to the relativistic Hamiltonian]].
