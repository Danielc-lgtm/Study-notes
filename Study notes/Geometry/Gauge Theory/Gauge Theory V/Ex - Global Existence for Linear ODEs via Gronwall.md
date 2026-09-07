---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
tags: [geometry, gauge-theory]
---

# Problem Statement

In a trivialising chart the horizontal lift of a curve through a matrix-group connection is governed by the linear ordinary differential equation
$$\dot v(t)=-A(t)\,v(t),\qquad v(0)=v_0\in\mathbb{K}^n,$$
where $A\colon[0,L]\to\operatorname{Mat}(n\times n;\mathbb{K})$ is continuous (it is $A_\alpha(\dot c)$, the local connection form contracted with the velocity of the base curve) and $\mathbb{K}\in\{\mathbb{R},\mathbb{C}\}$. The proof that horizontal lifts exist on the *whole* interval, rather than only for short time, hinges on one analytic fact: a linear system with merely continuous coefficients has a solution defined on all of $[0,L]$, and that solution is unique. The subtlety, flagged in the source, is that the ordinary Picard–Lindelöf theorem yields only a solution on a possibly small subinterval; global existence needs a further estimate that rules out escape to infinity in finite time.

This exercise isolates that estimate as a stand-alone drill.

1. **State and prove Grönwall's inequality** in the following integral form. Let $\phi,\kappa\colon[0,L]\to[0,\infty)$ be continuous, let $C\ge0$ be a constant, and suppose
$$\phi(t)\le C+\int_0^t\kappa(s)\,\phi(s)\,ds\qquad\text{for all }t\in[0,L].$$
Then $\displaystyle \phi(t)\le C\exp\!\Big(\int_0^t\kappa(s)\,ds\Big)$ for all $t\in[0,L]$.

2. **Deduce global existence and uniqueness.** Show that for every continuous $A\colon[0,L]\to\operatorname{Mat}(n\times n;\mathbb{K})$ and every $v_0\in\mathbb{K}^n$ there is a unique $C^1$ map $v\colon[0,L]\to\mathbb{K}^n$ solving $\dot v=-A(t)v$, $v(0)=v_0$, defined on **all** of $[0,L]$. Uniqueness is to be obtained from Grönwall's inequality; existence from Picard iteration, with the convergence proved to be uniform on the whole interval.

This is exactly the piece labelled "Lemma 2a" in the proof of [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]] (the matrix-group case of its global-existence step), and the corresponding "main theorem of ordinary differential equations" quoted without proof in Haydys' treatment of parallel sections.

**Recall:**

The result being serviced is the existence and uniqueness of horizontal lifts; the analytic content is the global solvability of a linear system.

![[Thm - Existence and Uniqueness of Horizontal Lifts#Statement]]

For a matrix group $G\subset GL(n;\mathbb{K})$ the horizontality condition $\dot h=-\mathrm{d}R_h\big(A_\alpha(\dot c)\big)$ for the fibre coordinate $h$ becomes the **linear** equation $\dot h=-A_\alpha(\dot c)\,h$, and applying it column by column (or to any initial vector) is the system $\dot v=-A(t)v$ above with $A(t)=A_\alpha(\dot c(t))$. Thus proving global existence and uniqueness for this linear system is precisely what upgrades "a horizontal lift exists locally" to "a horizontal lift exists on the entire interval and is unique."

We use the following standing notions, all at the level of a first course in analysis.

- The **operator norm** on $\operatorname{Mat}(n\times n;\mathbb{K})$ is $\lVert B\rVert:=\sup_{|x|\le1}|Bx|$, where $|\cdot|$ is the Euclidean norm on $\mathbb{K}^n$; it is submultiplicative, $\lVert BC\rVert\le\lVert B\rVert\,\lVert C\rVert$, and satisfies $|Bx|\le\lVert B\rVert\,|x|$.
- $\lVert A\rVert_{C^0}:=\max_{t\in[0,L]}\lVert A(t)\rVert$; this maximum is finite and attained because $t\mapsto\lVert A(t)\rVert$ is continuous on the compact interval $[0,L]$ (extreme value theorem).
- A **$C^1$ solution** of $\dot v=-A(t)v$, $v(0)=v_0$ is equivalent, by the fundamental theorem of calculus, to a **continuous** solution of the integral equation
$$v(t)=v_0-\int_0^t A(s)\,v(s)\,ds,$$
since the right-hand side of the integral equation is automatically $C^1$ (its integrand is continuous) with derivative $-A(t)v(t)$, and conversely integrating the differential equation from $0$ to $t$ produces the integral equation.

---

# Convergent Strategy

**Problem class.** This is a *foundational a-priori-estimate* problem: prove a comparison inequality and then run it as an engine for a qualitative conclusion (no finite-time blow-up, hence global existence; and uniqueness by squeezing a difference to zero). It is the analytic backbone underneath every "the solution exists on the whole interval" statement in the theory of connections, geodesics, and flows. The recognisable trigger is a quantity controlled by its own running integral — "$\phi(t)$ is bounded by a constant plus the accumulated history $\int_0^t\kappa\phi$" — which is exactly the shape produced by integrating a differential inequality.

**Assumption pattern.** Two hypotheses do all the work and each is used once. *Continuity of $A$* gives a finite bound $M:=\lVert A\rVert_{C^0}$ on the compact interval; this single number both drives the geometric decay of the Picard increments (guaranteeing convergence on all of $[0,L]$, not just a short subinterval) and supplies the multiplier $\kappa\equiv M$ in the Grönwall step. *Linearity* is what makes the Picard scheme converge globally: the increment bound is $\lVert v_{k+1}-v_k\rVert\le\lVert v_0\rVert(ML)^{k+1}/(k+1)!$, whose sum is $\lVert v_0\rVert(e^{ML}-1)<\infty$ regardless of how large $L$ is, so there is no shrinking radius of convergence — the phenomenon that for nonlinear equations forces one to patch local solutions and worry about escape.

**Theorem routing.** For **uniqueness**: given two solutions, subtract to get $u=v-w$ with $u(t)=-\int_0^t A u$; bound $\lVert u(t)\rVert\le\int_0^t M\lVert u(s)\rVert\,ds$; apply Grönwall with $C=0$ to force $u\equiv0$. For **existence**: recast as the integral equation, run Picard iteration $v_{k+1}=v_0-\int_0^t A v_k$, prove the increment bound by induction, sum by the Weierstrass comparison to get a uniform limit $v$, and pass to the limit under the integral (licensed by uniform convergence and the fixed bound $M$) to see that $v$ solves the integral equation, hence the differential equation, on all of $[0,L]$.

**Key decision point.** The decisive structural choice is to prove Grönwall through the **integrating-factor trick** applied to the *running bound* $R(t):=C+\int_0^t\kappa\phi$, rather than trying to iterate the inequality into an infinite series by hand. One notes $R'=\kappa\phi\le\kappa R$ (because $\phi\le R$ and $\kappa\ge0$), so $\big(R\,e^{-\int_0^t\kappa}\big)'\le0$; monotonicity of this single auxiliary function delivers the exponential bound in three lines. The second decision — using Grönwall with $C=0$ for uniqueness — is what makes uniqueness a one-line corollary of the very inequality proved for existence's a-priori control, so the two halves of the ODE theorem share one tool.

---

# Legal Operations Used

This solution deploys the following operations, whose general forms are recorded on the chapter topic page's Legal Operations list; here we name each descriptively and show how it is applied.

1. **Replace a differential problem by its equivalent integral equation.** By the fundamental theorem of calculus, $\dot v=-Av$, $v(0)=v_0$ is equivalent to $v(t)=v_0-\int_0^t Av$; the integral form is stable under uniform limits and is what the iteration acts on.

2. **Bound an operator action by the operator norm.** At every step we use $|A(s)x|\le\lVert A(s)\rVert\,|x|\le M\,|x|$ to convert matrix estimates into scalar ones.

3. **Convert a running-integral bound into an exponential bound (Grönwall).** The self-referential estimate $\phi\le C+\int_0^t\kappa\phi$ is closed into the explicit $\phi\le Ce^{\int\kappa}$ by the integrating-factor argument on the running bound.

4. **Iterate a contraction-like map and sum by Weierstrass comparison.** The Picard increments are dominated by the terms of $\lVert v_0\rVert\sum(ML)^{k+1}/(k+1)!$, a convergent series of constants, giving uniform (hence global) convergence.

5. **Interchange limit and integral under a uniform bound.** Because $v_k\to v$ uniformly and $\lVert A\rVert\le M$, the integrals $\int_0^t Av_k$ converge to $\int_0^t Av$, so the limit satisfies the integral equation.

6. **Extract uniqueness from Grönwall with zero constant.** Setting $C=0$ turns the exponential bound into $\phi\equiv0$, collapsing the difference of two solutions to zero.

---

# Hints

> [!note]- Hint 1
> For Grönwall, do not try to iterate $\phi\le C+\int_0^t\kappa\phi$ into a series. Instead introduce the *right-hand side itself* as a new function, $R(t)=C+\int_0^t\kappa(s)\phi(s)\,ds$. It is differentiable (its integrand is continuous). What is $R'(t)$, and how does the hypothesis $\phi\le R$ let you bound it?

> [!note]- Hint 2
> You should find $R'(t)=\kappa(t)\phi(t)\le\kappa(t)R(t)$. That is a differential inequality of the form $R'\le\kappa R$. Multiply by the integrating factor $e^{-\int_0^t\kappa}$ and recognise the left side as an exact derivative. Which way does that derivative point?

> [!note]- Hint 3
> For **uniqueness**, suppose $v$ and $w$ both solve the problem with the same $v_0$. Look at $u=v-w$. Its initial value is $0$ and it satisfies the integral equation with no constant term: $u(t)=-\int_0^t A(s)u(s)\,ds$. Bound $\lVert u(t)\rVert$ and feed it into Grönwall with $C=0$.

> [!note]- Hint 4
> For **existence**, set $v_0(t)\equiv v_0$ and $v_{k+1}(t)=v_0-\int_0^t A v_k$. Prove by induction that $\lVert v_{k+1}(t)-v_k(t)\rVert\le\lVert v_0\rVert\,(Mt)^{k+1}/(k+1)!$ with $M=\lVert A\rVert_{C^0}$. Sum a telescoping series to see that $(v_k)$ is uniformly Cauchy on all of $[0,L]$; its limit solves the integral equation. Nothing here is local — the factorial in the denominator beats $(ML)^{k+1}$ for any $L$.

---

# Solution

The plan has three movements. First, Grönwall's inequality is proved by turning the self-referential integral bound into a differential inequality for its own running integral and killing it with an integrating factor. Second, uniqueness is read off Grönwall with vanishing constant. Third, existence on the whole interval is produced by Picard iteration, whose increments decay factorially and therefore sum uniformly on $[0,L]$, with the limit shown to solve the integral equation. Throughout, $M:=\lVert A\rVert_{C^0}=\max_{[0,L]}\lVert A(t)\rVert<\infty$ and $|\cdot|$ is the Euclidean norm on $\mathbb{K}^n$, extended to $\lVert\cdot\rVert$ as the operator norm on matrices.

**Step 1: Grönwall's inequality.**

Under the hypotheses $\phi,\kappa\ge0$ continuous, $C\ge0$, and $\phi(t)\le C+\int_0^t\kappa\phi$, one has $\phi(t)\le C\exp\!\big(\int_0^t\kappa\big)$.

> [!note]- Derivation
> Define the running bound
> $$R(t):=C+\int_0^t\kappa(s)\phi(s)\,ds,\qquad t\in[0,L].$$
> Its integrand $\kappa\phi$ is continuous (product of continuous functions), so by the fundamental theorem of calculus $R$ is continuously differentiable with
> $$R'(t)=\kappa(t)\phi(t)\qquad\text{(fundamental theorem of calculus).}$$
> The hypothesis is exactly $\phi(t)\le R(t)$. Since $\kappa(t)\ge0$, multiplying the inequality $\phi(t)\le R(t)$ by $\kappa(t)$ preserves its direction, giving
> $$R'(t)=\kappa(t)\phi(t)\le\kappa(t)R(t)\qquad(\phi\le R\text{ and }\kappa\ge0).$$
> **Apply the integrating factor.** Let $\mu(t):=\exp\!\big(-\int_0^t\kappa(s)\,ds\big)>0$, so $\mu'(t)=-\kappa(t)\mu(t)$. Consider $G(t):=R(t)\mu(t)$. Then
> $$G'(t)=R'(t)\mu(t)+R(t)\mu'(t)=\big(R'(t)-\kappa(t)R(t)\big)\mu(t)\le0\qquad(\mu>0\text{ and }R'-\kappa R\le0\text{ from the previous line}).$$
> Hence $G$ is nonincreasing on $[0,L]$, so $G(t)\le G(0)$. But $G(0)=R(0)\mu(0)=C\cdot1=C$ (since $R(0)=C$ and $\mu(0)=e^0=1$). Therefore
> $$R(t)\mu(t)\le C\quad\Longrightarrow\quad R(t)\le C\,\mu(t)^{-1}=C\exp\!\Big(\int_0^t\kappa(s)\,ds\Big).$$
> Combining with $\phi(t)\le R(t)$,
> $$\phi(t)\le C\exp\!\Big(\int_0^t\kappa(s)\,ds\Big),$$
> which is the assertion. Note that when $C=0$ the bound reads $\phi(t)\le0$; together with $\phi\ge0$ this forces $\phi\equiv0$.

**Step 2: Uniqueness of solutions.**

Two $C^1$ solutions of $\dot v=-A(t)v$ with the same initial value coincide on all of $[0,L]$.

> [!note]- Derivation
> Suppose $v,w\colon[0,L]\to\mathbb{K}^n$ are $C^1$ and both satisfy $\dot v=-Av$, $\dot w=-Aw$, and $v(0)=w(0)=v_0$. Set $u:=v-w$. By linearity $\dot u=-A(t)u$ and $u(0)=0$, so, integrating (fundamental theorem of calculus),
> $$u(t)=-\int_0^t A(s)\,u(s)\,ds.$$
> Take norms and use $|A(s)u(s)|\le\lVert A(s)\rVert\,|u(s)|\le M|u(s)|$ together with the triangle inequality for integrals $\big|\int_0^t f\big|\le\int_0^t|f|$:
> $$|u(t)|\le\int_0^t|A(s)u(s)|\,ds\le\int_0^t M\,|u(s)|\,ds\qquad(\text{operator-norm bound; }\lVert A\rVert\le M).$$
> This is the Grönwall hypothesis with $\phi(t):=|u(t)|$ (continuous and $\ge0$), $\kappa\equiv M\ge0$, and constant $C=0$. By **Step 1** with $C=0$,
> $$|u(t)|\le0\cdot\exp(Mt)=0\qquad\text{for all }t\in[0,L].$$
> Hence $u(t)=0$, i.e. $v(t)=w(t)$, for every $t\in[0,L]$. Uniqueness is established.

**Step 3: Existence on the whole interval by Picard iteration — the increment bound.**

Define $v_0(t):=v_0$ and $v_{k+1}(t):=v_0-\int_0^t A(s)v_k(s)\,ds$. Then $\lVert v_{k+1}(t)-v_k(t)\rVert\le|v_0|\,(Mt)^{k+1}/(k+1)!$ for all $k\ge0$ and $t\in[0,L]$.

> [!note]- Derivation
> Each $v_k$ is continuous on $[0,L]$: $v_0$ is constant, and if $v_k$ is continuous then $t\mapsto\int_0^t Av_k$ is continuous (indeed $C^1$), so $v_{k+1}$ is continuous. We prove the bound by induction on $k$, writing $|\cdot|$ for the Euclidean norm of the vector-valued differences.
>
> **Base case $k=0$.** Using $|A(s)v_0|\le M|v_0|$,
> $$|v_1(t)-v_0(t)|=\Big|{-}\int_0^t A(s)v_0\,ds\Big|\le\int_0^t|A(s)v_0|\,ds\le\int_0^t M|v_0|\,ds=M|v_0|\,t=|v_0|\frac{(Mt)^1}{1!}.$$
>
> **Inductive step.** Assume $|v_k(t)-v_{k-1}(t)|\le|v_0|\,(Mt)^k/k!$ for all $t$. By linearity of the iteration,
> $$v_{k+1}(t)-v_k(t)=-\int_0^t A(s)\big(v_k(s)-v_{k-1}(s)\big)\,ds,$$
> so, using $|A(s)(v_k-v_{k-1})(s)|\le M\,|v_k(s)-v_{k-1}(s)|$ and the inductive hypothesis,
> $$|v_{k+1}(t)-v_k(t)|\le\int_0^t M\,|v_k(s)-v_{k-1}(s)|\,ds\le\int_0^t M\cdot|v_0|\frac{(Ms)^k}{k!}\,ds=|v_0|\frac{M^{k+1}}{k!}\int_0^t s^k\,ds.$$
> Since $\int_0^t s^k\,ds=t^{k+1}/(k+1)$,
> $$|v_{k+1}(t)-v_k(t)|\le|v_0|\frac{M^{k+1}}{k!}\cdot\frac{t^{k+1}}{k+1}=|v_0|\frac{(Mt)^{k+1}}{(k+1)!},$$
> completing the induction.

**Step 4: Uniform convergence of the Picard sequence on all of $[0,L]$.**

The sequence $(v_k)$ converges uniformly on $[0,L]$ to a continuous limit $v$.

> [!note]- Derivation
> Write the telescoping identity $v_k=v_0+\sum_{j=0}^{k-1}(v_{j+1}-v_j)$. By **Step 3**, for every $t\in[0,L]$,
> $$|v_{j+1}(t)-v_j(t)|\le|v_0|\frac{(Mt)^{j+1}}{(j+1)!}\le|v_0|\frac{(ML)^{j+1}}{(j+1)!}=:M_j,$$
> a bound independent of $t$. The series of constants $\sum_{j\ge0}M_j=|v_0|\sum_{j\ge0}\frac{(ML)^{j+1}}{(j+1)!}=|v_0|\big(e^{ML}-1\big)$ converges (it is the exponential series). By the Weierstrass comparison test, the series $\sum_{j\ge0}(v_{j+1}-v_j)$ converges **uniformly** on $[0,L]$; equivalently the partial sums $v_k$ form a uniformly Cauchy sequence. Since $\big(C^0([0,L];\mathbb{K}^n),\lVert\cdot\rVert_{C^0}\big)$ is complete, the uniform limit
> $$v(t):=\lim_{k\to\infty}v_k(t)$$
> exists and is continuous on $[0,L]$. Crucially the bound $\sum M_j=|v_0|(e^{ML}-1)$ is finite for **any** $L$, however large: there is no shrinking radius of convergence, so the limit is defined on the entire interval at once.

**Step 5: The limit solves the equation on all of $[0,L]$.**

The continuous limit $v$ satisfies the integral equation $v(t)=v_0-\int_0^t Av$, hence is $C^1$ and solves $\dot v=-A(t)v$, $v(0)=v_0$.

> [!note]- Derivation
> Fix $t\in[0,L]$. In the defining relation $v_{k+1}(t)=v_0-\int_0^t A(s)v_k(s)\,ds$ we pass to the limit $k\to\infty$. The left side tends to $v(t)$. For the right side, estimate the error of replacing $v_k$ by $v$ under the integral:
> $$\Big|\int_0^t A(s)v_k(s)\,ds-\int_0^t A(s)v(s)\,ds\Big|\le\int_0^t|A(s)\big(v_k(s)-v(s)\big)|\,ds\le\int_0^t M\,|v_k(s)-v(s)|\,ds\le ML\,\lVert v_k-v\rVert_{C^0},$$
> using the operator-norm bound and then bounding the integrand by its supremum over $[0,L]$. By **Step 4**, $\lVert v_k-v\rVert_{C^0}\to0$, so the right side tends to $0$; this is exactly the uniform-convergence licence to interchange limit and integral. Therefore $\int_0^t Av_k\to\int_0^t Av$, and passing to the limit in the iteration gives
> $$v(t)=v_0-\int_0^t A(s)\,v(s)\,ds.$$
> The right-hand side has a continuous integrand $A v$, so by the fundamental theorem of calculus $v$ is $C^1$ with $\dot v(t)=-A(t)v(t)$; and $v(0)=v_0-\int_0^0Av=v_0$. Thus $v$ is a $C^1$ solution defined on all of $[0,L]$.

> [!note]- Complete formal solution
> **Grönwall.** Let $\phi,\kappa\colon[0,L]\to[0,\infty)$ be continuous, $C\ge0$, and $\phi(t)\le C+\int_0^t\kappa\phi$ for all $t$. Put $R(t)=C+\int_0^t\kappa\phi$; then $R\in C^1$ with $R'=\kappa\phi\le\kappa R$ (as $\phi\le R$, $\kappa\ge0$). With $\mu(t)=e^{-\int_0^t\kappa}$ one has $(R\mu)'=(R'-\kappa R)\mu\le0$, so $R(t)\mu(t)\le R(0)\mu(0)=C$, whence $\phi(t)\le R(t)\le Ce^{\int_0^t\kappa}$. When $C=0$, $\phi\equiv0$.
>
> **Existence.** Let $A\colon[0,L]\to\operatorname{Mat}(n\times n;\mathbb{K})$ be continuous, $M=\max_{[0,L]}\lVert A\rVert<\infty$, and $v_0\in\mathbb{K}^n$. Define $v_0(t)\equiv v_0$ and $v_{k+1}(t)=v_0-\int_0^t Av_k$. By induction $|v_{k+1}(t)-v_k(t)|\le|v_0|(Mt)^{k+1}/(k+1)!$: the base case is $|{-}\int_0^t Av_0|\le M|v_0|t$, and the step follows from $v_{k+1}-v_k=-\int_0^t A(v_k-v_{k-1})$ with $\int_0^t s^k\,ds=t^{k+1}/(k+1)$. Since $\sum_j|v_0|(ML)^{j+1}/(j+1)!=|v_0|(e^{ML}-1)<\infty$, the telescoping series $v_0+\sum_j(v_{j+1}-v_j)$ converges uniformly on $[0,L]$ (Weierstrass comparison), so $v_k\to v$ uniformly with $v$ continuous. Because $|\int_0^t A(v_k-v)|\le ML\lVert v_k-v\rVert_{C^0}\to0$, passing to the limit gives $v(t)=v_0-\int_0^t Av$; by the fundamental theorem of calculus $v\in C^1$, $\dot v=-Av$, $v(0)=v_0$. The solution is defined on the whole of $[0,L]$.
>
> **Uniqueness.** If $v,w$ are two such solutions, $u=v-w$ satisfies $u(0)=0$ and $u(t)=-\int_0^t Au$, so $|u(t)|\le\int_0^t M|u(s)|\,ds$. Grönwall with $C=0$, $\kappa\equiv M$ gives $|u|\equiv0$, so $v=w$. $\blacksquare$

> [!warning] Illegal but tempting: quoting Picard–Lindelöf for the whole interval
> The tempting shortcut is to say "the right-hand side $f(t,v)=-A(t)v$ is continuous in $t$ and (locally) Lipschitz in $v$, so Picard–Lindelöf gives a solution — done." Picard–Lindelöf in its standard form gives a solution only on a subinterval whose length is controlled by a bound on $f$ on a *box* around the initial point, and a naive continuation could in principle escape to infinity before reaching $t=L$. What rescues the linear case is precisely the *global* Lipschitz constant $M=\lVert A\rVert_{C^0}$ valid on all of $[0,L]\times\mathbb{K}^n$, which makes the Picard increments decay like $(Mt)^{k+1}/(k+1)!$ with a factorial that defeats any interval length. The extra condition that legalises "one shot on all of $[0,L]$" is exactly this: the coefficient is bounded on the whole interval, which linearity supplies for free but which a general nonlinear $f$ need not. This is the content of Remark 2.6.2 in the source: the interval-wide existence "is not apparent from the usual Picard–Lindelöf theorem," and for matrix groups it follows because the lift equation is linear.

> [!note]- Independent sanity check: the scalar case
> For $n=1$ and $A(t)=a(t)$ real-valued, the equation $\dot v=-a(t)v$ has the elementary closed-form solution $v(t)=v_0\exp\!\big(-\int_0^t a\big)$, defined on all of $[0,L]$ and manifestly unique. Our general bound $|v(t)|\le|v_0|e^{\int_0^t|a|}$ (Grönwall applied to $|v(t)|\le|v_0|+\int_0^t|a||v|$) is consistent with $|v(t)|=|v_0|e^{-\int_0^t a}\le|v_0|e^{\int_0^t|a|}$, and the Picard series $v_0\sum_k(-\int_0^t a)^k/k!$ is exactly the Taylor series of $v_0e^{-\int_0^t a}$. The abstract machinery reproduces the answer one already knows in one dimension.

---

# Key Takeaways

**Grönwall's inequality is the universal device that turns a self-referential integral bound into an explicit exponential one, and its proof is a single integrating-factor line.** The pattern to internalise is: whenever a nonnegative quantity is bounded by a constant plus its own accumulated integral, $\phi(t)\le C+\int_0^t\kappa\phi$, it is automatically bounded by $Ce^{\int_0^t\kappa}$. The proof never iterates the inequality; it names the running bound $R=C+\int_0^t\kappa\phi$, observes $R'\le\kappa R$, and multiplies by $e^{-\int\kappa}$ so the product is monotone. The trigger for reaching for Grönwall is the appearance of the accumulated-history term $\int_0^t\kappa\phi$; the diagnostic payoff is twofold — with $C>0$ it forbids finite-time blow-up (the quantity can grow at most exponentially), and with $C=0$ it forces the quantity to vanish identically, which is the standard route to uniqueness and to continuous dependence on data. This one lemma underlies the completeness of geodesics, the well-posedness of the flow of a vector field in [[Thm - Existence and Uniqueness of Integral Curves|the integral-curve theorem]], and the stability estimates of the entire theory of connections.

**Linearity is what makes existence global rather than merely local: the Lipschitz constant is uniform on the whole interval.** For a general nonlinear system, Picard–Lindelöf yields a solution only on a short interval, and one must argue separately that the maximal solution does not escape to infinity before the interval ends. A linear system $\dot v=-A(t)v$ escapes this bookkeeping because its Lipschitz constant in $v$ is the *fixed* number $M=\lVert A\rVert_{C^0}$, valid uniformly over all of $[0,L]$ and all of $\mathbb{K}^n$. The Picard increments then decay like $(ML)^{k+1}/(k+1)!$, whose factorial denominator beats the numerator for every interval length, so the iteration converges uniformly in one shot. The transferable recognition is that "global existence for linear systems" is not a deep theorem but a consequence of a bounded coefficient plus a convergent exponential series; when a problem reduces to a linear equation with continuous (hence bounded, on a compact interval) coefficients, one may assert existence on the entire interval without any continuation argument. This is exactly why the horizontal-lift theorem's matrix-group case needs no separate blow-up analysis, whereas its general-group case must instead run the maximality-and-extension argument of Remark 2.6.2.

**Existence and uniqueness for a linear system are two faces of the same estimate.** The striking economy of this circle of ideas is that a single inequality serves both halves of the fundamental theorem of ordinary differential equations. The Picard increment bound that proves existence, $\lVert v_{k+1}-v_k\rVert\le|v_0|(Mt)^{k+1}/(k+1)!$, and the uniqueness argument, $|u(t)|\le\int_0^t M|u|$, are both instances of "the growth of a quantity is controlled by its own integral against the bounded coefficient $M$." Grönwall packages that control; setting $C=0$ specialises it to uniqueness, while summing the increments specialises it to existence. When returning to this material after time, the reconstruction hinges on remembering just the operator-norm bound $|A(s)x|\le M|x|$ and the integrating-factor proof of Grönwall — everything else is forced. The same estimate, applied to the difference of a solution and its perturbation, gives continuous dependence on the initial datum and on the coefficient $A$, which is what makes parallel transport a *continuous* (indeed smooth) function of the connection, the fact that underlies the whole moduli-theoretic picture of later chapters.
