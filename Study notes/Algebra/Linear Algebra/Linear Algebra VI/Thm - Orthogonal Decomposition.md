---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal Complement"
  - "Def - Direct Sum"
  - "Def - Orthonormal Basis"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. $U \subseteq V$ is a subspace (typically finite-dimensional). $U^\perp$ is the orthogonal complement of $U$ in $V$. The notation registry is on [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Orthogonal Decomposition).** Let $V$ be an inner product space and $U \subseteq V$ a finite-dimensional subspace. Then $V = U \oplus U^\perp$ — every $v \in V$ has a unique decomposition
> $$v = u + w, \qquad u \in U,\ w \in U^\perp.$$

> **Corollary (Dimension formula).** If $V$ is finite-dimensional, $\dim U + \dim U^\perp = \dim V$.

> **Corollary (Double-perp).** For $U$ finite-dimensional, $(U^\perp)^\perp = U$.

> **Corollary ($U^\perp = \{0\} \iff U = V$, for finite-dim $U$).** If $U$ is a finite-dimensional subspace and $U^\perp = \{0\}$, then $U = V$.

---

# Motivation

The orthogonal decomposition is the structural backbone of the chapter. Once you know $V = U \oplus U^\perp$, every problem about $V$ can be split into a problem about $U$ and a problem about $U^\perp$ — and the two halves do not interact (orthogonally), so they can be analyzed independently. This is the recurring structural pattern that powers Cauchy-Schwarz (decompose along $\operatorname{span}(v)$ and $\operatorname{span}(v)^\perp$), orthogonal projections (the operator $P_U$ is well-defined only because $U \oplus U^\perp = V$), the best-approximation theorem (the closest point in $U$ to $v$ is the $U$-component of $v$), and Riesz representation (write $V = \ker\varphi \oplus (\ker\varphi)^\perp$ and the representing vector lives in the second summand).

The theorem matters most for what it makes constructive. In a general vector space, "complementary subspaces" exist (any subspace has a complement), but the complement is not unique. With an inner product, the orthogonal complement *is* unique and canonical, and the decomposition $V = U \oplus U^\perp$ is forced — no further choice required. This canonicality is what lets orthogonal projection be a *canonical* operator, not a choice-dependent one.

The theorem fails in infinite-dimensional inner product spaces when $U$ is not closed. The pathological example is $U = \{f \in C[-1, 1] : f(0) = 0\}$ in $L^2[-1, 1]$ — then $U^\perp = \{0\}$ (any continuous $g$ orthogonal to every $f \in U$ must vanish on $[-1, 0) \cup (0, 1]$ by density arguments, hence everywhere) but $U \neq V$ (the constant function $1$ is in $V$, not $U$). The repair is the **Hilbert projection theorem**: $V = U \oplus U^\perp$ holds for closed subspaces in any Hilbert space. The finite-dimensional case avoids the pathology because in finite dimensions every subspace is automatically closed.

The orthogonal decomposition is also the **finite-dimensional version of the projection theorem** that, in Hilbert spaces, extends to closed convex subsets. The much stronger statement "every closed convex subset $C$ of a Hilbert space has a unique closest point to any $v$" is the centerpiece of convex optimization in infinite dimensions, and it has the orthogonal decomposition as its closed-subspace special case.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is: a finite-dimensional subspace of an inner product space.

The first source is **the span of a finite list of vectors $v_1, \dots, v_m$**. Property $B$: $U = \operatorname{span}(v_1, \dots, v_m)$ is finite-dimensional (dimension $\leq m$). Bridge: the orthogonal decomposition applies to any such $U$; specifically, $V = U \oplus U^\perp$.

The second source is **the range of a finite-dimensional-domain linear map**. Property $B$: $T : V_0 \to W$ with $V_0$ finite-dimensional; then $\operatorname{range} T$ has dimension $\leq \dim V_0$, hence is finite-dimensional. Bridge: $W = \operatorname{range} T \oplus (\operatorname{range} T)^\perp$.

The third source is **the kernel of a non-zero linear functional**. Property $B$: $\varphi \neq 0$ is a linear functional on $V$ (finite-dimensional), and $\ker\varphi$ has codimension $1$ — equivalently, $(\ker\varphi)^\perp$ has dimension $1$. Bridge: $V = \ker\varphi \oplus (\ker\varphi)^\perp$, and the representing vector for $\varphi$ via Riesz lives in the $1$-dimensional second summand.

The fourth source is **the kernel of a linear map**. Property $B$: $T : V \to W$ with $V$ finite-dimensional; then $\ker T \subseteq V$ is finite-dimensional. Bridge: $V = \ker T \oplus (\ker T)^\perp$, and the restriction $T|_{(\ker T)^\perp}$ is injective. This is the structural identity behind the [[Def - Pseudoinverse|pseudoinverse]] construction.

**Targets (Output Amplification)**

The conclusion gives the unique decomposition $v = u + w$.

The first target is the **construction of orthogonal projection** $P_U \in \mathcal{L}(V)$. Property $D$: given $v$, the decomposition is unique. Combination: define $P_U v = u$ (the $U$-component); this is well-defined linear operator that satisfies all the properties of an orthogonal projection. Without orthogonal decomposition, no canonical $P_U$ exists.

The second target is the **best-approximation theorem**. Property $D$: for any $u' \in U$ and $v \in V$, write $v - u' = (v - P_U v) + (P_U v - u')$ — an orthogonal decomposition (since $v - P_U v \in U^\perp$ and $P_U v - u' \in U$). Combination: Pythagoras gives $\|v - u'\|^2 = \|v - P_U v\|^2 + \|P_U v - u'\|^2 \geq \|v - P_U v\|^2$, with equality iff $u' = P_U v$.

The third target is **dimension counting and double-perp**. Property $D$: combining the dimension formula $\dim U + \dim U^\perp = \dim V$ with $(U^\perp)^\perp \supseteq U$, the dimension of $(U^\perp)^\perp$ equals $\dim V - \dim U^\perp = \dim U$, so $(U^\perp)^\perp = U$. Combination: gives the "involutive" character of the orthogonal-complement operation.

The fourth target is the **kernel-range decomposition for linear maps**. Property $D$: $V = \ker T \oplus (\ker T)^\perp$, and $T$ restricted to $(\ker T)^\perp$ is injective. Combination: gives the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] in orthogonal form, the foundation of the pseudoinverse and the [[Linear Algebra VII — §7 Operators on Inner Product Spaces|singular value decomposition]].

---

# Why Is It True

The intuition is constructive: **the decomposition can be computed explicitly by orthogonal projection onto $U$ using any orthonormal basis of $U$**.

Choose an orthonormal basis $e_1, \dots, e_m$ of $U$ (existing by [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]]). For any $v \in V$, define
$$
u = \sum_{k=1}^m \langle v, e_k\rangle e_k \in U,
$$
$$
w = v - u = v - \sum_{k=1}^m \langle v, e_k\rangle e_k.
$$
Then $u \in U$ by construction. And $w$ is orthogonal to every $e_k$ (by direct computation: $\langle w, e_l\rangle = \langle v, e_l\rangle - \sum_k \langle v, e_k\rangle\langle e_k, e_l\rangle = \langle v, e_l\rangle - \langle v, e_l\rangle = 0$), so $w \perp U$, i.e., $w \in U^\perp$.

**The one-liner mechanism: project $v$ onto $U$ via the orthonormal-basis formula $u = \sum_k \langle v, e_k\rangle e_k$, and the residual $w = v - u$ is automatically in $U^\perp$ by the orthonormality of the basis.**

Uniqueness: if $v = u_1 + w_1 = u_2 + w_2$ with $u_1, u_2 \in U$ and $w_1, w_2 \in U^\perp$, then $u_1 - u_2 = w_2 - w_1$. The left side is in $U$, the right side is in $U^\perp$; their difference is in $U \cap U^\perp = \{0\}$ (the only vector orthogonal to itself is $0$). So $u_1 = u_2$ and $w_1 = w_2$.

The dimension formula follows: $V = U \oplus U^\perp$ as a direct sum means $\dim V = \dim U + \dim U^\perp$. Specialising further: $(U^\perp)^\perp \supseteq U$ (any vector in $U$ is orthogonal to everything orthogonal to $U$, by symmetry); combining with the dimension formula $(\dim (U^\perp)^\perp = \dim V - \dim U^\perp = \dim U)$ forces $(U^\perp)^\perp = U$.

---

# What Makes This Hard

The proof is two lines using Gram-Schmidt, but two subtleties merit attention.

First, **uniqueness** is what gives the decomposition its power. Without uniqueness, the operator $P_U$ would not be well-defined. The argument $u_1 - u_2 = w_2 - w_1 \in U \cap U^\perp = \{0\}$ is the entire content of uniqueness, but it relies on the fact that $U \cap U^\perp = \{0\}$ — i.e., the only vector orthogonal to itself is zero, which is the definiteness axiom of the inner product. Without definiteness (e.g., in indefinite spaces like Minkowski space), the intersection $U \cap U^\perp$ can contain *nonzero* lightlike vectors, and the decomposition fails to be unique.

Second, **the finite-dimensionality of $U$** is essential. In infinite dimensions, the construction $u = \sum_k \langle v, e_k\rangle e_k$ requires a *countable* orthonormal basis of $U$ and an *infinite sum*, which converges by Bessel's inequality only in the *closure* of $U$. So the natural decomposition is $V = \overline{U} \oplus U^\perp$, which collapses to $V = U \oplus U^\perp$ exactly when $U$ is closed. In the example $U = \{f \in C[-1, 1] : f(0) = 0\}$ which is dense but not closed in $L^2$, the closure is the entire space $L^2$, $U^\perp = \{0\}$, and the "decomposition" $V = U + \{0\}$ holds only at the level of $\overline{U} = V$, not of $U$ itself.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Existence: project $v$ onto $U$ using any orthonormal basis of $U$, then take the residual. Uniqueness: $U \cap U^\perp = \{0\}$.

**Subgoal decomposition:**

1. **Choose an orthonormal basis of $U$.** Let $e_1, \dots, e_m$ be an orthonormal basis of $U$ (existing by Gram-Schmidt).
   - *Hint:* finite-dimensional $\Rightarrow$ Gram-Schmidt applies.
   - *Why needed:* makes the projection explicitly computable.

2. **Define the candidate decomposition.** Set $u = \sum_{k=1}^m \langle v, e_k\rangle e_k$ and $w = v - u$.
   - *Hint:* $u \in U$ by construction (it is a linear combination of the $e_k$'s).
   - *Why needed:* explicit construction of the decomposition.

3. **Verify $w \in U^\perp$.** Show $\langle w, e_l\rangle = 0$ for each $l$.
   - *Hint:* direct computation using orthonormality.
   - *Why needed:* this is the orthogonality half.

4. **Uniqueness.** If $v = u_1 + w_1 = u_2 + w_2$ with $u_i \in U, w_i \in U^\perp$, then $u_1 - u_2 = w_2 - w_1 \in U \cap U^\perp = \{0\}$.
   - *Hint:* the intersection is $\{0\}$ because the only vector orthogonal to itself is zero.
   - *Why needed:* completes the direct-sum claim.

---

# Lemma Decomposition

> [!note]- Lemma 1: $U \cap U^\perp = \{0\}$
> **Statement:** For any subspace $U$ of an inner product space, $U \cap U^\perp = \{0\}$.
>
> **Hint:** If $u \in U \cap U^\perp$, then $u \perp u$, hence $\langle u, u\rangle = 0$, hence $u = 0$ by definiteness.
>
> **Why needed:** This is the cornerstone of uniqueness in the orthogonal decomposition.
>
> > [!note]- Full proof
> > Suppose $u \in U \cap U^\perp$. Since $u \in U^\perp$ and $u \in U$, we have $\langle u, u\rangle = 0$. By definiteness of the inner product, $u = 0$.

> [!note]- Lemma 2: Existence — the candidate decomposition works
> **Statement:** Let $e_1, \dots, e_m$ be an orthonormal basis of $U$. For $v \in V$, set $u = \sum_k \langle v, e_k\rangle e_k$ and $w = v - u$. Then $u \in U$, $w \in U^\perp$, and $v = u + w$.
>
> **Hint:** $u$ is a linear combination of the $e_k$'s. Compute $\langle w, e_l\rangle$ for each $l$ and verify it equals $0$.
>
> **Why needed:** This is the existence half — the explicit construction of the orthogonal decomposition.
>
> > [!note]- Full proof
> > By construction, $u = \sum_k \langle v, e_k\rangle e_k \in U$, and $v = u + w$ trivially.
> >
> > To show $w \in U^\perp$, we verify $\langle w, e_l\rangle = 0$ for each $l \in \{1, \dots, m\}$ (then by linearity $w$ is orthogonal to all of $U = \operatorname{span}(e_1, \dots, e_m)$):
> > $$\langle w, e_l\rangle = \left\langle v - \sum_k \langle v, e_k\rangle e_k, e_l\right\rangle = \langle v, e_l\rangle - \sum_k \langle v, e_k\rangle \langle e_k, e_l\rangle = \langle v, e_l\rangle - \langle v, e_l\rangle = 0,$$
> > using orthonormality ($\langle e_k, e_l\rangle = \delta_{kl}$, so only the $k = l$ term survives).

> [!note]- Lemma 3: Uniqueness — the decomposition is unique
> **Statement:** If $v = u_1 + w_1 = u_2 + w_2$ with $u_1, u_2 \in U$ and $w_1, w_2 \in U^\perp$, then $u_1 = u_2$ and $w_1 = w_2$.
>
> **Hint:** Subtract the two decompositions and use $U \cap U^\perp = \{0\}$.
>
> **Why needed:** This makes the decomposition unambiguous — and hence the orthogonal projection well-defined.
>
> > [!note]- Full proof
> > From $u_1 + w_1 = u_2 + w_2$, rearrange to $u_1 - u_2 = w_2 - w_1$. The left side $u_1 - u_2 \in U$ (a difference of elements of $U$); the right side $w_2 - w_1 \in U^\perp$ (a difference of elements of $U^\perp$). Hence both equal an element of $U \cap U^\perp = \{0\}$. So $u_1 = u_2$ and $w_1 = w_2$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $V$ be an inner product space and $U$ a finite-dimensional subspace. Then $V = U \oplus U^\perp$.
>
> *Proof.* **Existence ($V = U + U^\perp$):** Let $e_1, \dots, e_m$ be an orthonormal basis of $U$ (existing by [[Thm - Gram-Schmidt Procedure|Gram-Schmidt]] applied to any basis of $U$). For any $v \in V$, by Lemma 2, $v = u + w$ with $u = \sum_k \langle v, e_k\rangle e_k \in U$ and $w = v - u \in U^\perp$.
>
> **Uniqueness:** By Lemma 3, the decomposition is unique. Equivalently, $U \cap U^\perp = \{0\}$ by Lemma 1.
>
> Combining existence and uniqueness, $V = U \oplus U^\perp$. $\qquad\blacksquare$
>
> **Corollary (dimension formula).** $\dim U + \dim U^\perp = \dim V$ when $V$ is finite-dimensional.
>
> *Proof.* The dimension of a direct sum is the sum of dimensions.
>
> **Corollary (double-perp).** $(U^\perp)^\perp = U$ for $U$ finite-dimensional.
>
> *Proof.* The inclusion $U \subseteq (U^\perp)^\perp$ is immediate from the definitions: every $u \in U$ is orthogonal to every $w \in U^\perp$, hence $u \in (U^\perp)^\perp$.
>
> Conversely, suppose $v \in (U^\perp)^\perp$. Decompose $v = u + w$ with $u \in U$ and $w \in U^\perp$ (orthogonal decomposition applied to $U$). Then $v - u = w \in U^\perp$. But $v \in (U^\perp)^\perp$ and $u \in U \subseteq (U^\perp)^\perp$, so $v - u \in (U^\perp)^\perp$. Hence $v - u = w \in U^\perp \cap (U^\perp)^\perp = \{0\}$ (by Lemma 1 applied to $U^\perp$). So $v = u \in U$.
>
> Together, $(U^\perp)^\perp = U$.
>
> **Corollary ($U^\perp = \{0\} \iff U = V$).** For finite-dimensional $U$, $U^\perp = \{0\}$ iff $U = V$.
>
> *Proof.* If $U = V$, then $V^\perp = \{0\}$ trivially. Conversely, if $U^\perp = \{0\}$, then by the dimension formula $\dim U = \dim V$, and $U \subseteq V$ with equal dimensions forces $U = V$.

---

# Cross-Field Exercise Suggestions

**Fundamental Theorem of Linear Algebra (in inner-product form).** For $T \in \mathcal{L}(V, W)$ between finite-dimensional inner product spaces, the four fundamental subspaces are $\ker T \subseteq V$, $\operatorname{range} T \subseteq W$, $(\ker T)^\perp \subseteq V$, and $(\operatorname{range} T)^\perp \subseteq W$. The orthogonal decomposition gives $V = \ker T \oplus (\ker T)^\perp$ and $W = \operatorname{range} T \oplus (\operatorname{range} T)^\perp$. Moreover, $(\ker T)^\perp = \operatorname{range} T^*$ and $(\operatorname{range} T)^\perp = \ker T^*$ (where $T^*$ is the adjoint). The four-subspace picture is the orthogonal-decomposition view of the rank-nullity theorem, and it underlies the SVD.

**Probability: $L^2$ decomposition along a $\sigma$-subalgebra.** Given a probability space $(\Omega, \mathcal{F}, P)$ and a sub-$\sigma$-algebra $\mathcal{G} \subseteq \mathcal{F}$, the space $L^2(\mathcal{G}) \subseteq L^2(\mathcal{F})$ is a closed subspace, and $L^2(\mathcal{F}) = L^2(\mathcal{G}) \oplus L^2(\mathcal{G})^\perp$. The orthogonal projection of $X \in L^2(\mathcal{F})$ onto $L^2(\mathcal{G})$ is the **conditional expectation** $E[X|\mathcal{G}]$. The orthogonal-decomposition framework is the cleanest way to define and manipulate conditional expectations: $X = E[X|\mathcal{G}] + (X - E[X|\mathcal{G}])$, with the residual having mean zero on $\mathcal{G}$-measurable sets (the "innovation").

**PDE theory: weak solutions and orthogonality conditions.** In the weak formulation of $-\Delta u = f$ on $\Omega$ with $u = 0$ on $\partial\Omega$, the solution lives in the Hilbert space $H_0^1(\Omega)$. A solvability condition is that $\int f\, \phi$ vanishes for every $\phi$ in the kernel of $-\Delta$ (which is $\{0\}$ for the Dirichlet problem, but nontrivial for the Neumann problem). This solvability condition is the orthogonal-decomposition statement: $f$ must lie in the orthogonal complement of the kernel of the dual operator, i.e., in the range of $-\Delta$. The **Fredholm alternative** is this orthogonal-decomposition theorem applied to compact operators.

---

# Bridges

- **[[Def - Orthogonal Projection|Orthogonal Projection]]** — the orthogonal decomposition is the existence statement that makes orthogonal projection well-defined. Without $V = U \oplus U^\perp$, the operator $P_U v = u$ would not be uniquely defined. The decomposition gives existence; the uniqueness gives well-definedness of $P_U$.

- **[[Thm - Best Approximation by Orthogonal Projection|Best Approximation Theorem]]** — best approximation is the immediate corollary of orthogonal decomposition applied to $v - u'$ for $u' \in U$. The decomposition $v - u' = (v - P_U v) + (P_U v - u')$ is orthogonal, so Pythagoras gives $\|v - u'\|^2 \geq \|v - P_U v\|^2$ with equality iff $u' = P_U v$.

- **Hilbert Projection Theorem** *(Functional Analysis)* — in a Hilbert space, the orthogonal decomposition $V = U \oplus U^\perp$ holds for **closed** subspaces $U$ (not just finite-dimensional ones). The proof uses the existence of a closest point in $U$ to any $v \in V$ (by a compactness argument or by Bessel-style construction with an orthonormal basis of $U$). More generally, the **Hilbert projection theorem** extends from closed subspaces to closed convex subsets: every $v$ has a unique closest point in any closed convex subset of a Hilbert space.

- **Fundamental Theorem of Linear Algebra** *(Linear Algebra III)* — the orthogonal decomposition combined with adjoints gives the four-subspace decomposition: $V = \ker T \oplus \operatorname{range} T^*$ and $W = \operatorname{range} T \oplus \ker T^*$. This is the inner-product-space refinement of the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]], and it is the algebraic content of the **singular value decomposition**.

- **Fredholm Alternative** *(Operator Theory)* — for a compact operator $K$ on a Hilbert space, the orthogonal-decomposition framework gives the **Fredholm alternative**: $(I - K)v = f$ is solvable for $v$ if and only if $f$ is orthogonal to $\ker(I - K^*)$. This is the infinite-dimensional analog of $V = \ker T \oplus (\ker T)^\perp$ for an operator $T$ that fails to be invertible only in a "compact" way. Fredholm theory is the workhorse of elliptic-PDE existence proofs.
