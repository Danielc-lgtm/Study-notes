---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Electromagnetic Waves"
  - "Def - The Four-Potential"
  - "Thm - Maxwell Equations"
tags: [physics, special-relativity]
---

# Problem Statement

Construct and analyse the plane electromagnetic wave.

1. Starting from the vacuum field equation $\Box F = 0$, show that any field of the form $F = F_1(x - ct)$ (components depending only on the null combination $\xi = x - ct$) is a solution, and that it propagates at speed $c$ in the $+x$ direction.
2. Take the potential $A_\mu = a_\mu\cos(k\cdot x)$ with constant amplitude $a_\mu$ and wave-vector $k$. Show that $\Box A = 0$ (vacuum, Lorenz gauge) requires $k$ to be **null**, $k\cdot k = 0$, and that the Lorenz gauge $\nabla\cdot A = 0$ requires $k\cdot a = 0$ (transversality).
3. Compute the field $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ and show it is the wedge $F = -(k\wedge a)\sin(k\cdot x)$, hence that both invariants vanish: $F_{\mu\nu}F^{\mu\nu} = 0$ and ${\star}F_{\mu\nu}F^{\mu\nu} = 0$ — the wave is **null**.
4. Decompose onto an observer and show $\mathbf E\perp\mathbf B\perp\hat{\mathbf n}$ form a right-handed orthogonal triad with $|\mathbf E| = c|\mathbf B|$.

**Recall:**

![[Thm - Electromagnetic Waves#Statement]]

The [[Def - The Four-Potential|four-potential]] is the $1$-form $A$ with $F = dA$, i.e. $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. The d'Alembertian is $\Box = \nabla_\mu\nabla^\mu = \partial_t^2 - \nabla^2$ (in inertial coordinates, $c = 1$, signature $(+{-}{-}{-})$). The wave-vector $k$ has $k\cdot x = \eta_{\mu\nu}k^\mu x^\nu = k^0 x^0 - \mathbf k\cdot\mathbf x$; relative to an observer, $k^\mu = (\omega, \mathbf k)$ with $\omega$ the frequency, and $k$ null means $\omega = |\mathbf k|$ (so the phase velocity is $c$).

---

# Convergent Strategy

**Problem class.** A *characterise-a-field's-structure* problem combined with a *solve-Maxwell* problem, the third and fourth targets of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: build a solution of the wave equation and read off its invariants and polarisation. The routine is to posit a plane-wave ansatz, impose the wave equation and gauge condition to constrain it, then compute the field and its invariants.

**Assumption pattern.** The given is the vacuum wave equation $\Box F = 0$ (equivalently $\Box A = 0$ in Lorenz gauge). The signpost is "plane wave" — dependence on a single phase $k\cdot x$, which reduces the partial differential equation to algebraic conditions on $k$ and $a$. What this unlocks is that $\Box A = 0$ becomes $k\cdot k = 0$ (null) and $\nabla\cdot A = 0$ becomes $k\cdot a = 0$ (transverse).

**Theorem routing.** The route is: $\Box F = 0 \to$ d'Alembert solution $F_1(x - ct)$ (Lemma 2 of [[Thm - Electromagnetic Waves]]); plane-wave ansatz $A = a\cos(k\cdot x) \to \Box A = -(k\cdot k)A$, so $k\cdot k = 0$; Lorenz gauge $\to k\cdot a = 0$; field $F = -(k\wedge a)\sin \to$ invariants vanish (Lemma 3); decompose $\to \mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ triad (Lemma 4).

**Key decision point.** The crux is realising that the wedge structure $F = k\wedge a$ — forced by $F = dA$ with $A$ depending only on $k\cdot x$ — is what makes *both* invariants vanish automatically, classifying the wave as null. The temptation is to compute the invariants by brute force in components; the insight is that the wedge $F = p\wedge q$ kills ${\star}F\cdot F$ by antisymmetry (repeated arguments in $\epsilon$) and kills $F\cdot F$ by $k\cdot k = k\cdot a = 0$. Recognising the wedge is the shortcut.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the field as $F = dA$).** Parts 2–3 work through the potential $A = a\cos(k\cdot x)$ and compute $F = dA$.

2. **Operation 4 from the topic page (choose the Lorenz gauge).** Part 2 imposes $\nabla\cdot A = 0$, giving the transversality $k\cdot a = 0$.

3. **Operation 8 from the topic page (recognise an exterior product $F = p\wedge q$ to kill $I_2$).** Part 3 uses the wedge $F = -(k\wedge a)\sin$ to show both invariants vanish.

4. **Operation 7 from the topic page (project onto an observer).** Part 4 decomposes the wedge into $\mathbf E$, $\mathbf B$ relative to an observer.

---

# Hints

> [!note]- Hint 1
> Factor the d'Alembertian in the $(t, x)$ plane: $\Box = \partial_t^2 - \partial_x^2 = (\partial_t - \partial_x)(\partial_t + \partial_x)$ (with $c = 1$). The operator $\partial_t + \partial_x$ annihilates functions of $x - t$. So any $F_1(x - ct)$ solves $\Box F = 0$; it is constant on the planes $x - ct = \text{const}$, which move at $dx/dt = c$.

> [!note]- Hint 2
> For $A = a\cos(k\cdot x)$, $\partial_\mu A_\nu = -a_\nu k_\mu\sin(k\cdot x)$, so $\Box A_\nu = \partial^\mu\partial_\mu A_\nu = -(k^\mu k_\mu)a_\nu\cos(k\cdot x) = -(k\cdot k)A_\nu$. For $\Box A = 0$ with $A \ne 0$, need $k\cdot k = 0$. For Lorenz gauge, $\nabla\cdot A = \partial^\mu A_\mu = -(k^\mu a_\mu)\sin(k\cdot x) = -(k\cdot a)\sin$, which vanishes iff $k\cdot a = 0$.

> [!note]- Hint 3
> $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = -(k_\mu a_\nu - k_\nu a_\mu)\sin(k\cdot x) = -(k\wedge a)_{\mu\nu}\sin$. For the invariants of a wedge $F = k\wedge a$: $F_{\mu\nu}F^{\mu\nu} = 2[(k\cdot k)(a\cdot a) - (k\cdot a)^2]$, which is zero since $k\cdot k = 0$ and $k\cdot a = 0$; and ${\star}F_{\mu\nu}F^{\mu\nu} \propto \epsilon_{\mu\nu\rho\sigma}k^\mu a^\nu k^\rho a^\sigma = 0$ (repeated $k$, $a$ in the totally antisymmetric $\epsilon$).

> [!note]- Hint 4
> Write $k = \omega(U_0 + \hat{\mathbf n})$ for an observer of four-velocity $U_0$, with $\hat{\mathbf n}$ the unit propagation direction. The polarisation $a$, transverse to $k$ and (after a residual gauge choice) to $U_0$, is a spatial vector $\mathbf a\perp\hat{\mathbf n}$. From $F = k\wedge a$: $\mathbf E = F(\cdot, U_0) \propto \omega\mathbf a$ and $\mathbf B = {\star}F(\cdot, U_0) \propto \omega\,\hat{\mathbf n}\times\mathbf a$; check orthogonality and $|\mathbf E| = c|\mathbf B|$.

---

# Solution

The plane wave is built from a single null wave-vector and a transverse polarisation. Step 1 establishes the d'Alembert solution; Step 2 imposes the wave equation and Lorenz gauge to fix $k$ null and $a$ transverse; Step 3 computes the field as a wedge and shows both invariants vanish; Step 4 reads off the $\mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ triad. The non-obvious move is in Step 3: the wedge structure kills both invariants at once.

**Step 1: Any $F = F_1(x - ct)$ solves the wave equation and propagates at $c$.**

> [!note]- Derivation
> In the $(t, x)$ plane, the d'Alembertian factors:
> $$\Box = \partial_t^2 - \partial_x^2 = (\partial_t - \partial_x)(\partial_t + \partial_x) \qquad (c = 1).$$
> Let $\xi = x - ct$. Then $\partial_t f(\xi) = -c f'(\xi)$ and $\partial_x f(\xi) = f'(\xi)$, so $(\partial_t + c\partial_x)f(\xi) = 0$. Hence $\Box F_1(x - ct) = 0$: any field depending only on $\xi = x - ct$ solves the vacuum wave equation. Such a field is constant on the surfaces $x - ct = \text{const}$, which advance at $dx/dt = c$ in the $+x$ direction — a wave propagating at the speed of light. (The general solution is $F_1(x - ct) + F_2(x + ct)$, left- and right-movers.)

**Step 2: $\Box A = 0$ forces $k$ null; Lorenz gauge forces $k\cdot a = 0$.**

> [!note]- Derivation
> Take the [[Def - The Four-Potential|potential]] $A_\nu = a_\nu\cos(k\cdot x)$ with constant $a_\nu$, $k_\mu$. Differentiate: $\partial_\mu A_\nu = -a_\nu k_\mu\sin(k\cdot x)$, and $\partial^\mu\partial_\mu A_\nu = -a_\nu(k^\mu k_\mu)\cos(k\cdot x) = -(k\cdot k)A_\nu$. So
> $$\Box A_\nu = -(k\cdot k)A_\nu.$$
> For a nontrivial wave ($A \ne 0$), $\Box A = 0$ requires
> $$k\cdot k = 0 \qquad\text{(null wave-vector)}.$$
> Relative to an observer, $k^\mu = (\omega, \mathbf k)$ and $k\cdot k = \omega^2 - |\mathbf k|^2 = 0$ gives $\omega = |\mathbf k|$ — the phase velocity $\omega/|\mathbf k| = 1 = c$. The [[Def - Gauge Choice and the Lorenz Gauge|Lorenz gauge]] condition $\nabla\cdot A = \partial^\mu A_\mu = -(k^\mu a_\mu)\sin(k\cdot x) = -(k\cdot a)\sin(k\cdot x)$ vanishes for all $x$ iff
> $$k\cdot a = 0 \qquad\text{(transversality)}.$$

**Step 3: The field is a wedge, so both invariants vanish.**

> [!note]- Derivation
> Compute $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu = -(k_\mu a_\nu - k_\nu a_\mu)\sin(k\cdot x)$, i.e.
> $$F = -(k\wedge a)\sin(k\cdot x), \qquad F_{\mu\nu} = -(k_\mu a_\nu - k_\nu a_\mu)\sin(k\cdot x).$$
> First invariant:
> $$F_{\mu\nu}F^{\mu\nu} = \sin^2(k\cdot x)\cdot 2[(k\cdot k)(a\cdot a) - (k\cdot a)^2] = 0,$$
> since $k\cdot k = 0$ and $k\cdot a = 0$ (Step 2). Second invariant:
> $${\star}F_{\mu\nu}F^{\mu\nu} = \tfrac12\epsilon_{\mu\nu\rho\sigma}F^{\rho\sigma}F^{\mu\nu} \propto \sin^2(k\cdot x)\,\epsilon_{\mu\nu\rho\sigma}k^\mu a^\nu k^\rho a^\sigma = 0,$$
> because the totally antisymmetric $\epsilon$ is contracted with $k$ appearing twice (indices $\mu, \rho$) and $a$ twice (indices $\nu, \sigma$). **Both invariants vanish: the wave is null.** This means no observer can transform it to a purely electric or purely magnetic field; it looks like a wave to everyone, only Doppler-shifted.

**Step 4: $\mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ are a right-handed orthogonal triad with $|\mathbf E| = c|\mathbf B|$.**

> [!note]- Derivation
> Relative to an observer of four-velocity $U_0$, decompose the null wave-vector as $k = \omega(U_0 + \hat{\mathbf n})$ with $\hat{\mathbf n}$ a unit spatial vector ($|\hat{\mathbf n}| = 1$, the propagation direction) and $\omega$ the frequency. The polarisation $a$ is transverse to $k$; using the residual gauge freedom to set $a\cdot U_0 = 0$, $a = \mathbf a$ is a spatial vector, and $k\cdot a = 0$ becomes $\hat{\mathbf n}\cdot\mathbf a = 0$, so $\mathbf a\perp\hat{\mathbf n}$.
>
> From $F = -(k\wedge a)\sin$, the electric field is $\mathbf E = F(\cdot, U_0)$. Since $k\wedge a = (\omega U_0 + \omega\hat{\mathbf n})\wedge\mathbf a$ and $\mathbf a\perp U_0$, contracting with $U_0$ picks out $\mathbf E \propto \omega\mathbf a\sin(k\cdot x)$ — **transverse**, along $\mathbf a$. The magnetic field is $\mathbf B = {\star}F(\cdot, U_0) \propto \omega(\hat{\mathbf n}\times\mathbf a)\sin(k\cdot x)$ — also transverse, and **perpendicular to $\mathbf E$** (since $\hat{\mathbf n}\times\mathbf a\perp\mathbf a$). The magnitudes:
> $$|\mathbf B| = |\hat{\mathbf n}\times\mathbf a|\,\frac{\omega}{c} = |\mathbf a|\,\frac{\omega}{c} = \frac{|\mathbf E|}{c},$$
> using $|\hat{\mathbf n}| = 1$ and $\hat{\mathbf n}\perp\mathbf a$. So $\mathbf E$, $\mathbf B$, $\hat{\mathbf n}$ are mutually orthogonal with $|\mathbf E| = c|\mathbf B|$, and the orientation $\mathbf E\times\mathbf B \parallel \hat{\mathbf n}$ (the Poynting vector points along propagation) makes the triad right-handed — exactly the polarisation structure of light.

> [!note]- Complete formal solution
> The d'Alembertian factors as $(\partial_t - \partial_x)(\partial_t + \partial_x)$, so $F = F_1(x - ct)$ solves $\Box F = 0$ and propagates at $c$. For $A_\nu = a_\nu\cos(k\cdot x)$, $\Box A = -(k\cdot k)A$ forces $k\cdot k = 0$ (null), and Lorenz gauge $\nabla\cdot A = -(k\cdot a)\sin$ forces $k\cdot a = 0$ (transverse). The field $F = -(k\wedge a)\sin(k\cdot x)$ is a wedge, so $F_{\mu\nu}F^{\mu\nu} = 2[(k\cdot k)(a\cdot a) - (k\cdot a)^2]\sin^2 = 0$ and ${\star}F_{\mu\nu}F^{\mu\nu} \propto \epsilon_{\mu\nu\rho\sigma}k^\mu a^\nu k^\rho a^\sigma = 0$ — the wave is null. Decomposing $k = \omega(U_0 + \hat{\mathbf n})$ and $a = \mathbf a\perp\hat{\mathbf n}$ gives $\mathbf E \propto \omega\mathbf a$, $\mathbf B \propto \omega\hat{\mathbf n}\times\mathbf a$, mutually orthogonal with $|\mathbf E| = c|\mathbf B|$ and $\mathbf E\times\mathbf B\parallel\hat{\mathbf n}$ — a right-handed transverse triad, the structure of a light wave. $\blacksquare$

---

# Key Takeaways

**A plane wave reduces the wave equation to algebra: dependence on a single phase turns $\Box$ into $-k\cdot k$.** The technique that makes plane waves tractable, and that underlies all of Fourier analysis, is that an ansatz depending only on the phase $k\cdot x$ converts the differential operator $\Box$ into the algebraic factor $-(k\cdot k)$, and the gauge condition $\nabla\cdot A$ into $-(k\cdot a)$. The wave equation $\Box A = 0$ becomes the dispersion relation $k\cdot k = 0$ (the null condition, $\omega = |\mathbf k|$, propagation at $c$), and the Lorenz gauge becomes the transversality $k\cdot a = 0$. The trigger is "a field depending on a single linear phase"; the reaction is "replace each derivative $\partial_\mu$ by $k_\mu$ and solve the resulting algebraic conditions". This is exactly the momentum-space method of quantum field theory, where $\partial_\mu \to ik_\mu$ turns field equations into on-shell conditions.

**The wedge structure $F = k\wedge a$ makes both invariants vanish, classifying the wave as null in a single stroke.** Rather than computing $F_{\mu\nu}F^{\mu\nu}$ and ${\star}F_{\mu\nu}F^{\mu\nu}$ by grinding through components, recognise that a field of the form $F = p\wedge q$ (a wedge of two $1$-forms) automatically has ${\star}F\cdot F = 0$ — the $\epsilon$ tensor, totally antisymmetric, is fed the same two vectors twice and vanishes. For the wave, the additional facts $k\cdot k = 0$ and $k\cdot a = 0$ also kill $F\cdot F$. So the wave is null ($I_1 = I_2 = 0$), a frame-independent classification that distinguishes it from a Coulomb field (which can be boosted to purely electric). This wedge shortcut recurs throughout the topic: the [[Thm - The Liénard-Wiechert Potential|field of any single charge]] is also a wedge, so $\mathbf E\perp\mathbf B$ for any single charge. The transferable diagnostic: when a field strength is a wedge, its invariants are nearly free.

**The polarisation structure of light — $\mathbf E\perp\mathbf B\perp\hat{\mathbf n}$, $|\mathbf E| = c|\mathbf B|$, right-handed — is read directly off the geometry of the bivector.** The experimental facts of a light wave (transverse, with perpendicular and in-phase electric and magnetic fields of ratio $c$, and a Poynting vector along propagation) are not separate empirical inputs; they follow from decomposing the wedge $F = k\wedge a$ onto an observer, with $k$ null and $a$ transverse. The reusable insight is that the polarisation of a wave is encoded geometrically in the field $2$-form, and projecting it onto a frame extracts $\mathbf E$ and $\mathbf B$ with their orthogonality and ratio automatic. The two independent choices of transverse polarisation $\mathbf a$ are the two physical polarisation states, which upon quantisation become the two helicity states of the photon — the masslessness (only two states, not three) being forced by the gauge freedom that removes the longitudinal and timelike polarisations.
