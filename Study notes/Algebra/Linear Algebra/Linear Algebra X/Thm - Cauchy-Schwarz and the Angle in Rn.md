---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Norm and Distance"
  - "Def - Angle Between Vectors"
tags: [algebra, linear-algebra, applied, inequality]
---

# Notation

Throughout, $a, b \in \mathbb R^n$ are vectors (with $n \geq 1$); the standard inner product is $a^T b = \sum_i a_i b_i$, and the Euclidean norm is $\|a\| = \sqrt{a^T a}$. The angle between two nonzero vectors is $\angle(a, b) \in [0, \pi]$; see [[Def - Angle Between Vectors]].

---

# Statement

> **Theorem (Cauchy–Schwarz inequality).** For any vectors $a, b \in \mathbb R^n$,
> $$|a^T b| \leq \|a\| \|b\|.$$
> Equality holds if and only if one of $a, b$ is a scalar multiple of the other (in particular, equality always holds when either vector is zero).

> **Corollary (well-definedness of angle).** For nonzero $a, b \in \mathbb R^n$, the number $a^T b/(\|a\|\|b\|)$ lies in the closed interval $[-1, 1]$, so the **angle** $\angle(a, b) = \arccos(a^T b/(\|a\|\|b\|)) \in [0, \pi]$ is well-defined.

The named inequality is attributed to Cauchy (for finite-dimensional sums) and Schwarz (for integrals); in the general inner-product-space setting it is sometimes called the Cauchy–Bunyakovsky–Schwarz inequality, after Bunyakovsky, who proved an integral version.

---

# Motivation

Without Cauchy–Schwarz, the entire geometric apparatus built on the Euclidean inner product collapses: the **angle** between vectors is undefined (the arccos formula would attempt to take an out-of-range argument); the **correlation coefficient** is not constrained to $[-1, 1]$; the **triangle inequality** has no proof; the **Pythagorean theorem** does not generalise cleanly. So this inequality is the linchpin of inner-product geometry — it is what permits all the geometric notions that follow from norm and inner product to be coherent.

The inequality is also one of the most-used facts in applied mathematics. It bounds *every* inner product by the product of the norms, which converts any expression involving $a^T b$ into a bound involving only magnitudes. This is what makes Cauchy–Schwarz the universal first-line estimate in analysis: when you see an inner product in the middle of an inequality and want to control it, Cauchy–Schwarz is the move.

The non-obvious depth of the theorem is the **equality characterisation**: equality holds exactly when one vector is a scalar multiple of the other (the *aligned* case). This is what makes the inequality tight — it cannot be strengthened without further hypotheses — and what gives the angle its full range from $0$ (aligned) through $\pi/2$ (orthogonal) to $\pi$ (anti-aligned). Without this characterisation, we would not know that the bound is "saturated" by aligned vectors, and the angle could not take the extreme values $0$ and $\pi$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of Cauchy–Schwarz is bare: *any two vectors in $\mathbb R^n$*. The skill is recognising the inequality's applicability in problems that do not mention vectors at all, by spotting the underlying inner-product structure.

**Source 1 — sums of products.** Any expression of the form $\sum_i a_i b_i$ — a sum of products of $n$ pairs — *is* an inner product. So Cauchy–Schwarz bounds any such sum by $\sqrt{\sum_i a_i^2}\sqrt{\sum_i b_i^2}$. The non-obvious bridge is from "a sum of products" (an algebraic expression) to "an inner product" (a geometric object). Example: bound $\sum_i \sqrt{x_i}$ for $x_i \geq 0$ by recognising it as $\sum_i 1 \cdot \sqrt{x_i}$, which is the inner product of $\mathbf 1$ with $(\sqrt{x_1}, \dots, \sqrt{x_n})$. Cauchy–Schwarz gives $\sum_i \sqrt{x_i} \leq \sqrt n \cdot \sqrt{\sum_i x_i}$ — a sharp bound used constantly in statistics.

**Source 2 — expectation of a product.** For a probability space with random variables $X, Y$, the expectation $\mathbb E[XY]$ is an inner product on $L^2$, and Cauchy–Schwarz gives $|\mathbb E[XY]| \leq \sqrt{\mathbb E[X^2]}\sqrt{\mathbb E[Y^2]}$. This is the probabilistic incarnation, and it bounds covariance by the product of standard deviations: $|\operatorname{Cov}(X, Y)| \leq \sigma_X \sigma_Y$, which is exactly the statement that the correlation coefficient lies in $[-1, 1]$. The bridge is from "expectation of a product" to "inner product in $L^2$".

**Source 3 — integral of a product.** The original Schwarz form applies to integrals: for measurable $f, g$ on a measure space, $|\int fg \, d\mu| \leq \sqrt{\int f^2 \, d\mu}\sqrt{\int g^2 \, d\mu}$. This is the case of an infinite-dimensional inner product space ($L^2(\mu)$), but the proof is the same. The bridge is from "integral of a product" to "inner product in $L^2(\mu)$", and the result underlies Hölder's inequality, the variational characterisation of eigenvalues, and many classical analysis results.

**Targets (Output Amplification)**

The conclusion of Cauchy–Schwarz, $|a^T b| \leq \|a\|\|b\|$, is itself a bound, but combined with other facts it gives further structural results.

**Target 1 — Triangle inequality.** Combining Cauchy–Schwarz ($|a^T b| \leq \|a\|\|b\|$) with the expansion $\|a + b\|^2 = \|a\|^2 + 2 a^T b + \|b\|^2$ gives $\|a + b\|^2 \leq \|a\|^2 + 2\|a\|\|b\| + \|b\|^2 = (\|a\| + \|b\|)^2$, hence $\|a + b\| \leq \|a\| + \|b\|$. So the triangle inequality is *a consequence of Cauchy–Schwarz*; it is not an independent assumption.

**Target 2 — Correlation coefficient bounds.** For two non-constant vectors $a, b$ with de-meaned versions $\tilde a, \tilde b$, the correlation coefficient is $\rho = \tilde a^T \tilde b/(\|\tilde a\|\|\tilde b\|)$. Cauchy–Schwarz applied to $\tilde a, \tilde b$ gives $|\rho| \leq 1$, with equality iff $\tilde a, \tilde b$ are scalar multiples (i.e., $b$ is an affine function of $a$). This is the deterministic version of Pearson's correlation lying in $[-1, 1]$, and it underwrites the entire interpretation of correlation as a "normalised covariance".

**Target 3 — Operator-norm and matrix bounds.** For any matrix $A$ and vector $x$, $\|Ax\|^2 = \sum_i (a_i^T x)^2 \leq \sum_i \|a_i\|^2 \|x\|^2 = \|A\|_F^2 \|x\|^2$, using Cauchy–Schwarz row-by-row. This gives $\|Ax\| \leq \|A\|_F \|x\|$, the **operator-norm bound** by the Frobenius norm. This bound is fundamental in numerical analysis: it controls how matrix–vector products amplify the size of a vector.

**Target 4 — Variance of weighted sum.** For random variables $X_1, \dots, X_n$ and weights $w_1, \dots, w_n$, $\operatorname{Var}(\sum_i w_i X_i) \leq \|w\|^2 \cdot \max_i \operatorname{Var}(X_i)$ — by Cauchy–Schwarz on the cross terms in the variance expansion. This is the basic bound in portfolio theory and statistics for the variance of a linear combination.

---

# Why Is It True

The geometric picture is the cleanest path to intuition: $a^T b = \|a\|\|b\|\cos\theta$ where $\theta$ is the angle between $a$ and $b$. Since $|\cos\theta| \leq 1$, we immediately have $|a^T b| \leq \|a\|\|b\|$, with equality iff $\cos\theta = \pm 1$ iff $a, b$ are aligned or anti-aligned.

But of course this argument is circular if the angle is *defined* by Cauchy–Schwarz — we cannot use the angle's existence to prove the inequality that gives it meaning. So the actual proof must be algebraic: it starts from $\|\beta a - \alpha b\|^2 \geq 0$ for appropriate $\alpha, \beta$ and rearranges.

**The mechanism in one bolded line: the squared norm $\|\beta a - \alpha b\|^2$ is always non-negative, expands to a quadratic in the cross term $a^T b$, and rearranging the resulting inequality is exactly Cauchy–Schwarz.** This is the proof "one-shot": the inequality is just non-negativity of a particular squared norm, expanded.

Why does this specific quadratic give Cauchy–Schwarz cleanly? Because choosing $\alpha = \|a\|$ and $\beta = \|b\|$ makes the quadratic *balanced*: the diagonal terms $\beta^2 \|a\|^2 = \alpha^2 \|b\|^2 = \|a\|^2 \|b\|^2$ are equal, and the cross term $-2\alpha\beta(a^T b) = -2\|a\|\|b\|(a^T b)$ pulls out the inequality $a^T b \leq \|a\|\|b\|$ after a single division. Applying the same argument with $-a$ in place of $a$ flips the sign and gives $a^T b \geq -\|a\|\|b\|$, so $|a^T b| \leq \|a\|\|b\|$.

The equality case is read off from the proof: equality holds iff $\|\beta a - \alpha b\|^2 = 0$, iff $\beta a = \alpha b$, iff $a, b$ are positive scalar multiples (and similarly the sign-flipped case for anti-alignment). For the zero vector, both sides are zero, so equality is trivial.

---

# What Makes This Hard

The proof itself is short and elementary once you know to start from $\|\beta a - \alpha b\|^2 \geq 0$, but the non-obvious step is *choosing $\alpha = \|a\|$ and $\beta = \|b\|$* rather than $\alpha = \beta = 1$ or some other arbitrary choice. The natural starting point — "expand $\|a - b\|^2 \geq 0$" — gives the *weaker* bound $a^T b \leq (\|a\|^2 + \|b\|^2)/2$ (the AM-GM inequality), which is missing the multiplicative structure. The trick of using $\alpha = \|a\|$, $\beta = \|b\|$ rebalances the diagonal terms so that the cross term gives Cauchy–Schwarz directly. Once this trick is seen, the proof is mechanical.

The common error is to attempt to *use the angle* in the proof — to write $a^T b = \|a\|\|b\|\cos\theta$ and conclude $|a^T b| \leq \|a\|\|b\|$ from $|\cos\theta| \leq 1$. But the angle is defined by Cauchy–Schwarz, so this is circular.

A second pitfall is forgetting the equality case. The inequality alone does not tell you when it is tight; the equality characterisation (scalar multiples) is what gives Cauchy–Schwarz its full structural content, and many corollaries (the equality case of the triangle inequality, the saturation of correlation at $\pm 1$) require it.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Start from $\|\beta a - \alpha b\|^2 \geq 0$ with $\alpha = \|a\|, \beta = \|b\|$. Expand using the squared-norm identity. The diagonal terms equalise, the cross term yields $-2\|a\|\|b\|(a^T b)$, and rearranging gives $a^T b \leq \|a\|\|b\|$. Applying the same argument to $-a, b$ gives the lower bound, and combining yields $|a^T b| \leq \|a\|\|b\|$.

**Subgoal decomposition:**

1. **Dispatch the trivial case.** If $a = 0$ or $b = 0$, both sides of the inequality are zero, so equality holds.
   - *Hint:* $\|0\| = 0$ and $0^T b = 0$.
   - *Why needed:* The proof below assumes $a, b \neq 0$ implicitly when dividing by $\|a\|\|b\|$.

2. **Expand the squared norm with chosen coefficients.** Assume $a, b \neq 0$. Set $\alpha = \|a\|, \beta = \|b\|$. Show $\|\beta a - \alpha b\|^2 = 2\|a\|^2\|b\|^2 - 2\|a\|\|b\|(a^T b)$.
   - *Hint:* Use $\|x - y\|^2 = \|x\|^2 - 2 x^T y + \|y\|^2$, with $x = \beta a$ and $y = \alpha b$.
   - *Why needed:* This identity contains the inner product $a^T b$ and the norms in a linear arrangement, allowing direct rearrangement.

3. **Conclude the upper bound.** From step 2 and $\|\beta a - \alpha b\|^2 \geq 0$, derive $a^T b \leq \|a\|\|b\|$.
   - *Hint:* $0 \leq 2\|a\|^2\|b\|^2 - 2\|a\|\|b\|(a^T b)$, divide both sides by $2\|a\|\|b\| > 0$.
   - *Why needed:* This is half of Cauchy–Schwarz (the upper bound).

4. **Derive the lower bound.** Apply step 3 to $-a$ and $b$ to get $-a^T b \leq \|a\|\|b\|$, equivalently $a^T b \geq -\|a\|\|b\|$.
   - *Hint:* $\|-a\| = \|a\|$ and $(-a)^T b = -a^T b$.
   - *Why needed:* Combined with step 3, this gives $|a^T b| \leq \|a\|\|b\|$.

5. **Identify the equality case.** Equality in step 3 corresponds to $\|\beta a - \alpha b\| = 0$, i.e., $\|b\| a = \|a\| b$, i.e., $a$ is a positive scalar multiple of $b$ (when both are nonzero). Equality in step 4 corresponds to $a$ being a *negative* multiple of $b$. Conversely, scalar multiplicity always gives equality.
   - *Hint:* $\|v\| = 0 \iff v = 0$ (definiteness of the norm).
   - *Why needed:* The equality characterisation is essential for downstream applications (triangle inequality equality, correlation $= \pm 1$).

---

# Lemma Decomposition

Each lemma below is independently practiceable in about five minutes.

> [!note]- Lemma 1: $\|x - y\|^2 = \|x\|^2 - 2 x^T y + \|y\|^2$
> **Statement:** For any vectors $x, y \in \mathbb R^n$, $\|x - y\|^2 = \|x\|^2 - 2 x^T y + \|y\|^2$.
>
> **Hint:** Expand $(x - y)^T(x - y)$ directly and use the bilinearity of the inner product.
>
> **Why needed:** This is the key algebraic identity used to expand $\|\beta a - \alpha b\|^2$ in the main proof.
>
> > [!note]- Full proof
> > By definition $\|x - y\|^2 = (x - y)^T (x - y)$. Expanding:
> > $$(x - y)^T (x - y) = x^T x - x^T y - y^T x + y^T y = \|x\|^2 - 2 x^T y + \|y\|^2,$$
> > using $x^T y = y^T x$ (the inner product is symmetric).

> [!note]- Lemma 2: Norm of scalar multiple
> **Statement:** For any vector $x \in \mathbb R^n$ and scalar $\alpha \in \mathbb R$, $\|\alpha x\| = |\alpha| \|x\|$.
>
> **Hint:** $\|\alpha x\|^2 = (\alpha x)^T(\alpha x) = \alpha^2 x^T x$, then take the square root.
>
> **Why needed:** Used to identify $\|\beta a\|^2 = \beta^2 \|a\|^2$ and similarly $\|\alpha b\|^2 = \alpha^2 \|b\|^2$ in the main expansion.
>
> > [!note]- Full proof
> > $\|\alpha x\|^2 = (\alpha x)^T (\alpha x) = \alpha (x^T \alpha x) = \alpha^2 (x^T x) = \alpha^2 \|x\|^2$. Taking the non-negative square root, $\|\alpha x\| = |\alpha| \|x\|$.

> [!note]- Lemma 3: Equality $\|v\| = 0 \iff v = 0$
> **Statement:** For any $v \in \mathbb R^n$, $\|v\| = 0$ if and only if $v = 0$.
>
> **Hint:** $\|v\|^2 = \sum_i v_i^2$ is a sum of non-negative terms; if it is zero, each $v_i^2 = 0$.
>
> **Why needed:** This is the definiteness property of the norm, used to extract the equality characterisation $\beta a - \alpha b = 0 \iff a, b$ are scalar multiples.
>
> > [!note]- Full proof
> > If $v = 0$, then $\|v\|^2 = \sum_i 0 = 0$, so $\|v\| = 0$. Conversely, if $\|v\| = 0$, then $\|v\|^2 = \sum_i v_i^2 = 0$. Each $v_i^2 \geq 0$, and a sum of non-negative terms is zero iff each is zero. So $v_i^2 = 0$, hence $v_i = 0$, for all $i$, hence $v = 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For any $a, b \in \mathbb R^n$, $|a^T b| \leq \|a\| \|b\|$, with equality iff one of $a, b$ is a scalar multiple of the other.
>
> *Proof.* If $a = 0$, then $a^T b = 0$ and $\|a\|\|b\| = 0$, so the inequality holds with equality (and trivially $a = 0 \cdot b$ is a scalar multiple). The case $b = 0$ is symmetric.
>
> Suppose now $a, b \neq 0$. Set $\alpha = \|a\| > 0$ and $\beta = \|b\| > 0$. Consider the vector $\beta a - \alpha b$, which is non-zero only when $\beta a \neq \alpha b$. We have, by Lemma 1 applied to $x = \beta a$ and $y = \alpha b$:
> $$\|\beta a - \alpha b\|^2 = \|\beta a\|^2 - 2(\beta a)^T(\alpha b) + \|\alpha b\|^2.$$
> By Lemma 2, $\|\beta a\|^2 = \beta^2 \|a\|^2 = \|b\|^2 \|a\|^2$ and $\|\alpha b\|^2 = \alpha^2 \|b\|^2 = \|a\|^2 \|b\|^2$. So both diagonal terms equal $\|a\|^2\|b\|^2$. The cross term is $-2\alpha\beta (a^T b) = -2\|a\|\|b\|(a^T b)$. Substituting:
> $$\|\beta a - \alpha b\|^2 = 2\|a\|^2\|b\|^2 - 2\|a\|\|b\|(a^T b).$$
>
> The left side is non-negative, so
> $$0 \leq 2\|a\|^2\|b\|^2 - 2\|a\|\|b\|(a^T b).$$
> Dividing by $2\|a\|\|b\| > 0$, we get
> $$a^T b \leq \|a\|\|b\|. \quad (\star)$$
>
> Applying $(\star)$ to $-a$ in place of $a$ (with $\|-a\| = \|a\|$, $(-a)^T b = -a^T b$):
> $$-a^T b \leq \|a\|\|b\|, \text{ i.e. } a^T b \geq -\|a\|\|b\|.$$
> Combined with $(\star)$, $|a^T b| \leq \|a\| \|b\|$, which is Cauchy–Schwarz.
>
> **Equality case.** From the derivation, equality in $(\star)$ holds iff $\|\beta a - \alpha b\|^2 = 0$, iff $\beta a = \alpha b$ (by Lemma 3), iff $\|b\| a = \|a\| b$. Since $\|a\|, \|b\| > 0$, this is iff $a = (\|a\|/\|b\|) b$, i.e., $a$ is a positive scalar multiple of $b$. Equality in the lower bound ($a^T b = -\|a\|\|b\|$) corresponds, by the same argument applied to $-a$, to $a = -(\|a\|/\|b\|)b$, a negative multiple. Combined: $|a^T b| = \|a\|\|b\|$ iff $a, b$ are scalar multiples (with the sign of $a^T b$ matching the sign of the scalar). $\quad\blacksquare$
>
> **Corollary.** $a^T b / (\|a\|\|b\|) \in [-1, 1]$ for nonzero $a, b$, so $\angle(a, b) = \arccos(\cdot)$ is well-defined in $[0, \pi]$.

---

# Cross-Field Exercise Suggestions

**Probability — bound on covariance.** Given two random variables $X, Y$ with finite second moments on a probability space, $|\operatorname{Cov}(X, Y)| \leq \sigma_X \sigma_Y$, where $\sigma_X = \sqrt{\operatorname{Var}(X)}$. The proof: $\operatorname{Cov}(X, Y) = \mathbb E[(X - \mu_X)(Y - \mu_Y)]$ is an $L^2$ inner product of the centred variables; Cauchy–Schwarz gives the bound. This is the basis of the Pearson correlation coefficient being in $[-1, 1]$.

**Analysis — Hölder's inequality.** Cauchy–Schwarz is the case $p = q = 2$ of **Hölder's inequality**: for $p, q$ with $1/p + 1/q = 1$, $|\int fg \,d\mu| \leq \|f\|_p \|g\|_q$. The general case is proved by a similar non-negativity-of-a-square argument, replacing the $L^2$-inner-product structure by a more general convexity argument.

**Combinatorics — number-of-edges bound.** Given a bipartite graph with $n + m$ vertices and $e$ edges, with $d_i$ the degree of vertex $i$, $\sum_i d_i = e$. Cauchy–Schwarz applied to $(d_1, \dots, d_n)$ and $\mathbf 1$ gives $e = \sum d_i \leq \sqrt n \sqrt{\sum d_i^2}$, which translates degree distributions into edge counts.

**Quantum mechanics — uncertainty principle.** The Heisenberg uncertainty principle $\Delta x \Delta p \geq \hbar/2$ is a Cauchy–Schwarz inequality applied to the operators $x$ and $p$ in the inner product of square-integrable wavefunctions. The non-commutativity $[x, p] = i\hbar$ enters as a non-trivial correction to the basic Cauchy–Schwarz bound, but the structure is the same.

---

# Bridges

- **[[Def - Norm and Distance|Triangle inequality]]** — Cauchy–Schwarz is the engine of the triangle inequality, via expanding $\|a + b\|^2 = \|a\|^2 + 2 a^T b + \|b\|^2 \leq \|a\|^2 + 2 |a^T b| + \|b\|^2 \leq \|a\|^2 + 2\|a\|\|b\| + \|b\|^2 = (\|a\| + \|b\|)^2$. The triangle inequality is *derived* from Cauchy–Schwarz, not an independent axiom — though it could equivalently be taken as the starting axiom in the abstract theory of normed spaces.

- **[[Def - Angle Between Vectors|Angle between vectors]]** — Cauchy–Schwarz is precisely what makes the angle well-defined. The ratio $a^T b/(\|a\|\|b\|)$ is constrained to $[-1, 1]$ by the inequality, with the extreme values $\pm 1$ corresponding to alignment and anti-alignment. Without Cauchy–Schwarz the arccos formula would fail.

- **[[Def - Standard Deviation and Correlation Coefficient|Correlation coefficient]]** — applying Cauchy–Schwarz to the de-meaned vectors $\tilde a, \tilde b$ gives $|\rho(a, b)| \leq 1$, the structural fact behind the entire interpretation of correlation. The equality case $\rho = \pm 1$ corresponds to $b$ being an affine function of $a$ (positive or negative slope), the deterministic analogue of "perfect linear relationship".

- **The pseudoinverse least-squares formula** — when solving over-determined systems, Cauchy–Schwarz is what controls the size of the projection: $|q^T b| \leq \|q\|\|b\|$ for any unit vector $q$, with the projection onto the column space being the saturating choice. This makes the QR-derived pseudoinverse $A^\dagger = R^{-1} Q^T$ the natural object.

- **The operator norm and matrix norms in numerical analysis** — for any matrix $A$, the **spectral norm** $\|A\|_2 = \max_{\|x\| = 1} \|A x\|$ measures the maximum amplification of $A$, and Cauchy–Schwarz gives the weaker (but easier-to-compute) Frobenius-norm bound $\|A x\| \leq \|A\|_F \|x\|$. The spectral norm is the *tight* operator norm; the Frobenius norm is a Cauchy–Schwarz upper bound on it.

---

# Unlocked by This

> [!tip] Hölder's Inequality and $L^p$ Spaces *(from Functional Analysis)*
> Cauchy–Schwarz is the case $p = q = 2$ of **Hölder's inequality** $|\int fg| \leq \|f\|_p \|g\|_q$ for $1/p + 1/q = 1$. Hölder generalises Cauchy–Schwarz to arbitrary $L^p$ spaces and is the fundamental inequality underlying the entire theory of $L^p$ spaces in analysis.

> [!tip] Heisenberg's Uncertainty Principle *(from Quantum Mechanics)*
> The fundamental uncertainty $\Delta x \Delta p \geq \hbar/2$ for position and momentum operators in quantum mechanics is a direct application of Cauchy–Schwarz in the inner-product structure of square-integrable wavefunctions, modified by a commutator term. The Robertson uncertainty principle generalises this to any pair of non-commuting observables.
