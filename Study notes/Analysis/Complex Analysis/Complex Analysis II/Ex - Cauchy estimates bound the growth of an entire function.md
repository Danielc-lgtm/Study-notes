---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Cauchy Estimates"
  - "Thm - Liouville's Theorem"
  - "Thm - Higher Derivatives via CIF"
  - "Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $f : \mathbb{C} \to \mathbb{C}$ be entire, and suppose there are constants $A > 0$, $R_0 > 0$, and a non-negative integer $n$ such that
$$|f(z)| \;\leq\; A|z|^n \qquad \text{for all } |z| \geq R_0.$$
Show that $f$ is a polynomial of degree at most $n$.

In words: an entire function whose growth at infinity is *at most polynomial of degree $n$* is itself a polynomial of degree $\leq n$. The case $n = 0$ is [[Thm - Liouville's Theorem|Liouville's theorem]] (bounded entire $\Rightarrow$ constant); the result generalises Liouville from $n = 0$ to every integer.

**Recall:**

![[Thm - Cauchy Estimates#Statement]]

![[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)#Statement]]

An **entire** function is one that is holomorphic on all of $\mathbb{C}$. The Taylor series of an entire $f$ at $0$ converges on the entire plane: $f(z) = \sum_{k=0}^\infty c_k z^k$ with $c_k = f^{(k)}(0)/k!$, and this identity holds for *every* $z \in \mathbb{C}$ (the radius of convergence is infinite). $f$ is a **polynomial of degree $\leq n$** iff its Taylor series has $c_k = 0$ for every $k > n$; in this case the apparent infinite sum collapses to a finite one.

---

# Convergent Strategy

**Problem class.** This is a *growth-controls-structure* problem, the signature class of §2.4: a *quantitative* bound on $|f|$ at infinity is converted, via [[Thm - Cauchy Estimates|Cauchy estimates]], into a *structural* conclusion about $f$ — namely that its Taylor series truncates. The class is identified by the prompt "entire $+$ growth bound" together with a structural conclusion. The reusable shape is: *use the Cauchy estimate to bound each Taylor coefficient $c_k$ individually, then let the radius go to infinity to force vanishing of all coefficients beyond a certain index.* This is *exactly* the structure of [[Thm - Liouville's Theorem|Liouville's theorem]] generalised one rung up the ladder — Liouville is the case $n = 0$.

**Assumption pattern.** Two features make the problem tractable. First, $f$ is *entire*, so the [[Thm - Cauchy Estimates|Cauchy estimate]] applies on a disc $D(0, R)$ for *every* $R > 0$ — no upper bound on the radius. This is what lets us take $R \to \infty$ at the end. Second, the growth bound $|f(z)| \leq A|z|^n$ is *polynomial* in $|z|$: the supremum $M(R) := \sup_{|z| = R}|f(z)|$ grows at most like $A R^n$. The Cauchy estimate $|f^{(k)}(0)| \leq k! M(R)/R^k$ then reads $|f^{(k)}(0)| \leq A k! R^{n - k}$, where the exponent $n - k$ is *negative* for every $k > n$ — and this is the structural reason the high coefficients are forced to zero.

**Theorem routing.** The route has three links. (a) [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|Power series globally]]: $f(z) = \sum c_k z^k$ on all of $\mathbb{C}$ since $f$ is entire (the radius of convergence is $\infty$). (b) [[Thm - Cauchy Estimates|Cauchy estimates]] at $a = 0$ with radius $R$: $|f^{(k)}(0)| \leq k! M(R)/R^k$. (c) The growth bound gives $M(R) \leq A R^n$ for $R \geq R_0$; substituting and letting $R \to \infty$ kills $c_k$ for every $k > n$. The chain *converts* the size bound at infinity into a vanishing-coefficient statement, which is then read backwards as polynomial structure.

**Key decision point.** The non-obvious choice is *to let $R \to \infty$* — and to realise that this is *possible* only because $f$ is entire (every $R$ is in the domain of holomorphicity). The Cauchy estimate yields *one* inequality $|c_k| \leq A R^{n-k}$ for every $R \geq R_0$; the *strength* of the estimate is in choosing $R$ optimally. For $k > n$, the exponent $n - k$ is negative, so larger $R$ gives a sharper bound — the limit $R \to \infty$ gives the sharpest possible bound, which is $0$. For $k \leq n$, the exponent $n - k$ is non-negative, so larger $R$ gives a *weaker* bound, and the limit gives no information (which is fine — we *do not* want to force the low coefficients to vanish, only the high ones). Recognising that the same family of inequalities can be made sharp or vacuous by choosing $R$ — and using that freedom to surgically kill only the high coefficients — is the reusable insight.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Complex Analysis II — Cauchy's Theorem and its Consequences#Legal Operations|the topic page's Legal Operations]]:

1. **Use power series for local computation** (operation 7 from the topic page). Since $f$ is entire, its Taylor series at $0$ converges on all of $\mathbb{C}$, so "$f$ is a polynomial of degree $\leq n$" is equivalent to "$c_k = 0$ for every $k > n$." This reduces the structural question (is $f$ a polynomial?) to a coefficient-level question (do the high coefficients vanish?), which is the language Cauchy estimates speak.

2. **Apply the Cauchy estimate to bound coefficients.** The Cauchy estimate $|f^{(k)}(0)| \leq k! M(R)/R^k$ provides a family of inequalities indexed by $R > 0$. The growth hypothesis gives $M(R) \leq A R^n$, so $|c_k| = |f^{(k)}(0)|/k! \leq A R^{n - k}$ for every $R \geq R_0$. The Cauchy estimate is the *universal bridge* from "I know how big $f$ is on a circle" to "I know how big $f^{(k)}(a)$ is at the centre."

3. **Use Liouville to force constancy from boundedness** (operation 5 from the topic page), in disguise. The original proof of Liouville is the case $n = 0$ of this very argument: $|c_k| \leq A R^{-k} \to 0$ as $R \to \infty$ for $k > 0$, so $c_k = 0$ for $k \geq 1$, hence $f$ is the constant $c_0$. This exercise generalises that strategy.

4. **Let $R \to \infty$ on the Cauchy estimate.** For $k > n$, the bound $|c_k| \leq A R^{n - k}$ has $R$ to a negative power, so the bound shrinks without limit as $R$ grows. The Cauchy estimate as a *function of $R$* is what gives the killing power; taking the infimum (or limit) over $R$ extracts that power.

---

# Hints

> [!note]- Hint 1
> Since $f$ is entire, the [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|power series expansion]] $f(z) = \sum_{k=0}^\infty c_k z^k$ converges on all of $\mathbb{C}$ (the radius of convergence is $\infty$). The claim "$f$ is a polynomial of degree $\leq n$" is equivalent to "$c_k = 0$ for every $k > n$."

> [!note]- Hint 2
> Apply [[Thm - Cauchy Estimates|Cauchy estimates]] at $a = 0$ with arbitrary radius $R > 0$: $|f^{(k)}(0)| \leq k! M(R)/R^k$ where $M(R) = \sup_{|z|=R}|f(z)|$. The hypothesis bounds $M(R)$.

> [!note]- Hint 3
> For $R \geq R_0$, the hypothesis gives $M(R) \leq A R^n$. Substitute into the Cauchy estimate to get $|c_k| = |f^{(k)}(0)|/k! \leq A R^{n - k}$ for *every* $R \geq R_0$.

> [!note]- Hint 4
> For $k > n$, the exponent $n - k < 0$, so $R^{n - k} \to 0$ as $R \to \infty$. The bound on $|c_k|$ tends to $0$; since the inequality holds for arbitrarily large $R$, $|c_k| = 0$, i.e., $c_k = 0$.

> [!note]- Hint 5
> For $k \leq n$, the same bound gives $|c_k| \leq A R^{n - k}$ with $n - k \geq 0$, which provides no information as $R \to \infty$ — this is fine; we *do not need* to kill the low coefficients. The conclusion is that $c_k = 0$ for $k > n$ and the high tail of the power series vanishes, leaving a polynomial.

---

# Solution

The plan is to compress the growth bound on $f$ into vanishing of the high Taylor coefficients via Cauchy estimates. Step 1 expands $f$ as a Taylor series at $0$, valid on all of $\mathbb{C}$ because $f$ is entire. Step 2 applies the Cauchy estimate with the growth bound to produce $|c_k| \leq A R^{n - k}$ for every $R \geq R_0$. Step 3 lets $R \to \infty$ for $k > n$, killing every coefficient beyond index $n$ and exhibiting $f$ as a polynomial of degree $\leq n$.

**Step 1: Global Taylor expansion.**

Since $f$ is entire, by [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|the analyticity theorem]] it has a Taylor series at $0$ that converges on all of $\mathbb{C}$:
$$f(z) \;=\; \sum_{k = 0}^\infty c_k z^k, \qquad c_k \;=\; \frac{f^{(k)}(0)}{k!}.$$

> [!note]- Derivation
> The [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|local power series theorem]] says that for $f$ holomorphic on $D(a, R)$, the Taylor series at $a$ converges on $D(a, R)$ — in particular, the radius of convergence is at least $R$. For an entire $f$, $R$ can be taken arbitrarily large: $f$ is holomorphic on $D(0, R)$ for every $R > 0$, hence the radius of convergence of the Taylor series at $0$ is at least every positive real number, i.e., it is $\infty$. The series therefore converges on all of $\mathbb{C}$, and the formula $c_k = f^{(k)}(0)/k!$ comes from differentiating the series termwise and evaluating at $z = 0$.

**Step 2: Cauchy estimate on every disc.**

For every $R > 0$ and every $k \geq 0$:
$$|f^{(k)}(0)| \;\leq\; \frac{k!\, M(R)}{R^k}, \qquad M(R) \;:=\; \sup_{|z| = R}|f(z)|.$$
For $R \geq R_0$ the growth hypothesis gives $M(R) \leq A R^n$, so $|c_k| = |f^{(k)}(0)|/k! \leq A R^{n - k}$.

> [!note]- Derivation
> *Cauchy estimate.* Since $f$ is holomorphic on $D(0, R)$ for every $R > 0$, the [[Thm - Cauchy Estimates|Cauchy estimate]] applies at the centre $a = 0$ with the full radius $R$:
> $$|f^{(k)}(0)| \;\leq\; \frac{k!\, M(R)}{R^k} \qquad \text{for every } R > 0, \; k \geq 0.$$
> The estimate is the [[Thm - ML Estimate|ML estimate]] applied to the [[Thm - Higher Derivatives via CIF|higher-derivative CIF]] $f^{(k)}(0) = (k!/2\pi i)\oint_{|z|=R} f(z)/z^{k+1}\,dz$ — namely $|f^{(k)}(0)| \leq (k!/2\pi)\cdot M(R)/R^{k+1}\cdot 2\pi R = k!M(R)/R^k$.
>
> *Bounding $M(R)$ by the growth hypothesis.* For $R \geq R_0$, the growth hypothesis is $|f(z)| \leq A|z|^n = A R^n$ on the circle $|z| = R$, hence $M(R) \leq A R^n$.
>
> *Combine.* For $R \geq R_0$:
> $$|f^{(k)}(0)| \;\leq\; \frac{k! \cdot A R^n}{R^k} \;=\; A k!\, R^{n - k},$$
> and so $|c_k| = |f^{(k)}(0)|/k! \leq A R^{n - k}$. This holds for *every* $R \geq R_0$ — a family of inequalities, one per radius.

**Step 3: Let $R \to \infty$ to kill the high coefficients.**

For every $k > n$, $c_k = 0$. Hence the Taylor series of $f$ is a polynomial of degree at most $n$.

> [!note]- Derivation
> Fix $k > n$. Then $n - k$ is a *negative* integer, so $R^{n - k} \to 0$ as $R \to \infty$. The bound $|c_k| \leq A R^{n - k}$ holds for every $R \geq R_0$, hence in the limit $R \to \infty$:
> $$|c_k| \;\leq\; \lim_{R \to \infty} A R^{n - k} \;=\; 0.$$
> Since $|c_k|$ is non-negative and bounded above by $0$, $|c_k| = 0$ and hence $c_k = 0$.
>
> This holds for *every* $k > n$. The Taylor series collapses:
> $$f(z) \;=\; \sum_{k=0}^\infty c_k z^k \;=\; \sum_{k=0}^n c_k z^k \;+\; \sum_{k=n+1}^\infty 0 \cdot z^k \;=\; \sum_{k=0}^n c_k z^k.$$
> This is a polynomial of degree at most $n$ — the actual degree is the largest $k \leq n$ with $c_k \neq 0$, which may be strictly less than $n$ if the high coefficients happen to vanish.
>
> Note that *no* claim about $c_k$ for $k \leq n$ is required: the exercise asks only "degree $\leq n$," not "degree exactly $n$." The Cauchy estimate is silent on the low coefficients (it gives $|c_k| \leq A R^{n - k}$ with $n - k \geq 0$, a non-trivial *constraint* but no vanishing in the limit), and that is exactly right — we do not want to force $c_0, \dots, c_n$ to vanish; we want only to truncate the tail.

> [!note]- Complete formal solution
> *(Power series.)* Since $f$ is entire, by [[Thm - Holomorphic Functions are Analytic (Local Power Series Expansion)|the analyticity theorem]] $f(z) = \sum_{k=0}^\infty c_k z^k$ on all of $\mathbb{C}$, with $c_k = f^{(k)}(0)/k!$.
>
> *(Cauchy estimate combined with growth bound.)* For any $R \geq R_0$, the [[Thm - Cauchy Estimates|Cauchy estimate]] gives
> $$|c_k| \;=\; \frac{|f^{(k)}(0)|}{k!} \;\leq\; \frac{M(R)}{R^k} \;\leq\; \frac{A R^n}{R^k} \;=\; A R^{n - k},$$
> using $M(R) := \sup_{|z|=R}|f(z)| \leq A R^n$ from the growth hypothesis.
>
> *(Vanishing of high coefficients.)* For $k > n$, $n - k < 0$, so $A R^{n - k} \to 0$ as $R \to \infty$. The inequality $|c_k| \leq A R^{n - k}$ holds for every $R \geq R_0$, hence in the limit $|c_k| \leq 0$, so $c_k = 0$.
>
> *(Polynomial conclusion.)* The Taylor series becomes $f(z) = \sum_{k=0}^n c_k z^k$, a polynomial of degree at most $n$. $\blacksquare$

> [!note]- Sanity check: the case $n = 0$ recovers Liouville
> If $n = 0$, the growth bound reads $|f(z)| \leq A$ for $|z| \geq R_0$, and continuity of $f$ on the compact disc $\overline{D(0, R_0)}$ gives $|f(z)| \leq A'$ there for some $A'$, so $f$ is *bounded* on all of $\mathbb{C}$. The above argument then gives $c_k = 0$ for every $k > 0$, leaving $f(z) = c_0$ — i.e., $f$ is constant. This is exactly [[Thm - Liouville's Theorem|Liouville's theorem]]. The exercise generalises Liouville from $n = 0$ to every integer $n \geq 0$, and the proof is literally the same with the growth bound $|f| \leq A$ replaced by $|f| \leq A|z|^n$.

---

# Key Takeaways

**Growth at infinity controls polynomial degree, and the Cauchy estimate is the bridge.**

This exercise establishes one of the *cleanest* structural theorems in complex analysis: an entire function with polynomial growth of degree $n$ is itself a polynomial of degree $\leq n$. The bridge from analytic data (a size bound on $f$) to algebraic structure (the truncation of the Taylor series) is the [[Thm - Cauchy Estimates|Cauchy estimate]], which converts a sup-norm bound on a circle into a coefficient-by-coefficient bound. The *quantitative* form $|c_k| \leq M(R)/R^k$ is the engine of every "growth $\Rightarrow$ structure" result in complex analysis: bounded entire $\Rightarrow$ constant (Liouville, the $n = 0$ case); polynomial-growth entire $\Rightarrow$ polynomial (this exercise); sub-exponential entire $\Rightarrow$ controlled by an explicit growth order (Hadamard's factorization theorem, downstream in [[Complex Analysis IV — Mapping Theory and Applications|CA IV]]). The reusable trigger is precise: any time you have an entire function with a control on $|f(z)|$ as $|z| \to \infty$, reach for Cauchy estimates with $R \to \infty$ to translate the control into vanishing of high Taylor coefficients. The complex setting has no real-analytic analogue — real polynomials cannot be detected by their growth at infinity in any comparable way, because real-analytic functions can have arbitrary tails.

**Take $R \to \infty$: the same inequality is sharp or vacuous depending on the index.**

The Cauchy estimate gives a *family* of inequalities indexed by the radius $R$: $|c_k| \leq A R^{n - k}$ for every $R \geq R_0$. The crucial observation is that the *same* inequality is informative for *different* indices $k$ at *different* radii. For $k > n$, the exponent $n - k$ is negative, so $R \to \infty$ tightens the bound to $0$ — the high coefficients are forced to vanish. For $k < n$, the exponent is positive, so $R \to \infty$ loosens the bound to $\infty$ — no information; we have to use small $R$ instead, where the bound is finite but offers no killing power. For $k = n$, the bound is the constant $A$ regardless of $R$ — the coefficient $c_n$ is *not* forced to vanish, but is *bounded* (by $A$, the growth-bound constant). This trichotomy — kill the high, bound the middle, leave the low — is the structural fingerprint of the Cauchy-estimate proof, and it generalises directly: for any growth rate $M(R)$ that is a function of $R$, the bound $|c_k| \leq M(R)/R^k$ kills the indices where $M(R)/R^k \to 0$ and constrains the indices where it stays bounded. The reusable trigger is: *whenever a Cauchy-estimate proof faces an arbitrary radius $R$, ask which index range each value of $R$ gives information about, and tune $R$ accordingly.*

**The polynomial-degree theorem is half a classification of entire functions.**

The result you have just proved sits at the second rung of a ladder classifying entire functions by their growth at infinity. The rungs are: *(rung 0)* bounded $\Rightarrow$ constant ([[Thm - Liouville's Theorem|Liouville]]); *(rung n)* $O(|z|^n)$ at infinity $\Rightarrow$ polynomial of degree $\leq n$ (this exercise); *(rung $\rho$, $\rho \in [0, \infty]$)* growth of *order* $\rho$ (defined via $\limsup \log\log M(R)/\log R = \rho$) and *type* gives the Hadamard factorization, which writes $f$ as a product of a polynomial in $z$, an exponential factor, and a canonical product over its zeros. The structural moral is that entire functions are classified *up to growth at infinity*, in striking contrast to merely smooth or even merely $C^\infty$ functions, which admit no such classification. This is the deepest analytic-vs-algebraic phenomenon in §2: a *single quantitative* control (the size of $|f|$ at infinity) determines *all* of the *algebraic* structure (which Taylor coefficients are non-zero, what factorisations are possible). Everything in §2 — Liouville, the fundamental theorem of algebra, the maximum modulus principle — is a special case or refinement of this growth-vs-structure correspondence.

**Cross-link to companion exercises.**

This exercise is the natural sequel to [[Ex - Liouville for harmonic functions]] (which generalises Liouville to *harmonic* functions via the harmonic-conjugate-and-exponentiate trick) and the more focused [[Ex - Cauchy estimates bound polynomial degree]] (which the present exercise re-derives in expanded form, with explicit attention to *which* indices each value of $R$ controls). Together these three exercises drill the universal pattern *growth bound* + *Cauchy estimate* + *radius limit* $\Rightarrow$ *structural conclusion*, in three different forms: bounded $\Rightarrow$ constant (Liouville); polynomial-growth $\Rightarrow$ polynomial (this exercise); harmonic + bounded $\Rightarrow$ constant (the harmonic case). Recognising the shared trigger is the goal of the chapter's §2.4 exercise sequence.
