---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Boosts as Hyperbolic Rotations"
  - "Thm - Polar Decomposition of the Lorentz Group"
  - "Def - Thomas Rotation"
  - "Thm - Relativistic Velocity Addition"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\Lambda_1, \Lambda_2$ are [[Def - Boosts as Hyperbolic Rotations|Lorentz boosts]] of planes $\Pi_1, \Pi_2$, Lorentz factors $\Gamma_1, \Gamma_2$, rapidities $\psi_1, \psi_2$, velocity moduli $V_1, V_2$. When the planes differ, $\chi \in [0,\pi]$ is the angle between the boost velocities relative to the intermediate observer. $\Gamma = \cosh\psi$ is the Lorentz factor of the composite boost; $\varphi_T$ the [[Def - Thomas Rotation|Thomas rotation]] angle. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Statement

> **Theorem (Composition of boosts).** Let $\Lambda_1, \Lambda_2 \in SO^+(1,3)$ be Lorentz boosts.
>
> **(Coplanar case.)** If $\Lambda_1, \Lambda_2$ share a plane $\Pi$ (collinear velocities), then $\Lambda_2\circ\Lambda_1$ is again a boost of plane $\Pi$, with rapidities adding,
> $$\psi = \psi_1 + \psi_2, \qquad \Gamma = \Gamma_1\Gamma_2(1 + V_1 V_2), \qquad V = \frac{V_1 + V_2}{1 + V_1 V_2}.$$
> Coplanar boosts commute, $\Lambda_2\circ\Lambda_1 = \Lambda_1\circ\Lambda_2$, and form an abelian subgroup of $SO^+(1,3)$.
>
> **(General case.)** If the planes differ (velocities at angle $\chi \in (0,\pi)$), then $\Lambda_2\circ\Lambda_1$ is **not** a boost: its matrix in a semi-adapted basis is not symmetric. By the polar decomposition,
> $$\Lambda_2\circ\Lambda_1 = S \circ R,$$
> where $S$ is a boost with Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$ and velocity the relativistic sum $\mathbf{V}_1\oplus\mathbf{V}_2$, and $R \ne \mathrm{Id}$ is the Thomas rotation in the plane $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$.

---

# Motivation

The composition of boosts is the question that exposes the true structure of the Lorentz group, because the answer is counterintuitive. From the one-dimensional theory of [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group|Special Relativity IV]] — where collinear boosts compose by adding rapidities — one naturally generalises to "the composition of two boosts is a boost." This theorem says that is *false* in general. Two boosts in different directions compose to a boost *plus a rotation*, and the rotation is the Thomas rotation.

The coplanar case is the reassuring half, and it is worth stating first because it is the case one's intuition was built on. When the two boosts share a plane, everything works as expected: the result is a boost in that plane, rapidities add (so the composition is just addition in the rapidity parameter), and the boosts commute. This recovers the relativistic velocity-addition law for collinear velocities and shows that boosts along a *fixed direction* do form a one-parameter abelian subgroup. The motivation for treating this case explicitly is to mark exactly where the intuition is valid — and where it breaks.

The general case is the discovery. The key recognition is *how to tell* that the product is not a boost: a boost in a semi-adapted basis has a symmetric matrix, and the product of two boosts in non-coplanar planes is not symmetric (because the boosts do not commute, and the product of non-commuting symmetric matrices is not symmetric). So the asymmetry of the product is a flag that signals "not a boost," and the polar decomposition extracts the boost part and the leftover rotation part. The motivation is to make precise the statement "the composition of boosts fails to be a boost, and the failure is measured by a rotation."

The structural payoff is the deepest motivation. The coplanar case shows boosts along *one* direction form a subgroup; the general case shows boosts *as a whole* do not, because the composition leaves a rotation. This is the chapter's central structural fact: the set of all boosts is not a subgroup of $SO^+(1,3)$, and the obstruction is the Thomas rotation. The theorem is the bridge from the kinematics of velocity addition to the algebra of the group's simplicity.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\Lambda_1, \Lambda_2$ are boosts." The disguised sources are the situations where two boosts must be composed.

The first disguised source is **"a particle's velocity is given in a moving observer's frame."** When a particle moves with velocity $\mathbf{V}_2$ relative to an observer who moves with velocity $\mathbf{V}_1$ relative to the lab, the lab velocity is the composition of the two boosts; if the velocities are non-collinear, a Thomas rotation accompanies the change of frame. The bridge is that the change between the three frames is a product of two boosts. *Example problem:* find the lab velocity of a particle whose velocity is measured in a transversely-moving frame, including the frame rotation.

The second disguised source is **"a sequence of accelerations is applied."** A particle accelerated first in one direction, then another, undergoes successive boosts, and the net transformation is their product — a boost times a Thomas rotation when the accelerations are non-collinear. The bridge is that each acceleration increment is an infinitesimal boost. *Example problem:* compute the net frame rotation of a particle subjected to two perpendicular acceleration bursts.

The third disguised source is **"a closed loop in velocity space."** A gyroscope whose velocity traverses a closed loop (e.g. circular orbit) returns to its initial velocity but with its frame rotated by the accumulated Thomas rotations; this is the source of Thomas precession. The bridge is that the loop is a product of many infinitesimal boosts whose net is a pure rotation (since the velocity returns). *Example problem:* compute the precession of a gyroscope after one orbit by integrating infinitesimal Thomas rotations.

**Targets (Output Amplification)**

The conclusion is "$\Lambda_2\circ\Lambda_1 = S\circ R$, a boost times a (possibly trivial) Thomas rotation."

Combine the conclusion with **the velocity-addition law**. The boost factor $S$ has velocity $\mathbf{V}_1\oplus\mathbf{V}_2$ and Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$, recovering the general (non-collinear) relativistic velocity-addition formula. The further result is that velocity addition is the *boost part* of the composition, the rotation being a separate output. The combination is useful because it cleanly separates the magnitude-and-direction change (velocity addition) from the frame rotation (Thomas).

Combine the conclusion with **the non-commutativity $\Lambda_2\Lambda_1 \ne \Lambda_1\Lambda_2$**. Since the order matters, $\mathbf{V}_1\oplus\mathbf{V}_2$ and $\mathbf{V}_2\oplus\mathbf{V}_1$ have the same magnitude but differ in direction by the Thomas rotation, $\mathbf{V}_1\oplus\mathbf{V}_2 = R[\mathbf{V}_1,\mathbf{V}_2](\mathbf{V}_2\oplus\mathbf{V}_1)$. The further result is the gyrogroup structure of velocity space. The combination is nonobvious because it explains the non-commutativity of velocity addition as exactly the Thomas rotation.

Combine the conclusion with **iteration around a loop**. Composing many boosts whose velocities return to the start gives a *pure rotation* (the boost factor is trivial since the net velocity is zero), the integrated Thomas precession. The further result is the precession rate $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$. The combination is the route to Thomas precession and atomic fine structure.

---

# Why Is It True

The coplanar case is direct algebra and the general case is the polar decomposition; both rest on a single recognition about symmetry.

**Coplanar.** Two boosts of the same plane $\Pi$, in adapted coordinates with $\Pi = \mathrm{Span}(e_0, e_1)$, have $2\times 2$ matrices $\begin{pmatrix}\cosh\psi_i & \sinh\psi_i\\ \sinh\psi_i & \cosh\psi_i\end{pmatrix}$ on $\Pi$ (identity on $\Pi^\perp$). Their product on $\Pi$ is $\begin{pmatrix}\cosh\psi_1 & \sinh\psi_1\\ \sinh\psi_1 & \cosh\psi_1\end{pmatrix}\begin{pmatrix}\cosh\psi_2 & \sinh\psi_2\\ \sinh\psi_2 & \cosh\psi_2\end{pmatrix} = \begin{pmatrix}\cosh(\psi_1+\psi_2) & \sinh(\psi_1+\psi_2)\\ \sinh(\psi_1+\psi_2) & \cosh(\psi_1+\psi_2)\end{pmatrix}$, using the hyperbolic addition formulas. This is a boost of rapidity $\psi_1 + \psi_2$ — so **rapidities add, exactly as rotation angles add for rotations in a common plane**. The product is symmetric (a product of two commuting symmetric matrices), confirming it is a boost. Commutativity is immediate: the $2\times 2$ matrices commute (they are functions of the same generator), so $\Lambda_2\Lambda_1 = \Lambda_1\Lambda_2$.

**General.** The crucial recognition: a boost in a semi-adapted basis is *symmetric*, $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$. The product of two boosts in non-coplanar planes is *not* symmetric — because $(\Lambda_2\Lambda_1)^{\mathsf T} = \Lambda_1^{\mathsf T}\Lambda_2^{\mathsf T} = \Lambda_1\Lambda_2 \ne \Lambda_2\Lambda_1$ (the boosts being symmetric but non-commuting, since non-coplanar boosts do not commute). So $\Lambda_2\Lambda_1$ is not symmetric, hence **not a boost**. By the [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]] it factors uniquely as $S\circ R$ with $S$ a (symmetric) boost and $R$ a rotation, and since the product is not symmetric, $R \ne \mathrm{Id}$ — the asymmetry *is* the Thomas rotation. **The mechanism is that the product of two non-commuting symmetric matrices is not symmetric, and the symmetric part is the boost while the leftover rotation is the asymmetry.**

That the boost factor has the velocity-addition Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$ follows from computing $\Gamma = e_0\cdot(\Lambda_2\Lambda_1)(e_0)$, the time-component of the image of the initial 4-velocity, which is exactly the relativistic velocity-addition expression. The collinear case $\chi = 0$ recovers $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2)$ and $\varphi_T = 0$, and the general case is the same computation with the angle restored.

---

# What Makes This Hard

The conceptual leap is abandoning the natural expectation that "boost times boost is a boost" — true for collinear boosts, false in general — and the technical key is recognising symmetry as the boost criterion: a boost is symmetric, so the product of two non-commuting boosts (which is not symmetric) cannot be a boost. The common error is to compute the velocity-addition formula, get a velocity, and conclude the result is the boost to that velocity — missing the rotation entirely. The second subtlety is that the angle $\chi$ in the formulas is the angle between the velocities *relative to a specific intermediate observer*, not an absolute angle, and getting the reference frame wrong corrupts the Thomas-angle computation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Coplanar: multiply the $2\times 2$ boost matrices in the common plane and use hyperbolic addition to see rapidities add. General: show the product of two non-coplanar boosts is not symmetric (hence not a boost), then polar-decompose to extract the boost $S$ (velocity the relativistic sum) and the leftover Thomas rotation $R$.

**Subgoal decomposition:**

1. **Coplanar boosts compose with rapidities adding.** Multiply the $2\times 2$ matrices and apply hyperbolic addition formulas.
   - *Hint:* $\cosh\psi_1\cosh\psi_2 + \sinh\psi_1\sinh\psi_2 = \cosh(\psi_1+\psi_2)$.
   - *Why needed:* It establishes the coplanar case and the abelian subgroup.

2. **A boost is symmetric in a semi-adapted basis.** Recall $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$ for a boost when $e_0$ lies in its plane.
   - *Hint:* The semi-adapted boost matrix has $\Lambda^0{}_j = \Lambda^j{}_0 = \Gamma V_j$ and a symmetric spatial block.
   - *Why needed:* It is the criterion that distinguishes boosts from non-boosts.

3. **The product of non-coplanar boosts is not symmetric.** Show $(\Lambda_2\Lambda_1)^{\mathsf T} = \Lambda_1\Lambda_2 \ne \Lambda_2\Lambda_1$.
   - *Hint:* Transpose reverses order; symmetric factors give $(\Lambda_2\Lambda_1)^{\mathsf T} = \Lambda_1\Lambda_2$; non-coplanar boosts do not commute.
   - *Why needed:* It proves the product is not a boost.

4. **Polar-decompose to extract the boost and the Thomas rotation.** Apply the polar decomposition; the boost has $\Gamma = e_0\cdot\Lambda_2\Lambda_1(e_0) = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$, and the leftover rotation is the Thomas rotation.
   - *Hint:* The boost factor is forced by the image of $e_0$; the rotation is the asymmetry.
   - *Why needed:* It delivers the general statement and the Thomas rotation.

---

# Lemma Decomposition

> [!note]- Lemma 1: Coplanar boosts add rapidities and commute
> **Statement:** Two boosts of a common plane $\Pi$, rapidities $\psi_1, \psi_2$, compose to a boost of $\Pi$ with rapidity $\psi_1 + \psi_2$, and they commute.
>
> **Hint:** Multiply the $2\times 2$ matrices; use hyperbolic addition.
>
> **Why needed:** It is the coplanar case and the abelian-subgroup statement.
>
> > [!note]- Full proof
> > In adapted coordinates with $\Pi = \mathrm{Span}(e_0, e_1)$, each boost acts on $\Pi$ by $B(\psi_i) = \begin{pmatrix}\cosh\psi_i & \sinh\psi_i\\ \sinh\psi_i & \cosh\psi_i\end{pmatrix}$ and as the identity on $\Pi^\perp$. The product on $\Pi$ is
> > $$B(\psi_2)B(\psi_1) = \begin{pmatrix}\cosh\psi_2\cosh\psi_1 + \sinh\psi_2\sinh\psi_1 & \cosh\psi_2\sinh\psi_1 + \sinh\psi_2\cosh\psi_1\\ \sinh\psi_2\cosh\psi_1 + \cosh\psi_2\sinh\psi_1 & \sinh\psi_2\sinh\psi_1 + \cosh\psi_2\cosh\psi_1\end{pmatrix} = B(\psi_1+\psi_2),$$
> > using $\cosh(a+b) = \cosh a\cosh b + \sinh a\sinh b$ and $\sinh(a+b) = \sinh a\cosh b + \cosh a\sinh b$. This is a boost of rapidity $\psi_1 + \psi_2$. Since $B(\psi_2)B(\psi_1) = B(\psi_1+\psi_2) = B(\psi_1)B(\psi_2)$, they commute. Translating to velocities via $V = \tanh\psi$, $\Gamma = \cosh\psi$, $\Gamma V = \sinh\psi$ gives $\Gamma = \cosh(\psi_1+\psi_2) = \Gamma_1\Gamma_2 + \Gamma_1V_1\Gamma_2V_2 = \Gamma_1\Gamma_2(1+V_1V_2)$ and $V = \tanh(\psi_1+\psi_2) = (V_1+V_2)/(1+V_1V_2)$. $\blacksquare$

> [!note]- Lemma 2: A boost in a semi-adapted basis is symmetric
> **Statement:** A boost of plane $\Pi$, in any orthonormal basis with $e_0 \in \Pi$ (semi-adapted), has a symmetric matrix $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$.
>
> **Hint:** The semi-adapted boost matrix is $\Lambda^0{}_0 = \Gamma$, $\Lambda^0{}_j = \Lambda^j{}_0 = \Gamma V_j$, $\Lambda^i{}_j = \delta^i_j + \frac{\Gamma-1}{V^2}V^iV^j$.
>
> **Why needed:** Symmetry is the criterion separating boosts from non-boosts.
>
> > [!note]- Full proof
> > Let $\mathbf{V} = V^i e_i$ be the boost velocity in the rest space of $e_0$. The boost acts by $\Lambda(e_0) = \Gamma(e_0 + V^i e_i)$ and on a spatial vector $\mathbf{v}$ it is the identity plus the velocity-dependent correction; in components,
> > $$\Lambda^\alpha{}_\beta = \begin{pmatrix} \Gamma & \Gamma V_j \\ \Gamma V^i & \delta^i_j + \frac{\Gamma - 1}{V^2}V^i V^j \end{pmatrix}.$$
> > This matrix is manifestly symmetric: $\Lambda^0{}_j = \Gamma V_j = \Gamma V^j = \Lambda^j{}_0$ (lowering and raising spatial indices with the Euclidean metric of the rest space), and the spatial block $\delta^i_j + \frac{\Gamma-1}{V^2}V^iV^j$ is symmetric in $i, j$. Hence $\Lambda^\alpha{}_\beta = \Lambda^\beta{}_\alpha$. $\blacksquare$

> [!note]- Lemma 3: The product of non-coplanar boosts is not symmetric
> **Statement:** If $\Lambda_1, \Lambda_2$ are boosts whose planes are not coplanar (velocities at angle $\chi \in (0,\pi)$), then $\Lambda_2\Lambda_1$ is not symmetric, hence not a boost.
>
> **Hint:** Transpose reverses the order; non-coplanar boosts do not commute.
>
> **Why needed:** It proves the product is not a boost, forcing the polar decomposition.
>
> > [!note]- Full proof
> > By Lemma 2, $\Lambda_1, \Lambda_2$ are symmetric in a common semi-adapted basis (with $e_0$ the intermediate 4-velocity, in both planes). Then $(\Lambda_2\Lambda_1)^{\mathsf T} = \Lambda_1^{\mathsf T}\Lambda_2^{\mathsf T} = \Lambda_1\Lambda_2$. If $\Lambda_2\Lambda_1$ were symmetric, we would have $\Lambda_2\Lambda_1 = \Lambda_1\Lambda_2$, i.e. the boosts would commute. But two boosts of non-coplanar planes do not commute (their composition depends on the order, as the velocity-addition directions $\mathbf{V}_1\oplus\mathbf{V}_2 \ne \mathbf{V}_2\oplus\mathbf{V}_1$ differ by the Thomas rotation). Hence $\Lambda_2\Lambda_1$ is not symmetric, and by Lemma 2 it is not a boost. $\blacksquare$

> [!note]- Lemma 4: Polar decomposition extracts the boost and the Thomas rotation
> **Statement:** $\Lambda_2\Lambda_1 = S\circ R$, where $S$ is the boost with $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$ carrying $e_0$ to the final velocity, and $R$ is the Thomas rotation.
>
> **Hint:** Apply the polar decomposition relative to $e_0$; the boost is determined by the image $\Lambda_2\Lambda_1(e_0)$.
>
> **Why needed:** It delivers the general statement.
>
> > [!note]- Full proof
> > By the [[Thm - Polar Decomposition of the Lorentz Group|polar decomposition]] relative to $e_0$, $\Lambda_2\Lambda_1 = S\circ R$ uniquely, with $S$ the boost carrying $e_0$ to $e_0'' := \Lambda_2\Lambda_1(e_0)$ and $R = S^{-1}\Lambda_2\Lambda_1$ a rotation fixing $e_0$. The Lorentz factor of $S$ is
> > $$\Gamma = e_0\cdot e_0'' = e_0\cdot\Lambda_2\Lambda_1(e_0) = \Gamma_1\Gamma_2(1 + V_1 V_2\cos\chi),$$
> > the time-component of the doubly-boosted 4-velocity, which is the relativistic velocity-addition expression for non-collinear velocities. By Lemma 3 the product is not symmetric, so $R \ne \mathrm{Id}$: this $R$ is the [[Def - Thomas Rotation|Thomas rotation]], in the plane $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$. For collinear boosts ($\chi = 0$), the product *is* symmetric (Lemma 1), so $R = \mathrm{Id}$ and the composite is a pure boost. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\Lambda_1, \Lambda_2 \in SO^+(1,3)$ be boosts.
>
> **Coplanar case.** Suppose $\Lambda_1, \Lambda_2$ share a plane $\Pi$. By Lemma 1, in adapted coordinates their product on $\Pi$ is the boost of rapidity $\psi_1 + \psi_2$, so $\Lambda_2\Lambda_1$ is a boost of $\Pi$ with $\psi = \psi_1+\psi_2$, $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2)$, $V = (V_1+V_2)/(1+V_1V_2)$, and the boosts commute. Boosts of a fixed plane thus form an abelian subgroup (closed under products by this computation, under inverses since $-\psi$ gives the inverse boost, containing the identity $\psi = 0$).
>
> **General case.** Suppose the planes differ, velocities at angle $\chi \in (0,\pi)$ relative to the intermediate observer $e_0$. By Lemma 2, $\Lambda_1, \Lambda_2$ are symmetric in a semi-adapted basis with $e_0$ in both planes. By Lemma 3, $\Lambda_2\Lambda_1$ is not symmetric, hence not a boost. By Lemma 4, the polar decomposition gives $\Lambda_2\Lambda_1 = S\circ R$ with $S$ a boost of Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$ and velocity $\mathbf{V}_1\oplus\mathbf{V}_2$, and $R \ne \mathrm{Id}$ the Thomas rotation in $\mathrm{Span}(\mathbf{V}_1,\mathbf{V}_2)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Non-commuting flows and the BCH formula.** Composing two boosts is composing two flows $\exp(\psi_1 K_1)\exp(\psi_2 K_2)$, and the Baker–Campbell–Hausdorff formula gives the result as $\exp(\psi_1 K_1 + \psi_2 K_2 + \tfrac12[\psi_1 K_1, \psi_2 K_2] + \cdots)$; the commutator $[K_1, K_2] = -J_3$ (a rotation generator) is the infinitesimal Thomas rotation. The application is to recognise the Thomas rotation as the BCH commutator term, $\tfrac12[\mathbf{V}_1, \mathbf{V}_2]$-like, and to see why boosts close only when collinear (commuting). It is out-of-distribution because BCH is usually met in Lie theory and quantum mechanics, not relativistic kinematics.

**Parallel transport on the hyperboloid.** The composition of boosts is parallel transport on the velocity hyperboloid (hyperbolic space), and the Thomas rotation is the holonomy around the geodesic triangle traced by the two boosts. The application connects to the Gauss–Bonnet theorem: the holonomy angle equals the area of the triangle (with the curvature $-1$ of the unit hyperboloid). It battle-tests the "holonomy = enclosed curvature" pattern, the same one behind the Foucault pendulum and Berry's phase.

**Rotation composition and the spherical excess.** The Euclidean analogue: composing two *rotations* about different axes is a rotation about a third axis, and the "defect" is governed by the spherical triangle of the axes (spherical excess). The application is to compare the Thomas rotation (hyperbolic, from boosts) with the rotation-composition defect (spherical, from rotations), recognising both as holonomy — one on the hyperboloid of velocities, the other on the sphere of rotation axes. It is a surprising parallel between the composition laws of the two halves of the Lorentz group.

---

# Bridges

- **[[Def - Thomas Rotation]]** — this theorem is the existence proof and computation of the Thomas rotation: the rotation factor $R$ in the polar decomposition of the product of two non-coplanar boosts. The definition names the object; the theorem produces it and identifies the controlling parameter $\chi$, the angle between the boost velocities.

- **[[Thm - Relativistic Velocity Addition|Relativistic velocity addition]]** — the boost factor $S$ has velocity exactly $\mathbf{V}_1\oplus\mathbf{V}_2$, so the velocity-addition law is the *boost part* of the composition of boosts. For collinear velocities the rotation vanishes and the law is the familiar $V = (V_1+V_2)/(1+V_1V_2)$; for non-collinear velocities the law gives the boost velocity and the Thomas rotation is the extra rotation. This theorem is the bridge that explains *why* non-collinear velocity addition is non-commutative — the two orders differ by the Thomas rotation.

- **The simplicity of $SO^+(1,3)$** — the general case shows the boosts do not form a subgroup, which is the kinematic shadow of the algebraic fact that $SO^+(1,3)$ is a *simple* group with no proper normal subgroup. If the boosts formed a subgroup it would (being preserved by conjugation, since a conjugate of a boost is a boost) be normal — contradicting simplicity. The Thomas rotation is the obstruction that simplicity demands, and this theorem is where it appears.

---

# Unlocked by This

> [!tip] Thomas Precession from the Integrated Rotation *(from Special Relativity XVI)*
> Iterating this theorem around a closed velocity loop — the situation of an accelerating particle — gives the **Thomas precession**: the velocity returns to its start (so the net boost is trivial), but the accumulated infinitesimal Thomas rotations integrate to a net spatial rotation of the particle's frame. For circular motion the rate is $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$, derived precisely by composing the infinitesimal boosts of successive instants and extracting the rotation factor this theorem provides. This is the kinematic origin of the relativistic correction to spin precession, measured in atomic fine structure and in the precession of gyroscopes in orbit. See [[Special Relativity XVI — Accelerated Observers]] and [[Thm - The Thomas Equation]].
