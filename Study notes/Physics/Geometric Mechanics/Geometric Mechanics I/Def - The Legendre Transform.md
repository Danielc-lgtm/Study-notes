---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - The Lagrangian Function"
  - "Def - Hamiltonian Function"
  - "Def - The Tangent Bundle"
  - "Def - Cotangent Space and Cotangent Bundle"
tags: [physics, geometric-mechanics, lagrangian-mechanics, hamiltonian-mechanics]
---

# Notation

$Q$ is a smooth manifold of dimension $n$ (configuration space). $TQ$ and $T^*Q$ are the tangent and cotangent bundles, with bundle coordinates $(q^i, \dot q^i)$ on $TQ$ and $(q^i, p_i)$ on $T^*Q$. $L : TQ \to \mathbb{R}$ is a smooth function (a [[Def - The Lagrangian Function|Lagrangian]]), and $H : T^*Q \to \mathbb{R}$ is a smooth function (a [[Def - Hamiltonian Function|Hamiltonian]]). The **Legendre transform** is the fibre-by-fibre map $\mathbb{F}L : TQ \to T^*Q$ defined below.

---

# Axiom Motivation

We have two natural arenas for classical mechanics: the **tangent bundle** $TQ$ (positions and velocities), where the Lagrangian $L = T - V$ lives and Hamilton's principle is the variational tool; and the **cotangent bundle** $T^*Q$ (positions and momenta), where the Hamiltonian $H = T + V$ lives and the symplectic structure provides Hamilton's equations. We want a canonical map between the two pictures that converts a Lagrangian dynamics into a Hamiltonian dynamics and vice versa. The motivating question is: **what is the natural way to convert velocities into momenta?**

The answer is **momentum is the derivative of the Lagrangian with respect to velocity**:

$$p_i := \frac{\partial L}{\partial \dot q^i}.$$

This is the **conjugate momentum** to the coordinate $q^i$, and it converts the velocity $\dot q^i$ (a vector at $q$) into a covector at $q$ — the momentum. For the standard mechanical Lagrangian $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j - V$, we compute $p_i = g_{ij}\dot q^j$, which is the **lowered-index version of the velocity vector** using the kinetic-energy metric. So in mechanical examples, momenta are velocities-with-index-lowered.

The map $(q, \dot q) \mapsto (q, \partial L/\partial \dot q)$ is the **Legendre transform** $\mathbb{F}L : TQ \to T^*Q$. It is fibrewise (preserves the basepoint $q$ in $Q$), and it is a (local) diffeomorphism if and only if the Lagrangian is **regular** — i.e., the Hessian matrix $\partial^2 L/\partial \dot q^i\partial \dot q^j$ is invertible. The Hessian governs the Jacobian of $\mathbb{F}L$ in the velocity directions, so invertibility of the Hessian is precisely the invertibility of $\mathbb{F}L$ (by the implicit function theorem).

Why must we work with momenta on $T^*Q$ rather than velocities on $TQ$? Three reasons.

1. **The cotangent bundle has a canonical symplectic structure.** $T^*Q$ comes equipped with the canonical 1-form $\theta = p\,dq$ and symplectic form $\omega = -d\theta = dp \wedge dq$ — entirely intrinsic, no extra structure required. The tangent bundle $TQ$ does not. The symplectic machinery — Hamilton's equations, Poisson brackets, Liouville's theorem — all live on $T^*Q$.

2. **Momenta transform tensorially with no metric.** Under a coordinate change on $Q$, the momentum components $p_i$ transform as a covector — by the **inverse Jacobian transpose** $p'_j = (\partial q^i/\partial q'^j) p_i$. This is the natural transformation law for "things you integrate against velocity to get a number". Velocities themselves transform as vectors, $\dot q'^j = (\partial q'^j/\partial q^i)\dot q^i$, which is also natural, but the *combination* $p_i\dot q^i$ (the canonical pairing) is invariant — making it the right quantity for the action integral $\int p\,dq$.

3. **Momenta naturally arise from observation.** In a physical experiment, you can measure the position of a particle (definite spatial location) and you can apply impulses to it (corresponding to momentum changes). Velocity is a derived quantity; momentum is the fundamental "impulse-like" observable. In quantum mechanics this primacy of momentum is sharpened: $\hat p = -i\hbar\partial_q$ is the operator dual to $\hat q$, with the canonical commutator $[\hat q, \hat p] = i\hbar$.

So the Legendre transform is the conversion from "velocity language" (natural for variational principles) to "momentum language" (natural for symplectic dynamics). It is **involutive on the level of fibres of the bundles**: applying the Legendre transform to the Hamiltonian (with respect to $p$) recovers the Lagrangian (with respect to $\dot q$). Concretely, define

$$H(q, p) := p_i\dot q^i - L(q, \dot q),$$

where $\dot q$ is solved in terms of $(q, p)$ via $p_i = \partial L/\partial \dot q^i$. Then $\partial H/\partial p_i = \dot q^i$ (recovered as a derivative of $H$), and $\partial H/\partial q^i = -\partial L/\partial q^i$. So Hamilton's equations $\dot q^i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q^i$ are equivalent (via the Legendre transform) to the Euler–Lagrange equations.

**What if the Lagrangian is not regular?** Then $\mathbb{F}L$ is not a local diffeomorphism, and the relationship between $TQ$ and $T^*Q$ is not bijective. Either:
- $\mathbb{F}L$ is not surjective onto $T^*Q$: some momenta don't correspond to any velocity (a **constraint** on the momenta).
- $\mathbb{F}L$ is not injective: some momenta correspond to multiple velocities (**gauge freedom**).

These are the **Dirac constraints** of gauge theory, and they reflect the fact that gauge theories have redundant degrees of freedom that must be quotiented out. For *regular* Lagrangians (the standard mechanical case), no constraints arise and the Legendre transform is a clean diffeomorphism.

**What is the geometric meaning of the formula $H = p\dot q - L$?** It is a **Legendre dual** in the convex-analysis sense: when $L$ is convex in $\dot q$, the Legendre transform of $L$ at fixed $q$ is exactly $H$, computed via $H(p) = \sup_{\dot q}(p\dot q - L(\dot q))$. The supremum is achieved at $\dot q$ satisfying $p = \partial L/\partial \dot q$, recovering the fibrewise Legendre transform. The Legendre transform in convex analysis is the master tool for converting "primal" to "dual" formulations, and the mechanics setting is just one instance.

---

# The Definition

Let $Q$ be a smooth manifold and let $L : TQ \to \mathbb{R}$ be a smooth function (a **Lagrangian**).

**The Legendre transform** of $L$ is the fibre-preserving smooth map

$$\mathbb{F}L : TQ \to T^*Q, \qquad (q, \dot q) \mapsto (q, p) \quad \text{where} \quad p_i = \frac{\partial L}{\partial \dot q^i}(q, \dot q).$$

The map sends a tangent vector $\dot q \in T_qQ$ to the cotangent vector $p \in T^*_qQ$ whose components in the dual basis are the velocity-derivatives of $L$.

The Lagrangian $L$ is **regular** (or **hyperregular**) if $\mathbb{F}L$ is a local diffeomorphism (resp. global diffeomorphism), equivalently the Hessian matrix $(\partial^2 L/\partial \dot q^i\partial \dot q^j)(q, \dot q)$ is invertible (resp. invertible and $\mathbb{F}L$ globally bijective) at every point.

**The Hamiltonian** $H$ associated to a regular Lagrangian $L$ is the smooth function on $T^*Q$ defined by

$$H(q, p) := p_i \dot q^i - L(q, \dot q),$$

where $\dot q = \dot q(q, p)$ is the unique solution of $p_i = \partial L/\partial \dot q^i$ — i.e., the value of $\dot q$ obtained by inverting the Legendre transform fibrewise. The function $H$ is well-defined precisely because $\mathbb{F}L$ is invertible (which it is, by regularity).

**The inverse Legendre transform** $\mathbb{F}H : T^*Q \to TQ$ is defined symmetrically, sending $(q, p) \mapsto (q, \dot q)$ with $\dot q^i = \partial H/\partial p_i$. The composition $\mathbb{F}H \circ \mathbb{F}L = \mathrm{id}_{TQ}$ and $\mathbb{F}L \circ \mathbb{F}H = \mathrm{id}_{T^*Q}$ — the Legendre transform is involutive.

**Equivalence of dynamics.** For a regular Lagrangian $L$ with associated Hamiltonian $H = p\dot q - L$:

$$\text{Euler–Lagrange:} \quad \frac{d}{dt}\frac{\partial L}{\partial \dot q^i} - \frac{\partial L}{\partial q^i} = 0$$

is equivalent to

$$\text{Hamilton:} \quad \dot q^i = \frac{\partial H}{\partial p_i}, \quad \dot p_i = -\frac{\partial H}{\partial q^i}.$$

The two are related by the Legendre transform: a curve $(q(t), \dot q(t))$ in $TQ$ satisfies EL iff $(q(t), p(t)) = \mathbb{F}L(q(t), \dot q(t))$ satisfies Hamilton in $T^*Q$.

**Standard example.** For $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j - V$, the Legendre transform gives $p_i = g_{ij}\dot q^j$ (so $\dot q^i = g^{ij}p_j$), and the Hamiltonian is

$$H(q, p) = p_i\dot q^i - L = p_i g^{ij}p_j - \tfrac{1}{2}g_{ij}g^{ik}p_k g^{jl}p_l + V = \tfrac{1}{2}g^{ij}p_ip_j + V = T + V,$$

the total energy. So for mechanical Lagrangians, $L = T - V$ Legendre-transforms to $H = T + V$.

---

# Categorical / Structural Definition

The Legendre transform is the **bridge between the variational ($TQ$) and Hamiltonian ($T^*Q$) formulations of mechanics**. As a categorical statement, it gives an equivalence (for regular Lagrangians):

$$\{\text{regular Lagrangians on } TQ\} \xrightarrow{\sim} \{\text{regular Hamiltonians on } T^*Q\}$$

with the correspondence $L \leftrightarrow H$ via $H = p\dot q - L$, $L = p\dot q - H$. The dynamics on either side — Euler–Lagrange on $TQ$, Hamilton on $T^*Q$ — are intertwined by the Legendre map $\mathbb{F}L$, in the sense that solution curves correspond bijectively.

The **induced symplectic structure on $TQ$** from a regular Lagrangian is $\omega_L := (\mathbb{F}L)^*\omega$ where $\omega = dp \wedge dq$ on $T^*Q$. In coordinates, $\omega_L = \sum_{i, j} \frac{\partial^2 L}{\partial \dot q^i \partial \dot q^j} d\dot q^j \wedge dq^i + (\text{position-derivative terms})$. With this structure, the Lagrangian dynamics on $TQ$ is Hamiltonian for the energy function $E_L := \dot q^i (\partial L/\partial \dot q^i) - L$.

For **singular Lagrangians** — those with degenerate Hessian — the Legendre transform is not a diffeomorphism, and the image $\mathbb{F}L(TQ) \subset T^*Q$ is a proper submanifold defined by **primary constraints**. The Dirac–Bergmann–Bergmann algorithm extracts the dynamics on this constraint surface. Gauge theories (electromagnetism, Yang–Mills, general relativity) are paradigm examples of singular Lagrangians, and the constraint analysis is essential to their canonical formulation.

In the language of convex analysis, the Legendre transform is the **involution** on smooth convex functions: for $L$ convex in $\dot q$, the function $H(p) = \sup_{\dot q}(p\dot q - L(\dot q))$ is convex in $p$, and the operation is involutive: $L(\dot q) = \sup_p(p\dot q - H(p))$. The smoothness conditions and strict convexity translate to regularity conditions on $L$ in the mechanics setting.

---

# Relate to Other Fields / Compression

The Legendre transform is the **convex-analysis involution** specialized to mechanics. In thermodynamics, the same construction relates the **internal energy** $U(S, V)$ (a function of entropy and volume) to the **Helmholtz free energy** $F(T, V) = U - TS$ (a function of temperature and volume) by Legendre transforming with respect to the conjugate pair $(S, T)$. Similarly $U \to H = U + pV$ (enthalpy) and $U \to G = U - TS + pV$ (Gibbs free energy). The dictionary is:

| Mechanics | Thermodynamics |
|---|---|
| Position $q$ | Volume $V$, Entropy $S$, ... |
| Momentum $p$ | Pressure $-p$, Temperature $T$, ... |
| Lagrangian $L(q, \dot q)$ | Internal energy $U(S, V)$ |
| Hamiltonian $H(q, p)$ | Free energies $F, G, H$ |

In both cases, the Legendre transform converts between equivalent formulations of the same physics, with the choice of "primal" or "dual" variables made by experimental convenience.

In **optimization theory**, the Legendre transform is the **dual convex function**, and its use in convex duality (Lagrangian duality, weak/strong duality, the KKT conditions) is the central tool for converting "primal" optimization problems into "dual" ones.

**True name:** the true name of the Legendre transform is **"the involution converting velocities to momenta (or one set of conjugate variables to its dual) by differentiation"** — the operational statement that captures both the mechanics application ($\mathbb{F}L : (q, \dot q) \mapsto (q, \partial L/\partial \dot q)$) and the convex-analysis generalization ($f \mapsto f^*$ where $f^*(p) = \sup_x(px - f(x))$).

---

# Examples / Corollaries

**Is an instance: standard mechanical Lagrangian $L = \tfrac{1}{2}m|\dot q|^2 - V(q)$.** Legendre transform: $p_i = m\dot q^i$, hence $\dot q^i = p_i/m$. Hamiltonian: $H = p\dot q - L = (p^2/m) - (p^2/(2m) - V) = p^2/(2m) + V$. Standard total-energy Hamiltonian, as expected.

**Is an instance: Riemannian-metric Lagrangian.** $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$. Legendre transform: $p_i = g_{ij}\dot q^j$. Hamiltonian: $H = \tfrac{1}{2}g^{ij}p_ip_j$. This is the **kinetic-energy Hamiltonian** whose flow is the geodesic flow.

**Is an instance: charged particle in EM field.** $L = \tfrac{1}{2}m|\dot q|^2 - e\phi + eA\cdot\dot q$. Legendre transform: $p_i = m\dot q^i + eA_i$ (the **canonical momentum** is the kinetic momentum *plus* the gauge field). Hamiltonian: $H = p\dot q - L = |p - eA|^2/(2m) + e\phi$. This is the **minimal coupling** Hamiltonian for a charged particle.

**Is an instance: relativistic free particle.** $L = -mc^2\sqrt{1 - |\dot q|^2/c^2}$. Legendre transform: $p_i = m\dot q^i/\sqrt{1 - |\dot q|^2/c^2}$, the relativistic momentum. Hamiltonian: $H = \sqrt{|p|^2c^2 + m^2c^4}$, the relativistic energy-momentum relation.

**Is NOT an instance (singular): $L = \dot q^1 q^2$ on $T\mathbb{R}^2$.** Hessian $\partial^2 L/\partial \dot q^i\partial \dot q^j = 0$ — completely degenerate. Legendre transform: $p_1 = q^2$, $p_2 = 0$. The image is the constraint surface $p_1 = q^2, p_2 = 0$ — a submanifold of $T^*\mathbb{R}^2$ of dimension $1$, much smaller than $\dim T^*\mathbb{R}^2 = 4$. This is a *highly* singular Lagrangian.

**Is NOT an instance (singular): Lagrangian for general relativity.** The Einstein–Hilbert Lagrangian $\mathcal{L} = R\sqrt{-g}/(16\pi G)$ is singular: the diffeomorphism symmetry of general relativity produces constraints (the Hamiltonian and momentum constraints of the ADM formalism), and the Legendre transform is not invertible. The constraint analysis is the **ADM formulation** of general relativity.

**Corollary (Hamilton's equations from Euler–Lagrange).** Differentiate $H = p\dot q - L$: $dH = \dot q\,dp + p\,d\dot q - dL = \dot q\,dp + p\,d\dot q - (\partial L/\partial q)dq - (\partial L/\partial \dot q)d\dot q = \dot q\,dp - (\partial L/\partial q)dq$ (the $d\dot q$ terms cancel by $p = \partial L/\partial \dot q$). So $\partial H/\partial p = \dot q$ and $\partial H/\partial q = -\partial L/\partial q$. Combined with Euler–Lagrange $dp/dt = \partial L/\partial q$ (which equals $-\partial H/\partial q$), we get Hamilton's equations.

**Corollary (involution).** The Legendre transform $\mathbb{F}L$ has inverse $\mathbb{F}H$: applying both gives the identity. Equivalently, $H = p\dot q - L$ Legendre-transforms back to $L = p\dot q - H$, recovering the original Lagrangian.

**Corollary (energy = Hamiltonian).** The energy function $E_L = \dot q^i(\partial L/\partial \dot q^i) - L$ on $TQ$ equals the Hamiltonian $H$ on $T^*Q$ pulled back via the Legendre transform: $E_L = H \circ \mathbb{F}L$.

**Corollary (regularity criterion).** $\mathbb{F}L$ is a local diffeomorphism iff the Hessian $\partial^2 L/\partial\dot q^i\partial\dot q^j$ is invertible. For $L = T - V$ with $T = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$, this Hessian is $g_{ij}$, invertible since $g$ is a Riemannian metric.

**Calibration check.** If you can do these three things, you have understood the definition. First, compute the Legendre transform of $L = \tfrac{1}{2}m\dot q^2 - \tfrac{1}{2}m\omega_0^2 q^2$ (harmonic oscillator Lagrangian) and verify the resulting Hamiltonian is $H = p^2/(2m) + \tfrac{1}{2}m\omega_0^2 q^2$. Second, verify the involution property for this example: compute the Legendre transform of $H$ and recover $L$. Third, show that the Hessian of $L = \tfrac{1}{2}m\dot q^2$ on $T\mathbb{R}$ is the $1\times 1$ matrix $(m)$, which is invertible since $m > 0$, confirming regularity.

---

# Unlocked by This

> [!tip] Thermodynamic Potentials and Maxwell Relations *(from Statistical Mechanics)*
> The Legendre transform pervades thermodynamics. From the internal energy $U(S, V)$ (a function of the natural variables entropy and volume), one obtains the **enthalpy** $H = U + pV$ (Legendre transform from $V$ to $p$), the **Helmholtz free energy** $F = U - TS$ (Legendre transform from $S$ to $T$), and the **Gibbs free energy** $G = U + pV - TS$ (both transforms). Each potential is the natural one for a specific physical context: $U$ for isolated systems, $F$ for systems at fixed temperature, $G$ for systems at fixed pressure and temperature. The **Maxwell relations** between thermodynamic derivatives are second-derivative identities of these Legendre-related potentials.

> [!tip] Convex Duality in Optimization *(from Applied Math)*
> The Legendre transform generalizes to the **Legendre–Fenchel transform** for general convex functions: $f^*(p) = \sup_x(px - f(x))$, with $f^{**} = f$ for convex $f$. This is the fundamental tool in convex analysis and optimization: it converts primal problems (minimize $f(x)$ subject to constraints) to dual problems (maximize $-f^*(p) - g^*(p)$), with strong duality holding under regularity conditions. The KKT conditions for constrained optimization are the Lagrangian-multiplier version of this duality.

> [!tip] Dirac Constraint Analysis for Singular Lagrangians *(from Gauge Theory)*
> When a Lagrangian is singular (degenerate Hessian) — as in every gauge theory — the Legendre transform $\mathbb{F}L$ is not invertible, and the image $\mathbb{F}L(TQ) \subset T^*Q$ is a proper constraint surface defined by **primary constraints** $\phi_i(q, p) = 0$. Demanding the constraints be preserved by the dynamics produces **secondary constraints**, and the iteration continues until closure. The result is the **Dirac–Bergmann–Bergmann algorithm**, which produces the **first-class** (gauge-generating) and **second-class** (genuinely constraining) constraints, and the dynamics on the reduced constraint surface. This is the canonical formulation of gauge theories (electromagnetism, Yang–Mills, general relativity), and it is essential for canonical quantization.
