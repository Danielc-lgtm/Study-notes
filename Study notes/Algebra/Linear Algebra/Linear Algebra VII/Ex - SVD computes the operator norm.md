---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Singular Value Decomposition"
  - "Def - Singular Values"
  - "Def - Adjoint of a Linear Map"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ and $W$ be finite-dimensional inner product spaces and $T \in \mathcal{L}(V, W)$ a linear map. The **operator norm** of $T$ is

$$\|T\|_{\text{op}} = \sup_{v \in V, \|v\| = 1} \|Tv\| = \sup_{v \in V, v \neq 0} \frac{\|Tv\|}{\|v\|}.$$

Show that $\|T\|_{\text{op}} = s_1(T)$, the largest singular value of $T$.

**Recall:**

![[Def - Singular Values#The Definition]]

The [[Thm - Singular Value Decomposition|singular value decomposition]] gives orthonormal bases $\{e_j\}$ of $V$ and $\{f_j\}$ of (a [[Def - Subspace|subspace]] of) $W$, and non-negative real numbers $s_1 \geq s_2 \geq \cdots \geq s_n \geq 0$, such that $T e_j = s_j f_j$ for each $j$.

---

# Convergent Strategy

**Problem class.** This is a *computation* problem dressed as a verification: express the operator norm (defined as a supremum) in terms of an explicit invariant (the largest singular value). The class is: convert a definition-as-supremum into a definition-as-spectral-data, using the SVD to access the spectral structure of the operator.

**Assumption pattern.** The hypothesis is that $T$ admits an SVD $T = U \Sigma V^*$ (which is automatic — see [[Thm - Singular Value Decomposition]]). The unit ball of $V$ is the source — vectors $v$ with $\|v\| = 1$ — and the operator norm is a maximum over this set.

**Theorem routing.** The route is to expand $v$ in the orthonormal right-singular basis $\{e_j\}$ of $V$, write $\|Tv\|^2$ as a weighted sum of squared singular values, and read off the maximum.

**Key decision point.** The non-obvious move is using the orthonormal eigenbasis of $T^* T$ (= the right-singular basis of $T$) as the coordinate system in which to do the supremum. In the standard basis, the supremum has no closed form; in the singular-value basis, it is immediate.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VII — §7 Operators on Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the SVD to access spectral data** — Decompose $T$ via $T = U \Sigma V^*$ to get orthonormal coordinates aligned with the operator.

2. **Use orthonormal coordinates to expand $\|Tv\|^2$** — In the singular-value basis, $\|Tv\|^2$ becomes a weighted sum of $|\alpha_j|^2$ with weights $s_j^2$.

3. **Bound a weighted sum by its largest weight** — A weighted sum $\sum c_j s_j^2$ with $\sum c_j = 1$ is bounded by $\max s_j^2$, with equality when the mass concentrates on the largest weight.

---

# Hints

> [!note]- Hint 1
> Use the singular value decomposition. There are orthonormal $\{e_j\}$ in $V$ such that $T e_j = s_j f_j$, with $f_j$ orthonormal in $W$. Express an arbitrary unit vector $v$ in this basis.

> [!note]- Hint 2
> Write $v = \sum_j \alpha_j e_j$. Compute $\|v\|^2$ and $\|T v\|^2$ in terms of the $\alpha_j$ and singular values $s_j$.

> [!note]- Hint 3
> $\|v\|^2 = \sum |\alpha_j|^2$ and $\|Tv\|^2 = \sum |\alpha_j|^2 s_j^2$ (using orthonormality of $\{f_j\}$). The constraint $\|v\|^2 = 1$ becomes $\sum |\alpha_j|^2 = 1$. Maximise $\sum |\alpha_j|^2 s_j^2$ subject to $\sum |\alpha_j|^2 = 1$, with $s_1 \geq s_2 \geq \cdots$.

---

# Solution

The proof has two parts: an upper bound $\|Tv\| \leq s_1 \|v\|$ for all $v$, and an explicit vector $v = e_1$ achieving this bound. Together they show the supremum equals $s_1$.

**Step 1: Expand $v$ in the right-singular orthonormal basis.**

Let $\{e_1, \ldots, e_n\}$ be the orthonormal basis of $V$ from the SVD, with $T e_j = s_j f_j$ and $s_1 \geq s_2 \geq \cdots \geq s_n \geq 0$. For any $v \in V$, write $v = \sum_j \alpha_j e_j$ with $\alpha_j = \langle v, e_j \rangle \in \mathbb{F}$.

By orthonormality of $\{e_j\}$, $\|v\|^2 = \sum_j |\alpha_j|^2$. So $\|v\| = 1$ iff $\sum |\alpha_j|^2 = 1$.

> [!note]- Derivation
> Any vector in $V$ is uniquely expressed in an orthonormal basis, and the Parseval identity gives $\|v\|^2 = \sum |\langle v, e_j \rangle|^2$ when the basis is orthonormal. Here $\alpha_j = \langle v, e_j \rangle$, so $\|v\|^2 = \sum |\alpha_j|^2$.

**Step 2: Compute $\|Tv\|^2$ in this basis.**

$$Tv = T \sum_j \alpha_j e_j = \sum_j \alpha_j T e_j = \sum_j \alpha_j s_j f_j.$$
By orthonormality of $\{f_j\}$,
$$\|Tv\|^2 = \left\|\sum_j \alpha_j s_j f_j \right\|^2 = \sum_j |\alpha_j|^2 s_j^2.$$

> [!note]- Derivation
> Linearity of $T$ gives $Tv = \sum \alpha_j T e_j = \sum \alpha_j s_j f_j$. Orthonormality of $\{f_j\}$ then gives $\|Tv\|^2 = \sum |\alpha_j s_j|^2 = \sum |\alpha_j|^2 |s_j|^2 = \sum |\alpha_j|^2 s_j^2$ (using $s_j \geq 0$).

**Step 3: Bound $\|Tv\|^2$ by $s_1^2 \|v\|^2$.**

Since $s_1 \geq s_j$ for all $j$, $s_j^2 \leq s_1^2$ for all $j$. Therefore
$$\|Tv\|^2 = \sum_j |\alpha_j|^2 s_j^2 \leq \sum_j |\alpha_j|^2 s_1^2 = s_1^2 \sum_j |\alpha_j|^2 = s_1^2 \|v\|^2.$$
Taking square roots, $\|Tv\| \leq s_1 \|v\|$, so $\|T\|_{\text{op}} \leq s_1$.

> [!note]- Derivation
> The inequality $s_j^2 \leq s_1^2$ uses the singular values being in decreasing order with $s_1$ the maximum. The weighted sum $\sum |\alpha_j|^2 s_j^2$ is bounded by the same sum with each $s_j^2$ replaced by $s_1^2$, which factors out as $s_1^2 \sum |\alpha_j|^2 = s_1^2 \|v\|^2$.

**Step 4: Show $\|T\|_{\text{op}} \geq s_1$ by exhibiting an extremal vector.**

Take $v = e_1$ (so $\alpha_1 = 1$ and all other $\alpha_j = 0$). Then $\|v\| = 1$, and $T e_1 = s_1 f_1$, so $\|Te_1\| = s_1 \|f_1\| = s_1$. Therefore $\|T\|_{\text{op}} \geq s_1$.

> [!note]- Derivation
> Direct: $v = e_1$ has norm $1$, and $T e_1 = s_1 f_1$ has norm $s_1$ since $f_1$ is a unit vector. So $\|T e_1\| / \|e_1\| = s_1$, which is a lower bound for the supremum $\|T\|_{\text{op}}$.

**Step 5: Conclude.**

Combining Steps 3 and 4: $s_1 \leq \|T\|_{\text{op}} \leq s_1$, so $\|T\|_{\text{op}} = s_1$. ✓

> [!note]- Complete formal solution
> By the SVD, there are orthonormal $\{e_j\}$ in $V$ and $\{f_j\}$ in $W$ such that $T e_j = s_j f_j$ for non-negative $s_1 \geq \cdots \geq s_n \geq 0$.
>
> **Upper bound.** For any $v = \sum_j \alpha_j e_j$ with $\|v\| = 1$ (i.e., $\sum |\alpha_j|^2 = 1$):
> $$\|Tv\|^2 = \left\|\sum_j \alpha_j s_j f_j\right\|^2 = \sum_j |\alpha_j|^2 s_j^2 \leq s_1^2 \sum_j |\alpha_j|^2 = s_1^2.$$
> So $\|Tv\| \leq s_1$.
>
> **Achieved at $v = e_1$.** $\|Te_1\| = \|s_1 f_1\| = s_1$.
>
> Therefore $\|T\|_{\text{op}} = \sup_{\|v\| = 1} \|Tv\| = s_1$. $\blacksquare$

> [!note]- Alternative route: use $\|T\|_{\text{op}}^2 = \|T^*T\|_{\text{op}}$
> An indirect route: the operator norm squared equals the operator norm of $T^*T$. For self-adjoint operators (and $T^*T$ is self-adjoint), the operator norm equals the largest eigenvalue. The largest eigenvalue of $T^*T$ is $s_1^2$, so $\|T\|_{\text{op}}^2 = s_1^2$, hence $\|T\|_{\text{op}} = s_1$. This route uses two facts: (i) $\|T\|_{\text{op}}^2 = \|T^*T\|_{\text{op}}$, and (ii) for self-adjoint operators, operator norm equals largest eigenvalue. The direct route via SVD is more transparent because it gives the extremal vector explicitly.

---

# Key Takeaways

**The largest singular value is the right operator-theoretic notion of "size".** The operator norm $\|T\|_{\text{op}}$ measures the maximum stretching factor of $T$ on the unit ball; the largest singular value $s_1$ is the length of the longest principal semi-axis of the image ellipsoid. These are the same quantity. For non-normal operators, $s_1$ is the right thing to use as "$|T|$" — *not* the largest eigenvalue of $T$, which can be much smaller. The matrix $\begin{pmatrix} 1 & 1000 \\ 0 & 1 \end{pmatrix}$ has eigenvalues $\{1, 1\}$ but $s_1 \approx 1000$, and $\|T\|_{\text{op}} \approx 1000$. The eigenvalues are misleading for the size of a non-normal operator; singular values are correct.

**SVD reduces every "extremum on the unit ball" problem to a singular-value computation.** The technique used here — expand in the right-singular basis, write the quantity of interest as a weighted sum of singular values — works for many extremum problems beyond operator norm. The smallest singular value $s_n$ gives the *minimum* of $\|Tv\|/\|v\|$ (for invertible $T$ — otherwise the minimum is $0$, attained on the kernel). The ratio $s_1/s_n$ is the **condition number**. The product $\prod s_j = |\det T|$ is the volume distortion. The sum $\sum s_j^2 = \|T\|_F^2$ is the Frobenius norm squared. Each invariant has a closed-form expression in terms of singular values.

**The extremal vector is the top right-singular vector $e_1$.** The vector achieving the operator-norm supremum is $e_1$, the right-singular vector for the largest singular value. This is the **dominant eigenvector** in the sense of the power iteration algorithm: iterating $v \mapsto T^* T v / \|T^* T v\|$ converges to $e_1$ generically, and the corresponding $\|Tv\|/\|v\|$ converges to $s_1$. This is the basis of the **power iteration** method for computing the top singular value (and the top eigenvector for symmetric matrices) without doing a full SVD — used in PageRank, in dominant eigenvector computations in chemistry and physics, and as the inner loop of more sophisticated iterative algorithms.
