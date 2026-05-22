---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Norm Induced by an Inner Product"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$. The norm $\|v\| = \sqrt{\langle v, v\rangle}$ is the inner-product norm. $\bar\lambda$ is the complex conjugate; $\operatorname{Re} z$ is the real part of $z \in \mathbb{C}$. The full notation registry lives on the parent page [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Cauchy-Schwarz Inequality).** Let $V$ be an inner product space over $\mathbf{F}$. For all $u, v \in V$,
> $$|\langle u, v\rangle| \leq \|u\|\,\|v\|.$$
> Equality holds if and only if one of $u, v$ is a scalar multiple of the other (allowing the scalar to be $0$, so the case $u = 0$ or $v = 0$ is automatically equality).

> **Corollary (Cauchy-Schwarz for sums).** For real numbers $a_1, \dots, a_n, b_1, \dots, b_n$,
> $$\left|\sum_{k=1}^n a_k b_k\right|^2 \leq \left(\sum_{k=1}^n a_k^2\right)\left(\sum_{k=1}^n b_k^2\right).$$

> **Corollary (Cauchy-Schwarz for integrals).** For continuous real-valued functions $f, g$ on $[a, b]$,
> $$\left|\int_a^b f(x) g(x)\, dx\right|^2 \leq \left(\int_a^b f(x)^2\, dx\right)\left(\int_a^b g(x)^2\, dx\right).$$

The two corollaries are the inequality applied to $(\mathbf{F}^n, \text{Euclidean})$ and $(C[a, b], L^2)$ respectively. They are the most-used forms in practice.

---

# Motivation

The Cauchy-Schwarz inequality is the most-used inequality in inner product spaces and arguably in all of analysis. It plays three foundational roles.

First, it **justifies the definition of angle** in inner product spaces of dimension $\geq 4$. The angle between two nonzero vectors $u, v$ is defined as $\theta = \arccos\bigl(\langle u, v\rangle / (\|u\|\,\|v\|)\bigr)$. For $\arccos$ to make sense, the argument must lie in $[-1, 1]$ — equivalently, $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. Without Cauchy-Schwarz, "the angle in $\mathbb{R}^n$ for $n \geq 4$" would be ill-defined. With Cauchy-Schwarz, the geometric intuition from $\mathbb{R}^2$ and $\mathbb{R}^3$ extends to all inner product spaces.

Second, it **proves the triangle inequality**. The triangle inequality $\|u + v\| \leq \|u\| + \|v\|$ is the geometric fact that makes the norm-induced metric a metric. Its proof routes through Cauchy-Schwarz: $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2 \leq \|u\|^2 + 2|\langle u, v\rangle| + \|v\|^2 \leq \|u\|^2 + 2\|u\|\,\|v\| + \|v\|^2 = (\|u\| + \|v\|)^2$. The middle step is exactly Cauchy-Schwarz. Without it, the inner product space is just a bilinear-form-on-a-vector-space; with it, it is a metric space.

Third, it is the **engine of correlation bounds** in statistics. The correlation coefficient $\rho(X, Y) = \operatorname{Cov}(X, Y) / (\sigma_X \sigma_Y)$ is the angle between mean-zero random variables. The statement $|\rho| \leq 1$ — that correlation lies between $-1$ and $+1$ — is exactly Cauchy-Schwarz applied to the inner product $\langle X, Y\rangle = E[XY]$ on the space of mean-zero finite-variance random variables. So Cauchy-Schwarz is the reason "correlation is bounded by $\pm 1$" in statistics.

The role of Cauchy-Schwarz across mathematics is that it converts a *bilinear* quantity $\langle u, v\rangle$ into a product of *unilinear* quantities $\|u\|, \|v\|$ — and unilinear quantities are easier to bound. This is the cleanest illustration of "trade joint information for marginal information" in mathematics, and it is what makes the inequality ubiquitous.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis Cauchy-Schwarz needs is bare: *any inner product space, any two vectors*. The skill is recognising that an unfamiliar quantity is an inner product in disguise.

The first source is **a sum $\sum_k a_k b_k$ of products**. Property $B$: the sum is the inner product $\langle (a_1, \dots, a_n), (b_1, \dots, b_n)\rangle$ in $\mathbb{R}^n$ with the Euclidean inner product. The bridge: Cauchy-Schwarz applies directly, giving $|\sum a_k b_k| \leq (\sum a_k^2)^{1/2}(\sum b_k^2)^{1/2}$ — a classical inequality known as **Cauchy's inequality** in nineteenth-century notation. This is the source behind almost every problem involving inequalities of finite sums.

The second source is **an integral $\int fg$ of a product**. Property $B$: the integral is $\langle f, g\rangle$ in the $L^2$ inner product space. The bridge: $|\int fg|^2 \leq \int f^2 \cdot \int g^2$ (or with absolute values to handle complex-valued or sign-changing functions). This is **Bunyakovsky's inequality** in its classical form (1859), and it is the source for integral inequalities throughout PDE analysis, signal processing, and probability theory.

The third source is **a covariance $E[(X - EX)(Y - EY)]$**. Property $B$: covariance is the inner product on mean-zero random variables. The bridge: $|\operatorname{Cov}(X, Y)| \leq \sigma_X \sigma_Y$, equivalently the correlation coefficient $|\rho(X, Y)| \leq 1$. This is the source for statistical bounds and the proof that "correlation is between $-1$ and $1$".

The fourth source is **a discrete sum with weights, $\sum_k c_k a_k b_k$ with $c_k > 0$**. Property $B$: this is the weighted inner product $\langle a, b\rangle = \sum c_k a_k b_k$ on $\mathbb{R}^n$. The bridge: Cauchy-Schwarz applies, giving inequalities like $|\sum c_k a_k b_k|^2 \leq (\sum c_k a_k^2)(\sum c_k b_k^2)$, often used in probability ($c_k = $ probabilities) and physics ($c_k = $ density weights).

A fifth, more disguised source is **a sum $\sum_k a_k / b_k$ of ratios** when each $b_k > 0$. Property $B$: write $a_k / b_k = (a_k / \sqrt{b_k}) \cdot (1 / \sqrt{b_k})$, then $\sum a_k / b_k = \langle (a_k/\sqrt{b_k})_k, (1/\sqrt{b_k})_k\rangle$. This is the source behind Cauchy-Schwarz applications like "$\sum (a_k^2 / b_k) \geq (\sum a_k)^2 / \sum b_k$", which is the **Titu's lemma** or **Engel form** of Cauchy-Schwarz, used extensively in mathematical-olympiad inequality problems.

**Targets (Output Amplification)**

The conclusion is $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. On its own, this bounds a single inner product. Combining with extra structure yields more.

The first target is **the triangle inequality $\|u + v\| \leq \|u\| + \|v\|$**. Property $D$: square both sides of the desired inequality. The combination: $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$; Cauchy-Schwarz gives $\operatorname{Re}\langle u, v\rangle \leq |\langle u, v\rangle| \leq \|u\|\,\|v\|$; therefore $\|u + v\|^2 \leq (\|u\| + \|v\|)^2$. The non-obvious part is squaring first — the bilinear/linear structure is only accessible at the squared level.

The second target is **the correlation bound $|\rho(X, Y)| \leq 1$** in statistics. Property $D$: dividing both sides of Cauchy-Schwarz by $\|u\|\,\|v\| = \sigma_X \sigma_Y$. The combination: $|\langle u, v\rangle| / (\|u\|\,\|v\|) \leq 1$, where the left-hand side is $|\rho|$. Useful because it bounds a normalised quantity (correlation, which depends on shape but not scale) by a constant ($1$).

The third target is **Bessel's inequality** $\sum_k |\langle v, e_k\rangle|^2 \leq \|v\|^2$ for any orthonormal list $e_1, \dots, e_m$. Property $D$: combine Cauchy-Schwarz with the orthogonal-projection decomposition. The combination: write $v = \sum_k \langle v, e_k\rangle e_k + w$ with $w$ orthogonal to the span, apply Pythagoras to get $\|v\|^2 = \sum |\langle v, e_k\rangle|^2 + \|w\|^2 \geq \sum |\langle v, e_k\rangle|^2$. Bessel's inequality is the infinite-dimensional foundation of Fourier-coefficient convergence and is itself a key Cauchy-Schwarz-derived bound.

The fourth target is the **angle definition $\theta = \arccos(\langle u, v\rangle/(\|u\|\,\|v\|))$** in $\mathbb{R}^n$ for $n \geq 4$. Property $D$: Cauchy-Schwarz forces the argument to lie in $[-1, 1]$, hence $\arccos$ is well-defined. The combination: a single use of $|\langle u, v\rangle| \leq \|u\|\,\|v\|$ provides the entire well-definedness, and the angle then satisfies all the Euclidean-geometry intuitions.

A fifth target is **the AM-QM inequality** in disguised forms. Property $D$: take $u = (1, 1, \dots, 1)$ and $v = (a_1, \dots, a_n)$ in $\mathbb{R}^n$. The combination: $|\sum a_k| \leq \sqrt{n} \cdot \sqrt{\sum a_k^2}$, which rearranges to $\bigl(\frac{\sum a_k}{n}\bigr)^2 \leq \frac{\sum a_k^2}{n}$ — the squared average is at most the average of squares. This is the same statement as $\operatorname{Var}(X) \geq 0$, and it appears in countless contexts.

---

# Why Is It True

The intuition behind Cauchy-Schwarz has a single clean form, and once you see it the inequality is unsurprising.

**The discriminant picture: $\|u - tv\|^2$ is a non-negative quadratic in $t$, so its discriminant is non-positive.**

Fix $u, v$ with $v \neq 0$, and consider the real-valued function $f(t) = \|u - tv\|^2$ as $t$ ranges over $\mathbb{R}$. Two things are clear: $f(t) \geq 0$ for all $t$ (norms are non-negative), and $f$ is a quadratic in $t$. Expanding,
$$
f(t) = \langle u - tv, u - tv\rangle = \|u\|^2 - t\,\overline{\langle u, v\rangle} - t\langle u, v\rangle + t^2\|v\|^2.
$$
Over $\mathbb{R}$, this is the *real* quadratic $f(t) = \|v\|^2 t^2 - 2\langle u, v\rangle t + \|u\|^2$. A non-negative real quadratic $At^2 + Bt + C$ with $A > 0$ has discriminant $B^2 - 4AC \leq 0$. Applied to $f$: $(2\langle u, v\rangle)^2 - 4 \|v\|^2 \|u\|^2 \leq 0$, which rearranges to $\langle u, v\rangle^2 \leq \|u\|^2 \|v\|^2$, hence $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. The complex case is similar with a careful choice of $t$.

**The one-liner mechanism: $\|u - tv\|^2 \geq 0$ for all real $t$ is a constraint strong enough to force Cauchy-Schwarz by minimising over $t$.**

The minimum of the quadratic $f(t)$ occurs at $t^* = \langle u, v\rangle / \|v\|^2$ (for the real case, or $t^* = \overline{\langle u, v\rangle} / \|v\|^2$ over $\mathbb{C}$); substituting back, $f(t^*) = \|u\|^2 - |\langle u, v\rangle|^2 / \|v\|^2$. This minimum is $\geq 0$, hence $|\langle u, v\rangle|^2 \leq \|u\|^2 \|v\|^2$. Equality $f(t^*) = 0$ corresponds to $u = t^* v$ — one vector is a scalar multiple of the other.

There is a beautiful **geometric interpretation** of $t^*$: the vector $t^* v$ is the orthogonal projection of $u$ onto the line through $v$. The residual $u - t^*v$ is what is left after projecting, and it is perpendicular to $v$. The Cauchy-Schwarz inequality is then the Pythagorean statement that the squared length of the projection is at most the squared length of $u$:
$$
\|u\|^2 = \|t^* v\|^2 + \|u - t^* v\|^2 \geq \|t^* v\|^2 = \frac{|\langle u, v\rangle|^2}{\|v\|^2}.
$$
This is the geometric reason Cauchy-Schwarz is true: **the length of the projection of $u$ onto a line is at most the length of $u$ itself**. Equality holds when $u$ lies entirely on the line — i.e., when $u$ is a scalar multiple of $v$.

A second perspective: the Cauchy-Schwarz inequality is **the special case of Bessel's inequality with a single orthonormal vector**. Take the orthonormal list to be just $e_1 = v/\|v\|$. Then Bessel's inequality says $|\langle u, e_1\rangle|^2 \leq \|u\|^2$, which unpacks to $|\langle u, v/\|v\|\rangle|^2 = |\langle u, v\rangle|^2/\|v\|^2 \leq \|u\|^2$, the Cauchy-Schwarz inequality. From this perspective, Cauchy-Schwarz is the simplest case of "the truncated orthonormal expansion has smaller norm than the full vector".

---

# What Makes This Hard

The proof is one line once you have the discriminant trick, but the *discovery* of the discriminant trick is non-obvious if you have not seen it. The most common error in attempted proofs is to try to bound $|\langle u, v\rangle|$ directly using the bilinear-form axioms, which gives nothing — the axioms are linear, the inequality is quadratic, and the gap must be bridged by squaring. The non-obvious step is to introduce the **auxiliary parameter $t$** and minimise over it; this converts a fixed-vector problem ("bound this inner product") into an optimisation problem ("find the $t$ minimising $\|u - tv\|^2$"). A second common error, specific to the complex case, is to forget conjugates in expanding $\|u - tv\|^2$ — the cross-terms over $\mathbb{C}$ involve $\overline{\langle u, v\rangle}$, and treating them as $\langle u, v\rangle$ silently produces wrong answers.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Consider the real-valued function $t \mapsto \|u - tv\|^2$. It is a non-negative quadratic in $t$, so its discriminant is non-positive, and that is exactly the Cauchy-Schwarz inequality.

**Subgoal decomposition:**

1. **Reduce to the case $v \neq 0$.**
   - *Hint:* if $v = 0$, both sides of $|\langle u, v\rangle| \leq \|u\|\,\|v\|$ are $0$, so the inequality is trivial.
   - *Why needed:* clears the denominator in the subsequent calculation.

2. **Set up the quadratic.** For each $t \in \mathbb{R}$ (in the real case) or $t \in \mathbf{F}$ (in the general case), compute $\|u - tv\|^2$ as a function of $t$.
   - *Hint:* expand $\langle u - tv, u - tv\rangle$ using sesquilinearity, getting a polynomial in $t$ and $\bar t$ (which simplifies in the real case to a quadratic in $t$).
   - *Why needed:* turns the inequality (about fixed vectors) into a quadratic-discriminant statement (one that the elementary algebra of polynomials can handle).

3. **Minimize the quadratic.** Compute the value of $t$ that minimises $\|u - tv\|^2$.
   - *Hint:* take the derivative with respect to $t$ (real case), or write $t = \langle u, v\rangle/\|v\|^2$ and verify the choice is optimal.
   - *Why needed:* the minimal value is the strongest constraint that $\|u - tv\|^2 \geq 0$ provides.

4. **Extract the inequality.** Setting the minimum value $\geq 0$ gives $\|u\|^2 - |\langle u, v\rangle|^2/\|v\|^2 \geq 0$, which rearranges to Cauchy-Schwarz.
   - *Hint:* algebraic manipulation only; no further insight required.
   - *Why needed:* this *is* the conclusion of the theorem.

5. **Track the equality case.** Equality in the discriminant condition corresponds to the minimum value being $0$, which means $u - t^* v = 0$ for the optimal $t^*$.
   - *Hint:* $u = t^* v$ says $u$ is a scalar multiple of $v$.
   - *Why needed:* completes the "if and only if" claim.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\|u - tv\|^2$ as a quadratic in $t$
> **Statement:** For $v \neq 0$ and any $t \in \mathbf{F}$,
> $$\|u - tv\|^2 = \|u\|^2 - t\overline{\langle u, v\rangle} - \bar t \langle u, v\rangle + |t|^2 \|v\|^2.$$
> Over $\mathbb{R}$ this simplifies to $\|u - tv\|^2 = \|v\|^2 t^2 - 2\langle u, v\rangle t + \|u\|^2$, a non-negative real quadratic in $t$.
>
> **Hint:** Expand $\langle u - tv, u - tv\rangle$ using additivity in both slots and linearity (first slot)/conjugate-linearity (second slot). Group terms.
>
> **Why needed:** This is the algebraic identity at the heart of the proof — without it there is no quadratic to minimise.
>
> > [!note]- Full proof
> > Expanding via sesquilinearity:
> > $$\langle u - tv, u - tv\rangle = \langle u, u\rangle + \langle u, -tv\rangle + \langle -tv, u\rangle + \langle -tv, -tv\rangle.$$
> > Using conjugate-linearity in the second slot, $\langle u, -tv\rangle = -\bar t\langle u, v\rangle$. Using linearity in the first slot, $\langle -tv, u\rangle = -t\langle v, u\rangle = -t \overline{\langle u, v\rangle}$. And $\langle -tv, -tv\rangle = |t|^2 \langle v, v\rangle = |t|^2 \|v\|^2$. So
> > $$\|u - tv\|^2 = \|u\|^2 - \bar t \langle u, v\rangle - t\overline{\langle u, v\rangle} + |t|^2 \|v\|^2.$$
> > Over $\mathbb{R}$, $\bar t = t$ and $\overline{\langle u, v\rangle} = \langle u, v\rangle$, so the cross-terms combine to $-2t\langle u, v\rangle$, giving the real-quadratic form. The result is $\geq 0$ for all $t$ because it is a squared norm.

> [!note]- Lemma 2: The optimal $t$ and the minimum value
> **Statement:** For $v \neq 0$, the function $t \mapsto \|u - tv\|^2$ over $\mathbf{F}$ has minimum at $t^* = \langle u, v\rangle / \|v\|^2$, and the minimum value is $\|u\|^2 - |\langle u, v\rangle|^2 / \|v\|^2$.
>
> **Hint:** Substitute $t = \langle u, v\rangle/\|v\|^2$ into the expansion from Lemma 1 and simplify. Verify it minimises by completing the square, or computing $d/dt$ in the real case.
>
> **Why needed:** The minimum value of a non-negative function is $\geq 0$; that inequality is Cauchy-Schwarz.
>
> > [!note]- Full proof
> > Substituting $t = \langle u, v\rangle / \|v\|^2$, so $\bar t = \overline{\langle u, v\rangle} / \|v\|^2$ (real $\|v\|^2$):
> > $$\|u - t^* v\|^2 = \|u\|^2 - \frac{\langle u, v\rangle \cdot \overline{\langle u, v\rangle}}{\|v\|^2} - \frac{\overline{\langle u, v\rangle} \cdot \langle u, v\rangle}{\|v\|^2} + \frac{|\langle u, v\rangle|^2}{\|v\|^4} \cdot \|v\|^2.$$
> > Using $\langle u, v\rangle \overline{\langle u, v\rangle} = |\langle u, v\rangle|^2$:
> > $$= \|u\|^2 - \frac{|\langle u, v\rangle|^2}{\|v\|^2} - \frac{|\langle u, v\rangle|^2}{\|v\|^2} + \frac{|\langle u, v\rangle|^2}{\|v\|^2} = \|u\|^2 - \frac{|\langle u, v\rangle|^2}{\|v\|^2}.$$
> > That this is the minimum follows from completing the square or differentiating in the real case. In the complex case, the same calculation applies with $\overline{\langle u, v\rangle}/\|v\|^2$ playing the role of $t$.

> [!note]- Lemma 3: Equality and the scalar-multiple condition
> **Statement:** Equality $|\langle u, v\rangle| = \|u\|\,\|v\|$ holds if and only if one of $u, v$ is a scalar multiple of the other.
>
> **Hint:** Equality in Cauchy-Schwarz forces $\|u - t^* v\|^2 = 0$, hence $u = t^* v$ — a scalar multiple. Trace the converse by direct calculation.
>
> **Why needed:** Completes the "if and only if" in the statement, characterising the equality case.
>
> > [!note]- Full proof
> > *($\Leftarrow$)* If $u = \alpha v$ for some $\alpha$, then $\langle u, v\rangle = \alpha \|v\|^2$, so $|\langle u, v\rangle| = |\alpha|\,\|v\|^2 = \|\alpha v\|\,\|v\| = \|u\|\,\|v\|$. Similarly if $v$ is a multiple of $u$. (The case $u = 0$ or $v = 0$ is included.)
> >
> > *($\Rightarrow$)* Suppose $|\langle u, v\rangle| = \|u\|\,\|v\|$. If $v = 0$ we are done. Otherwise, $\|u - t^* v\|^2 = \|u\|^2 - |\langle u, v\rangle|^2/\|v\|^2 = \|u\|^2 - \|u\|^2\|v\|^2/\|v\|^2 = 0$. The norm-zero condition forces $u - t^* v = 0$, i.e., $u = t^* v$ is a scalar multiple of $v$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For $u, v$ in an inner product space, $|\langle u, v\rangle| \leq \|u\|\,\|v\|$, with equality iff one vector is a scalar multiple of the other.
>
> *Proof.* If $v = 0$, both sides are $0$ and the inequality holds with equality (trivially). Assume $v \neq 0$.
>
> Set $t^* = \langle u, v\rangle / \|v\|^2 \in \mathbf{F}$ and consider the orthogonal decomposition (an instance of [[Thm - Orthogonal Decomposition|orthogonal decomposition]] applied to the one-dimensional subspace $\operatorname{span}(v)$):
> $$u = t^* v + w, \qquad \text{where } w = u - t^* v.$$
> By construction, $\langle w, v\rangle = \langle u, v\rangle - t^* \|v\|^2 = \langle u, v\rangle - \langle u, v\rangle = 0$, so $w \perp v$. The vectors $t^* v$ and $w$ are then orthogonal.
>
> By the [[Thm - Pythagorean Theorem|Pythagorean theorem]],
> $$\|u\|^2 = \|t^* v\|^2 + \|w\|^2 = |t^*|^2 \|v\|^2 + \|w\|^2 = \frac{|\langle u, v\rangle|^2}{\|v\|^2} + \|w\|^2.$$
> Since $\|w\|^2 \geq 0$,
> $$\|u\|^2 \geq \frac{|\langle u, v\rangle|^2}{\|v\|^2}.$$
> Multiplying both sides by $\|v\|^2$ and taking square roots gives $\|u\|\,\|v\| \geq |\langle u, v\rangle|$, as desired.
>
> **Equality case:** equality in the above holds if and only if $\|w\|^2 = 0$, i.e., $w = 0$, i.e., $u = t^* v$ is a scalar multiple of $v$. Conversely, if $u$ is a scalar multiple of $v$, direct calculation gives $|\langle u, v\rangle| = \|u\|\,\|v\|$. The symmetric case ($v$ a multiple of $u$, including $v = 0$) is handled by the trivial case above. $\qquad\blacksquare$

> [!note]- Alternative proof: the discriminant of $\|u - tv\|^2$
> *Proof.* Assume $v \neq 0$. The function $f : \mathbb{R} \to \mathbb{R}$ defined by $f(t) = \|u - tv\|^2$ is a non-negative real quadratic. Expanding (and taking the real part for the complex case),
> $$f(t) = \|v\|^2 t^2 - 2\operatorname{Re}\langle u, v\rangle\, t + \|u\|^2.$$
> A non-negative real quadratic $At^2 + Bt + C$ with $A > 0$ has discriminant $B^2 - 4AC \leq 0$. Applied here:
> $$4 (\operatorname{Re}\langle u, v\rangle)^2 - 4\|v\|^2 \|u\|^2 \leq 0,$$
> so $(\operatorname{Re}\langle u, v\rangle)^2 \leq \|u\|^2 \|v\|^2$.
>
> For the full inequality $|\langle u, v\rangle| \leq \|u\|\,\|v\|$ over $\mathbb{C}$, replace $v$ by $\bar\alpha v$ where $\alpha = \langle u, v\rangle/|\langle u, v\rangle|$ (so $|\alpha| = 1$): then $\langle u, \bar\alpha v\rangle = \alpha \langle u, v\rangle$, and choosing $\alpha$ to rotate $\langle u, v\rangle$ to the positive real axis makes $\operatorname{Re}\langle u, \bar\alpha v\rangle = |\langle u, v\rangle|$. The previous inequality applied to $u, \bar\alpha v$ then gives $|\langle u, v\rangle|^2 \leq \|u\|^2 \|\bar\alpha v\|^2 = \|u\|^2 \|v\|^2$, as desired. $\qquad\blacksquare$

> [!note]- Alternative proof: orthogonal projection
> *Proof.* Assume $v \neq 0$. Let $U = \operatorname{span}(v)$ be the one-dimensional subspace. The orthogonal projection of $u$ onto $U$ is
> $$P_U u = \frac{\langle u, v\rangle}{\|v\|^2} v.$$
> By [[Thm - Best Approximation by Orthogonal Projection|the best-approximation property]] or by direct computation,
> $$\|P_U u\| \leq \|u\|.$$
> Compute $\|P_U u\| = |\langle u, v\rangle|/\|v\|$. So $|\langle u, v\rangle|/\|v\| \leq \|u\|$, i.e., $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Statistics: the correlation coefficient bound.** For random variables $X, Y$ with finite variance, $|\operatorname{Cov}(X, Y)| \leq \sigma_X \sigma_Y$. Equivalently, the correlation coefficient $\rho(X, Y) \in [-1, 1]$. The bridge from "$B$: $X, Y$ are random variables with finite variance" to the precondition "$A$: $X, Y$ are vectors in an inner product space" is the identification of mean-zero finite-variance random variables (modulo a.s. equality) with vectors in a Hilbert space under $\langle X, Y\rangle = E[XY]$. The application is so deeply embedded in statistics that "correlation is bounded by $\pm 1$" is usually taken as an empirical fact, but it is exactly Cauchy-Schwarz.

**Number theory: the AM-GM inequality and friends.** Setting $u = (1, 1, \dots, 1)$ and $v = (\sqrt{a_1}, \dots, \sqrt{a_n})$ with each $a_k > 0$ in $\mathbb{R}^n$ Cauchy-Schwarz gives $(\sum \sqrt{a_k})^2 \leq n \sum a_k$, equivalently $\left(\frac{\sum \sqrt{a_k}}{n}\right)^2 \leq \frac{\sum a_k}{n}$ — the squared average of $\sqrt{a_k}$ is at most the average of $a_k$, which is **Jensen's inequality** for the concave function $\sqrt{\cdot}$. Many AM-GM-style inequalities follow from Cauchy-Schwarz with a clever choice of vectors.

**PDE analysis: bounding integrals.** For functions $f, g \in L^2(\Omega)$, Cauchy-Schwarz gives $|\int_\Omega fg|^2 \leq \int_\Omega f^2 \cdot \int_\Omega g^2$. This is the central inequality for $L^2$-based energy estimates in PDE theory: estimates of the form $\int u\, v\, dx \leq \|u\|_{L^2} \|v\|_{L^2}$ are used to bound nonlinear-coupling terms in weak formulations of PDEs and to prove existence by compactness.

**Quantum mechanics: the uncertainty principle.** The Heisenberg uncertainty principle $\sigma_X \sigma_P \geq \hbar / 2$ in its general formulation $\sigma_A \sigma_B \geq \tfrac{1}{2}|\langle[A, B]\rangle|$ — for any two self-adjoint observables $A, B$ — follows from Cauchy-Schwarz applied to the operators $(A - \langle A\rangle I)\psi$ and $(B - \langle B\rangle I)\psi$ on the state $\psi$. The Cauchy-Schwarz inequality, applied at the level of an inner-product Hilbert space, is what powers the lower bound on the product of standard deviations of non-commuting observables.

**Probability: the variance of a sum is bounded.** For random variables $X_1, \dots, X_n$, the variance of the sum is bounded by $n \sum \operatorname{Var}(X_k)$ — Cauchy-Schwarz applied to $(1, 1, \dots, 1)$ and $(X_1 - EX_1, \dots, X_n - EX_n)$ in the $L^2$ inner product. This appears in the proof of the law of large numbers and concentration inequalities.

---

# Bridges

- **[[Thm - Triangle Inequality|Triangle Inequality]]** — the triangle inequality is the direct downstream consequence of Cauchy-Schwarz: $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2 \leq \|u\|^2 + 2\|u\|\,\|v\| + \|v\|^2 = (\|u\| + \|v\|)^2$. The middle step *is* Cauchy-Schwarz applied to the real-part term. Without Cauchy-Schwarz, the inner-product norm would not satisfy the triangle inequality, hence would not be a norm. So Cauchy-Schwarz is the load-bearing inequality that turns an inner-product space into a normed (and hence metric, and hence topological) space.

- **Bessel's Inequality** *(within this topic, see proof of [[Thm - Best Approximation by Orthogonal Projection]])* — Cauchy-Schwarz is the special case of Bessel's inequality with a single orthonormal vector $e_1 = v/\|v\|$: it says $|\langle u, e_1\rangle|^2 \leq \|u\|^2$, which is $|\langle u, v\rangle|^2/\|v\|^2 \leq \|u\|^2$. Bessel's inequality extends this to a list of orthonormal vectors and is the infinite-dimensional foundation of Fourier-coefficient convergence. From this perspective Cauchy-Schwarz is "Bessel with one term".

- **Hilbert space generalization** *(Functional Analysis)* — Cauchy-Schwarz holds verbatim in any inner product space, finite- or infinite-dimensional. In Hilbert spaces it is the bedrock of the entire theory: continuity of the inner product as a map $H \times H \to \mathbf{F}$ follows from Cauchy-Schwarz (the map is jointly Lipschitz), the dual space $H^* \cong H$ identification (Riesz) uses Cauchy-Schwarz to bound $\|\varphi\| = \|v\|$, and convergence of orthonormal expansions $\sum c_n e_n$ uses Bessel's inequality (a direct consequence). Every result about Hilbert spaces routes through Cauchy-Schwarz somewhere.

- **[[Def - Minkowski Space and the Metric|Minkowski space]] and the reverse Cauchy-Schwarz** *(Special Relativity)* — in Minkowski space with indefinite signature, the Cauchy-Schwarz inequality **reverses direction** for timelike vectors: if $u, v$ are both future-pointing timelike, then $\langle u, v\rangle \leq -\sqrt{|\langle u, u\rangle| \cdot |\langle v, v\rangle|}$ (with the convention that timelike norms are imaginary). This is the algebraic content of the **twin paradox**: a straight-line worldline is *longer* in proper time than a broken path between the same events, the opposite of the Euclidean triangle inequality. The signature change flips the direction of the bound, but the *form* of the inequality (a product of square roots bounds an inner product) is preserved.

- **Hölder's inequality** *(Analysis)* — the generalization of Cauchy-Schwarz to $L^p$ spaces is **Hölder's inequality**: for $1 \leq p, q \leq \infty$ with $1/p + 1/q = 1$, $|\int fg| \leq \|f\|_p \|g\|_q$. Cauchy-Schwarz is the $p = q = 2$ case. Hölder's inequality is the workhorse of $L^p$ analysis, replacing Cauchy-Schwarz everywhere the Hilbert-space structure is unavailable. The proof of Hölder uses Young's inequality $ab \leq a^p/p + b^q/q$ — which itself reduces to a convexity statement — rather than the orthogonal-projection picture available in the Hilbert case.

---

# Unlocked by This

> [!tip] Heisenberg Uncertainty Principle *(from Quantum Mechanics)*
> For two self-adjoint observables $A, B$ on a state $\psi$ in a Hilbert space, the **Heisenberg uncertainty principle** gives
> $$\sigma_A(\psi)\, \sigma_B(\psi) \geq \frac{1}{2}|\langle[A, B]\rangle_\psi|,$$
> where $\sigma_A(\psi) = \sqrt{\langle\psi | (A - \langle A\rangle_\psi)^2 | \psi\rangle}$ and $[A, B] = AB - BA$ is the commutator. The proof is Cauchy-Schwarz applied to the vectors $(A - \langle A\rangle)\psi$ and $(B - \langle B\rangle)\psi$, with the commutator emerging from the antisymmetric (imaginary) part of $\langle (A - \langle A\rangle)\psi, (B - \langle B\rangle)\psi\rangle$. For $A = X$ (position) and $B = P$ (momentum), $[X, P] = i\hbar I$ gives the canonical $\sigma_X \sigma_P \geq \hbar/2$ — the original uncertainty relation. The full uncertainty principle in quantum mechanics is, at root, an instance of Cauchy-Schwarz.
