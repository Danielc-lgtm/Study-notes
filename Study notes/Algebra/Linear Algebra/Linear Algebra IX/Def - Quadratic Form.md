---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Bilinear Form"
  - "Def - Symmetric and Alternating Bilinear Form"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$ of characteristic $\neq 2$. A quadratic form on $V$ is a function $q : V \to \mathbb{F}$. For a [[Def - Bilinear Form|bilinear form]] $\beta$ on $V$, the **associated quadratic form** is $q_\beta(v) := \beta(v, v)$.

> [!warning] Convention: characteristic $\neq 2$
> The polarisation identity (and the bijection between quadratic forms and symmetric bilinear forms) requires the factor $\frac{1}{2}$, hence $\operatorname{char}(\mathbb{F}) \neq 2$.

---

# Axiom Motivation

A quadratic form is what you get when you fold a bilinear form's two inputs into one. The motivating examples are the squared norm $\|v\|^2 = \langle v, v\rangle$ on a real inner product space, the kinetic energy $T(v) = \tfrac{1}{2} m\|v\|^2$ of a moving particle, the proper time $\tau^2 = -\eta(v, v) = c^2 t^2 - \|\vec x\|^2$ in special relativity, and the second-derivative test $q(h) = \tfrac{1}{2} h^t H h$ for the Hessian $H$ at a critical point. All of these are functions $V \to \mathbb{F}$ that are *homogeneous of degree 2* — scaling $v$ by $\lambda$ scales $q(v)$ by $\lambda^2$ — and have the structure of a "diagonal evaluation" of some symmetric pairing.

The key conceptual move is: a quadratic form *looks like* a function of one vector, but it secretly *is* a symmetric bilinear form. In characteristic $\neq 2$, every quadratic form arises from a *unique* symmetric bilinear form via the diagonal $q(v) = \rho(v, v)$, and conversely $\rho$ is recovered from $q$ via the **polarisation identity** $\rho(u, w) = \tfrac{1}{2}(q(u + w) - q(u) - q(w))$. So we have two equivalent presentations of the same data, and we choose between them according to which view is more useful: the quadratic form perspective is natural when computing values on individual vectors (energies, lengths, second-derivative tests), and the bilinear form perspective is natural when relating two different vectors (orthogonality, projections, change-of-basis).

**Why "polarisation" is the right inversion formula.** Given a symmetric bilinear form $\rho$, the polarisation identity is checked directly: $\tfrac{1}{2}(\rho(u + w, u + w) - \rho(u, u) - \rho(w, w)) = \tfrac{1}{2}(\rho(u, w) + \rho(w, u)) = \rho(u, w)$, using symmetry in the last step. So $q$ determines $\rho$ uniquely. The argument requires $\operatorname{char}(\mathbb{F}) \neq 2$ for the factor of $\tfrac{1}{2}$; in characteristic 2 this fails and there are quadratic forms not arising from any bilinear form (and bilinear forms with the same associated quadratic form). This is one of the principal reasons "characteristic $\neq 2$" recurs throughout the chapter.

**Why we must restrict to *symmetric* bilinear forms.** Without the symmetry restriction, the map $\beta \mapsto q_\beta$ from bilinear forms to quadratic forms is *not* injective: any antisymmetric form has $q_\alpha(v) = \alpha(v, v) = 0$, so $\beta + \alpha$ and $\beta$ have the same associated quadratic form whenever $\alpha$ is alternating. The unique symmetric bilinear form $\rho$ realising a given quadratic form $q$ is the one with no alternating piece. This is a clean instance of the general decomposition $V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}}$: the quadratic form sees only the symmetric component.

**Why we don't just call it a "homogeneous-of-degree-2 function".** The condition $q(\lambda v) = \lambda^2 q(v)$ alone is too weak — it does not even force $q$ to be a polynomial in coordinates. Consider $q(x, y) = x^2 \cdot \operatorname{sign}(x)$ on $\mathbb{R}^2$ (with $\operatorname{sign}(0) = 0$): this is degree-2 homogeneous but is not a quadratic form, because it is not a polynomial. The additional condition we need is that $(u, w) \mapsto q(u + w) - q(u) - q(w)$ be bilinear — that is, the polarisation candidate is itself a bilinear form. LADR's theorem 9.21 makes this precise: $q$ is a quadratic form iff $q(\lambda v) = \lambda^2 q(v)$ and the polarisation candidate is symmetric bilinear.

---

# The Definition

A **quadratic form** on $V$ is a function $q : V \to \mathbb{F}$ for which there exists a [[Def - Bilinear Form|bilinear form]] $\beta$ on $V$ such that

$$q(v) = \beta(v, v) \quad \text{for all } v \in V.$$

The notation $q_\beta$ refers to the quadratic form associated with the bilinear form $\beta$: $q_\beta(v) := \beta(v, v)$.

**Equivalent characterisation (LADR 9.21).** Over a field of characteristic $\neq 2$, the following are equivalent for a function $q : V \to \mathbb{F}$:

1. $q$ is a quadratic form.
2. There exists a **unique** symmetric bilinear form $\rho$ on $V$ with $q = q_\rho$.
3. $q(\lambda v) = \lambda^2 q(v)$ for all $\lambda \in \mathbb{F}$, $v \in V$, and the function $(u, w) \mapsto q(u + w) - q(u) - q(w)$ is a symmetric bilinear form on $V$.

**Polarisation identity (the inversion formula).** Given a quadratic form $q$, the unique symmetric bilinear form $\rho$ with $q = q_\rho$ is recovered by

$$\rho(u, w) = \tfrac{1}{2}\big( q(u + w) - q(u) - q(w) \big).$$

**Coordinate form (LADR 9.20).** A function $q : \mathbb{F}^n \to \mathbb{F}$ is a quadratic form if and only if there exist scalars $A_{jk} \in \mathbb{F}$ (for $j, k \in \{1, \dots, n\}$) such that

$$q(x_1, \dots, x_n) = \sum_{j, k = 1}^n A_{jk} x_j x_k.$$

The matrix $A = (A_{jk})$ can be chosen symmetric (replacing $A_{jk}$ by $\tfrac{1}{2}(A_{jk} + A_{kj})$ if necessary), and is uniquely determined by $q$ as the symmetric matrix of the associated symmetric bilinear form.

**Diagonalisation (LADR 9.23).** For every quadratic form $q$ on a finite-dimensional space $V$, there exists a basis $(e_1, \dots, e_n)$ of $V$ and scalars $\lambda_1, \dots, \lambda_n \in \mathbb{F}$ such that

$$q(x_1 e_1 + \cdots + x_n e_n) = \lambda_1 x_1^2 + \cdots + \lambda_n x_n^2$$

for all $x_1, \dots, x_n \in \mathbb{F}$. When $\mathbb{F} = \mathbb{R}$ and $V$ is an inner product space, the basis can be chosen orthonormal. The number of positive, negative, and zero $\lambda_i$ — the signature — is an intrinsic invariant by [[Thm - Sylvester's Law of Inertia|Sylvester's law]].

---

# Relate to Other Fields / Compression

A quadratic form is **a symmetric bilinear form's diagonal**. The polarisation identity gives a canonical bijection (in characteristic $\neq 2$):

$$V^{(2)}_{\mathrm{sym}} \;\longleftrightarrow\; \{\text{quadratic forms on } V\}, \qquad \rho \leftrightarrow q_\rho.$$

So everything one can say about symmetric bilinear forms can be said about quadratic forms, and vice versa.

From the analysis side, a quadratic form is **a homogeneous-degree-2 polynomial function** $V \to \mathbb{F}$. The quadratic forms are precisely the elements of degree 2 in the symmetric algebra $\operatorname{Sym}^2(V^*)$ of the dual space. From the differential-geometric side, a quadratic form on $V$ is the same data as a $(0, 2)$-tensor that has been symmetrised — the symmetric part of a tensor of type $(0, 2)$ on a single point.

**True name:** A quadratic form is "the squared norm of a vector under some pairing". In linear algebra terms, the diagonal of a symmetric bilinear form.

The polarisation identity is the most-used inversion formula in analysis as well: for *any* function $q$ defined on a vector space, the bilinear-form candidate $\rho_q(u, w) := \tfrac{1}{2}(q(u + w) - q(u) - q(w))$ is the *symmetric part* of "$q$ thought of as a bilinear form at zero", and asking when $q$ is recovered exactly from this candidate is a foundational question.

---

# Examples / Corollaries

**Is an instance: the squared norm $q(v) = \|v\|^2$ on a real inner product space.** Here $q = q_\rho$ where $\rho(u, w) = \langle u, w\rangle$. The polarisation identity gives the famous formula

$$\langle u, w\rangle = \tfrac{1}{2}(\|u + w\|^2 - \|u\|^2 - \|w\|^2),$$

which is what allows one to *recover* an inner product from its induced norm — a deep fact (the parallelogram law characterises norms that come from inner products). This is the prototype quadratic form.

**Is an instance: the kinetic energy $T(v) = \tfrac{1}{2} m \|v\|^2$ of a particle.** A scaled squared norm, hence a quadratic form. The fact that doubling the speed quadruples the kinetic energy is the $\lambda^2$ homogeneity.

**Is an instance: the proper-time squared $\tau^2 = -\eta(v, v) = c^2 t^2 - \|\vec x\|^2$ in special relativity.** The quadratic form of the [[Def - Minkowski Space and the Metric|Minkowski metric]] has signature $(1, 3)$, and the proper-time-squared is the associated quadratic form (with a sign convention). The fact that it can be negative (for spacelike-separated events) reflects the indefinite signature.

**Is an instance: the second-order Taylor expansion of a smooth function.** For a smooth $f : \mathbb{R}^n \to \mathbb{R}$ with $f(x_0) = 0$ and $\nabla f(x_0) = 0$, the leading-order behaviour near $x_0$ is

$$f(x_0 + h) = \tfrac{1}{2} h^t H h + O(\|h\|^3),$$

where $H$ is the Hessian. The map $h \mapsto \tfrac{1}{2} h^t H h$ is a quadratic form on $\mathbb{R}^n$, and its signature classifies the critical point: $(n, 0)$ is a local minimum, $(0, n)$ a maximum, anything else is a saddle.

**Is an instance: $q(x, y) = x^2 + 2xy + 3y^2$ on $\mathbb{R}^2$.** A polynomial of degree 2, hence a quadratic form. The associated symmetric matrix is $\begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}$ (note the $2xy$ contributes $1$ to each off-diagonal entry, since $A_{12} x y + A_{21} y x = 2 A_{12} xy$ in the symmetric case). Diagonalising, the eigenvalues are $2 \pm \sqrt{2}$, both positive, so $q$ is positive definite with signature $(2, 0)$.

**Is an instance: the determinant in two dimensions.** On $\mathbb{F}^2$ with $v = (x, y)$, the quadratic form $q(v) = \det(v\ v) = xy - yx = 0$ is identically zero — because the determinant of two equal columns is zero. This illustrates that *alternating* bilinear forms have *zero* associated quadratic form, which is why the quadratic form sees only the symmetric part.

**Is NOT an instance: the function $f(v) = \|v\|$ on a real inner product space.** Degree-1 homogeneous, not degree-2: $f(\lambda v) = |\lambda| \|v\|$, not $\lambda^2 \|v\|$. So the norm itself is not a quadratic form; only its square is.

**Is NOT an instance: $q(x, y) = x^3 - y^3$ on $\mathbb{R}^2$.** Homogeneous (degree 3) but not degree-2, so not a quadratic form. The polarisation candidate $(u, w) \mapsto q(u + w) - q(u) - q(w)$ here gives $3(u_1^2 w_1 + u_1 w_1^2) - 3(u_2^2 w_2 + u_2 w_2^2)$, which is not bilinear (each term is cubic in $(u, w)$, not bilinear).

**Is NOT an instance: $q(v) = \|v\|^2 + 1$ on a real inner product space.** Not homogeneous: $q(0) = 1 \neq 0$, but any quadratic form satisfies $q(0) = \beta(0, 0) = 0$. So affine functions of quadratic forms are not quadratic forms.

**Corollary (uniqueness of the symmetric realisation).** If $q$ is a quadratic form and both $\rho_1, \rho_2$ are symmetric bilinear forms with $q_{\rho_1} = q_{\rho_2} = q$, then $\rho_1 = \rho_2$. Reason: $q_{\rho_1 - \rho_2} = 0$, so $\rho_1 - \rho_2 \in V^{(2)}_{\mathrm{sym}} \cap V^{(2)}_{\mathrm{alt}}$ (it is symmetric by hypothesis, and alternating because its associated quadratic form is zero), hence $\rho_1 - \rho_2 = 0$.

**Corollary (positive definite quadratic forms ↔ inner products).** A quadratic form $q$ on a real vector space is **positive definite** if $q(v) > 0$ for all $v \neq 0$. The positive-definite quadratic forms are in bijection with the inner products on $V$, via $\rho_q$. Every choice of inner product is a choice of positive-definite quadratic form, and vice versa.

**Calibration check.** If you have understood the definition, you should be able to: (i) starting from the quadratic form $q(x, y) = 3x^2 - 4xy + 7y^2$, recover the symmetric bilinear form $\rho((x, y), (x', y')) = 3xx' - 2(xy' + x'y) + 7yy'$ (note the factor of $\tfrac{1}{2}$ converts the $-4xy$ coefficient to $-2$ off-diagonal); (ii) verify the polarisation identity for the squared norm in two dimensions; and (iii) identify the signature of the quadratic form $q(x, y, z) = x^2 - y^2$ on $\mathbb{R}^3$ as $(1, 1, 1)$ (one positive, one negative, one zero — the form is degenerate because $z$ does not appear).

---

# Unlocked by This

> [!tip] Hessian Test for Critical Points *(from Multivariate Analysis)*
> At a critical point of a smooth function, the second-order behaviour is governed by the quadratic form $h \mapsto \tfrac{1}{2} h^t H h$ of the Hessian. The signature of this quadratic form classifies the critical point. See the [[Def - The Total Derivative and Differentiability|total derivative]] and Hessian formalism.

> [!tip] Energy Functional *(from PDE Analysis)*
> Many variational problems are minimisations of a quadratic-form-like energy: $E(u) = \tfrac{1}{2}\int |\nabla u|^2 \, dx + \int V(x) u^2\, dx$ on a function space. The Euler-Lagrange equation is the gradient of this energy, and the second-variation analysis uses the *bilinear form* associated with $E$.

> [!tip] Conic Sections and Quadrics *(from Geometry)*
> An ellipse, hyperbola, or parabola in $\mathbb{R}^2$ is a level set of a quadratic form plus a linear plus a constant; the classification is governed by the signature of the quadratic part. In higher dimensions, *quadric surfaces* (ellipsoids, hyperboloids, cones) are classified the same way — their geometry is determined entirely by the signature of the underlying quadratic form (Sylvester's law again).

> [!tip] Bilinear Form on a Lie Algebra (Killing Form) *(from Lie Theory)*
> The Killing form $K(X, Y) = \operatorname{tr}(\operatorname{ad}_X \operatorname{ad}_Y)$ on a Lie algebra is symmetric and bilinear. Its non-degeneracy is the **Cartan criterion** for semisimplicity, and its signature classifies real semisimple Lie algebras.
