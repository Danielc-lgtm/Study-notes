---
type: theorem
subject: geometric-mechanics
prereqs:
  - "Def - The Lagrangian Function"
  - "Def - Hamiltonian Function"
  - "Def - The Legendre Transform"
  - "Thm - Hamilton's Principle in TQ Gives Euler-Lagrange Equations"
tags: [physics, geometric-mechanics, lagrangian-mechanics, hamiltonian-mechanics]
---

# Notation

$Q$ is a smooth manifold of dimension $n$ (configuration space). $TQ$ and $T^*Q$ are the tangent and cotangent bundles. $L : TQ \times \mathbb{R} \to \mathbb{R}$ is a smooth Lagrangian; $H : T^*Q \times \mathbb{R} \to \mathbb{R}$ is the associated Hamiltonian via the Legendre transform. $\mathbb{F}L : TQ \to T^*Q$ is the Legendre transform $(q, \dot q) \mapsto (q, \partial L/\partial \dot q)$. In coordinates $(q^i, \dot q^i)$ on $TQ$ and $(q^i, p_i)$ on $T^*Q$.

---

# Statement

> **Theorem (equivalence of formalisms).** Let $L : TQ \times \mathbb{R} \to \mathbb{R}$ be a regular Lagrangian and let $H : T^*Q \times \mathbb{R} \to \mathbb{R}$ be the associated Hamiltonian via the Legendre transform: $H(q, p, t) = p_i \dot q^i - L(q, \dot q, t)$, with $\dot q$ expressed in terms of $(q, p)$ via $p_i = \partial L/\partial \dot q^i$.
>
> A curve $\gamma : [a, b] \to Q$ satisfies the **Euler–Lagrange equations**
> $$\frac{\partial L}{\partial q^i} - \frac{d}{dt}\frac{\partial L}{\partial \dot q^i} = 0$$
> if and only if the lifted curve $(\gamma(t), p(t))$ in $T^*Q$, with $p(t) = \partial L/\partial \dot q (\gamma(t), \dot\gamma(t), t)$, satisfies **Hamilton's equations**
> $$\dot q^i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q^i}.$$
>
> Equivalently, the variational principles
> $$\delta\int_a^b L(\gamma, \dot\gamma, t)\, dt = 0 \quad \text{on } TQ \times \mathbb{R}$$
> and
> $$\delta\int_a^b \big(p_i\dot q^i - H(q, p, t)\big)\, dt = 0 \quad \text{on } T^*Q \times \mathbb{R}$$
> have the same stationary trajectories (when the second variational principle is taken with $q$ fixed at the endpoints but $p$ free).

---

# Motivation

This theorem is the **bridge** between the two foundational formulations of classical mechanics: the variational ($TQ$, Hamilton's principle, Euler–Lagrange) and the symplectic ($T^*Q$, Hamilton's equations, symplectic geometry). Without it, the two would be parallel but unconnected formalisms. With it, they are equivalent descriptions of the same dynamics, related by the Legendre transform.

The Lagrangian picture is **natural for**:
- **Constrained systems**: just restrict $L$ to the constraint manifold.
- **Field theory**: $\mathcal{L}$ becomes a density, action is a spacetime integral, manifest Lorentz invariance.
- **Variational symmetries**: Noether's theorem in its cleanest form.
- **Path integrals**: $e^{iS/\hbar}$ in Feynman's quantization.

The Hamiltonian picture is **natural for**:
- **Conservation laws**: Poisson brackets and the algebraic structure of observables.
- **Statistical mechanics**: Liouville's theorem on phase-space volume.
- **Symplectic geometry**: the geometric structure of phase space.
- **Canonical quantization**: $[\hat q, \hat p] = i\hbar$ as a deformation of the Poisson algebra.
- **Integrable systems**: Arnold–Liouville, action-angle variables, KAM theory.

The theorem says you can **freely switch between pictures** depending on which is more convenient. The Legendre transform is the dictionary, and the equivalence is an exact one-to-one correspondence of trajectories. This is one of the most useful conceptual tools in classical mechanics: it lets you exploit the strengths of each formulation as needed.

The conceptual content of the theorem is **dual**: the Lagrangian $L$ on $TQ$ and the Hamiltonian $H$ on $T^*Q$ are **Legendre duals** in the convex-analysis sense, with each containing the same information as the other (when the Lagrangian is regular). The two pictures are not just isomorphic — they are *the same picture viewed from two different sides*, with the Legendre transform providing the precise correspondence.

---

# Sources and Targets

**Sources (Input Broadening).**

The hypothesis is a regular Lagrangian. Several physical setups give regular Lagrangians automatically.

**Source: standard mechanical Lagrangian $L = T - V$.** With $T = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ (positive-definite kinetic energy), the Hessian $\partial^2 L/\partial \dot q^i\partial \dot q^j = g_{ij}$ is invertible, so $L$ is regular. The associated Hamiltonian is $H = T + V$ (total energy). *Example use:* every "ordinary" mechanical system has a regular Lagrangian, and the theorem applies — switching between Lagrangian and Hamiltonian pictures is always available.

**Source: relativistic free particle.** $L = -mc^2\sqrt{1 - |\dot q|^2/c^2}$ is regular when $|\dot q| < c$. The Hessian is computable and invertible. The associated Hamiltonian is $H = \sqrt{|p|^2c^2 + m^2c^4}$ — the relativistic energy.

**Source: geodesic Lagrangian.** $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ is regular when $g$ is nondegenerate. The Hamiltonian is $H = \tfrac{1}{2}g^{ij}p_ip_j$ — the kinetic-energy Hamiltonian whose flow is the geodesic flow.

**Source: a Hamiltonian on $T^*Q$ given directly.** Sometimes the natural starting point is the Hamiltonian (e.g., for systems specified by their conservation laws). If $H$ is "regular" in the dual sense — $\partial^2 H/\partial p_i\partial p_j$ is invertible — then the inverse Legendre transform produces a regular Lagrangian on $TQ$, and the theorem applies.

**Targets (Output Amplification).**

The equivalence has many consequences when combined with other facts.

**Target + Noether's theorem = symplectic moment map from variational symmetry.** A continuous symmetry of $L$ on $TQ$ produces, by variational Noether, a conserved quantity. The Legendre transform maps this to a conserved Hamiltonian function on $T^*Q$, and the symplectic moment map perspective unifies it with the geometry of group actions on $T^*Q$. *Combination use:* derive the moment map for rotational symmetry from the Lagrangian invariance under rotations.

**Target + path integral = Hamiltonian-Lagrangian duality in quantization.** Feynman's path integral $\int e^{iS[\gamma]/\hbar}\mathcal{D}[\gamma]$ over $TQ$-paths can be reformulated as $\int e^{i\int(p\dot q - H)dt/\hbar}\mathcal{D}[(\gamma, p)]$ over $T^*Q$-paths. The equivalence of the two integration measures (after performing the Gaussian integral over momenta) is the variational version of the Legendre transform. *Combination use:* derive canonical-quantization commutators from Feynman's path-integral measure.

**Target + symplectic reduction = constrained Lagrangians.** A Lagrangian on a constrained subspace $S \subset Q$ Legendre-transforms to a Hamiltonian on a Lagrangian submanifold of $T^*Q$, related to the original $T^*S$ by an inclusion. The Hamiltonian reduction by constraints (Dirac–Bergmann) is the Hamiltonian analogue of the Lagrangian constraint analysis. *Combination use:* understand gauge symmetries by Lagrangian or Hamiltonian methods interchangeably.

---

# Why Is It True

**The mechanism in one sentence:** *the Legendre transform converts the Euler–Lagrange equations on $TQ$ into Hamilton's equations on $T^*Q$ by the chain rule, with the Hamiltonian $H = p\dot q - L$ being the convex-analytic dual of the Lagrangian.*

Here is the calculation. Given $H = p_i\dot q^i - L$ with $p_i = \partial L/\partial \dot q^i$, we want to derive Hamilton's equations from the Euler–Lagrange equations.

**Differentiating $H$**. We have $H(q, p, t)$ as a function of $(q, p, t)$, with $\dot q$ an implicit function of $(q, p, t)$ via the Legendre transform. Compute the total differential:
$$dH = \dot q^i\, dp_i + p_i\, d\dot q^i - \frac{\partial L}{\partial q^i}dq^i - \frac{\partial L}{\partial \dot q^i}d\dot q^i - \frac{\partial L}{\partial t}dt.$$

Now use $p_i = \partial L/\partial \dot q^i$ — the $d\dot q^i$ terms cancel:
$$dH = \dot q^i\,dp_i - \frac{\partial L}{\partial q^i}dq^i - \frac{\partial L}{\partial t}dt.$$

Comparing with the expression $dH = (\partial H/\partial q^i)dq^i + (\partial H/\partial p_i)dp_i + (\partial H/\partial t)dt$:
$$\frac{\partial H}{\partial p_i} = \dot q^i, \qquad \frac{\partial H}{\partial q^i} = -\frac{\partial L}{\partial q^i}, \qquad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}.$$

These three are **algebraic identities** following directly from the definition $H = p\dot q - L$ and $p = \partial L/\partial \dot q$. They are the **partial-derivative relations** between $L$ and $H$.

**Now apply Euler–Lagrange**. EL says $\partial L/\partial q^i = d/dt(\partial L/\partial \dot q^i) = dp_i/dt$. Combining with the identity $\partial H/\partial q^i = -\partial L/\partial q^i$, we get
$$\frac{\partial H}{\partial q^i} = -\frac{dp_i}{dt}, \quad \text{i.e.,} \quad \dot p_i = -\frac{\partial H}{\partial q^i}.$$

This is the second Hamilton's equation. The first Hamilton's equation $\dot q^i = \partial H/\partial p_i$ comes from the first algebraic identity above. So **EL on $TQ$ + Legendre transform = Hamilton on $T^*Q$**.

The reverse direction (Hamilton $\to$ EL) follows by the same calculation in reverse: from Hamilton's equations, the algebraic identities give back EL.

**Equivalence of variational principles.** The action $\int L\,dt$ on $TQ$-paths and the action $\int(p\dot q - H)dt$ on $T^*Q$-paths differ by $\int H\,dt - \int(p\dot q - L)dt = \int(H + L - p\dot q)dt = 0$ (using $H = p\dot q - L$). Wait, that's not quite right. Let me redo: the two actions differ by an additive *constant* on solutions (where $p = \partial L/\partial \dot q$), but the variational principle on $T^*Q$ allows arbitrary variations of $p$ — not constrained to $p = \partial L/\partial \dot q$. The variational principle on $T^*Q$ produces *two* sets of equations: $\delta p$ gives $\dot q = \partial H/\partial p$ (Legendre transform), and $\delta q$ gives $\dot p = -\partial H/\partial q$ (Hamilton's other equation). Together these are equivalent to EL (once Legendre is used to relate $p$ and $\dot q$).

---

# What Makes This Hard

The proof is mostly bookkeeping with the chain rule, but several subtleties trip up beginners. (1) Understanding **why $H = p\dot q - L$ is well-defined** — i.e., why $\dot q$ can be expressed as a function of $(q, p)$ via the Legendre transform — requires regularity of $L$ (invertible Hessian). For singular Lagrangians the formula is ambiguous, and the constraint analysis of Dirac is needed. (2) The **two variational principles look different**: the Lagrangian one varies $q$ alone (with $\dot q$ determined by $q$); the Hamiltonian one varies $q$ and $p$ independently. The reconciliation: the Hamiltonian principle's $\delta p$ variation produces the Legendre transform $p = \partial L/\partial \dot q$, recovering the Lagrangian constraint. (3) The **sign conventions** for $H$ vary in the literature (some define $H = L - p\dot q$ rather than $p\dot q - L$), and the sign affects Hamilton's equations and the Poisson bracket.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Compute the partial derivatives of $H$ via the chain rule, using $H = p\dot q - L$ and $p = \partial L/\partial \dot q$. Three identities emerge: $\partial H/\partial p = \dot q$, $\partial H/\partial q = -\partial L/\partial q$, $\partial H/\partial t = -\partial L/\partial t$. The first is one of Hamilton's equations directly; the second, combined with EL, gives the second Hamilton equation $\dot p = -\partial H/\partial q$.

**Subgoal decomposition:**

1. **Compute $dH$ via chain rule.** Express $dH$ as a sum involving $dq, dp, d\dot q, dt$.
   - *Hint:* differentiate $H = p\dot q - L$ as a function of $(q, \dot q, p, t)$ with $\dot q$ implicitly $\dot q(q, p, t)$.
   - *Why needed:* sets up the identification of $\partial H/\partial q$, $\partial H/\partial p$, $\partial H/\partial t$.

2. **Apply $p = \partial L/\partial \dot q$ to cancel $d\dot q$ terms.** The terms involving $d\dot q$ are $p\,d\dot q - (\partial L/\partial \dot q)d\dot q = 0$.
   - *Hint:* the Legendre transform definition.
   - *Why needed:* simplifies $dH$ to involve only $dq, dp, dt$.

3. **Identify partial derivatives of $H$.** Match terms in $dH$ to get $\partial H/\partial p = \dot q$, $\partial H/\partial q = -\partial L/\partial q$, $\partial H/\partial t = -\partial L/\partial t$.
   - *Hint:* coefficient matching in the differential.
   - *Why needed:* gives the three algebraic identities relating $H$ and $L$.

4. **First Hamilton's equation.** $\dot q^i = \partial H/\partial p_i$ is one of the identities, holding automatically.
   - *Hint:* this is just the Legendre transform restated.
   - *Why needed:* the first half of Hamilton's equations.

5. **Second Hamilton's equation via EL.** From EL: $\partial L/\partial q^i = (d/dt)(\partial L/\partial \dot q^i) = \dot p_i$. Combined with $\partial H/\partial q^i = -\partial L/\partial q^i$, this gives $\dot p_i = -\partial H/\partial q^i$.
   - *Hint:* apply EL to convert $\partial L/\partial q^i$ into $\dot p_i$.
   - *Why needed:* the second half of Hamilton's equations.

6. **Equivalence of variational principles.** The action $\int(p\dot q - H)dt$ on $T^*Q$-paths, with $q$-endpoints fixed and $p$ free, has stationary trajectories that satisfy both Hamilton's equations (one from $\delta p$, one from $\delta q$). These are equivalent to EL via the Legendre transform.
   - *Hint:* compute $\delta\int(p\dot q - H)dt$ explicitly.
   - *Why needed:* shows the two variational principles produce the same dynamics.

---

# Lemma Decomposition

> [!note]- Lemma 1: Partial derivatives of $H$ given Legendre transform
> **Statement:** Given $H(q, p, t) = p_i \dot q^i - L(q, \dot q, t)$ with $p_i = \partial L/\partial \dot q^i$ (so $\dot q$ is implicitly a function of $(q, p, t)$), the partial derivatives are:
> $$\frac{\partial H}{\partial p_i} = \dot q^i, \qquad \frac{\partial H}{\partial q^i} = -\frac{\partial L}{\partial q^i}, \qquad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}.$$
>
> **Hint:** Differentiate $H = p\dot q - L$ using the chain rule and use the Legendre transform relation to cancel the $d\dot q$ terms.
>
> **Why needed:** These three identities are the algebraic content of the Legendre duality and the key to the equivalence of formalisms.
>
> > [!note]- Full proof
> > Compute $dH$ treating $H$ as a function of $(q, p, t)$ with $\dot q = \dot q(q, p, t)$ implicitly. By the chain rule:
> > $$dH = \dot q^i\,dp_i + p_i\,d\dot q^i - \frac{\partial L}{\partial q^i}dq^i - \frac{\partial L}{\partial \dot q^i}d\dot q^i - \frac{\partial L}{\partial t}dt,$$
> > where $d\dot q^i = (\partial \dot q^i/\partial q^j)dq^j + (\partial \dot q^i/\partial p_j)dp_j + (\partial \dot q^i/\partial t)dt$ (chain rule on the implicit $\dot q(q, p, t)$).
> >
> > Apply the Legendre relation $p_i = \partial L/\partial \dot q^i$: the coefficients of $d\dot q^i$ are $p_i - \partial L/\partial \dot q^i = 0$, so the $d\dot q^i$ terms cancel.
> >
> > The remaining terms are:
> > $$dH = \dot q^i\,dp_i - \frac{\partial L}{\partial q^i}dq^i - \frac{\partial L}{\partial t}dt.$$
> >
> > Compare with $dH = (\partial H/\partial q^i)dq^i + (\partial H/\partial p_i)dp_i + (\partial H/\partial t)dt$:
> > $$\frac{\partial H}{\partial p_i} = \dot q^i, \quad \frac{\partial H}{\partial q^i} = -\frac{\partial L}{\partial q^i}, \quad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}.$$

> [!note]- Lemma 2: EL implies $\dot p = -\partial H/\partial q$
> **Statement:** If $\gamma : [a, b] \to Q$ satisfies the Euler–Lagrange equations, then the lifted curve $(\gamma, p) \in T^*Q$ with $p = \partial L/\partial \dot q$ satisfies $\dot p_i = -\partial H/\partial q^i$ at every $t$.
>
> **Hint:** Substitute Lemma 1 and EL.
>
> **Why needed:** The second Hamilton equation, derived from EL via the Legendre transform.
>
> > [!note]- Full proof
> > EL: $\partial L/\partial q^i = (d/dt)(\partial L/\partial \dot q^i) = (d/dt)p_i = \dot p_i$, using $p_i = \partial L/\partial \dot q^i$.
> >
> > By Lemma 1: $\partial H/\partial q^i = -\partial L/\partial q^i = -\dot p_i$.
> >
> > Hence: $\dot p_i = -\partial H/\partial q^i$.

> [!note]- Lemma 3: Hamilton $\Rightarrow$ EL
> **Statement:** If $(\gamma, p)$ satisfies Hamilton's equations $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$, then $\gamma$ satisfies the Euler–Lagrange equations for $L = p\dot q - H$ (the inverse Legendre transform).
>
> **Hint:** Reverse the argument of Lemma 2.
>
> **Why needed:** Provides the reverse direction of the equivalence.
>
> > [!note]- Full proof
> > By Lemma 1 (applied to the inverse Legendre transform), $\partial L/\partial q^i = -\partial H/\partial q^i$ and $\partial L/\partial \dot q^i = p_i$.
> >
> > Hamilton: $\dot p_i = -\partial H/\partial q^i = \partial L/\partial q^i$. Also $\dot p_i = (d/dt)p_i = (d/dt)(\partial L/\partial \dot q^i)$. Combining: $\partial L/\partial q^i = (d/dt)(\partial L/\partial \dot q^i)$ — the Euler–Lagrange equations.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $L : TQ \times \mathbb{R} \to \mathbb{R}$ be a regular Lagrangian, and let $H : T^*Q \times \mathbb{R} \to \mathbb{R}$ be defined by $H(q, p, t) = p_i \dot q^i - L(q, \dot q, t)$ with $\dot q = \dot q(q, p, t)$ via the Legendre transform $p_i = \partial L/\partial \dot q^i$ (inverted using regularity).
>
> **Step 0 — Well-posedness of $H$.** Regularity of $L$ means the Hessian $\partial^2 L/\partial \dot q^i\partial \dot q^j$ is invertible, so by the implicit function theorem the equation $p_i = \partial L/\partial \dot q^i$ can be uniquely solved for $\dot q$ in terms of $(q, p)$ at each $t$. Hence $H(q, p, t)$ is well-defined and smooth.
>
> **Step 1 — Partial derivatives of $H$.** By Lemma 1:
> $$\frac{\partial H}{\partial p_i} = \dot q^i, \quad \frac{\partial H}{\partial q^i} = -\frac{\partial L}{\partial q^i}, \quad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}.$$
>
> **Step 2 — EL $\Rightarrow$ Hamilton.** Suppose $\gamma$ satisfies EL: $\partial L/\partial q^i = (d/dt)(\partial L/\partial \dot q^i)$.
>
> First Hamilton equation: $\dot q^i = \partial H/\partial p_i$ — this is the first identity from Step 1, holding automatically along the lifted curve.
>
> Second Hamilton equation: by Lemma 2, $\dot p_i = -\partial H/\partial q^i$.
>
> So $(\gamma, p)$ satisfies both Hamilton's equations.
>
> **Step 3 — Hamilton $\Rightarrow$ EL.** Suppose $(\gamma, p)$ satisfies Hamilton's equations. By Lemma 3 (running the argument in reverse), $\gamma$ satisfies EL.
>
> **Step 4 — Equivalence of variational principles.** Hamilton's principle in phase space says $\delta\int(p_i\dot q^i - H(q, p, t))dt = 0$ for all variations with $q$ fixed at the endpoints (but $p$ free). Compute the variation:
> $$\delta\int_a^b (p_i\dot q^i - H)dt = \int_a^b \left[(\delta p_i)\dot q^i + p_i(\delta\dot q^i) - \frac{\partial H}{\partial q^i}\delta q^i - \frac{\partial H}{\partial p_i}\delta p_i\right] dt.$$
>
> Integrate $p_i\delta\dot q^i = p_i d(\delta q^i)/dt$ by parts: $\int p_i (d\delta q^i/dt)dt = [p_i\delta q^i]_a^b - \int \dot p_i \delta q^i\,dt$. Boundary term vanishes by fixed $q$-endpoints.
>
> Substitute:
> $$\delta\int = \int_a^b \left[(\dot q^i - \partial H/\partial p_i)\delta p_i + (-\dot p_i - \partial H/\partial q^i)\delta q^i\right] dt.$$
>
> Vanishing for all variations $(\delta q, \delta p)$ — with $\delta q$ fixed at endpoints, $\delta p$ free — forces both bracketed expressions to vanish pointwise (by the fundamental lemma):
> $$\dot q^i = \partial H/\partial p_i, \qquad \dot p_i = -\partial H/\partial q^i.$$
>
> These are Hamilton's equations. By Steps 2–3, they are equivalent to EL.
>
> So the Lagrangian variational principle on $TQ$ (Hamilton's principle, lifted) is equivalent to the Hamiltonian variational principle on $T^*Q$.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Thermodynamics: Legendre dual potentials.** The Legendre transform connecting $L$ to $H$ is exactly the same mathematical operation as the Legendre transform in thermodynamics relating energy potentials. Verify: from internal energy $U(S, V)$, the Helmholtz free energy is $F(T, V) = U - TS$ (Legendre dual in the $(S, T)$ pair), and the Gibbs free energy is $G(T, p) = F + pV = U - TS + pV$ (Legendre dual in both pairs). The "$H = p\dot q - L$" formula in mechanics is structurally identical to "$F = -TS + U$" in thermodynamics. The Maxwell relations between thermodynamic derivatives are second-derivative identities of these Legendre-related potentials, mirroring the relations $\partial H/\partial p_i = \dot q^i$ and $\partial L/\partial \dot q^i = p_i$ in mechanics.

**Convex optimization: primal-dual problems.** The Legendre transform converts a primal optimization problem (minimize $f(x)$) into its dual (maximize $-f^*(p)$ where $f^*(p) = \sup_x(px - f(x))$). The strong-duality theorem says these have the same optimal value under regularity conditions (convexity). Verify the analogy: a regular Lagrangian (positive-definite Hessian = strict convexity in $\dot q$) gives a unique Hamiltonian by Legendre, just as a strictly convex $f$ has a unique Legendre dual $f^*$. The mechanical action principle and the convex-optimization duality are the same mathematical structure.

**Path integrals: Lagrangian and Hamiltonian formulations.** Feynman's path integral can be formulated either way. The **Lagrangian path integral** is $\int e^{iS[\gamma]/\hbar}\mathcal{D}[\gamma]$ over paths in configuration space $Q$, weighted by the classical action $S = \int L\,dt$. The **Hamiltonian (phase-space) path integral** is $\int e^{i\int(p\dot q - H)dt/\hbar}\mathcal{D}[(\gamma, p)]$ over paths in phase space $T^*Q$. Performing the Gaussian integral over $p$ (for separable Hamiltonians $H = T(p) + V(q)$ with quadratic $T$) reduces the phase-space integral to the configuration-space integral, with the Legendre transform $p \to \dot q$ producing the equivalence. This is the path-integral version of the equivalence theorem.

---

# Bridges

- **[[Def - The Legendre Transform]]**: this theorem is the dynamical content of the Legendre transform. The transform provides the bijection $TQ \leftrightarrow T^*Q$; this theorem shows the bijection intertwines the two dynamics (EL and Hamilton's). Together they say: Lagrangian and Hamiltonian mechanics are the same theory in two languages.

- **[[Thm - Hamilton's Principle in TQ Gives Euler-Lagrange Equations]]**: this gives EL from a variational principle on $TQ$. The current theorem then converts EL to Hamilton's equations on $T^*Q$. Combining: a variational principle on $TQ$ produces dynamics on $T^*Q$ via the chain "variation $\to$ EL $\to$ Legendre $\to$ Hamilton".

- **Dirac constraint analysis (for singular Lagrangians)**: when $L$ is singular (degenerate Hessian), the Legendre transform is not invertible, and the image $\mathbb{F}L(TQ) \subset T^*Q$ is a proper constraint surface. The equivalence of Lagrangian and Hamiltonian formalisms requires the **Dirac–Bergmann constraint algorithm**: identify primary, secondary, ... constraints; classify as first-class (gauge-generating) or second-class (constraining); reduce to the physical phase space. This is the canonical formulation of gauge theories — electromagnetism, Yang–Mills, general relativity. The non-regular case is the generic case in field theory, and the constraint analysis is essential.

- **Path integral quantization**: the equivalence of Lagrangian and Hamiltonian classical mechanics extends to quantum mechanics via the path integral. The **configuration-space path integral** $\int e^{iS/\hbar}\mathcal{D}[\gamma]$ and the **phase-space path integral** $\int e^{i\int(p\dot q - H)dt/\hbar}\mathcal{D}[(\gamma, p)]$ are equivalent (for regular systems), with the Gaussian integration over momenta recovering one from the other.

---

# Unlocked by This

> [!tip] Dirac Constraint Analysis *(from Gauge Theory)*
> When a Lagrangian is singular (degenerate Hessian), the Legendre transform fails to be invertible, and the image $\mathbb{F}L(TQ)$ is a proper submanifold of $T^*Q$ — the **primary constraint surface**. Demanding that the constraints be preserved by the Hamiltonian flow gives **secondary constraints**, and the iteration continues until a final constraint surface is reached. The constraints split into **first-class** (those that Poisson-commute with all others on the surface — these generate gauge transformations) and **second-class** (those that have nontrivial Poisson brackets among themselves — these are genuine constraints reducing the physical phase space). This is the **Dirac–Bergmann–Bergmann algorithm**, and it is the foundation of the canonical formulation of gauge theories: electromagnetism, Yang–Mills, general relativity. The Hamiltonian formulation of these theories requires the full constraint machinery; the Lagrangian formulation hides the constraints inside the variational principle.

> [!tip] Hamilton–Jacobi Equation *(from Classical Mechanics)*
> The Hamiltonian formulation, via the **generating function** approach to canonical transformations, leads to the **Hamilton–Jacobi equation** $\partial S/\partial t + H(q, \partial S/\partial q, t) = 0$ — a first-order PDE for a function $S(q, t)$ (Hamilton's principal function). A **complete integral** $S(q, \alpha, t)$ depending on $n$ parameters $\alpha$ gives the general solution of Hamilton's equations by quadratures: trajectories are level sets of $\partial S/\partial \alpha$. This is the most powerful classical solution method for integrable systems, and it is the bridge to the **WKB approximation** in quantum mechanics: $\psi \approx e^{iS/\hbar}$ in the semiclassical limit, with $S$ the Hamilton–Jacobi function. The Lagrangian-Hamiltonian equivalence is what makes Hamilton–Jacobi theory work.

> [!tip] Canonical Quantization and the Heisenberg Algebra *(from Quantum Mechanics)*
> The Hamiltonian formulation, with its Poisson algebra of observables $C^\infty(T^*Q)$, is the natural starting point for **canonical quantization**. The substitution $\{f, g\} \to [\hat f, \hat g]/i\hbar$ promotes the Poisson algebra to the operator algebra on a Hilbert space; the fundamental Poisson brackets $\{q^i, p_j\} = \delta^i_j$ become the canonical commutation relations $[\hat q^i, \hat p_j] = i\hbar\delta^i_j$ — the **Heisenberg algebra**. By the **Stone–von Neumann theorem**, all irreducible representations of the Heisenberg algebra are unitarily equivalent, giving uniqueness of canonical quantization for finite-dimensional systems. The Lagrangian formulation provides the alternative quantization via Feynman's path integral, which is sometimes more convenient (especially for field theory with manifest Lorentz invariance), but both routes produce the same quantum mechanics.
