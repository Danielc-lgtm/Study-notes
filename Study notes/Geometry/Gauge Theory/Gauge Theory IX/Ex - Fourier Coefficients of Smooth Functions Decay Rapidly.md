---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Fourier Series of Smooth Functions on the Torus"
  - "Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order"
difficulty: "⭐"
tags: [geometry, gauge-theory, analysis, fourier-series]
---

# Problem Statement

We work on the torus $T^n = \mathbb{R}^n / 2\pi\mathbb{Z}^n$ with the flat metric, and on the circle $S^1 = T^1 = \mathbb{R}/2\pi\mathbb{Z}$ as the case $n=1$. For a smooth function $u \in C^\infty(T^n; \mathbb{C})$ the Fourier coefficients are
$$\hat u(\xi) := (2\pi)^{-n} \int_{T^n} u(x)\, e^{-i\langle \xi, x\rangle}\, dx, \qquad \xi \in \mathbb{Z}^n,$$
where $\langle \xi, x\rangle = \sum_{j=1}^n \xi_j x_j$ is the standard pairing. The problem has three parts.

**Part (a) — rapid decrease.** Prove that for every $u \in C^\infty(T^n;\mathbb{C})$ and every integer $N \ge 0$ there is a constant $C_N = C_N(u, n) < \infty$ with
$$|\hat u(\xi)| \le C_N\,(1 + |\xi|)^{-N} \qquad \text{for all } \xi \in \mathbb{Z}^n,$$
where $|\xi| = \big(\sum_j \xi_j^2\big)^{1/2}$ is the Euclidean length. Do this by repeated integration by parts, exhibiting $C_N$ explicitly in terms of finitely many supremum norms of derivatives of $u$.

**Part (b) — a corner: $u(\theta) = \theta(2\pi - \theta)$ on $S^1$.** Regard $u$ as the $2\pi$-periodic extension of the polynomial $\theta \mapsto \theta(2\pi - \theta)$ on $[0, 2\pi]$. Show that $u$ is continuous on $S^1$ but not $C^1$ across the point $\theta \equiv 0$, compute all its Fourier coefficients, and verify that they decay like $n^{-2}$.

**Part (c) — another corner: $v(\theta) = |\sin\theta|$ on $S^1$.** Compute all Fourier coefficients of $v(\theta) = |\sin\theta|$, identify where $v$ fails to be $C^1$, and confirm that its coefficients again decay like $n^{-2}$.

**Part (d) — read off the dictionary.** State in words the relationship between the smoothness of a periodic function and the decay rate of its Fourier coefficients that these three computations illustrate.

**Recall:**

The single fact this exercise drills is part (i) of the theorem on Fourier series of smooth functions, which supplies both the integration-by-parts identity and the target statement of part (a).

![[Thm - Fourier Series of Smooth Functions on the Torus#Statement]]

We isolate the two clauses of part (i) used below. First, **differentiation is multiplication by $i\xi$ on the Fourier side**: for $u \in C^\infty(T^n)$ and each coordinate direction $j$,
$$\widehat{\partial_j u}(\xi) = i\xi_j\, \hat u(\xi),$$
and, iterating over a multi-index $\alpha = (\alpha_1, \dots, \alpha_n) \in \mathbb{Z}_{\ge 0}^n$ with $\partial^\alpha = \partial_1^{\alpha_1}\cdots \partial_n^{\alpha_n}$ and $|\alpha| = \sum_j \alpha_j$,
$$\widehat{\partial^\alpha u}(\xi) = (i\xi)^\alpha\, \hat u(\xi), \qquad (i\xi)^\alpha := \prod_{j=1}^n (i\xi_j)^{\alpha_j}.$$
Second, the conclusion **rapid decrease**: $|\hat u(\xi)| \le C_N (1 + |\xi|)^{-N}$ for every $N$. Part (a) is precisely the proof of the second clause from the first.

![[Def - Fourier Series on the Torus and Sobolev Spaces of Integer Order#The Definition]]

On $S^1$ the coefficients are indexed by $n \in \mathbb{Z}$ and read $\hat u(n) = \tfrac{1}{2\pi}\int_0^{2\pi} u(\theta) e^{-in\theta}\, d\theta$. A function on $S^1$ is exactly a $2\pi$-periodic function on $\mathbb{R}$, so "continuous (respectively $C^1$) on $S^1$" means "continuous (respectively $C^1$) and $2\pi$-periodic on $\mathbb{R}$"; the periodicity requirement is what the endpoint identification $\theta \equiv 0 \equiv 2\pi$ enforces.

---

# Convergent Strategy

**Problem class.** This is a *quantitative decay* problem: turn a qualitative regularity hypothesis ("$u$ is smooth", or "$u$ is continuous but has a corner") into a numerical rate for $|\hat u(\xi)|$. The whole Sobolev theory of this chapter rests on the observation being drilled here — that on the Fourier side, regularity of a function is encoded as decay of its coefficients — so the recognisable shape of the problem is: *I am given control of derivatives and I want control of coefficients (or conversely)*, and the bridge is always the identity $\widehat{\partial^\alpha u} = (i\xi)^\alpha \hat u$.

**Assumption pattern.** In part (a) the hypothesis "$u \in C^\infty$" is used in exactly one way: it guarantees that $\partial^\alpha u$ exists and is continuous — hence bounded, because $T^n$ is compact — for every multi-index $\alpha$, so that every supremum norm $\|\partial^\alpha u\|_{C^0}$ appearing in the estimate is finite. In parts (b) and (c) the operative hypothesis is weaker and more delicate: the functions are only continuous with a jump in the first derivative, so integration by parts may be applied *once* cleanly but the *second* application picks up a boundary term, and that boundary term is exactly what fixes the decay rate at $n^{-2}$ rather than the $n^{-N}$ of the smooth case.

**Theorem routing.** For part (a), the route is: apply the differentiation identity $\widehat{\partial^\alpha u} = (i\xi)^\alpha \hat u$ (part (i) of [[Thm - Fourier Series of Smooth Functions on the Torus|the Fourier theorem]]) to bound each monomial $|\xi^\alpha \hat u(\xi)|$ by the crude estimate "coefficient $\le$ average of $|\partial^\alpha u|$", then combine finitely many such monomial bounds ($|\alpha| = 0$ and $|\alpha| = N$ in each coordinate) into a bound on $(1 + |\xi|)^N |\hat u(\xi)|$ using elementary inequalities between $(1+|\xi|)^N$ and the monomials $|\xi_j|^N$. For parts (b) and (c) the route is direct computation of $\hat u(n) = \tfrac{1}{2\pi}\int_0^{2\pi} u\, e^{-in\theta}\, d\theta$ by integration by parts, reading off the rate from the surviving boundary terms.

**Key decision point.** The one genuinely non-obvious move in part (a) is the passage from "I can bound each monomial $\xi^\alpha \hat u(\xi)$" to "I can bound $(1+|\xi|)^N \hat u(\xi)$". A single monomial such as $\xi_1^N$ controls the coefficient only in directions where $\xi_1$ is large; the vector $(1,0,\dots,0)$-heavy and $(0,\dots,0,1)$-heavy frequencies need *different* monomials. The resolution is to bound the isotropic quantity $(1+|\xi|)^N$ by a *sum* of the axis monomials $1 + \sum_j |\xi_j|^N$, so that whichever coordinate of $\xi$ is largest, the corresponding term does the work. In parts (b) and (c) the decisive observation is that the functions are continuous but their derivatives jump, so one must count exactly how many integrations by parts run before a boundary term appears.

---

# Legal Operations Used

The [[Gauge Theory IX — Sobolev Spaces, Elliptic Operators, and Elliptic Complexes|topic page]] for this chapter is not yet assembled, so the operations are named descriptively; the orchestrator will reconcile the numbering against the topic page's Legal Operations list.

1. **Move a derivative across the Fourier kernel by integration by parts.** On the closed manifold $T^n$ there is no boundary, and $u$ together with $e^{-i\langle\xi,x\rangle}$ is periodic, so $\int_{T^n} (\partial_j u)\, e^{-i\langle\xi,x\rangle}\, dx = -\int_{T^n} u\, \partial_j\big(e^{-i\langle\xi,x\rangle}\big)\, dx$ with no boundary contribution. This is the operation that produces $\widehat{\partial_j u} = i\xi_j \hat u$.

2. **Bound a Fourier coefficient by the average of the absolute value of the function.** From $|e^{-i\langle\xi,x\rangle}| = 1$ and $\operatorname{vol}(T^n) = (2\pi)^n$, every coefficient satisfies $|\hat w(\xi)| \le (2\pi)^{-n} \int_{T^n} |w|\, dx \le \|w\|_{C^0}$. Applied with $w = \partial^\alpha u$ this converts derivative bounds into coefficient bounds.

3. **Dominate an isotropic weight by a sum of axis monomials.** Replace $(1+|\xi|)^N$ by $2^N\big(1 + n^{N/2}\sum_j |\xi_j|^N\big)$ so that a bound on each single-variable monomial $|\xi_j|^N |\hat u(\xi)|$ assembles into a bound on the full weighted coefficient.

4. **Read a decay rate off the surviving boundary term (parts (b), (c)).** Integrate the coefficient integral by parts as often as the boundary terms vanish; the first non-vanishing boundary term, of size $O(1/n)$ per integration performed, pins the rate.

5. **Reduce a real, even function to a cosine integral (part (c)).** When $v(-\theta) = v(\theta)$, the coefficients are real and $\hat v(n) = \hat v(-n)$, so $\hat v(n) = \tfrac{1}{2\pi}\int_0^{2\pi} v(\theta)\cos(n\theta)\, d\theta$ and the sine part drops out by symmetry.

---

# Hints

> [!note]- Hint 1
> For part (a), the only tool you are meant to use is $\widehat{\partial^\alpha u}(\xi) = (i\xi)^\alpha \hat u(\xi)$. Rearranged, this says $\xi^\alpha \hat u(\xi) = i^{-|\alpha|}\,\widehat{\partial^\alpha u}(\xi)$: a *monomial in $\xi$ times the coefficient of $u$* equals *the coefficient of a derivative of $u$*. How large can the coefficient of any smooth function be, in terms of the function itself?

> [!note]- Hint 2
> Every Fourier coefficient obeys $|\hat w(\xi)| \le \|w\|_{C^0}$, because $|\hat w(\xi)| \le (2\pi)^{-n}\int_{T^n}|w| \le (2\pi)^{-n}\operatorname{vol}(T^n)\sup|w| = \sup|w|$. So $|\xi^\alpha \hat u(\xi)| = |\widehat{\partial^\alpha u}(\xi)| \le \|\partial^\alpha u\|_{C^0}$. You now control every monomial $|\xi^\alpha|\,|\hat u(\xi)|$. The remaining task is bookkeeping: bound $(1+|\xi|)^N$ by finitely many of these monomials.

> [!note]- Hint 3
> For the bookkeeping, note $(1+|\xi|)^N \le 2^N(1 + |\xi|^N)$ and $|\xi|^N = (\sum_j \xi_j^2)^{N/2} \le n^{N/2}\max_j |\xi_j|^N \le n^{N/2}\sum_j |\xi_j|^N$. Combine these with Hint 2 applied to $\alpha = 0$ and to $\alpha = N e_j$ (all $N$ derivatives in one coordinate).

> [!note]- Hint 4
> For parts (b) and (c), compute $\hat u(n) = \tfrac{1}{2\pi}\int_0^{2\pi} u(\theta) e^{-in\theta}\, d\theta$ directly for $n \ne 0$ by integrating by parts. In part (b), the first integration by parts has *no* boundary term because $u(0) = u(2\pi) = 0$; the *second* one has a boundary term because $u'(0^+) \ne u'(2\pi^-)$. That surviving term is the source of the $n^{-2}$. In part (c), use evenness to reduce to $\int_0^{2\pi}|\sin\theta|\cos(n\theta)\,d\theta$ and split at $\theta = \pi$ where $\sin$ changes sign.

---

# Solution

The three parts share one mechanism, seen from two sides. Part (a) shows that smoothness — the existence and boundedness of *all* derivatives — forces the coefficients below every polynomial rate. Parts (b) and (c) show the converse edge: two functions that are merely continuous, each with a corner where the first derivative jumps, have coefficients that decay at exactly the rate $n^{-2}$, no faster. The general dictionary they illustrate is stated in part (d): the number of times one may integrate by parts before a boundary term appears is the number of orders of decay.

**Step 1 (Part (a)): the differentiation identity converts monomials into derivative coefficients.**

For $u \in C^\infty(T^n)$ and any multi-index $\alpha$, $\xi^\alpha \hat u(\xi) = i^{-|\alpha|}\,\widehat{\partial^\alpha u}(\xi)$, and consequently $|\xi^\alpha|\,|\hat u(\xi)| \le \|\partial^\alpha u\|_{C^0}$.

> [!note]- Derivation
> **Establish the one-step identity.** Fix a coordinate direction $j$. Because $T^n$ is a closed manifold (no boundary) and both $u$ and $x \mapsto e^{-i\langle\xi,x\rangle}$ are smooth and $2\pi$-periodic in every variable, integration by parts in the $x_j$ variable produces no boundary term:
> $$\widehat{\partial_j u}(\xi) = (2\pi)^{-n}\int_{T^n} (\partial_j u)\, e^{-i\langle\xi,x\rangle}\, dx = -(2\pi)^{-n}\int_{T^n} u\, \partial_j\!\big(e^{-i\langle\xi,x\rangle}\big)\, dx \qquad \text{(integration by parts, periodicity kills the boundary term)}.$$
> Since $\partial_j\big(e^{-i\langle\xi,x\rangle}\big) = -i\xi_j\, e^{-i\langle\xi,x\rangle}$ (chain rule), the right-hand side equals
> $$-(2\pi)^{-n}\int_{T^n} u\,(-i\xi_j)\, e^{-i\langle\xi,x\rangle}\, dx = i\xi_j\, (2\pi)^{-n}\int_{T^n} u\, e^{-i\langle\xi,x\rangle}\, dx = i\xi_j\, \hat u(\xi) \qquad \text{(definition of } \hat u\text{)}.$$
> This is the clause $\widehat{\partial_j u}(\xi) = i\xi_j \hat u(\xi)$ of [[Thm - Fourier Series of Smooth Functions on the Torus|the Fourier theorem]], part (i).
>
> **Iterate.** Applying the one-step identity $\alpha_1$ times in the first variable, then $\alpha_2$ times in the second, and so on — each application is licensed because $\partial^\beta u \in C^\infty(T^n)$ for every $\beta$, so the hypothesis of the one-step identity holds at each stage — gives
> $$\widehat{\partial^\alpha u}(\xi) = (i\xi_1)^{\alpha_1}\cdots (i\xi_n)^{\alpha_n}\, \hat u(\xi) = (i\xi)^\alpha\, \hat u(\xi) \qquad \text{(one-step identity applied } |\alpha| \text{ times)}.$$
> Because $|(i\xi)^\alpha| = |\xi^\alpha|$, taking absolute values and using $|\hat w(\xi)| \le (2\pi)^{-n}\int_{T^n}|w|\,dx \le (2\pi)^{-n}\,\mathrm{vol}(T^n)\,\|w\|_{C^0} = \|w\|_{C^0}$ (from $|e^{-i\langle\xi,x\rangle}| = 1$ and $\mathrm{vol}(T^n) = (2\pi)^n$) with $w = \partial^\alpha u$ yields
> $$|\xi^\alpha|\,|\hat u(\xi)| = |\widehat{\partial^\alpha u}(\xi)| \le \|\partial^\alpha u\|_{C^0} < \infty \qquad \text{(triangle inequality for the integral; } \partial^\alpha u \text{ continuous on the compact } T^n\text{)}.$$
> The supremum is finite precisely because $u$ is smooth and $T^n$ is compact: this is the only place smoothness enters.

**Step 2 (Part (a)): assemble the isotropic weight from axis monomials.**

Bounding $(1+|\xi|)^N$ by a sum of the monomials of Step 1 gives $|\hat u(\xi)| \le C_N(1+|\xi|)^{-N}$ with an explicit $C_N$.

> [!note]- Derivation
> **Bound the weight by monomials.** For any $\xi \in \mathbb{R}^n$ and integer $N \ge 0$,
> $$(1+|\xi|)^N \le 2^N \max(1, |\xi|)^N = 2^N \max(1, |\xi|^N) \le 2^N\big(1 + |\xi|^N\big) \qquad \text{(since } 1 + t \le 2\max(1,t) \text{ for } t \ge 0\text{)},$$
> and, writing $|\xi|^N = \big(\textstyle\sum_{j} \xi_j^2\big)^{N/2}$,
> $$|\xi|^N \le \big(n \max_j \xi_j^2\big)^{N/2} = n^{N/2} \max_j |\xi_j|^N \le n^{N/2} \sum_{j=1}^n |\xi_j|^N \qquad \text{(each } \xi_j^2 \le \max_j \xi_j^2\text{, so the sum is at most } n \text{ times the max)}.$$
> Combining,
> $$(1+|\xi|)^N \le 2^N + 2^N n^{N/2}\sum_{j=1}^n |\xi_j|^N \qquad \text{(substitute the second bound into the first)}.$$
>
> **Multiply through by $|\hat u(\xi)|$ and apply Step 1.** Multiplying the last display by $|\hat u(\xi)| \ge 0$,
> $$(1+|\xi|)^N |\hat u(\xi)| \le 2^N |\hat u(\xi)| + 2^N n^{N/2}\sum_{j=1}^n |\xi_j|^N |\hat u(\xi)|.$$
> By Step 1 with $\alpha = 0$ we have $|\hat u(\xi)| \le \|u\|_{C^0}$, and with $\alpha = N e_j$ (all $N$ derivatives in the $j$-th coordinate, so $|\xi_j|^N = |\xi^\alpha|$) we have $|\xi_j|^N |\hat u(\xi)| \le \|\partial_j^N u\|_{C^0}$. Therefore
> $$(1+|\xi|)^N |\hat u(\xi)| \le 2^N \|u\|_{C^0} + 2^N n^{N/2}\sum_{j=1}^n \|\partial_j^N u\|_{C^0} =: C_N \qquad \text{(Step 1 for } \alpha = 0 \text{ and } \alpha = N e_j\text{)}.$$
> Every term of $C_N$ is a finite supremum of a continuous function on the compact torus, so $C_N < \infty$; it depends only on $N$, on the dimension $n$, and on $u$ through finitely many of its derivatives. Dividing by $(1+|\xi|)^N > 0$ gives $|\hat u(\xi)| \le C_N (1+|\xi|)^{-N}$ for every $\xi \in \mathbb{Z}^n$, as required.

**Step 3 (Part (b)): the corner of $u(\theta) = \theta(2\pi - \theta)$ and its coefficients.**

The periodic extension of $u$ is continuous but not $C^1$ at $\theta \equiv 0$, and $\hat u(0) = \tfrac{2\pi^2}{3}$, $\hat u(n) = -\tfrac{2}{n^2}$ for $n \ne 0$.

> [!note]- Derivation
> **Continuity and the failure of $C^1$.** On $[0, 2\pi]$, $u(\theta) = \theta(2\pi - \theta) = 2\pi\theta - \theta^2$, so $u(0) = 0$ and $u(2\pi) = 2\pi(2\pi - 2\pi) = 0$. The two endpoints agree, so the $2\pi$-periodic extension is continuous across the identified point $\theta \equiv 0 \equiv 2\pi$. Its derivative is $u'(\theta) = 2\pi - 2\theta$, giving the one-sided limits
> $$u'(0^+) = 2\pi, \qquad u'(2\pi^-) = 2\pi - 4\pi = -2\pi \qquad \text{(evaluate } u' \text{ at the two ends)}.$$
> Since $u'(0^+) = 2\pi \ne -2\pi = u'(2\pi^-)$, the periodic extension has a jump of $u'(0^+) - u'(2\pi^-) = 4\pi$ in its first derivative at $\theta \equiv 0$: $u$ is continuous but not $C^1$ there.
>
> **The zeroth coefficient.** Directly,
> $$\hat u(0) = \frac{1}{2\pi}\int_0^{2\pi}(2\pi\theta - \theta^2)\, d\theta = \frac{1}{2\pi}\Big[\pi\theta^2 - \tfrac{\theta^3}{3}\Big]_0^{2\pi} = \frac{1}{2\pi}\Big(4\pi^3 - \tfrac{8\pi^3}{3}\Big) = \frac{1}{2\pi}\cdot\frac{4\pi^3}{3} = \frac{2\pi^2}{3} \qquad \text{(fundamental theorem of calculus)}.$$
>
> **The coefficients for $n \ne 0$, by two integrations by parts.** Write $f(\theta) = 2\pi\theta - \theta^2$, so $f'(\theta) = 2\pi - 2\theta$ and $f''(\theta) = -2$. Integrating by parts once, with antiderivative $\tfrac{e^{-in\theta}}{-in}$ of $e^{-in\theta}$,
> $$\int_0^{2\pi} f(\theta) e^{-in\theta}\, d\theta = \Big[f(\theta)\tfrac{e^{-in\theta}}{-in}\Big]_0^{2\pi} - \int_0^{2\pi} f'(\theta)\tfrac{e^{-in\theta}}{-in}\, d\theta = \frac{1}{in}\int_0^{2\pi} f'(\theta) e^{-in\theta}\, d\theta,$$
> where the boundary term vanishes because $f(0) = f(2\pi) = 0$ (continuity of $u$). Integrating by parts a second time,
> $$\int_0^{2\pi} f'(\theta) e^{-in\theta}\, d\theta = \Big[f'(\theta)\tfrac{e^{-in\theta}}{-in}\Big]_0^{2\pi} - \int_0^{2\pi} f''(\theta)\tfrac{e^{-in\theta}}{-in}\, d\theta.$$
> Here the boundary term does **not** vanish, and it is where the jump of $u'$ enters. Using $e^{-in\cdot 2\pi} = e^{0} = 1$ (as $n \in \mathbb{Z}$),
> $$\Big[f'(\theta)\tfrac{e^{-in\theta}}{-in}\Big]_0^{2\pi} = \frac{1}{-in}\big(f'(2\pi) - f'(0)\big) = \frac{1}{-in}\big(-2\pi - 2\pi\big) = \frac{-4\pi}{-in} = \frac{4\pi}{in} \qquad \text{(} f'(2\pi) = -2\pi,\ f'(0) = 2\pi\text{)}.$$
> The remaining integral vanishes: since $f'' = -2$ is constant and $\int_0^{2\pi} e^{-in\theta}\, d\theta = 0$ for $n \ne 0$,
> $$-\int_0^{2\pi} f''(\theta)\tfrac{e^{-in\theta}}{-in}\, d\theta = \frac{f''}{in}\int_0^{2\pi} e^{-in\theta}\, d\theta = 0 \qquad \text{(orthogonality of the characters for } n \ne 0\text{)}.$$
> Hence $\int_0^{2\pi} f' e^{-in\theta}\, d\theta = \tfrac{4\pi}{in}$, and combining the two integrations by parts,
> $$\int_0^{2\pi} f(\theta) e^{-in\theta}\, d\theta = \frac{1}{in}\cdot\frac{4\pi}{in} = \frac{4\pi}{(in)^2} = -\frac{4\pi}{n^2} \qquad \text{(} (in)^2 = -n^2\text{)}.$$
> Therefore $\hat u(n) = \tfrac{1}{2\pi}\big(-\tfrac{4\pi}{n^2}\big) = -\tfrac{2}{n^2}$ for $n \ne 0$, so $|\hat u(n)| = \tfrac{2}{n^2} \sim n^{-2}$.
>
> **Consistency check.** The corresponding real series is $u(\theta) = \tfrac{2\pi^2}{3} + \sum_{n\ne 0}\big(-\tfrac{2}{n^2}\big)e^{in\theta} = \tfrac{2\pi^2}{3} - 4\sum_{n\ge 1}\tfrac{\cos n\theta}{n^2}$. At $\theta = 0$ this gives $\tfrac{2\pi^2}{3} - 4\sum_{n\ge 1}\tfrac{1}{n^2} = \tfrac{2\pi^2}{3} - 4\cdot\tfrac{\pi^2}{6} = 0 = u(0)$, using $\sum_{n\ge 1} n^{-2} = \tfrac{\pi^2}{6}$; the coefficients are correct.

**Step 4 (Part (c)): the corners of $v(\theta) = |\sin\theta|$ and its coefficients.**

The function $v = |\sin\theta|$ is continuous with corners at $\theta \equiv 0$ and $\theta \equiv \pi$; $\hat v(n) = 0$ for odd $n$ and $\hat v(n) = -\tfrac{2}{\pi(n^2 - 1)}$ for even $n$, so $|\hat v(n)| \sim n^{-2}$.

> [!note]- Derivation
> **Where $v$ fails to be $C^1$.** On $(0, \pi)$, $\sin\theta > 0$ so $v(\theta) = \sin\theta$ and $v'(\theta) = \cos\theta$; on $(\pi, 2\pi)$, $\sin\theta < 0$ so $v(\theta) = -\sin\theta$ and $v'(\theta) = -\cos\theta$. At $\theta = \pi$ the one-sided derivatives are $v'(\pi^-) = \cos\pi = -1$ and $v'(\pi^+) = -\cos\pi = 1$; at $\theta \equiv 0$ they are $v'(0^+) = \cos 0 = 1$ and $v'(2\pi^-) = -\cos 2\pi = -1$. In both places the one-sided derivatives disagree, so $v$ is continuous (as $|\sin\theta|$ is a composition of continuous functions and is $2\pi$-periodic) but not $C^1$, with a corner at each of $\theta \equiv 0$ and $\theta \equiv \pi$.
>
> **Reduce to a cosine integral.** Because $v(-\theta) = |\sin(-\theta)| = |\sin\theta| = v(\theta)$, the function is even, so its coefficients are real and $\hat v(n) = \hat v(-n)$; concretely, the imaginary part $\tfrac{1}{2\pi}\int_0^{2\pi} v(\theta)\sin(n\theta)\,d\theta$ vanishes by the substitution $\theta \mapsto 2\pi - \theta$ (under which $v$ is invariant and $\sin(n\theta)$ changes sign), leaving
> $$\hat v(n) = \frac{1}{2\pi}\int_0^{2\pi} |\sin\theta|\cos(n\theta)\, d\theta = \frac{1}{2\pi}\cdot 2\int_0^{\pi}\sin\theta\,\cos(n\theta)\, d\theta \qquad \text{(evenness of } |\sin\theta|\cos(n\theta) \text{ about } \theta = \pi\text{)},$$
> where the last equality uses that $\theta \mapsto |\sin\theta|\cos(n\theta)$ is symmetric under $\theta \mapsto 2\pi - \theta$ so that the integral over $[\pi, 2\pi]$ equals the integral over $[0,\pi]$, and on $[0,\pi]$ we have $|\sin\theta| = \sin\theta$.
>
> **Evaluate.** Using the product-to-sum identity $\sin\theta\cos(n\theta) = \tfrac{1}{2}\big(\sin((n+1)\theta) - \sin((n-1)\theta)\big)$ — which follows from $\sin A \cos B = \tfrac12(\sin(A+B) + \sin(A-B))$ with $A = \theta$, $B = n\theta$ and $\sin(-x) = -\sin x$ — we get, for $n \ne 1$,
> $$\int_0^{\pi}\sin\theta\cos(n\theta)\,d\theta = \frac{1}{2}\Big[-\frac{\cos((n+1)\theta)}{n+1} + \frac{\cos((n-1)\theta)}{n-1}\Big]_0^{\pi}.$$
> Evaluate the bracket using $\cos(m\pi) = (-1)^m$ and $\cos 0 = 1$:
> $$= \frac{1}{2}\Big[\Big(-\frac{(-1)^{n+1}}{n+1} + \frac{(-1)^{n-1}}{n-1}\Big) - \Big(-\frac{1}{n+1} + \frac{1}{n-1}\Big)\Big] = \frac{1}{2}\big(1 + (-1)^{n}\big)\Big(\frac{1}{n+1} - \frac{1}{n-1}\Big),$$
> where we used $(-1)^{n+1} = (-1)^{n-1} = -(-1)^n$ to collect the two $(-1)^{\cdots}$ terms. The factor $1 + (-1)^n$ is $0$ when $n$ is odd and $2$ when $n$ is even. For even $n$,
> $$\frac{1}{n+1} - \frac{1}{n-1} = \frac{(n-1) - (n+1)}{(n+1)(n-1)} = \frac{-2}{n^2 - 1},$$
> so $\int_0^\pi \sin\theta\cos(n\theta)\,d\theta = \tfrac12\cdot 2\cdot\tfrac{-2}{n^2-1} = \tfrac{-2}{n^2-1}$ and
> $$\hat v(n) = \frac{1}{2\pi}\cdot 2\cdot\frac{-2}{n^2 - 1} = -\frac{2}{\pi(n^2 - 1)} \qquad (n \text{ even}, n \ne \pm 1); \qquad \hat v(n) = 0 \qquad (n \text{ odd}).$$
> The odd case includes $n = 1$: a direct check gives $\int_0^\pi \sin\theta\cos\theta\, d\theta = \tfrac12\int_0^\pi \sin(2\theta)\, d\theta = \tfrac12\big[-\tfrac{\cos 2\theta}{2}\big]_0^\pi = 0$, consistent with $\hat v(1) = 0$. Finally $n = 0$ gives $\hat v(0) = -\tfrac{2}{\pi(0 - 1)} = \tfrac{2}{\pi}$, which agrees with $\hat v(0) = \tfrac{1}{2\pi}\int_0^{2\pi}|\sin\theta|\,d\theta = \tfrac{1}{2\pi}\cdot 2\int_0^\pi \sin\theta\,d\theta = \tfrac{1}{2\pi}\cdot 4 = \tfrac{2}{\pi}$.
>
> For even $n$, $|\hat v(n)| = \tfrac{2}{\pi(n^2-1)} \sim \tfrac{2}{\pi} n^{-2}$: the coefficients decay like $n^{-2}$, exactly as in part (b).

**Step 5 (Part (d)): the smoothness–decay dictionary.**

Both $u$ and $v$ are continuous with a jump in their first derivative and have coefficients of exact order $n^{-2}$; a smooth function has coefficients of order $n^{-N}$ for every $N$. The unifying statement is: *each order of decay costs one clean integration by parts, and a jump in the $m$-th derivative caps the rate at $n^{-(m+1)}$.*

> [!note]- Derivation
> The mechanism is Step 1 read as bookkeeping on boundary terms. For a periodic function $w$ that is continuous with $w', \dots, w^{(m)}$ continuous and periodic but $w^{(m)}$ having a jump, integration by parts may be carried out $m+1$ times against $e^{-in\theta}$; the first $m$ integrations produce no boundary term (each of $w, \dots, w^{(m-1)}$ is periodic and continuous), so
> $$\hat w(n) = \frac{1}{(in)^{m}}\,\widehat{w^{(m)}}(n) \qquad (n \ne 0),$$
> and one further integration by parts of $\widehat{w^{(m)}}(n)$ produces a *non-vanishing* boundary term of size $O(1)$ coming from the jump of $w^{(m)}$, contributing an $O(1/n)$ factor; the leftover integral is $O(1/n)$ as well. The net rate is $|\hat w(n)| \sim |n|^{-(m+1)}$.
>
> For $u(\theta) = \theta(2\pi - \theta)$ the first discontinuous derivative is $u'$ (here $m = 1$), so the rate is $n^{-(1+1)} = n^{-2}$: exactly one clean integration by parts (from $u(0) = u(2\pi)$) then a boundary term (from $u'(0^+) \ne u'(2\pi^-)$), which is precisely what Step 3 exhibited. For $v = |\sin\theta|$ the first discontinuous derivative is again $v'$ ($m = 1$), giving $n^{-2}$, matching Step 4. For a smooth $u$ every $w^{(m)}$ is continuous and periodic, so the boundary term never appears: one may integrate by parts $N$ times for every $N$, and the rate is $n^{-N}$ for all $N$ — which is part (a). The three parts are one theorem seen at $m = \infty$, $m = 1$, and $m = 1$.

> [!note]- Complete formal solution
> **Part (a).** Let $u \in C^\infty(T^n;\mathbb{C})$ and $N \ge 0$. Integration by parts on the closed manifold $T^n$ gives, with no boundary term by periodicity, $\widehat{\partial_j u}(\xi) = i\xi_j \hat u(\xi)$ for each $j$; iterating over a multi-index $\alpha$ (legitimate since $\partial^\beta u \in C^\infty$ for all $\beta$) gives $\widehat{\partial^\alpha u}(\xi) = (i\xi)^\alpha \hat u(\xi)$. Since $|\hat w(\xi)| \le (2\pi)^{-n}\int_{T^n}|w| \le \|w\|_{C^0}$ (as $|e^{-i\langle\xi,x\rangle}| = 1$ and $\mathrm{vol}(T^n) = (2\pi)^n$), taking $w = \partial^\alpha u$ yields $|\xi^\alpha|\,|\hat u(\xi)| \le \|\partial^\alpha u\|_{C^0}$. Now $(1+|\xi|)^N \le 2^N(1+|\xi|^N)$ and $|\xi|^N \le n^{N/2}\sum_j |\xi_j|^N$, so
> $$(1+|\xi|)^N|\hat u(\xi)| \le 2^N|\hat u(\xi)| + 2^N n^{N/2}\sum_j |\xi_j|^N|\hat u(\xi)| \le 2^N\|u\|_{C^0} + 2^N n^{N/2}\sum_{j=1}^n \|\partial_j^N u\|_{C^0} =: C_N,$$
> a finite constant because each supremum is that of a continuous function on the compact $T^n$. Dividing, $|\hat u(\xi)| \le C_N(1+|\xi|)^{-N}$.
>
> **Part (b).** The periodic extension of $u(\theta) = \theta(2\pi-\theta)$ satisfies $u(0) = u(2\pi) = 0$, hence is continuous, while $u'(0^+) = 2\pi \ne -2\pi = u'(2\pi^-)$, hence not $C^1$. Direct integration gives $\hat u(0) = \tfrac{2\pi^2}{3}$. For $n \ne 0$, with $f = 2\pi\theta - \theta^2$, two integrations by parts against $e^{-in\theta}$ (the first boundary term vanishing by $f(0) = f(2\pi) = 0$, the second equal to $\tfrac{4\pi}{in}$ from $f'(2\pi) - f'(0) = -4\pi$, the final integral vanishing by orthogonality of characters) give $\int_0^{2\pi} f e^{-in\theta} = -\tfrac{4\pi}{n^2}$, so $\hat u(n) = -\tfrac{2}{n^2}$; thus $|\hat u(n)| \sim n^{-2}$.
>
> **Part (c).** The function $v = |\sin\theta|$ is continuous and $2\pi$-periodic, with corners (jumps in $v'$) at $\theta \equiv 0$ and $\theta \equiv \pi$. By evenness, $\hat v(n) = \tfrac{1}{2\pi}\cdot 2\int_0^\pi \sin\theta\cos(n\theta)\,d\theta$; the product-to-sum identity and $\cos(m\pi) = (-1)^m$ give the bracket $\tfrac12(1+(-1)^n)\big(\tfrac{1}{n+1} - \tfrac{1}{n-1}\big)$, which vanishes for odd $n$ and equals $\tfrac{-2}{n^2-1}$ for even $n$. Hence $\hat v(n) = 0$ ($n$ odd) and $\hat v(n) = -\tfrac{2}{\pi(n^2-1)}$ ($n$ even), so $|\hat v(n)| \sim n^{-2}$.
>
> **Part (d).** For a periodic $w$ whose first discontinuous derivative is the $m$-th, one may integrate by parts $m$ times without a boundary term, giving $\hat w(n) = (in)^{-m}\widehat{w^{(m)}}(n)$, and the next integration produces the jump-driven boundary term of order $n^{-1}$; hence $|\hat w(n)| \sim n^{-(m+1)}$. For $u$ and $v$, $m = 1$ gives $n^{-2}$; for a smooth function, $m = \infty$ gives faster-than-polynomial decay, which is part (a). $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to prove part (a) by writing $|\hat u(\xi)| \le |\xi|^{-N}\,|\widehat{\partial^\alpha u}(\xi)|$ with a *single* monomial $\xi^\alpha$ of degree $N$, say $\alpha = (N, 0, \dots, 0)$, and calling it done. This fails for frequencies with $\xi_1 = 0$ but $|\xi|$ large — for instance $\xi = (0, R, 0, \dots, 0)$, where $\xi^\alpha = 0$ and the bound is vacuous. The estimate must control *every* direction, which is exactly why Step 2 dominates $(1+|\xi|)^N$ by the *sum* $\sum_j |\xi_j|^N$ over all axes rather than one of them. The single-monomial bound becomes legitimate only after one already knows $|\xi| \le \sqrt{n}\max_j|\xi_j|$, i.e. after restoring the sum.

---

# Key Takeaways

**Regularity is coefficient decay: the bridge is always $\widehat{\partial^\alpha u} = (i\xi)^\alpha\hat u$.** The reusable principle is that on the torus the Fourier transform diagonalises every constant-coefficient differential operator — differentiation in $x_j$ becomes multiplication by $i\xi_j$ — and integration by parts is what proves it, with the closedness of $T^n$ (no boundary) ensuring the identity is exact. The trigger to reach for this dictionary is any problem that hands you control over derivatives and asks for control over coefficients, or the reverse: pointwise smoothness bounds translate into weighted-$\ell^2$ or pointwise decay bounds on $(\hat u(\xi))$, and vice versa. This is the mechanism underneath the whole chapter — the definition of the Sobolev spaces $H_k(T^n)$ by the weights $(1+|\xi|^2)^k$, the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] (enough coefficient decay forces a continuous representative), and the elliptic estimates (an elliptic operator's symbol is invertible, so it *gains* the full order of decay). Whenever a torus computation feels intractable in physical space, transplant it to the frequency lattice, where derivatives are diagonal.

**A finite decay rate is read off the first surviving boundary term, and it counts the regularity exactly.** The transferable diagnostic from parts (b) and (c) is: to find how fast the coefficients of a piecewise-smooth periodic function decay, integrate by parts and watch for the *first* integration that produces a non-vanishing boundary term. Each clean integration (no boundary term) buys one power of $1/n$; the first boundary term — which appears exactly when the derivative being moved across is discontinuous at the identified endpoint — is $O(1)$ and produces the last usable power, after which the rate saturates. A jump in the $m$-th derivative therefore yields $n^{-(m+1)}$ decay, and no better. Both worked functions have $m = 1$ (a corner: continuous value, jumping slope) and both land at $n^{-2}$; had we cubed instead of squared, taking a function whose *second* derivative jumped, we would have found $n^{-3}$. This is a diagnostic one can run in one's head: "how many derivatives are continuous across the seam?" is the same question as "how fast do the coefficients decay?"

**The converse edge is what makes these examples worth remembering: decay that is exactly $n^{-2}$, not faster, certifies membership in some Sobolev spaces and exclusion from others.** The function $u(\theta) = \theta(2\pi-\theta)$ has $|\hat u(n)| = 2n^{-2}$, so $\sum_n (1+n^2)|\hat u(n)|^2 \sim \sum_n n^2 \cdot n^{-4} = \sum_n n^{-2} < \infty$ but $\sum_n (1+n^2)^2 |\hat u(n)|^2 \sim \sum_n n^4 \cdot n^{-4} = \sum_n 1 = \infty$; by the Fourier characterisation of Sobolev norms this places $u$ in $W^{1,2}(S^1) = H_1$ but not in $W^{2,2}(S^1) = H_2$, precisely mirroring "$u'$ exists in $L^2$, $u''$ does not (it is a jump, hence a measure, not an $L^2$ function)". This is the standard way one certifies that a concrete function sits at a given rung of the Sobolev ladder without ever estimating a norm directly: compute the coefficient decay and count. The companion exercise [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]] pushes the same edge in two dimensions, where a function barely in $W^{1,2}$ can even be unbounded — the borderline case $2k = n$ of the embedding theorem.
