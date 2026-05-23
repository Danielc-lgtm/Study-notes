---
type: exercise
subject: geometric-mechanics
difficulty: "⭐⭐"
prereqs:
  - "Def - Riemannian Metric"
  - "Def - The Canonical Symplectic Form on a Cotangent Bundle"
  - "Def - Hamiltonian Vector Field"
  - "Def - Hamiltonian Function"
tags: [physics, geometric-mechanics, symplectic-geometry, riemannian-geometry]
---

# Problem Statement

Let $(M, g)$ be a Riemannian manifold with metric $g_{ij}$ (and inverse $g^{ij}$) in local coordinates $(q^i)$. Define the **geodesic Hamiltonian** on the cotangent bundle $T^*M$ (with canonical symplectic form $\omega = \sum_i dp_i \wedge dq^i$) by

$$H(q, p) := \frac{1}{2}g^{ij}(q)\,p_i p_j.$$

This is half the squared norm of the covector $p \in T^*_qM$.

(a) Compute the Hamiltonian vector field $X_H$ and write down Hamilton's equations explicitly.

(b) Show that the projection $\pi : T^*M \to M$ of an integral curve of $X_H$ to $M$ is a **geodesic** of the Riemannian metric $g$, parametrized by arc length (up to a constant).

(c) Verify that $H$ is conserved along the flow, and interpret the conserved value geometrically.

(d) Use the Legendre-transform relationship to show that the Lagrangian giving the same dynamics is $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$, and verify that the Euler–Lagrange equations are the geodesic equations.

**Recall:**

A geodesic in $(M, g)$ is a curve $\gamma(t)$ satisfying $\ddot q^k + \Gamma^k_{ij}\dot q^i\dot q^j = 0$, where the Christoffel symbols are $\Gamma^k_{ij} = \tfrac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. The geodesic equation is the Euler–Lagrange equation for the Lagrangian $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ (the geodesic energy functional), or equivalently for $L = \sqrt{g_{ij}\dot q^i\dot q^j}$ (the arc-length functional, modulo reparametrization invariance).

![[Def - Hamiltonian Vector Field#The Definition]]

---

# Convergent Strategy

**Problem class:** This is the **prototypical Hamiltonian system on a cotangent bundle**: take the simplest possible Hamiltonian (the kinetic energy in the dual metric), and show its dynamics is exactly the geodesic flow of the base manifold. The problem class is "show that a specific physical dynamics is Hamiltonian for a specific $H$ on a specific phase space" — and here the physical dynamics is geodesic motion.

**Assumption pattern:** We have a Riemannian manifold $(M, g)$ — providing the metric coefficients $g_{ij}$ and the Christoffel symbols. We choose the Hamiltonian $H = \tfrac{1}{2}g^{ij}p_ip_j$ on $T^*M$. The goal is to derive the geodesic equation as the projection of Hamilton's equations.

**Theorem routing:** Apply the [[Def - Hamiltonian Vector Field|Hamiltonian vector field formula]] to $H$ in canonical coordinates: $\dot q^k = \partial H/\partial p_k = g^{kj}p_j$ and $\dot p_k = -\partial H/\partial q^k = -\tfrac{1}{2}(\partial_k g^{ij})p_ip_j$. Substitute $p_j = g_{jl}\dot q^l$ (from the first equation) into the second and rewrite using Christoffel symbols to recover the geodesic equation. Verify conservation of $H$ via $X_H(H) = 0$ (the abstract reason) or by direct substitution. Cross-check via the Lagrangian: $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ has Legendre transform $p_i = g_{ij}\dot q^j$, $H = \tfrac{1}{2}g^{ij}p_ip_j$ — consistent.

**Key decision point:** The non-obvious step is the **conversion from $(p, \dot q)$ to coordinates with Christoffels**: starting from $\dot p_k = -\tfrac{1}{2}(\partial_k g^{ij})p_ip_j$ and $p_j = g_{jl}\dot q^l$, derive $\ddot q^m + \Gamma^m_{ij}\dot q^i\dot q^j = 0$ requires the identity $\partial_k g^{ij} = -g^{ia}g^{jb}\partial_k g_{ab}$ (from differentiating $g^{ij}g_{jk} = \delta^i_k$) and the definition of $\Gamma$. The calculation is mechanical but the key insight is that **the geodesic equation is hiding inside the Hamilton's equations for the kinetic-energy Hamiltonian**.

---

# Legal Operations Used

1. **Operation 1 from the topic page (Compute $X_H$ from $\iota_{X_H}\omega = dH$ in canonical coordinates).** Used to write Hamilton's equations for $H = \tfrac{1}{2}g^{ij}p_ip_j$.

2. **Operation 6 from the topic page (Legendre transform between Lagrangian and Hamiltonian pictures).** Used to identify the Lagrangian $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ corresponding to $H = \tfrac{1}{2}g^{ij}p_ip_j$, and to cross-check that the Euler–Lagrange equations give the geodesic equation.

3. **Operation 3 from the topic page (check $\{f, H\} = 0$).** Used to verify $H$ is conserved (with $f = H$, $\{H, H\} = 0$ automatically by antisymmetry). The conserved value $H = \tfrac{1}{2}|\dot\gamma|^2_g$ is the squared speed.

---

# Hints

> [!note]- Hint 1
> Hamilton's equations for $H = \tfrac{1}{2}g^{ij}p_ip_j$: $\dot q^k = \partial H/\partial p_k = g^{kj}p_j$ and $\dot p_k = -\partial H/\partial q^k = -\tfrac{1}{2}(\partial_k g^{ij})p_ip_j$. Note $p$ is a covector and $g^{ij}p_j$ is its raised-index version.

> [!note]- Hint 2
> Use the identity $\partial_k g^{ij} = -g^{ia}g^{jb}\partial_k g_{ab}$ (from differentiating $g^{ij}g_{jl} = \delta^i_l$). This lets you express $\dot p_k$ in terms of $g_{ab}$ derivatives rather than $g^{ab}$ derivatives.

> [!note]- Hint 3
> Use the chain rule to compute $\ddot q^m = (d/dt)(g^{mj}p_j) = (\partial_l g^{mj})\dot q^l p_j + g^{mj}\dot p_j$. Substitute Hamilton's equations and identify the Christoffel symbols $\Gamma^m_{ij} = \tfrac{1}{2}g^{ml}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$.

> [!note]- Hint 4
> The Lagrangian counterpart is $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$. The conjugate momentum is $p_i = g_{ij}\dot q^j$ — the "lowered index" of the velocity. The Euler–Lagrange equation for this $L$ is the geodesic equation directly (this is the variational characterization of geodesics, see [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]]).

---

# Solution

The proof breaks into four steps. Step 1 writes Hamilton's equations. Step 2 derives the geodesic equation as the projection. Step 3 verifies energy conservation. Step 4 cross-checks via the Lagrangian.

**Step 1: Hamilton's equations for $H = \tfrac{1}{2}g^{ij}p_ip_j$.**

$\dot q^k = g^{kj}p_j$ and $\dot p_k = -\tfrac{1}{2}(\partial_k g^{ij})p_ip_j$.

> [!note]- Derivation
> Compute partial derivatives:
> $$\frac{\partial H}{\partial p_k} = \frac{1}{2}\cdot 2 g^{kj}p_j = g^{kj}p_j,$$
> using symmetry $g^{ij} = g^{ji}$ and the linearity of $\partial/\partial p_k$.
> $$\frac{\partial H}{\partial q^k} = \frac{1}{2}(\partial_k g^{ij})p_ip_j.$$
> Hamilton's equations:
> $$\dot q^k = \frac{\partial H}{\partial p_k} = g^{kj}p_j, \qquad \dot p_k = -\frac{\partial H}{\partial q^k} = -\frac{1}{2}(\partial_k g^{ij})p_ip_j.$$

**Step 2: The projected curve is a geodesic.**

Substituting $p_j = g_{jl}\dot q^l$ and using the Christoffel-symbol identities, $\ddot q^m + \Gamma^m_{ij}\dot q^i\dot q^j = 0$.

> [!note]- Derivation
> From step 1, $\dot q^k = g^{kj}p_j$, so $p_j = g_{jl}\dot q^l$ (inverting using $g^{kj}g_{jl} = \delta^k_l$).
>
> Differentiate $\dot q^k = g^{kj}p_j$ with respect to $t$:
> $$\ddot q^k = (\partial_l g^{kj})\dot q^l p_j + g^{kj}\dot p_j = (\partial_l g^{kj})\dot q^l (g_{jm}\dot q^m) + g^{kj}\dot p_j.$$
> Use $\partial_l g^{kj} = -g^{ka}g^{jb}(\partial_l g_{ab})$ (from differentiating $g^{kj}g_{ja} = \delta^k_a$):
> $$\ddot q^k = -g^{ka}g^{jb}(\partial_l g_{ab})\dot q^l g_{jm}\dot q^m + g^{kj}\dot p_j = -g^{ka}\delta^b_m(\partial_l g_{ab})\dot q^l\dot q^m + g^{kj}\dot p_j$$
> Wait, $g^{jb}g_{jm} = \delta^b_m$, so:
> $$\ddot q^k = -g^{ka}(\partial_l g_{ab})\dot q^l\dot q^b\delta^b_m\,(\text{wait, redo}).$$
>
> Let me redo this more carefully. We have $\ddot q^k = (\partial_l g^{kj})\dot q^l p_j + g^{kj}\dot p_j$.
>
> Substituting $p_j = g_{jm}\dot q^m$: $(\partial_l g^{kj})\dot q^l g_{jm}\dot q^m = -g^{ka}g^{jb}(\partial_l g_{ab})\dot q^l g_{jm}\dot q^m = -g^{ka}\delta^b_m(\partial_l g_{ab})\dot q^l\dot q^m = -g^{ka}(\partial_l g_{am})\dot q^l\dot q^m$.
>
> Substituting Hamilton's equation for $\dot p_j$: $g^{kj}\dot p_j = -\tfrac{1}{2}g^{kj}(\partial_j g^{ab})p_ap_b = -\tfrac{1}{2}g^{kj}(\partial_j g^{ab})g_{ai}\dot q^i g_{bm}\dot q^m = +\tfrac{1}{2}g^{kj}g^{ac}g^{bd}(\partial_j g_{cd})g_{ai}\dot q^i g_{bm}\dot q^m = +\tfrac{1}{2}g^{kj}\delta^c_i\delta^d_m(\partial_j g_{cd})\dot q^i\dot q^m = +\tfrac{1}{2}g^{kj}(\partial_j g_{im})\dot q^i\dot q^m$.
>
> Combining:
> $$\ddot q^k = -g^{ka}(\partial_l g_{am})\dot q^l\dot q^m + \tfrac{1}{2}g^{kj}(\partial_j g_{im})\dot q^i\dot q^m.$$
> Relabel: the first term has indices $(l, m)$ summed in $\dot q^l\dot q^m$; the second has $(i, m)$. Rename $l \to i$ in the first:
> $$\ddot q^k = -g^{ka}(\partial_i g_{am})\dot q^i\dot q^m + \tfrac{1}{2}g^{kj}(\partial_j g_{im})\dot q^i\dot q^m.$$
> Symmetrize the first term over $(i, m)$ since $\dot q^i\dot q^m$ is symmetric:
> $$-g^{ka}(\partial_i g_{am})\dot q^i\dot q^m = -\tfrac{1}{2}g^{ka}\big[(\partial_i g_{am}) + (\partial_m g_{ai})\big]\dot q^i\dot q^m.$$
> Combine all three terms:
> $$\ddot q^k = -\tfrac{1}{2}g^{ka}\big[\partial_i g_{am} + \partial_m g_{ai} - \partial_a g_{im}\big]\dot q^i\dot q^m$$
> (renaming $j \to a$ in the second term). The bracket is exactly $-2\Gamma^k_{im}$ since
> $$\Gamma^k_{im} = \tfrac{1}{2}g^{ka}(\partial_i g_{am} + \partial_m g_{ai} - \partial_a g_{im}).$$
> Therefore:
> $$\ddot q^k = -\Gamma^k_{im}\dot q^i\dot q^m, \quad \text{i.e.,} \quad \ddot q^k + \Gamma^k_{im}\dot q^i\dot q^m = 0.$$
> **This is the geodesic equation.** The projection $\gamma(t) := \pi(\phi^H_t(q_0, p_0))$ to $M$ of an integral curve of $X_H$ is a geodesic of the Riemannian metric $g$. ✓

**Step 3: $H$ is conserved.**

$H(q(t), p(t)) = H(q_0, p_0)$ — constant along the flow. Geometrically, $H = \tfrac{1}{2}|\dot\gamma|^2_g$ is the squared speed in the Riemannian metric, and the geodesic is parametrized by arc length (up to a constant scale).

> [!note]- Derivation
> Abstract reason: $X_H(H) = \omega(X_H, X_H) = 0$ by antisymmetry of $\omega$ (for any Hamiltonian, energy is conserved along its own flow).
>
> Concrete reason: $dH/dt = (\partial H/\partial q^k)\dot q^k + (\partial H/\partial p_k)\dot p_k$. By Hamilton's equations, $\dot q^k = \partial H/\partial p_k$ and $\dot p_k = -\partial H/\partial q^k$. So $dH/dt = (\partial H/\partial q^k)(\partial H/\partial p_k) - (\partial H/\partial p_k)(\partial H/\partial q^k) = 0$. ✓
>
> **Geometric interpretation:** $H = \tfrac{1}{2}g^{ij}p_ip_j = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j = \tfrac{1}{2}|\dot\gamma|^2_g$ — half the squared speed of the geodesic in the Riemannian metric. Conservation of $H$ means **the geodesic flow preserves the speed**, hence the parametrization is affine in arc length: $s = |\dot\gamma|_g \cdot t$, with $|\dot\gamma|_g = \sqrt{2H}$ constant.
>
> So **geodesics from the Hamiltonian flow of $H = \tfrac{1}{2}|p|^2_g$ are automatically parametrized by arc length (up to a constant scale equal to $\sqrt{2E}$, where $E$ is the energy)**.

**Step 4: Lagrangian cross-check.**

$L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ has Legendre transform $p_i = g_{ij}\dot q^j$, $H = \tfrac{1}{2}g^{ij}p_ip_j$. The Euler–Lagrange equation for $L$ is the geodesic equation directly.

> [!note]- Derivation
> The Lagrangian $L = \tfrac{1}{2}g_{ij}(q)\dot q^i\dot q^j$ has conjugate momentum
> $$p_i = \frac{\partial L}{\partial \dot q^i} = g_{ij}\dot q^j.$$
> So $\dot q^j = g^{ji}p_i$ — the inverse Legendre transform. The Hamiltonian:
> $$H = p_i\dot q^i - L = p_i g^{ij}p_j - \tfrac{1}{2}g_{ij}g^{ia}p_a g^{jb}p_b = g^{ij}p_ip_j - \tfrac{1}{2}\delta^a_j g^{jb}p_a p_b = g^{ij}p_ip_j - \tfrac{1}{2}g^{ab}p_ap_b = \tfrac{1}{2}g^{ij}p_ip_j.$$
> ✓
>
> The Euler–Lagrange equation for $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ is the standard geodesic-energy variational principle. Compute:
> $$\frac{\partial L}{\partial q^k} = \tfrac{1}{2}(\partial_k g_{ij})\dot q^i\dot q^j, \qquad \frac{\partial L}{\partial \dot q^k} = g_{kj}\dot q^j.$$
> Time derivative:
> $$\frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = (\partial_l g_{kj})\dot q^l\dot q^j + g_{kj}\ddot q^j.$$
> Euler–Lagrange:
> $$\frac{\partial L}{\partial q^k} - \frac{d}{dt}\frac{\partial L}{\partial \dot q^k} = \tfrac{1}{2}(\partial_k g_{ij})\dot q^i\dot q^j - (\partial_l g_{kj})\dot q^l\dot q^j - g_{kj}\ddot q^j = 0.$$
> Solve for $\ddot q^j$: $g_{kj}\ddot q^j = \tfrac{1}{2}(\partial_k g_{ij})\dot q^i\dot q^j - (\partial_l g_{kj})\dot q^l\dot q^j$. Symmetrize the second term over $(l, j)$:
> $$g_{kj}\ddot q^j = -\tfrac{1}{2}\big[\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj}\big]\dot q^l\dot q^j.$$
> Multiplying by $g^{mk}$ and using $g^{mk}g_{kj} = \delta^m_j$:
> $$\ddot q^m = -\tfrac{1}{2}g^{mk}\big[\partial_l g_{kj} + \partial_j g_{kl} - \partial_k g_{lj}\big]\dot q^l\dot q^j = -\Gamma^m_{lj}\dot q^l\dot q^j.$$
> So $\ddot q^m + \Gamma^m_{lj}\dot q^l\dot q^j = 0$ — **the geodesic equation**. ✓ The Lagrangian and Hamiltonian formulations give the same result.

> [!note]- Complete formal solution
> Given $(M, g)$ Riemannian, define $H : T^*M \to \mathbb{R}$ by $H(q, p) = \tfrac{1}{2}g^{ij}(q)p_ip_j$.
>
> **Hamilton's equations:** $\dot q^k = g^{kj}p_j$, $\dot p_k = -\tfrac{1}{2}(\partial_k g^{ij})p_ip_j$.
>
> **Projection is geodesic:** substitute $p_j = g_{jl}\dot q^l$ (from the first equation) into the second, use $\partial_l g^{kj} = -g^{ka}g^{jb}\partial_l g_{ab}$, and reorganize to obtain
> $$\ddot q^m + \Gamma^m_{ij}\dot q^i\dot q^j = 0,$$
> the geodesic equation with $\Gamma^m_{ij} = \tfrac{1}{2}g^{ml}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$.
>
> **Energy conservation:** $H = \tfrac{1}{2}|\dot\gamma|^2_g$ is constant; the geodesic is parametrized by arc length up to scale.
>
> **Lagrangian formulation:** $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ (Legendre dual to $H$) has Euler–Lagrange equation = geodesic equation directly.

---

# Key Takeaways

**The geodesic flow is the prototype Hamiltonian system on a cotangent bundle.** For any Riemannian manifold $(M, g)$, the kinetic-energy Hamiltonian $H = \tfrac{1}{2}|p|^2_g$ on $T^*M$ generates the geodesic flow. This is the cleanest example of "physical dynamics from geometric input": the metric $g$ alone determines both the Hamiltonian (kinetic energy) and the flow (geodesic motion). All the structure of symplectic dynamics — Liouville volume preservation, Poisson brackets, conservation laws — applies to geodesic flows directly. The **ergodicity of the geodesic flow on negatively curved compact manifolds** (Anosov's theorem) is one of the deepest results in dynamical systems, and it is fundamentally a statement about the geodesic flow as a Hamiltonian system. Whenever you study the dynamics of geodesics, you are studying a Hamiltonian system; whenever you study a Hamiltonian system whose Hamiltonian is purely quadratic in the momenta, you are studying a geodesic flow.

**Jacobi's principle of least action: dynamics with potentials is geodesic motion in a conformal metric.** Generalizing this exercise, for an autonomous system with Hamiltonian $H = \tfrac{1}{2}g^{ij}p_ip_j + V(q)$ — kinetic energy plus a potential — the trajectories at fixed energy $E$ are exactly geodesics of the **Jacobi metric** $g^J_{ij} = 2(E - V)g_{ij}$ on the classically allowed region $\{q : V(q) < E\}$. This is **Jacobi's principle of least action**, and it converts any autonomous mechanical system with potential into a pure geodesic problem in a (different, conformally modified) metric. The conservation of energy is built into the conformal factor; the potential disappears into the geometry. **Mechanics with potentials is hiding inside Riemannian geometry of the configuration space, with the metric encoding the potential**. See [[Ex - Jacobi's Principle for a Particle in a Central Potential]] for a worked example.

**The geodesic flow as a Hamiltonian flow on $T^*M$ vs. the geodesic flow on $TM$.** Both pictures exist and are equivalent via the musical isomorphism $\flat : TM \to T^*M$ induced by the metric $g$. On $TM$, the geodesic flow is the Lagrangian flow for $L = \tfrac{1}{2}g_{ij}\dot q^i\dot q^j$ (no symplectic structure intrinsically). On $T^*M$, it is the Hamiltonian flow for $H = \tfrac{1}{2}g^{ij}p_ip_j$ (with canonical symplectic structure). The two are related by the Legendre transform, which is the metric musical isomorphism: $p_i = g_{ij}\dot q^j$. The Hamiltonian formulation is **slightly cleaner** because of the intrinsic symplectic structure on $T^*M$ (no metric needed), but the Lagrangian formulation is **more variational** (Hamilton's principle on length). In both cases, **geodesics are extremals of the energy functional** (or equivalently, the arc-length functional up to reparametrization). For deeper study see [[Riemannian Geometry II — Geodesics, the Exponential Map, and Variational Principles]].
