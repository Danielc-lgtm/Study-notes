---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Dominated Convergence Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space, $U\subseteq\mathbb{R}$ open, and $f:U\times X\to\mathbb{R}$ such that

(i) $x\mapsto f(t,x)$ is $\mu$-integrable for each $t\in U$;
(ii) $t\mapsto f(t,x)$ is differentiable for each $x\in X$;
(iii) there is $g\in L^1(\mu)$ with $\big|\partial_t f(t,x)\big|\le g(x)$ for all $(t,x)$.

Prove that $F(t)=\int_X f(t,x)\,d\mu(x)$ is differentiable on $U$ with
$$F'(t)=\int_X\partial_t f(t,x)\,d\mu(x).$$

Then deduce: the [[Def - Characteristic Function|characteristic function]] $\varphi(t)=\int e^{itx}\,d\mu(x)$ of a measure with finite first moment is differentiable, with $\varphi'(t)=\int ix\,e^{itx}\,d\mu$.

**Recall:**

![[Thm - Dominated Convergence Theorem#Formal Statement]]

---

# Convergent Strategy

**Problem class:** justifying the interchange $\frac{d}{dt}\int=\int\frac{\partial}{\partial t}$.

**Assumption pattern:** a derivative is a *limit of difference quotients*; the difference quotient $\frac{f(t+h_n,x)-f(t,x)}{h_n}$ is a sequence of functions of $x$. By the [[#|mean value theorem]] it equals $\partial_t f(\theta,x)$ for some intermediate $\theta$, hence is dominated by $g$. DCT then passes the limit through.

**Theorem routing:** difference quotient $\to\partial_t f$ pointwise, $|$difference quotient$|\le g\in L^1$ (MVT), DCT $\Rightarrow$ limit of integrals $=$ integral of limit.

**Key decision point:** the MVT is what supplies the *uniform* (in $h$) integrable bound — the hypothesis DCT demands.

---

# Legal Operations Used

1. **Differentiation as a sequential limit** of difference quotients.
2. **Mean value theorem** to bound each difference quotient by $g$.
3. **DCT** to interchange limit and integral.

---

# Hints

> [!note]- Hint 1
> $F'(t)=\lim_{h\to0}\frac{F(t+h)-F(t)}{h}=\lim_h\int\frac{f(t+h,x)-f(t,x)}{h}\,d\mu$. It suffices to handle any sequence $h_n\to0$.

> [!note]- Hint 2
> By the MVT, $\frac{f(t+h_n,x)-f(t,x)}{h_n}=\partial_t f(\theta_{n,x},x)$ for some $\theta_{n,x}$ between $t$ and $t+h_n$. Bound this by $g(x)$.

> [!note]- Hint 3
> The difference quotient $\to\partial_t f(t,x)$ pointwise (hypothesis (ii)) and is $\le g\in L^1$ (MVT + (iii)). Apply DCT.

---

# Solution

**Step 1 — Reduce to a sequence.** Fix $t\in U$. To show $F$ is differentiable at $t$ with the claimed derivative, it suffices to show that for *every* sequence $h_n\to0$ (with $t+h_n\in U$),
$$\frac{F(t+h_n)-F(t)}{h_n}\ \longrightarrow\ \int_X\partial_t f(t,x)\,d\mu(x).$$

**Step 2 — The difference quotient as a dominated sequence.** Define $q_n(x)=\dfrac{f(t+h_n,x)-f(t,x)}{h_n}$. By [[Thm - Properties of the Integral|linearity]], $\frac{F(t+h_n)-F(t)}{h_n}=\int q_n\,d\mu$.

> [!note]- Derivation
> *Pointwise limit:* by hypothesis (ii), $t\mapsto f(t,x)$ is differentiable, so $q_n(x)\to\partial_t f(t,x)$ for every $x$.
> *Domination:* by the mean value theorem applied to $t\mapsto f(t,x)$ on the interval between $t$ and $t+h_n$, there is $\theta_{n,x}$ with $q_n(x)=\partial_t f(\theta_{n,x},x)$. Hypothesis (iii) gives $|q_n(x)|=|\partial_t f(\theta_{n,x},x)|\le g(x)$, with $g\in L^1$ — *uniformly in $n$*.

**Step 3 — Apply DCT.** The sequence $q_n$ is measurable in $x$, converges pointwise to $\partial_t f(t,\cdot)$, and is dominated by $g\in L^1$. By [[Thm - Dominated Convergence Theorem|DCT]],
$$\frac{F(t+h_n)-F(t)}{h_n}=\int q_n\,d\mu\ \longrightarrow\ \int\partial_t f(t,x)\,d\mu(x).$$
As the sequence $h_n\to0$ was arbitrary, $F'(t)=\int\partial_t f(t,x)\,d\mu$. (In particular $\partial_t f(t,\cdot)\in L^1$, being dominated by $g$.)

**Step 4 — Characteristic function.** With $f(t,x)=e^{itx}$, $\partial_t f=ix\,e^{itx}$, so $|\partial_t f(t,x)|=|x|$. If $\mu$ has finite first moment, $g(x)=|x|\in L^1(\mu)$ dominates, and the theorem gives $\varphi'(t)=\int ix\,e^{itx}\,d\mu$. (Iterating: a finite $k$-th moment gives $\varphi$ $k$ times differentiable, $\varphi^{(k)}(0)=i^k\int x^k\,d\mu$ — moments are read off derivatives of $\varphi$ at $0$.)

> [!note]- Complete formal solution
> Fix $t$, take any $h_n\to0$, set $q_n(x)=h_n^{-1}(f(t+h_n,x)-f(t,x))$. By (ii), $q_n\to\partial_t f(t,\cdot)$ pointwise; by the MVT and (iii), $|q_n|\le g\in L^1$. DCT gives $\int q_n\,d\mu\to\int\partial_t f(t,\cdot)\,d\mu$, i.e. $F'(t)=\int\partial_t f(t,x)\,d\mu$. For $\varphi(t)=\int e^{itx}d\mu$, $|\partial_t e^{itx}|=|x|\in L^1(\mu)$ under a finite first moment, so $\varphi'(t)=\int ixe^{itx}\,d\mu$. $\blacksquare$

---

# Key Takeaways

**Differentiation under the integral sign is DCT in disguise: a derivative is a limit of difference quotients, and DCT passes that limit through the integral.** The recipe is mechanical — write the derivative as a sequential limit, recognise the difference quotients as a sequence of functions of $x$, dominate them, invoke DCT. The single non-obvious ingredient is the **mean value theorem**, which converts the difference quotient into a value of $\partial_t f$ and thereby supplies the *uniform-in-$h$* integrable bound that DCT requires. Without an integrable bound on $\partial_t f$, the interchange can genuinely fail.

**This is the workhorse that makes [[Def - Characteristic Function|characteristic functions]] (and Laplace transforms, and the heat kernel) smooth, and turns moments into derivatives.** $\varphi^{(k)}(0)=i^k\mathbb{E}[X^k]$ — the $k$-th moment is the $k$-th derivative of the characteristic function at $0$, valid exactly when the $k$-th moment is finite (so $|x|^k$ dominates). This identity is the bridge from the analytic object $\varphi$ to the probabilistic data $\{\mathbb{E}[X^k]\}$, and it underlies the characteristic-function proof of the [[Thm - Central Limit Theorem|central limit theorem]].
