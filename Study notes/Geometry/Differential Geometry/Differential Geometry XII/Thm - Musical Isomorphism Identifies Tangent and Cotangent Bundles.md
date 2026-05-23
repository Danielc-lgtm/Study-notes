---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Musical Isomorphism (Flat and Sharp)"
  - "Def - Riemannian Metric"
  - "Def - The Tangent Space"
  - "Def - Cotangent Space and Cotangent Bundle"
tags: [geometry, differential-geometry, riemannian-geometry]
---

# Notation

$(M, g)$ — a Riemannian manifold (or semi-Riemannian, with $g$ non-degenerate). $\flat : TM \to T^*M$, $\sharp : T^*M \to TM$ — the [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphisms]]. $g^{ij}$ — the inverse metric components. $\mathrm{grad}_g f = (df)^\sharp$ — the gradient of a smooth function $f \in C^\infty(M)$. Full notation registry on [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

---

# Statement

> **Theorem (Tangent–Cotangent Isomorphism).** Let $(M, g)$ be a Riemannian manifold (or more generally, a semi-Riemannian manifold with $g$ non-degenerate). The flat map
> $$
> \flat : TM \longrightarrow T^*M, \qquad \flat_p(v) = g_p(v, \cdot),
> $$
> is a smooth bundle isomorphism. Its inverse is the sharp map $\sharp$, with $(g^{ij})$ the inverse matrix of $(g_{ij})$ in any coordinates.

This is the bundle isomorphism statement (Lee, around Theorem 13.29). It depends on the metric: a different $g$ gives a different isomorphism.

---

# Motivation

The tangent bundle $TM$ and the cotangent bundle $T^*M$ of a smooth manifold are *dual bundles* — they are pointwise dual vector spaces — but they are not naturally isomorphic without extra data. A Riemannian (or pseudo-Riemannian) metric provides exactly the extra data needed: a non-degenerate bilinear form $g_p$ on each $T_pM$, which yields the canonical "Riesz" isomorphism $T_pM \to T_p^*M$ at every point. The theorem asserts that this pointwise isomorphism assembles into a smooth bundle isomorphism.

The structural significance is that on a Riemannian manifold, "vector" and "covector" are *the same kind of object*: every vector field has a corresponding 1-form (its "flat"), and every 1-form has a corresponding vector field (its "sharp"). This identification is the formal mechanism behind index-raising and index-lowering in tensor calculus, and it is the device that makes the gradient $\mathrm{grad}_g f = (df)^\sharp$ a vector field rather than just a 1-form.

The theorem also gives the structural reason why the inverse metric $g^{ij}$ is the matrix of $\sharp$: it is the matrix-inverse of the matrix of $\flat$, which is $g_{ij}$. So "raise an index with $g^{ij}$" is exactly the inverse operation of "lower an index with $g_{ij}$".

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: Non-degenerate metric (Riemannian or pseudo-Riemannian).* The hypothesis is *non-degeneracy* of $g$ at every point, not positive-definiteness. So the theorem holds equally well for Riemannian and for [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian]] metrics — Lorentzian manifolds also have a musical isomorphism. The pullback formula $X_i = g_{ij}X^j$ works for any signature; only the sign behaviour changes (in Minkowski space, raising/lowering flips signs on spacelike components).

*Source 2: Any non-degenerate fibre form on a vector bundle.* The same theorem holds for any smooth vector bundle $E \to M$ equipped with a non-degenerate fibre-bilinear form $b \in \Gamma(\mathrm{Sym}^2 E^* \cup \Lambda^2 E^*)$: $b$ induces a smooth bundle isomorphism $E \to E^*$. The Riemannian case is $E = TM$ with $b = g$ symmetric positive-definite; the symplectic case is $b = \omega$ antisymmetric non-degenerate, where the same isomorphism $TM \to T^*M$ is the **musical isomorphism of symplectic geometry**, used to define Hamiltonian vector fields from Hamiltonian functions.

*Source 3: Tensor characterisation lemma applied to the flat map.* In Lee's proof, the bundle homomorphism nature of $\flat$ is verified via the **tensor characterisation lemma** (Lemma 12.24): $\hat g(X)(Y) = g(X, Y)$ is $C^\infty(M)$-linear in $Y$ (for fixed $X$), hence is a smooth covector field; the same map is $C^\infty(M)$-linear in $X$ as well, so $\hat g$ is a bundle homomorphism. *Trigger:* you need to verify a fibrewise-defined operation between bundles is a smooth bundle map; the tensor characterisation lemma converts $C^\infty(M)$-multilinearity into smoothness of the bundle map.

**Targets (Output Amplification)**

*Target combination 1: Definition of the gradient as a vector field.* Combined with the smooth differential $df : M \to T^*M$ of a smooth function, the sharp map produces the gradient $\mathrm{grad}_g f = (df)^\sharp$ — a vector field on $M$. This is the manifold-intrinsic notion of gradient, generalising the elementary calculus gradient (which only equals "vector of partials" in Cartesian coordinates).

*Target combination 2: Definition of divergence and Laplace–Beltrami.* The divergence of a vector field $X$ on $(M, g)$ can be defined as $\mathrm{div}(X) = \mathrm{tr}\,\nabla X$ using the Levi-Civita connection, or equivalently (in coordinates) $\mathrm{div}(X) = (1/\sqrt{\det g})\, \partial_i(\sqrt{\det g}\, X^i)$. The Laplace–Beltrami operator is the composition $\Delta_g f = \mathrm{div}(\mathrm{grad}_g f)$, and both pieces use the musical isomorphism (gradient explicitly, divergence implicitly through the metric volume form).

*Target combination 3: Index raising on higher-rank tensors.* For any tensor of mixed type, the metric can be used to raise or lower any index. For instance, the Riemann curvature tensor $R^l{}_{ijk}$ lowers to $R_{lijk} = g_{lm}R^m{}_{ijk}$. The general rule "lower an index with $g_{ij}$, raise with $g^{ij}$" generalises the basic flat/sharp construction to all tensor types.

---

# Why Is It True

**Mechanism summary:** **non-degeneracy of $g$ at every point makes the map $v \mapsto g(v, \cdot)$ injective, and dimension count makes it surjective, so it is a fibrewise isomorphism — and smoothness of $g$ makes the assembled map a smooth bundle isomorphism.**

The pointwise statement is pure linear algebra: a non-degenerate bilinear form on a finite-dimensional vector space gives a canonical isomorphism between the space and its dual. The map $v \mapsto g(v, \cdot)$ sends $v \in V$ to the linear functional $w \mapsto g(v, w)$ in $V^*$. Injectivity: if $g(v, \cdot) = 0$ as a linear functional, then $g(v, w) = 0$ for all $w$, so by non-degeneracy $v = 0$. Surjectivity: from injectivity plus $\dim V = \dim V^*$ (since $V$ is finite-dimensional). So at each point we have an isomorphism $T_pM \to T_p^*M$.

The smoothness — that the family of these isomorphisms is smooth in $p$ — comes from the smoothness of $g$. In coordinates, the matrix of $\flat_p$ is $g_{ij}(p)$, a smooth function of $p$. Its inverse $g^{ij}(p)$ exists pointwise (non-degeneracy means $\det(g_{ij}(p)) \neq 0$ for every $p$, hence $\det$ is a smooth function nowhere zero, and by Cramer's rule the inverse matrix has smooth entries). So $\flat$ and $\sharp$ are smooth bundle maps, and being inverses gives the bundle isomorphism.

Alternatively, via the tensor characterisation lemma: the map $X \mapsto g(X, \cdot)$ on vector fields is $C^\infty(M)$-linear ($g(fX, Y) = f g(X, Y)$ for $f \in C^\infty(M)$). The tensor characterisation lemma converts $C^\infty(M)$-linearity into a bundle map. The same map is also $C^\infty(M)$-linear in the second argument, so it is a bundle map between $TM$ and $T^*M$.

The decisive observation is the *pointwise* isomorphism — that is the whole content. Everything else is bookkeeping for smoothness, which follows from the smoothness of $g$.

---

# What Makes This Hard

The conceptual difficulty is **distinguishing the canonical isomorphism $V \cong V^{**}$ from the metric-dependent isomorphism $V \cong V^*$**. Every vector space is canonically isomorphic to its double dual via $v \mapsto (\omega \mapsto \omega(v))$, with no extra data needed. But no vector space is canonically isomorphic to its single dual — that requires a choice of bilinear form. Students often slip into identifying $V$ with $V^*$ as if it were canonical, especially when working in a coordinate chart where the basis $\partial_i$ and the dual basis $dx^i$ look like they should be identified by name. The musical isomorphism is the *only* canonical identification, and it depends on the metric: a different metric gives a different identification. This is the central distinction one must internalise to do Riemannian tensor calculus correctly.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Pointwise, the non-degeneracy of $g_p$ makes $v \mapsto g_p(v, \cdot)$ an isomorphism by injectivity and dimension count. Smoothness of $g$ promotes this to a smooth bundle isomorphism. The matrix of $\flat$ is $g_{ij}$; its inverse is $g^{ij}$.

**Subgoal decomposition:**

1. **Pointwise: $\flat_p$ is injective.** If $g_p(v, w) = 0$ for all $w$, then $v = 0$ by non-degeneracy.
   - *Hint:* Take $w = v$ to get $g_p(v, v) = 0$, and use positive-definiteness (or non-degeneracy in the Riemannian case automatically implies this; in general, use the formal non-degeneracy condition).
   - *Why needed:* Injectivity is the non-trivial half of the isomorphism (surjectivity follows from dimension count).

2. **Pointwise: $\flat_p$ is an isomorphism.** Injective linear map between equal-dimensional spaces.
   - *Hint:* $\dim T_pM = \dim T_p^*M$, so injective $\Rightarrow$ bijective.
   - *Why needed:* The fibrewise isomorphism is the goal.

3. **Coordinate expression: the matrix of $\flat_p$ is $g_{ij}(p)$.** Compute in a coordinate basis.
   - *Hint:* $\flat_p(\partial_i) = g_p(\partial_i, \cdot) = g_p(\partial_i, \partial_j) dx^j = g_{ij}(p) dx^j$, so the matrix is $g_{ij}(p)$.
   - *Why needed:* This is how one computes $\flat$ in practice and identifies its inverse.

4. **Inverse $\sharp$: matrix is $g^{ij}$.** Inverse of $g_{ij}$ by definition.
   - *Hint:* $g^{ij}g_{jk} = \delta^i_k$ by definition, so $g^{ij}$ is the matrix of $\sharp$ in the coordinate basis.
   - *Why needed:* The sharp map is the inverse, and its coordinate matrix is the inverse metric.

5. **Smoothness: $\flat$ and $\sharp$ are smooth bundle maps.** Smoothness of $g_{ij}(x)$ and $g^{ij}(x)$ as functions of $x$.
   - *Hint:* $g_{ij}(x)$ is smooth by hypothesis, and $g^{ij}(x)$ is smooth because $\det g_{ij}(x) \neq 0$ globally (non-degeneracy) and inverse-matrix entries are rational functions of input entries.
   - *Why needed:* Bundle maps require smoothness, not just pointwise linearity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pointwise — non-degenerate bilinear form gives an isomorphism $V \to V^*$
> **Statement:** Let $b : V \times V \to \mathbb{R}$ be a non-degenerate symmetric bilinear form on a finite-dimensional real vector space $V$. The map $\flat : V \to V^*$, $v \mapsto b(v, \cdot)$, is a linear isomorphism.
>
> **Hint:** Linearity is immediate; injectivity is non-degeneracy; bijectivity follows from $\dim V = \dim V^*$.
>
> **Why needed:** This is the pointwise content of the theorem, and the bundle version follows by parametrising in $p$.
>
> > [!note]- Full proof
> > **Linearity.** For $v_1, v_2 \in V$ and $\alpha \in \mathbb{R}$, $\flat(\alpha v_1 + v_2)(w) = b(\alpha v_1 + v_2, w) = \alpha b(v_1, w) + b(v_2, w) = \alpha \flat(v_1)(w) + \flat(v_2)(w)$, so $\flat(\alpha v_1 + v_2) = \alpha \flat(v_1) + \flat(v_2)$. Hence $\flat$ is linear.
> >
> > **Injectivity.** Suppose $\flat(v) = 0$ — that is, $b(v, w) = 0$ for every $w \in V$. By non-degeneracy of $b$, this forces $v = 0$. So $\ker\flat = \{0\}$.
> >
> > **Bijectivity.** A linear map between finite-dimensional vector spaces of equal dimension is bijective iff it is injective iff it is surjective. Here $\dim V^* = \dim V$, so injectivity of $\flat$ implies bijectivity.

> [!note]- Lemma 2: Coordinate expression — matrix of $\flat$ is $g_{ij}$
> **Statement:** In local coordinates $x^i$ with the coordinate basis $\{\partial_i\}$ of $T_pM$ and the dual basis $\{dx^j\}$ of $T_p^*M$, the matrix of $\flat_p : T_pM \to T_p^*M$ is $g_{ij}(p)$.
>
> **Hint:** Compute $\flat_p(\partial_i)$ in the dual basis.
>
> **Why needed:** This gives the coordinate formula for index lowering: $v_j = g_{ij}v^i$.
>
> > [!note]- Full proof
> > By definition, $\flat_p(\partial_i) \in T_p^*M$ is the covector $g_p(\partial_i, \cdot)$. Its components in the dual basis $\{dx^j\}$ are $\flat_p(\partial_i)(\partial_j) = g_p(\partial_i, \partial_j) = g_{ij}(p)$. So $\flat_p(\partial_i) = g_{ij}(p)\, dx^j$, and the matrix of $\flat_p$ with respect to these bases is $(g_{ij}(p))$.
> >
> > Equivalently, for a general vector $v = v^i \partial_i$, $\flat_p(v) = v^i \flat_p(\partial_i) = v^i g_{ij}(p) dx^j = (g_{ij}v^i) dx^j$, so the components of $\flat_p(v)$ are $v_j := g_{ij}v^i$ — the index-lowering formula.

> [!note]- Lemma 3: Smoothness of $\flat$ as a bundle map
> **Statement:** The fibrewise map $\flat : TM \to T^*M$ is a smooth bundle homomorphism.
>
> **Hint:** In any coordinate chart, the matrix of $\flat_p$ is the smooth matrix $g_{ij}(x)$. A bundle map with smooth coordinate representation is smooth.
>
> **Why needed:** Pointwise isomorphism is not enough; we need a smooth bundle isomorphism.
>
> > [!note]- Full proof
> > In a smooth chart, both $TM|_U$ and $T^*M|_U$ are trivial bundles $U \times \mathbb{R}^n$ via the coordinate frames $\{\partial_i\}$ and $\{dx^i\}$. The map $\flat$ in these trivialisations is $(x, v^1, \ldots, v^n) \mapsto (x, g_{1j}(x)v^j, \ldots, g_{nj}(x)v^j)$ — that is, multiplication by the matrix $g_{ij}(x)$. Since $g_{ij}(x)$ is smooth in $x$ by hypothesis, this is a smooth map.
> >
> > Smoothness in any chart implies smoothness of the global bundle map (smoothness is a local property). Linearity on fibres is immediate. So $\flat$ is a smooth bundle homomorphism.

> [!note]- Lemma 4: $\sharp$ is the inverse bundle isomorphism, with matrix $g^{ij}$
> **Statement:** The bundle homomorphism $\sharp : T^*M \to TM$ defined fibrewise by $\sharp_p = (\flat_p)^{-1}$ is a smooth bundle homomorphism with matrix $g^{ij}(x)$ — the inverse matrix of $g_{ij}(x)$.
>
> **Hint:** The inverse of the matrix $g_{ij}(x)$ is $g^{ij}(x)$ by definition. Smoothness of $g^{ij}$ in $x$ follows from non-degeneracy ($\det g \neq 0$ globally) and the formula for matrix inverse.
>
> **Why needed:** Completes the bundle isomorphism statement.
>
> > [!note]- Full proof
> > Pointwise, $\sharp_p : T_p^*M \to T_pM$ is the inverse of $\flat_p$, which exists by Lemma 1. In coordinates, its matrix is the inverse of $g_{ij}(p)$, i.e., $g^{ij}(p)$.
> >
> > Smoothness of $g^{ij}(x)$ in $x$ follows from non-degeneracy: $\det g_{ij}(x) \neq 0$ for every $x$, and since this is a continuous function of $x$ that never vanishes, it is bounded away from zero on compact sets. The entries of the inverse matrix are rational functions of the entries of the original matrix (Cramer's rule), with denominator $\det g$, which is smooth and nowhere zero. So $g^{ij}(x)$ is smooth in $x$.
> >
> > Hence $\sharp$ is a smooth bundle map with smooth coordinate matrix $g^{ij}(x)$, and it is the inverse of $\flat$ fibrewise. Together $\flat$ and $\sharp$ form mutually inverse bundle isomorphisms.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(M, g)$ be a Riemannian (or non-degenerate semi-Riemannian) manifold.
>
> **Step 0 — well-posedness.** Non-degeneracy of $g$ at every point ensures that the inverse matrix $g^{ij}$ exists pointwise, so the maps $\flat$ and $\sharp$ are well-defined fibrewise.
>
> **Step 1 — Pointwise isomorphism.** By Lemma 1, at each $p \in M$ the map $\flat_p : T_pM \to T_p^*M$, $v \mapsto g_p(v, \cdot)$, is a linear isomorphism with inverse $\sharp_p$.
>
> **Step 2 — Smoothness.** By Lemma 3, $\flat : TM \to T^*M$ is a smooth bundle homomorphism (with coordinate matrix $g_{ij}(x)$). By Lemma 4, $\sharp : T^*M \to TM$ is a smooth bundle homomorphism (with coordinate matrix $g^{ij}(x)$).
>
> **Step 3 — Mutual inverses.** Pointwise $\sharp_p \circ \flat_p = \mathrm{id}_{T_pM}$ and $\flat_p \circ \sharp_p = \mathrm{id}_{T_p^*M}$. So $\flat$ and $\sharp$ are mutually inverse smooth bundle homomorphisms, hence bundle isomorphisms.
>
> Therefore $TM$ and $T^*M$ are smoothly isomorphic as vector bundles via the metric-induced musical isomorphisms. $\blacksquare$

---

# Cross-Field Exercise Suggestions

*1. The symplectic version of the musical isomorphism.* For a symplectic manifold $(M, \omega)$ — a smooth manifold with a closed non-degenerate antisymmetric 2-form $\omega$ — the same construction gives a bundle isomorphism $\omega^\flat : TM \to T^*M$ via $X \mapsto \iota_X \omega = \omega(X, \cdot)$. The musical isomorphism of symplectic geometry is used to define **Hamiltonian vector fields**: for a smooth function $H : M \to \mathbb{R}$, the Hamiltonian vector field $X_H$ is the unique vector field with $\iota_{X_H}\omega = dH$, i.e., $X_H = (dH)^\sharp$ using the symplectic musical isomorphism. So Hamilton's equations are the symplectic analogue of "gradient flow", with the symplectic form replacing the metric.

*2. Holographic duality and raising/lowering in AdS spacetimes.* In the AdS/CFT correspondence, the bulk Lorentzian Anti-de Sitter spacetime has a non-degenerate metric, and the musical isomorphism identifies bulk tensor fields with their boundary counterparts via a specific scaling. The metric-induced index-raising/lowering interacts with the holographic dictionary in subtle ways.

*3. Bundles other than $TM$: index gymnastics on associated bundles.* For any vector bundle $E \to M$ equipped with a fibre metric $g_E$, the same musical isomorphism gives $E \cong E^*$. This is used in defining covariant derivatives on $E^*$ from those on $E$, in defining adjoint connections, and in setting up Hodge theory on $E$-valued differential forms.

*4. Fisher information metric and its dual.* In information geometry, the Fisher information metric $g_{ij}$ on a statistical model has both a "lowering" and a "raising" form. The dual coordinate system associated to the metric is what makes exponential families "dually flat" — they admit two flat affine connections related by the musical isomorphism. This is the Amari–Chentsov structure of information geometry.

---

# Bridges

- **Riesz representation theorem.** The pointwise content of the musical isomorphism is the Riesz representation theorem for finite-dimensional inner product spaces: every linear functional on an inner-product space is represented by inner product with a unique vector. This theorem extends to infinite-dimensional Hilbert spaces (with countability/separability assumptions) and is foundational in functional analysis. The musical isomorphism is the smooth-manifold version: at every tangent space, the Riesz representation operates, and the smoothness in the base point assembles into a bundle isomorphism.

- **Hodge star operator** (forward bridge). Combined with the [[Def - Riemannian Volume Form|Riemannian volume form]], the musical isomorphism extends to the **Hodge star** $\star : \Omega^k(M) \to \Omega^{n-k}(M)$, an isomorphism between $k$-forms and $(n-k)$-forms that is metric-and-orientation-dependent. The Hodge star is the engine of **Hodge theory**, which represents de Rham cohomology classes by harmonic forms on compact Riemannian manifolds. The musical isomorphism is the degree-$0$/degree-$1$ piece of this larger structure.

- **The dual of a vector bundle.** Every vector bundle $E \to M$ has a dual bundle $E^*$, with fibres $E_p^* = (E_p)^*$. The musical isomorphism shows that a fibre metric on $E$ identifies $E$ with $E^*$ as smooth vector bundles. In particular, $TM \cong T^*M$ as bundles whenever $M$ is Riemannian (or semi-Riemannian with non-degenerate metric). This is a global structural identification, distinct from the local-coordinate identification (which can be misleading because basis vectors $\partial_i$ and dual basis $dx^i$ look identical-labelled).

---

# Unlocked by This

> [!tip] The Gradient as a Vector Field *(from Vector Calculus on Manifolds)*
> Combining the musical isomorphism with the differential $df \in \Omega^1(M)$ of a smooth function, the **gradient** $\mathrm{grad}_g f = (df)^\sharp$ is a vector field on $M$. In coordinates: $(\mathrm{grad}_g f)^i = g^{ij}\partial_j f$. The gradient is the metric-dual of the differential and the *correct* manifold-intrinsic notion of "gradient" (the elementary calculus version $(\partial_1 f, \ldots, \partial_n f)$ agrees only in Cartesian coordinates on Euclidean space).

> [!tip] The Laplace–Beltrami Operator *(from Riemannian Geometry and PDE)*
> The musical isomorphism enables the definition of the **Laplace–Beltrami operator** $\Delta_g f = \mathrm{div}(\mathrm{grad}_g f)$. In coordinates,
> $$
> \Delta_g f = \frac{1}{\sqrt{\det g}}\, \partial_i\bigl(\sqrt{\det g}\, g^{ij}\partial_j f\bigr).
> $$
> This is the second-order elliptic operator on $(M, g)$ whose spectrum encodes geometric information about the manifold (Weyl's law, spectral geometry, "can you hear the shape of a drum"). The musical isomorphism is the input that makes the gradient (hence the Laplacian) well-defined.

> [!tip] The Hodge Decomposition *(from Hodge Theory and de Rham Cohomology)*
> The musical isomorphism extends to all degrees of forms via the Hodge star $\star$, and gives the **Hodge decomposition** on a compact oriented Riemannian manifold:
> $$
> \Omega^k(M) = \mathrm{im}\, d \oplus \mathrm{im}\, \delta \oplus \ker \Delta,
> $$
> where $\delta = (-1)^{...}\star d\star$ is the codifferential, $\Delta = d\delta + \delta d$ is the Hodge Laplacian, and the harmonic forms in $\ker \Delta$ uniquely represent de Rham cohomology classes. The musical isomorphism is the foundational structural input.

> [!tip] Index Gymnastics in Tensor Calculus *(from General Relativity and Tensor Calculus)*
> All of tensor calculus in general relativity, including the Einstein field equations $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} = 8\pi G T_{\mu\nu}$, uses index raising and lowering via $g^{\mu\nu}$ and $g_{\mu\nu}$. The musical isomorphism applied to higher-rank tensors gives the full machinery of "covariant-contravariant" conversion, and every component formula in relativistic physics passes through it.
