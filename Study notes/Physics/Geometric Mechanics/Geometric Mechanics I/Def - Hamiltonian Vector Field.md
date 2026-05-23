---
type: definition
subject: geometric-mechanics
prereqs:
  - "Def - Symplectic Manifold"
  - "Def - Vector Field on a Manifold"
  - "Def - Interior Product (Contraction with a Vector Field)"
  - "Def - Hamiltonian Function"
tags: [physics, geometric-mechanics, symplectic-geometry]
---

# Notation

$(M, \omega)$ is a [[Def - Symplectic Manifold|symplectic manifold]] of dimension $2n$. $H : M \to \mathbb{R}$ is a smooth function called a **Hamiltonian**. $X_H \in \Gamma(TM)$ is the **Hamiltonian vector field** associated to $H$. $\iota_{X_H}\omega$ is the [[Def - Interior Product (Contraction with a Vector Field)|interior product]] of $\omega$ with $X_H$, the $1$-form $v \mapsto \omega(X_H, v)$. $dH$ is the exterior derivative (differential) of $H$, also a $1$-form. The flow of $X_H$ is denoted $\phi^H_t : M \to M$.

---

# Axiom Motivation

We have a symplectic manifold $(M, \omega)$, the geometric arena of classical mechanics. We have a smooth function $H : M \to \mathbb{R}$ playing the role of energy. We want to produce, from $H$ alone, a **vector field** $X_H$ whose integral curves are the dynamical trajectories of the mechanical system. The motivating question is: **what is the natural recipe for converting an energy function into a flow?**

Begin with the Riemannian analogue, which gets the structure right but the dynamics wrong. On a Riemannian manifold $(M, g)$, every smooth function $f$ has a **gradient vector field** $\nabla f$ defined by $g(\nabla f, X) = X(f) = df(X)$ for all $X$. The integral curves of $\nabla f$ are the **gradient flow lines** — they descend the energy landscape, with $f$ strictly decreasing along them (except at critical points). This is a perfectly good way to convert a function into a flow, but it is the *wrong* dynamics for mechanics: classical mechanics conserves energy, and gradient flow dissipates it. We need a different recipe.

The remedy is to use an **antisymmetric** pairing in place of the symmetric metric pairing. Define $X_H$ by

$$\omega(X_H, X) = dH(X) \quad \text{for all } X.$$

By the antisymmetry of $\omega$, $\omega(X_H, X_H) = 0$, so $dH(X_H) = 0$ — meaning $X_H(H) = 0$. **Energy is conserved along the integral curves of $X_H$, by the very algebra of the definition.** This is the structural reason Hamiltonian flows preserve their Hamiltonians: the antisymmetric pairing $\omega$ makes the "gradient" point in a direction *perpendicular* to the level sets of $H$, in the symplectic sense (i.e., in a direction $X$ with $\omega(X_H, X_H) = 0$).

The defining equation $\omega(X_H, \cdot) = dH$ is cleaner when written in terms of the [[Def - Interior Product (Contraction with a Vector Field)|interior product]]: $\iota_{X_H}\omega = dH$. Now the question is whether this equation has a unique solution $X_H$ for any choice of $H$. The interior product map $X \mapsto \iota_X\omega$ goes from $\Gamma(TM)$ to $\Omega^1(M)$; it is a bundle map $TM \to T^*M$, and it is a bundle *isomorphism* if and only if $\omega$ is nondegenerate pointwise — which is **exactly** the nondegeneracy condition for $\omega$ to be symplectic. So nondegeneracy is exactly what makes the equation $\iota_{X_H}\omega = dH$ have a unique solution.

This is the key insight: **nondegeneracy of $\omega$ is the algebraic content of "every energy function generates a unique flow"**. Without nondegeneracy, some energies would generate no flow (when $dH$ is outside the image of $X \mapsto \iota_X\omega$), and many vector fields would be Hamiltonian for the same $H$ (giving the dynamics an ambiguity). Nondegeneracy is what makes Hamiltonian mechanics into a function: $H \mapsto X_H$ is a *well-defined* map.

Why this specific equation $\iota_{X_H}\omega = dH$ — why not, say, $\iota_{X_H}\omega = 2\, dH$ or $\iota_{X_H}\omega^2 = dH$? The first variation would just rescale time (a different normalization of the flow), and the dynamics would be qualitatively the same; this is a convention. The second is not even type-correct ($\omega^2$ is a $4$-form). The equation $\iota_{X_H}\omega = dH$ is the simplest type-correct definition of $X_H$ from $H$ using $\omega$, and the additional choices of sign and scale are conventions.

The sign in $\iota_{X_H}\omega = dH$ versus $\iota_{X_H}\omega = -dH$ is the most common confusion. The convention used here (Frankel, Marsden–Ratiu) is **$\iota_{X_H}\omega = dH$**. Arnold and some older texts use $\iota_{X_H}\omega = -dH$. The sign affects: the sign of the Poisson bracket, the sign of $X_H$, and the direction of dynamical evolution. As long as one convention is used consistently throughout, both produce equivalent physics.

**What if we drop the requirement that $X_H$ be a vector field**, allowing instead a more general object (a multi-vector field, a distribution)? Then the formalism generalizes to **multi-symplectic geometry** (relevant to field theory) and to **Poisson manifolds** with degenerate Poisson tensor. The single-vector-field case is the cleanest and matches finite-dimensional mechanics.

---

# The Definition

Let $(M, \omega)$ be a symplectic manifold and let $H : M \to \mathbb{R}$ be a smooth function (a **Hamiltonian**). The **Hamiltonian vector field** of $H$ is the unique vector field $X_H \in \Gamma(TM)$ satisfying

$$\iota_{X_H}\omega = dH, \qquad \text{equivalently} \qquad \omega(X_H, Y) = dH(Y) = Y(H) \text{ for all } Y \in \Gamma(TM).$$

Existence and uniqueness of $X_H$ follow from the nondegeneracy of $\omega$: the bundle map $\omega^\flat : TM \to T^*M$, $X \mapsto \iota_X\omega$, is an isomorphism, so $X_H = (\omega^\flat)^{-1}(dH)$.

**In canonical (Darboux) coordinates** $(q^1, \dots, q^n, p_1, \dots, p_n)$ on $M$ in which $\omega = \sum_i dp_i \wedge dq^i$, the Hamiltonian vector field of $H$ is

$$X_H = \sum_i \left( \frac{\partial H}{\partial p_i}\frac{\partial}{\partial q^i} - \frac{\partial H}{\partial q^i}\frac{\partial}{\partial p_i}\right).$$

The integral curves of $X_H$ — that is, the solutions $\gamma(t)$ of $\dot\gamma(t) = X_H(\gamma(t))$ — are the trajectories of **Hamilton's equations**:

$$\dot q^i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q^i}.$$

The flow $\phi^H_t$ of $X_H$ is called the **Hamiltonian flow** of $H$. It is defined locally always, and globally when $X_H$ is complete.

A vector field $X \in \Gamma(TM)$ is called **Hamiltonian** if there exists a (globally defined) smooth function $H$ with $X = X_H$. It is called **symplectic** if $\mathcal{L}_X\omega = 0$; equivalently $\iota_X\omega$ is closed. Every Hamiltonian vector field is symplectic (by Cartan's formula, see [[Thm - Hamiltonian Flows are Symplectomorphisms]]); the converse holds if and only if $\iota_X\omega$ is exact, which on a connected $M$ depends on whether $[\iota_X\omega] \in H^1_{dR}(M)$ vanishes.

---

# Categorical / Structural Definition

The Hamiltonian-vector-field construction is the composition of two linear maps:

$$C^\infty(M) \xrightarrow{d} \Omega^1(M) \xrightarrow{(\omega^\flat)^{-1}} \Gamma(TM), \qquad H \mapsto dH \mapsto X_H.$$

The first map $d$ is the exterior derivative; the second is the inverse of the bundle isomorphism $\omega^\flat$ induced by nondegeneracy of $\omega$. Both are linear, so $H \mapsto X_H$ is linear. Its kernel is the locally constant functions on $M$ (functions with $dH = 0$); on a connected $M$, $X_H = 0$ iff $H$ is a constant.

The map $H \mapsto X_H$ is a **Lie algebra homomorphism** when $C^\infty(M)$ is given the [[Def - Poisson Bracket|Poisson bracket]] $\{f, g\} = \omega(X_f, X_g)$ and $\Gamma(TM)$ is given the Lie bracket of vector fields:

$$X_{\{f, g\}} = -[X_f, X_g].$$

(The sign depends on convention; with $\omega = -d\theta$ the negative sign appears.) The kernel is the locally constant functions, and the image is the **Hamiltonian vector fields** — a Lie subalgebra of $\Gamma(TM)$. This is one of the cornerstone facts of symplectic geometry: **the assignment $H \mapsto X_H$ packages classical mechanics as a representation of the Lie algebra of observables on the Lie algebra of vector fields**, with the symplectic form providing the dictionary.

In language of category theory, the assignment $(M, \omega) \rightsquigarrow (C^\infty(M), \{\cdot, \cdot\})$ is a contravariant functor from symplectic manifolds (with symplectomorphisms as morphisms) to Poisson algebras (with Poisson algebra homomorphisms as morphisms), and the assignment $H \mapsto X_H$ is the geometric realization of this functorial structure.

---

# Relate to Other Fields / Compression

A Hamiltonian vector field is the **symplectic analogue of a gradient vector field**, with the antisymmetric symplectic pairing $\omega$ replacing the symmetric Riemannian pairing $g$. In Riemannian geometry, $\nabla f$ is defined by $g(\nabla f, \cdot) = df$, and its integral curves descend the function $f$. In symplectic geometry, $X_H$ is defined by $\omega(X_H, \cdot) = dH$, and its integral curves preserve $H$. The difference between "descent" and "preservation" is exactly the difference between symmetric and antisymmetric pairings: $g(\nabla f, \nabla f) = |\nabla f|^2 > 0$ (gradient flow strictly decreases $f$ at non-critical points), while $\omega(X_H, X_H) = 0$ for all vector fields (Hamiltonian flow preserves $H$ everywhere).

From the perspective of quantum mechanics, the Hamiltonian vector field is the classical limit of the **commutator with the Hamiltonian operator**: in quantum mechanics, the Heisenberg equation $d\hat A/dt = [\hat H, \hat A]/i\hbar$ governs the time evolution of an observable; in classical mechanics, $df/dt = \{f, H\} = X_H(f)$ governs the same. The map $f \mapsto X_H(f) = \{f, H\}$ is the classical operator of "time evolution by Hamiltonian $H$", with $X_H$ the corresponding vector field.

**True name:** the true name of $X_H$ is **"the vector field that moves observables in time"**, with the defining property that for any observable $f \in C^\infty(M)$,

$$\frac{d}{dt}\bigg|_{t=0} f \circ \phi^H_t = X_H(f) = \{f, H\}.$$

The operational characterization is "the derivative-along-the-flow operator", and the formal definition $\iota_{X_H}\omega = dH$ is the symplectic-geometric way of producing this derivative without specifying the flow first.

---

# Examples / Corollaries

**Is an instance: $X_H = (\partial H/\partial p)\partial_q - (\partial H/\partial q)\partial_p$ on $T^*\mathbb{R} = \mathbb{R}^2$.** For any $H(q, p)$, this is the Hamiltonian vector field for the canonical symplectic form $\omega = dp \wedge dq$. Verify: $\iota_{X_H}\omega = \iota_{(\partial_p H)\partial_q - (\partial_q H)\partial_p}(dp \wedge dq) = (\partial_p H)\,dp\wedge dq(\partial_q, \cdot) - (\partial_q H)\,dp\wedge dq(\partial_p, \cdot) = -(\partial_p H)\,dp - (\partial_q H)(-dq) = (\partial_q H)dq + (\partial_p H)dp = dH$. ✓

**Is an instance: the harmonic oscillator on $\mathbb{R}^2$.** For $H = \tfrac{1}{2}(q^2 + p^2)$, the Hamiltonian vector field is $X_H = p\,\partial_q - q\,\partial_p$. Hamilton's equations are $\dot q = p$, $\dot p = -q$, with solutions $q(t) = q_0 \cos t + p_0 \sin t$, $p(t) = p_0 \cos t - q_0 \sin t$ — rigid rotation of the $(q, p)$-plane.

**Is an instance: free particle in $\mathbb{R}^n$.** For $H = |p|^2/(2m) = \sum_i p_i^2/(2m)$ on $T^*\mathbb{R}^n$, the Hamiltonian vector field is $X_H = \sum_i (p_i/m)\partial_{q^i}$, giving straight-line motion $q(t) = q(0) + (p/m)t$, $p(t) = p(0)$ — Newton's first law.

**Is an instance: the geodesic Hamiltonian on $T^*M$.** For $H = \tfrac{1}{2}g^{ij}(q)p_ip_j$ on the cotangent bundle of a Riemannian manifold $(M, g)$, the Hamiltonian vector field is $X_H = g^{ij}p_j\partial_{q^i} - \tfrac{1}{2}(\partial_{q^k}g^{ij})p_ip_j\partial_{p_k}$. Its integral curves project to geodesics in $M$ — see [[Ex - Geodesic Flow on a Riemannian Manifold is Hamiltonian]].

**Is an instance (subtle): a constant $H$.** If $H$ is constant on $M$, then $dH = 0$, and $X_H = 0$. So constant Hamiltonians generate trivial dynamics. The kernel of $H \mapsto X_H$ on a connected $M$ is exactly the constants — adding a constant to $H$ does not change the dynamics, only the energy zero-point.

**Is NOT an instance: a vector field $X$ on a symplectic manifold whose flow does not preserve $\omega$.** The vector field $X = q\partial_q$ on $(\mathbb{R}^2, dp \wedge dq)$ scales $q$ exponentially in time, $\phi_t(q, p) = (e^t q, p)$, with $\phi_t^*\omega = e^t\, dp \wedge dq \neq \omega$. So $X$ is *not* Hamiltonian for any $H$. (Check: $\iota_X\omega = q\, dp$ is not closed — $d(q\, dp) = dq \wedge dp \neq 0$ — so $\iota_X\omega$ cannot equal $dH$ for any $H$.)

**Is NOT an instance: $X_f$ where $f$ has bad regularity.** Only smooth functions $H$ produce smooth vector fields $X_H$ via the construction; non-smooth Hamiltonians (e.g., piecewise-smooth $H$, or distributional $H$) require additional care.

**Corollary (energy conservation).** $X_H(H) = dH(X_H) = \omega(X_H, X_H) = 0$ by antisymmetry. So $H$ is constant along its own Hamiltonian flow — **energy is conserved**.

**Corollary (Hamiltonian flows preserve $\omega$).** $\mathcal{L}_{X_H}\omega = d\iota_{X_H}\omega + \iota_{X_H}d\omega = d(dH) + \iota_{X_H}(0) = 0$. So $(\phi^H_t)^*\omega = \omega$, i.e., Hamiltonian flows are symplectomorphisms. (See [[Thm - Hamiltonian Flows are Symplectomorphisms]].)

**Corollary (Hamiltonian flows preserve $\omega^n$).** From $\mathcal{L}_{X_H}\omega = 0$ and the Leibniz rule, $\mathcal{L}_{X_H}\omega^n = n\,\omega^{n-1} \wedge \mathcal{L}_{X_H}\omega = 0$. So the Liouville volume is preserved — **Liouville's theorem**, [[Thm - Liouville's Theorem on Phase Space Volume]].

**Corollary (linearity).** $X_{aH+bG} = aX_H + bX_G$ for constants $a, b$. The map $H \mapsto X_H$ is $\mathbb{R}$-linear.

**Corollary (commutator with Poisson bracket).** $[X_H, X_G] = -X_{\{H, G\}}$ (with our sign convention). So the Lie bracket of two Hamiltonian vector fields is again Hamiltonian, with Hamiltonian function (up to sign) the Poisson bracket of the two original Hamiltonians.

**Calibration check.** If you can do these three things, you have understood the definition. First, verify the coordinate formula by computing $\iota_{X_H}\omega$ for $X_H = (\partial_p H)\partial_q - (\partial_q H)\partial_p$ on $(\mathbb{R}^2, dp \wedge dq)$ and confirming it equals $dH$. Second, write down Hamilton's equations for $H = p^2/(2m) + V(q)$ on $T^*\mathbb{R}$ and identify them as Newton's second law $m\ddot q = -V'(q)$. Third, show explicitly that $H = q^2 + p^2$ is conserved along the flow $\phi_t(q, p) = (q\cos t + p\sin t, p\cos t - q\sin t)$ generated by the harmonic-oscillator vector field.

---

# Unlocked by This

> [!tip] Hamiltonian Group Actions and the Moment Map *(from Geometric Mechanics II)*
> When a Lie group $G$ acts on $(M, \omega)$ preserving $\omega$, each Lie algebra element $\xi \in \mathfrak{g}$ produces an **infinitesimal generator** $\xi_M$ — a vector field on $M$. If each $\xi_M$ is Hamiltonian — i.e., $\xi_M = X_{\mu^\xi}$ for some smooth function $\mu^\xi$ on $M$ — and the assignment $\xi \mapsto \mu^\xi$ is a $\mathfrak{g}$-equivariant Lie algebra homomorphism, then the assembled map $\mu : M \to \mathfrak{g}^*$ given by $\mu(p)(\xi) = \mu^\xi(p)$ is the **moment map** of the action. The components of $\mu$ are conserved quantities of any $G$-invariant Hamiltonian, providing the geometric content of **Noether's theorem**. For rotational symmetry $G = SO(3)$ on $T^*\mathbb{R}^3$, the moment map is the angular momentum vector.

> [!tip] Integrable Systems and Arnold–Liouville *(from Classical Mechanics)*
> A Hamiltonian system on a $2n$-dimensional symplectic manifold is **completely integrable** if it admits $n$ functionally independent Hamiltonians $f_1 = H, f_2, \dots, f_n$ in involution, $\{f_i, f_j\} = 0$. Their joint level sets $\{f_i = c_i\}$ are then $n$-dimensional submanifolds invariant under all the Hamiltonian flows $X_{f_i}$, and the **Arnold–Liouville theorem** says these (when compact and connected) are tori $T^n$ on which the dynamics becomes linear in suitable coordinates — the **action–angle variables**. Integrable systems are the rare class whose Hamiltonian flow can be solved exactly; **KAM theory** studies the persistence of these invariant tori under small perturbations of the Hamiltonian.

> [!tip] Symplectic Geometric Quantization *(from Mathematical Physics)*
> Geometric quantization is a program to assign a Hilbert space $\mathcal{H}$ and a representation of the Poisson algebra $(C^\infty(M), \{\cdot,\cdot\})$ on it, geometrically and functorially, to any symplectic manifold satisfying an integrality condition. The Hamiltonian vector field $X_H$ becomes (under quantization) the **Hamiltonian operator** $\hat H$ on $\mathcal{H}$, with the **classical-quantum correspondence** $X_H \leftrightarrow \hat H/i\hbar$. The integrality condition is the **Bohr–Sommerfeld condition** $[\omega/2\pi\hbar] \in H^2(M; \mathbb{Z})$, which restricts the values of $\hbar$ for which the quantization exists — the geometric origin of the quantum of action.
