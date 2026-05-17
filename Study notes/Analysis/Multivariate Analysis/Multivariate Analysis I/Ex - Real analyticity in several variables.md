---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Taylor's Theorem in Several Variables"
  - "Def - Higher-Order Derivatives and Ck Maps"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

A function $f : U \to \mathbb{R}$ on an open set $U \subseteq \mathbb{R}^n$ is **real-analytic** at $x_0 \in U$ if there is a ball $B(x_0, \rho) \subseteq U$ on which $f$ equals its Taylor series:
$$f(x_0 + h) = \sum_{\alpha \in \mathbb{N}^n} \frac{\partial^\alpha f(x_0)}{\alpha!}\,h^\alpha \qquad \text{for all } |h| < \rho.$$

1. Show that real-analyticity is *strictly stronger* than $C^\infty$: every real-analytic function is $C^\infty$, but there exists a $C^\infty$ function on $\mathbb{R}$ — hence on $\mathbb{R}^n$ — that is not real-analytic at the origin. *(Use the standard one-variable example $g(t) = e^{-1/t}$ for $t > 0$, $g(t) = 0$ for $t \le 0$.)*
2. Give the **derivative-bound criterion** for real-analyticity: if there are constants $C, r > 0$ with $|\partial^\alpha f(x)| \le C\,\dfrac{\alpha!}{r^{|\alpha|}}$ for all multi-indices $\alpha$ and all $x$ in a neighbourhood of $x_0$, then $f$ is real-analytic at $x_0$. Prove it by showing the Taylor remainder $R_{k+1} \to 0$.
3. Apply the criterion to show $f(x,y) = e^{x}\cos y$ is real-analytic at every point of $\mathbb{R}^2$.

**Recall:**

The framework is Taylor's theorem and its remainder estimate, pushed to $k \to \infty$.

![[Thm - Taylor's Theorem in Several Variables#Statement]]

[[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] gives, for $f \in C^{k+1}$, the expansion $f(x_0+h) = P_k(h) + R_{k+1}(x_0,h)$ with $R_{k+1}$ an explicit integral. Real-analyticity is the statement that $R_{k+1} \to 0$ as $k \to \infty$, so the partial sums $P_k$ converge to $f$.

A function is [[Def - Higher-Order Derivatives and Ck Maps|smooth]], denoted $C^\infty$, if it has continuous partials of every order. Real-analytic $\Rightarrow C^\infty$, but not conversely.

---

# Convergent Strategy

**Problem class.** This is a mixed *separating-example* and *verify-a-property* problem operating at the top of the regularity ladder. As the [[Multivariate Analysis I — Differentiation in Several Variables#Insights|topic page]] organises the $C^k$ classes into a strict hierarchy, this exercise adds the rung *above* $C^\infty$ — real-analyticity — and shows that gap is strict too, then gives the working criterion for landing on it.

**Assumption pattern.** Part 1 needs the canonical $C^\infty$-but-not-analytic function $g(t) = e^{-1/t}$; its defining feature is that *all* its derivatives vanish at the origin, so its Taylor series is identically zero while the function is not — the Taylor series converges, but to the wrong thing. Part 2's hypothesis is a *bound on all derivatives* of the precise form $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$ — the factorial growth rate that exactly cancels the $1/\alpha!$ in the Taylor coefficients, leaving a geometric series. Part 3's function $e^x\cos y$ is a product of functions whose derivatives are uniformly bounded, the textbook setting for the criterion.

**Theorem routing.** Part 1: real-analytic $\Rightarrow C^\infty$ because a convergent power series can be differentiated term by term to all orders; the converse fails via $g$, whose Taylor series at $0$ is the zero series. Part 2: feed the derivative bound into the [[Thm - Taylor's Theorem in Several Variables|Taylor remainder]] estimate $|R_{k+1}| \le \sum_{|\alpha|=k+1}\frac{|h^\alpha|}{\alpha!}\sup|\partial^\alpha f|$; the bound makes each term at most $C(|h|/r)^{k+1}$ times a multinomial count, and the geometric factor $(|h|/r)^{k+1} \to 0$ when $|h| < r$. Part 3: bound the derivatives of $e^x$ and $\cos y$ uniformly on a neighbourhood and assemble the criterion's hypothesis.

**Key decision point.** The crux is recognising *why the factorial in the bound is exactly right*. The Taylor coefficient is $\partial^\alpha f/\alpha!$. If $|\partial^\alpha f|$ is allowed to grow like $\alpha!$ (times a geometric factor $r^{-|\alpha|}$), then the coefficient $\partial^\alpha f/\alpha!$ is bounded by a pure geometric $r^{-|\alpha|}$ — and a geometric series converges. The factorial in the hypothesis is calibrated to *cancel* the factorial in the denominator of the Taylor coefficient, converting the series into a geometric one. Spotting this cancellation is the whole insight; without it the criterion looks arbitrary.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Approximate by a Taylor polynomial with controlled remainder.** Use the explicit integral remainder of [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] and its bound.

2. **Push the order $k \to \infty$.** Real-analyticity is the statement that the Taylor partial sums converge; the tool is to show $R_{k+1} \to 0$.

3. **Cancel a factorial against a factorial.** The derivative bound $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$ is designed to cancel the $1/\alpha!$ in the Taylor coefficient, leaving a geometric series.

4. **Bound derivatives of an explicit function uniformly.** For $e^x\cos y$, bound $\partial^\alpha f$ on a neighbourhood using $|e^x| \le e^{x_0+1}$ and $|\cos^{(k)}| \le 1$.

5. **Sum a multinomial-weighted geometric series.** Use $\sum_{|\alpha|=k+1}\frac{(k+1)!}{\alpha!}s^{|\alpha|} = (ns)^{k+1}$ to collapse the remainder bound.

---

# Hints

> [!note]- Hint 1
> For Part 1, the easy direction: a convergent power series can be differentiated term by term within its domain of convergence, infinitely often — so a real-analytic function is $C^\infty$. The hard direction: take $g(t) = e^{-1/t}$ for $t>0$ and $0$ for $t\le0$. Show every derivative $g^{(k)}(0) = 0$. Then the Taylor series of $g$ at $0$ is $0 + 0\cdot t + 0\cdot t^2 + \cdots$, which converges — to the zero function, not to $g$.

> [!note]- Hint 2
> For Part 2, the Taylor remainder satisfies $|R_{k+1}(x_0,h)| \le \sum_{|\alpha|=k+1}\frac{|h^\alpha|}{\alpha!}\sup_{[x_0,x_0+h]}|\partial^\alpha f|$. Substitute the hypothesis $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$. The $\alpha!$ cancels! You are left with $C\sum_{|\alpha|=k+1}\frac{|h^\alpha|}{r^{|\alpha|}}$.

> [!note]- Hint 3
> Bound $|h^\alpha| \le |h|^{|\alpha|}$ — actually use $|h_j| \le |h|$ so $|h^\alpha| = \prod|h_j|^{\alpha_j} \le |h|^{|\alpha|}$. Then $\sum_{|\alpha|=k+1}\frac{|h|^{k+1}}{r^{k+1}} = (|h|/r)^{k+1}\cdot\#\{\alpha : |\alpha|=k+1\}$. The number of such multi-indices is a polynomial in $k$, so the product still tends to $0$ when $|h| < r$. (A cleaner bound: $\sum_{|\alpha|=k+1}\frac{(k+1)!}{\alpha!}s^{|\alpha|} = (ns)^{k+1}$ by the multinomial theorem.)

> [!note]- Hint 4
> For Part 3, $f = e^x\cos y$. A partial $\partial^\alpha f = \partial_x^{\alpha_1}\partial_y^{\alpha_2}f = e^x\cdot(\pm\cos y \text{ or } \pm\sin y)$. So $|\partial^\alpha f(x,y)| \le e^x \le e^{x_0 + 1}$ on the ball of radius $1$ about $(x_0, y_0)$. This is $\le C$ for a constant $C$ — which fits the hypothesis $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$ with $r = 1$, since $C \le C\alpha!/1^{|\alpha|}$ (as $\alpha! \ge 1$).

---

# Solution

Real-analyticity sits one rung above $C^\infty$: it demands not just that all derivatives exist, but that the Taylor series actually *reconstructs* the function. The gap is real — $e^{-1/t}$ has every derivative zero at the origin yet is not zero — and the criterion that closes it is a factorial-rate bound on the derivatives, calibrated to cancel the $1/\alpha!$ in the Taylor coefficients and leave a convergent geometric series.

**Step 1: Real-analytic $\Rightarrow C^\infty$, but $C^\infty \not\Rightarrow$ real-analytic.**

> [!note]- Derivation
> *Real-analytic $\Rightarrow C^\infty$.* If $f$ equals a convergent power series $\sum_\alpha c_\alpha h^\alpha$ on a ball, then within that ball the series may be differentiated term by term, any number of times — a standard fact about power series, since termwise differentiation preserves the radius of convergence. Each differentiation yields another convergent power series, which is continuous. So all partial derivatives of $f$ of every order exist and are continuous: $f \in C^\infty$.
>
> *$C^\infty \not\Rightarrow$ real-analytic.* Consider, in one variable, $g(t) = e^{-1/t}$ for $t > 0$ and $g(t) = 0$ for $t \le 0$. For $t > 0$, by induction every derivative has the form $g^{(k)}(t) = P_k(1/t)\,e^{-1/t}$ for some polynomial $P_k$. As $t \to 0^+$, $e^{-1/t}$ decays faster than any power of $1/t$ grows, so $g^{(k)}(t) \to 0$; combined with $g^{(k)} \equiv 0$ for $t < 0$, a limit argument gives $g^{(k)}(0) = 0$ for every $k$. Hence $g \in C^\infty(\mathbb{R})$, and its Taylor series at $0$ is $\sum_k \frac{g^{(k)}(0)}{k!}t^k = \sum_k 0 = 0$.
>
> This series converges everywhere — to the *zero function*. But $g(t) > 0$ for every $t > 0$. So the Taylor series of $g$ does **not** equal $g$ on any neighbourhood of $0$: $g$ is not real-analytic at $0$. Promoting $g$ to $\mathbb{R}^n$ by $f(x) = g(x_1)$ gives a $C^\infty$ function on $\mathbb{R}^n$ that is not real-analytic at the origin. Real-analyticity is strictly stronger than $C^\infty$.

**Step 2: The derivative-bound criterion — if $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$ near $x_0$, then $f$ is real-analytic at $x_0$.**

> [!note]- Derivation
> Suppose $|\partial^\alpha f(x)| \le C\,\alpha!/r^{|\alpha|}$ for all $\alpha$ and all $x$ in a ball $B(x_0, \rho')$. We show the [[Thm - Taylor's Theorem in Several Variables|Taylor]] remainder $R_{k+1}(x_0,h) \to 0$ as $k \to \infty$, for $|h|$ small.
>
> The remainder bound from Taylor's theorem is
> $$|R_{k+1}(x_0,h)| \le \sum_{|\alpha|=k+1}\frac{|h^\alpha|}{\alpha!}\sup_{[x_0,x_0+h]}|\partial^\alpha f|.$$
> Substitute the hypothesis $\sup|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$. The factorial **cancels**:
> $$|R_{k+1}(x_0,h)| \le \sum_{|\alpha|=k+1}\frac{|h^\alpha|}{\alpha!}\cdot\frac{C\,\alpha!}{r^{|\alpha|}} = C\sum_{|\alpha|=k+1}\frac{|h^\alpha|}{r^{k+1}}.$$
> This cancellation is the heart of the criterion: the factorial in the derivative bound is precisely calibrated to annihilate the $1/\alpha!$ in the Taylor coefficient.
>
> Now bound the sum. Since each $|h_j| \le |h|$, $|h^\alpha| = \prod_j|h_j|^{\alpha_j} \le |h|^{|\alpha|} = |h|^{k+1}$. The multinomial theorem gives the sharp count: $\sum_{|\alpha|=k+1}\frac{(k+1)!}{\alpha!}s^{|\alpha|} = (ns)^{k+1}$, and dropping the $(k+1)!/\alpha! \ge 1$ weights, $\sum_{|\alpha|=k+1}|h^\alpha| \le \sum_{|\alpha|=k+1}\frac{(k+1)!}{\alpha!}|h|^{k+1} = (n|h|)^{k+1}$. Therefore
> $$|R_{k+1}(x_0,h)| \le \frac{C}{r^{k+1}}\,(n|h|)^{k+1} = C\left(\frac{n|h|}{r}\right)^{k+1}.$$
> If $|h| < r/n$, the ratio $n|h|/r < 1$, so $\big(n|h|/r\big)^{k+1} \to 0$ as $k \to \infty$. Hence $R_{k+1}(x_0,h) \to 0$, the Taylor partial sums converge to $f(x_0+h)$, and $f$ equals its Taylor series on the ball $|h| < \rho := \min(\rho', r/n)$. So $f$ is real-analytic at $x_0$.

**Step 3: $f(x,y) = e^x\cos y$ is real-analytic at every point of $\mathbb{R}^2$.**

> [!note]- Derivation
> Fix any $(x_0, y_0) \in \mathbb{R}^2$ and work on the ball $B((x_0,y_0), 1)$. A general partial derivative of $f$ is $\partial^\alpha f = \partial_x^{\alpha_1}\partial_y^{\alpha_2}(e^x\cos y) = e^x\cdot\big(\partial_y^{\alpha_2}\cos y\big)$, since $\partial_x^{\alpha_1}e^x = e^x$. The function $\partial_y^{\alpha_2}\cos y$ is one of $\pm\cos y, \pm\sin y$, so $|\partial_y^{\alpha_2}\cos y| \le 1$ everywhere. On the ball $B((x_0,y_0),1)$, $|x| \le |x_0| + 1$, so $e^x \le e^{|x_0|+1}$. Hence
> $$|\partial^\alpha f(x,y)| \le e^{|x_0|+1} =: C \qquad \text{for all } \alpha \text{ and all } (x,y) \in B((x_0,y_0),1).$$
> This uniform bound fits the criterion's hypothesis $|\partial^\alpha f| \le C\,\alpha!/r^{|\alpha|}$ with $r = 1$: since $\alpha! \ge 1$ and $r^{|\alpha|} = 1$, we have $C \le C\,\alpha!/1^{|\alpha|}$, so $|\partial^\alpha f| \le C \le C\alpha!/r^{|\alpha|}$. By the criterion of Step 2, $f$ is real-analytic at $(x_0, y_0)$. Since $(x_0,y_0)$ was arbitrary, $e^x\cos y$ is real-analytic on all of $\mathbb{R}^2$.
>
> (Indeed every entry of the Taylor series can be written down: $e^x\cos y = \operatorname{Re}\big(e^{x+iy}\big) = \operatorname{Re}\sum_k\frac{(x+iy)^k}{k!}$, exhibiting the convergent series directly.)

> [!note]- Complete formal solution
> **Claim.** Real-analytic $\Rightarrow C^\infty$ strictly; the bound $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$ implies real-analyticity; $e^x\cos y$ is real-analytic on $\mathbb{R}^2$.
>
> *Strictness.* A convergent power series is termwise infinitely differentiable, so real-analytic $\Rightarrow C^\infty$. The function $g(t) = e^{-1/t}$ ($t>0$), $0$ ($t\le0$) is $C^\infty$ with $g^{(k)}(0)=0$ for all $k$, so its Taylor series at $0$ is identically $0 \neq g$; thus $g$ (and $f(x) = g(x_1)$ on $\mathbb{R}^n$) is $C^\infty$ but not real-analytic.
>
> *Criterion.* Given $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$, the Taylor remainder bound $|R_{k+1}| \le \sum_{|\alpha|=k+1}\frac{|h^\alpha|}{\alpha!}\sup|\partial^\alpha f|$ becomes $|R_{k+1}| \le C\sum_{|\alpha|=k+1}|h^\alpha|/r^{k+1} \le C(n|h|/r)^{k+1}$ (multinomial theorem). For $|h| < r/n$ this $\to 0$, so $f$ equals its Taylor series — real-analytic.
>
> *Application.* For $f = e^x\cos y$, $\partial^\alpha f = e^x\cdot(\pm\cos y\text{ or }\pm\sin y)$, so $|\partial^\alpha f| \le e^{|x_0|+1} =: C$ on $B((x_0,y_0),1)$, fitting the criterion with $r=1$. Hence $e^x\cos y$ is real-analytic everywhere. $\blacksquare$

---

# Key Takeaways

**Real-analyticity is strictly stronger than $C^\infty$, and the gap is the difference between "the Taylor series converges" and "it converges to the right function".** The regularity ladder does not stop at $C^\infty$. A smooth function has all derivatives, hence a well-defined formal Taylor series — but that series might converge to something other than $f$, or fail to converge at all. Real-analyticity is the genuine top rung: the Taylor series converges *and reconstructs $f$*. The witness to the strict gap, $e^{-1/t}$, is worth carrying permanently: it is flat to infinite order at the origin (every derivative vanishes), so its Taylor series is the zero series, which converges beautifully — to zero — while the function itself is positive. The lesson is that "has a Taylor series" and "equals its Taylor series" are different statements, and the second is real-analyticity. This same function $e^{-1/t}$ is also the building block of bump functions and partitions of unity, which exist precisely *because* smoothness does not force analyticity — an analytic bump function would have to vanish on an open set and hence everywhere.

**The route from $C^\infty$ to real-analyticity is to show the Taylor remainder vanishes as the order grows — Taylor's theorem with its explicit remainder is exactly the tool.** [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] is usually used at a fixed finite order $k$, to get a polynomial approximation with an $O(|h|^{k+1})$ error. Real-analyticity is what you get by letting $k \to \infty$: the partial sums $P_k$ are the truncated Taylor series, and they converge to $f$ exactly when the remainder $R_{k+1} \to 0$. So the explicit remainder formula — the thing that looked like technical baggage — is the precise instrument for establishing analyticity. The general pattern: any "the series converges to the function" question is a "the remainder vanishes" question, and the remainder estimate is the bridge. This is the same logic by which one proves the one-variable series for $e^t$, $\sin t$, $\cos t$ converge to those functions.

**A factorial-rate bound on all derivatives is the working criterion for analyticity, because the factorial cancels the $1/\alpha!$ in the Taylor coefficient and leaves a geometric series.** The criterion $|\partial^\alpha f| \le C\alpha!/r^{|\alpha|}$ looks arbitrary until one sees the cancellation. The Taylor coefficient is $\partial^\alpha f/\alpha!$. If the derivatives are allowed to grow as fast as $\alpha!$ (times a geometric factor $r^{-|\alpha|}$) but no faster, then the *coefficient* $\partial^\alpha f/\alpha!$ is bounded by the pure geometric $r^{-|\alpha|}$ — and a geometric series with ratio below $1$ converges. The factorial in the hypothesis is precisely the factorial that the Taylor coefficient's denominator can absorb; the leftover is geometric, and geometric is convergent. This calibration is the reusable insight: whenever you must decide if a smooth function is analytic, bound its derivatives and ask whether the growth rate is *at most factorial* — sub-factorial or factorial growth gives analyticity, super-factorial growth (like $g^{(k)}(t) \sim (k!)^2$, which $e^{-1/t}$ exhibits near the origin) is what destroys it. Entire functions like $e^x$, $\sin$, $\cos$ — and any product or composition of them — have uniformly bounded or polynomially-bounded derivatives, comfortably within the factorial budget, which is why they are analytic everywhere.
