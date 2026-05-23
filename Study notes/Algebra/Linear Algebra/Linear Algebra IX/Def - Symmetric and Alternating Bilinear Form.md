---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Bilinear Form"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ is a finite-dimensional vector space over a field $\mathbb{F}$ of characteristic $\neq 2$, and $\beta : V \times V \to \mathbb{F}$ is a [[Def - Bilinear Form|bilinear form]]. The set of bilinear forms is denoted $V^{(2)}$, the subset of symmetric forms $V^{(2)}_{\mathrm{sym}}$, and the subset of alternating forms $V^{(2)}_{\mathrm{alt}}$.

This is a compound page: it defines two interlocking notions — **symmetric bilinear form** and **alternating bilinear form** — because they are introduced together, decompose $V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}}$, and are mutually defined by what each *excludes* of the other.

> [!warning] Convention: characteristic $\neq 2$
> The decomposition $V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}}$ and the equivalence "alternating $\iff$ antisymmetric" both require the underlying field to have characteristic $\neq 2$. In characteristic 2, the symmetric and antisymmetric notions coincide ($-1 = 1$), but the alternating notion remains strictly stronger than the antisymmetric notion. Throughout this page we assume $\operatorname{char}(\mathbb{F}) \neq 2$, which is the universal convention in LADR.

---

# Axiom Motivation

The two notions are dual: symmetric says the form *ignores* the order of its inputs, alternating says it *reverses sign* under swap. Both are constraints on a [[Def - Bilinear Form|bilinear form]] beyond the basic bilinearity axioms, and both pick out vital subclasses.

**Why symmetric is natural.** The defining example of a bilinear form is the [[Def - Inner Product Space|inner product]] $\langle u, v\rangle$, and the inner product satisfies $\langle u, v\rangle = \langle v, u\rangle$ (in the real case). More broadly, *any quantity that measures a relationship between two vectors without preferring one over the other* should be symmetric — energy, distance, correlation, area, angle. The axiom $\rho(u, w) = \rho(w, u)$ is the algebraic encoding of "this pairing is order-blind". The diagonal $q(v) := \rho(v, v)$ is the **quadratic form** attached to $\rho$, and (in characteristic $\neq 2$) the polarisation identity recovers $\rho$ from $q$ uniquely — symmetric bilinear forms and quadratic forms carry the same information. The most important structural fact about symmetric bilinear forms is that they can always be diagonalised: there is a basis in which the matrix is diagonal, and the signs of the diagonal entries are intrinsic ([[Thm - Sylvester's Law of Inertia|Sylvester's law]]). This is what makes "the Minkowski metric has signature $(1, 3)$" a coordinate-free statement.

**Why alternating is natural.** The defining example is the determinant restricted to two columns: $\det(u\ v)$ on $\mathbb{F}^2$. Swapping the two columns of a determinant flips its sign — that *is* what "alternating" means. More broadly, *any quantity that measures a signed area, oriented volume, or chirality* will be alternating. The axiom $\alpha(v, v) = 0$ — vanishing on diagonal pairs — is the algebraic encoding of "this pairing cannot measure a vector against itself, only against a different direction". From it follows the symmetric form's negation: $\alpha(u, w) = -\alpha(w, u)$. The whole theory of alternating multilinear forms in §9B is the generalisation of this two-input case to many inputs, culminating in the uniqueness of the determinant.

**Why we ask "$\alpha(v, v) = 0$" rather than "$\alpha(u, w) = -\alpha(w, u)$" as the definition of alternating.** The two are equivalent in characteristic $\neq 2$, so for our purposes the choice is cosmetic — but the diagonal-vanishing form is the *right* generalisation. The argument: from $\alpha(v, v) = 0$ for all $v$, apply bilinearity to $\alpha(u + w, u + w) = 0$, expand to get $\alpha(u, u) + \alpha(u, w) + \alpha(w, u) + \alpha(w, w) = 0$, and use $\alpha(u, u) = \alpha(w, w) = 0$ to conclude $\alpha(u, w) = -\alpha(w, u)$. Conversely, from $\alpha(u, w) = -\alpha(w, u)$ with $u = w$ we get $\alpha(v, v) = -\alpha(v, v)$, so $2\alpha(v, v) = 0$, hence $\alpha(v, v) = 0$ — *provided* $2 \neq 0$ in the field, that is, $\operatorname{char}(\mathbb{F}) \neq 2$. In characteristic 2, "antisymmetric" becomes the same as "symmetric" (both say $\alpha(u, w) = \alpha(w, u)$), but "alternating" remains strictly stronger. Always use the diagonal-vanishing form as the definition; it is the right notion in every characteristic and the cleanest formulation generally.

**Per-axiom failure analysis for the symmetric case.** The symmetric axiom is a *single* equation $\rho(u, w) = \rho(w, u)$. What breaks if we drop it: the matrix of $\rho$ in a basis is not symmetric, so [[Thm - Diagonalization of a Symmetric Bilinear Form|diagonalisation]] fails — there is no basis in which the form looks like $\sum \lambda_i x_i^2$. What breaks: the polarisation identity does not uniquely recover $\rho$ from $q_\rho$, because the antisymmetric part of $\rho$ has $q_\rho \equiv 0$. What is excluded if we strengthen to "positive definite" ($\rho(v, v) > 0$ for $v \neq 0$): the indefinite symmetric forms like the Minkowski metric, which have signature $(p, q)$ with $p, q \geq 1$. Strengthening to positive definite cuts away all the interesting pseudo-Riemannian content.

**Per-axiom failure analysis for the alternating case.** The alternating axiom is also a single equation $\alpha(v, v) = 0$. What breaks if we drop it: the form does not have the antisymmetry-under-swap property, so it does not behave like a determinant in two inputs. What breaks: the form can be nonzero on linearly dependent pairs (which is exactly the property the alternating axiom forbids — see the multilinear generalisation in [[Def - Alternating Multilinear Form]]). What is excluded if we strengthen to "non-degenerate alternating" ($v \mapsto \alpha(v, \cdot)$ is injective): the degenerate cases. A non-degenerate alternating form is called a **symplectic form** in characteristic $\neq 2$; it exists only on even-dimensional spaces and is the structural ingredient of symplectic geometry and Hamiltonian mechanics.

---

# The Definition

**Symmetric bilinear form.** A [[Def - Bilinear Form|bilinear form]] $\rho \in V^{(2)}$ is **symmetric** if

$$\rho(u, w) = \rho(w, u) \quad \text{for all } u, w \in V.$$

The set of symmetric bilinear forms on $V$ is denoted $V^{(2)}_{\mathrm{sym}}$ and is a [[Def - Subspace|subspace]] of $V^{(2)}$.

**Alternating bilinear form.** A bilinear form $\alpha \in V^{(2)}$ is **alternating** if

$$\alpha(v, v) = 0 \quad \text{for all } v \in V.$$

The set of alternating bilinear forms on $V$ is denoted $V^{(2)}_{\mathrm{alt}}$ and is a [[Def - Subspace|subspace]] of $V^{(2)}$.

**Symmetric matrix.** A square matrix $A$ is **symmetric** if $A = A^t$. A bilinear form $\rho$ on $V$ is symmetric if and only if its matrix in *some* (equivalently, *every*) basis of $V$ is a symmetric matrix.

**Equivalent characterisation of alternating (in characteristic $\neq 2$).** A bilinear form $\alpha$ on $V$ is alternating if and only if it is **antisymmetric**:

$$\alpha(u, w) = -\alpha(w, u) \quad \text{for all } u, w \in V.$$

The matrix of an alternating bilinear form in any basis is antisymmetric: $A^t = -A$, with zeros on the diagonal.

**Decomposition.** In characteristic $\neq 2$,

$$V^{(2)} = V^{(2)}_{\mathrm{sym}} \oplus V^{(2)}_{\mathrm{alt}},$$

via $\beta = \rho + \alpha$ with $\rho(u, w) = \tfrac{1}{2}(\beta(u, w) + \beta(w, u))$ (symmetrisation) and $\alpha(u, w) = \tfrac{1}{2}(\beta(u, w) - \beta(w, u))$ (antisymmetrisation). The intersection $V^{(2)}_{\mathrm{sym}} \cap V^{(2)}_{\mathrm{alt}} = \{0\}$, because a form both symmetric and alternating satisfies $\beta(u, w) = \beta(w, u) = -\beta(u, w)$, so $2\beta(u, w) = 0$, hence $\beta = 0$ (using $\operatorname{char} \neq 2$).

---

# Relate to Other Fields / Compression

A symmetric bilinear form is **a quadratic form with its bilinear partner remembered**. The polarisation identity $\rho(u, w) = \tfrac{1}{2}(q(u + w) - q(u) - q(w))$ shows that in characteristic $\neq 2$, the symmetric bilinear forms and the quadratic forms are in canonical bijection. The "quadratic form" presentation emphasises the values on individual vectors; the "symmetric bilinear form" presentation emphasises pairs.

An alternating bilinear form is **the antisymmetrised two-input determinant**. On $\mathbb{F}^2$, the unique alternating bilinear form up to scalar is $\alpha(u, v) = u_1 v_2 - u_2 v_1 = \det(u\ v)$. On higher-dimensional spaces, alternating bilinear forms are the "components" of an alternating multilinear gadget; the full determinant appears in §9B as an alternating $n$-linear form. The connection becomes precise via the **exterior square** $\Lambda^2 V$: alternating bilinear forms on $V$ are exactly elements of $(\Lambda^2 V)^*$, the dual of the second exterior power.

**True name of "symmetric":** order-blind, the diagonal carries all the information, polarisation recovers everything.

**True name of "alternating":** signed-area-measuring, vanishes on repeated inputs, antisymmetric under swap.

---

# Examples / Corollaries

**Is an instance (symmetric): the inner product $\langle u, v\rangle$ on a real inner product space.** Symmetric by definition of real inner product. Its matrix in any orthonormal basis is the identity. This is the prototype.

**Is an instance (symmetric): the Minkowski form $\eta(u, v) = -u_0 v_0 + u_1 v_1 + u_2 v_2 + u_3 v_3$ on $\mathbb{R}^4$.** Symmetric, with matrix $\operatorname{diag}(-1, 1, 1, 1)$ in the standard basis. Signature $(3, 1)$ (or $(1, 3)$, depending on convention). See [[Def - Minkowski Space and the Metric]].

**Is an instance (symmetric, indefinite): $\rho(u, v) = u_1 v_1 - u_2 v_2$ on $\mathbb{R}^2$.** Symmetric, with signature $(1, 1)$. The quadratic form is $q(v) = v_1^2 - v_2^2$, the hyperbolic norm-squared. This is a non-trivial example to keep in mind alongside the positive-definite inner product.

**Is an instance (alternating): the determinant $\alpha(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{F}^2$.** Alternating (set $u = v$ and get $0$), with matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.

**Is an instance (alternating): the symplectic form $\omega = dq^1 \wedge dp_1 + dq^2 \wedge dp_2 + \cdots$ on $\mathbb{R}^{2n}$.** This is the non-degenerate alternating bilinear form whose matrix in a Darboux basis is the block-diagonal $J = \begin{pmatrix} 0 & I \\ -I & 0 \end{pmatrix}$. Symplectic forms exist only on even-dimensional spaces and are the foundation of Hamiltonian mechanics.

**Is an instance (alternating, integral form): $\alpha(p, q) = \int_0^1 (pq' - p'q)\, dx$ on $\mathcal{P}_n(\mathbb{R})$.** Bilinear (integration is linear in each integrand), and alternating because $pq' - p'q$ changes sign under swap of $p$ and $q$. The matrix in the basis $(1, x, x^2, \dots)$ is antisymmetric.

**Is NOT an instance of symmetric: $\beta(p, q) = p(0) q'(1)$ on $\mathcal{P}_n(\mathbb{R})$.** Bilinear, but $\beta(1, x) = 1$ while $\beta(x, 1) = 0$, so not symmetric. Its symmetric part is $\tfrac{1}{2}(p(0)q'(1) + p'(1)q(0))$, its alternating part is $\tfrac{1}{2}(p(0)q'(1) - p'(1)q(0))$.

**Is NOT an instance of alternating: any nonzero symmetric form.** From $\alpha(v, v) = 0$, in characteristic $\neq 2$, applied to a *symmetric* form $\rho$, we have $\rho(v, v) = 0$ identically, which forces $\rho \equiv 0$ by polarisation. So $V^{(2)}_{\mathrm{sym}} \cap V^{(2)}_{\mathrm{alt}} = \{0\}$.

**Corollary (matrix characterisation).** A bilinear form is symmetric iff its matrix in *every* basis is symmetric, iff its matrix in *some* basis is symmetric. Likewise for alternating: a bilinear form is alternating iff its matrix in *every* basis is antisymmetric, iff its matrix in *some* basis is antisymmetric. The reason "some" implies "every" is the change-of-basis formula $B = C^t A C$: if $A^t = A$, then $B^t = (C^t A C)^t = C^t A^t C = C^t A C = B$.

**Corollary ([[Def - Dimension|dimensions]]).** $\dim V^{(2)}_{\mathrm{sym}} = \binom{n+1}{2} = \frac{n(n+1)}{2}$ (symmetric matrices have $n$ diagonal entries plus $\binom{n}{2}$ above-diagonal entries free). $\dim V^{(2)}_{\mathrm{alt}} = \binom{n}{2} = \frac{n(n-1)}{2}$ (antisymmetric matrices have zeros on the diagonal and $\binom{n}{2}$ above-diagonal entries free). Their sum is $n^2 = \dim V^{(2)}$, consistent with the direct-sum decomposition.

**Calibration check.** If you have understood the definitions, you should be able to verify: (i) on $\mathbb{R}^2$, the matrices $\begin{pmatrix} 1 & 2 \\ 2 & 3\end{pmatrix}$ and $\begin{pmatrix} 0 & 5 \\ -5 & 0\end{pmatrix}$ define a symmetric and an alternating bilinear form respectively; (ii) the inner product is symmetric and not alternating; the determinant of column pairs in $\mathbb{R}^2$ is alternating and not symmetric; (iii) for $\beta$ with matrix $\begin{pmatrix} 1 & 3 \\ 1 & 5\end{pmatrix}$, the symmetric part has matrix $\begin{pmatrix} 1 & 2 \\ 2 & 5\end{pmatrix}$ and the alternating part has matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$.

---

# Unlocked by This

> [!tip] Quadratic Form *(LADR §9A)*
> The diagonal $q_\rho(v) = \rho(v, v)$ of a symmetric bilinear form. See [[Def - Quadratic Form]]. The polarisation identity makes symmetric bilinear forms and quadratic forms two views of the same data.

> [!tip] Symplectic Form *(from Hamiltonian Mechanics)*
> A non-degenerate alternating bilinear form on a vector space (or pointwise on a manifold). Symplectic forms exist only on even-dimensional spaces and are the geometric structure of phase space — the form $\omega = dq \wedge dp$ encodes the relationship between positions and momenta. Hamilton's equations $\dot q = \partial H/\partial p$, $\dot p = -\partial H/\partial q$ are the symplectic form applied to the Hamiltonian's gradient.

> [!tip] Hermitian Form *(from Complex Inner Product Theory)*
> The complex analogue of a symmetric bilinear form: a sesquilinear form $h$ with $h(u, v) = \overline{h(v, u)}$. Hermitian forms diagonalise with real eigenvalues (the Hermitian analogue of Sylvester) and are the foundation of quantum mechanics: observables are Hermitian operators.

> [!tip] Pseudo-Riemannian Metric *(from Differential Geometry)*
> A smoothly varying family of non-degenerate symmetric bilinear forms on the tangent spaces of a manifold. When the signature is $(n, 0)$, this is a Riemannian metric; when $(1, n-1)$, a Lorentzian metric (the setting of general relativity).
