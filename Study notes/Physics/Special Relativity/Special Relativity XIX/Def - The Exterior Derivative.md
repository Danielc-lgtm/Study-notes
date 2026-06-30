---
type: definition
subject: special-relativity
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - The Covariant Derivative"
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. On flat spacetime $\mathscr{E}$ with arbitrary coordinates $(x^\alpha)$ and coordinate basis $\vec{e}_\alpha$, a **differential $p$-form** $A$ is a smooth field of totally antisymmetric type $(0,p)$ tensors (alternate forms of valence $p$); its components are $A_{\alpha_1\cdots\alpha_p}$ (see [[Def - Alternate Forms and the Exterior Product]]). The covariant derivative is $\boldsymbol{\nabla}$ with connection coefficients $\Gamma^\gamma{}_{\alpha\beta}$; the exterior derivative is $\mathbf{d}$; $\partial_\alpha \equiv \partial/\partial x^\alpha$; $\mathfrak{S}_{p+1}$ is the symmetric group, $k(\sigma)$ the parity of a permutation $\sigma$. Full registry on [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]].

> [!warning] Convention: flat-spacetime exterior derivative
> This is the exterior derivative on *flat* Minkowski spacetime in arbitrary coordinates. It is the **same operator** as the manifold [[Def - Exterior Derivative on a Manifold|exterior derivative]] of [[Differential Geometry VIII — Differential Forms]] — bridge between the two pages, do not merge them. The exterior derivative is independent of the metric and the connection; although the definition below uses $\boldsymbol{\nabla}$, the result depends only on the differentiable structure (the connection terms cancel). Properties — nilpotency, Leibniz, Poincaré — are on the companion page [[Thm - Properties of the Exterior Derivative]].

---

# Axiom Motivation

A differential $p$-form $A$ is a tensor field of type $(0,p)$, so it already has a covariant derivative $\boldsymbol{\nabla}A$, a type $(0,p+1)$ tensor field. Why, then, introduce a *second* derivative? Because $\boldsymbol{\nabla}A$ is the wrong kind of object: it is a field of multilinear forms of valence $p+1$, but in general it is *not* antisymmetric, so it is not a differential $(p+1)$-form. The desideratum is a derivative that sends $p$-forms to $(p+1)$-forms — that stays inside the world of differential forms — because forms are the objects one integrates (next chapter), and a derivative that produces a form is what the generalised Stokes theorem needs.

The construction is forced once you accept that requirement. The only universal way to manufacture an antisymmetric tensor from an arbitrary one is to **antisymmetrise**: average the tensor over all permutations of its slots, weighted by the sign of the permutation. Applying this to $\boldsymbol{\nabla}A$ gives the exterior derivative $\mathbf{d}A$, an antisymmetric $(p+1)$-form by construction. This is the punchline: $\mathbf{d}A$ is the antisymmetric part of the covariant derivative of $A$. Any other prescription for differentiating forms that lands in the space of forms either coincides with this (because antisymmetric tensors are determined by their action on antisymmetric arguments) or fails to be natural under coordinate changes.

Now comes the property that makes the exterior derivative far more than a bookkeeping convenience, and it is genuinely surprising: **the exterior derivative does not depend on the connection at all**. When you write out the antisymmetrised covariant derivative in a coordinate basis, each $\nabla_\alpha A_{\beta\cdots}$ contributes a partial-derivative term $\partial_\alpha A_{\beta\cdots}$ and a string of Christoffel terms $-\Gamma^\mu{}_{\cdots}A_{\cdots}$. The Christoffel terms are *symmetric* in the index pairs they couple (because the coordinate-basis Christoffels are symmetric, $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$), while the antisymmetrisation makes the whole expression antisymmetric — and a symmetric object antisymmetrised is zero. So every Christoffel term cancels, and $\mathbf{d}A$ is built from partial derivatives alone. Concretely, for a $1$-form, $(\mathbf{d}A)_{\alpha\beta} = \nabla_\alpha A_\beta - \nabla_\beta A_\alpha = (\partial_\alpha A_\beta - \Gamma^\mu{}_{\beta\alpha}A_\mu) - (\partial_\beta A_\alpha - \Gamma^\mu{}_{\alpha\beta}A_\mu) = \partial_\alpha A_\beta - \partial_\beta A_\alpha$, the Christoffels having cancelled by their symmetry.

The consequence is structural and worth stating as the real motivation. Because the Christoffels cancel, $\mathbf{d}$ would give the *same* answer for *any* connection — including no connection at all. It therefore needs no metric: where the covariant derivative requires the metric (to build the Christoffels) and so is a metric/geometric operator, the exterior derivative requires only the differentiable structure of spacetime. This is why $\mathbf{d}$ is defined on *any* smooth manifold, with or without a metric, while $\boldsymbol{\nabla}$ needs a metric (or at least a chosen connection) to exist. The split runs through the whole subject: the metric-free $\mathbf{d}$ carries the *topological* content of physics (the existence of potentials, the conservation laws, $\mathbf{d}^2 = 0$), while the metric-dependent $\boldsymbol{\nabla}$ carries the *geometric* content (proper times, curvatures, divergences). Maxwell's equations split exactly along this seam, and recognising the seam is the conceptual reason the exterior derivative deserves its own name and its own page.

One must not over-extend $\mathbf{d}$. It applies *only* to differential forms, not to general tensor fields — there is no exterior derivative of a $(1,1)$ tensor, because antisymmetrising a mixed tensor is not natural. This is the exact complement of the covariant derivative, which applies to all tensors but needs a metric. The two derivatives are not competitors; they are the two halves of differential calculus on spacetime, one antisymmetric and metric-free, the other general and metric-dependent, and the chapter needs both because physics needs both.

---

# The Definition

Let $A$ be a differential $p$-form on $\mathscr{E}$. Its **exterior derivative** $\mathbf{d}A$ is the differential $(p+1)$-form obtained by antisymmetrising the covariant derivative $\boldsymbol{\nabla}A$: for any $(p+1)$ vectors $\vec{v}_1,\dots,\vec{v}_{p+1}$,
$$\mathbf{d}A(\vec{v}_1,\dots,\vec{v}_{p+1}) := \frac{1}{p!}\sum_{\sigma\in\mathfrak{S}_{p+1}}(-1)^{k(\sigma)}\,\boldsymbol{\nabla}_{\vec{v}_{\sigma(1)}}A\big(\vec{v}_{\sigma(2)},\dots,\vec{v}_{\sigma(p+1)}\big),$$
where $k(\sigma)$ is the parity of the permutation $\sigma$.

**Low-degree cases.**
- $0$-form (scalar field $f$): $\quad\mathbf{d}f = \boldsymbol{\nabla}f$, the gradient.
- $1$-form $A$: $\quad\mathbf{d}A(\vec{v}_1,\vec{v}_2) = \langle\boldsymbol{\nabla}_{\vec{v}_1}A, \vec{v}_2\rangle - \langle\boldsymbol{\nabla}_{\vec{v}_2}A, \vec{v}_1\rangle$.
- $2$-form $A$: $\quad\mathbf{d}A(\vec{v}_1,\vec{v}_2,\vec{v}_3) = \boldsymbol{\nabla}_{\vec{v}_1}A(\vec{v}_2,\vec{v}_3) + \boldsymbol{\nabla}_{\vec{v}_2}A(\vec{v}_3,\vec{v}_1) + \boldsymbol{\nabla}_{\vec{v}_3}A(\vec{v}_1,\vec{v}_2)$.

**Components (connection form).** In any basis,
$$(\mathbf{d}f)_\alpha = \nabla_\alpha f, \qquad (\mathbf{d}A)_{\alpha\beta} = \nabla_\alpha A_\beta - \nabla_\beta A_\alpha,$$
$$(\mathbf{d}A)_{\alpha\beta\gamma} = \nabla_\alpha A_{\beta\gamma} + \nabla_\beta A_{\gamma\alpha} + \nabla_\gamma A_{\alpha\beta}, \qquad (\mathbf{d}A)_{\alpha\beta\gamma\delta} = \nabla_\alpha A_{\beta\gamma\delta} - \nabla_\beta A_{\gamma\delta\alpha} + \nabla_\gamma A_{\delta\alpha\beta} - \nabla_\delta A_{\alpha\beta\gamma}.$$

**Components (partial derivatives).** In a coordinate basis the symmetric Christoffel terms cancel under antisymmetrisation, so $\mathbf{d}$ is built from partial derivatives alone — it is **independent of the metric and the connection**:
$$\boxed{\;(\mathbf{d}f)_\alpha = \frac{\partial f}{\partial x^\alpha}\;}\qquad\boxed{\;(\mathbf{d}A)_{\alpha\beta} = \frac{\partial A_\beta}{\partial x^\alpha} - \frac{\partial A_\alpha}{\partial x^\beta}\;}$$
$$(\mathbf{d}A)_{\alpha\beta\gamma} = \frac{\partial A_{\beta\gamma}}{\partial x^\alpha} + \frac{\partial A_{\gamma\alpha}}{\partial x^\beta} + \frac{\partial A_{\alpha\beta}}{\partial x^\gamma}, \qquad (\mathbf{d}A)_{\alpha\beta\gamma\delta} = \frac{\partial A_{\beta\gamma\delta}}{\partial x^\alpha} - \frac{\partial A_{\gamma\delta\alpha}}{\partial x^\beta} + \frac{\partial A_{\delta\alpha\beta}}{\partial x^\gamma} - \frac{\partial A_{\alpha\beta\gamma}}{\partial x^\delta}.$$
The exterior derivative applies *only* to differential forms, not to general tensor fields.

---

# Categorical / Structural Definition

The exterior derivative is the unique family of $\mathbb{R}$-linear maps $\mathbf{d} : \Omega^p(\mathscr{E}) \to \Omega^{p+1}(\mathscr{E})$ (where $\Omega^p$ is the space of differential $p$-forms) characterised by three axioms: (i) on $0$-forms it is the ordinary differential, $\mathbf{d}f$ is the gradient; (ii) it is a **graded derivation** of the exterior algebra, $\mathbf{d}(A\wedge B) = \mathbf{d}A\wedge B + (-1)^{\deg A}A\wedge\mathbf{d}B$; (iii) it is **nilpotent**, $\mathbf{d}\circ\mathbf{d} = 0$. These axioms determine $\mathbf{d}$ uniquely and make no reference to a metric, which is the abstract version of the cancellation observed above. This is exactly the [[Def - Exterior Derivative on a Manifold|exterior derivative on a manifold]] of [[Differential Geometry VIII — Differential Forms]].

The triple $(\Omega^\bullet(\mathscr{E}), \wedge, \mathbf{d})$ is a **differential graded algebra**: a graded-commutative algebra (under $\wedge$) equipped with a degree-$+1$ differential ($\mathbf{d}$) squaring to zero. The cohomology of this differential — closed forms modulo exact forms — is the **de Rham cohomology** of $\mathscr{E}$, a topological invariant. On the contractible affine space $\mathscr{E}$ it is trivial (every closed form is exact, the Poincaré lemma), which is why potentials always exist on flat spacetime. The functorial content is that a smooth map pulls forms back and commutes with $\mathbf{d}$ ($\mathbf{d}\,\Phi^* = \Phi^*\,\mathbf{d}$), so $\mathbf{d}$ is **natural** — it does not depend on coordinates, and this naturality is the abstract reason it is metric-free.

---

# Relate to Other Fields / Compression

The exterior derivative is the **unification of gradient, curl, and divergence** into a single metric-free operator, and the flat-spacetime version here is identical to the manifold operator of [[Differential Geometry VIII — Differential Forms]]. On a $0$-form it is the gradient; on the metric-dual $1$-form of a vector, its Hodge dual $\star\mathbf{d}$ is the curl; and $-\star\mathbf{d}\star$ is the divergence (see [[Thm - Divergence of a Vector and Tensor Field]]). The two classical vanishing identities $\mathrm{curl}\,\mathrm{grad} = 0$ and $\mathrm{div}\,\mathrm{curl} = 0$ are both the single statement $\mathbf{d}^2 = 0$.

**True name:** $\mathbf{d}$ is *the antisymmetric part of the derivative* — antisymmetrise $\boldsymbol{\nabla}A$ and the Christoffels die, leaving the alternating sum of partial derivatives. Operationally: for a $p$-form, $\mathbf{d}A$ is the alternating sum of $\partial_{\alpha}A_{\cdots}$ over the $p+1$ slots, *with no connection terms* — use partials. The single most important fact is that $\mathbf{d}$ needs no metric, so it is the same on flat and curved spacetime and is the operator in which the homogeneous Maxwell equations $\mathbf{d}F = 0$ are automatic.

---

# Examples / Corollaries

**Is an instance — the field strength $F = \mathbf{d}A$.** If $A$ is the electromagnetic potential $1$-form, its exterior derivative is the field-strength $2$-form $F$ with $F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$ — exactly the antisymmetric combination whose six independent components are the electric and magnetic fields. That $F$ is an exterior derivative immediately gives $\mathbf{d}F = 0$, the homogeneous Maxwell pair.

**Is an instance — the curl, as a component of $\star\mathbf{d}$.** For a vector field $\vec{v}$ on a spacelike hyperplane, with metric-dual $1$-form $\underline{v}$, the components of $\star\mathbf{d}\underline{v}$ reproduce the ordinary three-dimensional curl: $(\nabla\times\vec{v})^i = [i,j,k]\,\partial v^k/\partial x^j$ in Cartesian coordinates. So "$\mathbf{d}$ of a $1$-form" is the curl up to a Hodge star — the exterior derivative *is* a generalised curl.

**Is an instance — the gradient $\mathbf{d}f$.** For a scalar $f$, $(\mathbf{d}f)_\alpha = \partial f/\partial x^\alpha$ in every coordinate system. The $1$-form $\mathbf{d}f$ is the gradient as a covector; it is closed, $\mathbf{d}(\mathbf{d}f) = 0$, which is $\mathrm{curl}\,\mathrm{grad} = 0$.

**Is NOT an instance — a "derivative" that keeps the Christoffels.** The combination $\partial_\alpha A_\beta - \partial_\beta A_\alpha - \Gamma^\mu{}_{\beta\alpha}A_\mu + \Gamma^\mu{}_{\alpha\beta}A_\mu$ is *not* a different exterior derivative — the last two terms cancel by $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$, returning $\partial_\alpha A_\beta - \partial_\beta A_\alpha$. There is no metric-dependent variant of $\mathbf{d}$; attempting one double-counts and produces a non-tensorial expression.

**Is NOT an instance — $\mathbf{d}$ of a non-form.** A type $(1,1)$ tensor field has no exterior derivative: antisymmetrising a mixed tensor is not a natural operation, and the result would not transform tensorially. The exterior derivative is defined on differential forms only — its scope is exactly complementary to that of $\boldsymbol{\nabla}$.

**Corollary — the dual basis is exact.** The dual basis of a coordinate basis is $e^\alpha = \mathbf{d}x^\alpha$, the exterior derivative of the coordinate function $x^\alpha$ regarded as a scalar field. Hence every coordinate $1$-form $\mathbf{d}x^\alpha$ is closed, $\mathbf{d}(\mathbf{d}x^\alpha) = 0$, and a general $p$-form expands as $A = \sum_{\alpha_1<\cdots<\alpha_p}A_{\alpha_1\cdots\alpha_p}\,\mathbf{d}x^{\alpha_1}\wedge\cdots\wedge\mathbf{d}x^{\alpha_p}$.

**Calibration check.** You should be able to (i) write $(\mathbf{d}A)_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha$ and explain why no Christoffel terms appear; (ii) state why $\mathbf{d}$ needs no metric while $\boldsymbol{\nabla}$ does; and (iii) recognise $F = \mathbf{d}A$ and conclude $\mathbf{d}F = 0$ without computation.

---

# Unlocked by This

> [!tip] De Rham Cohomology *(from Differential Geometry and Algebraic Topology)*
> The maps $\Omega^0 \xrightarrow{\mathbf{d}} \Omega^1 \xrightarrow{\mathbf{d}} \cdots \xrightarrow{\mathbf{d}} \Omega^4$ with $\mathbf{d}^2 = 0$ form a cochain complex, and its cohomology (closed forms modulo exact) is the **de Rham cohomology**, a topological invariant of the underlying space. On the contractible affine spacetime it is trivial; on spaces with holes it counts the holes. This is the bridge from the local calculus of forms to global topology, and it is why the existence of potentials is a topological question. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

> [!tip] Maxwell's Equations *(from Electromagnetism)*
> Written with the exterior derivative, electromagnetism is two equations: $\mathbf{d}F = 0$ (homogeneous, automatic since $F = \mathbf{d}A$ and $\mathbf{d}^2 = 0$) and $\mathbf{d}\star F = \mu_0\star J$ (inhomogeneous, using the Hodge star). The first pair is metric-free and manifestly coordinate-invariant; the second uses the metric through $\star$. This is the cleanest possible statement of Maxwell's theory, and it lives natively on Minkowski space. See [[Special Relativity XXII — Maxwell's Equations]].

> [!tip] Stokes' Theorem *(from Integration on Manifolds)*
> The exterior derivative is the operator in the generalised Stokes theorem $\int_{\partial\Omega}\omega = \int_\Omega\mathbf{d}\omega$, which unifies the fundamental theorem of calculus, Green's theorem, the divergence theorem, and the classical Stokes theorem. The pairing of $\mathbf{d}$ (on forms) with $\partial$ (on regions) — adjoint operators, since "$\mathbf{d}$ and $\partial$ are dual" — is the content of the theorem, and it is the engine of every conservation law in the following chapters. See [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem]] and [[Thm - Stokes' Theorem on Manifolds]].
