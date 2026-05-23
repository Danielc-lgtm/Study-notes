---
type: exercise
subject: geometric-mechanics
difficulty: "⭐⭐"
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - The Canonical Symplectic Form on a Cotangent Bundle"
  - "Def - Hamiltonian Vector Field"
  - "Def - Poisson Bracket"
tags: [physics, geometric-mechanics, symplectic-geometry]
---

# Problem Statement

A point particle of mass $m$ is constrained to move on the unit sphere $S^2 \subset \mathbb{R}^3$ under uniform gravity. The configuration space is $Q = S^2$, with spherical coordinates $(\theta, \phi)$ where $\theta \in [0, \pi]$ is the polar angle from the vertical and $\phi \in [0, 2\pi)$ is the azimuthal angle. The position is $\vec x = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$, the gravitational potential is $V = mg\cos\theta$ (with $g$ the gravitational acceleration, taking the upper pole as the gravity origin; the lower pole has $V = -mg$).

(a) Write the Lagrangian $L = T - V$ in spherical coordinates and derive the conjugate momenta $p_\theta, p_\phi$.

(b) Compute the Hamiltonian $H(\theta, \phi, p_\theta, p_\phi)$ on $T^*S^2$ via the Legendre transform.

(c) Identify the conserved quantity arising from rotational symmetry about the vertical axis, and verify $\{p_\phi, H\} = 0$ from the canonical Poisson bracket.

(d) Reduce the dynamics to an effective one-dimensional problem in $\theta$ using conservation of $p_\phi$ and energy.

**Recall:**

![[Def - Hamiltonian Function#The Definition]]

The canonical Poisson bracket in coordinates $(q^i, p_i)$ is $\{f, g\} = \sum_i (\partial_{q^i}f \partial_{p_i}g - \partial_{p_i}f \partial_{q^i}g)$. A function $f$ is conserved along the flow of $H$ iff $\{f, H\} = 0$.

For motion on $S^2$, the kinetic energy is $T = \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2)$ (using the standard round metric on the unit sphere).

---

# Convergent Strategy

**Problem class:** This is a **constrained Hamiltonian system** with **continuous symmetry**, two recurring features of physical systems. The configuration space $S^2$ has nontrivial topology (not a single chart covers it), so the calculation requires choosing a chart carefully. The symmetry is rotational about the vertical axis (the gravitational direction), leading to conservation of angular momentum about that axis.

**Assumption pattern:** The given data are: (1) configuration space $Q = S^2$ with the round Riemannian metric; (2) gravitational potential $V = mg\cos\theta$. From these the Lagrangian $L = T - V$ follows, the Hamiltonian via Legendre transform, and the conservation law via the rotational symmetry. The crucial assumption is the **rotational invariance of $V$ about the vertical axis** — this is what makes $p_\phi$ conserved.

**Theorem routing:** Apply [[Def - The Legendre Transform|Legendre transform]] to get $H$ from $L$. Identify $p_\phi$ as a conserved quantity from rotational symmetry; verify $\{p_\phi, H\} = 0$ using the [[Def - Poisson Bracket|Poisson bracket formula]]. Use the two conservation laws — energy $E = H$ and angular momentum $p_\phi$ — to eliminate $\dot\phi$ via $p_\phi = m\sin^2\theta\,\dot\phi$ and reduce the dynamics to a single ODE in $\theta(t)$.

**Key decision point:** The non-obvious step is the **reduction**: once $p_\phi$ is known to be conserved, treat it as a constant in the energy expression and solve for $\dot\theta$ as a function of $\theta$ and $E$. The reduced problem is a one-dimensional motion in an effective potential $V_{\rm eff}(\theta) = mg\cos\theta + p_\phi^2/(2m\sin^2\theta)$ — the gravitational term plus a centrifugal-style term from the conserved angular momentum. This is the **symplectic-reduction picture** applied concretely: the rotational symmetry $S^1 = U(1)$ acting on $S^2$ reduces the 4-dimensional $T^*S^2$ to a 2-dimensional reduced phase space (parametrized by $(\theta, p_\theta)$ with $p_\phi$ a parameter).

---

# Legal Operations Used

1. **Operation 6 from the topic page (Legendre transform).** Applied to convert $L(\theta, \phi, \dot\theta, \dot\phi)$ to $H(\theta, \phi, p_\theta, p_\phi)$ via $p_\theta = \partial L/\partial\dot\theta$, $p_\phi = \partial L/\partial\dot\phi$.

2. **Operation 3 from the topic page (check $\{f, H\} = 0$).** Applied to verify $\{p_\phi, H\} = 0$, confirming $p_\phi$ is conserved by the Hamiltonian flow.

3. **Operation 9 from the topic page (symmetry reduction).** Applied to reduce the 4-dimensional phase space $T^*S^2$ to a 2-dimensional reduced phase space using the conserved $p_\phi$, exploiting the rotational symmetry.

---

# Hints

> [!note]- Hint 1
> Compute $T = \tfrac{1}{2}m|\dot{\vec x}|^2$ in spherical coordinates, using $\vec x(\theta, \phi)$ and the chain rule. The result is $T = \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2)$ — the standard round-metric kinetic energy on $S^2$.

> [!note]- Hint 2
> Conjugate momenta: $p_\theta = \partial L/\partial\dot\theta = m\dot\theta$; $p_\phi = \partial L/\partial\dot\phi = m\sin^2\theta\,\dot\phi$. Note that $p_\phi$ depends on $\theta$ through the $\sin^2\theta$ factor — this is a feature of the curved configuration space.

> [!note]- Hint 3
> The Hamiltonian comes out to $H = \tfrac{1}{2m}\big(p_\theta^2 + p_\phi^2/\sin^2\theta\big) + mg\cos\theta$. Since $H$ does not depend on $\phi$, the partial derivative $\partial H/\partial\phi = 0$, and by Hamilton's equations $\dot p_\phi = -\partial H/\partial\phi = 0$ — $p_\phi$ is conserved.

> [!note]- Hint 4
> Use the two conservation laws to reduce: from $H = E$ and $p_\phi = $ constant, solve $\dot\theta = \pm\sqrt{\tfrac{2}{m}(E - V_{\rm eff}(\theta))}$ where $V_{\rm eff}(\theta) = mg\cos\theta + p_\phi^2/(2m\sin^2\theta)$. This is now a one-dimensional problem.

---

# Solution

The proof breaks into four steps. Step 1 sets up the Lagrangian. Step 2 derives the Hamiltonian. Step 3 identifies the conserved $p_\phi$ from rotational symmetry. Step 4 reduces to a 1D problem.

**Step 1: Lagrangian and conjugate momenta.**

$L = \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2) - mg\cos\theta$. Conjugate momenta: $p_\theta = m\dot\theta$, $p_\phi = m\sin^2\theta\,\dot\phi$.

> [!note]- Derivation
> Position vector in spherical coordinates: $\vec x = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$. Velocity:
> $$\dot{\vec x} = \dot\theta(\cos\theta\cos\phi, \cos\theta\sin\phi, -\sin\theta) + \dot\phi(-\sin\theta\sin\phi, \sin\theta\cos\phi, 0).$$
> Squared speed:
> $$|\dot{\vec x}|^2 = \dot\theta^2 + \sin^2\theta\,\dot\phi^2,$$
> since the two basis vectors $\partial\vec x/\partial\theta$ and $\partial\vec x/\partial\phi$ are orthogonal in $\mathbb{R}^3$, with squared norms $1$ and $\sin^2\theta$ respectively.
>
> Kinetic energy: $T = \tfrac{1}{2}m|\dot{\vec x}|^2 = \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2)$.
>
> Potential: $V = mg(\vec x \cdot \hat z) = mg\cos\theta$ where $\hat z$ is the vertical unit vector.
>
> Lagrangian: $L = T - V = \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2) - mg\cos\theta$.
>
> Conjugate momenta:
> $$p_\theta = \frac{\partial L}{\partial \dot\theta} = m\dot\theta, \qquad p_\phi = \frac{\partial L}{\partial \dot\phi} = m\sin^2\theta\,\dot\phi.$$
>
> Note: $p_\phi$ has dimensions of angular momentum and represents the **angular momentum about the vertical ($z$) axis**, $L_z = m(\vec x \times \dot{\vec x})\cdot\hat z = m\sin^2\theta\,\dot\phi$.

**Step 2: Hamiltonian via Legendre transform.**

$H = \tfrac{1}{2m}\big(p_\theta^2 + p_\phi^2/\sin^2\theta\big) + mg\cos\theta$.

> [!note]- Derivation
> By the Legendre transform $H = p_\theta\dot\theta + p_\phi\dot\phi - L$, with $\dot\theta = p_\theta/m$ and $\dot\phi = p_\phi/(m\sin^2\theta)$ from inverting the conjugate-momentum relations. Substitute:
> $$H = p_\theta(p_\theta/m) + p_\phi(p_\phi/(m\sin^2\theta)) - \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2) + mg\cos\theta.$$
> $$= \frac{p_\theta^2}{m} + \frac{p_\phi^2}{m\sin^2\theta} - \tfrac{1}{2}m\left(\frac{p_\theta^2}{m^2} + \sin^2\theta \cdot \frac{p_\phi^2}{m^2\sin^4\theta}\right) + mg\cos\theta$$
> $$= \frac{p_\theta^2}{m} + \frac{p_\phi^2}{m\sin^2\theta} - \frac{p_\theta^2}{2m} - \frac{p_\phi^2}{2m\sin^2\theta} + mg\cos\theta$$
> $$= \frac{p_\theta^2}{2m} + \frac{p_\phi^2}{2m\sin^2\theta} + mg\cos\theta.$$
>
> This is the total energy $E = T + V$, as expected (kinetic $= p_\theta^2/(2m) + p_\phi^2/(2m\sin^2\theta)$, potential $= mg\cos\theta$).

**Step 3: $p_\phi$ is conserved (rotational symmetry).**

$\{p_\phi, H\} = -\partial H/\partial\phi = 0$, so $p_\phi$ is conserved.

> [!note]- Derivation
> The Poisson bracket in canonical coordinates $(\theta, \phi, p_\theta, p_\phi)$:
> $$\{p_\phi, H\} = \sum_i\left(\frac{\partial p_\phi}{\partial q^i}\frac{\partial H}{\partial p_i} - \frac{\partial p_\phi}{\partial p_i}\frac{\partial H}{\partial q^i}\right).$$
> Since $p_\phi$ is a coordinate, $\partial p_\phi/\partial q^i = 0$ for all $i$ (it doesn't depend on positions) and $\partial p_\phi/\partial p_i = \delta^{\phi}_i$ — only the $p_\phi$ derivative is nonzero, equal to $1$. So:
> $$\{p_\phi, H\} = -\frac{\partial H}{\partial \phi}.$$
> Compute $\partial H/\partial\phi$: $H = \tfrac{1}{2m}(p_\theta^2 + p_\phi^2/\sin^2\theta) + mg\cos\theta$ does not depend on $\phi$ at all (only on $\theta$ and the momenta). So $\partial H/\partial\phi = 0$, hence $\{p_\phi, H\} = 0$.
>
> Therefore **$p_\phi$ is conserved along the Hamiltonian flow**: $dp_\phi/dt = \{p_\phi, H\} = 0$. Physically, $p_\phi$ is the angular momentum about the vertical axis, conserved because the system is symmetric under rotations about the vertical (the potential $V = mg\cos\theta$ depends on $\theta$ but not $\phi$).
>
> **Noether's theorem connection:** the rotational symmetry $\phi \mapsto \phi + \alpha$ is a $1$-parameter group acting on $S^2$, lifting to a symplectomorphism of $T^*S^2$. By Noether's theorem (symplectic form), the moment map of this $S^1$-action is $p_\phi$, which is conserved by any $S^1$-invariant Hamiltonian. The conservation of $p_\phi$ here is the direct application.

**Step 4: Reduction to one-dimensional problem.**

Use $p_\phi = \ell$ (constant) and $H = E$ (constant) to get $\dot\theta = \pm\sqrt{2(E - V_{\rm eff}(\theta))/m}$ with $V_{\rm eff}(\theta) = mg\cos\theta + \ell^2/(2m\sin^2\theta)$.

> [!note]- Derivation
> With $p_\phi = \ell$ constant, the Hamiltonian becomes
> $$E = H = \frac{p_\theta^2}{2m} + \frac{\ell^2}{2m\sin^2\theta} + mg\cos\theta.$$
> Define the **effective potential**:
> $$V_{\rm eff}(\theta) := mg\cos\theta + \frac{\ell^2}{2m\sin^2\theta}.$$
> Then $E = p_\theta^2/(2m) + V_{\rm eff}(\theta)$ — a one-dimensional system with kinetic energy $p_\theta^2/(2m)$ and potential $V_{\rm eff}$. Solve for $p_\theta$:
> $$p_\theta = \pm\sqrt{2m(E - V_{\rm eff}(\theta))}.$$
> Using $\dot\theta = p_\theta/m$:
> $$\dot\theta = \pm\sqrt{\frac{2}{m}\big(E - V_{\rm eff}(\theta)\big)}.$$
>
> This separates: $dt = d\theta/\sqrt{(2/m)(E - V_{\rm eff}(\theta))}$, integrable by quadrature (an elliptic integral in general).
>
> **Geometric interpretation:** the effective potential $V_{\rm eff}$ has two terms:
> - **Gravitational** $mg\cos\theta$: decreases as $\theta$ increases (gravity pulls down to $\theta = \pi$).
> - **Centrifugal** $\ell^2/(2m\sin^2\theta)$: divergent at $\theta = 0, \pi$ (the poles), forcing the particle to avoid the poles if $\ell \neq 0$.
>
> The dynamics is **oscillation in $\theta$** between turning points where $E = V_{\rm eff}(\theta)$, while $\phi$ evolves according to $\dot\phi = p_\phi/(m\sin^2\theta) = \ell/(m\sin^2\theta)$ — a positive rotation (if $\ell > 0$) whose rate depends on $\theta$. The combined motion is a **precessing oscillation** about the vertical axis, like a spinning top.

> [!note]- Complete formal solution
> **Setup:** $Q = S^2$ with spherical coordinates $(\theta, \phi)$, round metric $g = d\theta^2 + \sin^2\theta\,d\phi^2$.
>
> **Lagrangian:** $L = \tfrac{1}{2}m(\dot\theta^2 + \sin^2\theta\,\dot\phi^2) - mg\cos\theta$.
>
> **Conjugate momenta:** $p_\theta = m\dot\theta$, $p_\phi = m\sin^2\theta\,\dot\phi$.
>
> **Hamiltonian (Legendre transform):** $H(\theta, \phi, p_\theta, p_\phi) = \frac{p_\theta^2}{2m} + \frac{p_\phi^2}{2m\sin^2\theta} + mg\cos\theta$.
>
> **Hamilton's equations:**
> $$\dot\theta = \partial_p H = p_\theta/m, \qquad \dot\phi = \partial_p H = p_\phi/(m\sin^2\theta),$$
> $$\dot p_\theta = -\partial_\theta H = \frac{p_\phi^2 \cos\theta}{m\sin^3\theta} + mg\sin\theta, \qquad \dot p_\phi = -\partial_\phi H = 0.$$
>
> **Conservation laws:**
> - Energy $E = H$ (autonomous Hamiltonian).
> - Angular momentum $\ell = p_\phi$ (rotational symmetry); verified by $\{p_\phi, H\} = -\partial H/\partial\phi = 0$.
>
> **Reduced 1D problem:** with $p_\phi = \ell$ fixed,
> $$E = \frac{p_\theta^2}{2m} + V_{\rm eff}(\theta), \qquad V_{\rm eff}(\theta) = mg\cos\theta + \frac{\ell^2}{2m\sin^2\theta}.$$
> Solve for $\dot\theta = \pm\sqrt{(2/m)(E - V_{\rm eff}(\theta))}$, separable.
>
> **Qualitative behavior:** for $\ell \neq 0$, the centrifugal barrier prevents the particle from reaching the poles; the dynamics is bounded oscillation in $\theta$ between turning points where $E = V_{\rm eff}(\theta)$. The azimuthal angle $\phi$ precesses with $\dot\phi = \ell/(m\sin^2\theta)$, fastest at small $\theta$ and slowest at large $\theta$.

---

# Key Takeaways

**The symplectic reduction picture in action: continuous symmetry reduces dimension by 2.** When a Hamiltonian system has a continuous $G$-symmetry preserving $H$ and $\omega$, the **Marsden–Weinstein quotient** reduces the dimension of phase space by $2\dim G$. Here $G = S^1$ (rotations about the vertical), so $T^*S^2$ (4-dimensional) reduces to a 2-dimensional reduced phase space — exactly the $(\theta, p_\theta)$ plane after fixing $p_\phi = \ell$. The reduced phase space carries its own symplectic structure $d\theta \wedge dp_\theta$ (inherited from $T^*S^2$) and its own Hamiltonian $E_{\rm red}(\theta, p_\theta) = p_\theta^2/(2m) + V_{\rm eff}(\theta)$. **This pattern recurs throughout mechanics:** any continuous symmetry produces a conserved quantity (Noether/moment map) and lets you reduce the dimension of the problem by 2. For the Kepler problem, the symmetry is $SO(3)$ (3-dimensional), reducing $T^*\mathbb{R}^3$ (6-dimensional) by 6 to a $\{0\}$-dimensional space — but only after using the energy and angular momentum (4 conservation laws), with the remaining 2 dimensions parametrizing the orbital plane. Symplectic reduction is **the universal mechanism for exploiting symmetry in classical mechanics**.

**Effective potentials and the centrifugal barrier.** When you eliminate a coordinate using a conserved momentum, the kinetic energy of that coordinate becomes an **effective potential energy** in the reduced problem. For the pendulum on a sphere, eliminating $\phi$ using $p_\phi = \ell$ produces the term $\ell^2/(2m\sin^2\theta)$ in $V_{\rm eff}$ — a **centrifugal barrier** at the poles. The general principle: **conserved-momentum elimination is energy-preserving but transfers "rotational" kinetic energy to "potential" form in the reduced description**. This is universal: for the Kepler problem, eliminating the angular momentum produces $\ell^2/(2mr^2)$ in the radial effective potential — the centrifugal barrier at $r = 0$. Identifying these effective potentials is the standard route to qualitative analysis of constrained-symmetric mechanical systems.

**Coordinate singularities at the poles.** The spherical coordinates $(\theta, \phi)$ are singular at the poles $\theta = 0, \pi$: $\phi$ becomes ill-defined, and the kinetic-energy metric coefficient $\sin^2\theta$ vanishes. This is a **coordinate artifact**, not a physical singularity — the geometry of $S^2$ is smooth at the poles, and the dynamics there is perfectly well-defined. However, the **Hamiltonian formulation with $p_\phi$ as a coordinate** has a genuine issue: the term $p_\phi^2/(2m\sin^2\theta)$ blows up as $\theta \to 0, \pi$ unless $p_\phi = 0$ at those points. This forces orbits with $\ell \neq 0$ to avoid the poles, and the dynamics in the reduced 1D picture exhibits a **centrifugal barrier**. The lesson: coordinate choices matter, and singularities of the coordinate system can disguise themselves as features of the dynamics. For numerical or qualitative work, switch to coordinates regular at the poles (Cartesian, or rotated spherical) when the dynamics approaches the singular region.
