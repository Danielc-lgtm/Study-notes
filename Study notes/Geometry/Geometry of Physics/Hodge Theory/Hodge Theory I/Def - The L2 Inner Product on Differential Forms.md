---
type: definition
subject: hodge-theory
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Riemannian Metric"
  - "Def - Riemannian Volume Form"
  - "Def - The Wedge Product on a Manifold"
tags: [geometry, hodge-theory, riemannian-geometry]
---

# Notation

$M$ is a smooth oriented Riemannian manifold of dimension $n$, with metric $g$ and orientation; $\operatorname{vol}_n = \operatorname{vol}_g$ denotes the [[Def - Riemannian Volume Form|Riemannian volume form]]. Forms are $\alpha, \beta \in \Omega^k(M)$, with $\Omega^k(M)$ the space of smooth differential $k$-forms (see [[Def - Differential k-Form on a Manifold]]). The pointwise inner product on $k$-forms induced by $g$ is written $\langle\alpha,\beta\rangle_g$ or simply $\langle\alpha,\beta\rangle$ when $g$ is fixed; the global $L^2$ inner product is $\langle\alpha,\beta\rangle_{L^2}$ or $(\alpha,\beta)$. In components on an orthonormal frame, with the convention that primed sums $\sum'_I$ run over increasing multi-indices $I = (i_1 < \cdots < i_k)$, $\langle\alpha,\beta\rangle_g = \sum'_I \alpha_I \beta^I = \alpha_I \beta^I$ (Einstein summation, with the prime understood). The wider conventions are in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Axiom Motivation

The construction is forced once you accept three desiderata: the inner product should be compatible with the metric on $M$, it should be a real inner product (positive definite) on a Riemannian manifold, and it should turn $\Omega^k(M)$ into a Hilbert-space-like object so that adjoints, projections, and orthogonal decompositions are available. Each of these constraints fixes one feature of the definition.

**Compatibility with $g$ — the pointwise inner product.** A Riemannian metric $g$ gives a positive-definite inner product on each tangent space $T_pM$. This dualizes — via the [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphism]] — to an inner product on each cotangent space $T_p^*M$, and then extends multilinearly to inner products on $\Lambda^k T_p^*M$ for each $k$. In an orthonormal coframe $\sigma^1, \dots, \sigma^n$ at $p$, the wedge products $\sigma^I = \sigma^{i_1} \wedge \cdots \wedge \sigma^{i_k}$ over increasing multi-indices $I$ form an orthonormal basis for $\Lambda^k T_p^*M$. The pointwise inner product of two $k$-forms is then $\langle\alpha,\beta\rangle_g(p) = \sum'_I \alpha_I(p)\beta_I(p)$ in this basis, where we sum only over increasing multi-indices to avoid overcounting. Equivalently, raising indices with the metric, $\langle\alpha,\beta\rangle_g = \alpha_{i_1\cdots i_k}\beta^{i_1\cdots i_k}/k!$ summed over all multi-indices. This is the unique inner product making the basis $\sigma^I$ orthonormal, and it is forced by the requirement that the inner product be compatible with the metric on $TM$.

**Positivity — the Riemannian case.** Why specifically a *positive-definite* inner product, requiring the Riemannian (not pseudo-Riemannian) hypothesis? Because we want $\|\omega\|^2 = \langle\omega,\omega\rangle$ to be a norm — so that "this form has small $L^2$ norm" is a meaningful constraint, and so that the orthogonal complement of a subspace is a well-defined complement. In the pseudo-Riemannian case (e.g., Lorentzian), the inner product is indefinite: there are nonzero $k$-forms with $\langle\omega,\omega\rangle_g = 0$ (null forms), and even nonzero forms with negative pointwise inner product (timelike forms in Lorentzian signature). The inner product is still useful for index-lowering and for defining $\star$, but it does not give a Hilbert-space structure. The full Hodge decomposition theorem requires positivity, which is why it holds for closed Riemannian manifolds but not for closed Lorentzian ones — the Laplacian on Lorentzian signature is hyperbolic (the d'Alembertian), not elliptic, and the kernel can be infinite-dimensional.

**Globalization — integration against the volume form.** A pointwise inner product is a function on $M$; integrating it against the volume form makes it a single real number — and only then is it usable as an inner product on the infinite-dimensional space $\Omega^k(M)$. The formula $\langle\alpha,\beta\rangle_{L^2} = \int_M \langle\alpha,\beta\rangle_g \operatorname{vol}_n$ is the unique extension of the pointwise inner product to a global one that respects $\mathbb{R}$-linearity in each argument. The use of the [[Def - Riemannian Volume Form|Riemannian volume form]] $\operatorname{vol}_g = \sqrt{|g|}\,dx^1\wedge\cdots\wedge dx^n$ rather than some other density is forced by orientation: integration of an $n$-form requires an orientation, and the Riemannian volume form is the unique positively oriented $n$-form with $\|\operatorname{vol}_g\|_g = 1$.

**Why the integration form is $\int_M \alpha\wedge\star\beta$.** The equivalent formulation $\langle\alpha,\beta\rangle_{L^2} = \int_M \alpha\wedge\star\beta$ uses the Hodge star to convert the inner product into a wedge product that can be integrated directly. This is essentially the defining property of $\star$: it is the unique $C^\infty(M)$-linear map $\Omega^k \to \Omega^{n-k}$ such that $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\,\operatorname{vol}_n$. So the two formulations of the $L^2$ inner product are tautologically equivalent given $\star$, and the wedge-product form is often more useful for computation (one needs to compute $\star\beta$ and then a single integral of the wedge).

**Finiteness — closed manifolds and compact support.** A subtlety: $\int_M \langle\alpha,\beta\rangle_g\operatorname{vol}_n$ need not converge for general smooth forms on a noncompact manifold. The convergence is automatic when (i) $M$ is compact (then $\langle\alpha,\beta\rangle_g$ is a continuous function on a compact manifold, hence bounded, so the integral converges); or (ii) at least one of $\alpha, \beta$ has compact support. For the Hodge theorem we need (i), the closed-manifold case; for noncompact manifolds we work with the dense subspace $\Omega^k_c(M)$ of compactly supported forms and complete to get $L^2\Omega^k(M)$.

**The completion is not the smooth forms.** The pre-Hilbert space $\Omega^k(M)$ on a compact $M$ is not complete in the $L^2$ norm — a Cauchy sequence of smooth forms may converge to a discontinuous form. The completion is the Hilbert space $L^2\Omega^k(M)$ of square-integrable forms, which contains all $L^2$ forms, not just smooth ones. For the Hodge theorem the relevant fact is that **the harmonic forms in $L^2$ are automatically smooth** (elliptic regularity), so the smooth and $L^2$ pictures of $\mathcal{H}^k$ agree.

---

# The Definition

Let $(M, g)$ be a smooth oriented Riemannian $n$-manifold (possibly with boundary).

**Pointwise inner product on $k$-forms.** The metric $g$ on $TM$ induces a metric on $T^*M$ via the [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphism]], and extends multilinearly to $\Lambda^k T^*M$. In an orthonormal coframe $(\sigma^1, \dots, \sigma^n)$ at $p \in M$, the wedge products $\sigma^I = \sigma^{i_1}\wedge\cdots\wedge\sigma^{i_k}$ for increasing $I$ form an orthonormal basis of $\Lambda^k T_p^*M$. If $\alpha = \sum'_I \alpha_I \sigma^I$ and $\beta = \sum'_I \beta_I\sigma^I$ in this basis, then
$$\langle\alpha,\beta\rangle_g(p) = \sum'_I \alpha_I(p)\,\beta_I(p),$$
extending to a smooth function $\langle\alpha,\beta\rangle_g : M \to \mathbb{R}$. Equivalently, raising indices with $g$, $\langle\alpha,\beta\rangle_g = \frac{1}{k!}\alpha_{i_1\cdots i_k}\beta^{i_1\cdots i_k}$ over all multi-indices.

**$L^2$ inner product on $k$-forms.** The **$L^2$ inner product** of two smooth $k$-forms $\alpha, \beta \in \Omega^k(M)$ is
$$\langle\alpha,\beta\rangle_{L^2} := \int_M \langle\alpha,\beta\rangle_g\,\operatorname{vol}_n = \int_M \alpha\wedge\star\beta,$$
defined whenever the integral converges (in particular, on a closed manifold, or for compactly supported forms). The two expressions are equal by the defining identity of the Hodge star, $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\,\operatorname{vol}_n$. The induced norm is $\|\omega\|_{L^2}^2 = \langle\omega,\omega\rangle_{L^2}$.

In the pseudo-Riemannian case (signature $(n-s, s)$ with $s \geq 1$), the same formulas define $\langle\cdot,\cdot\rangle_g$ and $\langle\cdot,\cdot\rangle_{L^2}$, but they are *indefinite*: there exist nonzero forms with $\langle\omega,\omega\rangle_g = 0$ or with $\langle\omega,\omega\rangle_g < 0$ at points. We then use the same notation but lose the Hilbert-space structure.

---

# Relate to Other Fields / Compression

This is the **Lebesgue $L^2$ inner product**, $\int fg \,d\mu$, applied to vector-valued ("form-valued") rather than scalar-valued functions, with the pointwise inner product on forms playing the role of the scalar product $fg$, and the Riemannian volume form playing the role of Lebesgue measure $d\mu$. In an orthonormal coframe, expanding the pointwise inner product makes the formula $\int_M \alpha\wedge\star\beta = \int_M\sum'_I \alpha_I\beta_I\operatorname{vol}_n$ literally $\int (\alpha\cdot\beta)\,d\mu$ for the "vector dot product" $\alpha\cdot\beta = \sum'_I\alpha_I\beta_I$.

On a Euclidean inner-product space (treating $\mathbb{R}^n$ as a flat Riemannian manifold), the $L^2$ inner product on $0$-forms (= functions) is the standard $\int_{\mathbb{R}^n} fg\,dx$, and on $1$-forms it is $\int_{\mathbb{R}^n}\sum_i f_i g_i\,dx$ where $\alpha = \sum f_i dx^i$ and $\beta = \sum g_i dx^i$. Higher-degree forms are similar: just the "dot product" of components followed by integration. The Riemannian generalization adds metric corrections (the index raising and the volume form $\sqrt{|g|}$).

**True name:** the $L^2$ inner product is the *unique* extension of the pointwise inner product on forms (induced by $g$) to a global bilinear form on $\Omega^k(M)$ that respects $\mathbb{R}$-linearity in each argument and is computed by integration. The metric and the volume form are both needed: the metric for the pointwise inner product (which raises indices and identifies $\Omega^k$ with itself), and the volume form for the integration (which converts a function into a number).

---

# Examples / Corollaries

**On $\mathbb{R}^n$ (Euclidean).** The $L^2$ inner product on $0$-forms is $\langle f, g\rangle_{L^2} = \int_{\mathbb{R}^n} fg\,d^n x$. On $1$-forms $\alpha = \sum_i a_i dx^i$ and $\beta = \sum_i b_i dx^i$, it is $\langle\alpha,\beta\rangle_{L^2} = \int_{\mathbb{R}^n}\sum_i a_i b_i\,d^n x$. On the volume form (top degree) $\alpha = f\,dx^1\wedge\cdots\wedge dx^n$, $\langle\alpha,\alpha\rangle_{L^2} = \int_{\mathbb{R}^n} f^2\,d^n x$.

**On the round $S^2$.** In spherical coordinates $(\theta, \varphi)$ with metric $g = d\theta^2 + \sin^2\theta\,d\varphi^2$ and volume form $\operatorname{vol}_g = \sin\theta\,d\theta\wedge d\varphi$, the orthonormal coframe is $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$. So $|d\theta|^2 = 1$ pointwise (constant on the sphere), and $|d\varphi|^2 = 1/\sin^2\theta$ (singular at the poles, but the pointwise inner product integrated against $\sin\theta$ remains finite). The $L^2$ norm $\|d\theta\|_{L^2}^2 = \int_{S^2} \sin\theta\,d\theta\,d\varphi = 4\pi$, finite.

**Is an instance: the cohomology pairing on a closed orientable manifold.** When $\alpha \in \Omega^k(M)$ and $\beta \in \Omega^{n-k}(M)$ are both closed, $\int_M \alpha\wedge\beta$ depends only on the cohomology classes $[\alpha], [\beta]$ (by Stokes' theorem). This descends to the bilinear pairing $H^k(M;\mathbb{R})\times H^{n-k}(M;\mathbb{R})\to\mathbb{R}$. Hodge theory makes the connection precise: the pairing is the $L^2$ inner product evaluated on harmonic representatives, since $\int_M\alpha\wedge\beta = \int_M\alpha\wedge\star\star^{-1}\beta = \langle\alpha,\star^{-1}\beta\rangle_{L^2}$.

**Is NOT an instance: a degenerate "inner product" from a non-Riemannian metric.** On a Lorentzian $4$-manifold, the formula $\langle\alpha,\beta\rangle_{L^2} = \int_M\alpha\wedge\star\beta$ still makes sense as a bilinear form, but it is *not* positive-definite. For a timelike $1$-form $\alpha = dt$ on Minkowski space ($g = -dt^2 + dx^2 + dy^2 + dz^2$), $|dt|^2 = g^{tt} = -1$, so $\langle dt, dt\rangle_g = -1$ everywhere. The "$L^2$ norm" $\langle dt, dt\rangle_{L^2}$ is negative — the bilinear form is indefinite. This is a non-example of an inner product: the operations of orthogonality and projection still make formal sense, but the Hilbert-space machinery is lost.

**Corollary (Cauchy–Schwarz).** $|\langle\alpha,\beta\rangle_{L^2}|^2 \leq \langle\alpha,\alpha\rangle_{L^2}\langle\beta,\beta\rangle_{L^2}$ on a closed Riemannian manifold (or for compactly supported forms). The proof is the standard one: the polynomial $t \mapsto \langle\alpha + t\beta, \alpha + t\beta\rangle_{L^2}$ is a nonnegative real quadratic in $t$, so its discriminant is nonpositive.

**Corollary (orthogonality of complementary-degree wedge integrals).** For $\alpha \in \Omega^k(M)$ and $\beta \in \Omega^\ell(M)$ with $k + \ell \neq n$, the wedge product $\alpha\wedge\beta$ is an $(k+\ell)$-form, not an $n$-form, so integrating it over $M$ does not make sense — the wedge of two non-complementary-degree forms is not directly comparable in the $L^2$ inner product. To compare forms of different degrees one must first apply $\star$ to bring them to the same degree.

**Calibration check.** If you can verify (i) the pointwise inner product is positive-definite on a Riemannian manifold (orthonormal-basis check), (ii) the formula $\langle\alpha,\beta\rangle_{L^2} = \int_M\alpha\wedge\star\beta$ is equivalent to $\int_M\langle\alpha,\beta\rangle_g\operatorname{vol}_n$ (defining identity of $\star$), and (iii) the $L^2$ norm of $d\theta$ on $S^2$ is finite (despite the coordinate singularity at the poles), you have understood the definition correctly.

---

# Unlocked by This

> [!tip] $L^2$-Cohomology *(from Geometric Analysis and Geometric Group Theory)*
> The $L^2$ inner product makes $\Omega^k(M)$ into a pre-Hilbert space; completing in the $L^2$ norm gives the Hilbert space $L^2\Omega^k(M)$ of square-integrable $k$-forms. On a noncompact Riemannian manifold (where the smooth Hodge decomposition fails), one defines **$L^2$-cohomology** $H^k_{(2)}(M) = \ker(d:L^2\Omega^k\to L^2\Omega^{k+1})/\overline{\mathrm{im}(d:L^2\Omega^{k-1}\to L^2\Omega^k)}$ (with the closure for the image, since the image need not be closed). This is the invariant that **Atiyah's $L^2$-index theorem** computes for free actions of discrete groups, and is the foundation of **Lück's approximation theorem** on Betti numbers of finite covers.

> [!tip] Variational Methods in Hodge Theory *(from Calculus of Variations)*
> The $L^2$ norm $\|\omega\|_{L^2}^2$ is the standard objective functional for variational arguments in Hodge theory. The **harmonic representative** of a de Rham cohomology class $[\omega]$ is the unique form in the class minimizing $\|\omega\|_{L^2}^2$. The **Yang–Mills connection** on a principal $G$-bundle over a Riemannian $4$-manifold minimizes $\int|F_A|^2\operatorname{vol}_g$, a curvature $L^2$ norm. The **Dirichlet energy** of a map between Riemannian manifolds is an $L^2$ norm of the differential, and its critical points are harmonic maps. The $L^2$ inner product on forms is the gateway to all of these.
