---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass"
  - "Def - Metric-Compatible Connection"
  - "Def - Levi-Civita Connection"
  - "Def - Covariant Derivative along a Curve"
  - "Def - Musical Isomorphism (Flat and Sharp)"
  - "Def - Causal Classification of Tangent Vectors"
  - "Def - Lorentzian Manifold"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Thm - Existence and Uniqueness of Integral Curves"
  - "Thm - Fundamental Theorem on Flows"
  - "Thm - Existence and Uniqueness of Geodesics"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is an oriented [[Def - Lorentzian Manifold|Lorentzian]] four-manifold with metric $\langle\cdot,\cdot\rangle = g$ of signature $(-,+,+,+)$, index $p = 1$; we use natural units with the speed of light $c = 1$. A tangent vector $v \in T_qM$ is **timelike** when $\langle v, v\rangle < 0$, **spacelike** when $\langle v, v\rangle > 0$, and **null** when $\langle v, v\rangle = 0$ (the [[Def - Causal Classification of Tangent Vectors|causal classification]]). The symbol $\nabla$ denotes the [[Def - Levi-Civita Connection|Levi-Civita connection]] of $g$ — the unique torsion-free connection on $TM$ that is [[Def - Metric-Compatible Connection|metric-compatible]] with $g$; along a smooth curve $c : I \to M$ (with $I \subseteq \mathbb{R}$ an open interval and parameter $\tau$) it induces the [[Def - Covariant Derivative along a Curve|covariant derivative along $c$]], written interchangeably $\frac{\nabla}{d\tau}$ or $\nabla_\tau$, acting on the space $\mathfrak{X}(c)$ of smooth vector fields along $c$. We write $c'(\tau) = \frac{dc}{d\tau}(\tau) \in T_{c(\tau)}M$ for the velocity field.

The letter $F \in \Omega^2(M; \mathbb{R})$ is the [[Def - U(1) Gauge Field and Electromagnetic Connection|electromagnetic field strength]], the real global two-form obtained from the curvature of the underlying $U(1)$-connection by $\bar\Omega = iF$; being a differential two-form it is **alternating**, $F(u, w) = -F(w, u)$ for $u, w \in T_qM$, so in particular $F(w, w) = 0$. For a one-form $\eta \in T_q^*M$ the **sharp** $\eta^\sharp \in T_qM$ is the [[Def - Musical Isomorphism (Flat and Sharp)|metric dual]], characterised by $\eta(Y) = \langle \eta^\sharp, Y\rangle$ for all $Y \in T_qM$; here $F(c', \cdot)^\sharp$ is the sharp of the one-form $Y \mapsto F(c', Y)$, so that $\langle F(c', \cdot)^\sharp, Y\rangle = F(c', Y)$ by definition. In a chart $(U, x^0, x^1, x^2, x^3)$ we write $g_{kl} = \langle \partial_k, \partial_l\rangle$, $g^{kl}$ for the inverse matrix, $\Gamma^k_{ij}$ for the Christoffel symbols of $\nabla$, and $F = \tfrac12 F_{ij}\, dx^i \wedge dx^j$ with $F_{ij} = F(\partial_i, \partial_j) = -F_{ji}$; the Einstein summation convention is in force, indices running $0, 1, 2, 3$. The **eigentime** (proper time) of a timelike curve is the parameter $s$ with $ds = \sqrt{-\langle c', c'\rangle}\, d\tau$; a curve is *parametrised by eigentime* when $\langle c', c'\rangle = -1$.

> [!warning] Convention: signature and the sign of the force
> Bär's electrodynamics chapter (the source for this page) uses signature $(-,+,+,+)$, index $p = 1$, and unit mass and charge, so timelike means $\langle v, v\rangle < 0$; the equation of motion reads $\frac{\nabla}{d\tau}c' + F(c', \cdot)^\sharp = 0$. The vault's special-relativity pages ([[Def - The Lorentz Four-Force]], SR XXI) use the opposite signature $(+,-,-,-)$ and SI units, where timelike means $\langle v, v\rangle > 0$ and the four-force reads $m\, dU/d\tau = q\, F(\cdot, U)^\sharp$. The dictionary is $g_{\text{SR}} = -g_{\text{Bär}}$ with the *same* two-form $F$ and the same fields $\vec E, \vec B$; the two forms of the equation of motion agree because reversing the sign of the metric reverses the sign of both the sharp and the meaning of "timelike" in a compensating way. This page works entirely in Bär's convention.

---

# Statement

> **Theorem (constant speed and well-posedness of the Lorentz force equation).** Let $M$ be an oriented Lorentzian four-manifold with Levi-Civita connection $\nabla$ and electromagnetic field strength $F \in \Omega^2(M; \mathbb{R})$. Consider the **equation of motion of a unit-mass, unit-charge test particle**,
> $$\frac{\nabla}{d\tau}c' + F(c', \cdot)^\sharp = 0, \qquad (3.12)$$
> for a smooth curve $c : I \to M$ with velocity $c'$.
>
> **Part (i) — constant speed.** Every solution $c$ of $(3.12)$ satisfies
> $$\frac{d}{d\tau}\langle c', c'\rangle = 0,$$
> so $\langle c', c'\rangle$ is constant along $c$. Consequently a solution that is timelike at one instant $\tau_0 \in I$ is timelike at every $\tau \in I$, and its parameter $\tau$ is an affine function of eigentime; that is, $c$ is parametrised proportionally to eigentime.
>
> **Part (ii) — existence and uniqueness.** For every point $p \in M$, every tangent vector $X \in T_pM$, and every $\tau_0 \in \mathbb{R}$ there is a unique maximal solution $c : I \to M$ of $(3.12)$ with $c(\tau_0) = p$ and $c'(\tau_0) = X$, defined on an open interval $I \ni \tau_0$; and the solution depends smoothly on the initial data $(\tau_0, p, X)$.

The two parts are independent in content — one is a conservation law, the other a statement of well-posedness — but they combine at once: choosing the initial velocity $X$ to be a unit timelike vector, $\langle X, X\rangle = -1$, Part (ii) produces a unique worldline and Part (i) guarantees it stays unit timelike for all $\tau$, so it is a genuine eigentime-parametrised worldline throughout its life.

---

# Motivation

Section 7.2 builds electrodynamics as a $U(1)$ gauge theory: the electromagnetic field is the curvature $F$ of a connection on a principal $U(1)$-bundle, Maxwell's equations are $dF = 0$ and $d\star F + J = 0$, and the coupling to matter is the [[Def - Worldline, Equation of Motion of a Charged Particle, and Relativistic Mass|equation of motion]] $(3.12)$, which says that the covariant acceleration of a charged test particle equals the electromagnetic force $-F(c', \cdot)^\sharp$. Having *written down* this law, we owe two things before it can be used as physics. First, we must check that it is consistent with the kinematic constraint that defines a worldline: a worldline is by hypothesis timelike, $\langle c', c'\rangle < 0$, and it would be incoherent if the very force we imposed could push the particle's velocity to the speed of light or beyond. Part (i) removes that worry decisively — the Lorentzian length of the velocity is a conserved quantity, so a particle that starts slower than light stays slower than light, forever. Second, we must know that the law *determines* the motion: given where the particle is and how fast it is going now, its entire future and past worldline should be fixed. Part (ii) is that determinism, in the sharp mathematical form of existence, uniqueness, maximality, and smooth dependence on initial conditions.

The theorem is therefore the hinge on which the physical interpretation of the whole section turns. It licenses the standing assumption, used everywhere afterwards, that a solution may be taken to satisfy $\langle c', c'\rangle = -1$ and $t' > 0$ — an assumption that would be meaningless if $\langle c', c'\rangle$ were not conserved and empty if solutions did not exist. It is also the exact place where the geometry of the connection does real work: the conservation law is not an accident of electromagnetism but a direct consequence of two structural facts — that the connection is metric-compatible and that the force two-form is alternating — and recognising this lets us see immediately which other force laws share the property and which do not.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of Part (i) is narrow — a curve solving the specific equation $(3.12)$ — but the *reason* Part (i) holds is broad, and recognising the broad reason lets one apply the same argument far outside electromagnetism.

The first disguised source is **any equation of motion "covariant acceleration $=$ force" in which the force is pointwise $g$-orthogonal to the velocity**. The bridge $B \Rightarrow A$ is the calculation of Part (i): $\frac{d}{d\tau}\langle c', c'\rangle = 2\langle \frac{\nabla}{d\tau}c', c'\rangle$, and if the covariant acceleration $\frac{\nabla}{d\tau}c'$ is orthogonal to $c'$ then the right-hand side vanishes and the speed is conserved. Electromagnetism supplies orthogonality through the alternating property of $F$, but the orthogonality is what matters, not its source. *Example problem:* a bead constrained to a surface and driven only by the normal reaction force, or a particle subject to a gyroscopic (velocity-perpendicular) control force, has conserved kinetic speed by the identical argument, even though no field two-form is present.

The second disguised source is **the geodesic equation itself**, which is the case $F = 0$. The bridge is trivial as an inclusion — set the field to zero — but conceptually important: it shows that "constant speed of geodesics" and "constant speed of charged particles" are one theorem, distinguished only by whether the extra force term happens to be orthogonal to the velocity. *Example problem:* deducing that an unforced test particle in curved spacetime moves on a geodesic with $\langle c', c'\rangle$ constant is exactly Part (i) applied with $F = 0$, recovering the corollary proved on [[Def - Metric-Compatible Connection|the metric-compatibility page]].

The third disguised source, feeding Part (ii), is **any second-order ordinary differential equation for a curve on a manifold whose right-hand side is a smooth function of position and velocity**. The bridge $B \Rightarrow A$ is the lift to a first-order system on the tangent bundle $TM$: a second-order equation $\ddot c = f(c, \dot c)$ becomes the pair $\dot x = v$, $\dot v = f(x, v)$, which is the integral-curve equation of a smooth vector field on $TM$, so the [[Thm - Existence and Uniqueness of Integral Curves|integral-curve existence theorem]] applies verbatim. *Example problem:* the equation of a particle in a position-dependent potential, $\frac{\nabla}{d\tau}c' = -\operatorname{grad} V(c)$, is well-posed for exactly this reason, and so is any Newton-type law with a smooth force field.

**Targets (Output Amplification)**

The bare conclusions — a conserved speed and a unique smooth flow — combine with further structure to give much more.

Combine Part (i) with **the geometry of the mass shell**. The conserved value $\langle c', c'\rangle = -1$ says that the velocity of an eigentime-parametrised solution lives, for all $\tau$, on the closed submanifold $\Sigma_p = \{v \in T_pM : \langle v, v\rangle = -1\}$ of each tangent space — the unit future hyperboloid, or "mass shell". The further result $E$ is that the electromagnetic flow of Part (ii) restricts to a flow on the mass-shell bundle $\{(q, v) : \langle v, v\rangle = -1\} \subseteq TM$; this is what makes the phase space of a relativistic charged particle a fixed hypersurface rather than all of $TM$, and it is the entry point to the Hamiltonian and symplectic formulation of the motion.

Combine Part (i) with **a Killing vector field of $g$ and a symmetry of $F$**. When $M$ has a Killing field $\xi$ under which $F$ is invariant, the quantity $\langle c', \xi\rangle$ (plus a field-dependent term) is conserved along solutions, by an argument that reuses the orthogonality identity of Part (i). The further result is a conservation law — energy for a timelike Killing field, angular momentum for a rotational one — so Part (i) is the first and simplest member of a Noether-type family of conserved quantities for charged motion.

Combine Part (ii) with **smooth dependence and compactness of a time interval** to obtain a genuine time-evolution map. Because the solution depends smoothly on $(\tau_0, p, X)$ and is unique, the assignment "initial data $\mapsto$ data one unit of eigentime later" is a smooth partial map on $TM$, the electromagnetic analogue of the geodesic exponential. The further result is that families of charged particles evolve by a smooth flow, which is what allows one to speak of the classical field–particle system, of caustics of charged trajectories, and of the classical limit of quantum electrodynamics.

---

# Why Is It True

Picture the velocity $c'(\tau)$ as an arrow riding along the worldline, and ask what could change its Lorentzian length $\langle c', c'\rangle$. The length can change only through the covariant acceleration $\frac{\nabla}{d\tau}c'$, and precisely by the component of that acceleration *along* the velocity — this is the content of the product rule for a metric-compatible connection, $\frac{d}{d\tau}\langle c', c'\rangle = 2\langle \frac{\nabla}{d\tau}c', c'\rangle$, in which metric compatibility is exactly what guarantees that differentiating the inner product only sees the covariant derivatives and no stray term from the metric. Now the equation of motion says the covariant acceleration *is* the force $-F(c', \cdot)^\sharp$. So the question becomes: how much of the electromagnetic force points along the velocity? The answer is none, and for a completely structural reason: the force is built from the two-form $F$ by feeding the velocity into one slot, and a two-form is alternating, so feeding the velocity into the *other* slot as well returns zero. In symbols, $\langle F(c', \cdot)^\sharp, c'\rangle = F(c', c') = 0$. The force is always exactly perpendicular to the motion.

> **The electromagnetic force does no work: it is $g$-orthogonal to the velocity because $F$ is alternating, so it can bend a worldline but never lengthen or shorten its velocity vector, and the Lorentzian speed is conserved.**

This is why the magnetic force in ordinary mechanics changes a charge's direction but not its kinetic energy, and Part (i) is the relativistic, coordinate-free version of that fact. Once the speed is known to be conserved, "timelike throughout" is immediate — a continuous quantity that is constant and negative at one instant is negative at every instant — and "proportional to eigentime" is just the observation that a constant speed integrates to an arc length linear in the parameter.

Part (ii) is true because $(3.12)$, despite its second-order and nonlinear appearance, is nothing more exotic than a smooth vector field on the tangent bundle $TM$. Reading the equation in coordinates turns it into $\ddot c^k = -\Gamma^k_{ij}\dot c^i \dot c^j - g^{kl}F_{il}\dot c^i$, whose right-hand side is a smooth function of position and velocity; introducing $v = \dot c$ as an independent coordinate lifts it to the first-order system $\dot x = v$, $\dot v = (\text{smooth})$, and a first-order system with a smooth right-hand side is exactly what the fundamental theorem of ordinary differential equations solves — uniquely, maximally, and with smooth dependence on where you start. The Lorentz force equation and the geodesic equation are the same kind of object; only the extra velocity-linear term distinguishes them.

---

# What Makes This Hard

The genuinely non-obvious step in Part (ii) is realising that the equation is well-posed *despite not being linear*: the source (Bär, Remark 3.2.2) asserts existence and uniqueness "since $(3.12)$ is a linear ODE of second order", but this is a slip — the geodesic term $\Gamma^k_{ij}\dot c^i \dot c^j$ is quadratic in the velocities, so the equation is second-order with smooth coefficients but not linear in general. The correct justification is not linearity but smoothness: one lifts to a first-order system on $TM$ and applies the Picard–Lindelöf theorem in the form of the integral-curve existence theorem, which needs only a smooth vector field, never linearity. The common error is to trust the word "linear" and reach for the linear-ODE global existence theorem, which would falsely claim solutions defined for all $\tau$; in truth the maximal interval $I$ can be bounded, exactly as for geodesics on an incomplete manifold.

The second trap concerns the phrase "parametrised proportionally to eigentime". Unlike the geodesic equation, the Lorentz force equation is **not invariant under affine reparametrisation** of $\tau$: rescaling $\tilde c(\tau) = c(\lambda\tau)$ multiplies the covariant acceleration by $\lambda^2$ but the velocity-linear force by only $\lambda$, so a rescaled solution solves $(3.12)$ only when $\lambda = 1$ (or the force vanishes). Consequently "proportional to eigentime" is a statement about the *conserved value* of $\langle c', c'\rangle$ making the parameter an affine function of proper time, not a licence to rescale a given solution into eigentime parametrisation. Eigentime parametrisation is instead secured at the level of initial data, by choosing $X$ with $\langle X, X\rangle = -1$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For Part (i), differentiate the conserved quantity $\langle c', c'\rangle$ using the metric-compatible product rule, substitute the equation of motion, and kill the surviving term with the alternating property of $F$; then read off "timelike throughout" and "proportional to eigentime" from constancy. For Part (ii), write $(3.12)$ in coordinates as a second-order system, lift it to a first-order smooth vector field $Z$ on $TM$, and invoke the integral-curve existence-uniqueness theorem and the fundamental theorem on flows.

**Subgoal decomposition:**

1. **Product rule along the curve.** Establish $\frac{d}{d\tau}\langle V, W\rangle = \langle \nabla_\tau V, W\rangle + \langle V, \nabla_\tau W\rangle$ for vector fields $V, W$ along $c$, using metric compatibility.
   - *Hint:* Work in a chart, expand $\langle V, W\rangle = g_{ij}V^i W^j$, and use the coordinate Ricci identity $\partial_k g_{ij} = g_{lj}\Gamma^l_{ki} + g_{il}\Gamma^l_{kj}$ from metric compatibility.
   - *Why needed:* It is the only tool that connects the ordinary derivative of the speed to the covariant acceleration.

2. **The force does no work.** Show $\langle F(c', \cdot)^\sharp, c'\rangle = 0$.
   - *Hint:* Unfold the sharp: $\langle F(c', \cdot)^\sharp, c'\rangle = F(c', c')$, then use that $F$ is alternating.
   - *Why needed:* It is what makes the surviving term in Part (i) vanish.

3. **Assemble Part (i).** Combine subgoals 1 and 2 with the equation of motion to get $\frac{d}{d\tau}\langle c', c'\rangle = 0$, then deduce timelike-throughout and proportional-to-eigentime.
   - *Hint:* A constant that is negative once is negative always; a constant speed integrates to arc length linear in $\tau$.
   - *Why needed:* This is the conclusion of Part (i).

4. **Coordinate form and the lift to $TM$.** Rewrite $(3.12)$ as $\ddot c^k + \Gamma^k_{ij}\dot c^i \dot c^j + g^{kl}F_{il}\dot c^i = 0$, and show this is the integral-curve equation of a globally defined smooth vector field $Z$ on $TM$.
   - *Hint:* Introduce $v^k = \dot c^k$; the system $\dot x^k = v^k$, $\dot v^k = -\Gamma^k_{ij}v^i v^j - g^{kl}F_{il}v^i$ defines $Z$; check global well-definedness via the invariant description $Z = S - (F(v, \cdot)^\sharp)^{\text{vert}}$.
   - *Why needed:* It converts the abstract equation into a smooth first-order ODE, the only kind the existence theorem handles.

5. **Assemble Part (ii).** Apply the integral-curve existence-uniqueness theorem and the fundamental theorem on flows to $Z$, and project back to $M$.
   - *Hint:* Initial data $(p, X) \in TM$; the projection of the integral curve is the solution; smooth dependence comes from the flow theorem.
   - *Why needed:* This is the conclusion of Part (ii).

---

# Lemma Decomposition

> [!note]- Lemma 1: Product rule for the covariant derivative along a curve
> **Statement:** Let $\nabla$ be a connection on $TM$ that is metric-compatible with $g$, let $c : I \to M$ be smooth, and let $V, W \in \mathfrak{X}(c)$ be smooth vector fields along $c$. Then
> $$\frac{d}{d\tau}\langle V, W\rangle = \Big\langle \frac{\nabla V}{d\tau}, W\Big\rangle + \Big\langle V, \frac{\nabla W}{d\tau}\Big\rangle.$$
>
> **Hint:** In a chart, differentiate $g_{ij}V^i W^j$ by the ordinary product rule, then substitute the coordinate Ricci identity for $\partial_k g_{ij}$ that metric compatibility supplies.
>
> **Why needed:** It is the sole bridge from $\frac{d}{d\tau}\langle c', c'\rangle$ (an ordinary derivative) to $\langle \frac{\nabla}{d\tau}c', c'\rangle$ (a covariant quantity), and hence the engine of Part (i).
>
> > [!note]- Full proof
> > Fix $\tau \in I$ and a chart $(U, x^0, \dots, x^3)$ around $c(\tau)$. Write $c^k(\tau) = x^k(c(\tau))$, $V(\tau) = V^i(\tau)\partial_i|_{c(\tau)}$, $W(\tau) = W^j(\tau)\partial_j|_{c(\tau)}$, and $g_{ij}(\tau) = g_{ij}(c(\tau))$. Then $\langle V, W\rangle = g_{ij}V^i W^j$, a product of smooth real functions of $\tau$, and the ordinary product rule gives
> > $$\frac{d}{d\tau}\langle V, W\rangle = (\partial_k g_{ij})\,\dot c^k V^i W^j + g_{ij}\dot V^i W^j + g_{ij}V^i \dot W^j \qquad \text{(product rule; } \tfrac{d}{d\tau}g_{ij} = (\partial_k g_{ij})\dot c^k \text{ by the chain rule).} \tag{1}$$
> >
> > **Insert metric compatibility.** Metric compatibility, in the coordinate (Ricci-identity) form recorded on [[Def - Metric-Compatible Connection|the metric-compatible connection page]], states $\partial_k g_{ij} = g_{lj}\Gamma^l_{ki} + g_{il}\Gamma^l_{kj}$. Substituting into the first term of $(1)$,
> > $$(\partial_k g_{ij})\dot c^k V^i W^j = g_{lj}\Gamma^l_{ki}\dot c^k V^i W^j + g_{il}\Gamma^l_{kj}\dot c^k V^i W^j \qquad \text{(Ricci identity from metric compatibility).} \tag{2}$$
> >
> > **Recognise the covariant derivatives.** By the coordinate formula for the [[Def - Covariant Derivative along a Curve|covariant derivative along a curve]], $\frac{\nabla V}{d\tau} = (\dot V^l + \Gamma^l_{ki}\dot c^k V^i)\partial_l$ and likewise for $W$. Pairing with the metric,
> > $$\Big\langle \frac{\nabla V}{d\tau}, W\Big\rangle = g_{lj}(\dot V^l + \Gamma^l_{ki}\dot c^k V^i)W^j = g_{lj}\dot V^l W^j + g_{lj}\Gamma^l_{ki}\dot c^k V^i W^j, \tag{3}$$
> > $$\Big\langle V, \frac{\nabla W}{d\tau}\Big\rangle = g_{il}(\dot W^l + \Gamma^l_{kj}\dot c^k W^j)V^i = g_{il}V^i \dot W^l + g_{il}\Gamma^l_{kj}\dot c^k V^i W^j. \tag{4}$$
> >
> > **Combine.** Adding $(3)$ and $(4)$, the two connection terms reproduce exactly the right-hand side of $(2)$, while the derivative terms $g_{lj}\dot V^l W^j$ and $g_{il}V^i \dot W^l$ are (after renaming the summed indices) the second and third terms of $(1)$. Therefore
> > $$\Big\langle \frac{\nabla V}{d\tau}, W\Big\rangle + \Big\langle V, \frac{\nabla W}{d\tau}\Big\rangle = (\partial_k g_{ij})\dot c^k V^i W^j + g_{ij}\dot V^i W^j + g_{ij}V^i \dot W^j = \frac{d}{d\tau}\langle V, W\rangle,$$
> > using $(2)$ for the first equality and $(1)$ for the second. Both sides are defined independently of the chart, so the identity holds at $\tau$; since $\tau$ was arbitrary it holds on all of $I$. Therefore the product rule holds along $c$. $\blacksquare$

> [!note]- Lemma 2: The electromagnetic force is orthogonal to the velocity
> **Statement:** For any $q \in M$ and any $w \in T_qM$, $\langle F(w, \cdot)^\sharp, w\rangle = 0$. In particular, along any curve $c$, $\big\langle F(c', \cdot)^\sharp, c'\big\rangle = 0$.
>
> **Hint:** Unfold the definition of the sharp, then use that a two-form vanishes on a repeated argument.
>
> **Why needed:** It is the fact that annihilates the one surviving term in the derivative of the speed; without it Part (i) is false (a symmetric force *would* do work).
>
> > [!note]- Full proof
> > Let $\eta = F(w, \cdot) \in T_q^*M$ be the one-form $Y \mapsto F(w, Y)$. By the defining property of the [[Def - Musical Isomorphism (Flat and Sharp)|sharp]], the vector $\eta^\sharp = F(w, \cdot)^\sharp$ satisfies $\langle \eta^\sharp, Y\rangle = \eta(Y) = F(w, Y)$ for every $Y \in T_qM$. Taking $Y = w$,
> > $$\langle F(w, \cdot)^\sharp, w\rangle = F(w, w) \qquad \text{(defining property of the sharp, with } Y = w\text{).}$$
> > Because $F \in \Omega^2(M; \mathbb{R})$ is a differential two-form, it is alternating: $F(u, v) = -F(v, u)$ for all $u, v$, and setting $u = v = w$ gives $F(w, w) = -F(w, w)$, hence $2F(w, w) = 0$ and $F(w, w) = 0$. Therefore $\langle F(w, \cdot)^\sharp, w\rangle = 0$. Applying this at $q = c(\tau)$ with $w = c'(\tau)$ gives $\langle F(c', \cdot)^\sharp, c'\rangle = 0$ at every $\tau$. $\blacksquare$

> [!note]- Lemma 3: The equation of motion lifts to a smooth vector field on $TM$
> **Statement:** In any chart $(U, x^0, \dots, x^3)$ the equation of motion $(3.12)$ is equivalent to the second-order system
> $$\ddot c^k + \Gamma^k_{ij}\dot c^i \dot c^j + g^{kl}F_{il}\dot c^i = 0 \qquad (k = 0, 1, 2, 3).$$
> Introducing the induced chart $(x^k, v^k)$ on $TM$, this is the integral-curve equation of the vector field
> $$Z_{(x, v)} = v^k \frac{\partial}{\partial x^k} - \big(\Gamma^k_{ij}(x)v^i v^j + g^{kl}(x)F_{il}(x)v^i\big)\frac{\partial}{\partial v^k},$$
> and $Z$ is a globally defined smooth vector field on $TM$, equal to $Z = S - (F(v, \cdot)^\sharp)^{\text{vert}}$ where $S$ is the geodesic spray and $(\cdot)^{\text{vert}}$ is the vertical lift. A curve $c$ solves $(3.12)$ if and only if its velocity lift $\tau \mapsto (c(\tau), c'(\tau))$ is an integral curve of $Z$.
>
> **Hint:** Expand $\frac{\nabla}{d\tau}c'$ and $F(c', \cdot)^\sharp$ in coordinates, then set $v = \dot c$ to demote the order.
>
> **Why needed:** The integral-curve existence theorem accepts only a smooth first-order vector field; this lemma produces exactly that object and certifies it is smooth and globally defined.
>
> > [!note]- Full proof
> > **Coordinate form of the covariant acceleration.** By the coordinate formula for the [[Def - Covariant Derivative along a Curve|covariant derivative along $c$]] applied to $V = c' = \dot c^i \partial_i$,
> > $$\frac{\nabla}{d\tau}c' = \big(\ddot c^k + \Gamma^k_{ij}\dot c^i \dot c^j\big)\partial_k \qquad \text{(coordinate formula for } \nabla_\tau \text{, with } V^i = \dot c^i \text{).}$$
> >
> > **Coordinate form of the force.** The one-form $F(c', \cdot)$ has components $(F(c', \cdot))_l = F(c', \partial_l) = \dot c^i F(\partial_i, \partial_l) = \dot c^i F_{il}$ (bilinearity of $F$ and $F_{il} = F(\partial_i, \partial_l)$). Raising the index with the [[Def - Musical Isomorphism (Flat and Sharp)|sharp]], whose coordinate action is $(\eta^\sharp)^k = g^{kl}\eta_l$,
> > $$\big(F(c', \cdot)^\sharp\big)^k = g^{kl}(F(c', \cdot))_l = g^{kl}F_{il}\dot c^i \qquad \text{(coordinate form of the sharp).}$$
> >
> > **Assemble the system.** Equation $(3.12)$, $\frac{\nabla}{d\tau}c' = -F(c', \cdot)^\sharp$, thus reads componentwise $\ddot c^k + \Gamma^k_{ij}\dot c^i \dot c^j = -g^{kl}F_{il}\dot c^i$, that is
> > $$\ddot c^k + \Gamma^k_{ij}\dot c^i \dot c^j + g^{kl}F_{il}\dot c^i = 0, \qquad k = 0, 1, 2, 3, \tag{5}$$
> > as claimed. Setting $v^k := \dot c^k$ makes $(5)$ the first-order system $\dot x^k = v^k$, $\dot v^k = -\Gamma^k_{ij}v^i v^j - g^{kl}F_{il}v^i$, which is by definition the integral-curve equation of the vector field $Z$ displayed above.
> >
> > **Smoothness.** The components of $Z$ are polynomials in $v$ with coefficients $\Gamma^k_{ij}(x)$, $g^{kl}(x)$, $F_{il}(x)$, each a smooth function of $x$ (the Christoffel symbols are smooth because $g$ is; $g^{kl}$ is smooth by Cramer's rule since $\det(g_{ij}) \neq 0$; $F_{il}$ is smooth because $F$ is a smooth form). Hence $Z$ is smooth on the chart domain $\pi^{-1}(U) \subseteq TM$, where $\pi : TM \to M$ is the projection.
> >
> > **Global well-definedness.** We exhibit $Z$ invariantly, so that the chart expressions patch. The **geodesic spray** $S$, $S_{(x,v)} = v^k \partial_{x^k} - \Gamma^k_{ij}v^i v^j \partial_{v^k}$, is a globally defined smooth vector field on $TM$ whose integral curves project to geodesics; this is established on [[Thm - Existence and Uniqueness of Geodesics|the geodesics page]] (its Lemma constructing the spray). For $w \in T_qM$, the **vertical lift** at $v \in T_qM$ is $w^{\text{vert}}_v := \frac{d}{ds}\big|_{s=0}(v + sw) \in T_v(TM)$, the tangent to the straight line $s \mapsto v + sw$ inside the vector space $T_qM$; in the induced chart, if $w = w^k \partial_{x^k}$ then $w^{\text{vert}}_v = w^k \partial_{v^k}$, and the construction is chart-independent because $v + sw$ is defined by the vector-space structure of the fibre alone. The assignment $v \mapsto \big(-F(v, \cdot)^\sharp\big)^{\text{vert}}_v$ is therefore a globally defined smooth vector field on $TM$: $F(v, \cdot)^\sharp \in T_qM$ is built from the global form $F$ and the metric sharp, both invariant, and its vertical lift is invariant. Its chart components are $-g^{kl}F_{il}v^i$ in the $\partial_{v^k}$ directions, matching the force part of $Z$. Hence $Z = S - (F(v, \cdot)^\sharp)^{\text{vert}}$ is a single globally defined smooth vector field on $TM$ whose local expression is the one displayed, and the chart formula $(5)$ is chart-independent.
> >
> > **Equivalence of solutions.** If $c$ solves $(3.12)$ then, by $(5)$, the curve $\gamma(\tau) := (c(\tau), c'(\tau))$ in $TM$ satisfies $\dot\gamma = Z \circ \gamma$, i.e. $\gamma$ is an integral curve of $Z$. Conversely, if $\gamma(\tau) = (x(\tau), v(\tau))$ is an integral curve of $Z$ then $\dot x = v$ forces $v = \dot x$, and the $\dot v$ equation then reads $(5)$ for $c := x$, which is $(3.12)$; moreover $\gamma = (c, c')$ is the velocity lift of $c$. Therefore solutions of $(3.12)$ correspond bijectively to integral curves of $Z$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be an oriented Lorentzian four-manifold with Levi-Civita connection $\nabla$ and electromagnetic field strength $F \in \Omega^2(M; \mathbb{R})$, and let $c$ range over smooth solutions of the equation of motion $\frac{\nabla}{d\tau}c' + F(c', \cdot)^\sharp = 0$ from $(3.12)$.
>
> **Step 0 — preconditions.** The connection $\nabla$ is the Levi-Civita connection of $g$, so it is metric-compatible with $g$ (this is one of the two defining properties of the [[Def - Levi-Civita Connection|Levi-Civita connection]]); Lemma 1 therefore applies. The field $F$ is a differential two-form, hence alternating; Lemma 2 therefore applies. Both preconditions hold for every $M$ in the hypothesis.
>
> **Part (i) — the speed is constant.** We must show $\frac{d}{d\tau}\langle c', c'\rangle = 0$. Apply Lemma 1 (product rule along $c$) with $V = W = c'$:
> $$\frac{d}{d\tau}\langle c', c'\rangle = \Big\langle \frac{\nabla}{d\tau}c', c'\Big\rangle + \Big\langle c', \frac{\nabla}{d\tau}c'\Big\rangle = 2\Big\langle \frac{\nabla}{d\tau}c', c'\Big\rangle \qquad \text{(Lemma 1, then symmetry of } g\text{).}$$
> **Substitute the equation of motion.** By $(3.12)$, $\frac{\nabla}{d\tau}c' = -F(c', \cdot)^\sharp$, so
> $$2\Big\langle \frac{\nabla}{d\tau}c', c'\Big\rangle = 2\big\langle -F(c', \cdot)^\sharp, c'\big\rangle = -2\big\langle F(c', \cdot)^\sharp, c'\big\rangle \qquad \text{(equation of motion } (3.12) \text{, then bilinearity).}$$
> **Kill the term with orthogonality.** By Lemma 2, $\langle F(c', \cdot)^\sharp, c'\rangle = F(c', c') = 0$. Combining the last two displays,
> $$\frac{d}{d\tau}\langle c', c'\rangle = -2 \cdot 0 = 0.$$
> Hence the real function $\tau \mapsto \langle c'(\tau), c'(\tau)\rangle$ has vanishing derivative on the interval $I$ and is therefore a constant $\kappa \in \mathbb{R}$.
>
> **Timelike throughout.** Suppose $c$ is timelike at some $\tau_0 \in I$, i.e. $\langle c'(\tau_0), c'(\tau_0)\rangle < 0$. Then $\kappa = \langle c'(\tau_0), c'(\tau_0)\rangle < 0$, and since $\langle c'(\tau), c'(\tau)\rangle = \kappa$ for all $\tau \in I$, we have $\langle c'(\tau), c'(\tau)\rangle < 0$ for every $\tau \in I$; that is, $c$ is timelike at every instant.
>
> **Proportional to eigentime.** With $\kappa < 0$, the speed $|c'(\tau)| := \sqrt{-\langle c', c'\rangle} = \sqrt{-\kappa}$ is a positive constant. The eigentime measured from $\tau_0$ is
> $$s(\tau) = \int_{\tau_0}^{\tau} \sqrt{-\langle c'(\sigma), c'(\sigma)\rangle}\, d\sigma = \sqrt{-\kappa}\,(\tau - \tau_0),$$
> an affine function of $\tau$ with nonzero slope $\sqrt{-\kappa}$. Thus $\tau$ is an affine function of eigentime; equivalently, $c$ is parametrised proportionally to eigentime. (When one wishes the exact normalisation $\langle c', c'\rangle = -1$, it suffices to choose the initial velocity $X$ with $\langle X, X\rangle = -1$ in Part (ii), for then $\kappa = -1$ and $s(\tau) = \tau - \tau_0$; one cannot instead rescale a given solution's parameter, because $(3.12)$ is not invariant under affine reparametrisation.) This proves Part (i).
>
> **Part (ii) — existence, uniqueness, maximality, smooth dependence.** Fix $p \in M$, $X \in T_pM$, and $\tau_0 \in \mathbb{R}$. By Lemma 3, solving $(3.12)$ is equivalent to finding an integral curve of the globally defined smooth vector field $Z$ on the manifold $TM$, and the initial conditions $c(\tau_0) = p$, $c'(\tau_0) = X$ correspond exactly to the initial point $(p, X) \in TM$ at parameter $\tau_0$ for that integral curve.
>
> **Apply the integral-curve theorem.** We invoke the following, whose complete proof is on its own page.
>
> > **Theorem (local existence and uniqueness of integral curves).** For a smooth vector field $Y$ on a smooth manifold $N$ and every point $y \in N$ there is $\varepsilon > 0$ and a smooth integral curve $\gamma : (-\varepsilon, \varepsilon) \to N$ of $Y$ with $\gamma(0) = y$; any two integral curves of $Y$ that agree at one parameter value agree on the intersection of their domains. Moreover ([[Thm - Existence and Uniqueness of Integral Curves|Corollary]]) each point lies on a *unique maximal* integral curve, defined on an open interval containing that parameter value.
>
> Applying this ([[Thm - Existence and Uniqueness of Integral Curves]]) to $Y = Z$, $N = TM$, $y = (p, X)$, and translating the parameter so that the base value is $\tau_0$ rather than $0$ (the vector field $Z$ is independent of $\tau$, so a solution through $(p, X)$ at parameter $0$ becomes one at parameter $\tau_0$ by the shift $\tau \mapsto \tau - \tau_0$), there is a unique maximal integral curve $\gamma : I \to TM$ of $Z$ with $I \ni \tau_0$ open and $\gamma(\tau_0) = (p, X)$. By the equivalence in Lemma 3, its projection $c := \pi \circ \gamma : I \to M$ is the unique maximal solution of $(3.12)$ with $c(\tau_0) = p$ and $c'(\tau_0) = X$: existence and maximality are those of $\gamma$, and uniqueness follows because any solution of $(3.12)$ with these data would lift, again by Lemma 3, to an integral curve of $Z$ through $(p, X)$ at $\tau_0$, which the theorem forces to coincide with $\gamma$ on the overlap, hence to have $c$ coincide with $\pi \circ \gamma$.
>
> **Smooth dependence.** We invoke the following.
>
> > **Theorem (fundamental theorem on flows).** For a smooth vector field $Y$ on a smooth manifold $N$, the map $(t, y) \mapsto \theta(t, y)$ sending a point to the value of its maximal integral curve is smooth on the open set $\mathcal{D} = \{(t, y) : t \in \mathcal{D}^{(y)}\} \subseteq \mathbb{R} \times N$ of definition.
>
> By this theorem ([[Thm - Fundamental Theorem on Flows]]) applied to $Z$ on $TM$, the map $(\tau, (p, X)) \mapsto \gamma_{(p, X)}(\tau)$ is smooth on its open domain; composing with the smooth projection $\pi$ and accounting for the parameter shift by $\tau_0$, the solution $c$ and its velocity $c'$ depend smoothly on $(\tau_0, p, X)$. This proves Part (ii).
>
> **Conclusion.** Every solution of $(3.12)$ has $\langle c', c'\rangle$ constant, so a solution timelike at one instant is timelike throughout and parametrised proportionally to eigentime; and for each $(\tau_0, p, X)$ there is a unique maximal solution with those initial data, depending smoothly on them. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Nonrelativistic magnetic motion and the work–energy theorem.** In ordinary three-dimensional mechanics, a charge in a magnetic field feels the force $q\,\vec v \times \vec B$, which is perpendicular to $\vec v$; the elementary theorem "the magnetic force does no work, so kinetic energy is conserved" is Part (i) stripped of its relativistic clothing. The theorem applies because $\vec v \times \vec B$ is the three-dimensional shadow of $F(c', \cdot)^\sharp$, and the perpendicularity that makes the cross product vanish against $\vec v$ is exactly the alternating property of $F$. The application is non-obvious in reverse: a student who has only seen the cross-product argument rarely realises that "perpendicular" is forced by antisymmetry of a two-form, and that the same one line proves conservation of Lorentzian speed in curved spacetime.

**Constant speed of geodesics on a Riemannian manifold.** Setting $F = 0$, Part (i) becomes the statement that an affinely parametrised geodesic has constant speed $|\dot\gamma|$, the fact underlying "arc-length parametrisation" in Riemannian geometry. The theorem applies because a geodesic is the $F = 0$ solution and the argument only used metric compatibility and the vanishing of the force term. The subtlety worth drilling is the contrast that opens up once $F \neq 0$: geodesics may be affinely reparametrised freely and remain geodesics, whereas charged trajectories may not, so the constancy of speed has a different status in the two cases even though the conservation law is proved identically.

**Well-posedness of a control or dissipative system on a manifold.** In control theory and in the study of dissipative mechanical systems, one writes equations $\frac{\nabla}{d\tau}c' = f(c, c')$ with a smooth but non-conservative force $f$ (friction, thrust, feedback). Part (ii) applies verbatim to establish that trajectories exist, are unique, and depend smoothly on initial conditions, because the lift to a smooth vector field on $TM$ needs only smoothness of $f$, not any conservation law. This is non-obvious because such systems visibly do *not* conserve energy — Part (i) fails for them — yet the well-posedness half of the theorem is completely indifferent to that failure, a clean illustration that existence-uniqueness and conservation are logically separate.

---

# Bridges

- **The geodesic equation is the $F = 0$ case.** The whole theorem specialises to [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness of geodesics]] and to "geodesics have constant speed" by deleting the force term. Concretely, the vector field $Z = S - (F(v, \cdot)^\sharp)^{\text{vert}}$ reduces to the geodesic spray $S$ when $F = 0$, so Part (ii) becomes the geodesic flow, and the orthogonality identity of Part (i) becomes trivially true because the acceleration itself vanishes. The Lorentz force equation is thus the geodesic equation perturbed by a velocity-linear, velocity-orthogonal force, and everything structural about geodesics that survives the perturbation is exactly what this page proves survives.

- **Metric compatibility is the load-bearing hypothesis of Part (i).** The conservation of speed uses [[Def - Metric-Compatible Connection|metric compatibility]] through Lemma 1 and nothing else about the connection — not torsion-freeness, not the specific Levi-Civita formula. Any metric-compatible connection would give the same conservation law, which is why the corollary "parallel transport preserves inner products" and this theorem are two faces of one hypothesis: the connection ferries the velocity vector around without distorting its length, and a force orthogonal to the velocity cannot supply the distortion either.

- **The lift to $TM$ is the universal well-posedness device.** The passage from the second-order equation on $M$ to the first-order vector field $Z$ on $TM$, used in Lemma 3, is the same construction that proves existence-uniqueness for geodesics, for Newtonian motion in a potential, and for the [[Thm - Existence and Uniqueness of Integral Curves|integral curves]] of any vector field. The bridge is that a manifold's second-order dynamics is a first-order flow on its tangent bundle; once this is internalised, "existence and uniqueness for a second-order ODE with smooth coefficients" needs no separate theorem beyond the first-order one.

- **Constant speed prepares the reduction to the Lorentz force law in coordinates.** The normalisation $\langle c', c'\rangle = -1$ with $t' > 0$, licensed by Part (i), is precisely the hypothesis under which [[Thm - The Lorentz Force Law from the Equation of Motion|the equation of motion reduces to the classical Lorentz force law]] $\frac{d}{dt}(m\vec v) = \vec E + \vec v \times \vec B$ on Minkowski space. Without the conserved speed the relativistic mass $m = m_0 t'$ would not be a well-behaved function of the trajectory, and the projection from eigentime $\tau$ to coordinate time $t$ would not be the clean reparametrisation it is on the next page.

---

# Unlocked by This

> [!tip] The mass shell as phase space *(from Geometric Mechanics)*
> Because Part (i) pins an eigentime-parametrised velocity to the unit hyperboloid $\{v : \langle v, v\rangle = -1\}$ for all time, the true phase space of a relativistic charged particle is not $TM$ but the **mass-shell bundle** over $M$, and the electromagnetic flow of Part (ii) restricts to it. This is the starting point for the symplectic and Hamiltonian formulation of charged motion and for the minimal-coupling prescription $p \mapsto p - A$.

> [!tip] Noether charges for charged motion *(from Geometric Mechanics)*
> The orthogonality identity behind Part (i) generalises: for each symmetry of the pair $(g, F)$ — a Killing field of the metric under which the field strength is invariant — there is a conserved quantity along solutions. Part (i) is the case of the "symmetry" that is the conservation of the norm itself, and the same computation yields energy and momentum conservation when a timelike or translational Killing field is present.
