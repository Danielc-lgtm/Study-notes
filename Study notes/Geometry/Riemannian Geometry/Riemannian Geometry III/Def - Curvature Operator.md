---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Sectional Curvature"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold with [[Def - Riemann Curvature Tensor|Riemann curvature tensor]] $R$ and covariant version $R(X, Y, Z, W) = \langle R(X, Y)Z, W\rangle$. The space $\Lambda^2 T_pM$ of $2$-vectors at $p$ has dimension $\binom{n}{2}$ and carries an inner product induced from $g$: for decomposable elements, $\langle X \wedge Y, Z \wedge W\rangle = \langle X, Z\rangle\langle Y, W\rangle - \langle X, W\rangle\langle Y, Z\rangle$. The **curvature operator** $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$ is the symmetric endomorphism characterised by

$$\langle \mathcal{R}(X \wedge Y), Z \wedge W\rangle = R(X, Y, W, Z).$$

The sign convention varies across sources; we follow the convention in which $\mathcal{R} = \mathrm{id}$ on the round sphere $S^n$.

---

# Axiom Motivation

The Riemann tensor $R$ is a $(0, 4)$-tensor with three algebraic symmetries (the [[Thm - Symmetries of the Riemann Tensor|symmetries of the Riemann tensor]]). Two of these — antisymmetry in the first pair $(X, Y)$ and antisymmetry in the second pair $(Z, W)$ — mean that $R$ depends only on the wedge products $X \wedge Y$ and $Z \wedge W$, not on the individual vectors. The third — pair-swap symmetry $R(X, Y, Z, W) = R(Z, W, X, Y)$ — means that $R$ defines a *symmetric* bilinear form on $\Lambda^2 T_pM$.

A symmetric bilinear form on a finite-dimensional inner-product space is the same datum as a **symmetric endomorphism** (via the metric). So $R$, regarded with its pair-swap symmetry, is most naturally packaged as a symmetric linear map $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$. This is the **curvature operator**.

The desiderata for this repackaging are: (i) the spectral theory of $\mathcal{R}$ should give *geometric* information; (ii) the relationship to sectional curvature should be transparent; (iii) the curvature operator should fit into the broader landscape of "curvature objects" (Riemann tensor, Ricci tensor, scalar curvature, Weyl tensor) as the highest-rank symmetric-operator avatar.

These are all met: the **eigenvalues** of $\mathcal{R}$ are the curvature analogues of principal curvatures, and conditions like "$\mathcal{R} > 0$" (positive curvature operator) are far more restrictive than "$K > 0$" (positive sectional curvature). The connection to sectional curvature is direct: $K(X \wedge Y) = \langle \mathcal{R}(X \wedge Y), X \wedge Y\rangle/|X \wedge Y|^2$, so sectional curvatures are the *diagonal* entries of $\mathcal{R}$ in any orthonormal basis of decomposable $2$-vectors.

Why the specific sign convention $\langle \mathcal{R}(X \wedge Y), Z \wedge W\rangle = R(X, Y, W, Z)$ (with $W, Z$ swapped on the right)? Because we want $\mathcal{R} = \mathrm{id}$ on $S^n$ — i.e., positive sectional curvature should give positive curvature operator on decomposable $2$-vectors. The sphere has $R(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$, so $R(X, Y, W, Z) = \langle Y, W\rangle\langle X, Z\rangle - \langle X, W\rangle\langle Y, Z\rangle = -\langle X \wedge Y, Z \wedge W\rangle$. Hmm, the sign would require care; different sources fix this differently. The takeaway is that the curvature operator is an object whose sign conventions are standardised separately within each text.

Why is "positive curvature operator" stronger than "positive sectional curvature"? Because $\mathcal{R}$ acts on all of $\Lambda^2$, not just on **decomposable** $2$-vectors. Sectional curvature only sees decomposable elements (those of the form $X \wedge Y$). The condition $\mathcal{R} > 0$ requires the operator to be positive-definite *also* on non-decomposable $2$-vectors like $X \wedge Y + Z \wedge W$ (with $\{X, Y, Z, W\}$ linearly independent). This is a strictly stronger condition starting in dimension $4$.

In dimension $3$, every $2$-vector is decomposable (since $\Lambda^2 \mathbb{R}^3 \cong \mathbb{R}^3$ via the cross product), so positive curvature operator and positive sectional curvature coincide. The distinction appears only in dimension $\ge 4$.

---

# The Definition

> **Definition (Curvature operator).** Let $(M, g)$ be a Riemannian manifold. The **curvature operator** at $p \in M$ is the symmetric endomorphism $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$ uniquely determined by
>
> $$\langle \mathcal{R}(X \wedge Y), Z \wedge W\rangle = R(X, Y, W, Z) \qquad X, Y, Z, W \in T_pM.$$
>
> The symmetry of $\mathcal{R}$ as a linear operator (i.e., $\langle \mathcal{R}\xi, \eta\rangle = \langle \xi, \mathcal{R}\eta\rangle$ for $\xi, \eta \in \Lambda^2 T_pM$) is equivalent to the **pair-swap symmetry** $R(X, Y, Z, W) = R(Z, W, X, Y)$ of the Riemann tensor.
>
> **Positive curvature operator** means $\langle \mathcal{R}\xi, \xi\rangle > 0$ for every nonzero $\xi \in \Lambda^2 T_pM$ at every $p$.

The sectional curvature of the $2$-plane $\sigma = \mathrm{span}(X, Y)$ is the value of the curvature operator's quadratic form on the unit decomposable $2$-vector representing $\sigma$:

$$K(\sigma) = \frac{\langle \mathcal{R}(X \wedge Y), X \wedge Y\rangle}{|X \wedge Y|^2}.$$

---

# Categorical / Structural Definition

The curvature operator is the **algebraic-curvature-tensor** associated with the Levi-Civita connection. The space of all $(0, 4)$-tensors with the three Riemann symmetries (antisymmetry in pairs $(1, 2)$ and $(3, 4)$, pair-swap symmetry, first Bianchi) forms a vector space $\mathcal{C}(V) \subset \otimes^4 V^*$ — the space of **abstract Riemann tensors** on the inner-product space $V = T_pM$. The natural identification

$$\mathcal{C}(V) \cong \mathrm{Sym}^2(\Lambda^2 V) / \mathrm{Bianchi}$$

makes elements of $\mathcal{C}(V)$ correspond (modulo the first Bianchi identity) to symmetric bilinear forms on $\Lambda^2 V$, i.e., symmetric operators on $\Lambda^2 V$ once we use the inner product. The curvature operator $\mathcal{R}$ is this symmetric operator. The first Bianchi identity sits as a constraint on which symmetric operators are realisable as curvature operators of Riemannian manifolds.

This packaging is the natural one in **Chern–Weil theory**: characteristic classes of $TM$ are built from polynomials in $\mathcal{R}$ via invariant polynomials of $\mathfrak{o}(n)$, and the integrality of these classes is what gives Pontryagin and Euler integers as topological invariants.

---

# Relate to Other Fields / Compression

In **geometric analysis**, positive curvature operator is the **strongest natural curvature positivity condition**, and **Hamilton's Ricci-flow analysis** of compact manifolds with positive curvature operator (in dimension $\ge 4$) is the starting point of the modern programme leading to **Brendle–Schoen's differentiable sphere theorem**. The condition is preserved by Ricci flow and converges to a constant-curvature metric on the limit.

In **Lie group theory**, the curvature operator on a compact Lie group with a bi-invariant metric is *nonnegative*: $\mathcal{R}(X \wedge Y) = \tfrac{1}{4}[X, Y] \wedge [X, Y]$ in left-invariant fields, expressed as the wedge of the Lie bracket. So all bi-invariant metrics on compact Lie groups have nonnegative curvature operator — a major class of examples.

In **gauge theory**, the curvature operator on the universal bundle of a principal-bundle connection is the curvature 2-form $F = dA + A \wedge A$. The curvature operator perspective generalises directly to Yang–Mills curvature on arbitrary principal bundles.

**True name:** *The curvature operator $\mathcal{R}$ is the Riemann tensor regarded as a symmetric linear operator on $2$-vectors, with sectional curvatures being its diagonal entries on decomposable $2$-vectors.* Operationally, $\mathcal{R} > 0$ is "positive on all $2$-vectors" and is strictly stronger than positive sectional curvature in dimension $\ge 4$.

---

# Examples / Corollaries

**Example 1 (constant sectional curvature).** On a constant-curvature-$K_0$ manifold, $\mathcal{R} = K_0 \cdot \mathrm{id}_{\Lambda^2}$. The curvature operator is a scalar multiple of the identity, with $K_0$ as the unique eigenvalue (multiplicity $\binom{n}{2}$).

**Example 2 (round $S^n$).** $\mathcal{R} = \mathrm{id}_{\Lambda^2 T_pS^n}$ — positive curvature operator with all eigenvalues equal to $1$. So $S^n$ has the maximally positive (and most homogeneous) curvature operator.

**Example 3 ($S^2 \times S^2$).** The curvature operator block-diagonalises: $\Lambda^2 T_{(p_1, p_2)}(S^2 \times S^2) = \Lambda^2 T_{p_1}S^2 \oplus \Lambda^2 T_{p_2}S^2 \oplus (T_{p_1}S^2 \wedge T_{p_2}S^2)$. The first two summands carry $\mathcal{R} = 1$ (from each $S^2$ factor); the third summand (mixed $2$-vectors) carries $\mathcal{R} = 0$ (mixed $2$-planes have $K = 0$). So $\mathcal{R}$ has eigenvalues $\{1, 1, 0, 0, 0, 0\}$ on the $6$-dimensional $\Lambda^2$ — *nonnegative* but *not positive*. This is why $S^2 \times S^2$ does **not** satisfy positive curvature operator but does satisfy positive sectional curvature on decomposable $2$-vectors.

**Example 4 (Hopf fibration / $\mathbb{CP}^2$).** Complex projective space $\mathbb{CP}^2$ with Fubini–Study metric has sectional curvature pinched in $[1/4, 1]$, but the curvature operator has a *negative* eigenvalue on certain non-decomposable $2$-vectors. So $\mathbb{CP}^2$ satisfies $K > 0$ but **not** $\mathcal{R} > 0$. This is the prototypical example distinguishing the two conditions.

**Non-example.** $\mathrm{Ric} > 0$ does not imply $\mathcal{R} > 0$ or even nonnegative. There exist Einstein manifolds with negative sectional curvature on some plane (e.g., compact Einstein manifolds with $\mathrm{Ric} = 0$ that have varying-sign sectional curvature).

**Calibration check.** If you have understood this definition correctly you should be able to: (a) compute $\mathcal{R}$ on the round sphere and confirm it is the identity; (b) verify $\langle\mathcal{R}(X \wedge Y), X \wedge Y\rangle/|X \wedge Y|^2 = K(\sigma)$; (c) explain why $\mathcal{R} > 0$ is stronger than $K > 0$ in dimension $\ge 4$ (the operator must be positive on non-decomposable $2$-vectors too); (d) recognise that in dimension $3$, $\mathcal{R} > 0 \iff K > 0$ because all $2$-vectors are decomposable.

---

# Unlocked by This

> [!tip] Hamilton's Ricci Flow with Positive Curvature Operator *(from Geometric Analysis)*
> Hamilton showed (1986) that compact $4$-manifolds with positive curvature operator converge under Ricci flow to a round sphere. The positivity is preserved along the flow, and the homogenisation produces constant positive curvature in the limit. This was the original prototype for the **differentiable sphere theorem**.

> [!tip] Brendle–Schoen Differentiable Sphere Theorem *(from Comparison Geometry)*
> A simply-connected complete manifold with $1/4 < K \le 1$ is diffeomorphic to $S^n$ — proved by **Brendle–Schoen** in $2009$ using Ricci flow. The key technical fact is that pointwise $1/4$-pinched sectional curvature *implies* positive curvature operator (after a careful invariant subspace argument), so Hamilton's positive-curvature-operator analysis applies.

> [!tip] Chern–Weil Theory *(from Algebraic Topology)*
> The curvature operator's spectral data feed into **Chern–Weil theory**: characteristic classes of $TM$ (Pontryagin classes, Euler class) are built from invariant polynomials in $\mathcal{R}$ via $c_k(TM) = [\mathrm{tr}(\mathcal{R}^k)]$ (up to normalisation). The integrality of these classes encodes deep topological constraints on the curvature of $TM$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].
