---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Geodesic"
  - "Def - Length and Energy Functionals"
  - "Def - Hamiltonian Flow of the Kinetic Energy"
  - "Thm - First Variation of Arc Length"
tags: [geometry, riemannian-geometry, variational-calculus, hamiltonian-mechanics, lagrangian]
---

# Notation

$(M, g)$ a Riemannian manifold with local coordinates $(q^1, \ldots, q^n)$ and induced coordinates $(q^i, \dot q^i)$ on $TM$ or $(q^i, p_i)$ on $T^*M$. The kinetic-energy Lagrangian is $L(q, \dot q) = \tfrac12 g_{ij}(q) \dot q^i \dot q^j$. The kinetic-energy Hamiltonian is $H(q, p) = \tfrac12 g^{ij}(q) p_i p_j$. The Legendre transform is $p_i = \partial L/\partial \dot q^i = g_{ij}\dot q^j$. Christoffel symbols of $g$ are $\Gamma^k_{ij}$. Full registry on [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].

---

# Statement

> **Theorem (Hamilton's Principle Gives the Geodesic Equation).** Let $(M, g)$ be a Riemannian manifold. For a smooth curve $\gamma : [a, b] \to M$ with fixed endpoints, the following are equivalent:
>
> (i) $\gamma$ is a critical point of the energy $E(\gamma) = \tfrac12 \int_a^b g(\dot\gamma, \dot\gamma)\, dt$ with respect to all fixed-endpoint smooth variations.
>
> (ii) $\gamma$ satisfies the Euler–Lagrange equations of the Lagrangian $L(q, \dot q) = \tfrac12 g_{ij}\dot q^i \dot q^j$ on $TM$:
> $$\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = \frac{\partial L}{\partial q^k}, \qquad k = 1, \ldots, n.$$
>
> (iii) $\gamma$ is a [[Def - Geodesic|geodesic]] of $g$, i.e. $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i \dot\gamma^j = 0$.
>
> (iv) The lifted curve $(q^i(t), p_i(t)) \in T^*M$ with $p_i(t) = g_{ij}(q(t))\dot q^j(t)$ satisfies Hamilton's equations of the Hamiltonian $H(q, p) = \tfrac12 g^{ij} p_i p_j$:
> $$\dot q^i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q^i}.$$

> **Corollary.** Free-particle Newtonian mechanics on a Riemannian manifold (no external forces) is exactly geodesic flow.

---

# Motivation

This theorem is the formal bridge between three different formulations of the same dynamical system:

- **Geometric:** [[Def - Geodesic|geodesics]], defined by $\nabla_{\dot\gamma}\dot\gamma = 0$ — the covariant-acceleration formulation.
- **Lagrangian:** trajectories of a particle with Lagrangian $L = T$, derived via Hamilton's principle.
- **Hamiltonian:** flow of the Hamiltonian $H = \tfrac12 |p|^2_{g^{-1}}$ on the symplectic manifold $T^*M$.

These are not three different theories — they are three views of *the same* dynamical system. The theorem says: the variational principle, the Lagrangian formalism, the Hamiltonian formalism, and the connection-based geodesic equation all describe the same curves on $M$.

Why does this matter? Three reasons.

First, **it explains "why" the geodesic equation is the right physics**: it is the equation of motion of a free particle. In curved space (or curved time), a free particle moves along a geodesic. This is the kinematic content of general relativity (Einstein's equivalence principle), and the precise statement is the equivalence in this theorem applied in Lorentzian signature.

Second, **it makes the entire machinery of classical mechanics available for Riemannian geometry**: action–angle coordinates, KAM theory, the variational principle of minimum action, Noether's theorem for conservation laws, Poisson brackets, symplectic reduction. Conversely, the Riemannian-geometric tools (curvature, comparison geometry, the Bonnet–Myers bound) become applicable to all conservative mechanical systems via Jacobi's principle.

Third, **it makes precise the duality between $TM$ and $T^*M$**, the velocity and momentum formulations. The Legendre transform $\dot q \mapsto p$ is a [[Def - Diffeomorphism|diffeomorphism]] (and a *symplectic* map in an appropriate sense), and the choice between formulations is just the choice of which variables are more convenient. For the kinetic-energy Lagrangian/Hamiltonian, the Hamiltonian on $T^*M$ has a particularly clean form ($\tfrac12 g^{ij}p_i p_j$), so the cotangent-bundle formulation is preferred for symplectic-geometry analyses; the tangent-bundle formulation is preferred for variational derivations.

The equivalence (i) ⟺ (ii) is the standard calculus-of-variations result: critical points of a Lagrangian action are solutions of the Euler–Lagrange equations. The equivalence (ii) ⟺ (iii) is the *content* of the theorem: computing the Euler–Lagrange equations of $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ produces the geodesic equation. The equivalence (iii) ⟺ (iv) is the Legendre transform: converting from velocity formulation $(q, \dot q)$ on $TM$ to momentum formulation $(q, p)$ on $T^*M$, with $H = p\dot q - L$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a smooth curve on a Riemannian manifold. Sources are problems where one wants to translate between geometric and mechanical formulations.

The most common source is **a classical mechanics problem on a curved configuration space**. Pendula on spheres, particles on tori, Foucault pendula on the rotating Earth — all have configuration manifolds with nontrivial geometry. The Lagrangian or Hamiltonian formulation translates the problem into the geometric language, where the Euler–Lagrange (resp. Hamilton's) equations become the geodesic equation. Bridge: "particle on $M$ with kinetic energy $\tfrac12 g_{ij}\dot q^i \dot q^j$" $\Leftrightarrow$ "geodesic of $(M, g)$".

A subtler source is **a problem with a potential**. A particle with Lagrangian $L = T - V$ on $(M, g)$ does *not* directly become a geodesic problem — but by [[Ex - Pendulum as a Geodesic in a Conformally Modified Metric (Jacobi)|Jacobi's principle]], at fixed total energy $E$, the trajectories are geodesics of the rescaled Jacobi metric $\tilde g = 2(E - V) g$. Bridge: "particle with Lagrangian $T - V$ at energy $E$" $\Leftrightarrow$ "geodesic of $2(E-V)g$".

A third source is **a problem involving symmetry and conservation laws**. Continuous isometries of $g$ are Killing fields; by Noether's theorem applied to the variational principle, each Killing field gives a conserved quantity along geodesic flow (specifically $g(\dot\gamma, X)$). Bridge: "geodesic flow preserves the metric symmetries" — and by the theorem, this gives conservation laws for the Hamiltonian flow on $T^*M$.

**Targets (Output Amplification)**

The conclusions are the four equivalences. Targets are the constructions and theorems that use them.

The most important combination is **theorem + the Hamiltonian formulation on $T^*M$ ⟹ the symplectic structure of geodesic flow**. Geodesic flow lifts to a Hamiltonian flow on $T^*M$, preserving the canonical symplectic form $\omega = dq^i \wedge dp_i$. By Liouville's theorem, it preserves the symplectic volume; on a compact manifold this gives a natural invariant measure for the flow, the precondition for ergodic theory. See [[Def - Hamiltonian Flow of the Kinetic Energy]].

A second combination is **theorem + a continuous symmetry ⟹ Noether's theorem**. A one-parameter family of isometries of $(M, g)$ corresponds (via the variational principle) to a one-parameter family of length-preserving curve-variations, which by Noether produces a conserved quantity. Explicitly: a Killing field $X$ gives the conserved $g(\dot\gamma, X)$, equivalently $X^i p_i$ in the cotangent-bundle picture, equivalently the moment of the Killing-field action.

A third combination is **theorem + Jacobi's principle ⟹ classical mechanics ≡ Riemannian geometry**. Combining the energy-only formulation (geodesics of $g$) with the potential formulation (geodesics of the Jacobi metric) shows that *every* conservative mechanical system is a geodesic problem in some metric. So classical mechanics on configuration manifolds is *exactly* Riemannian geometry, and tools from one transfer freely to the other.

A fourth combination is **theorem + Lorentzian signature ⟹ the equation of motion in general relativity**. In a Lorentzian spacetime $(M, g)$, the free-particle Lagrangian for a massive particle is $L = -m\sqrt{-g_{ij}\dot q^i \dot q^j}$ (proportional to proper time). Hamilton's principle then gives the geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ as the equation of motion. So free-fall in GR = timelike geodesic flow = Hamiltonian flow of $H = \tfrac12 g^{ij}p_i p_j$ in the cotangent bundle of spacetime. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Why Is It True

**Mechanism summary:** **the Euler–Lagrange equation of $L = \tfrac12 g_{ij}\dot q^i \dot q^j$ unfolds to $\ddot q^k + \Gamma^k_{ij}\dot q^i \dot q^j = 0$ after a chain-rule computation; the Legendre transform $p_i = g_{ij}\dot q^j$ converts this to the Hamiltonian system on $T^*M$ with $H = \tfrac12 g^{ij}p_i p_j$ — and Hamilton's equations $\dot q^i = \partial H/\partial p_i, \dot p_i = -\partial H/\partial q^i$ are equivalent to the Euler–Lagrange equations by the standard duality.**

(i) ⟺ (ii) is the standard calculus-of-variations result. Given the variational integral $S(\gamma) = \int L(\gamma, \dot\gamma)\, dt$ with fixed endpoints, the first variation is
$$\delta S = \int \frac{\partial L}{\partial q^k}\delta q^k + \frac{\partial L}{\partial \dot q^k}\delta \dot q^k\, dt = \int \left(\frac{\partial L}{\partial q^k} - \frac{d}{dt}\frac{\partial L}{\partial \dot q^k}\right)\delta q^k\, dt$$
after integration by parts. Vanishing for all $\delta q$ with $\delta q(a) = \delta q(b) = 0$ gives the Euler–Lagrange equations by the fundamental lemma. This is the abstract version of the [[Thm - First Variation of Arc Length|first variation of arc length]] argument.

(ii) ⟺ (iii) is the *content* of the theorem. Compute the Euler–Lagrange equations for $L = \tfrac12 g_{ij}\dot q^i \dot q^j$:
- $\frac{\partial L}{\partial \dot q^k} = g_{kj}\dot q^j$, so $\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = \frac{\partial g_{kj}}{\partial q^l}\dot q^l \dot q^j + g_{kj}\ddot q^j$.
- $\frac{\partial L}{\partial q^k} = \tfrac12 \frac{\partial g_{ij}}{\partial q^k}\dot q^i \dot q^j$.

Setting these equal:
$$g_{kj}\ddot q^j + \frac{\partial g_{kj}}{\partial q^l}\dot q^l \dot q^j - \tfrac12 \frac{\partial g_{ij}}{\partial q^k}\dot q^i \dot q^j = 0.$$
Symmetrising the second term (which has $j, l$ as dummy indices, so we can write it as $\tfrac12 (\partial_l g_{kj} + \partial_j g_{kl})\dot q^l \dot q^j$):
$$g_{kj}\ddot q^j + \tfrac12 (\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj})\dot q^l \dot q^j = 0.$$
Recognising the Christoffel symbol formula: $\Gamma^m_{lj} = \tfrac12 g^{mk}(\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj})$. So multiplying by $g^{mk}$ and renaming:
$$\ddot q^m + \Gamma^m_{lj}\dot q^l \dot q^j = 0,$$
the geodesic equation. The Christoffel-symbol formula is what makes the Euler–Lagrange equations of $\tfrac12 g_{ij}\dot q^i \dot q^j$ coincide with the geodesic equation. This is a small miracle: the calculus-of-variations machinery, applied to the kinetic energy of a free particle, exactly reproduces the geodesic equation of the metric.

(iii) ⟺ (iv) is the Legendre transform. Define $p_i := \partial L/\partial \dot q^i = g_{ij}\dot q^j$, which is invertible to $\dot q^j = g^{ji}p_i$. The Hamiltonian is $H := p_i \dot q^i - L$, with the $\dot q$ now expressed in terms of $p$:
$$H = p_i g^{ij}p_j - \tfrac12 g_{ij} g^{ik}p_k g^{jl}p_l = g^{ij}p_i p_j - \tfrac12 \delta^i_k g^{jl}p_i p_l = g^{ij}p_i p_j - \tfrac12 g^{il}p_i p_l = \tfrac12 g^{ij}p_i p_j.$$
Hamilton's equations $\dot q^i = \partial H/\partial p_i = g^{ij}p_j$ and $\dot p_i = -\partial H/\partial q^i = -\tfrac12 (\partial_i g^{jk})p_j p_k$ are equivalent to the Euler–Lagrange equations by the standard Lagrange-Hamilton duality.

The result is that **all four formulations describe the same curves**, justifying the use of any one as a starting point for analysis.

---

# What Makes This Hard

The conceptual difficulty is **the Christoffel-symbol identity** in the Euler–Lagrange computation. Computing $\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} - \frac{\partial L}{\partial q^k}$ for $L = \tfrac12 g_{ij}\dot q^i \dot q^j$ produces a combination of metric-derivative terms that exactly assembles into the Christoffel symbol $\Gamma^k_{ij} = \tfrac12 g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. This is not obvious until you actually do the computation — the symmetrisation pattern is *exactly* the one in the Christoffel formula.

The technical difficulty is the **Legendre transform** for general Lagrangians. The transform $\dot q \mapsto p$ requires the Lagrangian to be *convex* in $\dot q$ (so $p$ is uniquely determined), which is automatic for the kinetic-energy Lagrangian (positive-definite metric) but not for arbitrary Lagrangians.

The most common error is to **forget the symmetrisation of indices** in the Euler–Lagrange computation. The middle term $\partial g_{kj}/\partial q^l \cdot \dot q^l \dot q^j$ has $j$ and $l$ as dummy indices, so we can symmetrise it to $\tfrac12 (\partial_l g_{kj} + \partial_j g_{kl})$. Without this symmetrisation, the Christoffel pattern doesn't emerge cleanly.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute the Euler–Lagrange equations of $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ directly. Use the symmetrisation of dummy indices to recognise the Christoffel-symbol pattern. Apply the Legendre transform to get the Hamiltonian formulation; verify Hamilton's equations are equivalent.

**Subgoal decomposition:**

1. **Compute $\partial L/\partial \dot q^k$ and its $t$-derivative.** $\partial L/\partial \dot q^k = g_{kj}\dot q^j$. $\frac{d}{dt} = \partial_l g_{kj}\dot q^l \dot q^j + g_{kj}\ddot q^j$.
   - *Hint:* chain rule on $g_{kj}(q(t))$.
   - *Why needed:* one side of Euler–Lagrange.

2. **Compute $\partial L/\partial q^k = \tfrac12 \partial_k g_{ij}\dot q^i \dot q^j$.**
   - *Hint:* direct partial differentiation.
   - *Why needed:* other side of Euler–Lagrange.

3. **Combine and symmetrise.** Set them equal and rewrite the middle term using $\partial_l g_{kj}\dot q^l\dot q^j = \tfrac12 (\partial_l g_{kj} + \partial_j g_{kl})\dot q^l \dot q^j$ (by relabelling dummy indices).
   - *Hint:* the trick is recognising that the middle term is symmetric in $(l, j)$ as a quadratic form in $\dot q$.
   - *Why needed:* prepares for Christoffel recognition.

4. **Recognise the Christoffel symbol.** The combined equation $g_{kj}\ddot q^j + \tfrac12(\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj})\dot q^l\dot q^j = 0$ becomes, after multiplying by $g^{mk}$, $\ddot q^m + \Gamma^m_{lj}\dot q^l\dot q^j = 0$ — the geodesic equation.
   - *Hint:* compare with $\Gamma^m_{lj} = \tfrac12 g^{mk}(\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj})$.
   - *Why needed:* establishes (ii) ⟺ (iii).

5. **Apply Legendre transform.** $p_i = \partial L/\partial \dot q^i = g_{ij}\dot q^j$, $H = p\dot q - L = \tfrac12 g^{ij}p_i p_j$.
   - *Hint:* compute $H$ in terms of $p$ by inverting the Legendre.
   - *Why needed:* gets the Hamiltonian formulation.

6. **Verify Hamilton's equations are equivalent.** $\dot q^i = g^{ij}p_j$ (consistent with $p = g \dot q$); $\dot p_i = -\partial H/\partial q^i$ (compute and check equivalent to the geodesic equation).
   - *Hint:* substitute and check the two sides of Hamilton's equations both reduce to the geodesic equation.
   - *Why needed:* establishes (iii) ⟺ (iv).

---

# Lemma Decomposition

> [!note]- Lemma 1: Euler–Lagrange equations of $L = \tfrac12 g_{ij}\dot q^i \dot q^j$ give the geodesic equation
> **Statement:** $\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} - \frac{\partial L}{\partial q^k} = 0$ for $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ is equivalent to $\ddot q^k + \Gamma^k_{ij}\dot q^i \dot q^j = 0$.
>
> **Hint:** Compute, symmetrise the dummy indices, recognise the Christoffel pattern.
>
> **Why needed:** Direct identification of the calculus-of-variations equation with the geodesic equation.
>
> > [!note]- Full proof
> > $\partial L/\partial \dot q^k = g_{kj}\dot q^j$ (using $\partial(\dot q^i\dot q^j)/\partial \dot q^k = \delta^i_k \dot q^j + \dot q^i \delta^j_k = 2\dot q^k$, and the factor of $\tfrac12 g_{ij}$ becomes $g_{kj}\dot q^j$ after combining).
> >
> > $\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = \frac{d}{dt}(g_{kj}\dot q^j) = (\partial_l g_{kj})\dot q^l \dot q^j + g_{kj}\ddot q^j$.
> >
> > $\partial L/\partial q^k = \tfrac12 (\partial_k g_{ij})\dot q^i \dot q^j$.
> >
> > Euler–Lagrange:
> > $$g_{kj}\ddot q^j + (\partial_l g_{kj})\dot q^l\dot q^j - \tfrac12 (\partial_k g_{ij})\dot q^i\dot q^j = 0.$$
> > Symmetrising the middle term ($\dot q^l\dot q^j$ is symmetric in $(l, j)$, so we can replace $\partial_l g_{kj}$ by $\tfrac12 (\partial_l g_{kj} + \partial_j g_{kl})$):
> > $$g_{kj}\ddot q^j + \tfrac12 (\partial_l g_{kj} + \partial_j g_{kl})\dot q^l\dot q^j - \tfrac12 (\partial_k g_{ij})\dot q^i\dot q^j = 0.$$
> > Renaming dummy indices on the last term ($i \to l, j \to j$):
> > $$g_{kj}\ddot q^j + \tfrac12 (\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj})\dot q^l\dot q^j = 0.$$
> > Multiply by $g^{mk}$ and use $g^{mk}g_{kj} = \delta^m_j$ on the first term, and the Christoffel formula $\Gamma^m_{lj} = \tfrac12 g^{mk}(\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj})$ on the second:
> > $$\ddot q^m + \Gamma^m_{lj}\dot q^l\dot q^j = 0,$$
> > the geodesic equation.

> [!note]- Lemma 2: Legendre transform gives $H = \tfrac12 g^{ij}p_i p_j$
> **Statement:** The Legendre transform of $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ is $H = \tfrac12 g^{ij}p_i p_j$, with $p_i = g_{ij}\dot q^j$ and the inverse relation $\dot q^j = g^{ji}p_i$.
>
> **Hint:** Compute $H = p\dot q - L$ with $\dot q$ expressed in terms of $p$.
>
> **Why needed:** Establishes the Hamiltonian formulation.
>
> > [!note]- Full proof
> > $p_i = \partial L/\partial \dot q^i = g_{ij}\dot q^j$ (Lemma 1). Invert: $\dot q^j = g^{ji}p_i$ (using $g^{ji}g_{ik} = \delta^j_k$).
> >
> > $H = p_i \dot q^i - L = p_i g^{ij}p_j - \tfrac12 g_{ij}\dot q^i \dot q^j = g^{ij}p_i p_j - \tfrac12 g_{ij}(g^{ik}p_k)(g^{jl}p_l)$.
> >
> > Simplify the second term: $g_{ij}g^{ik}g^{jl} = \delta^k_j g^{jl} = g^{kl}$. So
> > $$H = g^{ij}p_i p_j - \tfrac12 g^{kl}p_k p_l = \tfrac12 g^{ij}p_i p_j.$$

> [!note]- Lemma 3: Hamilton's equations of $H = \tfrac12 g^{ij}p_i p_j$ are equivalent to the geodesic equation
> **Statement:** The Hamilton equations $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$ for $H = \tfrac12 g^{ij}p_i p_j$ are equivalent (via $p_i = g_{ij}\dot q^j$) to the geodesic equation $\ddot q^k + \Gamma^k_{ij}\dot q^i\dot q^j = 0$.
>
> **Hint:** Compute $\dot q^i = g^{ij}p_j$ (gives Legendre transform back); compute $\dot p_i = -\tfrac12 (\partial_i g^{jk})p_j p_k$, substitute $p = g\dot q$, simplify using the identity $\partial_i(g^{jk})g_{km}g_{jl} = -\partial_i g_{lm}$.
>
> **Why needed:** Establishes (iii) ⟺ (iv).
>
> > [!note]- Full proof (sketch)
> > $\dot q^i = \partial H/\partial p_i = g^{ij}p_j$ — this is the Legendre transform inverted.
> >
> > $\dot p_i = -\partial H/\partial q^i = -\tfrac12 (\partial_i g^{jk})p_j p_k$. Substituting $p_j = g_{jl}\dot q^l, p_k = g_{km}\dot q^m$:
> > $$\dot p_i = -\tfrac12 (\partial_i g^{jk}) g_{jl}g_{km}\dot q^l \dot q^m.$$
> > Using the identity $g^{jk}g_{km} = \delta^j_m$, differentiate both sides: $\partial_i g^{jk} \cdot g_{km} + g^{jk}\partial_i g_{km} = 0$, so $\partial_i g^{jk} \cdot g_{km} = -g^{jk}\partial_i g_{km}$. Multiply by $g_{jl}$: $(\partial_i g^{jk}) g_{jl} g_{km} = -g^{jk}g_{jl}\partial_i g_{km} = -\delta^k_l \partial_i g_{km} = -\partial_i g_{lm}$. So
> > $$\dot p_i = \tfrac12 (\partial_i g_{lm})\dot q^l \dot q^m.$$
> > Now also compute $\dot p_i$ as the $t$-derivative of $g_{ij}\dot q^j$:
> > $$\dot p_i = \frac{d}{dt}(g_{ij}\dot q^j) = (\partial_l g_{ij})\dot q^l \dot q^j + g_{ij}\ddot q^j.$$
> > Equating the two expressions:
> > $$g_{ij}\ddot q^j + (\partial_l g_{ij})\dot q^l\dot q^j = \tfrac12 (\partial_i g_{lm})\dot q^l\dot q^m,$$
> > which after symmetrisation of dummy indices is the equation derived in Lemma 1's proof, equivalent to the geodesic equation.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** A smooth curve $\gamma : [a, b] \to M$ with fixed endpoints is a critical point of $E$ iff it satisfies the Euler–Lagrange equations of $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ iff it is a geodesic of $g$ iff its lift to $T^*M$ satisfies Hamilton's equations of $H = \tfrac12 g^{ij}p_i p_j$.
>
> *Proof.* (i) ⟺ (ii): standard fundamental result of the calculus of variations, applied to the Lagrangian $L$. (Already established as the [[Thm - First Variation of Arc Length|first variation of energy]] applied to the energy functional.)
>
> (ii) ⟺ (iii): Lemma 1.
>
> (iii) ⟺ (iv): Lemma 2 establishes the form of $H$; Lemma 3 establishes the equivalence of Hamilton's equations with the geodesic equation.
>
> So all four conditions are equivalent. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Classical mechanics: the Kepler problem.** The Kepler problem (motion of a particle in a $1/r$ gravitational potential) is a classical mechanics problem with Lagrangian $L = \tfrac12 |\dot{\mathbf q}|^2 + k/|\mathbf q|$. By Jacobi's principle and Hamilton's principle, the bound orbits at fixed negative energy $E < 0$ become geodesics of the Jacobi metric $\tilde g = 2(E + k/r) \delta$ on the appropriate annular region. The integrability of Kepler (closed orbits = ellipses, the Runge–Lenz vector) is then a geometric statement about this specific metric.

**Quantum mechanics: the Schrödinger equation on a Riemannian manifold.** The classical Hamiltonian $H = \tfrac12 g^{ij}p_i p_j$ becomes the quantum operator $-\tfrac{1}{2}\Delta_g$ (the Laplace-Beltrami operator). The Schrödinger equation $i\partial_t \psi = -\tfrac12 \Delta_g \psi$ on $(M, g)$ describes a free quantum particle on the manifold. The semiclassical limit recovers classical geodesic flow (Egorov's theorem), and the spectrum of $\Delta_g$ encodes geometric information (the Weyl law, the heat-kernel expansion, the trace formula).

**Optics: Fermat's principle.** Light rays in an inhomogeneous medium with index of refraction $n(\mathbf x)$ follow paths extremising the optical length $\int n\, ds$. Treating $n^2 \delta_{ij}$ as a Riemannian metric, the optical paths are *geodesics* of this conformally rescaled metric. Snell's law (refraction at interfaces) and the equations of geometric optics fall out by direct application of Hamilton's principle.

**General relativity: free-fall as timelike geodesic.** In a Lorentzian spacetime, free-falling massive particles follow timelike geodesics maximising proper time $\tau = \int \sqrt{-g_{ij}\dot q^i \dot q^j}\, dt$. By an analogous Hamilton-principle argument (in Lorentzian signature, signs flip and the extremum is a maximum, not a minimum), the geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ is the equation of motion. The Hamiltonian on the cotangent bundle of spacetime is $H = \tfrac12 g^{\mu\nu}p_\mu p_\nu$, with conserved $H = -m^2/2$ for massive particles ($-1/2$ for unit mass) and $H = 0$ for light. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Def - Geodesic|Geodesic]]** — the geometric formulation. The geodesic equation $\nabla_{\dot\gamma}\dot\gamma = 0$ is the kinematic content, and the theorem says it is the Euler–Lagrange equation of the kinetic-energy Lagrangian.

- **[[Def - Length and Energy Functionals|Length and Energy Functionals]]** — the variational principle. The energy $E(\gamma) = \tfrac12 \int |\dot\gamma|^2\, dt$ is the action of the free particle, and its critical points are geodesics. The length $L$ is the *image*-based version; both have the same critical points after the constant-speed parametrisation.

- **[[Def - Hamiltonian Flow of the Kinetic Energy|Hamiltonian Flow of the Kinetic Energy]]** — the cotangent-bundle formulation. The Hamiltonian $H = \tfrac12 g^{ij}p_i p_j$ on $T^*M$ generates geodesic flow, and the entire symplectic-geometry apparatus (Liouville's theorem, Poisson brackets, action–angle) is available.

- **[[Thm - First Variation of Arc Length|First Variation of Arc Length]]** — the source. The theorem is essentially the same as the first variation of energy, lifted to a Lagrangian-mechanics framework. The Euler–Lagrange equations *are* the equations derived from the first-variation analysis.

- **Jacobi's Principle** — the extension to systems with potentials. A Lagrangian $L = T - V$ at fixed energy $E$ gives trajectories that are geodesics of the **Jacobi metric** $\tilde g = 2(E - V)g$ — see [[Ex - Pendulum as a Geodesic in a Conformally Modified Metric (Jacobi)]]. This extends Hamilton's principle from pure-kinetic to potential-augmented systems.

---

# Unlocked by This

> [!tip] Symplectic Geometry of Geodesic Flow *(from Geometric Mechanics)*
> The Hamiltonian formulation lifts geodesic flow into the world of symplectic geometry on $T^*M$, where Liouville's theorem, Poisson brackets, action–angle coordinates, and the entire integrability theory apply. The geodesic flow becomes one example among many of a Hamiltonian dynamical system, and the general framework is developed in [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

> [!tip] **Noether's Theorem for Geodesic Flow** *(from Geometric Mechanics)*
> Every continuous symmetry of the Lagrangian $L = \tfrac12 g_{ij}\dot q^i\dot q^j$ — equivalently, every isometry of $(M, g)$ — gives a conserved quantity along geodesics. For a Killing field $X$, the conserved quantity is $g(\dot\gamma, X) = p_i X^i$ in the Lagrangian/Hamiltonian formulation. This is the source of conservation of angular momentum on rotation-symmetric manifolds, conservation of energy in time-independent Hamiltonians, and all conservation laws in classical mechanics arising from geometric symmetries.

> [!tip] **Jacobi's Principle of Least Action** *(from Geometric Mechanics)*
> Extending Hamilton's principle from purely-kinetic to potential-augmented systems: a particle with Lagrangian $L = T - V$ at fixed energy $E$ traces a geodesic of the **Jacobi metric** $\tilde g = 2(E - V) g$ on the classically-allowed region $\{V < E\}$. This converts *every* conservative mechanical system into a geodesic problem in some metric. See [[Ex - Pendulum as a Geodesic in a Conformally Modified Metric (Jacobi)]].
