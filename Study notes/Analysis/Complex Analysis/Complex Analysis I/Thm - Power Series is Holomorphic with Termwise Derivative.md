---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Power Series and Radius of Convergence"
  - "Def - Holomorphic Function"
  - "Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs"
tags: [analysis, complex-analysis]
---

# Notation

$f(z) = \sum_{n=0}^\infty c_n (z - a)^n$ — a power series with radius of convergence $R > 0$. We freely shift to $a = 0$ by the change of variables $z \mapsto z - a$. Full registry on [[Complex Analysis I — Basic Notions]].

---

# Motivation

A power series with positive radius of convergence defines a function on its disc of convergence — but in what sense is this function "nice"? The strongest possible answer: it is *holomorphic*, with the derivative obtained by differentiating term-by-term, and this derivative is itself a power series with the *same* radius of convergence. Iterating, we get $f \in C^\infty$ on $D(a, R)$, with $f^{(n)}(a) = n! c_n$ — the coefficient formula.

This is the foundational structural result for power series: it says they behave *algebraically* like polynomials with respect to differentiation (term-by-term) while also being *analytic* objects with concrete derivatives at every point. It is also the bridge from the formal/algebraic notion of power series to the analytic notion of holomorphic function — and combined with the converse direction proved in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]] ("every holomorphic function is a power series"), it gives the equivalence *power series = holomorphic function*.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "a power series $\sum c_n (z - a)^n$ with $R > 0$".

The first disguised source is **a function defined as a uniform-on-compacts limit of polynomials**: by the radius-of-convergence theorem ([[Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs]]), the partial sums $S_N(z) = \sum_{n=0}^N c_n (z - a)^n$ converge uniformly on compact subsets to $f$. So *any* function arising as a uniform-on-compacts limit of polynomials *is* a power series (by Runge's theorem in suitable settings), and inherits holomorphicity.

The second disguised source is **a function defined via Cauchy's integral formula**: $f(z) = \frac{1}{2\pi i}\int_\gamma g(w)/(w - z)\,dw$ for $g$ continuous on $\gamma$. Expanding $1/(w - z)$ as a geometric series in $z$ exhibits $f$ as a power series — this is the proof of holomorphicity from CIF in [[Complex Analysis II — Cauchy's Theorem and its Consequences|CA II]].

**Targets (Output Amplification)**

The conclusion is "$f$ is holomorphic on $D(a, R)$ with $f'(z) = \sum n c_n (z - a)^{n-1}$".

Combine with **iteration.** Property $D$: apply termwise differentiation again. The amplified result: $f^{(k)}(z) = \sum n(n-1)\ldots(n-k+1) c_n (z - a)^{n-k}$ for every $k$, also same radius. So $f \in C^\infty$ and $f^{(k)}(a) = k! c_k$ — the **Taylor coefficient formula**.

Combine with **the coefficient formula.** Property $D$: $f$ given as a power series. The amplified result: the coefficients are uniquely determined by $f$ via $c_k = f^{(k)}(a)/k!$. This is the uniqueness of power-series representation.

Combine with **termwise integration.** Property $D$: integrate along a path in $D(a, R)$. The amplified result: $\int f(z)\,dz = \sum c_n \int (z - a)^n\,dz$ is also a power series. Used to build power-series representations of antiderivatives.

---

# Why Is It True

The intuition is that uniform convergence is just strong enough to let limits commute with derivatives, *if* we have uniform control of the derivatives. Here we get this control: the formally differentiated series $\sum n c_n (z - a)^{n-1}$ has the same radius of convergence as the original ($\limsup |n c_n|^{1/n} = \limsup |c_n|^{1/n}$, since $n^{1/n} \to 1$). So both series converge uniformly on closed sub-discs, and the formal derivative is itself a continuous function on $D(a, R)$.

To prove that the formal derivative is the *actual* derivative, the trick is to set up a *bivariate* series $g(z, w) = \sum c_n (z^{n-1} + z^{n-2} w + \ldots + w^{n-1})$ (the inner sum is the algebraic identity $(z^n - w^n)/(z - w)$). This series converges uniformly on $|z|, |w| \leq r$ for $r < R$, defining a continuous function $g$. Then $g(z, w) = (f(z) - f(w))/(z - w)$ for $z \neq w$, and $g(w, w) = \sum n c_n w^{n-1}$. Continuity of $g$ at $(w, w)$ gives $\lim_{z \to w}(f(z) - f(w))/(z - w) = g(w, w) = \sum n c_n w^{n-1}$, which is the desired derivative formula.

The deep insight: uniform convergence of the bivariate series is what lets us *commute the limit-as-$z \to w$ with the infinite sum*. The series for $g(z, w)$ has terms each of which is a polynomial in $z, w$ (continuous), and the uniform convergence lifts the continuity to the sum.

---

# What Makes This Hard

The non-obvious step is the *bivariate* series $g(z, w) = (f(z) - f(w))/(z - w)$ and the observation that it is a *uniformly convergent* power series in two variables on closed bi-discs. The naive approach — try to bound $|S_N'(w) - f'(w)|$ directly — runs into the difficulty that termwise differentiation is only justified once we *know* $f$ is differentiable. The bivariate trick circumvents this by working with the difference quotient directly, never invoking $f'$ until the very last step.

---

# Rederivation Scaffold

**High-level strategy:**
Show the formal derivative $g(w) = \sum n c_n (w - a)^{n-1}$ has the same radius $R$. Define $\phi(z, w) = (f(z) - f(w))/(z - w)$ via a bivariate power series, show it is continuous, and identify $\phi(w, w) = g(w)$. Conclude $f'(w) = g(w)$.

**Subgoal decomposition:**

1. **The formal derivative has the same radius.**
   - *Hint:* $\limsup |n c_n|^{1/n} = \limsup |c_n|^{1/n}$ since $n^{1/n} \to 1$.
   - *Why needed:* the differentiated series is a power series with the same convergence disc.

2. **The bivariate series $\sum c_n \sum_{j+k=n-1} z^j w^k$ converges uniformly on closed bi-discs.**
   - *Hint:* Weierstrass $M$-test: the $n$-th term has bound $n|c_n| r^{n-1}$, summable by step 1.
   - *Why needed:* defines a continuous function $\phi(z, w)$ extending the difference quotient.

3. **$\phi(z, w) = (f(z) - f(w))/(z - w)$ for $z \neq w$, and $\phi(w, w) = g(w)$.**
   - *Hint:* $z^n - w^n = (z - w)(z^{n-1} + z^{n-2} w + \ldots + w^{n-1})$.
   - *Why needed:* identifies $\phi$ as the difference quotient.

4. **Continuity of $\phi$ gives $\lim_{z \to w} \phi(z, w) = \phi(w, w)$, i.e., $f'(w) = g(w)$.**
   - *Why needed:* delivers the conclusion.

5. **Iteration: $f^{(k)}(z) = \sum n(n-1)\ldots(n-k+1) c_n (z - a)^{n-k}$ and $f^{(k)}(a) = k! c_k$.**
   - *Why needed:* the coefficient formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: The differentiated series has the same radius
> **Statement:** $\limsup |n c_n|^{1/n} = \limsup |c_n|^{1/n}$.
>
> **Hint:** $n^{1/n} \to 1$ as $n \to \infty$.
>
> **Why needed:** Confirms the formal derivative is a power series on the same disc.
>
> > [!note]- Full proof
> > $|n c_n|^{1/n} = n^{1/n} |c_n|^{1/n}$. Since $n^{1/n} \to 1$, $\limsup |n c_n|^{1/n} = 1 \cdot \limsup |c_n|^{1/n} = \limsup |c_n|^{1/n}$.

> [!note]- Lemma 2: Uniform convergence of the bivariate series
> **Statement:** The series $g(z, w) = \sum_{n=1}^\infty c_n (z^{n-1} + z^{n-2} w + \ldots + w^{n-1})$ (assuming $a = 0$) converges uniformly on $\{(z, w) : |z|, |w| \leq \rho\}$ for any $\rho < R$.
>
> **Hint:** Each summand is bounded by $n |c_n| \rho^{n-1}$; apply Weierstrass.
>
> **Why needed:** $g$ is continuous on the bi-disc; identifies the derivative.
>
> > [!note]- Full proof
> > For $|z|, |w| \leq \rho$: $|z^{n-1} + z^{n-2} w + \ldots + w^{n-1}| \leq n \rho^{n-1}$. So $|c_n (z^{n-1} + \ldots + w^{n-1})| \leq n |c_n| \rho^{n-1}$. By Lemma 1, $\sum n |c_n| \rho^{n-1} < \infty$ for $\rho < R$. By the Weierstrass $M$-test, the bivariate series converges uniformly on $\{|z|, |w| \leq \rho\}$. Each term is continuous in $(z, w)$ (a polynomial), so $g$ is continuous on the bi-disc. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Without loss of generality $a = 0$. By Lemma 1, the formal derivative $\sum_{n=1}^\infty n c_n z^{n-1}$ has radius of convergence $R$, so it converges on $D(0, R)$ to a continuous function — call it $g(w)$.
>
> Consider the bivariate series
> $$\phi(z, w) := \sum_{n=1}^\infty c_n \big(z^{n-1} + z^{n-2} w + \ldots + w^{n-1}\big).$$
> By Lemma 2, this converges uniformly on $\{|z|, |w| \leq \rho\}$ for any $\rho < R$, and defines a continuous function $\phi$ on $\{(z, w) : |z|, |w| < R\}$.
>
> For $z \neq w$ with $|z|, |w| < R$: the algebraic identity $z^n - w^n = (z - w)(z^{n-1} + z^{n-2} w + \ldots + w^{n-1})$ gives
> $$\phi(z, w) = \sum_{n=1}^\infty c_n \frac{z^n - w^n}{z - w} = \frac{f(z) - f(w)}{z - w}.$$
> (The interchange of summation and division by $z - w$ is justified by absolute convergence.)
>
> For $z = w$: $\phi(w, w) = \sum_{n=1}^\infty c_n \cdot n w^{n-1} = g(w)$.
>
> By continuity of $\phi$ at $(w, w)$:
> $$\lim_{z \to w} \frac{f(z) - f(w)}{z - w} = \lim_{z \to w} \phi(z, w) = \phi(w, w) = g(w).$$
> Hence $f'(w)$ exists and equals $g(w) = \sum_{n=1}^\infty n c_n w^{n-1}$. So $f$ is holomorphic on $D(0, R)$ with the stated derivative formula.
>
> **Iteration.** Applying the result to $f'$ (itself a power series with radius $R$): $f''(w) = \sum_{n=2}^\infty n(n-1) c_n w^{n-2}$. By induction, $f^{(k)}(w) = \sum_{n=k}^\infty n(n-1)\ldots(n-k+1) c_n w^{n-k}$. Evaluating at $w = 0$: only the $n = k$ term survives, giving $f^{(k)}(0) = k! c_k$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Holomorphic functional calculus.** For a bounded operator $T$ on a Banach space and $f(z) = \sum c_n z^n$ a power series with radius greater than the spectral radius of $T$, one defines $f(T) := \sum c_n T^n$. The series converges in the operator norm, and the resulting operator $f(T)$ inherits the algebraic properties of $f$ (sum, product, derivative formulas). This is the foundation of holomorphic functional calculus.

**Generating functions in combinatorics.** A generating function $A(z) = \sum a_n z^n$ has Taylor coefficients $a_n = A^{(n)}(0)/n!$. The theorem then says: differentiating $A$ extracts the next coefficient (after a factor of $n!$), and conversely $a_n$ encodes $A^{(n)}(0)$. This is the bidirectional bridge between sequence and function.

**Asymptotic expansions in analysis.** Functions like $f(z) = e^{-z^2}$ have well-defined Taylor series at $0$ with all real coefficients explicit; the radius of convergence is $\infty$. For functions like $f(z) = 1/(z^2 + 1)$ (singularities at $\pm i$), the radius at $0$ is exactly $1$ — the distance to the nearest pole.

---

# Bridges

- **[[Thm - Radius of Convergence Formula and Uniform Convergence on Sub-Discs]]** — gives the uniform convergence used here.

- **[[Thm - Identity Theorem for Power Series]]** — uses the coefficient formula $c_k = f^{(k)}(a)/k!$ to prove uniqueness of representation.

- **[[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)]]** — the converse direction proved in CA II, completing the equivalence "power series $\Leftrightarrow$ holomorphic".
