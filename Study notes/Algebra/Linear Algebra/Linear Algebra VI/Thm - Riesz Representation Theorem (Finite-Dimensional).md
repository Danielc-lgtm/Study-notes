---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthonormal Basis"
  - "Def - Dual Space"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is a finite-dimensional inner product space over $\mathbf{F}$. $V' = \mathcal{L}(V, \mathbf{F})$ is the dual space — the space of linear functionals on $V$. A linear functional is denoted $\varphi : V \to \mathbf{F}$. The map $v \mapsto \varphi_v$, where $\varphi_v(u) = \langle u, v\rangle$, will be central. See [[Linear Algebra VI — §6 Inner Product Spaces]] for the full notation registry.

---

# Statement

> **Theorem (Riesz Representation Theorem, finite-dimensional).** Let $V$ be a finite-dimensional inner product space over $\mathbf{F}$, and let $\varphi \in V'$ be a linear functional on $V$. Then there exists a unique vector $v \in V$ such that
> $$\varphi(u) = \langle u, v\rangle \qquad \text{for every } u \in V.$$

> **Corollary (Antilinear isomorphism).** The map $\Phi : V \to V'$ defined by $\Phi(v) = \varphi_v$, where $\varphi_v(u) = \langle u, v\rangle$, is an antilinear (conjugate-linear) bijection. When $\mathbf{F} = \mathbb{R}$, it is a linear isomorphism $V \cong V'$. When $\mathbf{F} = \mathbb{C}$, it is a conjugate-linear isomorphism.

The Riesz representation theorem identifies $V$ with its dual via the inner product. Every linear functional on $V$ is "take the inner product with some specific vector".

---

# Motivation

The Riesz representation theorem is the structural result that makes an inner product space deserve the description "self-dual". In a general vector space $V$, the dual $V'$ is a different space — abstractly isomorphic to $V$ in finite dimensions (both have the same dimension), but there is no *canonical* isomorphism. To identify $V$ with $V'$, you have to *choose* a basis and use the dual basis, but the choice is arbitrary — a different basis gives a different isomorphism. The inner product fixes this: it provides a single canonical isomorphism, the Riesz map, that does not depend on any further choice.

The practical consequence is enormous. Every linear functional on $V$ is "an inner product with something", which lets you replace abstract functionals (functions from $V$ to $\mathbf{F}$) with concrete vectors. The mapping is **mechanical**: given $\varphi$, the representing vector is $v = \sum_k \overline{\varphi(e_k)}\, e_k$ in any orthonormal basis $e_1, \dots, e_n$, with the overline being the complex conjugate (which disappears over $\mathbb{R}$).

Three uses recur throughout linear algebra and analysis:

First, it is the **bridge between integrals and vectors**. In the inner product space $C[a, b]$ with $\langle f, g\rangle = \int fg$, a linear functional like $\varphi(f) = \int_a^b f(x) k(x)\, dx$ for some kernel function $k$ is, by Riesz, the inner product with $k$ itself. Linear functionals defined by integrals are *vectors* in $L^2$, identified via the integral as inner product. This is the foundation for **distribution theory** and **weak formulations** of partial differential equations.

Second, it is the **construction of the adjoint operator**. For $T \in \mathcal{L}(V, W)$ between inner product spaces, the **adjoint** $T^* \in \mathcal{L}(W, V)$ is defined by $\langle Tv, w\rangle = \langle v, T^* w\rangle$. The existence of $T^*$ as a unique linear map relies on Riesz: for each fixed $w \in W$, the functional $v \mapsto \langle Tv, w\rangle$ on $V$ is linear, so by Riesz it equals $\langle v, T^* w\rangle$ for a unique $T^* w \in V$. The adjoint exists because Riesz gives existence and uniqueness of the representing vector. The entire theory of self-adjoint, normal, and unitary operators in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] depends on this.

Third, in **infinite-dimensional Hilbert spaces**, the theorem extends with a continuity hypothesis: every **continuous** linear functional on a Hilbert space is represented by some vector. This is the **Riesz representation theorem for Hilbert spaces**, and it gives the canonical isomorphism $H \cong H^*$ (between $H$ and its continuous-dual) for any Hilbert space. The finite-dimensional version is the prototype.

The theorem is also a striking instance of **canonicality from structure**: in a general vector space, $V \cong V'$ requires a choice of basis. Adding an inner product upgrades the isomorphism from "exists" to "canonical" — the structure of the inner product is sufficient to single out one isomorphism among all possible ones.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: a linear functional on a finite-dimensional inner product space. The skill is recognising when a problem provides such a functional.

The first source is **an explicit linear functional defined by an integral, sum, or formula**. Property $B$: $\varphi(f) = \int_a^b f(x) k(x)\, dx$ for some specific $k$; or $\varphi(v) = \sum_k a_k v_k$ for specific $a_k$; or $\varphi(p) = p(c)$ (point evaluation). Bridge: each of these is linear in $f, v, p$ respectively, so Riesz gives a representing vector $v_\varphi$. The non-obvious step is identifying which vector $v_\varphi$ represents the functional — for the integral case, $v_\varphi = k$ if it lies in the space; for the point-evaluation, it requires more work.

The second source is **a functional that arises from a different inner product**. Property $B$: $\varphi(f) = \int f g$ where $g$ might not be in the relevant space. Bridge: even if $g \notin V$, the functional $\varphi$ is still defined on $V$ and is linear, so Riesz produces a unique $v_\varphi \in V$ with $\varphi(f) = \langle f, v_\varphi\rangle = \int f v_\varphi$. The representing vector $v_\varphi$ is then the *orthogonal projection* of $g$ onto $V$. This is LADR Example 6.44.

The third source is **an inequality of the form $\varphi(u) \leq C \|u\|$ for all $u$**. Property $B$: the functional is bounded by the norm with constant $C$. Bridge: by Riesz, $\varphi(u) = \langle u, v_\varphi\rangle$, and Cauchy-Schwarz gives $|\varphi(u)| \leq \|v_\varphi\|\,\|u\|$. The smallest valid $C$ is $\|v_\varphi\|$, and equality is achieved at $u = v_\varphi/\|v_\varphi\|$. This characterizes the **operator norm of $\varphi$** as $\|v_\varphi\|$.

The fourth source is **a linear-functional condition on a subspace, extending to the whole space**. Property $B$: $\varphi$ is defined on a subspace $U \subseteq V$, and you want a representing vector. Bridge: extend $\varphi$ to $V$ by some method (e.g., the [[Thm - Best Approximation by Orthogonal Projection|projection-based extension]]), then Riesz on $V$ gives a representing vector. The Hahn-Banach theorem in functional analysis is the infinite-dimensional refinement of this idea.

**Targets (Output Amplification)**

The conclusion is "$\varphi(u) = \langle u, v_\varphi\rangle$" for some unique $v_\varphi \in V$.

The first target is the **construction of adjoint operators**. Property $D$: $T \in \mathcal{L}(V, W)$, and you want $T^* \in \mathcal{L}(W, V)$ with $\langle Tv, w\rangle = \langle v, T^* w\rangle$. Combination: for each $w \in W$, the functional $v \mapsto \langle Tv, w\rangle$ on $V$ is linear; Riesz gives a unique $T^* w \in V$ with $\langle Tv, w\rangle = \langle v, T^* w\rangle$. The assignment $w \mapsto T^* w$ is linear (by uniqueness in Riesz). The entire spectral theory of inner-product operators depends on this construction.

The second target is **dual-basis identification**. Property $D$: an orthonormal basis $e_1, \dots, e_n$ of $V$. Combination: the dual basis $e_1^*, \dots, e_n^*$ of $V'$ is, under the Riesz isomorphism, $e_k^* \leftrightarrow e_k$. So orthonormal bases of $V$ are "self-dual" under the Riesz identification.

The third target is the **representation of integrals as inner products**. Property $D$: an explicit integral expression for $\varphi$. Combination: by Riesz, the integrand factors as the inner product with a single specific function — concretely, an integral $\int f k$ over $[a, b]$ in $L^2$ is "the inner product with $k$" (if $k \in L^2$).

The fourth target is **the duality $V \cong V'$ for infinite-dimensional Hilbert spaces**. Property $D$: continuity of the functional (in infinite dimensions). Combination: Riesz extends to continuous linear functionals on Hilbert spaces, providing the canonical identification $H \cong H^*$, the cornerstone of variational calculus, the calculus of variations, and weak formulations of PDEs.

---

# Why Is It True

The intuition is short and clean: **in a finite-dimensional space, a linear functional is determined by its values on a basis, and an orthonormal basis turns those values into a vector by the "stack them up" formula**.

Let $e_1, \dots, e_n$ be an orthonormal basis of $V$. A linear functional $\varphi$ is determined by the $n$ values $\varphi(e_1), \dots, \varphi(e_n)$ — these are scalars in $\mathbf{F}$. Now form the vector
$$
v = \overline{\varphi(e_1)}\, e_1 + \overline{\varphi(e_2)}\, e_2 + \cdots + \overline{\varphi(e_n)}\, e_n,
$$
where the overline is the complex conjugate (which disappears over $\mathbb{R}$). The conjugate is the price of the convention "linear in first slot, conjugate-linear in second" — see the warning callout on the parent topic page.

Check: for any $u \in V$, expand $u = \sum_k \langle u, e_k\rangle e_k$ (orthonormal-basis expansion). Compute $\langle u, v\rangle$ via the sesquilinear formula:
$$
\langle u, v\rangle = \left\langle \sum_k \langle u, e_k\rangle e_k, \sum_j \overline{\varphi(e_j)} e_j\right\rangle = \sum_{k, j} \langle u, e_k\rangle \overline{\overline{\varphi(e_j)}} \langle e_k, e_j\rangle = \sum_{k, j} \langle u, e_k\rangle \varphi(e_j) \delta_{kj} = \sum_k \langle u, e_k\rangle \varphi(e_k).
$$
But by linearity of $\varphi$, the right-hand side is $\varphi(\sum_k \langle u, e_k\rangle e_k) = \varphi(u)$. So $\langle u, v\rangle = \varphi(u)$, as desired.

**The one-liner mechanism: in an orthonormal basis, a linear functional is determined by its values $\varphi(e_k)$ on the basis vectors, and the representing vector is the "stack-them-up" sum $\sum_k \overline{\varphi(e_k)}\, e_k$ — the conjugation pays for the choice of "linear in first slot" convention.**

The uniqueness is easier: if $\varphi(u) = \langle u, v_1\rangle = \langle u, v_2\rangle$ for all $u$, then $\langle u, v_1 - v_2\rangle = 0$ for all $u$, so taking $u = v_1 - v_2$ gives $\|v_1 - v_2\|^2 = 0$, hence $v_1 = v_2$.

There is a second, more conceptual proof using orthogonal complements. If $\varphi = 0$ then $v = 0$ trivially. Otherwise $\ker\varphi$ is a hyperplane of codimension $1$, and $(\ker\varphi)^\perp$ is a $1$-dimensional subspace. Pick any nonzero $w \in (\ker\varphi)^\perp$; the representing vector must be a scalar multiple of $w$, and the scalar is determined by the requirement that $\varphi(w) = \langle w, v\rangle$. Explicitly, $v = \frac{\overline{\varphi(w)}}{\|w\|^2} w$. This proof (LADR's "revisited" proof, 6.58) emphasizes the geometric content: the representing vector lives in $(\ker\varphi)^\perp$, the perpendicular to the hyperplane on which $\varphi$ vanishes.

---

# What Makes This Hard

The proof is straightforward in finite dimensions but has two genuinely subtle points.

First, **the conjugate in the construction formula**. Over $\mathbb{R}$, $v = \sum_k \varphi(e_k) e_k$ is correct. Over $\mathbb{C}$, the formula is $v = \sum_k \overline{\varphi(e_k)} e_k$ — the conjugates are essential because of "linear in first slot, conjugate-linear in second". A common mistake is to drop the conjugates and get a *similar* but wrong representing vector.

Second, **the failure in infinite dimensions without continuity**. The theorem fails for general linear functionals on infinite-dimensional Hilbert spaces — only continuous (equivalently, bounded) functionals are representable. The pathology is that on an infinite-dimensional space, there exist discontinuous linear functionals (constructible using Hamel bases and the axiom of choice), and these cannot be represented by inner products with any vector. LADR Exercise 6B.22 gives a concrete example: on $C[-1, 1]$ with $\langle f, g\rangle = \int fg$, the functional $\varphi(f) = f(0)$ (point evaluation) is linear but cannot be represented as $\langle f, g\rangle$ for any continuous $g$. The reason is that point evaluation is not continuous in the $L^2$ norm — a sequence of functions converging in $L^2$ to a function need not converge pointwise.

A third subtle point: the **map $v \mapsto \varphi_v$ is antilinear over $\mathbb{C}$**, not linear. $\varphi_{\lambda v}(u) = \langle u, \lambda v\rangle = \bar\lambda \langle u, v\rangle = \bar\lambda \varphi_v(u)$. So the Riesz isomorphism is a conjugate-linear bijection, not a linear isomorphism, in the complex case. Over the reals, conjugation is trivial and the map is linear.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Pick an orthonormal basis. Define the representing vector by stacking up conjugated values of $\varphi$ on the basis. Verify directly that this gives the desired representation.

**Subgoal decomposition:**

1. **Choose an orthonormal basis.** Let $e_1, \dots, e_n$ be an orthonormal basis of $V$.
   - *Hint:* exists by Gram-Schmidt + corollary on existence of orthonormal bases.
   - *Why needed:* gives a concrete set of "axes" along which the functional's values can be tabulated.

2. **Define the candidate vector.** Set $v = \sum_k \overline{\varphi(e_k)}\, e_k$.
   - *Hint:* the conjugate is dictated by the convention "linear in first slot, conjugate-linear in second" — otherwise the formula would not work over $\mathbb{C}$.
   - *Why needed:* this is the explicit form of the representing vector.

3. **Verify representation.** Show $\langle u, v\rangle = \varphi(u)$ for every $u \in V$.
   - *Hint:* expand $u = \sum_k \langle u, e_k\rangle e_k$ and use bilinearity/sesquilinearity to compute $\langle u, v\rangle$; the result simplifies to $\sum_k \langle u, e_k\rangle \varphi(e_k) = \varphi(u)$ by linearity of $\varphi$.
   - *Why needed:* this is the existence statement.

4. **Verify uniqueness.** If $\varphi(u) = \langle u, v_1\rangle = \langle u, v_2\rangle$ for all $u$, then $v_1 = v_2$.
   - *Hint:* the inner-product condition $\langle u, v_1 - v_2\rangle = 0$ for all $u$, in particular for $u = v_1 - v_2$, gives $\|v_1 - v_2\|^2 = 0$.
   - *Why needed:* the uniqueness statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Existence — the candidate $v$ represents $\varphi$
> **Statement:** Let $e_1, \dots, e_n$ be an orthonormal basis of $V$, and $\varphi \in V'$. Set $v = \sum_{k=1}^n \overline{\varphi(e_k)}\, e_k$. Then $\langle u, v\rangle = \varphi(u)$ for every $u \in V$.
>
> **Hint:** Expand $u$ in the orthonormal basis, use sesquilinearity to compute $\langle u, v\rangle$, and simplify using orthonormality and linearity of $\varphi$.
>
> **Why needed:** This is the existence half of the theorem — explicit construction of the representing vector.
>
> > [!note]- Full proof
> > By the orthonormal-basis expansion, $u = \sum_k \langle u, e_k\rangle e_k$. Hence
> > $$\varphi(u) = \varphi\left(\sum_k \langle u, e_k\rangle e_k\right) = \sum_k \langle u, e_k\rangle \varphi(e_k)$$
> > by linearity of $\varphi$.
> >
> > On the other hand,
> > $$\langle u, v\rangle = \left\langle \sum_k \langle u, e_k\rangle e_k, \sum_j \overline{\varphi(e_j)}\, e_j\right\rangle.$$
> > By sesquilinearity (linear in the first slot, conjugate-linear in the second), this is
> > $$\sum_{k, j} \langle u, e_k\rangle \overline{\overline{\varphi(e_j)}}\, \langle e_k, e_j\rangle = \sum_{k, j} \langle u, e_k\rangle \varphi(e_j) \delta_{kj} = \sum_k \langle u, e_k\rangle \varphi(e_k) = \varphi(u),$$
> > where we used $\overline{\overline{\varphi(e_j)}} = \varphi(e_j)$ and $\langle e_k, e_j\rangle = \delta_{kj}$.

> [!note]- Lemma 2: Uniqueness — the representing vector is unique
> **Statement:** If $\varphi(u) = \langle u, v_1\rangle = \langle u, v_2\rangle$ for every $u \in V$, then $v_1 = v_2$.
>
> **Hint:** Subtract the two equations and use the definiteness of the inner product.
>
> **Why needed:** This is the uniqueness half of the theorem; without it, the construction in Lemma 1 might produce many different representing vectors depending on the basis.
>
> > [!note]- Full proof
> > For every $u$, $\langle u, v_1\rangle = \langle u, v_2\rangle$, so $\langle u, v_1 - v_2\rangle = 0$. Take $u = v_1 - v_2$: $\langle v_1 - v_2, v_1 - v_2\rangle = 0$, i.e., $\|v_1 - v_2\|^2 = 0$. By definiteness of the inner product, $v_1 - v_2 = 0$, so $v_1 = v_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be a finite-dimensional inner product space and $\varphi \in V'$. There exists a unique $v \in V$ with $\varphi(u) = \langle u, v\rangle$ for every $u \in V$.
>
> *Proof.* **Existence:** Let $e_1, \dots, e_n$ be an orthonormal basis of $V$ (existing by [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]]). Define $v = \sum_{k=1}^n \overline{\varphi(e_k)}\, e_k$. By Lemma 1, $\langle u, v\rangle = \varphi(u)$ for every $u$.
>
> **Uniqueness:** By Lemma 2. $\qquad\blacksquare$
>
> **Corollary (antilinear isomorphism).** The map $\Phi : V \to V'$ defined by $\Phi(v) = \varphi_v$, where $\varphi_v(u) = \langle u, v\rangle$, is an antilinear bijection.
>
> *Proof.* Bijectivity: surjectivity is the theorem (every $\varphi$ comes from some $v$); injectivity is uniqueness (different $v$'s give different $\varphi$'s). Antilinearity: $\Phi(\lambda v + w)(u) = \langle u, \lambda v + w\rangle = \bar\lambda \langle u, v\rangle + \langle u, w\rangle = \bar\lambda \varphi_v(u) + \varphi_w(u) = (\bar\lambda \Phi(v) + \Phi(w))(u)$.

> [!note]- Alternative proof via orthogonal complement (LADR's "Riesz Representation Theorem, Revisited")
> *Proof.* If $\varphi = 0$, take $v = 0$. Assume $\varphi \neq 0$.
>
> Then $\ker\varphi$ is a hyperplane of $V$ (codimension $1$), so $(\ker\varphi)^\perp$ has dimension $1$ (by the dimension formula for orthogonal complements). Pick any nonzero $w \in (\ker\varphi)^\perp$. By construction, $w \notin \ker\varphi$, so $\varphi(w) \neq 0$. Set
> $$v = \frac{\overline{\varphi(w)}}{\|w\|^2}\, w.$$
> Then $v \in (\ker\varphi)^\perp$ (it is a scalar multiple of $w$).
>
> We verify $\langle u, v\rangle = \varphi(u)$ for every $u$. Decompose $u = u_K + u_{K^\perp}$ along $V = \ker\varphi \oplus (\ker\varphi)^\perp$. Then:
> $$\langle u, v\rangle = \langle u_K, v\rangle + \langle u_{K^\perp}, v\rangle = 0 + \langle u_{K^\perp}, v\rangle$$
> (since $u_K \perp v$ because $v \in (\ker\varphi)^\perp$). Since $u_{K^\perp}$ is a scalar multiple $\alpha w$ of $w$, $\langle u_{K^\perp}, v\rangle = \alpha\langle w, v\rangle = \alpha \cdot \frac{\overline{\varphi(w)}}{\|w\|^2}\langle w, w\rangle = \alpha \overline{\varphi(w)}$, which... wait, let me redo this calculation with the conjugates carefully.
>
> Actually, the cleanest verification is: $\langle w, v\rangle = \langle w, \frac{\overline{\varphi(w)}}{\|w\|^2} w\rangle = \frac{\varphi(w)}{\|w\|^2}\|w\|^2 = \varphi(w)$ (using $\langle w, \bar\alpha w\rangle = \alpha\|w\|^2$). And $\varphi(u_K) = 0$, so $\varphi(u) = \varphi(u_{K^\perp})$. Both $\varphi$ and $\langle\cdot, v\rangle$ are linear and agree on $w$ and on $\ker\varphi$ (both vanish on the latter), so by linearity they agree on the span — i.e., on all of $V$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Distribution theory and weak formulations of PDEs.** In the theory of distributions, a distribution on $\Omega \subseteq \mathbb{R}^n$ is a continuous linear functional on the space of smooth compactly-supported test functions $C_c^\infty(\Omega)$. Many distributions are representable as integrals against locally-integrable functions, $T(\phi) = \int \phi f$ — these are the **regular distributions**, and the representation theorem connecting them to functions is a generalization of Riesz. But some distributions (the Dirac delta $\delta(\phi) = \phi(0)$, the principal value of $1/x$) cannot be represented this way; they require the broader framework of distributions. The breakdown of "every functional is an integral" is exactly the failure of Riesz beyond Hilbert spaces.

**Weak formulations of partial differential equations.** A weak formulation of a PDE like $-\Delta u = f$ on $\Omega$ converts it into "find $u \in H^1_0(\Omega)$ such that $\int \nabla u \cdot \nabla\phi = \int f\phi$ for every $\phi \in H^1_0(\Omega)$". The bilinear form $a(u, \phi) = \int \nabla u \cdot \nabla\phi$ is a (non-symmetric in general) version of an inner product, and the right-hand side is a linear functional in $\phi$. Existence of a solution $u$ follows from the **Lax-Milgram theorem**, which is the generalization of Riesz to (bounded, coercive) bilinear forms. So existence of solutions of elliptic PDEs is a Riesz-style functional-representation theorem.

**Construction of the adjoint operator.** For a linear map $T : V \to W$ between inner product spaces, the adjoint $T^* : W \to V$ is defined by $\langle Tv, w\rangle = \langle v, T^*w\rangle$ for all $v, w$. The existence of $T^*$ relies on Riesz: for each fixed $w$, the functional $v \mapsto \langle Tv, w\rangle$ on $V$ is linear, so Riesz gives a unique $T^*w \in V$ representing it. The linearity of $w \mapsto T^*w$ is automatic from uniqueness. This construction is the engine of the spectral theory in [[Linear Algebra VII — §7 Operators on Inner Product Spaces]].

**Probability: conditional expectation as orthogonal projection.** The conditional expectation $E[X | \mathcal{G}]$ of a random variable $X$ given a $\sigma$-algebra $\mathcal{G}$ is, in the $L^2$ inner product space, the orthogonal projection of $X$ onto $L^2(\mathcal{G})$ — the subspace of $\mathcal{G}$-measurable random variables. The defining property — $E[X 1_A] = E[E[X|\mathcal{G}] 1_A]$ for every $A \in \mathcal{G}$ — is exactly the Riesz characterization of $E[X|\mathcal{G}]$ as the representing vector for the linear functional $Y \mapsto E[XY]$ restricted to $L^2(\mathcal{G})$.

---

# Bridges

- **[[Def - Dual Space|Dual Space]]** *(from Linear Algebra IV)* — the dual $V'$ of a vector space is the space of linear functionals. Without an inner product, $V \cong V'$ holds in finite dimensions but not canonically (the isomorphism depends on the choice of basis). With an inner product, Riesz provides a canonical isomorphism $V \cong V'$ — the "self-dual" structure that inner-product spaces possess. The map is antilinear over $\mathbb{C}$ (linear over $\mathbb{R}$).

- **Adjoint Operators** *(Linear Algebra VII)* — Riesz is the proof that adjoints exist. For $T \in \mathcal{L}(V, W)$, the adjoint $T^* \in \mathcal{L}(W, V)$ is the unique map with $\langle Tv, w\rangle = \langle v, T^*w\rangle$. Existence: fix $w$; the functional $v \mapsto \langle Tv, w\rangle$ on $V$ is linear, so Riesz gives a unique $T^*w \in V$ representing it. Linearity in $w$: by uniqueness in Riesz. The entire theory of self-adjoint, normal, unitary operators rests on this.

- **Hilbert Projection Theorem and infinite-dimensional Riesz** *(Functional Analysis)* — the Riesz representation theorem extends to Hilbert spaces with the modification that **continuous** (equivalently, bounded) linear functionals are representable: for $\varphi \in H^*$ (the continuous dual), there exists unique $v \in H$ with $\varphi(u) = \langle u, v\rangle$. This gives the canonical isometric isomorphism $H \cong H^*$ (antilinear over $\mathbb{C}$). The proof uses the orthogonal-projection construction (LADR 6.58 generalizes), and it is one of the foundational theorems of functional analysis. Without continuity, the theorem fails: there exist discontinuous linear functionals on infinite-dim Hilbert spaces (using Hamel bases and choice) that have no representing vector.

- **Lax-Milgram theorem** *(PDE Theory)* — for a continuous, coercive bilinear form $a : H \times H \to \mathbf{F}$ (not necessarily symmetric or Hermitian) on a Hilbert space $H$, and any continuous linear functional $\varphi \in H^*$, there exists a unique $u \in H$ with $a(u, v) = \varphi(v)$ for all $v$. This is the generalization of Riesz to non-symmetric bilinear forms, and it is the existence theorem for solutions of elliptic PDEs in weak formulation.

- **Bra-ket notation in quantum mechanics** *(Physics)* — in Dirac notation, a "bra" $\langle\phi|$ is a linear functional on a Hilbert space (an element of $H^*$), and a "ket" $|\psi\rangle$ is a vector in $H$. Riesz says: every bra is the dual (Riesz-conjugate) of some ket, $\langle\phi| = (|\phi\rangle)^*$ — the canonical conjugate-linear identification provided by the inner product. The pairing $\langle\phi|\psi\rangle$ is then the inner product $\langle\phi, \psi\rangle$ in physics convention (with $\phi$ in the conjugate-linear slot). The whole bra-ket formalism is Riesz applied systematically in quantum mechanics.
