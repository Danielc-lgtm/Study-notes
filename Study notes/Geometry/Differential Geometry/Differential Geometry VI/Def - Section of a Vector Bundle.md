---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Smooth Map between Manifolds"
  - "Def - Smooth Function on a Manifold"
  - "Def - The Smooth Functions Ring"
  - "Def - Module"
tags: [geometry, differential-geometry, bundles, sections]
---

# Notation

$\pi : E \to M$ is a smooth vector bundle of rank $k$ over a smooth manifold $M$ (see [[Def - Vector Bundle]]). A section is denoted $\sigma : M \to E$, with $\sigma(p) \in E_p$ for each $p \in M$. The space of smooth global sections is $\Gamma(E)$ or $\Gamma(M, E)$; for the tangent bundle, $\Gamma(TM) = \mathfrak{X}(M)$. The ring of smooth real-valued functions on $M$ is $C^\infty(M)$, see [[Def - The Smooth Functions Ring]]. The zero section is denoted $\sigma_0$ or just $0 : M \to E$, $0(p) = 0_p$, the zero vector of $E_p$.

---

# Axiom Motivation

A section is what becomes of "a smoothly varying field of vectors" once the vectors are required to live in fibre-dependent vector spaces. In ordinary multivariable calculus, a vector field on $\mathbb{R}^n$ is a function $\mathbf{F} : \mathbb{R}^n \to \mathbb{R}^n$ — the same target vector space $\mathbb{R}^n$ for every input point. On a manifold this breaks: tangent vectors at $p$ live in $T_pM$, tangent vectors at $q$ live in $T_qM$, and these are different vector spaces. So the right notion of "vector field on $M$" cannot be a function $M \to \text{(common target)}$; it must be a function that, at each $p$, lands in the fibre $E_p$ over $p$. The section construction is exactly this.

The defining condition $\pi \circ \sigma = \mathrm{id}_M$ — "$\sigma$ is a right inverse to the projection" — is what enforces this. For each $p \in M$, $\sigma(p)$ is an element of $E$ whose projection $\pi(\sigma(p))$ equals $p$, so $\sigma(p)$ must lie in $E_p$. The condition is the minimum needed to say "$\sigma$ chooses, for each $p$, an element of the fibre over $p$".

What is forced by demanding **smoothness** of $\sigma : M \to E$ rather than just continuity? Smoothness is what makes calculus on the bundle work. A smooth section can be differentiated (with a connection), integrated (on appropriate bundles), and combined with other smooth sections by smooth-function multiplication. Continuous-but-non-smooth sections are useful in some contexts — they form a sheaf and admit [[Def - Homotopy|homotopy]] classification — but they live in topological-bundle theory, not in smooth-bundle theory.

What is forced by demanding sections be **globally defined** on $M$? Many natural sections are not — vector fields with prescribed local behaviour, or local frames associated with charts, are intrinsically local. So the theory distinguishes **local sections** (defined on open $U \subseteq M$) from **global sections** (defined on all of $M$). Global sections form $\Gamma(E)$; local sections form the **sheaf** $\Gamma(\cdot, E)$ on $M$. Local sections always exist (from local frames); global sections may not. The question "does a global section with property $P$ exist?" is the central nontrivial question of bundle theory and has topological obstructions.

The deeper motivation is that the space $\Gamma(E)$ of smooth global sections is **not just a vector space but a module over $C^\infty(M)$**. The vector-space structure comes from pointwise addition and scalar multiplication by real numbers: $(\sigma + \tau)(p) := \sigma(p) + \tau(p)$ in $E_p$, $(c\sigma)(p) := c \cdot \sigma(p)$ for $c \in \mathbb{R}$. But there is more: for any smooth function $f \in C^\infty(M)$, the product $f \sigma$ is defined by $(f\sigma)(p) := f(p) \cdot \sigma(p)$, where $f(p) \in \mathbb{R}$ is a scalar that multiplies the vector $\sigma(p) \in E_p$. This is a $C^\infty(M)$-action on $\Gamma(E)$, satisfying all the module axioms (see [[Def - Module]]). The module structure is the richer algebraic content: it lets one talk about "linear combinations of sections with smooth-function coefficients", which is the natural framework for tensorial constructions and bundle maps.

What if we **strengthened** to require sections be bundle [[Def - Homomorphism|homomorphisms]] from the trivial bundle? A section can be reinterpreted as a bundle homomorphism $\mathbb{R} \to E$ over $M$ (where $\mathbb{R}$ denotes the trivial line bundle $M \times \mathbb{R}$), sending each $(p, 1)$ to $\sigma(p)$. This is a perfectly reasonable rephrasing — it shows that sections are "morphisms from the unit object" in the category of vector bundles — but it does not add new content, only a categorical perspective.

What if we **weakened** by dropping smoothness? Then we have rough sections (continuous or even discontinuous maps with $\pi \circ \sigma = \mathrm{id}$). These exist always (for instance the zero section is smooth, so smoothness alone is no constraint on existence); the question becomes whether smooth sections with prescribed properties exist. This is the foundational question of differential topology: the existence of a nowhere-vanishing smooth section is equivalent to the existence of a smooth section with extra structure, and obstructions live in characteristic classes.

In summary, three demands — the projection condition $\pi \circ \sigma = \mathrm{id}_M$ (which makes $\sigma(p)$ live in $E_p$), smoothness (which makes $\sigma$ amenable to calculus), and global-vs-local distinction (which separates trivial existence from substantive existence questions) — define the section concept, and the $C^\infty(M)$-module structure on $\Gamma(E)$ packages the algebraic content.

---

# The Definition

Let $\pi : E \to M$ be a smooth vector bundle. A **smooth global section** of $E$ is a smooth map $\sigma : M \to E$ such that
$$\pi \circ \sigma = \mathrm{id}_M.$$
Equivalently, for every $p \in M$, $\sigma(p) \in E_p$.

The set of smooth global sections is denoted $\Gamma(E)$. It carries:

- A real vector space structure under pointwise operations: $(\sigma + \tau)(p) := \sigma(p) + \tau(p)$ and $(c\sigma)(p) := c \cdot \sigma(p)$ for $c \in \mathbb{R}$.
- A $C^\infty(M)$-module structure: for $f \in C^\infty(M)$ and $\sigma \in \Gamma(E)$, the product $f\sigma \in \Gamma(E)$ is defined by $(f\sigma)(p) := f(p) \cdot \sigma(p)$, where the right-hand side uses the vector-space structure of $E_p$.

A **local section** of $E$ over an open set $U \subseteq M$ is a smooth map $\sigma : U \to E$ with $\pi \circ \sigma = \mathrm{id}_U$; equivalently, a global section of the restricted bundle $E|_U \to U$. The set of local sections is denoted $\Gamma(U, E)$ or $\Gamma(E|_U)$, and the assignment $U \mapsto \Gamma(U, E)$ is a sheaf of $C^\infty(M)$-[[Def - Module|modules]] on $M$.

The **zero section** is the smooth global section $\sigma_0(p) := 0 \in E_p$, where $0$ denotes the zero vector of $E_p$. It is the identity element of $\Gamma(E)$ under addition. The **support** of a section $\sigma$ is $\mathrm{supp}(\sigma) := \overline{\{p \in M : \sigma(p) \neq 0\}}$.

When $E = TM$ is the tangent bundle, $\Gamma(TM) = \mathfrak{X}(M)$ is the space of smooth vector fields on $M$. When $E = T^*M$ is the cotangent bundle, $\Gamma(T^*M) = \Omega^1(M)$ is the space of smooth $1$-forms on $M$. Other bundles give tensor fields, differential forms of higher degree, spinor fields, and so on.

---

# Relate to Other Fields / Compression

A section is the **bundle-theoretic version of a function**, generalizing $f : M \to \mathbb{R}$ (a "scalar field") to a map $\sigma : M \to E$ that takes values in fibres rather than in a fixed target. The trivial bundle case $E = M \times \mathbb{R}$ recovers ordinary smooth functions: a section of the trivial line bundle is the same as a smooth function $M \to \mathbb{R}$, via $f \leftrightarrow (p \mapsto (p, f(p)))$.

A section is also a **map of bundles over $M$**: the assignment $\sigma : M \to E$ is the same as a bundle homomorphism $M \times \mathbb{R} \to E$ from the trivial line bundle, given by $(p, c) \mapsto c \cdot \sigma(p)$. So sections are morphisms from the "unit" trivial line bundle in the category of vector bundles over $M$. This perspective is useful when comparing sections of different bundles by maps.

The Serre–Swan theorem completes the algebraic picture: **the functor $E \mapsto \Gamma(E)$ is an equivalence of categories between smooth vector bundles over $M$ and finitely generated projective $C^\infty(M)$-modules**. So bundle theory and the theory of projective modules over the smooth-function ring are formally the same subject. This is the bridge to non-commutative geometry: replacing $C^\infty(M)$ by a non-commutative ring gives "bundles" over non-commutative spaces, with sections defined algebraically as projective modules.

**True name:** the true name of a section is "**a smooth choice, at each point $p$ of $M$, of an element of the fibre $E_p$**". The technical condition $\pi \circ \sigma = \mathrm{id}_M$ is what makes "$\sigma(p) \in E_p$" hold; the smoothness condition is what makes "smooth choice" precise. In practice, one constructs sections by writing them in a local frame as $\sigma = f^i \sigma_i$ for smooth functions $f^i$, and verifies smoothness by checking that the $f^i$ are smooth.

A useful slogan: **a section is a global object whose existence may fail; a local section is a local object whose existence is automatic**. The whole nontrivial theory of bundles is about extending local sections to global ones, and the obstructions are topological.

---

# Examples / Corollaries

**Is an instance — the zero section.** For any vector bundle $E$, the map $\sigma_0(p) = 0 \in E_p$ is a smooth global section. Smoothness is checked in any local trivialization: in $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$, the zero section is $p \mapsto (p, 0)$, manifestly smooth. The zero section embeds $M$ as a submanifold of $E$.

**Is an instance — coordinate vector fields.** In a coordinate chart $(U, x^i)$ of $M$, the assignments $\partial/\partial x^i : U \to TM$ are smooth local sections of $TM$ over $U$. They form a local frame for $TM$, and every local vector field on $U$ has unique smooth components in this frame.

**Is an instance — coordinate covector fields.** Dually, the assignments $dx^i : U \to T^*M$ are smooth local sections of $T^*M$ over $U$, forming the dual local frame.

**Is an instance — angular velocity field on $S^1$.** The vector field $\partial/\partial\theta$ on $S^1$ is a nowhere-vanishing smooth global section of $TS^1$. Its existence shows $TS^1$ is trivial.

**Is an instance — global section of the trivial bundle = smooth function.** For $E = M \times \mathbb{R}^k$, a section $\sigma : M \to M \times \mathbb{R}^k$ with $\pi_1 \circ \sigma = \mathrm{id}$ has the form $\sigma(p) = (p, f(p))$ for a smooth function $f : M \to \mathbb{R}^k$. So $\Gamma(M \times \mathbb{R}^k) \cong C^\infty(M, \mathbb{R}^k)$.

**Is NOT an instance — a non-smooth assignment.** Define $\sigma : \mathbb{R} \to T\mathbb{R} = \mathbb{R} \times \mathbb{R}$ by $\sigma(x) = (x, |x|)$. This is continuous but not smooth at $x = 0$, so it is a continuous section but not a smooth one. It illustrates that smooth-section is a strictly stronger condition than continuous-section.

**Is NOT a section — a map $\sigma : M \to E$ that doesn't fibre-preserve.** Define $\sigma : \mathbb{R} \to T\mathbb{R} = \mathbb{R} \times \mathbb{R}$ by $\sigma(x) = (2x, 1)$. This is a smooth map, but $\pi \circ \sigma(x) = 2x \neq x$, so it is not a section. It fails the projection-compatibility condition.

**Is NOT generally a global section — a nowhere-vanishing section of $TS^2$.** The hairy ball theorem says no smooth global section of $TS^2$ is nowhere vanishing. Local nonvanishing sections exist trivially (any nonzero tangent vector at $p$ extends to a nonvanishing local section near $p$), but they cannot be patched together globally. This is one of the deepest theorems of the chapter, demonstrating that the global existence question for sections is topologically substantive.

**Corollary — $\Gamma(E)$ is a $C^\infty(M)$-module.** For $f, g \in C^\infty(M)$ and $\sigma, \tau \in \Gamma(E)$, the module axioms hold: $(f + g) \sigma = f\sigma + g\sigma$, $f(\sigma + \tau) = f\sigma + f\tau$, $(fg)\sigma = f(g\sigma)$, $1 \cdot \sigma = \sigma$. The verifications are pointwise.

**Corollary — $\Gamma(E)$ is a *free* $C^\infty(M)$-module when $E$ is trivial.** If $E = M \times \mathbb{R}^k$ with global frame $(e_1, \dots, e_k)$, then every section has a unique expression $\sigma = f^i e_i$ for $f^i \in C^\infty(M)$. So $\Gamma(E) \cong C^\infty(M)^k$ as a $C^\infty(M)$-module. For nontrivial bundles, $\Gamma(E)$ is projective but not free.

**Corollary — sections form a sheaf.** The assignment $U \mapsto \Gamma(U, E)$ is a sheaf of $C^\infty(U)$-modules on $M$. Restriction to smaller opens, gluing of locally-defined sections that agree on overlaps, and the sheaf axioms all hold automatically. This sheaf is locally free of rank $k$ — that is the sheaf-theoretic content of local triviality.

**Calibration check.** Verify that the zero section of any vector bundle is smooth by computing it in a local trivialization. Verify that $f\sigma + g\tau$ is a smooth global section whenever $f, g \in C^\infty(M)$ and $\sigma, \tau \in \Gamma(E)$. Express the coordinate frame $(\partial/\partial x^i)$ of $TU$ as a $C^\infty(U)$-basis for $\Gamma(TU)$, and convince yourself that every local vector field is a unique $C^\infty(U)$-linear combination of the coordinate vector fields.

---

# Unlocked by This

> [!tip] Local Frame and Local Trivialization Equivalence *(from this topic)*
> A local trivialization of $E$ over $U$ is equivalent to a choice of smooth local frame for $E$ over $U$ — see [[Def - Local Frame]] and [[Thm - Local Frames Span Sections]]. Sections in a frame are tuples of smooth functions, recovering ordinary multivariable calculus on each chart.

> [!tip] Tensor Field as Section of a Tensor Bundle *(from Differential Geometry VII)*
> A **$(p, q)$-tensor field** on $M$ is a smooth section of the bundle $T^{p,q}M := (TM)^{\otimes p} \otimes (T^*M)^{\otimes q}$ — the appropriate tensor power of $TM$ and $T^*M$. This realises all of multilinear algebra on manifolds as section theory of an appropriate vector bundle. The Riemannian metric is a $(0, 2)$-tensor; the Riemann curvature tensor is a $(1, 3)$-tensor; the stress-energy tensor in physics is a $(0, 2)$-tensor.

> [!tip] Differential Form as Section of a Form Bundle *(from Differential Geometry VIII)*
> A **differential $k$-form** on $M$ is a smooth section of the bundle $\Lambda^k T^*M$ — the $k$-th exterior power of the cotangent bundle. The space of $k$-forms is $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$, with $\Omega^0(M) = C^\infty(M)$ and $\Omega^1(M)$ the 1-forms of this chapter. The exterior derivative, wedge product, pullback, and integration all live natively on sections of these bundles.

> [!tip] Sheaf of Sections *(from Algebraic Geometry and Sheaf Theory)*
> The assignment $U \mapsto \Gamma(U, E)$ is a *sheaf* on $M$, locally free of rank $k$. In algebraic geometry, locally free sheaves of $\mathcal{O}_X$-modules over a scheme $X$ are precisely the algebraic analogue of vector bundles, and the entire theory of bundles transports to that setting. The Serre–Swan theorem realises smooth vector bundles as projective $C^\infty(M)$-modules, completing the dictionary between differential geometry and module theory.
