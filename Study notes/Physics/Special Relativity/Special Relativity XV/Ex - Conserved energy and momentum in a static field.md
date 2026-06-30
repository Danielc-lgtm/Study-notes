---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Thm - Noether Theorem (Relativistic Particle)"
  - "Def - Lagrangian for a Particle in a Vector Field"
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
tags: [physics, special-relativity]
---

# Problem Statement

A charged particle moves in a vector field with Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu} + q A_\mu(x)\dot x^\mu$ (with $c = 1$). Use [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] to find conserved quantities from cyclic coordinates.

1. Suppose the potential is **static**: $A_\mu$ does not depend on the time coordinate $x^0 = t$. Show that the energy $p_0 = m u_0 + q A_0$ is conserved, and identify the generator.
2. Suppose the potential is **independent of $x^1$** (translational symmetry in the $x$-direction). Show that $p_1 = m u_1 + q A_1$ is conserved.
3. Suppose the potential is **axially symmetric** about the $z$-axis. Show that the angular momentum $J_{xy} = x p_y - y p_x$ is conserved (where $p_i$ are the canonical momenta).
4. Contrast the conserved *canonical* momentum with the *kinetic* momentum, and explain which is conserved.

**Recall:**

![[Thm - Noether Theorem (Relativistic Particle)#Statement]]

A coordinate $x^{\mu_0}$ is **cyclic** if the Lagrangian does not depend on it explicitly, $\partial L/\partial x^{\mu_0} = 0$. The generalized (canonical) four-momentum is $p_\mu = \partial L/\partial\dot x^\mu = m u_\mu + q A_\mu$ for a particle in a vector field; the kinetic momentum is $m u_\mu = p_\mu - q A_\mu$ (see [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]). Noether's theorem applied to a cyclic coordinate gives conservation of its conjugate canonical momentum.

---

# Convergent Strategy

**Problem class.** A *cyclic-coordinate* problem — the simplest application of [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]], where the symmetry is the absence of a coordinate from the Lagrangian and the conserved quantity is the conjugate canonical momentum. This is the relativistic version of "ignorable coordinates" from classical mechanics.

**Assumption pattern.** Each part supplies a symmetry of the *potential*: time-independence (static field), $x^1$-independence (translational symmetry), or axial symmetry. Each is the statement that the Lagrangian has no explicit dependence on the corresponding coordinate, i.e. that coordinate is cyclic, so its canonical momentum is conserved.

**Theorem routing.** A cyclic coordinate $x^{\mu_0}$ is a translation symmetry with generator $G^\mu = \delta^\mu_{\;\mu_0}$; [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] gives $p_\mu G^\mu = p_{\mu_0} = \text{const}$, the conjugate [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian|canonical momentum]]. For the axial case the generator is a rotation, $G^\mu = (\text{rotation})^\mu_{\;\nu}x^\nu$, giving conserved $J_{xy}$.

**Key decision point.** The crucial point is that the conserved quantity is the *canonical* momentum $p_\mu = m u_\mu + q A_\mu$, *not* the kinetic momentum $m u_\mu$. When a field is present, the kinetic momentum alone is not conserved even along a cyclic direction — the field exchanges momentum with the particle — but the canonical momentum, which includes the field's contribution $q A_\mu$, is. Recognising which momentum Noether conserves is the whole subtlety.

---

# Legal Operations Used

1. **Apply Noether's theorem** (operation 3 from the topic page). A cyclic coordinate is a translation symmetry; its canonical conjugate momentum is conserved.

2. **Compute the generalized four-momentum** (operation 5). For a particle in a vector field, $p_\mu = \partial L/\partial\dot x^\mu = m u_\mu + q A_\mu$, the canonical momentum that Noether conserves.

3. **Recognise a conserved quantity as a momentum contracted with a generator** (operation 9). A cyclic direction $x^{\mu_0}$ has generator $\delta^\mu_{\;\mu_0}$, so the conserved charge is $p_{\mu_0}$ itself.

---

# Hints

> [!note]- Hint 1
> If $A_\mu$ does not depend on $t = x^0$, then $\partial L/\partial x^0 = q(\partial_0 A_\nu)\dot x^\nu = 0$. The Euler–Lagrange equation $\tfrac{d}{d\lambda}(\partial L/\partial\dot x^0) = \partial L/\partial x^0 = 0$ gives $p_0 = \partial L/\partial\dot x^0 = m u_0 + q A_0 = \text{const}$. The generator is $G^\mu = \delta^\mu_{\;0}$ (time translation).

> [!note]- Hint 2
> Same logic with $x^1$: if $\partial L/\partial x^1 = 0$ then $p_1 = m u_1 + q A_1 = \text{const}$. The generator is $G^\mu = \delta^\mu_{\;1}$.

> [!note]- Hint 3
> Axial symmetry about $z$ means $L$ is invariant under rotations in the $xy$-plane, generator $G^\mu = (\text{rotation})^\mu_{\;\nu}x^\nu$ with $G^x = -y$, $G^y = x$ (others zero). Noether gives $p_\mu G^\mu = p_x(-y) + p_y(x) = x p_y - y p_x = J_{xy} = \text{const}$.

> [!note]- Hint 4
> The conserved $p_0 = m u_0 + q A_0$ includes the field term $q A_0$; the *kinetic* energy $m u_0$ alone is *not* conserved (the field does work). Only the canonical momentum, which accounts for the field's contribution, is conserved.

---

# Solution

The solution applies the cyclic-coordinate principle three times, for time-translation, space-translation, and rotation symmetry of the potential, and then draws the moral about canonical versus kinetic momentum. Each part is a direct application of Noether's theorem to a symmetry of the field; the only subtlety is that the conserved object is the canonical momentum, which carries the field term.

**Step 1: Static field — energy conservation.**

> [!note]- Derivation
> A static field has $\partial A_\mu/\partial x^0 = 0$ (no dependence on $t = x^0$). The position-derivative of the Lagrangian in the time direction is
> $$\frac{\partial L}{\partial x^0} = q\frac{\partial A_\nu}{\partial x^0}\dot x^\nu = 0,$$
> since the free part has no $x$-dependence and the interaction part's $x^0$-derivative vanishes. So $x^0$ is a **cyclic coordinate**: the Euler–Lagrange equation $\tfrac{d}{d\lambda}(\partial L/\partial\dot x^0) - \partial L/\partial x^0 = 0$ reduces to
> $$\frac{d}{d\lambda}\Big(\frac{\partial L}{\partial\dot x^0}\Big) = 0 \quad\Longrightarrow\quad p_0 = m u_0 + q A_0 = \text{const}.$$
> Equivalently, the generator of time translation is $G^\mu = \delta^\mu_{\;0}$, and [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] gives $p_\mu G^\mu = p_0 = \text{const}$. The conserved $p_0$ is the **total energy** of the particle in the static field, including the potential energy $q A_0 = q\phi$ (the electrostatic potential energy). A static field conserves energy.

**Step 2: $x$-translation symmetry — momentum conservation.**

> [!note]- Derivation
> If the potential is independent of $x^1$, then $\partial A_\mu/\partial x^1 = 0$, so $\partial L/\partial x^1 = 0$ and $x^1$ is cyclic. By the same argument,
> $$p_1 = m u_1 + q A_1 = \text{const},$$
> the conserved canonical momentum in the $x$-direction. The generator is $G^\mu = \delta^\mu_{\;1}$ (spatial translation along $x$). Physically: if the field configuration looks the same at every $x$ (translational symmetry in the $x$-direction), the $x$-component of canonical momentum is conserved. For example, a particle in a field that depends only on $y$ and $z$ conserves $p_1$.

**Step 3: Axial symmetry — angular momentum conservation.**

> [!note]- Derivation
> Axial symmetry about the $z$-axis means the Lagrangian is invariant under rotations in the $xy$-plane. The generator of such a rotation is $G^\mu = (R_z)^\mu_{\;\nu}x^\nu$ with the only nonzero entries giving $G^x = -y$, $G^y = +x$, $G^0 = G^z = 0$ (an infinitesimal rotation $\delta x = -\theta y$, $\delta y = +\theta x$). [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] gives the conserved charge
> $$p_\mu G^\mu = p_x G^x + p_y G^y = p_x(-y) + p_y(x) = x p_y - y p_x = J_{xy} = \text{const},$$
> the canonical angular momentum about the $z$-axis. (Here $p_x, p_y$ are the *canonical* spatial momenta $m u_i + q A_i$.) So an axially-symmetric field conserves the angular momentum about its axis — the relativistic analogue of conservation of $L_z$ for a central or axial potential. For a genuinely *central* field (spherically symmetric), all three components of angular momentum are conserved, by the same argument applied to the three rotation generators.

**Step 4: Canonical versus kinetic momentum.**

> [!note]- Derivation
> The conserved quantities are the *canonical* momenta $p_\mu = m u_\mu + q A_\mu$, which include the field contribution $q A_\mu$. The *kinetic* momentum $m u_\mu = p_\mu - q A_\mu$ is, in general, *not* conserved even along a symmetry direction, because the field exchanges momentum (and energy) with the particle. For instance, in a static electric field the kinetic energy $m u_0 = m\gamma$ changes as the particle accelerates, but the total energy $p_0 = m\gamma + q\phi$ — kinetic plus potential — is conserved: energy flows between the kinetic and potential reservoirs while the sum stays fixed. This is exactly why Noether conserves the *canonical* momentum: it is the canonical momentum, not the kinetic one, whose conjugate coordinate is cyclic, and the field term $q A_\mu$ is precisely the bookkeeping that accounts for the field's share. The lesson: when a field is present, ask for the *canonical* momentum's conservation, and remember that the kinetic momentum alone obeys no conservation law unless $A = 0$.

> [!note]- Complete formal solution
> For $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu} + q A_\mu\dot x^\mu$, a coordinate $x^{\mu_0}$ is cyclic when $\partial A_\mu/\partial x^{\mu_0} = 0$, giving $\partial L/\partial x^{\mu_0} = 0$ and hence (by Euler–Lagrange, or [[Thm - Noether Theorem (Relativistic Particle)|Noether]] with generator $\delta^\mu_{\;\mu_0}$) conservation of the canonical momentum $p_{\mu_0} = m u_{\mu_0} + q A_{\mu_0}$. A static field ($\partial_0 A = 0$) conserves the energy $p_0 = m u_0 + q A_0$; an $x^1$-independent field conserves $p_1 = m u_1 + q A_1$; an axially-symmetric field (rotation generator $G^x = -y$, $G^y = x$) conserves $J_{xy} = x p_y - y p_x$. In every case the conserved object is the *canonical* momentum including the field term $q A_\mu$; the *kinetic* momentum $m u_\mu$ alone is not conserved, because the field exchanges energy and momentum with the particle. $\blacksquare$

---

# Key Takeaways

**A cyclic coordinate conserves its canonical conjugate momentum — the simplest Noether statement, and the field term is included.** The absence of a coordinate from the Lagrangian is the simplest possible symmetry, and Noether's theorem immediately gives conservation of the conjugate canonical momentum. The relativistic content adds one wrinkle: when a field is present, the conserved canonical momentum is $p_\mu = m u_\mu + q A_\mu$, carrying the field's contribution $q A_\mu$, and it is this — not the kinetic momentum $m u_\mu$ — that is conserved. The reusable diagnostic: to find conserved quantities, look at which coordinates are *absent* from the Lagrangian (which symmetries the field respects), and write down the conjugate canonical momenta. A static field conserves energy; a translationally-symmetric field conserves linear momentum; an axially- or spherically-symmetric field conserves angular momentum. This is the workhorse method for finding constants of the motion in any field, and it is why one always seeks the symmetries of the potential first.

**Energy flows between kinetic and potential reservoirs; only the total (canonical) is conserved.** The contrast between canonical and kinetic momentum is the conceptual core of this exercise. In a static field the kinetic energy $m\gamma$ of the particle changes as it speeds up or slows down, but the total energy $m\gamma + q\phi$ stays fixed: energy is exchanged between the kinetic and potential forms while the sum is conserved. This is why Noether conserves the canonical momentum — the canonical momentum's conjugate coordinate is the cyclic one, and the field term is exactly the accounting that tracks energy moving into and out of the field. The reusable principle: in the presence of a field, the conserved quantity is always the canonical (total) momentum or energy, never the kinetic (mechanical) part alone, which obeys no conservation law on its own. This is the relativistic version of the elementary fact that mechanical energy is conserved only for conservative forces, and the canonical formalism makes it automatic.

**Symmetry of the field, not of the worldline, is what matters.** A subtle but important point: the conservation laws here come from symmetries of the *potential* $A_\mu(x)$ — its independence of time, of a spatial coordinate, or its rotational invariance — not from any property of the particular worldline. The same field conserves the same canonical momentum for *every* particle moving in it, regardless of the particle's trajectory, because the symmetry resides in the Lagrangian, which is the same for all worldlines. The trigger to recognise: to find what is conserved, examine the *field configuration*'s symmetries, not the motion; a field that looks the same under some transformation conserves the conjugate canonical momentum for all particles in it. This is why, in practice, one classifies fields by their symmetry group (static, axisymmetric, spherically symmetric) and immediately reads off the conserved quantities. For the free-particle case where all ten Poincaré symmetries hold, see [[Ex - Four-momentum conservation from translation invariance]] and [[Ex - Angular momentum and the centre of inertia from Lorentz invariance]].
