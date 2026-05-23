---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Singular Value Decomposition"
  - "Def - Singular Values"
  - "Ex - SVD computes the operator norm"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ and $W$ be finite-dimensional inner product spaces and $T \in \mathcal{L}(V, W)$ with singular value decomposition $T = \sum_{j=1}^{r} s_j f_j e_j^*$ (where $s_1 \geq s_2 \geq \cdots \geq s_r > 0$ are the nonzero singular values, $r = \operatorname{rank} T$). Define the **rank-$k$ truncation**:
$$T_k = \sum_{j=1}^{k} s_j f_j e_j^*, \quad 1 \leq k \leq r.$$

Prove the **Eckart–Young theorem**: $T_k$ is the unique best rank-$k$ approximation of $T$ in the operator norm:
$$\min_{\operatorname{rank} B \leq k} \|T - B\|_{\text{op}} = \|T - T_k\|_{\text{op}} = s_{k+1}.$$
(Equivalent statement also holds for the Frobenius norm, with the minimum equal to $\sqrt{\sum_{j > k} s_j^2}$.)

**Recall:**

![[Thm - Singular Value Decomposition#Statement]]

The operator norm is $\|T\|_{\text{op}} = \sup_{\|v\| = 1} \|Tv\|$, which equals the largest [[Def - Singular Values|singular value]] (see [[Ex - SVD computes the operator norm]]). The **Frobenius norm** is $\|T\|_F = \sqrt{\sum_j s_j^2(T)} = \sqrt{\operatorname{tr}(T^*T)}$.

The notation $f_j e_j^*$ denotes the rank-$1$ operator $v \mapsto \langle v, e_j \rangle f_j$ — the outer product. A rank-$k$ operator is one of the form $\sum_{j=1}^{k} \alpha_j x_j y_j^*$ for some scalars $\alpha_j$ and vectors $x_j, y_j$.

---

# Convergent Strategy

**Problem class.** This is a *deep extremum* problem: find the minimum of an operator distance over a constrained class (rank $\leq k$ matrices). The hardness comes from the constraint "rank $\leq k$" being non-convex — the set of low-rank matrices is a non-linear variety, not a subspace.

**Assumption pattern.** The hypothesis is the SVD of $T$ with singular values $s_1 \geq \cdots \geq s_r > 0$. The candidate optimum $T_k$ is the truncated SVD. The conclusion is that $T_k$ achieves the minimum, with value $s_{k+1}$.

**Theorem routing.** The route is in two parts. First, show $\|T - T_k\|_{\text{op}} = s_{k+1}$ — the candidate achieves the value $s_{k+1}$. Second, show that for any $B$ with $\operatorname{rank} B \leq k$, $\|T - B\|_{\text{op}} \geq s_{k+1}$ — every other candidate is at least as bad. The second is the substantive direction; the strategy is a **dimension count**: $B$'s kernel has dimension $\geq n - k$; combined with the $(k+1)$-dimensional subspace spanned by the top right-singular vectors $e_1, \ldots, e_{k+1}$, these have non-trivial intersection (in $\mathbb{F}^n$ with $n \geq k+1$), forcing $\|T - B\|_{\text{op}}$ to be at least $s_{k+1}$.

**Key decision point.** The non-obvious move is the **dimension intersection argument**: $\dim \operatorname{null} B + \dim \operatorname{span}(e_1, \ldots, e_{k+1}) \geq (n - k) + (k + 1) = n + 1 > n$, so the intersection is non-trivial. There exists a non-zero $v$ in both. On this $v$, $Bv = 0$, so $\|(T - B) v\| = \|Tv\|$. Compute $\|Tv\|$ for $v$ in the top-$(k+1)$ right-singular span: $\|Tv\| \geq s_{k+1} \|v\|$. So $\|T - B\|_{\text{op}} \geq s_{k+1}$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VII — §7 Operators on Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the SVD to access spectral data** — Use the SVD to express both $T$ and $T_k$ in terms of singular values and singular vectors.

2. **Compute operator norm via singular values** — Use $\|T\|_{\text{op}} = s_1(T)$, applied to $T - T_k$ (whose nonzero singular values are $s_{k+1}, s_{k+2}, \ldots, s_r$, with $s_{k+1}$ being the largest).

3. **Use a dimension count to force non-trivial intersection** — Two [[Def - Subspace|subspaces]] of [[Def - Dimension|dimensions]] summing to more than $n$ must intersect non-trivially.

4. **Bound $\|Tv\|$ from below on a subspace** — On $\operatorname{span}(e_1, \ldots, e_{k+1})$, $\|Tv\| \geq s_{k+1} \|v\|$ (the smallest singular value of $T$ restricted to this subspace).

---

# Hints

> [!note]- Hint 1
> First show that $T - T_k$ has the SVD $T - T_k = \sum_{j > k} s_j f_j e_j^*$, so its largest singular value is $s_{k+1}$.

> [!note]- Hint 2
> The hard direction is the lower bound. For any $B$ with $\operatorname{rank} B \leq k$, find a non-zero vector $v$ in both $\operatorname{null} B$ and $\operatorname{span}(e_1, \ldots, e_{k+1})$. Use a dimension argument.

> [!note]- Hint 3
> On such a $v$, $(T - B) v = Tv$. Compute $\|Tv\|$ using the SVD: $\|Tv\|^2 = \sum_{j \leq k+1} |\alpha_j|^2 s_j^2 \geq s_{k+1}^2 \sum_{j \leq k+1} |\alpha_j|^2 = s_{k+1}^2 \|v\|^2$. So $\|(T - B) v\| \geq s_{k+1} \|v\|$, giving $\|T - B\|_{\text{op}} \geq s_{k+1}$.

---

# Solution

The proof has two parts. The upper bound $\|T - T_k\|_{\text{op}} \leq s_{k+1}$ is direct: $T - T_k$ has SVD $\sum_{j > k} s_j f_j e_j^*$, with largest singular value $s_{k+1}$. The lower bound $\|T - B\|_{\text{op}} \geq s_{k+1}$ for any rank-$\leq k$ matrix $B$ uses a dimension argument: $\operatorname{null} B$ has dimension $\geq n - k$, and the top-$(k+1)$ right-singular span has dimension $k+1$; together they exceed $n$, forcing a non-trivial intersection where $T - B$ acts as $T$ alone, with operator norm at least $s_{k+1}$.

**Step 1: $\|T - T_k\|_{\text{op}} = s_{k+1}$.**

The operator $T - T_k$ has the form $T - T_k = \sum_{j > k} s_j f_j e_j^*$. This is an SVD of $T - T_k$ with singular values $s_{k+1}, s_{k+2}, \ldots, s_r, 0, \ldots, 0$ (the rest are zero), the largest being $s_{k+1}$. By [[Ex - SVD computes the operator norm]], $\|T - T_k\|_{\text{op}} = s_{k+1}$.

> [!note]- Derivation
> Subtract the first $k$ terms of the SVD: $T - T_k = \sum_{j=1}^{r} s_j f_j e_j^* - \sum_{j=1}^{k} s_j f_j e_j^* = \sum_{j=k+1}^{r} s_j f_j e_j^*$. The right-hand side is in SVD form (the $f_j$ are orthonormal for $j > k$, the $e_j$ are orthonormal for $j > k$, the $s_j$ are non-negative in decreasing order). So the singular values of $T - T_k$ are $\{s_{k+1}, s_{k+2}, \ldots, s_r, 0, \ldots, 0\}$ — the trailing singular values of $T$. The largest is $s_{k+1}$, equal to $\|T - T_k\|_{\text{op}}$.

**Step 2: For any $B$ with $\operatorname{rank} B \leq k$, $\|T - B\|_{\text{op}} \geq s_{k+1}$.**

Let $U_{k+1} = \operatorname{span}(e_1, \ldots, e_{k+1})$, the $(k+1)$-dimensional subspace spanned by the top $k+1$ right-singular vectors. We have $\dim \operatorname{null} B \geq n - k$ (rank-nullity: $\dim \operatorname{null} B = n - \operatorname{rank} B \geq n - k$). And $\dim U_{k+1} = k + 1$.

Now $\dim \operatorname{null} B + \dim U_{k+1} \geq (n - k) + (k + 1) = n + 1 > n$. So $\operatorname{null} B \cap U_{k+1}$ contains a non-zero vector $v$. Normalise to $\|v\| = 1$.

Compute $\|(T - B) v\|$: since $v \in \operatorname{null} B$, $Bv = 0$, so $(T - B) v = T v$. Since $v \in U_{k+1}$, write $v = \sum_{j=1}^{k+1} \alpha_j e_j$ with $\sum_{j=1}^{k+1} |\alpha_j|^2 = 1$. Then $Tv = \sum_{j=1}^{k+1} \alpha_j s_j f_j$, and
$$\|Tv\|^2 = \sum_{j=1}^{k+1} |\alpha_j|^2 s_j^2 \geq s_{k+1}^2 \sum_{j=1}^{k+1} |\alpha_j|^2 = s_{k+1}^2,$$
using $s_j \geq s_{k+1}$ for $j \leq k+1$ (decreasing-order singular values). So $\|Tv\| \geq s_{k+1}$, hence $\|(T - B) v\| \geq s_{k+1}$ for this $v$ with $\|v\| = 1$. So $\|T - B\|_{\text{op}} \geq s_{k+1}$. ✓

> [!note]- Derivation
> The dimension argument is the heart of the proof. The dimension formula $\dim(A) + \dim(B) = \dim(A + B) + \dim(A \cap B)$ in a finite-dimensional space implies $\dim(A \cap B) \geq \dim(A) + \dim(B) - n$ when both are [[Def - Subspace|subspaces]] of $V \cong \mathbb{F}^n$. With $A = \operatorname{null} B \subseteq V$ (dimension $\geq n - k$) and $B = U_{k+1} \subseteq V$ (dimension $k+1$), the intersection has dimension $\geq (n - k) + (k + 1) - n = 1$, so contains a non-zero vector.
>
> Once a vector $v$ is in both $\operatorname{null} B$ and $U_{k+1}$, the calculation $\|(T - B)v\| = \|Tv\| \geq s_{k+1} \|v\|$ uses the fact that on the span of the top $k+1$ right-singular vectors, $T$ stretches every unit vector by at least $s_{k+1}$ (since the smallest singular value in this span is $s_{k+1}$).

**Step 3: Conclude.**

Combining Steps 1 and 2: any rank-$\leq k$ matrix $B$ has $\|T - B\|_{\text{op}} \geq s_{k+1}$, with equality at $B = T_k$. So $T_k$ achieves the minimum, equal to $s_{k+1}$.

**Uniqueness** of the best rank-$k$ approximation: when $s_k > s_{k+1}$ (strict gap in the singular values), the truncated SVD $T_k$ is the unique best rank-$k$ approximation. When $s_k = s_{k+1}$, any other choice of top-$k$ singular components giving the same overall value yields the same approximation up to a unitary rotation within the equal-singular-value subspace.

> [!note]- Complete formal solution
> Let $T$ have SVD $T = \sum_{j=1}^{r} s_j f_j e_j^*$ with $s_1 \geq \cdots \geq s_r > 0$. The candidate is $T_k = \sum_{j=1}^{k} s_j f_j e_j^*$.
>
> *Achievement.* $T - T_k = \sum_{j > k} s_j f_j e_j^*$ has SVD form with largest singular value $s_{k+1}$. By [[Ex - SVD computes the operator norm]], $\|T - T_k\|_{\text{op}} = s_{k+1}$.
>
> *Lower bound.* For any $B$ with $\operatorname{rank} B \leq k$: by rank-nullity, $\dim \operatorname{null} B \geq n - k$. Let $U_{k+1} = \operatorname{span}(e_1, \ldots, e_{k+1})$, with $\dim U_{k+1} = k + 1$. Since $(n - k) + (k + 1) = n + 1 > n$, $\operatorname{null} B \cap U_{k+1}$ contains a unit vector $v$.
>
> On this $v$: $(T - B) v = Tv$ (since $Bv = 0$). Write $v = \sum_{j=1}^{k+1} \alpha_j e_j$ with $\sum |\alpha_j|^2 = 1$. Then $\|Tv\|^2 = \sum_{j=1}^{k+1} |\alpha_j|^2 s_j^2 \geq s_{k+1}^2 \sum |\alpha_j|^2 = s_{k+1}^2$. So $\|(T - B) v\| \geq s_{k+1}$, hence $\|T - B\|_{\text{op}} \geq s_{k+1}$.
>
> Combining, $\min_{\operatorname{rank} B \leq k} \|T - B\|_{\text{op}} = s_{k+1}$, achieved at $T_k$. $\blacksquare$
>
> **Frobenius norm version.** The same approach with the Frobenius norm: $\|T - T_k\|_F^2 = \sum_{j > k} s_j^2$, and the lower bound requires a more intricate argument (Weyl's inequality for singular values, $s_{j+\ell}(A + B) \leq s_{j+1}(A) + s_\ell(B)$, or a direct argument via von Neumann's trace inequality). The conclusion: $T_k$ is also the best rank-$k$ approximation in the Frobenius norm, with $\|T - T_k\|_F = \sqrt{\sum_{j > k} s_j^2}$.

---

# Key Takeaways

**The dimension intersection argument is the core of low-rank approximation theory.** The technique used here — two subspaces whose [[Def - Dimension|dimensions]] sum to more than the ambient dimension must intersect — is the foundational tool for nearly every lower bound in spectral approximation. The reason it works: for any candidate rank-$\leq k$ approximation $B$, the kernel of $B$ is at least $(n - k)$-dimensional; intersecting with the top-$(k+1)$ singular subspace (dimension $k+1$) forces a non-trivial vector where $T$ acts "with operator norm at least $s_{k+1}$". The same argument proves the Courant-Fischer min-max characterisation of eigenvalues, the Weyl inequalities for matrix sums, the Cauchy interlacing theorem for principal submatrices, and similar deep results about spectral interlacing.

**Eckart–Young is the foundation of all modern data approximation.** PCA, image compression, latent semantic analysis, recommender systems, randomised numerical linear algebra, sketching algorithms, matrix completion, dynamic mode decomposition, model order reduction in PDE — every one of these techniques exploits Eckart–Young to justify approximating large matrices by truncated SVDs. The fact that **the optimal rank-$k$ approximation is given by truncating the SVD** is the single most important computational fact in applied linear algebra. The decay rate of the singular values controls how compressible the matrix is, and the Eckart-Young error formula gives the precise reconstruction error.

**Low-rank approximation is non-convex but tractable thanks to SVD.** The set of rank-$\leq k$ matrices is *not* a subspace; it is an algebraic variety, the *secant variety* of the Segre variety. Optimisation problems with a low-rank constraint are *non-convex*, in general computationally hard (NP-hard for various norms). The Eckart-Young theorem is the special case where the non-convex constraint set admits a closed-form solution via SVD — the optimum can be read off without iterative optimisation. This makes low-rank SVD approximation tractable in a way that more general low-rank optimisation problems (like matrix completion with missing entries) are not. The exception is striking: a non-convex optimisation problem with a clean closed-form solution.

**The strict-singular-value-gap condition determines uniqueness.** When $s_k > s_{k+1}$ (a "spectral gap"), the truncated SVD $T_k$ is the unique best rank-$k$ approximation, and the principal subspaces are unambiguous. When $s_k = s_{k+1}$ (a "degenerate" or "tied" singular value), the best rank-$k$ approximation is not unique — there is a continuous family of equally good approximations, parameterised by rotations within the tied singular subspace. In data analysis applications, a strict spectral gap is what makes PCA's principal directions interpretable; without a gap, the "principal directions" are not well-defined and PCA outputs depend on numerical noise. The gap condition is what makes the analysis robust.
