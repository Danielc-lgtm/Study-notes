---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Complex Line Bundle"
  - "Def - Section of a Vector Bundle"
tags: [geometry, gauge-theory, hermitian, unitary]
---

# Notation

$E \to M$ is a smooth complex vector bundle of rank $K$ over a smooth manifold $M$ (see [[Def - Vector Bundle]] and [[Def - Complex Line Bundle]] for the $K = 1$ case). A hermitian metric is denoted $h$ or $\langle\cdot, \cdot\rangle$; the convention is **conjugate-linear in the first slot, complex-linear in the second** (the physicists' convention, opposite of some mathematicians' books). $|v|_h = \sqrt{h(v, v)}$ is the induced norm. $U(K)$ denotes the unitary group of $K \times K$ complex matrices satisfying $U^* U = I$, where $U^* = \bar U^T$ is the conjugate transpose; $\mathfrak{u}(K)$ is its Lie algebra of anti-hermitian matrices ($A^* = -A$). For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The motivating question is: **how do you measure the length of a section?** A complex vector bundle $E \to M$ comes with the structure of a complex vector space at each point, but with no canonical notion of magnitude — the fibre $E_p \cong \mathbb{C}^K$ is *abstractly* a vector space and has no preferred basis or inner product. For some purposes this is enough (the bundle by itself supports the differentiation theory of connections). But for quantum mechanics, where $|\psi|^2$ is a probability density that must integrate to $1$, "length squared" of a section is *essential*; without it, the basic interpretive structure of quantum mechanics is undefined.

A hermitian metric on $E$ is the choice of an inner product on every fibre, varying smoothly. The minimum it must do: (i) take two sections and produce a complex-valued function on $M$ (the pointwise inner product); (ii) be linear/conjugate-linear in the appropriate slots so it generalizes the complex inner product on $\mathbb{C}^K$; (iii) be *positive-definite* so $|v|^2 > 0$ for $v \ne 0$ and the norm is non-degenerate.

Why **sesquilinear** rather than $\mathbb{C}$-bilinear? Because $\mathbb{C}$-bilinear forms on a complex vector space are never positive: $\langle\lambda v, \lambda v\rangle = \lambda^2 \langle v, v\rangle$, and $\lambda^2$ can have any phase. To get $|v|^2 \in \mathbb{R}_{\geq 0}$ for *all* $v$ — including those obtained by multiplying by $i$ — you must conjugate one of the arguments: $\langle\lambda v, \lambda v\rangle = |\lambda|^2 \langle v, v\rangle$, which preserves positivity. Sesquilinearity is forced by positivity in the complex setting.

Why is **positive-definiteness** essential? Because we want a true *norm* $|v|$, not a quadratic form that may vanish or be negative. Drop positivity and you get **indefinite hermitian forms** — perfectly good objects (the metric of Lorentzian signature in relativity is the real analogue), but useless for the probability interpretation. Drop *definiteness* (allow $|v|^2 = 0$ for some $v \ne 0$) and you get a *degenerate* form, where the "null cone" of zero-length vectors contaminates analysis. For most physics applications we want strict positive-definiteness.

Why is **smooth variation in $p$** required? Because we want to integrate $|\psi|^2$ over $M$ to get a probability, and integration requires the integrand to be continuous (smooth, in our setting). Pointwise definitions of $h_p$ that jump from point to point would not produce a meaningful integral. Smoothness of $h$ ensures $p \mapsto h_p(\sigma(p), \tau(p))$ is a smooth function on $M$ for any smooth sections $\sigma, \tau$.

The Tightest formulation: $h$ is a *smooth section of $\overline{E^*} \otimes E^*$* satisfying conjugate-symmetry $\overline{h(v, w)} = h(w, v)$ and positivity $h(v, v) > 0$ for $v \ne 0$. The bar $\bar E$ denotes the *conjugate bundle* — same underlying real bundle but with $i$ acting as $-i$ — which is exactly what a sesquilinear form on $E$ is bilinear on.

The link to the **structure group reduction** is the payoff. In a general complex vector bundle, transition functions land in $\mathrm{GL}(K, \mathbb{C})$. Picking a hermitian metric and a *unitary* local frame (one where $h(e_\alpha, e_\beta) = \delta_{\alpha\beta}$ pointwise) constrains the transition functions between such frames: they must preserve the inner product, hence lie in $U(K) \subset \mathrm{GL}(K, \mathbb{C})$. Geometrically: a hermitian metric on $E$ is equivalent to a reduction of the structure group from $\mathrm{GL}(K, \mathbb{C})$ to $U(K)$. This is the structural fact that ties hermitian bundles to *unitary gauge theory* — the gauge group of the standard model, in the abstract.

What does this exclude? Without positivity, $h(v, v) = 0$ may occur for nonzero $v$, in which case $|v|^2$ has no probability interpretation. Without sesquilinearity, complex multiplication by $i$ ruins the positivity of "length squared". Without smoothness, no integration. The three axioms together force $h$ to be the *correct* generalisation to bundles of "Hermitian inner product on $\mathbb{C}^K$".

---

# The Definition

A **hermitian vector bundle** is a pair $(E, h)$ where $\pi : E \to M$ is a smooth complex vector bundle and

$$h = \{h_p : E_p \times E_p \to \mathbb{C}\}_{p \in M}$$

is a smoothly varying family of hermitian inner products on the fibres. Concretely, $h$ is required to be:

1. **Sesquilinear** (with the physicists' convention): for $u, v, w \in E_p$ and $\lambda \in \mathbb{C}$, $h_p(\lambda u + v, w) = \bar\lambda\,h_p(u, w) + h_p(v, w)$ and $h_p(u, \lambda v + w) = \lambda\,h_p(u, v) + h_p(u, w)$.
2. **Conjugate-symmetric**: $h_p(v, w) = \overline{h_p(w, v)}$.
3. **Positive-definite**: $h_p(v, v) \in \mathbb{R}_{>0}$ for all $v \in E_p \setminus \{0\}$ (and $h_p(0, 0) = 0$).
4. **Smooth**: for any smooth local sections $\sigma, \tau \in \Gamma(E|_U)$, the function $p \mapsto h_p(\sigma(p), \tau(p))$ is smooth on $U$.

A **local unitary frame** for $(E, h)$ on $U$ is a local frame $(e_1, \dots, e_K)$ with $h(e_\alpha, e_\beta) = \delta_{\alpha\beta}$ pointwise on $U$. Such frames exist locally (Gram-Schmidt applied to any local frame).

**Hermitian connection.** A connection $\nabla$ on $(E, h)$ is **hermitian** (or *metric-compatible*) if it satisfies

$$d\,h(\sigma, \tau) = h(\nabla\sigma, \tau) + h(\sigma, \nabla\tau)$$

for all $\sigma, \tau \in \Gamma(E)$ — equivalently, parallel transport preserves the hermitian inner product. In a local unitary frame, the connection 1-form matrix $\omega$ is **anti-hermitian**: $\omega^* = -\omega$, i.e., $\omega$ takes values in the Lie algebra $\mathfrak{u}(K)$.

**Structure-group reduction.** Equipping $E$ with a hermitian metric is equivalent to reducing the structure group from $\mathrm{GL}(K, \mathbb{C})$ to $U(K)$: transition functions between unitary frames are unitary matrices. For $K = 1$, this is the reduction from $\mathbb{C}^\times$ to $U(1)$.

---

# Categorical / Structural Definition

A hermitian metric on $E$ is a smooth section $h$ of the bundle $\overline{E^*} \otimes_{\mathbb{C}} E^*$ satisfying $h^* = h$ (under the canonical involution exchanging $\overline{E^*}$ and $E^*$) and positivity. Equivalently, a hermitian metric is a **vector-bundle isomorphism** $h : E \to \bar E^* = (\bar E)^*$ — sending $v \in E_p$ to the conjugate-linear functional $w \mapsto h_p(v, w)$. Positivity of $h$ corresponds to this isomorphism being an isomorphism (not merely an injection) and the induced sesquilinear form being positive.

In the principal-bundle picture, a hermitian metric on $E$ corresponds to a **reduction of structure group** from the frame bundle $\mathrm{Fr}(E)$ (a principal $\mathrm{GL}(K, \mathbb{C})$-bundle) to the **unitary frame bundle** $U(E)$ (a principal $U(K)$-bundle). This is one of the simplest examples of structure-group reduction — see [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the general theory.

The category of hermitian vector bundles over $M$ with metric-preserving isomorphisms is the category whose objects classify the topological types of $U(K)$-bundles on $M$; isomorphism classes are in bijection with $[M, BU(K)]$, where $BU(K)$ is the classifying space.

---

# Relate to Other Fields / Compression

A hermitian vector bundle is **"a complex vector bundle with a chosen probability measure on each fibre's unit sphere"** — concretely, with chosen inner products that distinguish a "unit sphere" $\{v : |v| = 1\}$ in each fibre.

**In Riemannian geometry**, the *real* analogue is a Riemannian metric on a real vector bundle — a smoothly varying positive-definite bilinear form. Riemannian metrics on $TM$ are how distances are measured on manifolds; hermitian metrics on complex bundles play the same role one rung up. The reduction of structure group is from $\mathrm{GL}(n, \mathbb{R})$ to $O(n)$ in the real case, from $\mathrm{GL}(K, \mathbb{C})$ to $U(K)$ in the complex case.

**In gauge theory and physics**, hermitian bundles with $U(K)$ structure group are the bundles on which unitary gauge fields live. For $K = 1$ this is electromagnetism (gauge group $U(1)$); for $K = 2$ with traceless connection it is part of the electroweak sector ($SU(2)$); for $K = 3$ it is the basis of QCD ($SU(3)$). The metric is what makes unitary the relevant symmetry: probability conservation in quantum mechanics demands evolution by *unitary* operators.

**In complex algebraic geometry**, hermitian metrics on holomorphic vector bundles are central — they connect topology (Chern classes), differential geometry (curvature), and complex analysis (vanishing theorems). The Kobayashi-Hitchin correspondence relates hermitian-Einstein metrics on stable holomorphic bundles to algebraic-geometric stability conditions.

**True name:** A hermitian vector bundle is **"a complex vector bundle equipped with the data needed to ask 'is this section unit-norm'?"**. Concretely, the data is an inner product per fibre, smoothly varying. The structure-group reduction $\mathrm{GL}(K, \mathbb{C}) \to U(K)$ is the technical face of the same fact: unitary transformations are exactly those preserving the inner product, so the bundle's symmetries are reduced to those that "preserve length".

---

# Examples / Corollaries

**Is an instance: Trivial hermitian bundle $M \times \mathbb{C}^K$.** With $h_p((p, v), (p, w)) = \bar v \cdot w$ (the standard hermitian inner product on $\mathbb{C}^K$). Trivially smooth. The trivial bundle is hermitian and any other hermitian structure on $M \times \mathbb{C}^K$ is conjugate to this one.

**Is an instance: Tangent bundle of a Kähler manifold.** On a Kähler manifold $X$, the (complexified) tangent bundle $T_X^{1, 0}$ — the $+i$-eigenspace of the almost-complex structure $J$ — is a holomorphic vector bundle. The Kähler metric makes it a *hermitian* bundle, and the Chern connection is the unique connection compatible with both the hermitian structure and the holomorphic structure. This is the natural setting of complex differential geometry — Calabi-Yau manifolds, Kähler-Einstein metrics, etc.

**Is an instance: The Hopf line bundle with its natural hermitian metric.** On the tautological line bundle $H \to \mathbb{CP}^n$, the fibre $H_{[v]} = \mathbb{C}v \subseteq \mathbb{C}^{n+1}$ inherits the hermitian metric of $\mathbb{C}^{n+1}$. This gives a canonical hermitian structure on $H$.

**Is an instance: Wave-function bundle in quantum mechanics.** Spacetime carries a hermitian complex line bundle $L$ on which the wave function $\psi$ of a charged particle is a section. The hermitian metric $h(\psi, \psi) = |\psi|^2$ is the probability density. Conservation of total probability requires the connection (electromagnetic potential) to be hermitian.

**Is NOT an instance: Lorentzian-signature "hermitian" bundle.** A sesquilinear form $h$ on $E$ that is *not* positive-definite — for instance, signature $(p, q)$ with $p + q = K$ — does not satisfy our positivity axiom. Such bundles arise (e.g., the spinor bundle on a Lorentzian spacetime), but they are *indefinite* hermitian bundles and require modified machinery.

**Is NOT an instance: A complex bundle without inner product structure.** Bare $E \to M$ without any chosen $h$. Such bundles exist (the cotangent bundle $T^{*1, 0}M$ of a complex manifold without a Kähler metric, etc.) but lack the structure needed to define unitary transformations or probability densities.

**Corollary (existence of hermitian metrics).** Every smooth complex vector bundle over a paracompact manifold admits a hermitian metric. Proof: in each trivializing patch $U_\alpha$ use the standard hermitian form on $\mathbb{C}^K$; given a [[Def - Partition of Unity on a Manifold|partition of unity]] $\{\rho_\alpha\}$, glue by $h = \sum_\alpha \rho_\alpha h_\alpha$. The sum is positive-definite since each $\rho_\alpha h_\alpha$ is positive semi-definite and at every $p$ at least one $\rho_\alpha(p) > 0$, making the sum positive-definite on the non-zero fibre.

**Corollary (structure-group reduction).** Choosing a hermitian metric is equivalent to choosing a reduction of the structure group from $\mathrm{GL}(K, \mathbb{C})$ to $U(K)$. The reduction does not change the topology of the bundle (since the inclusion $U(K) \hookrightarrow \mathrm{GL}(K, \mathbb{C})$ is a homotopy equivalence — $\mathrm{GL}(K, \mathbb{C})$ deformation-retracts onto $U(K)$ via polar decomposition), but it gives a preferred class of frames (the unitary ones).

**Corollary (Chern connection on holomorphic hermitian bundle).** On a holomorphic vector bundle $E \to X$ over a complex manifold $X$, equipped with a hermitian metric $h$, there is a *unique* connection $\nabla$ that is both hermitian (metric-compatible) and compatible with the holomorphic structure ($\nabla^{0,1} = \bar\partial_E$). This is the **Chern connection**, the central object of complex differential geometry.

**Calibration check.** (1) Verify that the standard inner product on $\mathbb{C}^K$ is conjugate-symmetric: $\overline{\bar v \cdot w} = v \cdot \bar w = \overline{\bar w \cdot v}$. (2) For the hermitian connection $\nabla\sigma = d\sigma + i A\sigma$ on a hermitian line bundle (with $A$ a real 1-form), verify metric compatibility: $d|\sigma|^2 = \overline{\nabla\sigma}\sigma + \bar\sigma\nabla\sigma = (d\bar\sigma - iA\bar\sigma)\sigma + \bar\sigma(d\sigma + iA\sigma) = d(\bar\sigma\sigma) = d|\sigma|^2$, automatic. (3) Identify the Lie algebra of $U(1)$ — answer: $\mathfrak{u}(1) = i\mathbb{R}$, the purely imaginary numbers, exactly the values a $U(1)$-connection 1-form can take.

---

# Unlocked by This

> [!tip] Reduction of Structure Group *(from Gauge Theory)*
> Choosing a hermitian metric on $E$ reduces the structure group from $\mathrm{GL}(K, \mathbb{C})$ to $U(K)$. More generally, "extra structure" on a bundle (orientation, spin structure, complex structure, symplectic structure) is precisely a **reduction of structure group**. The classification of which reductions are possible is governed by obstructions in cohomology — e.g., a real oriented bundle admits a spin structure iff the second Stiefel-Whitney class $w_2$ vanishes. See [[Gauge Theory II — Fibre Bundles, Principal Bundles, and Gauss–Bonnet]] for the principal-bundle formulation.

> [!tip] Hermitian-Einstein Metrics and the Kobayashi-Hitchin Correspondence *(from Complex Differential Geometry)*
> On a stable holomorphic vector bundle $E$ over a Kähler manifold, the existence of a **hermitian-Einstein metric** (one whose Chern-curvature is proportional to the Kähler form $\omega$) is equivalent to the algebraic-geometric notion of **slope stability**: $E$ admits a hermitian-Einstein metric iff every coherent subsheaf $F \subset E$ satisfies $\mu(F) \le \mu(E)$ for the slope $\mu = \deg/\mathrm{rank}$, with equality only when $F$ is a direct summand. This is the **Kobayashi-Hitchin / Donaldson-Uhlenbeck-Yau theorem**, one of the deepest results bridging complex algebraic geometry and gauge theory.
