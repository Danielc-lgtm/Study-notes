---
type: definition
subject: differential-geometry
prereqs:
  - "Def - The Tangent Space"
  - "Def - Vector Bundle"
  - "Def - Dual Space"
  - "Def - Dual Basis"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, cotangent, dual]
---

# Notation

$M$ is a smooth manifold of dimension $n$. For $p \in M$, $T_pM$ is the tangent space at $p$ (see [[Def - The Tangent Space]]). The cotangent space at $p$ is denoted $T_p^*M$ or $(T_pM)^*$ — they mean the same thing — and elements are called **covectors** at $p$, written $\omega_p, \eta_p, \dots$. The cotangent bundle is denoted $T^*M = \bigsqcup_{p \in M} T_p^*M$, with projection $\pi : T^*M \to M$, $\pi(\omega_p) = p$. In a coordinate chart $(U, x^i)$, the coordinate covector fields $dx^1, \dots, dx^n$ form the dual basis to the coordinate vector fields $\partial/\partial x^1, \dots, \partial/\partial x^n$ at each point — $dx^j(\partial/\partial x^i) = \delta^j_i$.

This is a **compound page**: it defines two interlocking notions — the cotangent space at a point and the cotangent bundle on a manifold — because they are introduced together and neither is fully usable without the other.

---

# Axiom Motivation

The cotangent space exists for one reason: **tangent vectors deserve to be measured**. A tangent vector at $p$ is, intrinsically, a directional derivative at $p$ acting on smooth functions — see [[Def - The Tangent Space]]. Its content is to assign a number $v(f) \in \mathbb{R}$ to each smooth function $f$. So tangent vectors are themselves "measurements of functions". The *dual* construction asks: what are the natural measurements of tangent vectors?

The answer is forced by linearity. A measurement of tangent vectors should be a function $T_pM \to \mathbb{R}$, and the natural class is the **linear** functions — those satisfying $\omega(v + w) = \omega(v) + \omega(w)$ and $\omega(cv) = c \omega(v)$ for $v, w \in T_pM$ and $c \in \mathbb{R}$. Linear measurements are the simplest class of measurements that respect the vector-space structure of $T_pM$, and they are the building blocks for every other linear-algebraic construction at $p$. So the cotangent space at $p$ is exactly $T_p^*M := \mathcal{L}(T_pM, \mathbb{R})$ — the space of linear functionals on $T_pM$, the dual vector space in the sense of [[Def - Dual Space]].

The cotangent bundle exists for a different reason: **manifold theory needs a home for smoothly varying covectors**. A covector field on $M$ — a smooth choice of $\omega_p \in T_p^*M$ for each $p$ — is the natural integrand of a line integral, the natural target of the differential operator $d$ on functions, and the natural object that pulls back along smooth maps. But the cotangent vectors $\omega_p$ for different $p$ live in different vector spaces ($T_p^*M$ varies with $p$), so a "field of covectors" is not a function with a fixed target. The cotangent bundle is the bundle whose sections are exactly these fields.

The construction follows the universal pattern of [[Def - Vector Bundle|vector bundle]]: the total space is the disjoint union $T^*M = \bigsqcup_p T_p^*M$; the projection sends $\omega_p \in T_p^*M$ to $p$; the smooth structure is forced by the requirement that coordinate covector fields $dx^i$ be smooth sections. The local trivializations come from coordinate charts on $M$: a chart $(U, \varphi)$ gives a local trivialization of $T^*M|_U$ via the dual coordinate basis.

What is forced by demanding $T^*M$ be the bundle whose **fibre at $p$ is $T_p^*M$**? This is the operational definition: the fibre records the local linear-algebra data at $p$. Demanding the fibre be the dual ensures that sections (covector fields) are exactly the objects we need — linear functionals on tangent vectors at each point.

What is forced by demanding the bundle structure be **smooth**? Smoothness of the bundle ensures that smoothness of sections makes sense. The local trivializations from charts must be [[Def - Diffeomorphism|diffeomorphisms]] (not just bijections), so the inverse-transpose Jacobians of coordinate transitions must be smooth on overlaps — and they are, because the original Jacobians are smooth and matrix inversion-and-transposition is smooth on $\mathrm{GL}(n, \mathbb{R})$.

What is forced by demanding the **dual coordinate vector fields $dx^i$** be smooth sections? This is the consistency requirement that aligns the cotangent bundle with the chart-induced structure on $TM$. In any chart, $\partial/\partial x^i$ are smooth sections of $TM$, and by duality $dx^j$ defined by $dx^j(\partial/\partial x^i) = \delta^j_i$ should be smooth sections of $T^*M$. The smooth structure on $T^*M$ is the *unique* one for which this holds (see [[Thm - The Cotangent Bundle is a Smooth Manifold]]).

What if we **strengthened** by demanding the cotangent bundle be globally trivial? On a manifold like $S^2$ the tangent bundle is nontrivial, so by duality the cotangent bundle is also nontrivial — demanding global triviality would exclude such manifolds. Local triviality is the strongest condition compatible with the interesting examples.

What if we **weakened** by allowing arbitrary linear functionals (not just smooth)? Then sections would be merely "measurable choices of covectors" — useful in distributional analysis (sections of $T^*M$ in the sense of distributions are forms with distributional coefficients), but losing the smooth-differential-geometry framework.

---

# The Definition

**The cotangent space.** Let $M$ be a smooth manifold and $p \in M$. The **cotangent space** at $p$ is
$$T_p^*M := (T_pM)^* = \mathcal{L}(T_pM, \mathbb{R}),$$
the vector space of all linear functionals $\omega : T_pM \to \mathbb{R}$, with pointwise vector-space operations: $(\omega + \eta)(v) := \omega(v) + \eta(v)$, $(c \omega)(v) := c \omega(v)$. The elements of $T_p^*M$ are called **covectors** (or **tangent covectors**) at $p$. By [[Thm - Dimension of Dual Space|the dimension theorem for the dual space]], $\dim T_p^*M = \dim T_pM = n = \dim M$.

In a coordinate chart $(U, \varphi)$ with coordinates $x^1, \dots, x^n$ around $p$, the **coordinate covectors** at $p$ are the elements $dx^1|_p, \dots, dx^n|_p \in T_p^*M$ defined by
$$dx^j|_p \left( \frac{\partial}{\partial x^i}\bigg|_p \right) = \delta^j_i = \begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases},$$
the [[Def - Dual Basis|dual basis]] to the coordinate basis of $T_pM$. Every covector at $p$ has a unique expression $\omega_p = \omega_i \, dx^i|_p$ for scalars $\omega_i \in \mathbb{R}$.

**The cotangent bundle.** The **cotangent bundle** of $M$ is the disjoint union
$$T^*M := \bigsqcup_{p \in M} T_p^*M$$
with projection $\pi : T^*M \to M$ sending $\omega_p \mapsto p$, and the **unique** smooth structure making $T^*M$ a smooth rank-$n$ vector bundle over $M$ such that the coordinate covector fields $(dx^i)$ (the maps $p \mapsto dx^i|_p$, defined on the chart's domain $U$) are smooth local sections for every chart of $M$. This existence and uniqueness is the content of [[Thm - The Cotangent Bundle is a Smooth Manifold]].

Equivalent construction via the [[Thm - Vector Bundle Construction Lemma|vector-bundle construction lemma]]: take the open cover $\{U_\alpha\}$ of $M$ by coordinate charts, fibres $T_p^*M$, and transition functions
$$\tau_{\alpha\beta}(p) = \left( \frac{\partial x^i_\alpha}{\partial x^j_\beta}(p) \right)_{i,j} = \left(\text{inverse transpose Jacobian of the chart transition}\right).$$
The cocycle condition is the chain rule for derivatives, applied to inverse-transposed matrices.

A **covector field** (or **differential 1-form**) on $M$ is a smooth section of $T^*M$ — see [[Def - Covector Field and Differential 1-Form]]. The most important canonical example is the **differential of a smooth function**: for $f \in C^\infty(M)$, the covector field $df$ is defined by $df_p(v) = v(f)$ for $v \in T_pM$ — see [[Def - The Differential of a Function as a 1-Form]].

---

# Categorical Definition

The cotangent bundle is the dual bundle of the tangent bundle, in the precise categorical sense.

**Dual functor on vector bundles.** Let $\mathbf{Vect}_M$ be the category of smooth vector bundles over $M$ with morphisms the bundle [[Def - Homomorphism|homomorphisms]] over $M$. The **dual functor**
$$(-)^* : \mathbf{Vect}_M^{\mathrm{op}} \to \mathbf{Vect}_M$$
sends a bundle $E \to M$ to its dual $E^* := \bigsqcup_p E_p^*$, with fibrewise dual. It sends a bundle homomorphism $F : E \to E'$ over $M$ to the dual bundle homomorphism $F^* : (E')^* \to E^*$, $(F^*\omega)_p(v) = \omega_p(F_p(v))$. This is a *contravariant* functor — arrows are reversed.

The cotangent bundle is then defined as
$$T^*M := (TM)^*,$$
the dual of the tangent bundle. The dual functor packages the linear-algebra of duality applied fibrewise, and ensures that all natural constructions on the cotangent bundle (transition functions, smooth structure, sections) are derived from corresponding constructions on the tangent bundle.

**Cotangent functor on smooth manifolds.** The construction $M \mapsto T^*M$ is *not* a functor on smooth manifolds in the same way $TM$ is. Specifically, for a smooth map $F : M \to N$, the differential $dF : TM \to TN$ is a bundle homomorphism *covering $F$* (going from $M$ to $N$), making $T$ a covariant functor. But for the cotangent bundle, there is no analogous bundle homomorphism $T^*M \to T^*N$ — instead, there is a *pullback* of covector fields $F^* : \Gamma(T^*N) \to \Gamma(T^*M)$, going in the opposite direction. So $T^*(-)$ is contravariant on the level of sections, not on the level of total spaces.

This asymmetry is the structural source of the difference between vectors and covectors: vectors push forward (along diffeomorphisms), covectors pull back (always). The categorical content is that $\Gamma(T^*(-))$ is a contravariant functor from smooth manifolds to vector spaces (or $C^\infty$-[[Def - Module|module]]-functors when one keeps track of the base [[Def - Ring|ring]]).

**Hom-functor perspective.** The cotangent space at a point is $T_p^*M = \mathrm{Hom}_{\mathbb{R}}(T_pM, \mathbb{R})$, the $\mathbb{R}$-linear-map space. Bundle-globally, this realises $T^*M$ as a "Hom bundle" — the bundle of fibrewise $\mathbb{R}$-linear maps from $TM$ to the trivial line bundle $M \times \mathbb{R}$. In categorical language, $T^*M = \mathcal{Hom}(TM, M \times \mathbb{R})$ within $\mathbf{Vect}_M$.

---

# Relate to Other Fields / Compression

The cotangent space and cotangent bundle are the **manifold-theoretic instance of the linear-algebraic dual construction**, applied fibrewise. The cotangent space at $p$ is the dual of the tangent space ([[Def - Dual Space]]); the dual basis ([[Def - Dual Basis]]) of the coordinate basis of $T_pM$ is the coordinate dual basis of $T_p^*M$. Every fact from linear-algebraic duality theory — biorthogonality, dual maps, contravariance, the natural isomorphism $V \cong V^{**}$ — applies to each cotangent space pointwise.

**True name:** the cotangent space at $p$ is "**the space of linear measurements on tangent vectors at $p$**", and the cotangent bundle is "**the smoothly-varying family of all such measurement spaces, glued by inverse-transpose Jacobian transition functions**". The operational consequence: every time you see "$df$" or "$\omega$" in a calculation on a manifold, you are working in a fibre of the cotangent bundle, and the same linear-algebra rules apply as for any dual space — with the addition that the fibre varies smoothly with $p$.

The cotangent bundle is also **the home of phase space in classical mechanics**: for a configuration manifold $Q$, the cotangent bundle $T^*Q$ is the **phase space**, equipped with a canonical 1-form $\theta = p_i \, dq^i$ (the "tautological 1-form") and the symplectic form $\omega = d\theta = dp_i \wedge dq^i$. The whole apparatus of Hamiltonian mechanics — Hamilton's equations, conservation laws, Liouville's theorem — lives natively on $T^*Q$. This is one of the most important applications of the cotangent bundle and the reason the construction is central to mathematical physics.

In **algebraic geometry**, the cotangent sheaf $\Omega^1_{X/k}$ on a scheme $X$ is the algebraic counterpart of the smooth cotangent bundle, defined via Kähler differentials. The theory of cotangent sheaves and their cohomology (e.g., Hodge theory, the Hodge decomposition $H^k(X, \mathbb{C}) = \bigoplus H^{p,q}(X)$) generalizes differential-geometric statements about the cotangent bundle to far more general spaces.

---

# Examples / Corollaries

**Is an instance — $T^*\mathbb{R}^n = \mathbb{R}^n \times (\mathbb{R}^n)^*$.** For Euclidean space, the tangent bundle is trivial: $T\mathbb{R}^n = \mathbb{R}^n \times \mathbb{R}^n$, with the second factor identified with the standard $\mathbb{R}^n$. Dually, $T^*\mathbb{R}^n = \mathbb{R}^n \times (\mathbb{R}^n)^*$, with the second factor the dual space $(\mathbb{R}^n)^*$. Picking the standard basis of $\mathbb{R}^n$, the dual basis is $(dx^1, \dots, dx^n)$, and a 1-form on $\mathbb{R}^n$ is $\omega = \omega_i(x) \, dx^i$ for smooth coefficient functions $\omega_i$.

**Is an instance — $T^*S^1 = S^1 \times \mathbb{R}$.** For the circle, the tangent bundle is trivial (via $\partial/\partial\theta$), so the cotangent bundle is also trivial. The 1-form $d\theta$, defined on $S^1$ by lifting to $\mathbb{R}$ and using the standard $d\theta$ there (well-defined since translation by $2\pi$ preserves $d\theta$), is a global nonvanishing section. So $T^*S^1 \cong S^1 \times \mathbb{R}$.

**Is an instance — $T^*S^2$ is nontrivial.** Since $TS^2$ has no nowhere-vanishing global section (hairy ball theorem), neither does $T^*S^2$ (the duality pairing preserves zeros). So $T^*S^2$ is a nontrivial rank-$2$ vector bundle over $S^2$.

**Is an instance — the canonical 1-form on $T^*Q$.** For any manifold $Q$, the cotangent bundle $T^*Q$ carries a **canonical (or tautological) 1-form** $\theta$, defined as follows: at a point $\omega_q \in T^*_qQ$ (which is itself an element of $T^*Q$), the tangent space is $T_{\omega_q}(T^*Q)$, and the projection $\pi : T^*Q \to Q$ gives a differential $d\pi_{\omega_q} : T_{\omega_q}(T^*Q) \to T_q Q$. The canonical 1-form is $\theta_{\omega_q}(X) := \omega_q(d\pi_{\omega_q}(X))$ for $X \in T_{\omega_q}(T^*Q)$. In coordinates $(q^i, p_i)$ on $T^*Q$, $\theta = p_i \, dq^i$. This is the foundation of symplectic geometry on $T^*Q$.

**Is NOT a cotangent vector — a smooth function $f : T_pM \to \mathbb{R}$.** Not every function $T_pM \to \mathbb{R}$ is a covector; only the *linear* ones. For example, $v \mapsto \|v\|^2$ (with respect to some chosen inner product) is a function on $T_pM$ but is quadratic, not linear, so it is not in $T_p^*M$. It is an element of $\mathrm{Sym}^2(T_p^*M)$, the space of symmetric bilinear forms — a different bundle.

**Is NOT a cotangent vector — an element of $T_pM$.** Tangent vectors and cotangent vectors live in different (though isomorphic, non-canonically) vector spaces. A tangent vector $v \in T_pM$ is not in $T_p^*M$ unless there is an additional structure (an inner product, a Riemannian metric) that identifies them via the musical isomorphism $\flat : v \mapsto g(v, \cdot)$.

**Corollary — [[Def - Dimension|dimension]] matches.** $\dim T^*M = 2n$, the same as $\dim TM$, because both are rank-$n$ vector bundles over the $n$-dimensional manifold $M$. The total spaces have the same dimension; the bundles are not canonically isomorphic without extra structure.

**Corollary — the dual coordinate basis.** In a chart $(U, x^i)$, the covectors $dx^1|_p, \dots, dx^n|_p$ are the dual basis to $\partial/\partial x^1|_p, \dots, \partial/\partial x^n|_p$, so $\dim T_p^*M = n$.

**Corollary — change-of-basis is contravariant.** Under a coordinate change from $x^i$ to $\tilde x^j$, the coordinate vectors transform by the Jacobian $\partial \tilde x^j / \partial x^i$, while the coordinate covectors transform by the *inverse transpose* Jacobian. This is the structural source of "contravariance" of covectors and "covariance" of vectors — the classical tensor-algebraic terminology of physics.

**Corollary — the differential of a function is a covector field.** For $f \in C^\infty(M)$, $df_p \in T_p^*M$ for each $p$, and $df : p \mapsto df_p$ is a smooth section of $T^*M$. So $df$ is a 1-form, automatically. See [[Def - The Differential of a Function as a 1-Form]].

**Calibration check.** Verify that $dx^j|_p (\partial/\partial x^i|_p) = \delta^j_i$ by computing directly in a chart. Verify that the transition functions of $T^*M$ between two charts are the inverse transposes of the transitions of $TM$, by working out how the dual basis transforms. Convince yourself that the canonical 1-form on $T^*Q$ is well-defined (does not depend on a choice of basis) by tracing through the definition.

---

# Unlocked by This

> [!tip] Differential 1-Forms *(from this topic)*
> Smooth sections of $T^*M$ are **differential 1-forms**, written $\omega \in \Omega^1(M)$. They are the natural integrands of line integrals, the natural output of $d$ applied to functions, and the first instance of the full apparatus of differential forms — see [[Def - Covector Field and Differential 1-Form]] and [[Differential Geometry VIII — Differential Forms]].

> [!tip] Tensor Fields and the Tensor Algebra *(from Differential Geometry VII)*
> Once $TM$ and $T^*M$ are in hand, all higher tensor bundles are constructed: the bundle of $(p, q)$-tensors is $T^{p,q}M = TM^{\otimes p} \otimes (T^*M)^{\otimes q}$, with sections forming the **tensor fields**. The Riemannian metric is a $(0, 2)$-tensor, the Riemann curvature is a $(1, 3)$-tensor, the Christoffel symbols transform like a $(1, 2)$-quantity but are not actually a tensor (they transform with an extra Jacobian term).

> [!tip] Differential $k$-Forms *(from Differential Geometry VIII)*
> Antisymmetrizing the tensor product gives the **exterior algebra**: the bundle $\Lambda^k T^*M$ has fibres $\Lambda^k T_p^*M$, the space of alternating $k$-linear forms on $T_pM$. Sections are **differential $k$-forms**, $\Omega^k(M) = \Gamma(\Lambda^k T^*M)$. The exterior derivative $d : \Omega^k(M) \to \Omega^{k+1}(M)$ generalizes the differential of a function and is the central operator of differential forms.

> [!tip] Symplectic Manifold and Phase Space *(from Symplectic Geometry / Hamiltonian Mechanics)*
> The cotangent bundle $T^*Q$ of any manifold $Q$ carries a canonical symplectic form $\omega = d\theta = dp_i \wedge dq^i$, making $(T^*Q, \omega)$ a **symplectic manifold**. This is the geometry of phase space in classical mechanics: the canonical Hamilton's equations on $T^*Q$ for a Hamiltonian $H : T^*Q \to \mathbb{R}$ are $\iota_{X_H} \omega = dH$, defining the Hamiltonian vector field $X_H$. Noether's theorem in this language is a one-line statement about moment maps for symmetry group actions. The whole theory of geometric mechanics — Poisson brackets, action-angle variables, Liouville integrability — lives on the cotangent bundle.

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> Since the cotangent bundle and its exterior powers $\Lambda^k T^*M$ admit the differential operator $d$ satisfying $d^2 = 0$, the **de Rham complex** $0 \to \Omega^0(M) \to \Omega^1(M) \to \Omega^2(M) \to \cdots$ has well-defined cohomology groups $H^k_{dR}(M) = \ker(d) / \mathrm{im}(d)$. These are smooth invariants of $M$, isomorphic (de Rham theorem) to singular cohomology $H^k(M; \mathbb{R})$ — so they are actually *topological* invariants. The cotangent bundle is thus the manifold-theoretic gateway to algebraic topology.
