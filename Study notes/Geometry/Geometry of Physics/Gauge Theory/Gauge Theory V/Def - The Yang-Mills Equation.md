---
type: definition
subject: gauge-theory
prereqs:
  - "Def - The Yang-Mills Field Strength"
  - "Def - The Yang-Mills Action Functional"
  - "Def - Gauge-Covariant Derivative"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Notation

$(M, g)$ is an oriented 4-manifold with metric; $G$ a compact Lie group; $A$ a connection on a principal $G$-bundle with field strength $F$. The exterior covariant derivative on $\mathfrak{g}$-valued forms is $d_A\alpha = d\alpha + [\omega, \alpha]$ (or $d_A\alpha = d\alpha - iq[A, \alpha]$ in physics notation), where the bracket is the graded Lie bracket on $\mathfrak{g}$-valued forms. The Hodge star $\star : \Omega^k \to \Omega^{n-k}$ depends on the metric and orientation; on a 4-manifold, $\star\star = (-1)^{k(n-k)}\cdot(\text{sign}) = (\pm)$ on $k$-forms depending on signature.

The formal adjoint of $d_A$ with respect to the $L^2$ inner product is $d_A^* = (-1)^{\bullet}\star d_A\star$ (with sign depending on degree and signature). For 2-forms on a Riemannian 4-manifold, $d_A^* F = -\star d_A\star F$, so $d_A^* F = 0 \iff d_A\star F = 0$.

A current source $J \in \Omega^1(M; \operatorname{ad} P)$ is a $\mathfrak{g}$-valued 1-form on $M$.

Wider conventions are in [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons]].

---

# Axiom Motivation

The Yang–Mills equation $d_A\star F = 0$ is what one *gets* from the action principle applied to $S_{\text{YM}}$. The motivation question, then, is not "what should the equation be?" — the action principle answers that — but rather "what does the resulting equation mean physically and geometrically?". The answer breaks into three layers, each addressing a separate way to read the equation.

*Geometrically: the YM equation says the curvature is "co-closed" in the covariant sense.* The exterior covariant derivative $d_A$ is the natural differential operator on $\mathfrak{g}$-valued forms — the analogue of $d$ on ordinary forms, extended to handle the non-trivial transformation of the gauge potential. Its formal adjoint $d_A^*$ is the *covariant codifferential*, and $d_A^*F = 0$ says $F$ is in the kernel of this operator. In analogy with harmonic forms ($\Delta\omega = 0$ on a Riemannian manifold), Yang–Mills connections are "covariantly harmonic" at the level of $F$ — they minimise the action subject to the topological constraint of fixed Chern class. The pair (Bianchi: $d_A F = 0$, YM: $d_A^* F = 0$) is the gauge-theoretic version of "$F$ is harmonic", and together they say $F$ is in the kernel of the covariant Hodge Laplacian $\Delta_A = d_A d_A^* + d_A^* d_A$.

*Variationally: the YM equation says $A$ is a critical point of the action.* The first variation $\delta S_{\text{YM}}[A]\cdot\delta A = (\delta A, d_A^* F)$ vanishes for all compactly-supported $\delta A$ iff $d_A^* F = 0$. This is the Euler–Lagrange equation in functional-derivative language. It is a second-order non-linear PDE on the connection $A$: writing it out in components, $\partial_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = 0$, with the second-order structure visible in the $\partial^2 A$ implicit in $\partial F$, and the non-linearity in the $[A, F]$ commutator coupling.

*Physically (with source): the YM equation describes the response of the gauge field to a current.* With matter coupling, the equation becomes $d_A\star F = \star J$, equivalently $\partial_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = J^\nu$. This says the divergence of the field strength is the source current — a non-abelian generalisation of $\partial_\mu F^{\mu\nu} = J^\nu$, Maxwell's equations in tensor form. The new feature is the commutator term $-iq[A_\mu, F^{\mu\nu}]$, which makes the gauge field itself a source — *the Yang–Mills field carries Yang–Mills charge*. This is responsible for the non-linear self-interactions of QCD gluons and ultimately for confinement.

Why is the YM equation only first-order in $F$? Because $F$ is the first derivative of $A$ (plus $A^2$), so an equation containing $\partial F$ is second-order in $A$ — which is the standard order for a field equation governing wave propagation (compare $\partial^2\phi = 0$ for a scalar field, $\partial^2 g =$ source for Einstein's equation). Higher derivatives would mean higher-order field equations, generally ill-behaved.

Why is the YM equation paired with the Bianchi identity? Because both are first-order in $F$, but they encode different information: the Bianchi identity $d_A F = 0$ is an *algebraic identity* (it follows automatically from $F$ being a curvature, no dynamics involved), while the YM equation $d_A\star F = 0$ is a *dynamical equation* (it is satisfied only by critical points of the action). Together they form a system parallel to Maxwell's equations: Bianchi gives the "homogeneous" Maxwell equations $dF = 0$ (i.e., $\operatorname{div}\vec B = 0$, Faraday), and YM gives the "inhomogeneous" Maxwell equations $d\star F = \star J$ (i.e., Gauss, Ampère–Maxwell). The duality between $F$ and $\star F$ in 4D is responsible for this pairing.

What if one dropped the variational principle and just wrote down a first-order equation $d_A^* F = 0$? Nothing would change, because the variational principle is what *justifies* the equation. The point of starting from $S_{\text{YM}}$ rather than from the equation is that the action determines the equation, the equation determines the dynamics, and the dynamics determine the physics — all derivable from one functional. This is the lesson of Lagrangian field theory.

---

# The Definition

A connection $A$ on a principal $G$-bundle over an oriented 4-manifold $(M, g)$ is called a **Yang–Mills connection** if its field strength $F$ satisfies the **Yang–Mills equation**

$$d_A \star F = 0,$$

equivalently $d_A^* F = 0$, where $d_A^* = -\star d_A\star$ is the formal adjoint of the covariant exterior derivative. In components, this reads

$$\nabla_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = 0,$$

or equivalently $\partial_\mu(\sqrt{|g|}F^{\mu\nu}) - iq[A_\mu, F^{\mu\nu}]\sqrt{|g|} = 0$ in coordinates.

The Bianchi identity

$$d_A F = 0,$$

equivalently $\nabla_{[\mu}F_{\nu\rho]} - iq[A_{[\mu}, F_{\nu\rho]}] = 0$, holds for *every* connection (not just Yang–Mills ones) as a consequence of $F$ being the curvature of $A$ — it is an algebraic identity following from the Jacobi identity in the Lie algebra.

With a current source $J \in \Omega^1(M; \operatorname{ad} P)$, the **sourced Yang–Mills equation** reads

$$d_A \star F = \star J,$$

equivalently $\nabla_\mu F^{\mu\nu} - iq[A_\mu, F^{\mu\nu}] = J^\nu$. Charge conservation $d_A \star J = 0$ then follows automatically from applying $d_A$ to both sides and using $d_A^2 = [F, \cdot]$ plus the Bianchi identity.

**Equivalent characterisations:**
1. $A$ is a critical point of the action $S_{\text{YM}}[A] = -\tfrac12\int_M\operatorname{tr}(F\wedge\star F)$ under all compactly-supported variations $\delta A$.
2. The covariant codifferential $d_A^* F$ vanishes, equivalently $d_A\star F$ vanishes (on a Riemannian or Lorentzian 4-manifold).
3. The pair $(F, \star F) \in \Omega^2(M; \operatorname{ad} P) \times \Omega^2(M; \operatorname{ad} P)$ is *jointly* $d_A$-closed (Bianchi gives $d_AF = 0$, YM gives $d_A\star F = 0$).

---

# Categorical / Structural Definition

The Yang–Mills equation has a clean structural meaning in the framework of **infinite-dimensional symplectic geometry on the cotangent bundle of the moduli space of connections**. The space $\mathcal{A}/\mathcal{G}$ has a natural Kähler structure (in the appropriate setting), and the Yang–Mills functional is the Kähler potential of an associated Liouville structure. Critical points of $S_{\text{YM}}$ correspond to fixed points of the gauge-theoretic *moment map* $\mu(A) = d_A\star F$, and the YM equation $\mu(A) = 0$ is the **moment-map equation** for the gauge group action.

In another structural framing, the YM equation is the **harmonicity condition** for a connection: viewing $A$ as a "harmonic map" from $M$ into the classifying space $BG$, the YM equation is the analogue of the harmonic-map equation. This perspective makes manifest the analogy with: harmonic functions ($\Delta f = 0$), harmonic forms ($\Delta\omega = 0$), harmonic maps ($\Delta_{\text{map}}\phi = 0$), and Yang–Mills connections ($\Delta_A F = 0$) — all critical points of squared-norm energy functionals.

A third structural framing: the pair (Bianchi, YM) is the **second Maxwell pair**, generalising the two pairs of Maxwell's equations. In differential-form language, Maxwell's equations are $dF = 0$ (Bianchi: no magnetic monopoles, Faraday's law) and $d\star F = \star J$ (Gauss's law for $\vec E$, Ampère–Maxwell). The Yang–Mills equations are the non-abelian generalisation: $d_A F = 0$ and $d_A\star F = \star J$. The difference between the two pairs is the structure group ($U(1)$ vs general compact $G$) and the corresponding linear/non-linear nature of the equations.

---

# Relate to Other Fields / Compression

**The YM equation is the natural generalisation of the source-free Maxwell equations to non-abelian gauge groups.** For $G = U(1)$, the YM equation $d\star F = 0$ reduces to the two Maxwell equations involving $\vec E$ and $\vec B$ directly: $\operatorname{div}\vec E = 0$ and $\operatorname{curl}\vec B - \partial_t\vec E = 0$ (sourceless). Adding the Bianchi identity $dF = 0$ gives the other two: $\operatorname{div}\vec B = 0$ and $\operatorname{curl}\vec E + \partial_t\vec B = 0$. So the pair $(d_A F = 0, d_A\star F = 0)$ is *literally* the four Maxwell equations in differential-form language. The non-abelian generalisation keeps the same first-order PDE structure but acquires commutator terms $-iq[A, \cdot]$ that make the gauge field self-sourcing.

**It is also the variational equation of a Yang–Mills connection on any vector bundle**, not just over 4-manifolds. On a Riemannian $n$-manifold the equation $d_A\star F = 0$ is well-defined for any $n$, but the *conformal invariance* of the Yang–Mills action is special to $n = 4$. In other dimensions the action $\int|F|^2$ scales non-trivially under metric rescaling, and instanton-like scale-free solutions do not exist; in particular, finite-action solutions of YM on $\mathbb{R}^n$ for $n \neq 4$ either do not exist (for $n > 4$, by a scaling argument due to Jackiw–Rebbi) or are trivial. Four dimensions is the only dimension where instantons live.

**True name:** the YM equation is the *covariant codifferential of the curvature vanishes*. The operational form $d_A^* F = 0$ is what you use to argue from properties of $d_A^*$ (formal adjoint of $d_A$, etc.), to apply Hodge theory, and to see the parallel with harmonic forms. The form $d_A\star F = 0$ is operationally what you use to do component calculations and to recognise the equation as "Maxwell with covariant derivative". The two are equivalent on a 4-manifold (up to a sign that absorbs into conventions), and the choice of which to use depends on whether you want the Hilbert-space perspective or the differential-forms perspective.

---

# Examples / Corollaries

**Example 1 — Trivial connection.** $A = 0$ on the trivial bundle has $F = 0$, hence trivially satisfies $d_A\star F = d\star 0 = 0$. The flat connection is the absolute minimum of $S_{\text{YM}}$ (it has $S = 0$) and is automatically Yang–Mills.

**Example 2 — Pure-gauge connection.** $A = -(i/q)g^{-1}dg$ for a smooth $g : M \to G$ has $F = 0$ (cf. [[Def - The Yang-Mills Field Strength]] Example 2), hence is Yang–Mills. All flat connections are Yang–Mills, and they form the "trivial" critical stratum of $S_{\text{YM}}$.

**Example 3 — The BPST instanton.** The BPST $SU(2)$ connection $A = \frac{\rho^2}{\rho^2+r^2}g^{-1}dg$ on $\mathbb{R}^4$ satisfies $F = \star F$ (self-dual), and self-duality plus Bianchi gives $d_A\star F = d_A F = 0$ — it is Yang–Mills. This is the prototype of a non-trivial Yang–Mills solution and the building block for all higher-charge instantons.

**Example 4 — Self-dual and anti-self-dual connections.** Any connection with $F = \pm\star F$ on an oriented Riemannian 4-manifold is automatically Yang–Mills: applying $d_A$ to $\star F = \pm F$ gives $d_A\star F = \pm d_A F = 0$ by Bianchi. This is the central observation that converts the second-order YM PDE into the first-order self-duality equation, drastically simplifying the analysis (cf. [[Thm - Self-Dual Connections Solve Yang-Mills Automatically]]).

**Non-example — A general connection with $\delta S_{\text{YM}}/\delta A \neq 0$.** Take $G = U(1)$ on $\mathbb{R}^4$ with $A = (x^2)\,dx^0$. Then $F = dA = 2x\,dx^1\wedge dx^0$, and $\star F = 2x\,dx^2\wedge dx^3$, so $d\star F = 2\,dx^1\wedge dx^2\wedge dx^3 \neq 0$. This connection is *not* Yang–Mills — it does not satisfy the field equation, and it is not a critical point of the Maxwell action.

**Calibration check.** A reader who has internalised the definition should be able to: (a) verify directly that the abelian Coulomb potential $A_0 = q/(4\pi r)$ on $\mathbb{R}^3 \times \mathbb{R}$ satisfies the Yang–Mills equation with a $\delta$-function source at the origin; (b) write down the YM equation explicitly in components for $G = SU(2)$ and identify the cubic and quartic self-interaction terms; (c) prove charge conservation $d_A\star J = 0$ from the sourced YM equation via $d_A^2\star F = [F, \star F]$ plus the Bianchi identity — and explain why this *does* vanish even though $d_A^2 \neq 0$ in general.

---

# Unlocked by This

> [!tip] Hitchin's Equations *(from Gauge Theory and Algebraic Geometry)*
> Dimensional reduction of the self-dual Yang–Mills equation $F = \star F$ from $\mathbb{R}^4$ to a Riemann surface $\Sigma^2 \times \mathbb{R}^2$ (assuming translation invariance in the two extra directions) produces **Hitchin's equations** $F_A + [\Phi, \Phi^*] = 0$ and $d_A\Phi = 0$ for a pair $(A, \Phi)$ of a connection and a "Higgs field" $\Phi \in \Omega^{1,0}(\Sigma; \operatorname{ad} P_{\mathbb{C}})$. The moduli space $\mathcal{M}_H(\Sigma, G)$ of solutions, modulo gauge equivalence, has rich structure: it carries a hyperkähler metric, a Hitchin integrable system, and a remarkable bijection (the **non-abelian Hodge correspondence**) with the moduli space of representations $\pi_1(\Sigma) \to G_{\mathbb{C}}$. This is one of the most beautiful objects in modern geometry and the starting point for the **geometric Langlands programme**.

> [!tip] The Atiyah–Bott Fixed-Point Formula and Equivariant Cohomology *(from Algebraic Topology)*
> Atiyah and Bott (1982) applied **equivariant cohomology** and a fixed-point formula to the Yang–Mills functional on the space of connections over a Riemann surface, computing the cohomology of the moduli space $\mathcal{M}_{\text{YM}}(\Sigma, G)$ of Yang–Mills connections in terms of the cohomology of the classifying space $BG$ and the Morse theory of $S_{\text{YM}}$. This work established **equivariant cohomology** as a major tool in mathematical physics, opened the door to the computation of Yang–Mills moduli space topology for any compact group $G$, and provided the template for later **localisation formulas** in supersymmetric gauge theory (Witten, Nekrasov) that compute non-perturbative gauge-theory partition functions exactly.
