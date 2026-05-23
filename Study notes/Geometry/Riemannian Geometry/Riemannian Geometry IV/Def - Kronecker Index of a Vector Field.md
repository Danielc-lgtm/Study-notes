---
type: definition
subject: differential-topology
prereqs:
  - "Def - Brouwer Degree of a Map"
  - "Def - Vector Field on a Manifold"
  - "Def - Orientation of a Smooth Manifold"
tags: [topology, differential-topology, vector-fields, index]
---

# Notation

Let $M^n$ be a closed oriented smooth $n$-manifold and $v$ a continuous (typically smooth) vector field on $M$ with isolated zeros — a finite set of points $\{p_1, \ldots, p_k\}$ at each of which $v(p_i) = 0$ and at each of which $v$ is nonzero on a deleted neighbourhood. A small ball around $p_i$ is $B_\epsilon(p_i)$ and its boundary sphere is $S^{n-1}_\epsilon(p_i) = \partial B_\epsilon(p_i)$. Full registry on [[Riemannian Geometry IV — Classical Geometry of Surfaces in R^3]].

---

# Axiom Motivation

The desideratum is to assign to each isolated zero $p$ of a continuous vector field $v$ an **integer "index"** $\mathrm{Ind}_p(v) \in \mathbb{Z}$ measuring the **topological behaviour of $v$ near $p$** — how the direction of $v$ rotates as one circles around $p$. The index should: (i) be an integer (to give a clean topological count); (ii) be invariant under small perturbations of $v$ that do not split the zero; (iii) add up over isolated zeros to give a topological invariant of $M$ (the Euler characteristic, via [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf]]).

**Why look at $v/|v|$ on a small sphere?** Near an isolated zero $p$, the field $v$ is nonzero on a deleted neighbourhood, so $v/|v|$ is a well-defined unit vector field on $B_\epsilon(p) \setminus \{p\}$. Restricting to the boundary sphere $S^{n-1}_\epsilon(p)$, $v/|v|$ becomes a map $S^{n-1}_\epsilon(p) \to S^{n-1}$ (the unit sphere in the tangent space, or in any reference Euclidean space via a local chart). This map has a well-defined Brouwer degree — and that degree is the index. The construction is natural because: (a) it only uses the *direction* of $v$ near $p$ (not its magnitude), so it captures topological data; (b) it is independent of the radius $\epsilon$ (any two small spheres give the same degree, because they bound an annulus $\{x : \epsilon_1 \leq |x| \leq \epsilon_2\}$ on which $v/|v|$ is defined, so the difference of degrees is zero by Stokes / homotopy invariance); (c) it gives an integer because Brouwer degree gives integers.

**Why "Kronecker" historically?** Kronecker studied integrals of the form $\int_{\partial U}\det(f, df)/|f|^{n+1}\, d\sigma$ (where $f : U \to \mathbb{R}^n$ has no zeros on $\partial U$) in the $19$th century, before Brouwer formalised degree theory. Kronecker's integral counts the number of solutions of the equation $f = 0$ in $U$, with signs depending on the Jacobian. This is exactly the modern Brouwer degree of $f/|f| : \partial U \to S^{n-1}$, applied to a vector-field-zero scenario. The name "Kronecker index" survives in older literature; the modern equivalent is "Brouwer degree of $v/|v|$ on a small sphere" or **Poincaré–Hopf index**.

**Why "isolated" zeros?** If the zero set of $v$ contains a positive-dimensional subset (a curve, a surface, etc.), the unit-vector-field map $v/|v|$ is not defined at all those points, and the boundary-sphere construction does not apply. For non-isolated zero sets, one needs the more general apparatus of **characteristic classes** of the zero set, which is beyond the scope of the classical index theory.

**Why does the index add over zeros to give a topological invariant?** This is the content of the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]]: $\sum_p \mathrm{Ind}_p(v) = \chi(M)$ for any vector field with isolated zeros on a closed oriented manifold. The key fact: the index of $v$ on the boundary of a region $U \subset M$ equals the sum of indices at the zeros of $v$ inside $U$ (an additivity / "excision" property). Taking $U = M$, the boundary is empty, so the "boundary index" must somehow account for the topology of $M$ — and the answer is $\chi(M)$.

A forward reference: the index is the bridge between **vector-field analysis** and **algebraic topology**. It says that any tangent vector field on a closed oriented surface "sees" the Euler characteristic — there is no way to put a vector field on $S^2$ without forcing the index sum to equal $\chi(S^2) = 2$, which means at least one zero must exist (since indices are integers and can sum to $2$ in many ways but none with zero terms summing to $\neq 0$). This is the **hairy ball theorem** in essence.

---

# The Definition

> **Definition (Kronecker / Poincaré–Hopf Index at an Isolated Zero).** Let $M^n$ be an oriented smooth manifold and $v$ a continuous vector field on $M$ with an isolated zero at $p \in M$. Choose a chart $(U, \varphi)$ around $p$ with $\varphi(p) = 0$ and a Euclidean ball $B_\epsilon(0) \subset \varphi(U)$ small enough that $p$ is the only zero in $\varphi^{-1}(B_\epsilon(0))$. The **Kronecker index** (or **Poincaré–Hopf index**) of $v$ at $p$ is
> $$
> \mathrm{Ind}_p(v) := \deg\left(\frac{v}{|v|} : S^{n-1}_\epsilon \to S^{n-1}\right) \;\in \mathbb{Z},
> $$
> the [[Def - Brouwer Degree of a Map|Brouwer degree]] of the unit-vector-field map on the boundary sphere.

The index is independent of $\epsilon$ (any two small radii give the same degree by homotopy invariance applied on the annulus), and independent of the chart $\varphi$ (any two charts give the same degree because orientation-preserving diffeomorphisms preserve the degree of the unit-vector map). So the definition is unambiguous.

> **Definition (Kronecker Index on a Boundary).** Let $U^{n+1} \subset \mathbb{R}^{n+1}$ be a compact region with smooth boundary $M^n = \partial U$, oriented with the outward normal. Let $v$ be a continuous unit vector field on $M$ (i.e., $|v| = 1$ everywhere on $M$; not required to be tangent to $M$). The **Kronecker index of $v$ on $M$** is
> $$
> \mathrm{Ind}(v; M) := \deg(v : M \to S^n),
> $$
> the Brouwer degree of $v$ as a map to the unit sphere $S^n \subset \mathbb{R}^{n+1}$.

For a non-unit but nowhere-zero $v$, replace $v$ with $v/|v|$; the result is the same.

**Index additivity (Frankel 8.3(10)).** If $v$ is defined on $\overline U$ except for isolated zeros $\{p_1, \ldots, p_k\}$ inside $U$, then
$$
\mathrm{Ind}(v; \partial U) = \sum_{i=1}^k \mathrm{Ind}_{p_i}(v).
$$
**Proof:** Excise small balls $B_\epsilon(p_i)$ from $U$; on the remaining region $U' = U \setminus \bigsqcup B_\epsilon(p_i)$, $v/|v|$ is a continuous unit field. By Stokes / degree-on-annulus, the degree on $\partial U$ equals the sum of degrees on each $-\partial B_\epsilon(p_i)$ (with the minus sign because the orientation of the inner boundary is opposite to the outward orientation of $U$, but the index at the zero is defined with the outward orientation of the small sphere — these signs cancel). Hence index on $\partial U$ = sum of indices at zeros inside.

---

# Categorical / Structural Definition

Structurally, the index is the **local Brouwer degree** of the section $v$ of the tangent bundle $TM \to M$, computed by projecting onto the unit-sphere bundle of $TM$ near the zero. From the bundle viewpoint, a vector field is a section $s : M \to TM$ with $\pi \circ s = \mathrm{id}_M$; zeros are intersections of $s(M)$ with the zero-section, and the index at an isolated intersection is the local intersection number — analogous to intersection number in intersection theory.

The total index sum is the **Euler number** of the tangent bundle $e(TM) \in \mathbb{Z}$:
$$
\sum_p \mathrm{Ind}_p(v) = e(TM) = \chi(M),
$$
where the last equality (for closed oriented $M$) is the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]]. So the index theory of vector fields is exactly the **Euler-class** computation for $TM$.

For higher-rank vector bundles $E \to M$ of rank $r$, the analogue is the Euler class $e(E) \in H^r(M; \mathbb{Z})$, computable as the index sum of any generic section. For oriented rank-$r$ bundles over closed oriented $r$-manifolds, this Euler number is an integer; for higher-dimensional base manifolds, the Euler class is a cohomology class of degree $r$.

Functorially: the index is invariant under orientation-preserving diffeomorphisms (pulling back $v$ along a diffeomorphism gives the same index at the corresponding zero), reverses sign under orientation-reversing diffeomorphisms, and is multiplicative under products (the index of a product zero is the product of indices).

---

# Relate to Other Fields / Compression

The Kronecker index is the **degree-theoretic count of how a vector field rotates near a zero**, generalising the **winding number** of a planar vector field to higher dimensions. For a planar vector field $v(x, y)$ with isolated zero at the origin, the index is the winding number of the curve $(v_1(\theta), v_2(\theta))/|v|$ as $\theta$ traces a small circle — exactly the winding number from complex analysis.

In **complex analysis**, for a holomorphic vector field $f(z)\partial_z$ on a Riemann surface, the index at an isolated zero $z_0$ equals the **algebraic order of vanishing** of $f$ at $z_0$ — the integer $n$ such that $f(z) = (z - z_0)^n g(z)$ with $g(z_0) \neq 0$. This is the **argument principle** in disguise: $\mathrm{Ind} = (1/2\pi i)\oint(f'/f)\, dz$ for a meromorphic function.

In **electromagnetism**, the index of an electric field on a closed surface (with the field nonzero on the surface) is the algebraic count of enclosed charges, by Gauss's law — exactly the divergence-theorem version of index additivity.

In **fluid dynamics**, the indices of the velocity field at stagnation points on a closed surface (like the surface of a sphere or torus) satisfy the Poincaré–Hopf identity, controlling the topological structure of streamlines.

In **catastrophe theory** and **Morse theory**, the indices of the gradient field $\nabla f$ at critical points of a smooth function $f$ are exactly $\pm 1$, and Morse theory gives $\sum_p \mathrm{Ind}_p(\nabla f) = \chi(M)$ as a special case of Poincaré–Hopf — recovering Euler characteristic from the alternating sum of Morse-index counts $\sum(-1)^k c_k = \chi$, where $c_k$ is the number of critical points of Morse index $k$.

**True name:** The Kronecker index is *the algebraic count of how the field's direction rotates around the zero*. The official "Brouwer degree of $v/|v|$ on a small sphere" is the right definition, but the operational picture is: stand at the zero $p$, walk in a small circle around it, and watch the field's direction. The integer count of complete rotations (with signs for orientation) is the index. For a sink or source, +1; for a saddle, $-1$; for higher-order zeros, $\pm k$.

---

# Examples / Corollaries

**Is an instance — a source.** $v(x, y) = (x, y)$ has zero at origin; $v/|v| = (x, y)/r$ on a circle of radius $r$ is exactly the identity map of the circle, with degree $+1$. So **a source has index $+1$**.

**Is an instance — a sink.** $v(x, y) = (-x, -y)$ has zero at origin; $v/|v| = -(x, y)/r$ is the antipodal map of the circle, degree $(-1)^{1+1} = +1$ in the $n = 1$ case (the antipodal map of $S^1$ has degree $-1$, but Frankel's 8.3(1) gives $(-1)^{n+1}$ for the antipodal map of $S^n$, so on $S^1$ it is $(-1)^2 = +1$ — let me recompute: the antipodal map of $S^1$ sends $\theta \mapsto \theta + \pi$, which is rotation by $\pi$, degree $+1$). So **a sink also has index $+1$**.

**Is an instance — a saddle.** $v(x, y) = (x, -y)$ has zero at origin. On the unit circle, $v(\cos\theta, \sin\theta) = (\cos\theta, -\sin\theta)$. The angle is $-\theta$ (going clockwise instead of counterclockwise), so as $\theta$ goes from $0$ to $2\pi$, the field's angle goes from $0$ to $-2\pi$ — winding number $-1$. So **a saddle has index $-1$**.

**Is an instance — a centre.** $v(x, y) = (-y, x)$ has zero at origin. On the unit circle, $v(\cos\theta, \sin\theta) = (-\sin\theta, \cos\theta)$, with angle $\theta + \pi/2$. As $\theta$ varies through $2\pi$, the field's angle varies by $2\pi$ — winding number $+1$. So **a centre has index $+1$**.

**Is an instance — higher-order zeros.** $v(z) = z^n$ on $\mathbb{C} = \mathbb{R}^2$ (interpreted as a vector field) has zero at origin. On the unit circle $|z| = 1$, $v(z) = z^n$, with argument $n\theta$. Winding number $n$. So **the index of $z^n\partial_z$ at $0$ is $n$**. Similarly $v(z) = \bar z^n$ has index $-n$.

**Is an instance — a vector field on $S^2$.** The "flow toward the north pole" field $v$ has zeros at both poles: index $+1$ at the south pole (source-like, since $v$ flows away from south) and index $+1$ at the north pole (sink-like). Total $\sum\mathrm{Ind} = 2 = \chi(S^2)$, consistent with Poincaré–Hopf. The hairy ball theorem follows: there is no nowhere-vanishing tangent vector field on $S^2$ because $\chi(S^2) = 2 \neq 0$.

**Is NOT an instance — a non-isolated zero.** The vector field $v(x, y) = (0, x)$ has zero on the entire $y$-axis (not isolated). The index construction does not apply at non-isolated zero sets, and one needs the more sophisticated apparatus of characteristic classes to assign topological data.

**Is NOT an instance — a continuous but non-smooth field.** The construction works for continuous fields (one needs only continuity to define $v/|v|$ on a deleted neighbourhood), but **smooth** fields are usually assumed for cleanness; the integer-degree value is the same for any continuous representative within a homotopy class.

**Corollary — index is invariant under continuous deformation of $v$ that does not introduce zero crossings into a small ball.** This is just homotopy invariance of Brouwer degree, applied on the boundary sphere.

**Corollary — for a nondegenerate zero (where $dv|_p$ is invertible as a linear map), $\mathrm{Ind}_p(v) = \mathrm{sign}\det(dv|_p)$.** In a chart around $p$, write $v(x) \approx (dv|_p)x$ for small $x$. The map $v/|v|$ on a small sphere is then $((dv|_p)x)/|(dv|_p)x|$ — exactly the unit-vector map of the linear isomorphism $dv|_p$, which has degree $\mathrm{sign}\det(dv|_p) = \pm 1$. So nondegenerate zeros have index $\pm 1$ — a useful computational shortcut.

**Corollary — the index sum is $\chi(M)$.** For any vector field with isolated zeros on a closed oriented manifold, $\sum_p\mathrm{Ind}_p(v) = \chi(M)$; this is the [[Thm - Poincare-Hopf Theorem for Surfaces|Poincaré–Hopf theorem]].

**Calibration check.** If you have understood the definition, you should be able to: (i) verify that the "$x$-axis flow" $v(x, y) = (1, 0)$ on $\mathbb{R}^2$ has no zeros, so trivially has no contribution to any index sum; (ii) check that the linear field $v(x, y) = A\cdot (x, y)$ for a nondegenerate $2\times 2$ matrix $A$ has index $\mathrm{sign}\det A = \pm 1$ at the origin, recovering the source/sink/saddle classification: $A$ with both eigenvalues positive (source) or both negative (sink) gives $\det A > 0$, index $+1$; $A$ with eigenvalues of opposite signs (saddle) gives $\det A < 0$, index $-1$; (iii) compute the index of $v(z) = z^2 + 1$ at its zeros $\pm i$ on $\mathbb{C}$ — each is a nondegenerate zero of a holomorphic field, hence index $+1$ each, total $2$.

---

# Unlocked by This

> [!tip] Poincaré–Hopf Theorem *(from §4.4)*
> For any vector field with isolated zeros on a closed oriented surface, $\sum_p \mathrm{Ind}_p(v) = \chi(M)$. The sum is a topological invariant of $M$ independent of the field. See [[Thm - Poincare-Hopf Theorem for Surfaces]].

> [!tip] The Hairy Ball Theorem *(from §4.4 Exercises)*
> No nowhere-vanishing continuous tangent vector field exists on $S^2$, because any field has index sum $= \chi(S^2) = 2 \neq 0$, hence must have at least one zero. See [[Ex - Hairy Ball Theorem from Poincare-Hopf]]. The same argument shows $S^{2n}$ has no nowhere-vanishing tangent field (for $n \geq 1$); $S^{2n-1}$ does (e.g., the Hopf flow on $S^3$).

> [!tip] Morse Theory and the Morse Inequalities *(from Algebraic Topology)*
> For a Morse function $f : M \to \mathbb{R}$ on a closed manifold, the gradient field $\nabla f$ has nondegenerate critical points only, with index $(-1)^{\text{Morse index}(p)}$. Poincaré–Hopf gives $\sum_p (-1)^{\mathrm{Ind}_M(p)} = \chi(M)$ — the **Morse equality**. The full **Morse inequalities** refine this to bounds on individual Betti numbers $b_k \leq c_k$, where $c_k$ is the number of critical points of Morse index $k$.

> [!tip] The Lefschetz Fixed-Point Theorem *(from Algebraic Topology)*
> For a self-map $\phi : M \to M$ on a closed oriented manifold, the **Lefschetz number** $L(\phi) = \sum_k(-1)^k\mathrm{tr}(\phi_* : H_k \to H_k)$ equals the sum of indices of fixed points of $\phi$. If $L(\phi) \neq 0$, then $\phi$ has a fixed point. The identity case $\phi = \mathrm{id}$ recovers the Poincaré–Hopf theorem.

> [!tip] The Atiyah–Singer Index Theorem *(from Algebraic Topology III)*
> The vector-field index is the simplest "index" in a family of analytic indices for elliptic operators. The **Atiyah–Singer index theorem** generalises: for any elliptic operator on a closed manifold, the **analytic index** (dimension of kernel minus dimension of cokernel) equals a **topological index** built from characteristic classes. Poincaré–Hopf for vector fields is the case of the de Rham complex; the general theorem covers Dirac operators, signature operators, and many more — see [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
