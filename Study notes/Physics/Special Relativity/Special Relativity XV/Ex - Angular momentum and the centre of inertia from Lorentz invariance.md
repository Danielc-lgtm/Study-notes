---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Noether Theorem (Relativistic Particle)"
  - "Def - Angular Momentum Four-Tensor"
  - "Def - The Poincaré Group"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

A free particle has Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ (with $c = 1$), generalized momentum $p_\mu = m u_\mu$.

1. Write the generator of an infinitesimal Lorentz transformation as $G^\mu = \omega^\mu_{\;\nu}x^\nu$ with $\omega_{\mu\nu} := \eta_{\mu\rho}\omega^\rho_{\;\nu}$ antisymmetric. Verify that $L$ is invariant.
2. Apply [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] and show the conserved charge is (proportional to) the **angular-momentum four-tensor** $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$.
3. Separate the six conserved components: the three **rotations** ($J_{ij}$) give conservation of the ordinary angular momentum, and the three **boosts** ($J_{i0}$) give the **centre-of-inertia theorem** $x^i - (P^i/E)\,t = \text{const}$.
4. Verify directly that $dJ^{\mu\nu}/d\tau = 0$ on the free worldline, and interpret the boost charge physically: why does the equivalence of inertial frames imply uniform motion of the centre of mass?

**Recall:**

![[Thm - Noether Theorem (Relativistic Particle)#Statement]]

The **angular-momentum four-tensor** about the origin is $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$, antisymmetric, with spatial part $J^{ij}$ the ordinary angular momentum and mixed part $J^{i0}$ the centre-of-inertia moment; see [[Def - Angular Momentum Four-Tensor]]. An infinitesimal [[Def - The Poincaré Group|Lorentz]] transformation is $\Lambda^\mu_{\;\nu} = \delta^\mu_{\;\nu} + \omega^\mu_{\;\nu}$ with $\omega_{\mu\nu}$ antisymmetric (the condition $\Lambda^{\mathsf T}\eta\Lambda = \eta$ at first order). The six independent components of $\omega$ are three rotations and three boosts.

---

# Convergent Strategy

**Problem class.** A *read-off-a-conserved-quantity-from-a-symmetry* problem, applying [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] to the *Lorentz* part of the Poincaré group (the translations were treated separately). The six Lorentz generators give six conserved quantities, packaged in the antisymmetric tensor $J^{\mu\nu}$.

**Assumption pattern.** The free Lagrangian depends on $\dot x^\mu$ only through the Lorentz-invariant scalar $\eta_{\mu\nu}\dot x^\mu\dot x^\nu$, so it is invariant under every Lorentz transformation. The generator of an infinitesimal Lorentz transformation is $G^\mu = \omega^\mu_{\;\nu}x^\nu$ with $\omega_{\mu\nu}$ *antisymmetric* — the antisymmetry is the infinitesimal form of the defining condition $\Lambda^{\mathsf T}\eta\Lambda = \eta$.

**Theorem routing.** Lorentz invariance feeds [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]]; the conserved charge $p_\mu G^\mu = p_\mu\omega^\mu_{\;\nu}x^\nu$, with $\omega$ antisymmetric and arbitrary, forces conservation of the antisymmetric combination $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$ ([[Def - Angular Momentum Four-Tensor]]). Decomposing $\omega$ into rotations and boosts splits $J$ into angular momentum ($J_{ij}$) and the centre-of-inertia charge ($J_{i0}$).

**Key decision point.** The crux is using the *antisymmetry* of $\omega_{\mu\nu}$ to extract the antisymmetric tensor $J^{\mu\nu}$. The charge $p_\mu\omega^\mu_{\;\nu}x^\nu = \omega_{\mu\nu}x^\nu p^\mu$ involves $\omega_{\mu\nu}$ contracted with $x^\nu p^\mu$; since $\omega$ is antisymmetric, only the antisymmetric part of $x^\nu p^\mu$ contributes, which is $\tfrac12(x^\nu p^\mu - x^\mu p^\nu) = -\tfrac12 J^{\mu\nu}$. The second subtlety is the *physical* reading of the boost charge: that boost invariance — a statement about the equivalence of frames — produces a *dynamical* conservation law (uniform centre-of-mass motion) is genuinely surprising and is the relativistic centre-of-mass theorem.

---

# Legal Operations Used

1. **Apply Noether's theorem** (operation 3 from the topic page). Lorentz invariance of $L$ yields the conserved charge $p_\mu G^\mu$, which the antisymmetry of $\omega$ converts into the angular-momentum tensor.

2. **Recognise a conserved quantity as a momentum contracted with a generator** (operation 9). The generator $G^\mu = \omega^\mu_{\;\nu}x^\nu$ is built from the Lorentz Lie-algebra element $\omega$; contracting with $p_\mu$ and using antisymmetry gives $J^{\mu\nu}$.

3. **Compute the generalized four-momentum** (operation 5). The free $p_\mu = m u_\mu$ enters the angular-momentum tensor $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$.

---

# Hints

> [!note]- Hint 1
> An infinitesimal Lorentz transformation is $x'^\mu = \Lambda^\mu_{\;\nu}x^\nu = (\delta^\mu_{\;\nu} + \omega^\mu_{\;\nu})x^\nu$, so $G^\mu = \omega^\mu_{\;\nu}x^\nu$. The condition $\Lambda^{\mathsf T}\eta\Lambda = \eta$ at first order gives $\omega_{\mu\nu} + \omega_{\nu\mu} = 0$, i.e. $\omega_{\mu\nu}$ (indices lowered) is antisymmetric. $L$ is invariant because $\eta_{\mu\nu}\dot x'^\mu\dot x'^\nu = \eta_{\mu\nu}\dot x^\mu\dot x^\nu$ (the defining property of Lorentz transformations).

> [!note]- Hint 2
> Noether gives $p_\mu G^\mu = p_\mu\omega^\mu_{\;\nu}x^\nu = \omega_{\mu\nu}x^\nu p^\mu = \text{const}$. Since $\omega_{\mu\nu}$ is antisymmetric and arbitrary, only the antisymmetric part of $x^\nu p^\mu$ survives: write $\omega_{\mu\nu}x^\nu p^\mu = -\tfrac12\omega_{\mu\nu}(x^\mu p^\nu - x^\nu p^\mu) = -\tfrac12\omega_{\mu\nu}J^{\mu\nu}$. Conservation for all antisymmetric $\omega$ means each $J^{\mu\nu}$ is conserved.

> [!note]- Hint 3
> The spatial components $J^{ij} = x^i p^j - x^j p^k$ are the ordinary angular momentum $\mathbf{L} = \mathbf{x}\times\mathbf{p}$ (rotations). The mixed components $J^{i0} = x^i p^0 - x^0 p^i = E x^i - t P^i$ (boosts); setting $J^{i0} = \text{const}$ and dividing by the conserved $E$ gives $x^i - (P^i/E)t = \text{const}$.

> [!note]- Hint 4
> Direct check: $dJ^{\mu\nu}/d\tau = \dot x^\mu p^\nu + x^\mu\dot p^\nu - (\mu\leftrightarrow\nu)$. On the free worldline $\dot p^\nu = 0$ (momentum conserved) and $\dot x^\mu = U^\mu \propto p^\mu$, so $\dot x^\mu p^\nu = \dot x^\nu p^\mu$ (both $\propto p^\mu p^\nu$) and the antisymmetrised combination vanishes. Physically: boost invariance means no inertial frame is preferred; in particular the centre-of-mass frame is as good as any, and in it the particle's spatial position moves uniformly — which, boosted to any frame, is $x^i - (P^i/E)t = \text{const}$.

---

# Solution

The solution proceeds in four steps. Step 1 writes the Lorentz generator and verifies invariance. Step 2 applies Noether and extracts the antisymmetric angular-momentum tensor. Step 3 splits the six components into angular momentum (rotations) and the centre-of-inertia law (boosts). Step 4 verifies conservation directly and interprets the boost charge. The decisive technical move is using the antisymmetry of $\omega$ to project out the antisymmetric tensor $J^{\mu\nu}$; the decisive conceptual point is that boost invariance yields a dynamical conservation law.

**Step 1: The Lorentz generator and invariance.**

> [!note]- Derivation
> An infinitesimal Lorentz transformation is $x'^\mu = \Lambda^\mu_{\;\nu}x^\nu$ with $\Lambda^\mu_{\;\nu} = \delta^\mu_{\;\nu} + \omega^\mu_{\;\nu}$ and $\omega$ infinitesimal. Comparing with $x'^\mu = x^\mu + \varepsilon G^\mu$, the generator is $G^\mu = \omega^\mu_{\;\nu}x^\nu$ (absorbing $\varepsilon$ into $\omega$). The defining condition $\Lambda^{\mathsf T}\eta\Lambda = \eta$ reads, at first order in $\omega$,
> $$(\delta + \omega)^{\mathsf T}\eta(\delta + \omega) = \eta \;\Rightarrow\; \omega^{\mathsf T}\eta + \eta\omega = 0 \;\Rightarrow\; \omega_{\nu\mu} + \omega_{\mu\nu} = 0,$$
> so $\omega_{\mu\nu} := \eta_{\mu\rho}\omega^\rho_{\;\nu}$ is **antisymmetric**. It has six independent components — three for rotations (the spatial $\omega_{ij}$) and three for boosts (the mixed $\omega_{0i}$). The Lagrangian is invariant because Lorentz transformations preserve the Minkowski norm: $\eta_{\mu\nu}\dot x'^\mu\dot x'^\nu = \eta_{\mu\nu}\Lambda^\mu_{\;\rho}\Lambda^\nu_{\;\sigma}\dot x^\rho\dot x^\sigma = \eta_{\rho\sigma}\dot x^\rho\dot x^\sigma$, so $L(x', \dot x') = L(x, \dot x)$.

**Step 2: Noether gives the angular-momentum tensor.**

> [!note]- Derivation
> By [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]], the conserved charge is
> $$p_\mu G^\mu = p_\mu\,\omega^\mu_{\;\nu}x^\nu = \omega_{\mu\nu}\,x^\nu p^\mu,$$
> where in the last step we lowered with $\eta$ to write $p_\mu\omega^\mu_{\;\nu} = \omega_{\mu\nu}p^\mu$ (raising $p$). Since $\omega_{\mu\nu}$ is antisymmetric, contracting it with $x^\nu p^\mu$ picks out only the antisymmetric part of $x^\nu p^\mu$ in the indices $\mu, \nu$:
> $$\omega_{\mu\nu}x^\nu p^\mu = \frac12\omega_{\mu\nu}(x^\nu p^\mu - x^\mu p^\nu) = -\frac12\omega_{\mu\nu}(x^\mu p^\nu - x^\nu p^\mu) = -\frac12\omega_{\mu\nu}J^{\mu\nu},$$
> where $J^{\mu\nu} := x^\mu p^\nu - x^\nu p^\mu$ is the **angular-momentum four-tensor** ([[Def - Angular Momentum Four-Tensor]]). The conservation $-\tfrac12\omega_{\mu\nu}J^{\mu\nu} = \text{const}$ holds for *every* antisymmetric $\omega$; choosing the six independent antisymmetric generators in turn shows each component $J^{\mu\nu}$ is separately conserved:
> $$J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu = \text{const along the worldline}.$$

**Step 3: Rotations give angular momentum, boosts give the centre-of-inertia law.**

> [!note]- Derivation
> The six conserved components of $J^{\mu\nu}$ split by the index structure.
> *Spatial components (rotations):* $J^{ij} = x^i p^j - x^j p^i$ is the ordinary angular momentum; in three-vector form $\mathbf{L} = \mathbf{x}\times\mathbf{p}$, with $J^{12} = L^3$, etc. Its conservation is **conservation of angular momentum**, the Noether charge of spatial rotations.
> *Mixed components (boosts):* $J^{i0} = x^i p^0 - x^0 p^i = E\,x^i - t\,P^i$, using $p^0 = E$ and $x^0 = t$. Its conservation reads $E x^i - t P^i = \text{const}$. Since the energy $E = p^0$ is itself conserved (from translation invariance, [[Ex - Four-momentum conservation from translation invariance]]), divide by $E$:
> $$x^i - \frac{P^i}{E}\,t = \text{const}.$$
> This says the spatial position $x^i$ moves linearly in time at the constant velocity $P^i/E$ — the **centre-of-inertia theorem**: the centre of inertia (here, the single particle) moves uniformly in a straight line. For a free particle this is just uniform rectilinear motion; for a system of particles, $J^{i0}$ tracks the centre of mass, and its conservation is the relativistic statement that the centre of mass moves at constant velocity.

**Step 4: Direct verification and physical interpretation.**

> [!note]- Derivation
> Differentiate $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$ along the worldline:
> $$\frac{dJ^{\mu\nu}}{d\tau} = \dot x^\mu p^\nu + x^\mu\dot p^\nu - \dot x^\nu p^\mu - x^\nu\dot p^\mu.$$
> On the free worldline, $\dot p^\nu = 0$ (four-momentum conserved), killing the $x\dot p$ terms. And $\dot x^\mu = U^\mu = p^\mu/m$ (proper-time parametrisation, $p^\mu = mU^\mu$), so
> $$\dot x^\mu p^\nu - \dot x^\nu p^\mu = \frac{1}{m}(p^\mu p^\nu - p^\nu p^\mu) = 0.$$
> Hence $dJ^{\mu\nu}/d\tau = 0$: the angular-momentum tensor is conserved, confirming the Noether result.
> *Physical interpretation of the boost charge.* Why does boost invariance — the statement that all inertial frames are equivalent, a claim about *observers* — produce a *dynamical* law about the centre of mass? Because boost invariance includes the equivalence of the centre-of-momentum frame with every other. In the centre-of-momentum frame the total spatial momentum vanishes, so the centre of inertia is at rest (or moves trivially); the statement "this frame is as valid as any" then says, boosted to an arbitrary frame, that the centre of inertia moves uniformly at the velocity of the boost. The conserved quantity $J^{i0} = E x^i - t P^i$ encodes exactly this: it is the (energy-weighted) position of the centre of inertia at $t = 0$, and its constancy is the relativistic centre-of-mass theorem. Boost invariance is the relativistic replacement for the Galilean boost invariance that, in Newtonian mechanics, gives the uniform motion of the centre of mass.

> [!note]- Complete formal solution
> An infinitesimal Lorentz transformation $x'^\mu = (\delta^\mu_{\;\nu} + \omega^\mu_{\;\nu})x^\nu$ has generator $G^\mu = \omega^\mu_{\;\nu}x^\nu$ with $\omega_{\mu\nu}$ antisymmetric (from $\Lambda^{\mathsf T}\eta\Lambda = \eta$ at first order), and leaves $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ invariant (Lorentz transformations preserve the norm). By [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]], $p_\mu G^\mu = \omega_{\mu\nu}x^\nu p^\mu = -\tfrac12\omega_{\mu\nu}J^{\mu\nu} = \text{const}$ for all antisymmetric $\omega$, where $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$; hence $J^{\mu\nu} = \text{const}$. The spatial part $J^{ij} = \mathbf{x}\times\mathbf{p}$ is conserved angular momentum (rotations); the mixed part $J^{i0} = E x^i - t P^i$ gives, on dividing by the conserved $E$, the centre-of-inertia law $x^i - (P^i/E)t = \text{const}$ (boosts). Direct check: $dJ^{\mu\nu}/d\tau = 0$ because $\dot p = 0$ and $\dot x^\mu p^\nu - \dot x^\nu p^\mu \propto p^\mu p^\nu - p^\nu p^\mu = 0$. Boost invariance produces the centre-of-mass theorem because the centre-of-momentum frame is equivalent to all others. $\blacksquare$

---

# Key Takeaways

**The angular-momentum tensor unifies rotations and boosts because the Lorentz group unifies them.** The six conserved Noether charges of Lorentz invariance fill out a single antisymmetric tensor $J^{\mu\nu}$, whose spatial part is ordinary angular momentum (the rotation charges) and whose mixed part is the centre-of-inertia moment (the boost charges). This packaging is forced by the structure of the [[Def - The Poincaré Group|Lorentz group]]: rotations and boosts are not separate symmetries but the spatial and mixed components of a single antisymmetric generator $\omega_{\mu\nu}$, and Noether's theorem maps that unification onto the conserved quantities. The reusable insight is that a continuous symmetry valued in an antisymmetric Lie algebra (like $\mathfrak{so}(1,3)$) produces a conserved *antisymmetric tensor*, not a collection of scalars — the index structure of the conserved charge mirrors the index structure of the symmetry generator. The trigger: when the generator is $G^\mu = \omega^\mu_{\;\nu}x^\nu$ with $\omega$ antisymmetric, expect a conserved antisymmetric tensor $J^{\mu\nu}$, and read off its physical pieces by decomposing $\omega$ into its irreducible parts (here rotations and boosts).

**Boost invariance is a dynamical statement: the centre of mass moves uniformly.** The most surprising result of this exercise is that boost invariance — which sounds like a passive statement about the equivalence of observers — produces an active conservation law, the uniform motion of the centre of inertia, $x^i - (P^i/E)t = \text{const}$. The resolution is that the equivalence of frames includes the equivalence of the centre-of-momentum frame, in which the centre of mass is at rest; boosting this to an arbitrary frame gives uniform centre-of-mass motion. This is the relativistic generalisation of the Newtonian centre-of-mass theorem, which follows from Galilean boost invariance. The reusable principle: a symmetry that mixes time and space (a boost) constrains how the system's "position" evolves in time, producing a law about centre-of-mass motion; this is why the full Poincaré group, not just rotations and translations, is needed to capture all conservation laws of an isolated system. The boost charge $J^{i0}$ is the often-forgotten member of the conserved set, but it is on exactly the same footing as energy, momentum, and angular momentum.

**Antisymmetry of the generator projects out the antisymmetric conserved tensor — a recurring contraction trick.** The technical heart of the derivation is that contracting the antisymmetric $\omega_{\mu\nu}$ with $x^\nu p^\mu$ keeps only the antisymmetric part of the latter, $-\tfrac12 J^{\mu\nu}$, because the contraction of an antisymmetric tensor with the symmetric part of anything vanishes. This is the same identity that made the Lorentz force pure ([[Ex - The Lorentz force from minimal coupling]]) — antisymmetric contracted with symmetric is zero — used in reverse to *extract* an antisymmetric object. The reusable trick: when a conserved charge is the contraction of an antisymmetric symmetry generator with some bilinear in positions and momenta, only the antisymmetric part of that bilinear is physical, and it is automatically a conserved antisymmetric tensor. Recognising which part of a contraction survives, based on the symmetry of the contracting tensor, is a constantly useful manoeuvre in relativistic computations. For the translation charges (four-momentum) see [[Ex - Four-momentum conservation from translation invariance]], and for the full ten-fold Poincaré story summarised see [[Thm - Noether Theorem (Relativistic Particle)]].
