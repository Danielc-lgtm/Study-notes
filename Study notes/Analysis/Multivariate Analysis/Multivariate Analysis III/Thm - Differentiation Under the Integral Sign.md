---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - The Riemann Integral in Several Variables"
  - "Thm - Fubini's Theorem"
tags: [analysis, multivariate-analysis]
---

# Notation

$R \subseteq \mathbb{R}^n$ is a [[Def - The Riemann Integral in Several Variables|cell]] (often an interval $[a,b]$); $t$ ranges over an open interval $J$, the **parameter**. A function $f : R \times J \to \mathbb{R}$, $(x,t) \mapsto f(x,t)$, has **partial derivative in the parameter** $\frac{\partial f}{\partial t}(x,t) = \partial_t f(x,t)$. The **parameter integral** is $F(t) = \int_R f(x,t)\,dx$. A function $M : R \to \mathbb{R}$ **dominates** $\partial_t f$ if $|\partial_t f(x,t)| \leq M(x)$ for all $x, t$, with $\int_R M < \infty$. For variable limits, $a(t), b(t)$ are differentiable real-valued functions. The full symbol registry is on [[Multivariate Analysis III — Integration in Several Variables]].

---

# Statement

> **Differentiation Under the Integral Sign.** Let $R \subseteq \mathbb{R}^n$ be a cell, $J$ an open interval, and $f : R \times J \to \mathbb{R}$ such that $f(\cdot, t)$ is integrable for each $t$, the partial derivative $\partial_t f$ exists on $R \times J$, and either (a) $R$ is compact and $\partial_t f$ is continuous on $R \times J$, or (b) there is an integrable $M : R \to \mathbb{R}$ with $|\partial_t f(x,t)| \leq M(x)$ for all $(x,t)$. Then $F(t) = \int_R f(x,t)\,dx$ is differentiable on $J$ and
> $$F'(t) = \int_R \frac{\partial f}{\partial t}(x,t)\,dx.$$
>
> **Leibniz rule (variable limits).** If additionally $a, b : J \to \mathbb{R}$ are differentiable and $f(\cdot, t)$ is continuous, then $F(t) = \int_{a(t)}^{b(t)} f(x,t)\,dx$ satisfies
> $$F'(t) = \int_{a(t)}^{b(t)} \frac{\partial f}{\partial t}(x,t)\,dx \;+\; f\big(b(t),t\big)\,b'(t) \;-\; f\big(a(t),t\big)\,a'(t).$$

---

# Motivation

Many quantities in mathematics and physics are integrals that carry a parameter — a temperature, a time, a coupling constant — and the natural question is how the quantity *changes* as the parameter changes. The integral $F(t) = \int_R f(x,t)\,dx$ is a function of $t$, and one wants $F'(t)$.

The hopeful guess is that the derivative simply passes through the integral sign: $F'(t) = \int_R \partial_t f(x,t)\,dx$. This would be enormously useful, because differentiating the integrand $f$ in the parameter often produces something far simpler than $f$ itself — and that is exactly the basis of a famous problem-solving technique. Faced with a definite integral you cannot evaluate, you *introduce* a parameter $t$, differentiate $F$ with respect to it, find that $F'(t)$ is a tractable integral, solve the resulting differential equation for $F$, and fix the constant of integration by a value of $F$ you do know. Richard Feynman popularized this trick, and it turns whole classes of otherwise-impossible integrals — $\int_0^\infty \frac{\sin x}{x}\,dx$, $\int_0^\infty \frac{e^{-ax}-e^{-bx}}{x}\,dx$ — into routine calculus.

But the move "differentiate under the integral sign" is an *interchange of two limiting operations*. The derivative $F'(t)$ is a limit of difference quotients; the integral $\int_R$ is a limit of sums. Passing the derivative inside swaps the order in which these two limits are taken, and like every interchange of limits, it can fail. The theorem identifies the exact hypothesis that licenses the swap — continuity of $\partial_t f$, or more generally a fixed integrable dominating function for $\partial_t f$ — and the failure mode it rules out is mass escaping to infinity or concentrating: a family of bumps whose total integral stays constant while the integrand's derivative grows unboundedly.

There is also the case where the *limits of integration* themselves depend on the parameter, $F(t) = \int_{a(t)}^{b(t)} f(x,t)\,dx$. Then differentiating picks up two extra boundary terms — this is the full **Leibniz integral rule** — and the boundary terms are exactly what the one-variable fundamental theorem of calculus contributes as the endpoints move.

Differentiation under the integral sign is, structurally, the close cousin of [[Thm - Fubini's Theorem|Fubini's theorem]]: Fubini commutes two integrals, this commutes a derivative and an integral. Both are licensed by a control hypothesis, both fail without it, and the Leibniz rule can in fact be *deduced* from Fubini.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\partial_t f$ exists and is suitably controlled — continuous on a compact parameter range, or dominated by a fixed integrable $M(x)$". The skill is recognizing this control from the structure of $f$.

The first disguised source is **$f$ is jointly continuous and $C^1$ in the parameter, on a compact region**. The property $B$ is "$f$ and $\partial_t f$ are continuous on $R \times [t_0, t_1]$". The bridge: a continuous function on a compact set is bounded, so $\partial_t f$ is automatically dominated by the constant $M = \sup|\partial_t f|$, which is integrable over the bounded cell $R$. The non-obvious part is that joint continuity *alone*, on a compact domain, supplies the domination for free — no separate bound need be exhibited. *Example problem:* differentiate $F(t) = \int_0^1 \cos(tx)\,dx$; the integrand is smooth, $R$ is compact, the rule applies with no further checking.

The second disguised source is **the integrand decays exponentially in $x$, uniformly for $t$ in a range**. The property $B$ is "$|\partial_t f(x,t)| \leq C\,e^{-c|x|}$ for all $t$ near $t_0$". The bridge: the exponential $C e^{-c|x|}$ is integrable over $\mathbb{R}^n$, so it serves as the dominating function $M$. The non-obviousness is that on an *unbounded* domain domination is the real hypothesis (continuity is not enough), and exponential decay is the most common way it is met. *Example problem:* differentiate $\int_0^\infty e^{-tx} g(x)\,dx$ — a Laplace transform — with respect to $t > 0$. See [[Ex - A parameter integral by differentiation under the integral sign]].

The third disguised source is **the parameter can be artificially introduced into a parameter-free integral**. The property $B$ is "a target integral $I$ can be written $I = F(t_1)$ for a well-chosen family $F(t) = \int f(x,t)\,dx$ with a tractable $\partial_t f$". The bridge is the Feynman trick: you *manufacture* the parameter so that differentiation simplifies the integrand. The non-obviousness is that the theorem's applicability is something you *create*, not something you find. *Example problem:* evaluate $\int_0^1 \frac{x-1}{\ln x}\,dx$ by writing it as $\int_0^1 \int_0^1 x^t\,dt\,dx$ and recognizing the inner structure.

**Targets (Output Amplification)**

The conclusion is "$F'(t) = \int_R \partial_t f(x,t)\,dx$" (plus boundary terms with variable limits).

Combine the conclusion with **a separable differential equation for $F$**. After differentiating, $F'(t)$ is often an elementary function of $t$, or proportional to $F(t)$ itself. The further result $E$: integrate the differential equation to recover $F$ in closed form, then fix the constant with a known value $F(t_0)$. This is the Feynman trick's payoff and is non-obvious because it relocates the difficulty from *integrating in $x$* (hard) to *solving an ODE in $t$* (often easy).

Combine the conclusion with **iteration to higher derivatives**. Re-applying the rule gives $F^{(k)}(t) = \int_R \partial_t^k f(x,t)\,dx$. The further result $E$: a power-series or moment expansion of $F$, since $F^{(k)}(t_0)$ are the Taylor coefficients. Applied to $F(t) = \int e^{-tx^2}\,dx$, the derivatives generate the Gaussian moments $\int x^{2k} e^{-x^2}\,dx$. This is non-obvious because one differentiation under the integral, iterated, becomes a generating-function machine.

Combine the conclusion with **the boundary terms of the Leibniz rule**. With variable limits, $F'(t) = \int_{a(t)}^{b(t)} \partial_t f\,dx + f(b(t),t) b'(t) - f(a(t),t) a'(t)$. The further result $E$: differentiating quantities whose *domain* moves — the time-derivative of an integral over a moving region, the **Reynolds transport theorem** of fluid mechanics. This is non-obvious because the boundary terms, which look like a technical correction, are precisely the physical flux through the moving boundary.

---

# Why Is It True

Strip the statement to its skeleton. The derivative $F'(t)$ is, by definition, the limit of difference quotients:
$$F'(t) = \lim_{h \to 0} \frac{F(t+h) - F(t)}{h} = \lim_{h \to 0} \int_R \frac{f(x, t+h) - f(x,t)}{h}\,dx.$$
The integrand inside is a difference quotient of $f$ in the parameter, and for each fixed $x$ it converges, as $h \to 0$, to $\partial_t f(x,t)$. So the question "$F'(t) = \int_R \partial_t f$?" is *exactly* the question "may the limit $h \to 0$ be moved inside the integral?". The theorem is one specific instance of the eternal analysis question: when does $\lim \int = \int \lim$?

That reframing tells you both why it should be true and why it needs a hypothesis. It should be true because the difference quotient $\frac{f(x,t+h)-f(x,t)}{h}$ is, by the mean value theorem, equal to $\partial_t f(x, \tau)$ for some $\tau$ between $t$ and $t+h$ — it is not some wild new function, it is just the derivative $\partial_t f$ evaluated at a slightly shifted parameter. If $\partial_t f$ is well-behaved, the difference quotient stays close to $\partial_t f(x,t)$ uniformly in $x$, the convergence inside the integral is uniform, and uniform convergence is exactly what permits passing a limit through an integral. On a compact domain with $\partial_t f$ continuous, this uniformity is automatic, and the theorem holds with nothing to check.

It needs a hypothesis because on a non-compact domain the convergence need not be uniform — and then mass can escape. Picture difference quotients that, as $h \to 0$, develop a tall thin spike traveling off to infinity in $x$: each individual integrand converges pointwise to $\partial_t f$, but the spike carries a fixed chunk of integral that the pointwise limit does not see. The integral of the limit then misses that chunk, and $\frac{d}{dt}\int \neq \int \frac{\partial}{\partial t}$. The dominating function $M(x)$ is the barrier against this: if every difference quotient is pinned below a fixed integrable $M$, no spike can grow, no mass can escape, and the interchange is legal. This is the same mechanism — and the same fix — as in the dominated convergence theorem; domination is the universal anti-escape hypothesis.

The boundary terms in the variable-limit case have an equally clean explanation. Write $F(t) = \int_{a(t)}^{b(t)} f(x,t)\,dx$ as a function of three things — the parameter $t$ inside the integrand, the upper limit $b(t)$, the lower limit $a(t)$ — and differentiate by the chain rule. The dependence through the integrand gives $\int \partial_t f$, by the fixed-limit case. The dependence through the upper limit gives, by the fundamental theorem of calculus, $f(b(t),t)\,b'(t)$ — the rate at which area is gained as the right endpoint moves. The dependence through the lower limit gives $-f(a(t),t)\,a'(t)$ — area lost at the left. The boundary terms are not corrections; they are the fundamental theorem of calculus accounting for the moving endpoints.

---

# What Makes This Hard

The single non-obvious point is that this is an **interchange of limits**, not an algebraic manipulation: $F'(t) = \int \partial_t f$ is the assertion $\lim_{h\to 0}\int = \int\lim_{h\to 0}$, and it is *false* without a uniformity or domination hypothesis. The most common error is to differentiate under the integral sign reflexively on an unbounded domain where $\partial_t f$ is continuous but *not dominated* — continuity alone suffices on a compact domain but not on $\mathbb{R}^n$, and the failure mode (a spike of integral escaping to infinity) is invisible if one only checks pointwise convergence. A second frequent slip, in the variable-limit case, is to forget the boundary terms $f(b,t)b' - f(a,t)a'$ entirely, or to get their signs wrong — the lower limit contributes with a minus sign.

---

# Rederivation Scaffold

**High-level strategy:**
Write $F'(t)$ as the limit of difference quotients of $F$, which is the integral of difference quotients of $f$. By the mean value theorem each difference quotient equals $\partial_t f$ at a shifted parameter; domination plus continuity of $\partial_t f$ make the convergence to $\partial_t f(x,t)$ uniform (compact case) or dominated (general case), licensing the limit to pass inside. For variable limits, split $F$ into a fixed-limit part and endpoint parts and apply the chain rule and the fundamental theorem of calculus.

**Subgoal decomposition:**

1. **Reduce to an interchange of limits.** Show $\frac{F(t+h)-F(t)}{h} = \int_R \frac{f(x,t+h)-f(x,t)}{h}\,dx$ and that the integrand converges pointwise to $\partial_t f(x,t)$ as $h \to 0$.
   - *Hint:* Linearity of the integral; definition of $\partial_t f$.
   - *Why needed:* It identifies the theorem as the question "may $\lim_{h\to 0}$ pass inside $\int$".

2. **Control the difference quotient.** By the mean value theorem, $\frac{f(x,t+h)-f(x,t)}{h} = \partial_t f(x, \tau_{x,h})$ for some $\tau_{x,h}$ between $t$ and $t+h$. Hence $|\frac{f(x,t+h)-f(x,t)}{h}| \leq M(x)$ if $|\partial_t f| \leq M$.
   - *Hint:* Apply the one-variable mean value theorem to $t \mapsto f(x,t)$ for each fixed $x$.
   - *Why needed:* It produces a fixed integrable bound on the difference quotients — the domination that forbids escaping mass.

3. **Pass the limit inside.** On a compact domain with $\partial_t f$ continuous, the convergence is uniform, so $\lim_h \int = \int \lim_h$. In general, domination plus the dominated-convergence mechanism gives the same.
   - *Hint:* Uniform continuity of $\partial_t f$ on the compact set $R \times [t-\delta, t+\delta]$ makes $\partial_t f(x,\tau_{x,h}) \to \partial_t f(x,t)$ uniformly in $x$.
   - *Why needed:* It is the actual interchange, yielding $F'(t) = \int_R \partial_t f(x,t)\,dx$.

4. **Variable limits.** Write $\Phi(t, u, v) = \int_u^v f(x,t)\,dx$ and $F(t) = \Phi(t, a(t), b(t))$; differentiate by the chain rule.
   - *Hint:* $\partial_t\Phi = \int_u^v \partial_t f$ (step 3); $\partial_v\Phi = f(v,t)$ and $\partial_u\Phi = -f(u,t)$ (fundamental theorem of calculus).
   - *Why needed:* It assembles the full Leibniz rule with its two boundary terms.

---

# Lemma Decomposition

> [!note]- Lemma 1: The difference quotient is a value of the partial derivative
> **Statement:** If $t \mapsto f(x,t)$ is differentiable on an interval containing $t$ and $t+h$, then for each $x$ there is $\tau$ strictly between $t$ and $t+h$ with $\frac{f(x,t+h) - f(x,t)}{h} = \partial_t f(x, \tau)$.
>
> **Hint:** This is the one-variable mean value theorem applied to the single-variable function $s \mapsto f(x,s)$.
>
> **Why needed:** It shows the difference quotient is not a new object but the partial derivative evaluated at a shifted parameter — which is what makes it controllable by a bound on $\partial_t f$.
>
> > [!note]- Full proof
> > Fix $x$. The function $\phi(s) = f(x,s)$ is differentiable on the closed interval with endpoints $t$ and $t+h$, with $\phi'(s) = \partial_t f(x,s)$. The mean value theorem gives a point $\tau$ strictly between $t$ and $t+h$ such that $\phi(t+h) - \phi(t) = \phi'(\tau)\,h$, that is $f(x,t+h) - f(x,t) = \partial_t f(x,\tau)\,h$. Dividing by $h \neq 0$ yields the claim. In particular, if $|\partial_t f| \leq M(x)$ everywhere, then $\big|\frac{f(x,t+h)-f(x,t)}{h}\big| = |\partial_t f(x,\tau)| \leq M(x)$, a bound uniform in $h$.
>
> [!note]- Lemma 2: Uniform convergence permits passing the limit inside the integral
> **Statement:** If $\varphi_h : R \to \mathbb{R}$ are integrable and $\varphi_h \to \varphi$ uniformly on the cell $R$ as $h \to 0$, with $\varphi$ integrable, then $\int_R \varphi_h \to \int_R \varphi$.
>
> **Hint:** Bound $|\int_R \varphi_h - \int_R \varphi| \leq \int_R |\varphi_h - \varphi| \leq \sup_R|\varphi_h - \varphi| \cdot V(R)$.
>
> **Why needed:** It is the interchange engine for the compact case: uniform convergence of the difference quotients to $\partial_t f$ delivers $F'(t) = \int \partial_t f$.
>
> > [!note]- Full proof
> > By linearity and monotonicity of the integral,
> > $$\Big| \int_R \varphi_h\,dV - \int_R \varphi\,dV \Big| = \Big| \int_R (\varphi_h - \varphi)\,dV \Big| \leq \int_R |\varphi_h - \varphi|\,dV \leq \Big( \sup_R |\varphi_h - \varphi| \Big) V(R).$$
> > Uniform convergence means $\sup_R|\varphi_h - \varphi| \to 0$ as $h \to 0$, and $V(R)$ is a fixed finite constant, so the right side $\to 0$. Hence $\int_R \varphi_h \to \int_R \varphi$. (On an unbounded domain $V(R) = \infty$ and uniform convergence is not enough; one needs a dominating function instead, and the conclusion follows from the dominated-convergence mechanism.)
>
> [!note]- Lemma 3: The fundamental theorem of calculus supplies the boundary terms
> **Statement:** For continuous $f(\cdot, t)$, the function $v \mapsto \int_u^v f(x,t)\,dx$ has derivative $f(v,t)$ in $v$, and $u \mapsto \int_u^v f(x,t)\,dx$ has derivative $-f(u,t)$ in $u$.
>
> **Hint:** The one-variable fundamental theorem of calculus.
>
> **Why needed:** It produces the two endpoint terms $f(b(t),t)b'(t)$ and $-f(a(t),t)a'(t)$ of the full Leibniz rule.
>
> > [!note]- Full proof
> > Fix $t$ and write $g(x) = f(x,t)$, continuous. By the fundamental theorem of calculus, the integral function $G(v) = \int_u^v g(x)\,dx$ is differentiable with $G'(v) = g(v) = f(v,t)$. Likewise $\int_u^v g = -\int_v^u g$, so as a function of the lower limit $u$, $\frac{\partial}{\partial u}\int_u^v g(x)\,dx = -g(u) = -f(u,t)$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Fixed limits.** Let $R$ be a cell, $J$ an open interval, and $f : R \times J \to \mathbb{R}$ such that $f(\cdot, t) \in \mathcal{R}(R)$ for each $t$, the partial derivative $\partial_t f$ exists on $R \times J$, and either (a) $R$ is compact and $\partial_t f$ is continuous on $R \times J$, or (b) there is an integrable $M : R \to \mathbb{R}$ with $|\partial_t f(x,t)| \leq M(x)$ for all $(x,t)$. Set $F(t) = \int_R f(x,t)\,dx$. Fix $t \in J$.
>
> For $h \neq 0$ small enough that $t + h \in J$, linearity of the integral gives
> $$\frac{F(t+h) - F(t)}{h} = \int_R \frac{f(x,t+h) - f(x,t)}{h}\,dx =: \int_R \varphi_h(x)\,dx.$$
> By Lemma 1, for each $x$ there is $\tau_{x,h}$ between $t$ and $t+h$ with $\varphi_h(x) = \partial_t f(x, \tau_{x,h})$. As $h \to 0$, $\tau_{x,h} \to t$, so $\varphi_h(x) \to \partial_t f(x,t)$ pointwise.
>
> *Case (a).* Restrict $h$ to $|h| \leq \delta$ with $[t-\delta, t+\delta] \subseteq J$. Then $\partial_t f$ is continuous on the compact set $R \times [t-\delta, t+\delta]$, hence *uniformly* continuous there. Given $\varepsilon > 0$, there is $\delta' > 0$ such that $|\partial_t f(x, s) - \partial_t f(x, t)| < \varepsilon$ whenever $|s - t| < \delta'$, uniformly in $x$. For $|h| < \delta'$, $|\tau_{x,h} - t| < \delta'$, so $|\varphi_h(x) - \partial_t f(x,t)| < \varepsilon$ for all $x$ — that is, $\varphi_h \to \partial_t f(\cdot, t)$ uniformly on $R$. By Lemma 2, $\int_R \varphi_h \to \int_R \partial_t f(x,t)\,dx$. Hence
> $$F'(t) = \lim_{h \to 0} \frac{F(t+h) - F(t)}{h} = \int_R \partial_t f(x,t)\,dx.$$
>
> *Case (b).* By Lemma 1, $|\varphi_h(x)| = |\partial_t f(x,\tau_{x,h})| \leq M(x)$ for all $x$ and all small $h$, with $M$ integrable. The functions $\varphi_h$ converge pointwise to $\partial_t f(\cdot,t)$ and are uniformly dominated by $M$; the dominated-convergence mechanism (no escape of mass past the fixed integrable barrier $M$) yields $\int_R \varphi_h \to \int_R \partial_t f(x,t)\,dx$, and again $F'(t) = \int_R \partial_t f(x,t)\,dx$. The continuity of $\partial_t f$ ensures the limit function is integrable.
>
> **Variable limits (Leibniz rule).** Suppose additionally $a, b : J \to \mathbb{R}$ are differentiable with values in an interval over which $f(\cdot, t)$ is continuous, and set $F(t) = \int_{a(t)}^{b(t)} f(x,t)\,dx$. Define $\Phi(t, u, v) = \int_u^v f(x,t)\,dx$, so $F(t) = \Phi(t, a(t), b(t))$. The three partial derivatives of $\Phi$ are: $\partial_t \Phi = \int_u^v \partial_t f(x,t)\,dx$ by the fixed-limit case; $\partial_v \Phi = f(v,t)$ and $\partial_u \Phi = -f(u,t)$ by Lemma 3. These partials are continuous, so $\Phi$ is differentiable and the chain rule applies:
> $$F'(t) = \partial_t\Phi + \partial_u\Phi \cdot a'(t) + \partial_v\Phi \cdot b'(t) = \int_{a(t)}^{b(t)} \partial_t f(x,t)\,dx + f(b(t),t)\,b'(t) - f(a(t),t)\,a'(t). \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Evaluating an intractable integral by the Feynman trick.** To compute $\int_0^\infty \frac{\sin x}{x}\,dx$, introduce $F(t) = \int_0^\infty e^{-tx}\frac{\sin x}{x}\,dx$. Differentiating in $t$ kills the awkward $1/x$: $F'(t) = -\int_0^\infty e^{-tx}\sin x\,dx = -\frac{1}{1+t^2}$, an elementary integral. Integrate: $F(t) = -\arctan t + C$, fix $C$ by $F(\infty) = 0$, and evaluate $F(0) = \pi/2$. The application is nonobvious because the parameter $e^{-tx}$ is *invented* solely so that differentiation simplifies the integrand — and the domination $|e^{-tx}\sin x| \leq e^{-tx}$ is what makes it legal on the unbounded domain.

**Generating moments of the Gaussian.** From $F(t) = \int_{-\infty}^\infty e^{-tx^2}\,dx = \sqrt{\pi/t}$ (a change-of-variables fact), iterate differentiation under the integral sign in $t$: each $\partial_t$ pulls down a factor $-x^2$, so $F^{(k)}(t) = (-1)^k\int x^{2k} e^{-tx^2}\,dx$, and differentiating the closed form $\sqrt{\pi}\,t^{-1/2}$ gives all the Gaussian moments $\int x^{2k}e^{-x^2}\,dx$ at $t=1$. The application is out-of-distribution because one theorem, iterated, becomes a moment-generating machine; the exponential decay $e^{-tx^2}$ supplies domination uniformly for $t$ in any $[t_0, \infty)$.

**Reynolds transport theorem in fluid mechanics.** The rate of change of a quantity $\int_{\Omega(t)} \rho(x,t)\,dV$ carried in a *moving* region $\Omega(t)$ is, by the multidimensional Leibniz rule, $\int_{\Omega(t)}\partial_t\rho\,dV$ plus a boundary flux term $\int_{\partial\Omega(t)} \rho\,(v\cdot n)\,dS$ accounting for the moving boundary. The application is nonobvious because the boundary terms — a technical correction in the one-variable rule — are here the physically essential flux of material through the deforming surface.

**Smoothness of the gamma and Bessel functions.** The gamma function $\Gamma(s) = \int_0^\infty x^{s-1}e^{-x}\,dx$ is infinitely differentiable on $s > 0$, because $\partial_s^k(x^{s-1}e^{-x}) = (\ln x)^k x^{s-1}e^{-x}$ is dominated, uniformly for $s$ in any compact subinterval, by an integrable function. Differentiation under the integral sign is the tool that proves integral-defined special functions are smooth. The application is nonobvious because "is this function differentiable" for an integral-defined function is exactly a domination check.

---

# Bridges

- **[[Thm - Fubini's Theorem|Fubini's Theorem]]** — the structural sibling. Both theorems commute two limiting operations licensed by a control hypothesis; differentiation under the integral sign can be *derived* from Fubini, by writing $f(x,t) - f(x,t_0) = \int_{t_0}^t \partial_s f(x,s)\,ds$, integrating in $x$, and swapping the $x$ and $s$ integrals.

- **The dominated convergence theorem** — the limit-interchange theorem this one specializes. The domination hypothesis $|\partial_t f| \leq M$ is precisely the dominating-function hypothesis of [[Measure Theory II — §2 Integration|the Lebesgue convergence theorems]]; the difference quotients are the "sequence", $M$ is the "dominating function", and the conclusion is $\lim\int = \int\lim$.

- **The fundamental theorem of calculus** — supplies the boundary terms. In the variable-limit Leibniz rule the endpoint contributions $f(b,t)b' - f(a,t)a'$ are exactly the fundamental theorem of calculus accounting for moving limits of integration.

- **The chain rule** — the variable-limit case is the [[Thm - The Chain Rule|chain rule]] applied to $F(t) = \Phi(t, a(t), b(t))$, decomposing the total $t$-dependence into the dependence through the integrand and through each endpoint.

---

# Unlocked by This

> [!tip] The Feynman Trick *(from Analysis problem-solving)*
> Introducing an auxiliary parameter into a parameter-free integral, differentiating to simplify, solving the resulting differential equation, and specializing is the standard technique for evaluating definite integrals with no elementary antiderivative. See [[Ex - A parameter integral by differentiation under the integral sign]].

> [!tip] Reynolds Transport Theorem *(from Continuum Mechanics)*
> The Leibniz rule for an integral over a moving region is the **Reynolds transport theorem**, the foundation of the differential form of the conservation laws (mass, momentum, energy) in fluid dynamics.
