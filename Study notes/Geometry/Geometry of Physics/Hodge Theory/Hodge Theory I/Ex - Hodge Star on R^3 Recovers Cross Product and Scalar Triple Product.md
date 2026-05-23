---
type: exercise
subject: hodge-theory
difficulty: "⭐"
prereqs:
  - "Def - The Hodge Star Operator"
  - "Thm - Properties of the Hodge Star"
  - "Def - Musical Isomorphism (Flat and Sharp)"
tags: [geometry, hodge-theory, vector-calculus]
---

# Problem Statement

Work in Euclidean $\mathbb{R}^3$ with coordinates $(x, y, z)$, the standard metric $g = dx^2 + dy^2 + dz^2$, and orientation $\operatorname{vol}_3 = dx \wedge dy \wedge dz$. Let $\star : \Omega^k(\mathbb{R}^3) \to \Omega^{3-k}(\mathbb{R}^3)$ be the Hodge star operator.

(a) Compute $\star$ on every basis $k$-form for $k = 0, 1, 2, 3$.

(b) Given two vectors $\vec u = u_1 e_1 + u_2 e_2 + u_3 e_3$ and $\vec v = v_1 e_1 + v_2 e_2 + v_3 e_3$ in $\mathbb{R}^3$, let $u^\flat = u_1 dx + u_2 dy + u_3 dz$ and $v^\flat = v_1 dx + v_2 dy + v_3 dz$ be their metric dual $1$-forms. Compute $u^\flat \wedge v^\flat$ as a $2$-form, then apply $\star$ to get a $1$-form, then apply the musical sharp $\sharp$ to get back a vector. Show that the result is the cross product $\vec u \times \vec v$:
$$(\star(u^\flat \wedge v^\flat))^\sharp = \vec u \times \vec v.$$

(c) Given three vectors $\vec u, \vec v, \vec w$, compute $\star(u^\flat \wedge v^\flat \wedge w^\flat)$ and show that it equals the scalar triple product $\vec u \cdot (\vec v \times \vec w) = \det\begin{pmatrix}\vec u & \vec v & \vec w\end{pmatrix}$.

**Recall:**

The Hodge star $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ on an oriented Riemannian manifold is defined by $\alpha \wedge \star\beta = \langle\alpha,\beta\rangle_g\operatorname{vol}_n$. By [[Thm - Properties of the Hodge Star]], on an orthonormal coframe with the standard orientation, $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$ where $I^c$ is the complementary multi-index in increasing order, and $\mathrm{sgn}(I, I^c) = \pm 1$ is the sign of the permutation taking $(1, \dots, n) \to (i_1, \dots, i_k, j_1, \dots, j_{n-k})$.

![[Def - The Hodge Star Operator#The Definition]]

The musical isomorphism $\flat : TM \to T^*M$ sends a vector $X$ to the $1$-form $X^\flat = g(X, \cdot)$. Its inverse is $\sharp$. On Euclidean $\mathbb{R}^3$, $u^\flat$ has the same components as $\vec u$: $(u_1 e_1 + u_2 e_2 + u_3 e_3)^\flat = u_1 dx + u_2 dy + u_3 dz$.

The cross product $\vec u \times \vec v = \det\begin{pmatrix} e_1 & e_2 & e_3 \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{pmatrix} = (u_2 v_3 - u_3 v_2)e_1 + (u_3 v_1 - u_1 v_3)e_2 + (u_1 v_2 - u_2 v_1)e_3$.

---

# Convergent Strategy

**Problem class:** Concrete computation of the Hodge star in low [[Def - Dimension|dimensions]], with the goal of recovering classical vector-calculus operations from Hodge-theoretic ones. The problem class is "translate between forms and vectors via $\flat$, $\sharp$, $\star$". The chapter's problem-solving strategy in §1.1 (compute $\star$ in coordinates) applies directly: use orthonormal-coframe formulas.

**Assumption pattern:** Euclidean $\mathbb{R}^3$ with standard metric and orientation. The orthonormal coframe is the coordinate coframe $(dx, dy, dz)$, with all metric signs $\epsilon_i = +1$. The orientation is positive, with $dx\wedge dy\wedge dz = \operatorname{vol}_3$. These standard choices simplify all signs and make the computation purely combinatorial.

**Theorem routing:** Use [[Thm - Properties of the Hodge Star]] property 5 (coordinate formula on orthonormal coframes) to compute $\star$ on basis forms. For the cross product identification, use the bilinearity of $\wedge$ and the definition of $\flat$ / $\sharp$ to relate basis-form computations to vector computations.

**Key decision point:** Recognize that the cross product's antisymmetry and bilinearity match exactly the $\wedge$-product's antisymmetry plus bilinearity. The Hodge star $\star : \Omega^2(\mathbb{R}^3) \to \Omega^1(\mathbb{R}^3)$ is the bridge, sending the $2$-form $u^\flat \wedge v^\flat$ (encoding bivector data) to the $1$-form $(\vec u \times \vec v)^\flat$ (encoding vector data). The key insight: classical vector calculus on $\mathbb{R}^3$ is form-calculus combined with the Hodge star.

---

# Legal Operations Used

1. **Apply the coordinate formula for $\star$** (operation 2 from the topic page, peeling off $\star\star$, but more directly the explicit coordinate formula). For each basis form $\sigma^I$, the formula $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$ gives the answer immediately. In $\mathbb{R}^3$ all signs $\epsilon_I = +1$, simplifying to just the orientation sign.

2. **Use the defining identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\operatorname{vol}_n$** (operation 1 from the topic page). For verification, computing the wedge product of basis forms and comparing with the inner-product times volume form provides a check.

3. **Compute the wedge product of $1$-forms via the determinant identity** $(\omega^1\wedge\omega^2)(v_1, v_2) = \det(\omega^i(v_j))$. For the cross product identification, this lets us compute $u^\flat\wedge v^\flat$ as the determinant pattern that matches the cross product.

---

# Hints

> [!note]- Hint 1
> Use the coordinate formula $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$ on the standard orthonormal coframe $(dx, dy, dz)$ of $\mathbb{R}^3$. For each multi-index $I$, identify the complementary multi-index $I^c$ and the sign of the permutation. The orientation $dx\wedge dy\wedge dz$ corresponds to the identity permutation, so $\mathrm{sgn} = +1$ when $I$ is in "cyclic" order.

> [!note]- Hint 2
> For part (b), expand $u^\flat\wedge v^\flat$ as a sum of basis $2$-forms: $u^\flat\wedge v^\flat = \sum_{i<j}(u_i v_j - u_j v_i)dx^i\wedge dx^j$. Apply $\star$ to each basis $2$-form using part (a). The result is a $1$-form whose coefficients are exactly the cross-product components.

> [!note]- Hint 3
> For part (c), $u^\flat\wedge v^\flat\wedge w^\flat$ is a top-degree form on $\mathbb{R}^3$. Use the determinant identity for the wedge of three $1$-forms to express it as $\det(u_i, v_j, w_k)dx\wedge dy\wedge dz = (\text{determinant}) \cdot \operatorname{vol}_3$. Applying $\star$ to $\operatorname{vol}_3$ gives $1$, so $\star(u^\flat\wedge v^\flat\wedge w^\flat) =$ the determinant.

---

# Solution

The proof has three parts corresponding to the three questions. Part (a) is a direct application of the coordinate formula for $\star$ on an orthonormal coframe. Part (b) expands $u^\flat\wedge v^\flat$ as a sum of basis $2$-forms, applies $\star$, and converts the result back to a vector via $\sharp$. Part (c) uses the determinant identity for the wedge of three $1$-forms.

**Step 1: Compute $\star$ on each basis form (part (a)).**

The orthonormal coframe of $\mathbb{R}^3$ is $(dx, dy, dz) = (\sigma^1, \sigma^2, \sigma^3)$ with the standard metric and orientation $\operatorname{vol}_3 = dx\wedge dy\wedge dz$.

> [!note]- Derivation
> Apply $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$ from [[Thm - Properties of the Hodge Star]]:
>
> **Degree $0$:** $I = \emptyset$, $I^c = \{1,2,3\}$, $\mathrm{sgn}(\emptyset, \{1,2,3\}) = +1$ (identity permutation). $\star 1 = +dx\wedge dy\wedge dz = \operatorname{vol}_3$. ✓
>
> **Degree $1$:** $I = \{i\}$ for $i \in \{1, 2, 3\}$. Then $I^c$ is the complementary pair.
> - $I = \{1\}$: $I^c = \{2, 3\}$, $\mathrm{sgn}(\{1\}, \{2, 3\})$ = sign of $(1, 2, 3)\to(1, 2, 3)$ = $+1$. So $\star dx = dy\wedge dz$.
> - $I = \{2\}$: $I^c = \{1, 3\}$, $\mathrm{sgn}(\{2\}, \{1, 3\})$ = sign of $(1, 2, 3)\to(2, 1, 3)$ = $-1$. So $\star dy = -dx\wedge dz = dz\wedge dx$.
> - $I = \{3\}$: $I^c = \{1, 2\}$, $\mathrm{sgn}(\{3\}, \{1, 2\})$ = sign of $(1, 2, 3)\to(3, 1, 2)$ = $+1$ (cyclic). So $\star dz = dx\wedge dy$.
>
> **Degree $2$:** $I = \{i, j\}$ with $i < j$. Apply the double-star formula: $\star\star = (-1)^{1\cdot 2 + 0} = +1$ on $1$-forms in $3$D, so $\star^{-1} = \star$. Hence:
> - $\star(dy\wedge dz) = \star\star dx = dx$.
> - $\star(dz\wedge dx) = \star\star dy = dy$.
> - $\star(dx\wedge dy) = \star\star dz = dz$.
>
> **Degree $3$:** $I = \{1, 2, 3\}$, $I^c = \emptyset$, $\mathrm{sgn}(\{1,2,3\}, \emptyset) = +1$. So $\star\operatorname{vol}_3 = \star(dx\wedge dy\wedge dz) = 1$.
>
> **Summary table:**
> | Form | Star |
> |---|---|
> | $1$ | $dx\wedge dy\wedge dz$ |
> | $dx$ | $dy\wedge dz$ |
> | $dy$ | $dz\wedge dx$ |
> | $dz$ | $dx\wedge dy$ |
> | $dy\wedge dz$ | $dx$ |
> | $dz\wedge dx$ | $dy$ |
> | $dx\wedge dy$ | $dz$ |
> | $dx\wedge dy\wedge dz$ | $1$ |
>
> All signs positive; the pattern is the "cyclic" identification $1 \leftrightarrow dx\wedge dy\wedge dz$, $dx \leftrightarrow dy\wedge dz$, etc.

**Step 2: Cross product from $\star(u^\flat \wedge v^\flat)$ (part (b)).**

Compute $u^\flat\wedge v^\flat$ first as a sum of basis $2$-forms, then apply $\star$, then apply $\sharp$ to convert the $1$-form back to a vector.

> [!note]- Derivation
> Expand the wedge product:
> $$u^\flat\wedge v^\flat = (u_1 dx + u_2 dy + u_3 dz)\wedge(v_1 dx + v_2 dy + v_3 dz).$$
>
> Distribute and collect using $dx\wedge dx = 0$, $dx\wedge dy = -dy\wedge dx$, etc.:
> $$u^\flat\wedge v^\flat = (u_1 v_2 - u_2 v_1)dx\wedge dy + (u_1 v_3 - u_3 v_1)dx\wedge dz + (u_2 v_3 - u_3 v_2)dy\wedge dz.$$
>
> Rewrite using the "cyclic" basis $dy\wedge dz, dz\wedge dx, dx\wedge dy$ (rearranging $dx\wedge dz = -dz\wedge dx$):
> $$u^\flat\wedge v^\flat = (u_2 v_3 - u_3 v_2)dy\wedge dz + (u_3 v_1 - u_1 v_3)dz\wedge dx + (u_1 v_2 - u_2 v_1)dx\wedge dy.$$
>
> Apply $\star$ using Step 1:
> $$\star(u^\flat\wedge v^\flat) = (u_2 v_3 - u_3 v_2)dx + (u_3 v_1 - u_1 v_3)dy + (u_1 v_2 - u_2 v_1)dz.$$
>
> Now $\sharp$ on this $1$-form (which on Euclidean $\mathbb{R}^3$ just converts $dx, dy, dz$ to $e_1, e_2, e_3$ by raising the index with the metric, which is the identity for the standard Euclidean metric):
> $$(\star(u^\flat\wedge v^\flat))^\sharp = (u_2 v_3 - u_3 v_2)e_1 + (u_3 v_1 - u_1 v_3)e_2 + (u_1 v_2 - u_2 v_1)e_3.$$
>
> By inspection, this is exactly the cross product $\vec u \times \vec v$ (using $\vec u \times \vec v = \det(\vec e, \vec u, \vec v)$ expanded along the first row).
>
> So $\star(u^\flat\wedge v^\flat)^\sharp = \vec u \times \vec v$. ✓

**Step 3: Scalar triple product from $\star(u^\flat\wedge v^\flat\wedge w^\flat)$ (part (c)).**

Compute the wedge of three $1$-forms via the determinant identity.

> [!note]- Derivation
> By the determinant identity for the wedge of three $1$-forms (special case of the wedge-product formula $(\omega^1\wedge\cdots\wedge\omega^k)(v_1,\dots,v_k) = \det(\omega^i(v_j))$, evaluated on the standard basis):
> $$u^\flat\wedge v^\flat\wedge w^\flat = \det\begin{pmatrix}u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3\end{pmatrix}\,dx\wedge dy\wedge dz.$$
>
> Equivalently, expanding the wedge directly: $u^\flat\wedge v^\flat\wedge w^\flat = u_i v_j w_k\,dx^i\wedge dx^j\wedge dx^k$, which is nonzero only when $\{i, j, k\} = \{1, 2, 3\}$, giving the alternating sum of products = determinant.
>
> Now apply $\star$ to the top-degree form: from Step 1, $\star(dx\wedge dy\wedge dz) = 1$. So
> $$\star(u^\flat\wedge v^\flat\wedge w^\flat) = \det\begin{pmatrix}u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3\end{pmatrix} = \vec u \cdot(\vec v\times\vec w),$$
> the scalar triple product. ✓

> [!note]- Complete formal solution
> **Part (a):** Using the formula $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$ on the orthonormal coframe $(dx, dy, dz)$ of $\mathbb{R}^3$ with orientation $\operatorname{vol}_3 = dx\wedge dy\wedge dz$:
> - $\star 1 = dx\wedge dy\wedge dz$, $\star\operatorname{vol}_3 = 1$.
> - $\star dx = dy\wedge dz$, $\star dy = dz\wedge dx$, $\star dz = dx\wedge dy$ (signs by the cyclic order of multi-indices).
> - $\star(dy\wedge dz) = dx$, $\star(dz\wedge dx) = dy$, $\star(dx\wedge dy) = dz$ (by the double-star formula $\star\star = +1$ on $1$-forms in $3$D, applied to part (a)'s degree-$1$ results).
>
> **Part (b):** For vectors $\vec u, \vec v \in \mathbb{R}^3$ with dual $1$-forms $u^\flat, v^\flat$:
> $$u^\flat\wedge v^\flat = (u_2 v_3 - u_3 v_2)dy\wedge dz + (u_3 v_1 - u_1 v_3)dz\wedge dx + (u_1 v_2 - u_2 v_1)dx\wedge dy.$$
> Applying $\star$ using part (a):
> $$\star(u^\flat\wedge v^\flat) = (u_2 v_3 - u_3 v_2)dx + (u_3 v_1 - u_1 v_3)dy + (u_1 v_2 - u_2 v_1)dz.$$
> Applying $\sharp$ (trivial on Euclidean $\mathbb{R}^3$, just raises $dx^i$ to $e_i$):
> $$(\star(u^\flat\wedge v^\flat))^\sharp = (u_2 v_3 - u_3 v_2)e_1 + (u_3 v_1 - u_1 v_3)e_2 + (u_1 v_2 - u_2 v_1)e_3 = \vec u\times\vec v.$$
>
> **Part (c):** For three vectors $\vec u, \vec v, \vec w$, by the determinant identity for $\wedge$:
> $$u^\flat\wedge v^\flat\wedge w^\flat = \det\begin{pmatrix}u_1 & u_2 & u_3\\v_1 & v_2 & v_3\\w_1 & w_2 & w_3\end{pmatrix}dx\wedge dy\wedge dz.$$
> Applying $\star$ and using $\star\operatorname{vol}_3 = 1$:
> $$\star(u^\flat\wedge v^\flat\wedge w^\flat) = \det\begin{pmatrix}u_1 & u_2 & u_3\\v_1 & v_2 & v_3\\w_1 & w_2 & w_3\end{pmatrix} = \vec u\cdot(\vec v\times\vec w).$$
> $\qquad\blacksquare$

---

# Key Takeaways

**Hodge star = vector calculus structures in disguise.** The most important takeaway is that classical vector calculus on $\mathbb{R}^3$ is *literally* the calculus of forms combined with the Hodge star and the musical isomorphism. The cross product is $(\star(u^\flat\wedge v^\flat))^\sharp$; the curl is $(\star d F^\flat)^\sharp$; the divergence is $-\delta F^\flat$ on $1$-forms. Every classical vector calculus identity ($\nabla\cdot(\nabla\times \vec F) = 0$, $\nabla\times(\nabla f) = 0$, the triple product expansion, etc.) is an instance of $d^2 = 0$ or $\star\star = \mathrm{id}$ in some degree. When stuck on a vector calculus problem, translate to forms — the form-language version is almost always cleaner and reveals the underlying structure.

**The Hodge star is "complementary multi-index" with orientation sign.** The most reusable algorithmic insight is that $\star$ on an orthonormal coframe is just "swap the multi-index for its complement, with a sign". The sign tracks the orientation: when the concatenation of the multi-index and its complement is a positive permutation of the standard order, the sign is $+1$; otherwise $-1$. This makes $\star$ purely combinatorial on basis forms, and the only complication in general computations comes from non-orthonormal coframes (where extra $\sqrt{|g|}$ factors appear) or from non-standard orientations.

**The cross product is special to $\mathbb{R}^3$.** The reason there is no "cross product" in $\mathbb{R}^4$ or other dimensions is that $\mathbb{R}^3$ is the unique dimension where $\binom{n}{2} = n$ — equivalently, where the Hodge star maps $2$-forms back to $1$-forms (so $\Omega^2 \cong \Omega^1$ via $\star$). In $\mathbb{R}^4$, $\star : \Omega^2 \to \Omega^2$ stays in degree $2$, giving the self-dual / anti-self-dual decomposition instead of a cross product. In $\mathbb{R}^n$ for $n \geq 4$, the wedge of two $1$-forms is genuinely a $2$-form, with no canonical conversion back to a $1$-form / vector. The cross product is a low-dimensional accident; the wedge product is the dimension-independent generalization.

This exercise complements [[Ex - Maxwell's Equations Use the Codifferential]] (which extends form-calculus to Lorentzian signature for electromagnetism) and [[Ex - Computing the Hodge Star on S^2]] (which computes $\star$ in spherical coordinates with a non-flat metric).
