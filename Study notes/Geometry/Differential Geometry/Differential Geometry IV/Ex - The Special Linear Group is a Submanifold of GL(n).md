---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Embedded Submanifold"
  - "Def - Regular and Critical Points"
  - "Def - Tangent Space of a Submanifold"
  - "Thm - Regular Value Theorem on Manifolds"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that the special linear group
$$\mathrm{SL}(n,\mathbb{R}) = \{A \in \mathrm{GL}(n,\mathbb{R}) : \det A = 1\}$$
is an embedded smooth submanifold of $\mathrm{GL}(n,\mathbb{R})$ of [[Def - Dimension|dimension]] $n^2 - 1$. Compute the tangent space at the identity $T_I \mathrm{SL}(n,\mathbb{R})$ explicitly, and verify it equals
$$\mathfrak{sl}(n,\mathbb{R}) = \{X \in \mathrm{Mat}_n(\mathbb{R}) : \mathrm{tr}\, X = 0\},$$
the space of trace-zero matrices. This is the **Lie algebra** of $\mathrm{SL}(n,\mathbb{R})$, and the exercise previews the general construction of a Lie algebra as the tangent space at the identity of a matrix Lie group.

**Recall:**

The general linear group $\mathrm{GL}(n,\mathbb{R}) = \{A \in \mathrm{Mat}_n(\mathbb{R}) : \det A \neq 0\}$ is an open subset of the matrix space $\mathrm{Mat}_n(\mathbb{R}) \cong \mathbb{R}^{n^2}$ (as the preimage of $\mathbb{R}\setminus\{0\}$ under the continuous map $\det$), hence an $n^2$-dimensional smooth manifold with tangent space $T_A \mathrm{GL}(n,\mathbb{R}) \cong \mathrm{Mat}_n(\mathbb{R})$ at every $A$.

The differential of $\det$ at $A$ (Jacobi's formula): for $A$ invertible,
$$d(\det)_A(X) = \det(A) \cdot \mathrm{tr}(A^{-1} X) \quad\text{for } X \in \mathrm{Mat}_n.$$
At $A = I$ this simplifies to $d(\det)_I(X) = \mathrm{tr}(X)$.

By [[Thm - Regular Value Theorem on Manifolds]], a regular level set is a properly embedded submanifold with tangent space equal to the kernel of the defining map's differential.

---

# Convergent Strategy

**Problem class:** This is a regular value theorem application to identify a matrix Lie group as a smooth submanifold. The strategy is the same as for the sphere ([[Ex - The Sphere as a Level Set]]): write the candidate as a level set, compute the differential, check it is surjective at every preimage point. The added subtlety is that the defining map is non-trivial (determinant rather than norm) and the dimension count $n^2 - 1$ is not as immediate as $n$.

**Assumption pattern:** $\mathrm{SL}(n)$ is the preimage of $1$ under the scalar function $\det : \mathrm{GL}(n,\mathbb{R}) \to \mathbb{R}_{> 0} \cup \mathbb{R}_{< 0}$ (which descends to $\det : \mathrm{Mat}_n \to \mathbb{R}$ restricted to the open subset of invertible matrices). The codomain is $\mathbb{R}$, scalar, so surjectivity of the differential is "differential nonzero". Jacobi's formula for $d(\det)_A$ gives a clean formula in terms of $A^{-1}$ and the trace.

**Theorem routing:** The route is single-step through [[Thm - Regular Value Theorem on Manifolds]]: at each $A \in \mathrm{SL}(n)$, compute $d(\det)_A$ via Jacobi's formula; check it is nonzero; conclude $1$ is a regular value; the level set is an embedded submanifold of codimension $1$, dimension $n^2 - 1$; the tangent space at $A$ is $\ker d(\det)_A = \{X \in \mathrm{Mat}_n : \mathrm{tr}(A^{-1} X) = 0\}$. At $A = I$, this becomes $\mathfrak{sl}(n) = \{X : \mathrm{tr}\, X = 0\}$.

**Key decision point:** The non-obvious step is computing $d(\det)_A$ via Jacobi's formula — most students don't immediately remember this is the right formula for differentiating the determinant. The trick is to view $\det$ as a multilinear function of the columns (or rows), and differentiate column-by-column. The alternative — direct power series expansion of $\det(I + tX)$ — is also viable: $\det(I + tX) = 1 + t \cdot \mathrm{tr}(X) + O(t^2)$, which immediately gives $d(\det)_I(X) = \mathrm{tr}(X)$. The general formula at $A$ comes from $\det(A + tX) = \det(A) \det(I + t A^{-1} X) = \det(A)(1 + t \cdot \mathrm{tr}(A^{-1} X) + O(t^2))$.

---

# Legal Operations Used

1. **Operation 2 (apply the regular value theorem):** the entire solution routes through this operation. Write $\mathrm{SL}(n)$ as $\det^{-1}(1)$, compute the differential, check surjectivity, conclude.

2. **Operation 1 (compute the differential in coordinates):** computing $d(\det)_A$ is the key technical step. Use Jacobi's formula or the power-series expansion $\det(A + tX) = \det(A)(1 + t \cdot \mathrm{tr}(A^{-1} X) + O(t^2))$.

3. **Operation 8 (identify tangent vectors as velocities of curves):** an alternative way to compute $T_I \mathrm{SL}(n)$. A curve $A(t)$ in $\mathrm{SL}(n)$ with $A(0) = I$ satisfies $\det A(t) = 1$ for all $t$; differentiating gives $d(\det)_I(A'(0)) = 0$, i.e., $\mathrm{tr}(A'(0)) = 0$. So $A'(0) \in \mathfrak{sl}(n)$. The converse (every trace-zero matrix is some $A'(0)$) comes from $A(t) = e^{tX}$ for $X \in \mathfrak{sl}(n)$, and $\det e^{tX} = e^{t \mathrm{tr} X} = 1$.

---

# Hints

> [!note]- Hint 1
> What single smooth function on $\mathrm{Mat}_n$ has $\mathrm{SL}(n,\mathbb{R})$ as a level set? Make sure the function is well-defined and smooth on the *open* set you actually need.

> [!note]- Hint 2
> The differential of the determinant. Compute $d(\det)_A(X)$ for an arbitrary $A \in \mathrm{GL}(n,\mathbb{R})$ and arbitrary $X \in \mathrm{Mat}_n$. (Hint: use $\det(A + tX) = \det(A) \det(I + t A^{-1} X)$ and the expansion $\det(I + t Y) = 1 + t \cdot \mathrm{tr}(Y) + O(t^2)$.)

> [!note]- Hint 3
> Once you have the differential at every point of $\mathrm{SL}(n)$, check it is nonzero. If so, $1$ is a regular value of $\det$, and the regular value theorem gives the submanifold structure.

> [!note]- Hint 4
> For the tangent space at $I$, plug $A = I$ into your formula for $d(\det)_A$. The result is the linear map $X \mapsto \mathrm{tr}(X)$, whose kernel is the trace-zero matrices.

---

# Solution

The proof breaks into three steps. Step 1 identifies $\mathrm{SL}(n,\mathbb{R})$ as the level set of $\det$ at $1$. Step 2 computes $d(\det)_A$ and verifies it is nonzero on $\mathrm{SL}(n)$. Step 3 applies the regular value theorem and reads off the tangent space.

**Step 1: $\mathrm{SL}(n, \mathbb{R})$ is the level set $\det^{-1}(1)$ of a smooth function.**

> [!note]- Derivation
> The determinant $\det : \mathrm{Mat}_n(\mathbb{R}) \to \mathbb{R}$ is a polynomial in the matrix entries, hence smooth on all of $\mathrm{Mat}_n$. Its restriction to $\mathrm{GL}(n,\mathbb{R}) = \det^{-1}(\mathbb{R} \setminus \{0\})$ (an open subset of $\mathrm{Mat}_n$, hence an open submanifold) is also smooth. The special linear group is by definition
> $$\mathrm{SL}(n, \mathbb{R}) = \{A \in \mathrm{GL}(n, \mathbb{R}) : \det A = 1\} = \det^{-1}(1).$$
> Since $\det \neq 0$ on $\mathrm{GL}(n,\mathbb{R})$, we can also view $\mathrm{SL}(n,\mathbb{R})$ as the level set $\det^{-1}(1)$ in $\mathrm{Mat}_n$, which sits entirely inside $\mathrm{GL}(n,\mathbb{R})$.

**Step 2: $d(\det)_A$ is nonzero at every $A \in \mathrm{SL}(n, \mathbb{R})$.**

> [!note]- Derivation
> Compute $d(\det)_A(X)$ for $A \in \mathrm{GL}(n,\mathbb{R})$ and $X \in T_A \mathrm{Mat}_n \cong \mathrm{Mat}_n$.
>
> Using multiplicativity of determinant, $\det(A + tX) = \det(A) \det(I + t A^{-1} X)$. The expansion of $\det(I + t Y)$ in powers of $t$ is
> $$\det(I + tY) = 1 + t \cdot \mathrm{tr}(Y) + \frac{t^2}{2}((\mathrm{tr}\, Y)^2 - \mathrm{tr}(Y^2)) + \dots + t^n \det Y$$
> (the coefficients are the elementary symmetric polynomials in the eigenvalues of $Y$). The leading-order term in $t$ is $t \cdot \mathrm{tr}(Y)$, so
> $$\det(A + tX) = \det(A) \cdot (1 + t \cdot \mathrm{tr}(A^{-1} X) + O(t^2)).$$
> Therefore
> $$\frac{d}{dt}\Big|_{t=0} \det(A + tX) = \det(A) \cdot \mathrm{tr}(A^{-1} X),$$
> which is **Jacobi's formula**: $d(\det)_A(X) = \det(A) \cdot \mathrm{tr}(A^{-1} X)$.
>
> Is this nonzero on $\mathrm{SL}(n,\mathbb{R})$? At $A \in \mathrm{SL}(n,\mathbb{R})$ we have $\det A = 1 \neq 0$. To show $d(\det)_A$ is nonzero (as a linear functional on $\mathrm{Mat}_n$), we need some $X$ with $d(\det)_A(X) \neq 0$ — equivalently, $\mathrm{tr}(A^{-1} X) \neq 0$ for some $X$.
>
> Take $X = A$. Then $A^{-1} X = A^{-1} A = I$, and $\mathrm{tr}(I) = n \neq 0$. So $d(\det)_A(A) = \det(A) \cdot n = n \neq 0$. Hence $d(\det)_A$ is nonzero at every $A \in \mathrm{SL}(n,\mathbb{R})$, i.e., $1$ is a regular value of $\det$.

**Step 3: Apply the regular value theorem to identify the submanifold and tangent space.**

> [!note]- Derivation
> By [[Thm - Regular Value Theorem on Manifolds]] (with $M = \mathrm{GL}(n,\mathbb{R})$ of dimension $n^2$, $N = \mathbb{R}$, $\Phi = \det$, $c = 1$), the level set $\mathrm{SL}(n,\mathbb{R}) = \det^{-1}(1)$ is a properly embedded smooth submanifold of $\mathrm{GL}(n,\mathbb{R})$ of codimension $\dim \mathbb{R} = 1$, hence of dimension
> $$\dim \mathrm{SL}(n,\mathbb{R}) = n^2 - 1.$$
> The tangent space at any $A \in \mathrm{SL}(n,\mathbb{R})$ is
> $$T_A \mathrm{SL}(n,\mathbb{R}) = \ker d(\det)_A = \{X \in \mathrm{Mat}_n : \det(A) \cdot \mathrm{tr}(A^{-1} X) = 0\} = \{X : \mathrm{tr}(A^{-1} X) = 0\}.$$
>
> At $A = I$, this becomes
> $$T_I \mathrm{SL}(n,\mathbb{R}) = \{X \in \mathrm{Mat}_n : \mathrm{tr}\, X = 0\} = \mathfrak{sl}(n, \mathbb{R}),$$
> the trace-zero matrices. The dimension of $\mathfrak{sl}(n)$ is $n^2 - 1$ (the kernel of the trace functional, which is one-dimensional in the dual space, has codimension $1$ in $\mathrm{Mat}_n$).

> [!note]- Complete formal solution
> Let $f = \det : \mathrm{GL}(n,\mathbb{R}) \to \mathbb{R}$; $f$ is smooth on the $n^2$-dimensional open submanifold $\mathrm{GL}(n,\mathbb{R}) \subseteq \mathrm{Mat}_n(\mathbb{R})$, and $\mathrm{SL}(n,\mathbb{R}) = f^{-1}(1)$.
>
> By Jacobi's formula (derived from the power-series expansion $\det(I + tY) = 1 + t \cdot \mathrm{tr}(Y) + O(t^2)$ applied to $Y = A^{-1} X$), the differential of $\det$ at $A$ is $df_A(X) = \det(A) \cdot \mathrm{tr}(A^{-1} X)$.
>
> At $A \in \mathrm{SL}(n,\mathbb{R})$, $\det(A) = 1 \neq 0$, and taking $X = A$ gives $df_A(A) = \mathrm{tr}(I) = n \neq 0$. So $df_A$ is a nonzero linear functional on $T_A \mathrm{Mat}_n \cong \mathrm{Mat}_n$, i.e., $df_A$ is surjective onto $\mathbb{R}$. Hence every $A \in \mathrm{SL}(n,\mathbb{R})$ is a regular point of $f$, and $1$ is a regular value.
>
> By [[Thm - Regular Value Theorem on Manifolds]], $\mathrm{SL}(n,\mathbb{R})$ is a properly embedded smooth submanifold of $\mathrm{GL}(n,\mathbb{R})$ of codimension $1$, hence of dimension $n^2 - 1$. The tangent space at any $A$ is
> $$T_A \mathrm{SL}(n,\mathbb{R}) = \ker df_A = \{X \in \mathrm{Mat}_n : \mathrm{tr}(A^{-1} X) = 0\}.$$
> Specialised to $A = I$:
> $$T_I \mathrm{SL}(n,\mathbb{R}) = \{X \in \mathrm{Mat}_n : \mathrm{tr}\, X = 0\} = \mathfrak{sl}(n, \mathbb{R}). \qquad\blacksquare$$
>
> **Sanity check via independent route.** Compute $T_I \mathrm{SL}(n,\mathbb{R})$ using the curve characterisation. A smooth curve $A : (-\varepsilon, \varepsilon) \to \mathrm{SL}(n)$ with $A(0) = I$ satisfies $\det A(t) = 1$ for all $t$. Differentiating at $t = 0$ with the chain rule and using $d(\det)_I = \mathrm{tr}$: $\mathrm{tr}(A'(0)) = 0$, so $A'(0) \in \mathfrak{sl}(n)$. Conversely, for any $X \in \mathfrak{sl}(n)$, the curve $A(t) = e^{tX}$ has $\det e^{tX} = e^{t \mathrm{tr} X} = e^0 = 1$, so $A(t) \in \mathrm{SL}(n)$, $A(0) = I$, $A'(0) = X$. Hence $T_I \mathrm{SL}(n) = \mathfrak{sl}(n)$, confirming the kernel computation.

---

# Key Takeaways

**Matrix Lie [[Def - Group|groups]] via the regular value theorem.** This is the prototypical construction of a matrix Lie group as a smooth manifold: identify the group as the level set of an explicit smooth function (a determinant, a defining quadratic form, a defining polynomial), apply the regular value theorem, read off the dimension and the tangent space at the identity. The pattern recurs for $\mathrm{O}(n)$ (defining function $A \mapsto A^T A$, see [[Ex - The Orthogonal Group as a Regular Level Set]]), $\mathrm{U}(n)$ (defining function $A \mapsto A^* A$), $\mathrm{SU}(n)$ (combine $A^*A$ and $\det$), and $\mathrm{Sp}(2n)$ (defining function $A \mapsto A^T J A$ for the symplectic matrix $J$). Each requires its own care: choosing the right defining function, the right codomain, and verifying surjectivity of the differential at the identity. The reward is that the manifold structure and the Lie algebra fall out of one computation.

**Jacobi's formula and the trace map.** The differential of the determinant at $A$ is $d(\det)_A(X) = \det(A) \mathrm{tr}(A^{-1} X)$. At $A = I$ this becomes the trace map. This is a recurring identity in matrix calculus and is worth memorising: it underlies the proof that $\mathrm{SL}(n)$ has dimension $n^2 - 1$, the formula for the variation of the determinant under perturbations, and the dimensional structure of various polynomial maps on matrices. The trick to deriving it is to factor out $\det(A)$ via $\det(A + tX) = \det(A) \det(I + t A^{-1} X)$ and use the expansion $\det(I + tY) = 1 + t \mathrm{tr}(Y) + O(t^2)$.

**The exponential map produces curves through the identity.** The construction $A(t) = e^{tX}$ for $X \in \mathfrak{sl}(n)$ gives a smooth curve in $\mathrm{SL}(n)$ through the identity with velocity $X$. This is the **exponential map** of the Lie group, and it is the standard way of producing tangent vectors at the identity. The general fact: for a matrix Lie group $G$ with Lie algebra $\mathfrak{g} = T_I G$, the exponential map $\exp : \mathfrak{g} \to G$ is a local [[Def - Diffeomorphism|diffeomorphism]] near the origin, and its differential at $0$ is the identity on $\mathfrak{g}$. This is developed in [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]], but the exercise above gives a first taste.

**Cross-link to companion exercises.** The companion [[Ex - The Orthogonal Group as a Regular Level Set]] illustrates the harder case where the codomain must be chosen carefully (symmetric matrices, not all matrices). The pair [[Ex - The Sphere as a Level Set]] and this exercise illustrate the spectrum of regular value theorem applications, from the simplest (scalar function) to the matrix-group cases (where dimension counting and tangent-space-at-identity become the key computations).
