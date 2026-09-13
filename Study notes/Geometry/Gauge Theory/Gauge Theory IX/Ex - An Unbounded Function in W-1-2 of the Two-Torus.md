---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Sobolev Space of Sections"
  - "Thm - Sobolev Norms on the Torus via Fourier Coefficients"
  - "Thm - Sobolev Embedding Theorem"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory, analysis, sobolev-spaces]
---

# Problem Statement

We work on the flat two-torus $T^2 = \mathbb{R}^2/2\pi\mathbb{Z}^2$, with $x = (x_1, x_2)$ and $|x| = (x_1^2 + x_2^2)^{1/2}$; the fundamental domain is $(-\pi, \pi)^2$, so a set contained in the disc $\{|x| < \pi\}$ embeds in $T^2$ without wrap-around. Fix a smooth cutoff $\chi \in C^\infty([0, \infty))$ with
$$0 \le \chi \le 1, \qquad \chi(r) = 1 \text{ for } r \le \tfrac14, \qquad \chi(r) = 0 \text{ for } r \ge \tfrac12,$$
and define, for $x$ in the fundamental domain,
$$u(x) := \chi(|x|)\,\log\log\!\big(1/|x|\big),$$
with $u(0)$ left undefined (a single point, of measure zero) and $u(x) = 0$ for $\tfrac12 \le |x| < \pi$; extend $u$ periodically to $T^2$. Because $\log(1/r) > 0$ for $0 < r < 1$, the composite $\log\log(1/r)$ is smooth on $0 < r < 1$, and since $\chi$ is supported in $\{r \le \tfrac12\} \subset \{r < 1\}$, the function $u$ is smooth on $T^2 \setminus \{0\}$ with its only singularity at the origin.

Prove the following.

**Part (a).** $u \in W^{1,2}(T^2)$: it lies in $L^2(T^2)$ and possesses weak first-order partial derivatives that also lie in $L^2(T^2)$.

**Part (b).** $u$ is unbounded near the origin, hence has no continuous representative: $u \notin C^0(T^2)$.

**Part (c).** Conclude that the inclusion $W^{1,2}(T^2) \subset C^0(T^2)$ is **false**, so that the strict inequality $k - \tfrac{n}{2} > r$ in the Sobolev embedding theorem cannot be relaxed to the non-strict $k - \tfrac{n}{2} \ge r$: the borderline exponent $2k = n$ (here $k = 1$, $n = 2$, $r = 0$) genuinely fails.

**Recall:**

Three ingredients are used: the definition of the Sobolev space, its Fourier characterisation on the torus (which supplies the working criterion for membership in $W^{1,2}$), and the embedding theorem whose sharpness is at issue.

![[Def - Sobolev Space of Sections#The Definition]]

On $T^2$ with the flat metric and trivial connection, $W^{1,2}(T^2)$ is the completion of $C^\infty(T^2)$ in the norm $\|u\|_{W^{1,2}}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2$, where $\nabla u = (\partial_1 u, \partial_2 u)$ and $\|\nabla u\|_{L^2}^2 = \int_{T^2}(|\partial_1 u|^2 + |\partial_2 u|^2)\, dx$.

![[Thm - Sobolev Norms on the Torus via Fourier Coefficients#Statement]]

The consequence we need is the standard identification of this completion: **$W^{1,2}(T^2)$ is exactly the space of $u \in L^2(T^2)$ whose distributional (weak) first partial derivatives $\partial_1 u, \partial_2 u$ are represented by $L^2(T^2)$ functions**, and on that space the norm is $\|u\|_{W^{1,2}}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2$. Here $v_i \in L^2(T^2)$ is the *weak partial derivative* $\partial_i u$ if
$$\int_{T^2} u\,\partial_i\phi\, dx = -\int_{T^2} v_i\,\phi\, dx \qquad \text{for every } \phi \in C^\infty(T^2).$$
We will verify membership through this weak-derivative criterion; the derivation below (Step 4) records the one-paragraph Parseval argument that ties it to the Fourier characterisation $\sum_\xi (1+|\xi|^2)|\hat u(\xi)|^2 < \infty$, so the page is self-contained.

![[Thm - Sobolev Embedding Theorem#Statement]]

For $T^2$ ($n = 2$) the relevant clause is: if $k, r \ge 0$ are integers with $k - \tfrac{n}{2} > r$, then $H_k(T^2) \hookrightarrow C^r(T^2)$ continuously. Taking $r = 0$, this requires $k - 1 > 0$, i.e. $k \ge 2$; it says **nothing** about $k = 1$, and this exercise shows why it cannot.

---

# Convergent Strategy

**Problem class.** This is a *sharpness* (counterexample) problem: a theorem holds under a strict inequality, and we must produce an explicit object showing the inequality cannot be weakened. The recognisable shape is "the estimate has a scaling parameter that sits exactly at a threshold; find the function that saturates it." The threshold here is the borderline dimension $2k = n$ of Sobolev embedding, and the saturating function is a slowly growing radial singularity.

**Assumption pattern.** The engineering is entirely in the choice of radial profile. A pure logarithm $\log(1/r)$ is already unbounded, but it is *not* in $W^{1,2}(\mathbb{R}^2)$ — its gradient $\sim 1/r$ gives $\int |\nabla|^2 \sim \int r\, dr/r^2 = \int dr/r$, which diverges logarithmically. To pass the $W^{1,2}$ test while keeping unboundedness, one damps the growth by a further logarithm: $\log\log(1/r)$ is still unbounded (barely) but its gradient $\sim (r\log(1/r))^{-1}$ gives $\int|\nabla|^2 \sim \int dr/(r\log(1/r)^2)$, which *converges*. The double logarithm is the minimal damping that clears the integral, and this is the whole content of the assumption pattern: **the borderline is logarithmic, so the counterexample is logarithmic.**

**Theorem routing.** The route is: (1) verify $u \in L^2$ by a polar-coordinate integral; (2) compute the pointwise gradient off the origin and verify $\nabla u \in L^2$ by the substitution $s = \log(1/r)$, which turns the borderline integral into the convergent $\int ds/s^2$; (3) prove that this pointwise gradient *is* the weak gradient, by integrating by parts on $T^2 \setminus B_\epsilon(0)$ and showing the boundary term over $\partial B_\epsilon$ vanishes as $\epsilon \to 0$ — the delicate step, since without it a singular (distributional) contribution at the origin could hide; (4) invoke the weak-derivative characterisation from [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|the Fourier theorem]] to conclude $u \in W^{1,2}$; then (5) note $u$ is unbounded and (6) read off the failure of the embedding.

**Key decision point.** Two moves carry the argument. The first is *the choice of profile* $\log\log(1/r)$, dictated by the substitution $s = \log(1/r)$: this is the unique change of variable that renders both the area weight $r\, dr$ and the singular gradient tractable, converting $\int \frac{dr}{r\,(\log 1/r)^2}$ into $\int \frac{ds}{s^2}$. The second, easy to overlook and genuinely necessary, is *checking that no distributional mass sits at the origin* — that the a.e.-defined classical gradient is the honest weak gradient. Skipping this step is the classic error: the one-dimensional Heaviside function is smooth off a point with a.e. gradient zero, yet its weak derivative is a Dirac mass, so "smooth off a point with $L^2$ pointwise gradient" does *not* by itself give membership in $W^{1,2}$. The boundary-term estimate $\epsilon\log\log(1/\epsilon) \to 0$ is what rules the singular part out here.

---

# Legal Operations Used

The [[Gauge Theory IX — Sobolev Spaces, Elliptic Operators, and Elliptic Complexes|topic page]] for this chapter is not yet assembled, so the operations are named descriptively; the orchestrator will reconcile the numbering against the topic page's Legal Operations list.

1. **Evaluate a radial integral in polar coordinates.** For a radial integrand $F(|x|)$ on the plane, $\int_{|x| < R} F(|x|)\, dx = 2\pi\int_0^R F(r)\, r\, dr$. The factor $r$ from the area element is decisive at the borderline: it is exactly what a single logarithm cannot beat and a double logarithm can.

2. **Clear a logarithmic integral by the substitution $s = \log(1/r)$.** With $s = \log(1/r)$, $ds = -dr/r$, the borderline integrals become power integrals in $s$: $\int_0 \frac{dr}{r\,(\log 1/r)^2} = \int^\infty \frac{ds}{s^2} < \infty$, whereas $\int_0 \frac{dr}{r\,(\log 1/r)} = \int^\infty \frac{ds}{s} = \infty$.

3. **Integrate by parts on the complement of a shrinking ball and control the boundary term.** To identify the weak derivative of a function singular at one point, apply the divergence theorem on $T^2 \setminus B_\epsilon(0)$, whose only boundary is the circle $\partial B_\epsilon$, and estimate the boundary integral by $\sup_{\partial B_\epsilon}|u| \cdot \|\phi\|_{C^0}\cdot \operatorname{length}(\partial B_\epsilon)$.

4. **Pass to the limit under the integral by dominated convergence.** As $\epsilon \to 0$ the sets $T^2 \setminus B_\epsilon$ exhaust $T^2$ up to the null set $\{0\}$; since $u\,\partial_i\phi$ and $(\partial_i u)\phi$ are in $L^1(T^2)$, their integrals over $T^2\setminus B_\epsilon$ converge to their integrals over $T^2$.

5. **Certify the absence of a continuous representative by unbounded continuity on a punctured neighbourhood.** A function that is continuous and unbounded on a punctured neighbourhood of a point cannot be almost-everywhere equal to any continuous function on the compact $T^2$, because a continuous function on a compact space is bounded.

---

# Hints

> [!note]- Hint 1
> Everything happens near the origin, where $\chi \equiv 1$ and $u(x) = \log\log(1/|x|)$. Work in polar coordinates $(r, \phi)$, so that $dx = r\, dr\, d\phi$ and $u$ depends on $r$ alone. First check the easy claim: is $u \in L^2$? The integrand $|u|^2 = (\log\log(1/r))^2$ blows up as $r \to 0$, but you are integrating $|u|^2\, r\, dr$ — does the factor $r$ save you?

> [!note]- Hint 2
> For a radial function $u = g(r)$, $|\nabla u| = |g'(r)|$. Differentiate $g(r) = \log\log(1/r)$: with $L(r) = \log(1/r) = -\log r$, we have $g = \log L$ and $g' = L'/L$. Compute $L'(r) = -1/r$, so $g'(r) = \tfrac{-1/r}{\log(1/r)} = \tfrac{-1}{r\log(1/r)}$ and $|\nabla u|^2 = \tfrac{1}{r^2(\log 1/r)^2}$. Now $\int_{r<1/4}|\nabla u|^2\, dx = 2\pi\int_0^{1/4}\tfrac{dr}{r(\log 1/r)^2}$. Substitute $s = \log(1/r)$.

> [!note]- Hint 3
> The substitution $s = \log(1/r)$ gives $ds = -dr/r$ and turns $\int_0^{1/4}\tfrac{dr}{r(\log 1/r)^2}$ into $\int_{\log 4}^{\infty}\tfrac{ds}{s^2} = \tfrac{1}{\log 4} < \infty$. So $\nabla u \in L^2$. (Notice that a single logarithm, $u = \log(1/r)$, would produce $\int ds/s = \infty$ and fail — that is why the double logarithm is needed.)

> [!note]- Hint 4
> You now have $u \in L^2$ and a pointwise gradient (defined off the origin) in $L^2$. This is *not yet* enough to conclude $u \in W^{1,2}$: you must show the pointwise gradient is the *weak* gradient, i.e. that no Dirac-type mass sits at the origin. Integrate by parts on $T^2 \setminus B_\epsilon(0)$ and estimate the boundary term over $\partial B_\epsilon$. Its size is at most $\sup_{\partial B_\epsilon}|u| \cdot \|\phi\|_{C^0}\cdot 2\pi\epsilon = \log\log(1/\epsilon)\cdot\|\phi\|_{C^0}\cdot 2\pi\epsilon$. Does this go to $0$?

> [!note]- Hint 5
> For the conclusion: $u(x) = \log\log(1/|x|) \to +\infty$ as $x \to 0$, so $u$ is unbounded. A continuous function on the compact torus is bounded, so $u$ has no continuous representative. Match this against the embedding theorem: with $n = 2$, $r = 0$, membership in $C^0$ is guaranteed only when $k - 1 > 0$; at $k = 1$ the inequality is an equality, and this $u \in W^{1,2}$ shows the equality is not enough.

---

# Solution

The plan is to certify $u \in W^{1,2}(T^2)$ in the two halves of the Sobolev norm and then read off the failure of the embedding. The $L^2$ bound on $u$ itself is immediate because the area element $r\, dr$ tames the double logarithm. The $L^2$ bound on the gradient is the crux: the singular gradient $|\nabla u| \sim (r\log(1/r))^{-1}$ is right at the borderline of square-integrability, and the substitution $s = \log(1/r)$ shows it clears the bar by converting the integral into $\int ds/s^2$. A separate step confirms that the pointwise gradient is the genuine weak gradient — no distributional mass at the origin — which is where a careless argument would go wrong. The function is then manifestly unbounded, and the contradiction with the embedding into $C^0$ is exactly the sharpness statement.

**Step 1: $u \in L^2(T^2)$.**

The integral $\int_{T^2}|u|^2\, dx$ is finite because the area weight $r$ dominates the growth of the double logarithm.

> [!note]- Derivation
> Since $u$ is supported in $\{|x| \le \tfrac12\}$ and is smooth (hence bounded) on the annulus $\tfrac14 \le |x| \le \tfrac12$, only the behaviour on $\{|x| < \tfrac14\}$, where $u = \log\log(1/|x|)$, can threaten integrability. In polar coordinates,
> $$\int_{|x| < 1/4} |u|^2\, dx = 2\pi\int_0^{1/4} \big(\log\log(1/r)\big)^2\, r\, dr \qquad \text{(polar coordinates, } dx = r\, dr\, d\phi\text{)}.$$
> The integrand $r\,(\log\log(1/r))^2$ tends to $0$ as $r \to 0^+$: the factor $r \to 0$ beats $(\log\log(1/r))^2 \to \infty$, because $\log\log(1/r)$ grows more slowly than any positive power of $1/r$, so $r\,(\log\log(1/r))^2 \le r \cdot r^{-1/2} = r^{1/2} \to 0$ for $r$ small enough (using $\log\log(1/r) \le r^{-1/4}$ near $0$). Hence the integrand is bounded on $(0, \tfrac14]$ and the integral over the bounded interval is finite. Adding the finite contribution from the annulus,
> $$\|u\|_{L^2(T^2)}^2 = \int_{T^2}|u|^2\, dx < \infty,$$
> so $u \in L^2(T^2)$.

**Step 2: the pointwise gradient and $\nabla u \in L^2(T^2)$.**

Off the origin, $u$ is smooth with $|\nabla u|^2 = |\chi'(r)\log\log(1/r) + \chi(r)g'(r)|^2$ where $g'(r) = -\big(r\log(1/r)\big)^{-1}$; the integral $\int_{T^2}|\nabla u|^2\, dx$ is finite, the borderline piece clearing by the substitution $s = \log(1/r)$.

> [!note]- Derivation
> **Compute the gradient off the origin.** On $T^2 \setminus \{0\}$ the function $u(x) = \chi(r)\,g(r)$ with $r = |x|$ and $g(r) = \log\log(1/r)$ is smooth and radial, so $\nabla u = \big(\chi'(r)g(r) + \chi(r)g'(r)\big)\,\tfrac{x}{r}$ and $|\nabla u| = |\chi'(r)g(r) + \chi(r)g'(r)|$ (as $|x/r| = 1$). Differentiating $g = \log L$ with $L(r) = \log(1/r) = -\log r$ and $L'(r) = -1/r$,
> $$g'(r) = \frac{L'(r)}{L(r)} = \frac{-1/r}{-\log r} = \frac{-1}{r\log(1/r)} \qquad \text{(chain rule, } \tfrac{d}{dr}\log L = L'/L\text{)}.$$
> **Split the integral into the core and the annulus.** On $\{r \le \tfrac14\}$, $\chi \equiv 1$ and $\chi' \equiv 0$, so there $|\nabla u| = |g'(r)| = \big(r\log(1/r)\big)^{-1}$ and $|\nabla u|^2 = \big(r^2(\log 1/r)^2\big)^{-1}$. On the annulus $\{\tfrac14 \le r \le \tfrac12\}$ both $\chi, \chi'$ and $g, g'$ are smooth and bounded (as $\tfrac14 \le r \le \tfrac12 < 1$ keeps $\log(1/r) > 0$ bounded away from $0$), so $|\nabla u|$ is bounded there and contributes a finite amount over a region of finite area. Thus finiteness of $\int_{T^2}|\nabla u|^2$ reduces to the core:
> $$\int_{|x| < 1/4}|\nabla u|^2\, dx = 2\pi\int_0^{1/4} \frac{1}{r^2(\log 1/r)^2}\, r\, dr = 2\pi\int_0^{1/4}\frac{dr}{r\,(\log 1/r)^2} \qquad \text{(polar coordinates; one power of } r \text{ cancels)}.$$
> **Clear the borderline integral.** Substitute $s = \log(1/r) = -\log r$, so $ds = -\tfrac{dr}{r}$, i.e. $\tfrac{dr}{r} = -ds$; as $r$ runs from $\tfrac14$ down to $0^+$, $s$ runs from $\log 4$ up to $+\infty$. Then
> $$2\pi\int_0^{1/4}\frac{dr}{r\,(\log 1/r)^2} = 2\pi\int_{\log 4}^{\infty}\frac{ds}{s^2} = 2\pi\Big[-\frac1s\Big]_{\log 4}^{\infty} = \frac{2\pi}{\log 4} < \infty \qquad \text{(substitution } s = \log(1/r)\text{)}.$$
> Adding the finite annulus contribution, $\|\nabla u\|_{L^2(T^2)}^2 < \infty$, so the pointwise gradient lies in $L^2(T^2)$.
>
> **Why the double logarithm is necessary.** Had we taken the single logarithm $u = \log(1/r)$, then $g'(r) = -1/r$, $|\nabla u|^2 = r^{-2}$, and the same reduction would give $2\pi\int_0^{1/4}\tfrac{dr}{r} = 2\pi\int_{\log 4}^{\infty}\tfrac{ds}{s} = +\infty$: the gradient would fail to be square-integrable. The extra logarithm converts $\int ds/s$ into the convergent $\int ds/s^2$; this is the minimal damping that clears the borderline while leaving $u$ unbounded.

**Step 3: the pointwise gradient is the weak gradient.**

For every test function $\phi \in C^\infty(T^2)$ and each coordinate $i$, $\int_{T^2} u\,\partial_i\phi\, dx = -\int_{T^2}(\partial_i u)\phi\, dx$; hence the a.e.-defined $\partial_i u$ of Step 2 is the weak partial derivative, and there is no distributional mass at the origin.

> [!note]- Derivation
> **Set up integration by parts away from the singularity.** Fix $\phi \in C^\infty(T^2)$ and $i \in \{1, 2\}$, and for $0 < \epsilon < \tfrac14$ let $\Omega_\epsilon := T^2 \setminus \overline{B_\epsilon(0)}$, where $B_\epsilon(0) = \{|x| < \epsilon\}$. On $\Omega_\epsilon$ the function $u$ is smooth, so the divergence theorem (integration by parts on the compact manifold-with-boundary $\Omega_\epsilon$, whose only boundary component is the circle $\partial B_\epsilon$, since the torus itself is closed) gives
> $$\int_{\Omega_\epsilon} u\,\partial_i\phi\, dx = -\int_{\Omega_\epsilon} (\partial_i u)\,\phi\, dx + \int_{\partial B_\epsilon} u\,\phi\,\nu_i\, dS \qquad \text{(divergence theorem applied to the vector field } u\phi\, e_i\text{)},$$
> where $\nu = (\nu_1, \nu_2)$ is the outward unit normal of $\Omega_\epsilon$ along $\partial B_\epsilon$ (which points *into* the removed ball, $\nu = -x/|x|$) and $dS$ is arc length.
>
> **Estimate the boundary term.** On $\partial B_\epsilon$ we have $|x| = \epsilon < \tfrac14$, so $\chi \equiv 1$ and $|u| = \log\log(1/\epsilon)$ is constant along the circle; also $|\nu_i| \le 1$ and the circle has length $2\pi\epsilon$. Therefore
> $$\Big|\int_{\partial B_\epsilon} u\,\phi\,\nu_i\, dS\Big| \le \sup_{\partial B_\epsilon}|u|\cdot\|\phi\|_{C^0}\cdot\operatorname{length}(\partial B_\epsilon) = \log\log(1/\epsilon)\cdot\|\phi\|_{C^0}\cdot 2\pi\epsilon \xrightarrow[\epsilon\to 0]{} 0,$$
> because $\epsilon\log\log(1/\epsilon) \to 0$ as $\epsilon \to 0^+$ (the factor $\epsilon$ dominates the double logarithm, exactly as in Step 1). This limit is the crux: it is the statement that the singularity of $u$ is too weak to create a boundary contribution, so no Dirac-type term appears.
>
> **Pass to the limit in the volume integrals.** As $\epsilon \to 0$, the sets $\Omega_\epsilon$ increase to $T^2 \setminus \{0\}$, which has full measure. The integrand $u\,\partial_i\phi$ lies in $L^1(T^2)$ (as $u \in L^2 \subset L^1$ on the finite-measure $T^2$ by Cauchy–Schwarz, and $\partial_i\phi$ is bounded) and likewise $(\partial_i u)\phi \in L^1(T^2)$ (as $\partial_i u \in L^2 \subset L^1$ by Step 2 and $\phi$ is bounded). By the dominated convergence theorem, with dominating functions $|u\,\partial_i\phi|$ and $|(\partial_i u)\phi|$ respectively,
> $$\int_{\Omega_\epsilon} u\,\partial_i\phi\, dx \to \int_{T^2} u\,\partial_i\phi\, dx, \qquad \int_{\Omega_\epsilon}(\partial_i u)\phi\, dx \to \int_{T^2}(\partial_i u)\phi\, dx \qquad (\epsilon \to 0).$$
> **Combine.** Taking $\epsilon \to 0$ in the integration-by-parts identity and using that the boundary term vanishes,
> $$\int_{T^2} u\,\partial_i\phi\, dx = -\int_{T^2}(\partial_i u)\phi\, dx \qquad \text{for all } \phi \in C^\infty(T^2).$$
> By the definition recalled above, this says the classical gradient $\partial_i u$ of Step 2 *is* the weak partial derivative of $u$. Since $\partial_i u \in L^2(T^2)$, the weak gradient lies in $L^2$.

**Step 4: assemble $u \in W^{1,2}(T^2)$.**

Having $u \in L^2$ (Step 1) with weak gradient $\nabla u \in L^2$ (Steps 2–3), the Fourier characterisation places $u$ in $W^{1,2}(T^2)$.

> [!note]- Derivation
> By [[Thm - Sobolev Norms on the Torus via Fourier Coefficients|the Fourier characterisation of Sobolev norms]], $W^{1,2}(T^2)$ coincides with $H_1(T^2)$, the space of $u \in L^2(T^2)$ with $\sum_\xi(1+|\xi|^2)|\hat u(\xi)|^2 < \infty$. The one-paragraph bridge to the weak-derivative criterion, included for self-containedness: for $u \in L^2(T^2)$ possessing weak derivatives $v_i = \partial_i u \in L^2$, testing the weak-derivative identity against $\phi(x) = e^{-i\langle\xi, x\rangle} \in C^\infty(T^2)$ gives
> $$\hat v_i(\xi) = (2\pi)^{-2}\int_{T^2} v_i\, e^{-i\langle\xi,x\rangle}\, dx = -(2\pi)^{-2}\int_{T^2} u\,\partial_i\big(e^{-i\langle\xi,x\rangle}\big)\, dx = i\xi_i\,\hat u(\xi),$$
> using $\partial_i e^{-i\langle\xi,x\rangle} = -i\xi_i e^{-i\langle\xi,x\rangle}$. Then, since $v_i \in L^2$, Parseval's identity (part (iii) of [[Thm - Fourier Series of Smooth Functions on the Torus|the Fourier theorem]], extended to $L^2$ by density) gives $\|v_i\|_{L^2}^2 = (2\pi)^2\sum_\xi |\xi_i|^2|\hat u(\xi)|^2 < \infty$, so summing over $i$ and adding $\|u\|_{L^2}^2 = (2\pi)^2\sum_\xi |\hat u(\xi)|^2$,
> $$\sum_\xi (1 + |\xi|^2)|\hat u(\xi)|^2 = (2\pi)^{-2}\big(\|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2\big) < \infty.$$
> Hence $u \in H_1(T^2) = W^{1,2}(T^2)$, with $\|u\|_{W^{1,2}}^2 = \|u\|_{L^2}^2 + \|\nabla u\|_{L^2}^2$, both terms finite by Steps 1–3. Therefore $u \in W^{1,2}(T^2)$.

**Step 5: $u$ is unbounded and has no continuous representative.**

As $x \to 0$, $u(x) \to +\infty$; since a continuous function on the compact torus is bounded, no function equal to $u$ almost everywhere can be continuous.

> [!note]- Derivation
> For $0 < |x| < \tfrac14$, $\chi(|x|) = 1$, so $u(x) = \log\log(1/|x|)$. As $|x| \to 0^+$, $\log(1/|x|) \to +\infty$, hence $\log\log(1/|x|) \to +\infty$: the function is unbounded on every punctured neighbourhood of the origin, and it is *continuous* there (a composition of continuous functions on $0 < |x| < \tfrac14$). Suppose, for contradiction, that some $w \in C^0(T^2)$ satisfies $w = u$ almost everywhere. On the punctured disc $\{0 < |x| < \tfrac14\}$ both $u$ and $w$ are continuous and agree on a dense subset (the complement of a null set), so they agree everywhere on the punctured disc; hence $w$ is also unbounded near $0$. But $w$ is continuous on the compact space $T^2$, so $w$ is bounded — a contradiction. Therefore $u$ has no continuous representative: $u \notin C^0(T^2)$.

**Step 6: sharpness of the Sobolev embedding at $2k = n$.**

The function $u$ lies in $W^{1,2}(T^2)$ yet not in $C^0(T^2)$, so $W^{1,2}(T^2) \not\subset C^0(T^2)$; hence the strict inequality in the embedding theorem is essential.

> [!note]- Derivation
> The [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] on the compact $n$-manifold $T^2$ (so $n = 2$) asserts a continuous inclusion $H_k(T^2) \hookrightarrow C^r(T^2)$ under the *strict* inequality $k - \tfrac{n}{2} > r$. For $r = 0$ this reads $k - 1 > 0$, i.e. $k \ge 2$; it does not cover $k = 1$, where $k - \tfrac{n}{2} = 1 - 1 = 0$ fails to be strictly positive. Steps 1–5 produce $u \in W^{1,2}(T^2) = H_1(T^2)$ with no continuous representative, i.e. $u \notin C^0(T^2)$. Consequently the inclusion $H_1(T^2) \subset C^0(T^2)$ is false. Were the theorem's hypothesis relaxed from $k - \tfrac{n}{2} > r$ to the non-strict $k - \tfrac{n}{2} \ge r$, the case $k = 1$, $n = 2$, $r = 0$ (which satisfies $1 - 1 \ge 0$) would assert exactly this false inclusion. Therefore the strict inequality cannot be weakened: the borderline exponent $2k = n$ genuinely fails, and $u$ is the witness. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** The function $u(x) = \chi(|x|)\log\log(1/|x|)$ lies in $W^{1,2}(T^2)$ but not in $C^0(T^2)$; hence $W^{1,2}(T^2) \not\subset C^0(T^2)$ and the strict inequality in the Sobolev embedding theorem is necessary.
>
> $u \in L^2$: in polar coordinates $\int_{|x|<1/4}|u|^2 = 2\pi\int_0^{1/4}(\log\log(1/r))^2 r\, dr < \infty$ since the integrand tends to $0$; the annulus contributes a finite amount and $u = 0$ beyond $\{r \le \tfrac12\}$.
>
> $\nabla u \in L^2$: off the origin $u$ is smooth and radial; with $g(r) = \log\log(1/r)$, $g'(r) = -\big(r\log(1/r)\big)^{-1}$, so on $\{r \le \tfrac14\}$ (where $\chi \equiv 1$) $|\nabla u|^2 = \big(r^2(\log 1/r)^2\big)^{-1}$, giving $\int_{|x|<1/4}|\nabla u|^2 = 2\pi\int_0^{1/4}\tfrac{dr}{r(\log 1/r)^2} = 2\pi\int_{\log 4}^\infty \tfrac{ds}{s^2} = \tfrac{2\pi}{\log 4} < \infty$ after $s = \log(1/r)$; the annulus contributes finitely.
>
> The classical gradient is the weak gradient: for $\phi \in C^\infty(T^2)$ and $\Omega_\epsilon = T^2 \setminus \overline{B_\epsilon}$, the divergence theorem gives $\int_{\Omega_\epsilon} u\,\partial_i\phi = -\int_{\Omega_\epsilon}(\partial_i u)\phi + \int_{\partial B_\epsilon} u\phi\nu_i\, dS$, and $|\int_{\partial B_\epsilon} u\phi\nu_i\, dS| \le \log\log(1/\epsilon)\|\phi\|_{C^0}2\pi\epsilon \to 0$; dominated convergence in the volume integrals ($u\,\partial_i\phi, (\partial_i u)\phi \in L^1$) yields $\int_{T^2} u\,\partial_i\phi = -\int_{T^2}(\partial_i u)\phi$. So $\partial_i u \in L^2$ is the weak derivative, and by the Fourier characterisation $u \in H_1(T^2) = W^{1,2}(T^2)$.
>
> $u \notin C^0$: $u(x) = \log\log(1/|x|) \to +\infty$ as $x \to 0$ and is continuous on the punctured disc, so any a.e.-equal continuous function would be unbounded on the compact $T^2$, impossible.
>
> Sharpness: with $n = 2$, $k = 1$, $r = 0$ one has $k - \tfrac n2 = 0 \not> 0$; the embedding $H_k \hookrightarrow C^0$ requires $k - \tfrac n2 > 0$, and $u \in H_1 \setminus C^0$ shows the non-strict version $k - \tfrac n2 \ge 0$ would be false. Hence the strict inequality cannot be dropped. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue "$u$ is smooth off the single point $0$, its pointwise gradient is in $L^2$, so $u \in W^{1,2}$" and skip Step 3. This is exactly the reasoning that fails for the one-dimensional Heaviside step $H = \mathbf 1_{[0,\infty)}$: it is smooth off one point with a.e. classical derivative $0 \in L^2$, yet its weak derivative is the Dirac mass $\delta_0$, which is *not* an $L^2$ function, so $H \notin W^{1,2}$. The missing ingredient is the boundary-term estimate: for the Heaviside function the analogue of $\int_{\partial B_\epsilon} u\phi\nu_i\, dS$ does *not* vanish (the jump is order $1$, not $\log\log(1/\epsilon)\cdot\epsilon$), which is precisely how the singular mass is created. The step becomes legitimate only after one verifies $\sup_{\partial B_\epsilon}|u|\cdot\operatorname{length}(\partial B_\epsilon) \to 0$, i.e. that the singularity is subcritical for the codimension of the removed point.

---

# Key Takeaways

**The area weight sets the threshold, and logarithms live exactly on it.** The reusable principle is that in $\mathbb{R}^n$ a radial singularity $g(r)$ contributes $\int_0 |g'(r)|^2 r^{n-1}\, dr$ to the squared $W^{1,2}$ seminorm, so square-integrability of the gradient is a competition between the singularity of $g'$ and the power $r^{n-1}$ from the area element. In dimension $n = 2$ the weight is $r^1$, and the borderline singular gradient is $g'(r) \sim 1/r$: a pure power just fails ($\int r\, dr/r^2 = \int dr/r = \infty$), and one must go to a *logarithmic* profile to sit on the threshold. The trigger to reach for a logarithm is precisely this: whenever a power-law attempt to build a Sobolev counterexample lands exactly at a divergent $\int dr/r$, replace the power by a logarithm and the log by a double log until the integral $\int ds/s^p$ (after $s = \log(1/r)$) has $p > 1$. The double logarithm $\log\log(1/r)$ is the canonical borderline object in $W^{1,2}(\mathbb{R}^2)$; its higher-dimensional and higher-order cousins ($\log(1/r)$ for $W^{1,n}(\mathbb{R}^n)$ borderline, iterated logs for sharper thresholds) are built by the same competition.

**"Smooth off a point with $L^2$ pointwise gradient" is not membership in $W^{1,2}$ — the boundary term is the whole story.** The transferable diagnostic is to never conflate the classical (a.e.) gradient with the weak gradient when a function is singular on a lower-dimensional set. The two agree if and only if the integration-by-parts boundary term over a shrinking tube around the singular set vanishes, and that term scales as $\sup|u| \times (\text{measure of the tube's boundary})$. For a point singularity in $\mathbb{R}^2$ the boundary is a circle of length $2\pi\epsilon$, so any $u$ growing slower than $1/\epsilon$ — in particular the double logarithm — has a vanishing boundary term and the classical gradient is honest; a genuine jump (Heaviside) has an order-$1$ boundary term and a Dirac weak derivative. The general lesson for spaced practice: when a function is defined piecewise or has an isolated singularity, the question "is the pointwise derivative the weak derivative?" is answered by one boundary estimate, and forgetting to run it is the single most common error in Sobolev-space arguments. The removed set's codimension enters through the measure of the tube boundary, so the same diagnostic tells you when a singularity along a curve, or a surface, is subcritical.

**Sharpness examples are the way one *reads* the hypotheses of an embedding theorem, not decorations on it.** The strict inequality $k - \tfrac n2 > r$ in the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] looks like a technicality until one sees that at equality it is simply false, and this function is the certificate. The reusable frame: every scaling-critical inequality in analysis (Sobolev, Hölder, Hardy, Gagliardo–Nirenberg) comes with a threshold, and the theorem holds strictly inside it and fails on the boundary; to understand which side of the boundary a given problem sits on, one keeps a stable of borderline objects — the double logarithm here, the fundamental solution $|x|^{2-n}$ for the critical Sobolev exponent, the Aubin–Talenti bubbles for the critical embedding $W^{1,2} \hookrightarrow L^{2n/(n-2)}$ — and tests the inequality against them. In this chapter the point is operational: it is why the four-dimensional Seiberg–Witten and Yang–Mills analysis works with $W^{k,2}$ for $k$ large enough that $2k > 4$ strictly (so $W^{k,2}(M^4) \subset C^0$ and the Sobolev spaces are Banach algebras), and never at the borderline $k = 2$. The companion exercise [[Ex - Fourier Coefficients of Smooth Functions Decay Rapidly]] shows the one-dimensional face of the same dictionary, where coefficient decay of a merely continuous function saturates at $n^{-2}$; both exercises probe the exact seam between regularity and its Sobolev or Fourier certificate.
