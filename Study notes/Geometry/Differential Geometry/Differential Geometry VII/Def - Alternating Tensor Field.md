---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Tensor Field on a Manifold"
  - "Def - Alternating Multilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
tags: [geometry, differential-geometry, forms, alternating-tensors]
---

# Notation

$V$ is a finite-dimensional real vector space, $\dim V = n$. $M$ is a smooth manifold. $S_k$ is the symmetric group on $k$ elements; $\operatorname{sgn}\sigma \in \{\pm 1\}$ is the sign of a permutation. $\Lambda^k(V^*) \subset T^k(V^*)$ is the subspace of alternating covariant $k$-tensors on $V$; $\Lambda^k(T^*M)$ is the corresponding subbundle of $T^kT^*M$. Sections of $\Lambda^k(T^*M)$ are *alternating $k$-tensor fields*, which in the next chapter will be called [[Def - Differential Form|differential k-forms]]. Components of an alternating tensor are denoted $\alpha_{[i_1\cdots i_k]}$, with square brackets reminding the reader that the indices are antisymmetrized. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Axiom Motivation

The motivating examples are the **determinant** (a covariant $n$-tensor on $\mathbb{R}^n$ that flips sign when two columns are interchanged), the **signed area** of a parallelogram (a covariant 2-tensor in 2D that flips sign when the order of the vectors is reversed, encoding orientation), and the **flux** of a vector field through a surface (a 2-form whose sign depends on the surface's orientation). All three are tensors that change sign under transposition of arguments — they are the algebraic encoding of *orientation*.

The axiom is: $\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\operatorname{sgn}\sigma)\,\alpha(v_1, \dots, v_k)$ for every $\sigma \in S_k$. As with the symmetric case, it suffices to require this for transpositions of adjacent slots; the general permutation case then follows because every permutation is a product of transpositions and the sign is multiplicative. So the operational axiom is just: swap any two arguments, get a minus sign.

A crucial consequence of alternation, **not present** in the symmetric case, is the **vanishing identity**: $\alpha(v_1, \dots, v_k) = 0$ whenever two of the arguments coincide. *Proof:* swapping the two coincident arguments gives $\alpha = -\alpha$, hence $\alpha = 0$. Iterating, an alternating $k$-tensor vanishes on any linearly dependent $k$-tuple of vectors. This is what makes alternating tensors **detect linear independence** — they are zero on dependent tuples and nonzero on at least some independent tuples. The determinant is the prototype: $\det(v_1, \dots, v_n) \neq 0 \iff (v_1, \dots, v_n)$ is a basis.

The vanishing identity has a striking dimension consequence: $\Lambda^k(V^*) = 0$ for $k > n$, because every $k$-tuple of vectors in an $n$-dimensional space with $k > n$ is linearly dependent. The non-trivial dimensions are $\dim \Lambda^k(V^*) = \binom{n}{k}$ for $0 \leq k \leq n$, with $\Lambda^n(V^*)$ being a 1-dimensional "top-form" space — the home of the determinant and of [[Def - Volume Form|volume forms]].

One could ask why we separate alternating tensors from symmetric tensors when both are defined in parallel. The reason is that **their downstream applications are radically different**. Alternating tensors are the home of **differential forms**, with the wedge product $\wedge$ (rather than the symmetric product), with the *exterior derivative* $d$ (a first-order differential operator with no analogue for symmetric tensors), and with *integration over submanifolds* (which requires alternation to give an oriented integral). The symmetric tensors are the home of metrics, quadratic forms, and Riemannian geometry. The whole next chapter, [[Differential Geometry VIII — Differential Forms]], is the study of alternating tensor fields with their characteristic operations.

The decision to give alternating tensor fields their own definition page, rather than treating them as a special case of "covariant tensor field with an extra condition", reflects the fact that the alternation condition unlocks a whole new layer of structure (wedge product, exterior derivative, integration, Poincaré lemma, de Rham cohomology). The symmetric case unlocks Riemannian geometry. The two strands almost never mix at the manipulation level: a problem about lengths and inner products is *symmetric*; a problem about fluxes, integration, and volumes is *alternating*. Keeping them as separate categories from the start prevents cross-contamination.

The manifold-level definition asks for the alternation to hold *fibrewise*: a smooth covariant $k$-tensor field is alternating if $A_p \in \Lambda^k(T_p^*M)$ for every $p$. As with symmetric tensor fields, smoothness of the section is the only smoothness condition; alternation is preserved automatically because it is a fibre-level algebraic property.

---

# The Definition

A covariant $k$-tensor $\alpha$ on a finite-dimensional real vector space $V$ is **alternating** (or *antisymmetric*, *skew-symmetric*) if

$$\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\operatorname{sgn}\sigma)\,\alpha(v_1, \dots, v_k) \qquad \text{for every } \sigma \in S_k, \text{ for all } v_1, \dots, v_k \in V.$$

Equivalently, the components $\alpha_{i_1\cdots i_k}$ in any basis satisfy $\alpha_{i_{\sigma(1)}\cdots i_{\sigma(k)}} = (\operatorname{sgn}\sigma)\,\alpha_{i_1\cdots i_k}$. The set of alternating covariant $k$-tensors on $V$ is denoted $\Lambda^k(V^*) \subset T^k(V^*)$.

**Alternating tensor field on a manifold.** Let $M$ be a smooth manifold. An **alternating covariant $k$-tensor field** on $M$ — equivalently, a **differential $k$-form** on $M$ in the language of [[Differential Geometry VIII — Differential Forms]] — is a smooth covariant $k$-tensor field $A : M \to T^kT^*M$ such that $A_p \in \Lambda^k(T_p^*M)$ for every $p$.

Equivalent characterizations:
1. $A_p$ is alternating for every $p$.
2. The component functions $A_{i_1\cdots i_k}$ in every chart are smooth and satisfy $A_{i_{\sigma(1)}\cdots i_{\sigma(k)}} = (\operatorname{sgn}\sigma)\,A_{i_1\cdots i_k}$.
3. The $C^\infty(M)$-multilinear map $\mathfrak{X}(M)^k \to C^\infty(M)$ induced by $A$ is alternating: $A(X_{\sigma(1)}, \dots, X_{\sigma(k)}) = (\operatorname{sgn}\sigma)\, A(X_1, \dots, X_k)$.

The space of smooth alternating covariant $k$-tensor fields is the space of smooth sections of $\Lambda^k(T^*M)$, denoted $\Omega^k(M)$ in the forms convention. So $\Omega^0(M) = C^\infty(M), \Omega^1(M) = $ 1-forms, etc.

**Dimension of the fibre.** $\dim \Lambda^k(V^*) = \binom{n}{k}$ for $0 \leq k \leq n$, and $\Lambda^k(V^*) = 0$ for $k > n$. In particular, $\dim \Lambda^n(V^*) = 1$: the "top" alternating space is 1-dimensional.

**Vanishing on linearly dependent tuples.** If $\alpha \in \Lambda^k(V^*)$ and $v_1, \dots, v_k \in V$ are linearly dependent, then $\alpha(v_1, \dots, v_k) = 0$. *Proof:* if $v_i = v_j$ for some $i \neq j$, swapping gives $\alpha = -\alpha$, so $\alpha = 0$. More generally, if $v_k = \sum_{i < k} c_i v_i$, expand by multilinearity and use the previous case.

**The wedge product (preview).** The wedge product $\alpha \wedge \beta \in \Lambda^{k+\ell}(V^*)$ for $\alpha \in \Lambda^k(V^*)$ and $\beta \in \Lambda^\ell(V^*)$ is the alternation of the tensor product, up to a combinatorial factor:

$$\alpha \wedge \beta = \frac{(k+\ell)!}{k!\,\ell!}\,\mathrm{Alt}(\alpha \otimes \beta).$$

The wedge product is associative and **graded commutative**: $\alpha \wedge \beta = (-1)^{k\ell}\beta \wedge \alpha$. The full development is in [[Differential Geometry VIII — Differential Forms]].

---

# Categorical / Structural Definition

$\Lambda^k(V^*)$ is the **sign representation** of $S_k$ inside $T^k(V^*)$:

$$\Lambda^k(V^*) = T^k(V^*)^{(\operatorname{sgn})} = \{\alpha \in T^k(V^*) : \sigma \cdot \alpha = (\operatorname{sgn}\sigma)\,\alpha \ \forall \sigma\},$$

where the $S_k$ action is the same as in the symmetric case (precomposition with the permutation). Equivalently, $\Lambda^k(V^*)$ is the image of the alternation projector $\mathrm{Alt} = \frac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma)\,\sigma$.

The graded vector space $\Lambda^\bullet(V^*) = \bigoplus_k \Lambda^k(V^*)$, with the wedge product, is the **exterior algebra** of $V^*$ — a graded-commutative associative algebra of dimension $2^n$ (sum of $\binom{n}{k}$ over $k$), generated by $V^* = \Lambda^1(V^*)$ subject to the relations $\omega \wedge \omega = 0$ for $\omega \in V^*$. Universal property: the exterior algebra is the free graded-commutative algebra generated by $V^*$ subject to $v \wedge v = 0$ in degree 1.

The exterior algebra is the alternating analogue of the symmetric algebra: just as $S^\bullet(V^*) \cong \mathbb{R}[V]$ (polynomial functions on $V$), $\Lambda^\bullet(V^*)$ is the algebra of "alternating multilinear functionals" — the natural input to integration over oriented submanifolds.

---

# Relate to Other Fields / Compression

Alternating covariant $k$-tensors are exactly the [[Def - Alternating Multilinear Form|alternating multilinear forms]] of [[Linear Algebra IX — §9 Multilinear Algebra and Determinants|LA IX]] §9B. Their study includes the [[Def - Determinant|determinant]] (the canonical alternating $n$-form), the [[Def - The Wedge Product|wedge product]], and (in the next chapter) the [[Def - The Exterior Derivative|exterior derivative]] — operations that have no analogue in the symmetric world.

From the geometric side, alternating tensor fields are **the algebraic encoding of orientation**. An oriented manifold has a global non-vanishing top form, and integration over oriented submanifolds is integration of alternating tensor fields against the submanifold's orientation form. The whole machinery of integration on manifolds — [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|Stokes's theorem]], de Rham cohomology, fluxes — is built on alternating tensor fields.

From the physics side, the **electromagnetic field strength** $F_{\mu\nu}$ is an alternating $(0, 2)$-tensor field on spacetime. The Maxwell equations $dF = 0$ and $d{*}F = J$ (using the Hodge star) are coordinate-free statements about $F$ as a differential form. Yang-Mills theory generalizes this with $F$ now a Lie-algebra-valued 2-form. Gauge theory in general is the systematic study of alternating-tensor-field-valued objects on principal bundles.

**True name:** An alternating covariant $k$-tensor on $V$ is **a $k$-multilinear functional that detects linear independence** — it vanishes on linearly dependent tuples and (for $k \leq n$) takes nonzero values on at least some bases. Operationally: alternating tensors are oriented-volume-like quantities.

---

# Examples / Corollaries

**Is an instance: the determinant $\det(v_1, \dots, v_n)$ on $\mathbb{R}^n$.** Alternating because $\det$ flips sign when two columns are swapped. It is moreover the *unique* (up to scalar) alternating $n$-tensor on $\mathbb{R}^n$, since $\dim \Lambda^n(\mathbb{R}^n{}^*) = 1$.

**Is an instance: any wedge product $\omega^1 \wedge \cdots \wedge \omega^k$ of 1-forms.** Defined by $(\omega^1 \wedge \cdots \wedge \omega^k)(v_1, \dots, v_k) = \det(\omega^i(v_j))$. Alternating by the alternating property of $\det$.

**Is an instance: the standard symplectic form on $\mathbb{R}^{2n}$.** $\omega = \sum_i dx^i \wedge dy^i = \sum_i (dx^i \otimes dy^i - dy^i \otimes dx^i)$, an alternating $(0, 2)$-tensor field. The symplectic form is **nondegenerate** ($\omega^n$ is a top form, nonzero everywhere) and **closed** ($d\omega = 0$); it is the geometric structure underlying Hamiltonian mechanics.

**Is an instance: the volume form on an oriented Riemannian manifold.** $\mathrm{vol}_g = \sqrt{|\det g|}\, dx^1 \wedge \cdots \wedge dx^n$ in coordinates. An alternating $n$-form, the unique (up to sign) unit-norm top form on an oriented Riemannian manifold, the integrand of the volume integral.

**Is an instance: the electromagnetic field strength $F_{\mu\nu}$ in special relativity.** An antisymmetric $(0, 2)$-tensor field on Minkowski space, encoding the electric and magnetic fields as $F_{0i} = E_i$ and $F_{ij} = -\epsilon_{ijk}B^k$. The antisymmetry $F_{\mu\nu} = -F_{\nu\mu}$ is intrinsic — the field strength is alternating by construction.

**Is NOT an instance: the metric tensor $g_{ij}$.** Symmetric, $g_{ij} = g_{ji}$, hence *not* alternating (except for the trivial case $g = 0$, which is not a metric). The metric and the symplectic form are the two prototypical $(0, 2)$-tensors, occupying opposite symmetry types.

**Is NOT an instance: a sum of a symmetric and an alternating tensor with both nonzero, e.g. $g + \omega$.** A tensor with mixed symmetric and alternating parts is *neither* symmetric nor alternating; only the projections $\mathrm{Sym}(g + \omega) = g$ and $\mathrm{Alt}(g + \omega) = \omega$ have definite symmetry type.

**Is NOT an instance: a $(0, k)$-tensor with $k > n$ on an $n$-manifold.** Such a tensor field has $\binom{n}{k} = 0$ independent components for $k > n$, so $\Lambda^k(T^*M) = 0$ — there is no nonzero alternating $k$-form for $k > n$. (Note: general covariant $k$-tensor fields for $k > n$ are *not* zero — there are $n^k$ components — but the alternating subspace is trivial.)

**Corollary (dimension).** $\dim \Lambda^k(V^*) = \binom{n}{k}$, with $\Lambda^k(V^*) = 0$ for $k > n$ and $\dim \Lambda^n(V^*) = 1$.

**Corollary (basis).** A basis of $\Lambda^k(V^*)$ is given by $\{\varepsilon^{i_1} \wedge \cdots \wedge \varepsilon^{i_k} : 1 \leq i_1 < i_2 < \cdots < i_k \leq n\}$, the wedge products of the dual basis indexed by *strictly increasing* tuples. The number of such tuples is $\binom{n}{k}$, agreeing with the dimension count. The strict inequality is forced because $\varepsilon^i \wedge \varepsilon^i = 0$ (alternation kills repeated arguments).

**Corollary (1-tensors are both symmetric and alternating).** $\Lambda^1(V^*) = T^1(V^*) = V^* = \Sigma^1(V^*)$. The vacuous-symmetry phenomenon: for $k = 1$ there are no pairs of indices to swap, so the conditions for symmetric and alternating coincide and are automatic.

**Calibration check.** If you have understood the definition, you should be able to: (i) compute $\dim \Lambda^2(\mathbb{R}^3{}^*) = \binom{3}{2} = 3$ and verify a basis $dx \wedge dy, dx \wedge dz, dy \wedge dz$ has 3 elements; (ii) verify that for $\omega \in \Lambda^k(V^*)$ and $v \in V$ with $v$ in the image of some other argument, $\omega(\dots, v, \dots, v, \dots) = 0$; (iii) check that the cross product $u \times v$ on $\mathbb{R}^3$ corresponds, via the Hodge star, to the alternating 2-form $\omega(a, b) = \det(u, v, a, b)$ — wait, that does not type-check; the actual statement is that the *Hodge dual* of $u \times v$ as a vector is the 2-form $\iota_{(u \times v)}(\mathrm{vol})$. For a clean version, just verify that on $\mathbb{R}^3$ the 2-form $\omega = a\, dy\wedge dz + b\, dz\wedge dx + c\, dx\wedge dy$ has $\omega(e_1, e_2) = c, \omega(e_2, e_3) = a, \omega(e_3, e_1) = b$, identifying its components with a vector $(a, b, c)$.

---

# Unlocked by This

> [!tip] Differential k-Form *(from [[Differential Geometry VIII — Differential Forms]])*
> A **differential $k$-form** on $M$ is, by definition, an alternating $(0, k)$-tensor field — i.e., a section of $\Lambda^k(T^*M)$. The whole next chapter is the development of forms with their characteristic operations: wedge product $\wedge$, exterior derivative $d$ (a first-order differential operator $\Omega^k \to \Omega^{k+1}$), interior product $\iota_X$, Lie derivative $\mathcal{L}_X$, and pullback $F^*$. These operations interact via **Cartan's magic formula** $\mathcal{L}_X = d \iota_X + \iota_X d$ and the *cochain complex* property $d^2 = 0$.

> [!tip] Volume Form and Orientation *(from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]])*
> A **volume form** on an $n$-manifold $M$ is a non-vanishing section of $\Lambda^n(T^*M)$. Equivalently, an orientation of $M$. A manifold admitting a volume form is **orientable**; the Möbius strip and the projective plane $\mathbb{RP}^2$ do not. On an oriented Riemannian manifold the metric induces a canonical volume form $\mathrm{vol}_g = \sqrt{|\det g|}\, dx^1\wedge\cdots\wedge dx^n$, which is the integrand of the [[Def - Riemannian Volume Form|Riemannian volume]] integral.

> [!tip] Symplectic Form *(from Symplectic Geometry)*
> A **symplectic form** $\omega$ on a $2n$-manifold $M$ is a closed ($d\omega = 0$), nondegenerate alternating 2-form. The geometric structure underlying Hamiltonian mechanics: position and momentum coordinates $(q^i, p_i)$ are paired by $\omega = \sum_i dp_i \wedge dq^i$. Darboux's theorem says every symplectic manifold looks locally like $(\mathbb{R}^{2n}, \omega_0)$ with the standard form, so symplectic geometry has *no local invariants* beyond dimension — a sharp contrast to Riemannian geometry, which has the curvature.

> [!tip] de Rham Cohomology *(from [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]])*
> The cohomology $H^k_{dR}(M) = \ker(d : \Omega^k \to \Omega^{k+1}) / \mathrm{im}(d : \Omega^{k-1} \to \Omega^k)$ is a topological invariant of $M$ (the de Rham theorem identifies it with singular cohomology with real coefficients). The whole construction is built on alternating tensor fields; the symmetric analogue does not produce a useful cohomology theory because the symmetric algebra is too rigid (it is just the polynomial ring).

> [!tip] Electromagnetic Field Strength *(from Special Relativity)*
> The electromagnetic field tensor $F$ is an alternating $(0,2)$-tensor field on Minkowski space, with Maxwell's equations $dF = 0$ and $d{*}F = J$ (or $\partial^\mu F_{\mu\nu} = J_\nu$ in components). The antisymmetry of $F$ is *forced* by Lorentz invariance and the no-magnetic-monopole equation; it is the prototype of how alternating tensor fields appear in gauge theory.
