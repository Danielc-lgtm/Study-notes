---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Lie-Algebra-Valued Differential Form"
  - "Def - The Maurer-Cartan Form"
tags: [geometry, gauge-theory, principal-bundles, gauge-potentials]
---

# Notation

$P \to M$ is a principal $G$-bundle with right action $R_g$, $\omega \in \Omega^1(P; \mathfrak{g})$ a [[Def - Connection 1-Form on a Principal Bundle|connection 1-form]], and $s : U \to P$ a smooth **local section** on an open set $U \subseteq M$ — that is, $\pi \circ s = \mathrm{id}_U$. We write $A := s^*\omega \in \Omega^1(U; \mathfrak{g})$ for the local gauge potential. When several sections $s_\alpha, s_\beta$ are in play, the corresponding gauge potentials are $A_\alpha, A_\beta$, and the transition function is $g_{\alpha\beta} : U_\alpha \cap U_\beta \to G$ defined by $s_\beta = s_\alpha \cdot g_{\alpha\beta}$.

---

# Axiom Motivation

A connection 1-form $\omega$ on a principal bundle $P \to M$ lives on the *total space* $P$, which makes it geometrically invariant but computationally inconvenient: we usually want to express the connection as a 1-form on the *base* $M$, in terms of local coordinates and a basis of $\mathfrak{g}$. The local connection 1-form (or **gauge potential**, the physics name) is exactly this: the pullback of $\omega$ to the base via a local section.

The construction is forced. Given a local section $s : U \to P$, the pullback $s^*\omega \in \Omega^1(U; \mathfrak{g})$ is a $\mathfrak{g}$-valued 1-form on the open set $U$. This is the gauge potential. The reasons for this definition:

**(i) It lives on $M$, not on $P$.** Once a section is chosen, the gauge potential is an object on the base — directly comparable to the matter fields (which are sections of associated bundles, and locally just $V$-valued functions on $M$). In physics, the gauge potential $A_\mu$ appears in equations of motion alongside matter fields $\psi(x)$, both as functions on spacetime — this is possible because both are local expressions on $M$, not global objects on $P$.

**(ii) It depends explicitly on the section.** Different sections give different gauge potentials. This is the *gauge freedom* of physics: the gauge potential is not invariantly defined on the base, only the underlying connection $\omega$ on the total space is. The freedom of section choice is the geometric content of gauge invariance.

**(iii) It transforms by the gauge transformation law.** Two sections $s_\alpha, s_\beta$ over the same open set are related by $s_\beta = s_\alpha \cdot g$ for some $g : U \to G$. The corresponding gauge potentials are related by $A_\beta = g^{-1}A_\alpha g + g^{-1}dg$ — the **gauge transformation law**, derived in [[Thm - Gauge Transformation Law for Local Connection 1-Forms]]. This law is the global content of the local-section freedom, and it is what makes "gauge invariance" precise: physical observables must be functionals of $A$ that are invariant under this transformation.

**(iv) On a trivialising open cover, the collection $\{A_\alpha\}$ plus transition data $\{g_{\alpha\beta}\}$ is equivalent to the connection $\omega$ on $P$.** This is the *cocycle description* of a connection: the local gauge potentials and the transition functions, together with the cocycle condition $g_{\alpha\beta}\,g_{\beta\gamma} = g_{\alpha\gamma}$ on triple overlaps, recover $\omega$ completely. So physicists who "only ever see the gauge potential" are not missing anything — they have full access to $\omega$ through the cocycle data, even though they may not phrase it this way.

What if we tried to define a single global gauge potential? On a non-trivial bundle this is impossible: a global gauge potential would require a global section $s : M \to P$, and the existence of such a section is *exactly* the condition that $P$ is trivial as a principal bundle. Non-trivial bundles — Dirac monopoles, instantons, twisted spinor bundles — have no global section, so the gauge potential exists only locally. This is the geometric origin of the *Dirac string* in the monopole calculation: one tries to write a global gauge potential, and the inevitable failure on a hemisphere is the string of singularity.

Why is the gauge potential *not* a tensor on $M$? Because of the inhomogeneous term $g^{-1}dg$ in its transformation law. A tensor would transform homogeneously under the gauge action; the gauge potential picks up the Maurer-Cartan form of the gauge transformation, which is an exact 1-form but not zero. The non-tensorial character is what allows the gauge potential to encode "how to differentiate covariantly" — see the [[Thm - Principal Connection Induces a Connection on Every Associated Bundle|induced connection]] formula $\nabla = d + d\rho(A)$, where $A$ must transform non-tensorially for $\nabla\psi$ to transform as a section.

The naming "gauge potential" comes from electromagnetism, where the 4-potential $A_\mu$ is the gauge potential of the $U(1)$-connection on a $U(1)$-principal bundle over spacetime. The pre-Yang-Mills name "potential" is preserved because $A$ literally is the "vector potential" that physicists have used since Maxwell — Yang and Mills generalised to non-abelian $G$, but kept the language.

---

# The Definition

Let $P \to M$ be a principal $G$-bundle with connection 1-form $\omega \in \Omega^1(P; \mathfrak{g})$, and let $s : U \to P$ be a smooth local section over an open set $U \subseteq M$.

The **local connection 1-form** (also called the **gauge potential** in physics) associated to the section $s$ is
$$
A := s^*\omega \in \Omega^1(U; \mathfrak{g}).
$$
In components, for a basis $\{E_R\}$ of $\mathfrak{g}$ and local coordinates $(x^\mu)$ on $U$:
$$
A = E_R \otimes A^R_\mu(x)\,dx^\mu = A^R_\mu(x)\,E_R \otimes dx^\mu.
$$
In matrix-group convention (when $\mathfrak{g}$ is a matrix Lie algebra), $A$ is a matrix of ordinary 1-forms, and the formula reads $A = A_\mu(x)\,dx^\mu$ where each $A_\mu(x)$ is an element of $\mathfrak{g}$ (a matrix).

**Gauge transformation law** (proved as [[Thm - Gauge Transformation Law for Local Connection 1-Forms]]): for two sections $s_\alpha, s_\beta$ over $U$ related by $s_\beta(x) = s_\alpha(x) \cdot g(x)$ with $g : U \to G$ smooth, the corresponding gauge potentials satisfy
$$
A_\beta = g^{-1} A_\alpha g + g^{-1}dg.
$$
The right-hand side is the **gauge transformation** of $A_\alpha$ by $g$. The inhomogeneous term $g^{-1}dg$ is the pullback $g^*\theta_G$ of the [[Def - The Maurer-Cartan Form|Maurer-Cartan form]] along $g : U \to G$.

**Cocycle data:** given a trivialising open cover $\{U_\alpha\}$ of $M$ with sections $s_\alpha : U_\alpha \to P$ and transition functions $g_{\alpha\beta} : U_\alpha \cap U_\beta \to G$ (with $s_\beta = s_\alpha \cdot g_{\alpha\beta}$), the collection $\{A_\alpha\}_\alpha$ together with $\{g_{\alpha\beta}\}_{\alpha\beta}$ satisfying $A_\beta = g_{\alpha\beta}^{-1}A_\alpha g_{\alpha\beta} + g_{\alpha\beta}^{-1}dg_{\alpha\beta}$ on overlaps is equivalent to the global connection 1-form $\omega$ on $P$.

The local **curvature** is $F = dA + \tfrac{1}{2}[A, A] = s^*\Omega$, where $\Omega$ is the curvature 2-form on $P$. See [[Def - Curvature 2-Form on a Principal Bundle]] and [[Thm - Cartan Structural Equation for Principal Connections]].

---

# Relate to Other Fields / Compression

In **electromagnetism**, the local gauge potential of a $U(1)$-connection is exactly the electromagnetic 4-potential $A_\mu(x)\,dx^\mu$, with $A_\mu$ real-valued (or $i$-times-real, depending on convention — physicists often absorb the $i$ from $\mathfrak{u}(1) = i\mathbb{R}$ into the definition). The gauge transformation $A \mapsto A + d\chi$ for a smooth function $\chi : U \to \mathbb{R}$ is the abelian special case of the general law: with $g = e^{i\chi}$, $g^{-1}dg = i d\chi$ and $g^{-1}A g = A$ (since $U(1)$ is abelian), giving $A_\beta = A_\alpha + i d\chi$ — same up to the $i$.

In **Yang-Mills theory**, the local gauge potential of an $SU(N)$-connection is the matrix-valued $A_\mu = A^a_\mu\,T_a$, where $T_a$ are the generators of $\mathfrak{su}(N)$ in some basis (the Gell-Mann matrices for $SU(3)$, e.g.). For $SU(3)$ this gives the eight gluon fields $A^a_\mu$ of QCD; for $SU(2) \times U(1)$ the three $W$ fields plus one $B$ field of the electroweak theory.

In **Riemannian geometry**, the local gauge potential of the Levi-Civita connection on the orthonormal frame bundle is the matrix of Cartan **connection 1-forms** $\omega^a{}_b$ — an $\mathfrak{o}(n)$-valued 1-form, with values in antisymmetric matrices. The components $\omega^a{}_b = \Gamma^a_{bc}\,\sigma^c$ are determined by the Christoffel symbols in the chosen frame. See [[Riemannian Geometry I — Connections and Covariant Differentiation|RG I §1.3]] for the Cartan structural equation perspective.

**True name:** the local gauge potential is *the pullback of the principal connection along a local section, equivalently a $\mathfrak{g}$-valued 1-form on $U$ in a fixed gauge*. The operational picture: $A$ is "the connection in some particular gauge", with the gauge specified by the section $s$. Physicists work in a fixed gauge (Lorenz, Coulomb, axial, light-cone, ...) and never explicitly choose a section, because the gauge choice *is* the section choice.

---

# Examples / Corollaries

**Example (canonical gauge potential on the trivial bundle).** For $P = M \times G$ with the canonical flat connection $\omega = \mathrm{pr}_G^*\theta_G$, and the canonical section $s : M \to M \times G$, $x \mapsto (x, e)$, the gauge potential is $A = s^*\omega = s^*\mathrm{pr}_G^*\theta_G = (\mathrm{pr}_G \circ s)^*\theta_G = e^*\theta_G$ — the pullback of the Maurer-Cartan form to a point. But $e^*\theta_G = 0$ because $\theta_G$ vanishes at the identity (the Maurer-Cartan form acts as the identity on $T_e G = \mathfrak{g}$, so on a 0-dimensional tangent space it is zero). So $A = 0$ in the canonical gauge of the trivial flat connection — the gauge potential vanishes, as expected.

**Example (gauge potential of the Dirac monopole).** On $S^2 = \mathbb{CP}^1$ with the Hopf bundle $S^3 \to S^2$ (a non-trivial $U(1)$-bundle), the standard $U(1)$-connection has gauge potential, in the northern hemisphere chart (using spherical coordinates $(\theta, \varphi)$ with $0 < \theta < \pi$, $\theta = 0$ excluded),
$$
A_N = \frac{ig}{4\pi}(1 - \cos\theta)\,d\varphi,
$$
where $g$ is the magnetic charge. In the southern hemisphere chart,
$$
A_S = -\frac{ig}{4\pi}(1 + \cos\theta)\,d\varphi.
$$
On the overlap (the equator minus poles), $A_N - A_S = \frac{ig}{2\pi}\,d\varphi$, which is the gauge transformation by $g^{-1}dg$ for $g = e^{ig\varphi/(2\pi)}$ — a well-defined smooth $U(1)$-valued function on the overlap iff $g$ is a (real-valued) integer multiple of $2\pi/e$ for unit charge $e$. This is **Dirac's quantisation condition** for magnetic charge.

**Example (gauge potential in Lorenz gauge).** For electromagnetism in Minkowski space, the **Lorenz gauge** $\partial_\mu A^\mu = 0$ is a constraint that picks out a specific section, modulo a residual gauge freedom (transformations by harmonic $\chi$, $\Box\chi = 0$). Within Lorenz gauge, the wave equation $\Box A_\mu = j_\mu$ has a particularly simple form. The **Coulomb gauge** $\nabla \cdot \mathbf{A} = 0$ is another choice, useful for static problems. Each gauge is a different section choice, with corresponding gauge potential.

**Is NOT an instance:** the global connection 1-form $\omega$ on $P$ is *not* a gauge potential — it lives on the total space, not the base. The gauge potential is its pullback under a section.

**Is NOT an instance:** the field strength $F = dA + \tfrac{1}{2}[A, A]$ is *not* a gauge potential — it is the *curvature*, a 2-form, not a 1-form. The field strength transforms in the adjoint representation ($F' = g^{-1}Fg$, no inhomogeneous term), while $A$ transforms inhomogeneously.

**Is NOT an instance:** for a non-trivial bundle, there is no global gauge potential — only local ones on each trivialising chart, glued by the gauge transformation law on overlaps. This is what distinguishes the local gauge potential from a 1-form section of $\mathrm{Ad}\,P$ (which *does* exist globally, but is not a gauge potential — it is the *difference* of two gauge potentials).

**Corollary.** The gauge potential of a connection in any gauge is *not* a tensor on $M$ — it transforms inhomogeneously. The *difference* of two gauge potentials $A_1 - A_2$ (with respect to the same section but two different connections) *is* a tensor — a 1-form section of $\mathrm{Ad}\,P$. This is the affine structure of the space of connections (see [[Ex - The Affine Space of Connections on a Principal Bundle]]).

**Corollary.** Under an *infinitesimal* gauge transformation $g = \exp(\varepsilon\lambda)$ with $\lambda : U \to \mathfrak{g}$, the gauge potential transforms as
$$
\delta A = A_\beta - A_\alpha \approx -\varepsilon\,d\lambda - \varepsilon\,[A, \lambda] + O(\varepsilon^2),
$$
or equivalently $\delta A = -d_A\lambda$ where $d_A$ is the [[Def - Exterior Covariant Derivative on Associated Bundles|exterior covariant derivative]] on $\mathrm{Ad}\,P$. This is the standard "infinitesimal gauge transformation" formula in physics.

**Calibration check.** If you have understood the definition, you should be able to: (i) compute the pullback $s^*\omega$ explicitly for the trivial flat connection on $M \times G$ and the canonical section, and verify it is zero; (ii) write down the gauge potential of the Dirac monopole in the northern hemisphere chart and verify that its $d\varphi$-component is $(1 - \cos\theta)$ times a constant (the magnetic charge); (iii) explain in one sentence why the gauge potential is *not* invariantly defined on $M$ — answer: it is the pullback of a global object on $P$ along a non-canonical local section, so different sections give different potentials related by the gauge transformation law.

---

# Unlocked by This

> [!tip] Gauge Transformation Law *(from Gauge Theory III)*
> The fundamental law relating two gauge potentials for the same connection: $A_\beta = g^{-1}A_\alpha g + g^{-1}dg$. This is derived in [[Thm - Gauge Transformation Law for Local Connection 1-Forms]] and is the master formula of all gauge theory — it explains why the gauge potential is not a tensor, why the field strength is, and why gauge invariance is a redundancy in description.

> [!tip] Local Field Strength *(from Gauge Theory III)*
> The local field strength is $F = dA + \tfrac{1}{2}[A, A]$, the pullback of the curvature 2-form $\Omega$ on $P$ along the section $s$. Under gauge transformations, $F$ transforms in the adjoint representation: $F_\beta = g^{-1}F_\alpha g = \mathrm{Ad}_{g^{-1}}F_\alpha$. See [[Def - Curvature 2-Form on a Principal Bundle]] and [[Thm - Cartan Structural Equation for Principal Connections]].

> [!tip] Wilson Loops and Path-Ordered Exponentials *(from Gauge Theory)*
> The holonomy of a connection around a closed loop $\gamma : S^1 \to M$ (parallel transport once around $\gamma$) is given by the **path-ordered exponential**
> $$ W(\gamma) = \mathcal{P}\exp\left(-\oint_\gamma A\right), $$
> a group-valued function of the loop. The trace $\mathrm{tr}_R W(\gamma)$ in any representation $R$ is the **Wilson loop** in representation $R$ — a gauge-invariant observable that does not require a connection 1-form on the base (which need not exist globally). Wilson loops are the natural observables of non-abelian gauge theory and are central to lattice gauge theory and the analysis of confinement.

> [!tip] Gribov Ambiguity *(from Gauge Theory Quantisation)*
> Non-abelian gauge-fixing is *non-trivial*: there is no smooth global slice through the orbits of the gauge group action on the space of connections. This is the **Gribov ambiguity**: the gauge-fixing condition (e.g., Lorenz gauge) is satisfied by multiple gauge-inequivalent gauge potentials in each orbit, in a fundamental obstruction to a clean Lagrangian formulation of non-abelian gauge theory at the quantum level. The ambiguity is geometric — it reflects the topology of the moduli space $\mathcal{A}/\mathcal{G}$ of connections modulo gauge transformations.
