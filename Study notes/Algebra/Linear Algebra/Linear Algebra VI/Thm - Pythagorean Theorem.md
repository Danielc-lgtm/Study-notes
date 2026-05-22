---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Orthogonal and Orthonormal Vectors"
  - "Def - Norm Induced by an Inner Product"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. Orthogonality is $u \perp v \iff \langle u, v\rangle = 0$. The notation registry is on the parent topic page [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Pythagorean Theorem).** Let $V$ be an inner product space. If $u, v \in V$ are orthogonal, then
> $$\|u + v\|^2 = \|u\|^2 + \|v\|^2.$$

> **Corollary (Pythagoras for an orthonormal list).** If $e_1, \dots, e_m$ is an orthonormal list and $a_1, \dots, a_m \in \mathbf{F}$, then
> $$\|a_1 e_1 + \cdots + a_m e_m\|^2 = |a_1|^2 + \cdots + |a_m|^2.$$

The corollary is the iterated form of the theorem, applied to mutually orthogonal vectors $a_1 e_1, \dots, a_m e_m$.

---

# Motivation

The Pythagorean theorem is the most fundamental geometric statement in inner product spaces, and it is the theorem that licenses the use of "Pythagoras" as a structural identity throughout the chapter. It says that the squared length of the hypotenuse of a right triangle equals the sum of the squared lengths of the legs — and this Euclidean fact, originally about right triangles in the plane, extends to **any** inner product space, no matter how exotic.

What makes the theorem genuinely powerful is its corollary: in an orthonormal basis (or orthonormal list), squared norms decompose as **sums of squared coordinates**. This is what makes orthonormal bases the computational gold standard: every norm-squared computation reduces to summing the absolute values of expansion coefficients, with no cross-terms to worry about. Parseval's identity, Bessel's inequality, the orthogonal-projection minimization theorem — all of these are downstream applications of the Pythagorean theorem applied to specific orthogonal decompositions.

The Pythagorean theorem is also the bedrock of the **orthogonal-decomposition view** of an inner product space. When $V = U \oplus U^\perp$ and $v = u + w$ with $u \in U$ and $w \in U^\perp$, the decomposition is orthogonal, so $\|v\|^2 = \|u\|^2 + \|w\|^2$. The norm decomposes additively along the orthogonal direct sum, just as the squared lengths of perpendicular legs sum to the squared hypotenuse. This is what makes "orthogonality controls norms" the operational reason every inner-product-space estimate works.

Among the chapter's results, the Pythagorean theorem is the *simplest* — its proof is two lines — yet also one of the most-used. Most computations in the chapter exploit its corollary on orthonormal lists, often without explicit mention. The chain "Cauchy-Schwarz → triangle inequality → best approximation → Bessel → Parseval" routes through Pythagoras at every step.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is that two vectors are orthogonal, $\langle u, v\rangle = 0$. The skill is recognising orthogonality in disguise.

The first source is **an orthogonal decomposition $v = u + w$ with $u \in U, w \in U^\perp$**. Property $B$: $u$ and $w$ are explicitly orthogonal because $w \in U^\perp$ and $u \in U$, so $\langle u, w\rangle = 0$. Bridge: Pythagoras gives $\|v\|^2 = \|u\|^2 + \|w\|^2$ for free, without any further computation. This is the source behind every result that uses "$v - P_U v \in U^\perp$ and $P_U v \in U$" to bound the residual.

The second source is **an orthonormal list and a linear combination of its members**. Property $B$: $a_j e_j$ and $a_k e_k$ are orthogonal for $j \neq k$ because the $e_k$'s are pairwise orthogonal. Bridge: iterated Pythagoras gives $\|\sum_k a_k e_k\|^2 = \sum_k |a_k|^2$. This is the "Parseval-style" formula behind every expansion-coefficient computation.

The third source is **the residual of an orthogonal projection**. Property $B$: for any $v \in V$ and finite-dimensional subspace $U$, the vector $v - P_U v$ is in $U^\perp$ (by the defining property of orthogonal projection), and $P_U v - u \in U$ for any $u \in U$. So $(v - P_U v)$ and $(P_U v - u)$ are orthogonal. Bridge: Pythagoras gives $\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2 \geq \|v - P_U v\|^2$ — the best-approximation theorem.

The fourth source is **a Cauchy-Schwarz equality case**. Property $B$: when $|\langle u, v\rangle| = \|u\|\,\|v\|$, the residual $u - (\langle u, v\rangle / \|v\|^2)v$ has zero norm — i.e., the orthogonal-projection construction collapses to "$u$ is on the line through $v$". Bridge: Pythagoras applied to $u = t^* v + 0$ verifies the structural picture.

**Targets (Output Amplification)**

The conclusion is $\|u + v\|^2 = \|u\|^2 + \|v\|^2$ for orthogonal $u, v$.

The first target is **Parseval's identity** $\|v\|^2 = \sum_k |\langle v, e_k\rangle|^2$ in an orthonormal basis. Property $D$: expand $v = \sum_k \langle v, e_k\rangle e_k$ and apply the iterated Pythagorean theorem. Combination: gives the squared-norm formula for any vector in terms of its expansion coefficients — the foundational identity for inner-product computations in orthonormal bases.

The second target is **Bessel's inequality** $\sum_k |\langle v, e_k\rangle|^2 \leq \|v\|^2$ for an orthonormal list (not a basis). Property $D$: write $v = \sum_k \langle v, e_k\rangle e_k + w$ where $w \perp$ each $e_k$. Combination: Pythagoras gives $\|v\|^2 = \sum_k |\langle v, e_k\rangle|^2 + \|w\|^2 \geq \sum_k |\langle v, e_k\rangle|^2$. Bessel's inequality is the engine of Fourier-coefficient convergence in $L^2$.

The third target is the **best-approximation theorem**. Property $D$: for any $u \in U$, write $v - u = (v - P_U v) + (P_U v - u)$ — an orthogonal decomposition. Combination: Pythagoras gives $\|v - u\|^2 = \|v - P_U v\|^2 + \|P_U v - u\|^2 \geq \|v - P_U v\|^2$, with equality iff $u = P_U v$. The Pythagorean theorem is the engine of orthogonal-projection minimization.

The fourth target is the **Cauchy-Schwarz inequality** via the orthogonal-projection picture. Property $D$: write $u = t^* v + w$ with $w \perp v$ where $t^* = \langle u, v\rangle / \|v\|^2$. Combination: Pythagoras gives $\|u\|^2 = |t^*|^2 \|v\|^2 + \|w\|^2 \geq |t^*|^2 \|v\|^2 = |\langle u, v\rangle|^2 / \|v\|^2$, hence $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. The Pythagorean theorem is the *geometric* engine behind Cauchy-Schwarz.

---

# Why Is It True

The intuition is the algebraic identity behind the inner-product expansion of $\|u + v\|^2$, with the cross-term killed by orthogonality.

Expanding $\|u + v\|^2 = \langle u + v, u + v\rangle$ via sesquilinearity:
$$
\|u + v\|^2 = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.
$$
When $\langle u, v\rangle = 0$, the cross-term vanishes:
$$
\|u + v\|^2 = \|u\|^2 + \|v\|^2.
$$
**The one-liner mechanism: orthogonality $\langle u, v\rangle = 0$ kills the cross-term $2\operatorname{Re}\langle u, v\rangle$ in the expansion of $\|u + v\|^2$, leaving only the diagonal $\|u\|^2 + \|v\|^2$.**

Geometrically, this is the classical Pythagorean theorem: if you walk distance $\|u\|$ in one direction, then distance $\|v\|$ in a perpendicular direction, your total displacement has length $\sqrt{\|u\|^2 + \|v\|^2}$. The proof in inner product spaces is a one-line algebraic identity; the proof in Euclidean geometry takes more work (classical proofs use area arguments or similar triangles). The algebraic version is the cleanest, because the inner product packages "perpendicular" and "length" into one operation, and the cross-term cancellation falls out automatically.

The iterated form for orthonormal lists is the same idea applied to many pairs at once: in $\|\sum a_k e_k\|^2 = \sum_{j, k} a_j \bar a_k \langle e_j, e_k\rangle$, all cross-terms ($j \neq k$) vanish because $\langle e_j, e_k\rangle = 0$, and the diagonal $j = k$ terms give $|a_k|^2 \langle e_k, e_k\rangle = |a_k|^2$. So the sum collapses to $\sum |a_k|^2$ — pure squared coordinates, no interactions.

This is the precise sense in which orthogonality controls norms: **orthogonal vectors do not interfere when you square the norm**. The cross-term that would carry the interaction is forced to zero by the orthogonality hypothesis.

---

# What Makes This Hard

The proof is two lines. The genuinely subtle point is recognising the *role* of the Pythagorean theorem in more complex arguments, especially when it appears multiple times within a single proof (as in the proof of the best-approximation theorem). A common mistake is to attempt to prove "$\|v - u\|^2 \geq \|v - P_U v\|^2$" by direct manipulation rather than recognising that $v - u = (v - P_U v) + (P_U v - u)$ is an orthogonal decomposition (so Pythagoras gives the inequality immediately). The skill is identifying when a decomposition is orthogonal and applying Pythagoras at that point.

A second subtlety is the complex case: the cross-term is $\langle u, v\rangle + \langle v, u\rangle = 2\operatorname{Re}\langle u, v\rangle$, not $2\langle u, v\rangle$. Orthogonality $\langle u, v\rangle = 0$ forces both terms to vanish, so the Pythagorean theorem holds; but if you only have $\operatorname{Re}\langle u, v\rangle = 0$ (a strictly weaker condition over $\mathbb{C}$), the conclusion still holds in the same form. This is a useful refinement: over $\mathbb{C}$, "real-orthogonal" suffices for Pythagoras at the norm level.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Expand $\|u + v\|^2$ using sesquilinearity; the orthogonality $\langle u, v\rangle = 0$ kills the cross-term.

**Subgoal decomposition:**

1. **Expand $\|u + v\|^2$.** Compute $\|u + v\|^2 = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2$.
   - *Hint:* sesquilinear expansion of $\langle u + v, u + v\rangle$; the cross-terms come from the two off-diagonal contributions.
   - *Why needed:* gives the expanded form to which orthogonality applies.

2. **Apply orthogonality.** Set $\langle u, v\rangle = 0$ and (by conjugate symmetry) $\langle v, u\rangle = \overline{\langle u, v\rangle} = 0$.
   - *Hint:* this is the hypothesis.
   - *Why needed:* zeros the cross-term.

3. **Conclude.** Read off $\|u + v\|^2 = \|u\|^2 + \|v\|^2$.
   - *Hint:* arithmetic.
   - *Why needed:* this is the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Expansion of $\|u + v\|^2$ via sesquilinearity
> **Statement:** For $u, v$ in an inner product space, $\|u + v\|^2 = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.
>
> **Hint:** Expand $\langle u + v, u + v\rangle$ using additivity in both slots; use conjugate symmetry to identify $\langle v, u\rangle = \overline{\langle u, v\rangle}$.
>
> **Why needed:** The expansion is the algebraic identity at the heart of the Pythagorean theorem; orthogonality is applied to it to kill the cross-term.
>
> > [!note]- Full proof
> > By additivity in the first slot, $\langle u + v, u + v\rangle = \langle u, u + v\rangle + \langle v, u + v\rangle$. By additivity in the second slot (which follows from additivity in the first slot and conjugate symmetry), each of these expands further: $\langle u, u + v\rangle = \langle u, u\rangle + \langle u, v\rangle$, and $\langle v, u + v\rangle = \langle v, u\rangle + \langle v, v\rangle$. Hence
> > $$\|u + v\|^2 = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2.$$
> > By conjugate symmetry, $\langle v, u\rangle = \overline{\langle u, v\rangle}$, so $\langle u, v\rangle + \langle v, u\rangle = \langle u, v\rangle + \overline{\langle u, v\rangle} = 2\operatorname{Re}\langle u, v\rangle$. Hence $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** If $u, v$ in an inner product space are orthogonal ($\langle u, v\rangle = 0$), then $\|u + v\|^2 = \|u\|^2 + \|v\|^2$.
>
> *Proof.* By Lemma 1,
> $$\|u + v\|^2 = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2.$$
> By hypothesis $\langle u, v\rangle = 0$, and by conjugate symmetry $\langle v, u\rangle = \overline{0} = 0$. Hence $\|u + v\|^2 = \|u\|^2 + \|v\|^2$. $\qquad\blacksquare$
>
> **Corollary (orthonormal list).** If $e_1, \dots, e_m$ is orthonormal and $a_1, \dots, a_m \in \mathbf{F}$, then $\|\sum_k a_k e_k\|^2 = \sum_k |a_k|^2$.
>
> *Proof.* The vectors $a_1 e_1, a_2 e_2, \dots, a_m e_m$ are pairwise orthogonal: $\langle a_j e_j, a_k e_k\rangle = a_j \bar a_k \langle e_j, e_k\rangle = a_j \bar a_k \cdot 0 = 0$ for $j \neq k$. By iterated Pythagoras (induction on $m$, using the binary case at each step), $\|\sum_k a_k e_k\|^2 = \sum_k \|a_k e_k\|^2 = \sum_k |a_k|^2 \|e_k\|^2 = \sum_k |a_k|^2$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Geometry: classical right triangles.** In a right triangle with legs of length $a, b$ and hypotenuse $c$, $c^2 = a^2 + b^2$. This is the original Pythagorean theorem, recovered by setting $V = \mathbb{R}^2$ with the dot product, $u = (a, 0)$ (one leg), $v = (0, b)$ (the other leg, perpendicular), and noting $u \perp v$ and $u + v = (a, b)$ is the hypotenuse.

**Probability: variance of independent random variables.** For uncorrelated random variables $X, Y$ (in particular, independent), $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$. This is the Pythagorean theorem on the inner-product space of mean-zero finite-variance random variables: "uncorrelated" means $\operatorname{Cov}(X, Y) = 0$, which is the orthogonality hypothesis. The variance is the squared norm. So "uncorrelated $\Rightarrow$ variances add" is Pythagoras in disguise.

**Signal processing: power of orthogonal signal components.** A signal $s(t)$ decomposed as a sum of orthogonal frequency components $s = \sum_k s_k$ (e.g., distinct Fourier modes) has total power (squared $L^2$-norm) equal to the sum of powers: $\|s\|^2 = \sum_k \|s_k\|^2$. This is the **Parseval/Plancherel identity** for Fourier components, an immediate consequence of the Pythagorean theorem for orthonormal lists.

**Quantum mechanics: probability conservation in measurement.** A pure state $|\psi\rangle$ expanded in the orthonormal eigenbasis of an observable, $|\psi\rangle = \sum_k c_k |e_k\rangle$, has $\sum_k |c_k|^2 = \|\psi\|^2 = 1$ (assuming normalized state). The squared coefficients $|c_k|^2$ are the probabilities of measurement outcomes, and their summing to $1$ is the Pythagorean-theorem statement for the orthonormal expansion. So "probabilities of measurement outcomes sum to $1$" is, structurally, Parseval's identity, hence the Pythagorean theorem.

---

# Bridges

- **[[Thm - Parallelogram Law|Parallelogram Law]]** — the parallelogram law generalises the Pythagorean theorem to non-orthogonal pairs, with a correction term. Specifically, $\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2)$ is the algebraic identity that holds without any orthogonality assumption; setting $\langle u, v\rangle = 0$ (orthogonality) and noting that both $\|u + v\|^2$ and $\|u - v\|^2$ equal $\|u\|^2 + \|v\|^2$ recovers Pythagoras as a degenerate case.

- **[[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz Inequality]]** — Cauchy-Schwarz uses Pythagoras as a step in the orthogonal-projection-based proof: $u = (\langle u, v\rangle/\|v\|^2) v + w$ with $w \perp v$, so $\|u\|^2 = |\langle u, v\rangle|^2/\|v\|^2 + \|w\|^2 \geq |\langle u, v\rangle|^2/\|v\|^2$ by Pythagoras. The Cauchy-Schwarz inequality is therefore Pythagoras applied to a specific orthogonal decomposition, with the inequality coming from $\|w\|^2 \geq 0$.

- **Parseval's identity and Bessel's inequality** *(internal)* — these are the iterated forms of the Pythagorean theorem for orthonormal lists: Parseval is the equality form for orthonormal bases, Bessel is the inequality form for orthonormal lists that may not span. Both follow from one-line applications of the corollary "$\|\sum a_k e_k\|^2 = \sum |a_k|^2$".

- **The "law of large numbers" in random-variable inner product spaces** *(Probability)* — for i.i.d. mean-zero random variables $X_1, X_2, \dots$ with finite variance $\sigma^2$, $\operatorname{Var}\bigl(\tfrac{1}{n}\sum X_k\bigr) = \tfrac{\sigma^2}{n}$ — the variance of the average shrinks like $1/n$. The Pythagorean theorem (applied to the $L^2$-orthogonal random variables) gives $\operatorname{Var}(\sum X_k) = n\sigma^2$, then dividing by $n^2$ to normalize gives $\sigma^2/n$. This is the bedrock variance-shrinkage of the weak law of large numbers, and it is Pythagoras applied to uncorrelated random variables.

- **Bias-variance decomposition** *(Statistics and Machine Learning)* — for an estimator $\hat\theta$ of a parameter $\theta$, $E[(\hat\theta - \theta)^2] = (E[\hat\theta] - \theta)^2 + \operatorname{Var}(\hat\theta)$ — the mean-squared error decomposes as bias-squared plus variance. This is the Pythagorean theorem in the inner-product space of $L^2$ random variables, applied to the orthogonal decomposition $\hat\theta - \theta = (E[\hat\theta] - \theta) + (\hat\theta - E[\hat\theta])$. The two summands are orthogonal in $L^2$ because the second has mean zero, so $E[(E[\hat\theta] - \theta)(\hat\theta - E[\hat\theta])] = (E[\hat\theta] - \theta) E[\hat\theta - E[\hat\theta]] = 0$.
