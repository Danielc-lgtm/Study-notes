---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
  - "Thm - The Closed Subgroup Theorem"
tags: [geometry, differential-geometry, lie-groups]
---

# Problem Statement

Show that $\mathfrak{so}(3) = T_I \mathrm{SO}(3)$, the Lie algebra of the rotation group $\mathrm{SO}(3)$, is the space of $3 \times 3$ antisymmetric real matrices,

$$\mathfrak{so}(3) = \{X \in M(3, \mathbb{R}) : X^T = -X\},$$

a $3$-dimensional vector space. Identify $\mathfrak{so}(3) \cong (\mathbb{R}^3, \times)$ as Lie algebras via the **hat map**, where $\times$ is the cross product.

**Recall:**

The **special orthogonal group** $\mathrm{SO}(3) = \{A \in \mathrm{GL}(3, \mathbb{R}) : A^T A = I, \det A = 1\}$ is the group of orientation-preserving orthogonal $3 \times 3$ matrices, the rotation group of $\mathbb{R}^3$. By [[Thm - The Closed Subgroup Theorem|the closed subgroup theorem]], $\mathrm{SO}(3)$ is an embedded Lie [[Def - Subgroup|subgroup]] of $\mathrm{GL}(3, \mathbb{R})$. Its **Lie algebra** is $\mathfrak{so}(3) = T_I \mathrm{SO}(3) \subseteq T_I \mathrm{GL}(3, \mathbb{R}) = M(3, \mathbb{R})$, as in [[Def - The Lie Algebra of a Lie Group]].

---

# Convergent Strategy

**Problem class:** Lie algebra computation for a classical matrix Lie group, defined by the equations $A^T A = I$ and $\det A = 1$. The strategy is to differentiate both equations at the identity matrix to extract the linear constraint on the tangent vector $X$.

**Assumption pattern:** $\mathrm{SO}(3)$ is given as the **level set** of two smooth functions $A \mapsto A^T A$ and $A \mapsto \det A$. Both are smooth, and the equations $A^T A = I$ and $\det A = 1$ are simultaneously satisfied iff $A \in \mathrm{SO}(3)$. To find the tangent space at $I$, we differentiate both equations at $I$.

**Theorem routing:** The route is: (1) parametrize a curve $A(t) = I + tX + O(t^2)$ in $\mathrm{SO}(3)$ with initial velocity $X$, (2) substitute into the defining equations, (3) expand to first order in $t$, (4) read off the linear constraint. The first equation gives $X + X^T = 0$ (antisymmetry); the second gives $\mathrm{tr} X = 0$, which is automatic for antisymmetric matrices. So the Lie algebra is the space of antisymmetric matrices.

**Key decision point:** The non-obvious move is noting that **the second equation ($\det A = 1$) imposes no new constraint** beyond antisymmetry. The derivative of $\det$ at $I$ is the trace $\mathrm{tr}$, and antisymmetric matrices have zero trace automatically. So the $\det = 1$ condition is "free" once antisymmetry is imposed — which is also why $\mathfrak{o}(n) = \mathfrak{so}(n)$ for all $n$ (the orthogonal and special orthogonal Lie algebras are the same, even though the [[Def - Group|groups]] differ by their components).

---

# Legal Operations Used

1. **Compute the Lie algebra by differentiating the defining equation (operation 1 from the topic page).** Here applied to two equations: $A^T A = I$ and $\det A = 1$. The first gives antisymmetry; the second is redundant.

2. **Use the matrix exponential identities (operation 12 from the topic page).** The identification $\det e^A = e^{\mathrm{tr} A}$ confirms that antisymmetric matrices (which have zero trace) exponentiate to matrices with determinant $1$ — consistent with $\mathfrak{so}(3) \subseteq \mathfrak{sl}(3)$.

---

# Hints

> [!note]- Hint 1
> A curve $A(t) \in \mathrm{SO}(3)$ with $A(0) = I$ and $A'(0) = X$ has the form $A(t) = I + tX + O(t^2)$. Substitute into the equation $A(t)^T A(t) = I$ and expand to first order in $t$.

> [!note]- Hint 2
> $A(t)^T A(t) = (I + tX + O(t^2))^T (I + tX + O(t^2)) = I + t(X + X^T) + O(t^2)$. For this to equal $I$ to first order, we need $X + X^T = 0$, i.e., $X^T = -X$ — antisymmetry.

> [!note]- Hint 3
> Antisymmetric matrices have zero diagonal entries, hence zero trace. The derivative of $\det$ at $I$ is the trace, so antisymmetry automatically implies the $\det A = 1$ condition is satisfied to first order. No new constraint.

> [!note]- Hint 4
> An antisymmetric $3 \times 3$ matrix has $\binom{3}{2} = 3$ independent entries (above the diagonal). So $\mathfrak{so}(3)$ is $3$-dimensional, matching $\dim \mathrm{SO}(3) = 3$.

> [!note]- Hint 5
> For the hat-map identification, write a general antisymmetric matrix as $\widehat v = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix}$ for $v = (v_1, v_2, v_3) \in \mathbb{R}^3$. Compute $[\widehat u, \widehat v] = \widehat u \widehat v - \widehat v \widehat u$ and verify it equals $\widehat{u \times v}$.

---

# Solution

The proof differentiates the defining equations of $\mathrm{SO}(3)$ at the identity, identifying the linear constraint as antisymmetry. The dimension count and the cross-product identification follow.

**Step 1: Differentiate $A^T A = I$ at $I$ to get antisymmetry.**

A smooth curve $A : (-\epsilon, \epsilon) \to \mathrm{SO}(3)$ with $A(0) = I$ has the form $A(t) = I + tX + O(t^2)$ for some $X \in M(3, \mathbb{R})$. Substituting into $A^T A = I$:

$$A(t)^T A(t) = (I + tX + O(t^2))^T (I + tX + O(t^2)) = I + t(X^T + X) + O(t^2).$$

For this to equal $I$ to first order in $t$, the coefficient of $t$ must vanish: $X + X^T = 0$, i.e., $X^T = -X$. So the tangent space at $I$ is contained in the space of antisymmetric matrices.

> [!note]- Derivation
> A tangent vector to $\mathrm{SO}(3)$ at $I$ is the velocity at $t = 0$ of a smooth curve in $\mathrm{SO}(3)$ passing through $I$. Such a curve has the form $A(t) = I + tX + (t^2/2) Y + \cdots$ for matrices $X, Y, \ldots$, with $X = A'(0)$. Substituting into $A^T A = I$:
> $$A(t)^T = I + tX^T + (t^2/2) Y^T + O(t^3),$$
> $$A(t)^T A(t) = (I + tX^T + \cdots)(I + tX + \cdots) = I + t(X^T + X) + t^2(X^T X + Y^T/2 + Y/2) + O(t^3).$$
> Setting equal to $I$, the order-$t$ coefficient must vanish: $X^T + X = 0$, i.e., $X^T = -X$. This is the first-order constraint, the definition of antisymmetry.

**Step 2: The $\det A = 1$ equation imposes no new constraint.**

The derivative of $\det : \mathrm{GL}(n) \to \mathbb{R}$ at $I$ is $\mathrm{tr} : M(n) \to \mathbb{R}$ (this is the Jacobi formula or a direct computation). So differentiating $\det A = 1$ at $I$ gives $\mathrm{tr} X = 0$. But antisymmetric matrices have zero diagonal entries, hence zero trace automatically. So the $\det = 1$ condition is implied by antisymmetry — no new constraint.

> [!note]- Derivation
> $\det(I + tX) = 1 + t \, \mathrm{tr} X + O(t^2)$. (This is a standard computation: the determinant of $I + tX$ is the product of eigenvalues of $I + tX$; for small $t$ these are $1 + t \lambda_i + O(t^2)$ where $\lambda_i$ are eigenvalues of $X$, and $\prod (1 + t\lambda_i) = 1 + t \sum \lambda_i + O(t^2) = 1 + t \, \mathrm{tr} X + O(t^2)$.) Setting $\det A(t) = 1$ gives $\mathrm{tr} X = 0$. Antisymmetric matrices have $X_{ii} = -X_{ii}$ for each $i$, hence $X_{ii} = 0$ and $\mathrm{tr} X = \sum_i X_{ii} = 0$. So antisymmetry implies $\mathrm{tr} X = 0$ automatically, and the $\det = 1$ equation provides no new linear constraint at first order.

**Step 3: Conclude $\mathfrak{so}(3) = \{X : X^T = -X\}$.**

The tangent space $T_I \mathrm{SO}(3)$ is contained in $\{X : X^T = -X\}$ by Step 1. Conversely, every antisymmetric $X$ gives a curve $A(t) = e^{tX} \in \mathrm{SO}(3)$ — because $e^{tX^T} = e^{-tX} = (e^{tX})^{-1}$, so $e^{tX}$ is orthogonal, and $\det e^{tX} = e^{t \mathrm{tr} X} = e^0 = 1$. Hence every antisymmetric matrix is tangent to a curve in $\mathrm{SO}(3)$, so $T_I \mathrm{SO}(3) \supseteq \{X : X^T = -X\}$. Combining: $T_I \mathrm{SO}(3) = \{X : X^T = -X\}$.

> [!note]- Derivation
> *Reverse inclusion.* Given $X$ antisymmetric, define $A(t) = e^{tX}$ (the matrix exponential). Then $A(t)^T = e^{tX^T} = e^{-tX} = (e^{tX})^{-1} = A(t)^{-1}$, so $A(t)^T A(t) = I$ — $A(t)$ is orthogonal. Also $\det A(t) = \det e^{tX} = e^{t \mathrm{tr} X} = e^0 = 1$ since $\mathrm{tr} X = 0$ for antisymmetric $X$. So $A(t) \in \mathrm{SO}(3)$, and $A'(0) = X \in T_I \mathrm{SO}(3)$. This shows every antisymmetric matrix is in the tangent space, completing the equality.

**Step 4: [[Def - Dimension|Dimension]] and the hat map.**

A general $3 \times 3$ antisymmetric matrix has the form $\widehat v = \begin{pmatrix} 0 & -v_3 & v_2 \\ v_3 & 0 & -v_1 \\ -v_2 & v_1 & 0 \end{pmatrix}$ for $v = (v_1, v_2, v_3) \in \mathbb{R}^3$ — three free parameters above the diagonal, with three corresponding entries below. The dimension is $3$, matching $\dim \mathrm{SO}(3) = 3$.

The **hat map** $\widehat{\cdot} : \mathbb{R}^3 \to \mathfrak{so}(3)$ is the linear isomorphism $v \mapsto \widehat v$. Under this identification, the matrix commutator becomes the cross product:

$$[\widehat u, \widehat v] = \widehat u \widehat v - \widehat v \widehat u = \widehat{u \times v}.$$

> [!note]- Derivation
> The hat map satisfies $\widehat u\,x=u\times x$. Therefore, for every $x\in\mathbb R^3$,
> $$[\widehat u,\widehat v]x=u\times(v\times x)-v\times(u\times x)=(u\times v)\times x=\widehat{u\times v}x,$$
> where the middle equality is the vector triple-product identity. Hence $[\widehat u,\widehat v]=\widehat{u\times v}$; in particular $[\widehat e_1,\widehat e_2]=\widehat e_3$.

> [!note]- Complete formal solution
> Let $A : (-\epsilon, \epsilon) \to \mathrm{SO}(3)$ be a smooth curve with $A(0) = I$ and $A'(0) = X$. Writing $A(t) = I + tX + O(t^2)$, substitute into the defining equation $A^T A = I$:
> $$I + t(X^T + X) + O(t^2) = I.$$
> The order-$t$ coefficient must vanish: $X + X^T = 0$, i.e., $X$ is antisymmetric. The second defining equation $\det A = 1$ gives $\mathrm{tr} X = 0$, which is automatic for antisymmetric $X$ (zero diagonal). Conversely, for any antisymmetric $X$, the curve $A(t) = e^{tX}$ lies in $\mathrm{SO}(3)$ because $A(t)^T = e^{-tX} = A(t)^{-1}$ (orthogonality) and $\det A(t) = e^{t \mathrm{tr} X} = 1$ (determinant $1$). So $T_I \mathrm{SO}(3) = \{X \in M(3, \mathbb{R}) : X^T = -X\}$.
>
> The dimension is $3$ (three free entries above the diagonal of a $3 \times 3$ antisymmetric matrix). Under the **hat map** $v \mapsto \widehat v$, $\mathfrak{so}(3) \cong \mathbb{R}^3$ as vector spaces, and the matrix commutator becomes the cross product: $[\widehat u, \widehat v] = \widehat{u \times v}$. (Verification: direct computation on basis vectors, extended by bilinearity.) $\qquad\blacksquare$

---

# Key Takeaways

**Differentiating the defining equation is the universal technique for computing matrix Lie algebras.**

The procedure used here generalizes to every classical matrix Lie group: substitute $A(t) = I + tX + O(t^2)$ into the defining equations, expand to first order, set the order-$t$ coefficients to zero. For $\mathrm{O}(n)$ this gives antisymmetry; for $\mathrm{U}(n)$ (using $A^* A = I$), skew-Hermiticity $X^* + X = 0$; for $\mathrm{SL}(n)$ (using $\det A = 1$), tracelessness $\mathrm{tr} X = 0$; for $\mathrm{Sp}(2n)$ (using $A^T J A = J$), the symplectic-compatibility condition $X^T J + J X = 0$. The pattern is universal: the Lie algebra is the kernel of the differential of the defining equation at $I$.

**The cross product is the Lie bracket on $\mathfrak{so}(3) \cong \mathbb{R}^3$.**

The hat-map identification $\mathfrak{so}(3) \cong \mathbb{R}^3$ is more than a vector-space isomorphism — it identifies the matrix-commutator bracket on $\mathfrak{so}(3)$ with the cross product on $\mathbb{R}^3$. This is a deeply useful identification: it means every cross product manipulation in $\mathbb{R}^3$ is secretly a Lie algebra computation, and conversely every $\mathfrak{so}(3)$ identity is a $\mathbb{R}^3$ identity. The Jacobi identity for the bracket becomes the Jacobi identity for the cross product, $u \times (v \times w) + v \times (w \times u) + w \times (u \times v) = 0$. The trigger: a problem in 3D involving "right-hand rule" cross products is, secretly, $\mathfrak{so}(3)$ Lie algebra theory; conversely, abstract $\mathfrak{so}(3)$ statements can be computed using cross products.

**$\mathfrak{so}(3) \cong \mathfrak{su}(2)$ as Lie algebras, even though $\mathrm{SO}(3) \not\cong \mathrm{SU}(2)$ as Lie groups.**

The Lie algebra $\mathfrak{so}(3)$, $3$-dimensional with cross-product bracket, is isomorphic to $\mathfrak{su}(2)$, also $3$-dimensional with traceless skew-Hermitian matrices under the matrix commutator. (Use the Pauli matrices: $\{i\sigma_a/2\}_{a=1,2,3}$ is a basis of $\mathfrak{su}(2)$, and $[i\sigma_a/2, i\sigma_b/2] = -\epsilon_{abc} i\sigma_c/2$, the same structure as $\mathfrak{so}(3)$ up to sign.) Yet the Lie groups are not isomorphic — $\mathrm{SU}(2)$ is simply connected, $\mathrm{SO}(3)$ has fundamental group $\mathbb{Z}/2$. This is the canonical demonstration that the Lie functor is not injective on objects, and it is the origin of the **double cover** $\mathrm{SU}(2) \to \mathrm{SO}(3)$ — see [[Ex - SU(2) is Diffeomorphic to S^3]]. The takeaway: Lie algebra isomorphism does *not* imply Lie group isomorphism; the gap is the fundamental group of the group.
