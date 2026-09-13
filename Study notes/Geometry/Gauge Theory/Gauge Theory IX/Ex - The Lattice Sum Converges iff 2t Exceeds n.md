---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Convergence of the Lattice Sum"
tags: [geometry, gauge-theory, analysis]
---

# Problem Statement

Fix the dimension $n \ge 1$ and a real exponent $t \in \mathbb{R}$. For a lattice point $\xi = (\xi_1,\dots,\xi_n) \in \mathbb{Z}^n$ write $\lvert\xi\rvert^2 = \xi_1^2 + \cdots + \xi_n^2$, and consider the **lattice sum**
$$\Sigma(t) := \sum_{\xi \in \mathbb{Z}^n} \big(1 + \lvert\xi\rvert^2\big)^{-t},$$
a series of non-negative terms (so its value in $[0,+\infty]$ is unambiguous, independent of any ordering).

Prove, entirely by comparison with the integral $\displaystyle\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx$:

1. **(Convergence criterion, both directions.)** $\Sigma(t) < \infty$ if and only if $2t > n$.

2. **(Tail estimate.)** When $2t > n$, there is a constant $C_{n,t} < \infty$ with
$$\sum_{\substack{\xi\in\mathbb{Z}^n \\ \lvert\xi\rvert \ge R}}(1+\lvert\xi\rvert^2)^{-t} \le C_{n,t}\,R^{\,n-2t} \qquad \text{for all } R \ge 1.$$

3. **(Exact value in the model case.)** For $n = 1$, $t = 1$ the criterion gives convergence ($2 > 1$); the exact value is
$$\sum_{m\in\mathbb{Z}}\frac{1}{1+m^2} = \pi\coth\pi \approx 3.153.$$
Verify this identity (as bold context, via the partial-fraction expansion of the hyperbolic cotangent) and check it numerically against the partial sums.

This is a drill of the technical lemma reused four times in Chapter IX — in the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]], the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]], the [[Thm - Sobolev Multiplication Theorem|Sobolev multiplication theorem]], and the elliptic estimates — where it is the arithmetic engine behind every statement of the form "$k$ derivatives in $L^2$ control $r$ derivatives, provided the surplus $k - r$ beats the dimension." The exercise reconstructs that lemma's proof so the mechanism is visible: the sum converges exactly when the tail integral converges, and the tail integral converges exactly when the radial exponent $n - 1 - 2t$ is below $-1$.

**Recall.**

The single named object is the lattice-sum theorem itself, which this exercise reproves and sharpens.

![[Thm - Convergence of the Lattice Sum#Statement]]

The [[Thm - Convergence of the Lattice Sum|lattice-sum theorem]] asserts exactly statements 1 and 2 above; the present exercise is its proof, carried out by the integral-comparison method, together with the explicit evaluation in the one-dimensional case. No result beyond elementary integration in polar coordinates and the comparison test for non-negative series is used; the partial-fraction identity for $\coth$ needed in statement 3 is invoked only as bold context and is not part of the required argument.

We will use two elementary facts about integration in $\mathbb{R}^n$, both standard and stated here for self-containedness. First, **integration in polar coordinates**: for a radial function $g(\lvert x\rvert)$,
$$\int_{\mathbb{R}^n} g(\lvert x\rvert)\,dx = \omega_{n-1}\int_0^\infty g(r)\,r^{n-1}\,dr, \qquad \omega_{n-1} := \operatorname{vol}(S^{n-1}) = \frac{2\pi^{n/2}}{\Gamma(n/2)},$$
where $\omega_{n-1}$ is the $(n-1)$-dimensional volume of the unit sphere. Second, the **comparison test for improper integrals**: $\int_1^\infty r^{a}\,dr$ converges if and only if $a < -1$, with value $\tfrac{1}{-a-1}$ when it does.

---

# Convergent Strategy

**Problem class.** This is an *integral-comparison for a lattice sum* problem: the object is a sum over $\mathbb{Z}^n$ of a positive, radially decreasing weight, and the target is a sharp threshold for finiteness together with a decay rate for the tail. The recognisable feature is that the summand $(1+\lvert\xi\rvert^2)^{-t}$ is the restriction to the integer lattice of a smooth radial function that is *monotone in $\lvert x\rvert$* for large $\lvert x\rvert$; whenever the summand is (eventually) a monotone sampling of a function, the sum and the integral of that function differ by a bounded factor, and the sum inherits the integral's convergence behaviour exactly.

**Assumption pattern.** The only structural input is that the terms are non-negative, which makes the value of the sum independent of ordering and lets us group the lattice points by the unit cubes centred at them without worrying about conditional convergence. The dimension $n$ enters solely through the volume growth of shells: there are on the order of $R^{n-1}$ lattice points at radius near $R$, so the sum over a shell of the weight $R^{-2t}$ is of order $R^{n-1-2t}$, and summing over shells is the discrete analogue of $\int r^{n-1-2t}\,dr$. This is why the threshold is a single inequality $n - 1 - 2t < -1$, i.e. $2t > n$.

**Theorem routing.** The route is a two-sided comparison via **unit cubes**. Attach to each lattice point $\xi$ the unit cube $Q_\xi = \xi + [-\tfrac12,\tfrac12]^n$; the cubes tile $\mathbb{R}^n$ disjointly and each has volume $1$. On $Q_\xi$ the weight $(1+\lvert x\rvert^2)^{-t}$ and the term $(1+\lvert\xi\rvert^2)^{-t}$ differ by a bounded factor (a **two-sided comparison** $1 + \lvert x\rvert^2 \asymp 1 + \lvert\xi\rvert^2$ for $x \in Q_\xi$), so the term is trapped between constants times $\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx$. Summing over $\xi$ turns the sum into the integral over $\mathbb{R}^n$ up to constants, and the integral is evaluated by **polar coordinates** and the **comparison test** to converge exactly when $2t > n$. The same cube comparison, restricted to $\lvert\xi\rvert \ge R$, delivers the tail estimate.

**Key decision point.** The one genuine choice is *which direction of the cube comparison to use where*. For convergence ($2t > n$) we bound the term *above* by a multiple of the cube integral, so that the finite integral dominates the sum. For divergence ($2t \le n$) we bound the term *below* by a multiple of the cube integral (valid once $\lvert\xi\rvert$ is large enough that the cube stays away from the origin), so that the infinite integral is dominated by the sum. Getting the two comparison constants — one from $\lvert x\rvert \le \lvert\xi\rvert + \tfrac{\sqrt n}2$ and one from $\lvert x\rvert \ge \lvert\xi\rvert - \tfrac{\sqrt n}2$ — is the whole content of the argument.

---

# Legal Operations Used

This solution uses the following operations, named descriptively (the §9.2 topic page's numbered Legal Operations register will subsume them).

1. **Tile $\mathbb{R}^n$ by unit cubes centred at lattice points.** Set $Q_\xi = \xi + [-\tfrac12,\tfrac12]^n$; the $\{Q_\xi\}_{\xi\in\mathbb{Z}^n}$ are disjoint (up to measure-zero boundaries), cover $\mathbb{R}^n$, and each has volume $1$. This converts a sum over $\mathbb{Z}^n$ into an integral over $\mathbb{R}^n$.

2. **Compare the sampled weight to the continuous weight on each cube (two-sided).** For $x \in Q_\xi$, control $1 + \lvert x\rvert^2$ above and below by constant multiples of $1 + \lvert\xi\rvert^2$, using $\big\lvert\lvert x\rvert - \lvert\xi\rvert\big\rvert \le \tfrac{\sqrt n}2$; raise to the power $-t$ to bound $(1+\lvert\xi\rvert^2)^{-t}$ against $\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx$.

3. **Evaluate the radial integral in polar coordinates and apply the comparison test.** Reduce $\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx$ to $\omega_{n-1}\int_0^\infty(1+r^2)^{-t}r^{n-1}\,dr$ and decide convergence by the asymptotics $r^{n-1-2t}$ at infinity.

4. **Localise the comparison to a half-space of the lattice for the tail.** Restrict the cube tiling to $\{\lvert\xi\rvert \ge R\}$ and compare with $\int_{\lvert x\rvert \ge R/2}$ to obtain the power-law tail bound $R^{n-2t}$.

5. **Invoke a closed-form summation identity as context.** Recognise $\sum_{m\in\mathbb{Z}}(1+m^2)^{-1}$ as the value $\pi\coth\pi$ from the partial-fraction (Mittag–Leffler) expansion of $\coth$, and confirm it numerically.

---

# Hints

> [!note]- Hint 1
> The summand $(1+\lvert\xi\rvert^2)^{-t}$ is the value at the lattice point $\xi$ of the smooth radial function $f(x) = (1+\lvert x\rvert^2)^{-t}$. For a positive, slowly-varying function, a sum over the lattice and the integral over $\mathbb{R}^n$ agree up to a bounded factor. What geometric object lets you compare "the value at $\xi$" with "the integral near $\xi$"?

> [!note]- Hint 2
> Put a unit cube $Q_\xi = \xi + [-\tfrac12,\tfrac12]^n$ around each lattice point. The cubes tile $\mathbb{R}^n$ and have volume $1$. On $Q_\xi$, how far can $\lvert x\rvert$ be from $\lvert\xi\rvert$? The diameter of the cube is $\sqrt n$, so $\lvert\lvert x\rvert - \lvert\xi\rvert\rvert \le \tfrac{\sqrt n}2$. Turn this into a two-sided bound $c_n(1+\lvert\xi\rvert^2) \le 1+\lvert x\rvert^2 \le C_n(1+\lvert\xi\rvert^2)$ for $x\in Q_\xi$.

> [!note]- Hint 3
> Raise the two-sided bound to the power $-t$ (with $t$ possibly of either sign, but the interesting case is $t > 0$) and integrate over $Q_\xi$ (volume $1$): this sandwiches the term $(1+\lvert\xi\rvert^2)^{-t}$ between constant multiples of $\int_{Q_\xi} f$. Sum over $\xi$: the sum is trapped between constants times $\int_{\mathbb{R}^n} f$. Now everything reduces to the convergence of one integral.

> [!note]- Hint 4
> Evaluate $\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx = \omega_{n-1}\int_0^\infty (1+r^2)^{-t}r^{n-1}\,dr$ in polar coordinates. Near $r = 0$ the integrand is bounded; near $r = \infty$ it behaves like $r^{n-1-2t}$. The comparison test says $\int^\infty r^{n-1-2t}\,dr$ converges iff $n - 1 - 2t < -1$, i.e. $2t > n$.

> [!note]- Hint 5
> For the tail, restrict the cubes to $\lvert\xi\rvert \ge R$; their union lies inside $\{\lvert x\rvert \ge R - \tfrac{\sqrt n}2\}$, which for $R \ge \sqrt n$ contains $\{\lvert x\rvert \ge R/2\}$-type control. The radial integral $\int_{R/2}^\infty r^{n-1-2t}\,dr$ evaluates to a constant times $R^{n-2t}$.

> [!note]- Hint 6
> For statement 3, recall the Mittag–Leffler expansion $\pi\coth(\pi z) = \tfrac1z + \sum_{m\ge1}\tfrac{2z}{z^2+m^2}$. Put $z = 1$ and split $\sum_{m\in\mathbb{Z}}\tfrac1{1+m^2}$ into the $m=0$ term plus twice the $m\ge1$ sum.

---

# Solution

The plan is to prove the finiteness criterion by trapping the sum between two constant multiples of the integral $\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx$, using unit cubes for the comparison, and then to read off both the threshold $2t > n$ and the tail rate $R^{n-2t}$ from a single polar-coordinate evaluation of that integral. The upper comparison (term $\le$ cube integral) handles convergence; the lower comparison (term $\ge$ cube integral, once the cube avoids the origin) handles divergence. The final step evaluates the one-dimensional sum in closed form as a check.

**Step 0: The two-sided cube comparison.**

For every $\xi \in \mathbb{Z}^n$ and every $x \in Q_\xi := \xi + [-\tfrac12,\tfrac12]^n$,
$$\tfrac14\big(1 + \lvert\xi\rvert^2\big) \;\le\; 1 + \lvert x\rvert^2 \;\le\; C_n\big(1 + \lvert\xi\rvert^2\big), \qquad C_n := 1 + \tfrac{3n}{4},$$
the lower bound holding under the additional assumption $\lvert\xi\rvert \ge \sqrt n$.

> [!note]- Derivation
> For $x \in Q_\xi$ each coordinate satisfies $\lvert x_i - \xi_i\rvert \le \tfrac12$, so $\lvert x - \xi\rvert = \big(\sum_i(x_i-\xi_i)^2\big)^{1/2} \le \big(n\cdot\tfrac14\big)^{1/2} = \tfrac{\sqrt n}2$. By the triangle inequality in $\mathbb{R}^n$,
> $$\big\lvert\,\lvert x\rvert - \lvert\xi\rvert\,\big\rvert \le \lvert x - \xi\rvert \le \tfrac{\sqrt n}2 \qquad \text{(reverse triangle inequality)}.$$
> **Upper bound.** From $\lvert x\rvert \le \lvert\xi\rvert + \tfrac{\sqrt n}2$,
> $$\lvert x\rvert^2 \le \lvert\xi\rvert^2 + \sqrt n\,\lvert\xi\rvert + \tfrac n4 \le \lvert\xi\rvert^2 + \tfrac12\big(\lvert\xi\rvert^2 + n\big) + \tfrac n4 = \tfrac32\lvert\xi\rvert^2 + \tfrac{3n}4 \qquad \text{(expanding, then } \sqrt n\,\lvert\xi\rvert \le \tfrac12(\lvert\xi\rvert^2 + n) \text{ by AM–GM)},$$
> so $1 + \lvert x\rvert^2 \le 1 + \tfrac32\lvert\xi\rvert^2 + \tfrac{3n}4 \le \big(1 + \tfrac{3n}4\big)\big(1 + \lvert\xi\rvert^2\big) = C_n\big(1+\lvert\xi\rvert^2\big)$, because the coefficient of $\lvert\xi\rvert^2$ on the left, $\tfrac32$, is at most $C_n = 1 + \tfrac{3n}4$ (as $n \ge 1$), and the constant term $1 + \tfrac{3n}4$ equals $C_n$.
> **Lower bound (assuming $\lvert\xi\rvert \ge \sqrt n$).** Then $\lvert x\rvert \ge \lvert\xi\rvert - \tfrac{\sqrt n}2 \ge \lvert\xi\rvert - \tfrac{\lvert\xi\rvert}2 = \tfrac{\lvert\xi\rvert}2$ (using $\tfrac{\sqrt n}2 \le \tfrac{\lvert\xi\rvert}2$), hence
> $$1 + \lvert x\rvert^2 \ge 1 + \tfrac14\lvert\xi\rvert^2 \ge \tfrac14\big(1 + \lvert\xi\rvert^2\big) \qquad \text{(since } 1 \ge \tfrac14 \text{ and } \tfrac14\lvert\xi\rvert^2 = \tfrac14\lvert\xi\rvert^2\text{)}.$$
> This proves both inequalities. Both are used below with the exponent $-t$; for $t > 0$ the map $s \mapsto s^{-t}$ is decreasing, so it reverses each inequality, and for $t \le 0$ the convergence question is trivial (see Step 1), so we may keep $t > 0$ in mind.

**Step 1: Convergence when $2t > n$.**

If $2t > n$ then $\Sigma(t) \le C_n^{\,t}\displaystyle\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx < \infty$.

> [!note]- Derivation
> First dispose of $t \le 0$: then $2t \le 0 < n$, and each term $(1+\lvert\xi\rvert^2)^{-t} \ge 1$, so $\Sigma(t) = \infty$; this is consistent with the criterion (the "if" hypothesis $2t > n$ is not met) and needs no integral. So assume $t > 0$.
>
> **Bound each term by its cube integral.** Fix $\xi$. For $x \in Q_\xi$, the upper bound of Step 0 gives $1 + \lvert x\rvert^2 \le C_n(1+\lvert\xi\rvert^2)$; raising to $-t < 0$ (which reverses the inequality) yields $(1+\lvert x\rvert^2)^{-t} \ge C_n^{-t}(1+\lvert\xi\rvert^2)^{-t}$. Integrating over $Q_\xi$, whose volume is $1$,
> $$\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx \ge C_n^{-t}(1+\lvert\xi\rvert^2)^{-t}\cdot\operatorname{vol}(Q_\xi) = C_n^{-t}(1+\lvert\xi\rvert^2)^{-t} \qquad \text{(Step 0 upper bound, raised to } -t\text{; } \operatorname{vol}(Q_\xi) = 1\text{)}.$$
> **Sum over the disjoint tiling.** The cubes $\{Q_\xi\}$ are pairwise disjoint up to their measure-zero boundaries and their union is all of $\mathbb{R}^n$, so summing the previous display over $\xi \in \mathbb{Z}^n$ and using additivity of the integral over the disjoint pieces,
> $$C_n^{-t}\,\Sigma(t) = \sum_{\xi} C_n^{-t}(1+\lvert\xi\rvert^2)^{-t} \le \sum_\xi \int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx = \int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx \qquad \text{(summing the cube bound; } \bigsqcup_\xi Q_\xi = \mathbb{R}^n\text{)}.$$
> **Evaluate the integral.** By integration in polar coordinates,
> $$\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx = \omega_{n-1}\int_0^\infty (1+r^2)^{-t}\,r^{n-1}\,dr \qquad \text{(polar coordinates, } \omega_{n-1} = \operatorname{vol}(S^{n-1})\text{)}.$$
> On $[0,1]$ the integrand is continuous, hence its integral is finite. On $[1,\infty)$ we have $(1+r^2)^{-t} \le r^{-2t}$, so $(1+r^2)^{-t}r^{n-1} \le r^{n-1-2t}$, and by the **comparison test** $\int_1^\infty r^{n-1-2t}\,dr$ converges because its exponent satisfies $n - 1 - 2t < -1 \iff 2t > n$, which holds by hypothesis. Therefore the integral is finite, and $\Sigma(t) \le C_n^{\,t}\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx < \infty$.

**Step 2: Divergence when $2t \le n$.**

If $2t \le n$ then $\Sigma(t) = \infty$.

> [!note]- Derivation
> As in Step 1 the case $t \le 0$ is immediate, so take $0 < t$ with $2t \le n$. We bound the sum *below* by an integral that diverges.
>
> **Bound the cube integral by the term (lower comparison).** Fix $\xi$ with $\lvert\xi\rvert \ge \sqrt n$. For $x \in Q_\xi$, the lower bound of Step 0 gives $1 + \lvert x\rvert^2 \ge \tfrac14(1+\lvert\xi\rvert^2)$; raising to $-t < 0$ reverses it: $(1+\lvert x\rvert^2)^{-t} \le 4^{t}(1+\lvert\xi\rvert^2)^{-t}$. Integrating over $Q_\xi$ (volume $1$),
> $$\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx \le 4^{t}(1+\lvert\xi\rvert^2)^{-t} \qquad \text{(Step 0 lower bound, raised to } -t\text{; } \operatorname{vol}(Q_\xi) = 1\text{)}.$$
> **Sum over the far lattice points.** Let $\Lambda_R := \{\xi \in \mathbb{Z}^n : \lvert\xi\rvert \ge \sqrt n\}$ and sum the display over $\xi \in \Lambda_{\sqrt n}$:
> $$4^{-t}\sum_{\xi\in\Lambda_{\sqrt n}}\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx \le \sum_{\xi\in\Lambda_{\sqrt n}}(1+\lvert\xi\rvert^2)^{-t} \le \Sigma(t) \qquad \text{(summing; the far sum is part of the full sum)}.$$
> **Locate an infinite integral inside the far cubes.** If $\lvert x\rvert \ge 2\sqrt n$ then the lattice point $\xi$ with $x \in Q_\xi$ satisfies $\lvert\xi\rvert \ge \lvert x\rvert - \tfrac{\sqrt n}2 \ge 2\sqrt n - \tfrac{\sqrt n}2 = \tfrac{3\sqrt n}2 \ge \sqrt n$, so $\xi \in \Lambda_{\sqrt n}$; hence $\{\lvert x\rvert \ge 2\sqrt n\} \subseteq \bigcup_{\xi\in\Lambda_{\sqrt n}} Q_\xi$. Therefore
> $$\sum_{\xi\in\Lambda_{\sqrt n}}\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx = \int_{\bigcup_{\xi\in\Lambda_{\sqrt n}}Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx \ge \int_{\lvert x\rvert \ge 2\sqrt n}(1+\lvert x\rvert^2)^{-t}\,dx \qquad \text{(monotonicity of the integral over the larger region)}.$$
> **The tail integral diverges.** In polar coordinates, $\int_{\lvert x\rvert \ge 2\sqrt n}(1+\lvert x\rvert^2)^{-t}\,dx = \omega_{n-1}\int_{2\sqrt n}^\infty (1+r^2)^{-t}r^{n-1}\,dr$. For $r \ge 1$, $(1+r^2)^{-t} \ge (2r^2)^{-t} = 2^{-t}r^{-2t}$, so the integrand is at least $2^{-t}r^{n-1-2t}$, and $\int_{2\sqrt n}^\infty r^{n-1-2t}\,dr = \infty$ because its exponent satisfies $n - 1 - 2t \ge -1$ (the negation of $2t > n$, using $2t \le n$). Chaining the three displays, $\Sigma(t) \ge 4^{-t}\cdot\infty = \infty$. Combined with Step 1, $\Sigma(t) < \infty \iff 2t > n$, which is statement 1.

**Step 3: The tail estimate for $2t > n$.**

For $2t > n$ there is $C_{n,t} < \infty$ with $\displaystyle\sum_{\lvert\xi\rvert\ge R}(1+\lvert\xi\rvert^2)^{-t} \le C_{n,t}\,R^{\,n-2t}$ for all $R \ge 1$.

> [!note]- Derivation
> **Reduce to a tail integral.** Exactly as in Step 1, for each $\xi$ the term is bounded by $C_n^{\,t}\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}\,dx$. Summing over $\lvert\xi\rvert \ge R$ and using that $\bigcup_{\lvert\xi\rvert\ge R}Q_\xi \subseteq \{\lvert x\rvert \ge R - \tfrac{\sqrt n}2\}$ (each such $x$ lies in some $Q_\xi$ with $\lvert\xi\rvert \ge \lvert x\rvert - \tfrac{\sqrt n}2$, but here we go the other way: if $x \in Q_\xi$ with $\lvert\xi\rvert \ge R$ then $\lvert x\rvert \ge \lvert\xi\rvert - \tfrac{\sqrt n}2 \ge R - \tfrac{\sqrt n}2$),
> $$\sum_{\lvert\xi\rvert\ge R}(1+\lvert\xi\rvert^2)^{-t} \le C_n^{\,t}\int_{\lvert x\rvert \ge R - \sqrt n/2}(1+\lvert x\rvert^2)^{-t}\,dx \qquad \text{(Step-1 comparison, restricted to the far cubes)}.$$
> **Case $R \ge \sqrt n$.** Then $R - \tfrac{\sqrt n}2 \ge \tfrac R2$, so the region of integration is contained in $\{\lvert x\rvert \ge R/2\}$, and in polar coordinates
> $$\int_{\lvert x\rvert \ge R/2}(1+\lvert x\rvert^2)^{-t}\,dx = \omega_{n-1}\int_{R/2}^\infty (1+r^2)^{-t}r^{n-1}\,dr \le \omega_{n-1}\int_{R/2}^\infty r^{n-1-2t}\,dr = \omega_{n-1}\,\frac{(R/2)^{\,n-2t}}{2t-n} \qquad \text{(} (1+r^2)^{-t}\le r^{-2t}\text{; comparison test, } 2t-n > 0\text{)}.$$
> Since $(R/2)^{n-2t} = 2^{2t-n}R^{n-2t}$, this is $C_{n,t}'\,R^{n-2t}$ with $C_{n,t}' = C_n^{\,t}\,\omega_{n-1}\,2^{2t-n}/(2t-n)$.
> **Case $1 \le R < \sqrt n$.** Here $R^{n-2t}$ is bounded below by $(\sqrt n)^{n-2t} > 0$ (the exponent $n-2t < 0$ and $R < \sqrt n$), while the tail sum is at most the full sum $\Sigma(t) < \infty$ from Step 1. Hence $\sum_{\lvert\xi\rvert\ge R}(1+\lvert\xi\rvert^2)^{-t} \le \Sigma(t) = \Sigma(t)\,(\sqrt n)^{2t-n}\,(\sqrt n)^{n-2t} \le \Sigma(t)\,(\sqrt n)^{2t-n}\,R^{n-2t}$, the last step because $R^{n-2t} \ge (\sqrt n)^{n-2t}$. Taking $C_{n,t} = \max\{C_{n,t}',\ \Sigma(t)(\sqrt n)^{2t-n}\}$ covers both cases and proves statement 2.

**Step 4: The exact value $\sum_{m\in\mathbb{Z}}(1+m^2)^{-1} = \pi\coth\pi$ (statement 3).**

> [!note]- Derivation
> This is a check, not part of the convergence proof; the identity is quoted as bold context and confirmed numerically.
>
> **The identity.** The hyperbolic cotangent has the Mittag–Leffler (partial-fraction) expansion
> $$\pi\coth(\pi z) = \frac1z + \sum_{m=1}^\infty \frac{2z}{z^2 + m^2}, \qquad z \in \mathbb{C}\setminus i\mathbb{Z},$$
> **a standard complex-analysis result** (the sum of residues of $\pi\coth(\pi w)/(w^2 - \cdots)$, or equivalently the substitution $z \mapsto iz$ in the cotangent expansion $\pi\cot(\pi z) = \tfrac1z + \sum_{m\ge1}\tfrac{2z}{z^2 - m^2}$; it is proved in the complex-analysis chapter and is used here only as recalled context, not as a proof obligation of this drill). Setting $z = 1$,
> $$\pi\coth\pi = 1 + \sum_{m=1}^\infty \frac{2}{1 + m^2}.$$
> On the other hand, splitting the doubly-infinite lattice sum into $m = 0$ and the symmetric pair $\pm m$,
> $$\sum_{m\in\mathbb{Z}}\frac{1}{1+m^2} = \frac{1}{1+0^2} + \sum_{m=1}^\infty\left(\frac{1}{1+m^2} + \frac{1}{1+(-m)^2}\right) = 1 + \sum_{m=1}^\infty\frac{2}{1+m^2} \qquad \text{(} (-m)^2 = m^2\text{)},$$
> which is the same expression. Hence $\sum_{m\in\mathbb{Z}}(1+m^2)^{-1} = \pi\coth\pi$.
>
> **Numerical check.** With $\coth\pi = \cosh\pi/\sinh\pi \approx 11.5920/11.5487 \approx 1.003742$, the closed form is $\pi\coth\pi \approx 3.14159\times1.003742 \approx 3.1534$. The partial sums confirm this: $1 + 2\sum_{m=1}^{M}\tfrac1{1+m^2}$ gives $2.9000$ at $M = 4$, $3.0642$ at $M = 10$, $3.1234$ at $M = 40$, and $3.1436$ at $M = 200$, increasing toward $3.1534$; the remaining gap at $M = 200$ is consistent with the tail estimate of Step 3, which for $n = 1$, $t = 1$ predicts a tail of order $\sum_{m > M} m^{-2} \sim M^{-1} = R^{n-2t}$ with $R = M$, i.e. about $2/200 = 0.010$ at $M = 200$, matching $3.1534 - 3.1436 \approx 0.0098$.

> [!note]- Complete formal solution
> **Claim.** For $n \ge 1$ and $t \in \mathbb{R}$: $\Sigma(t) = \sum_{\xi\in\mathbb{Z}^n}(1+\lvert\xi\rvert^2)^{-t} < \infty$ iff $2t > n$; and for $2t > n$, $\sum_{\lvert\xi\rvert\ge R}(1+\lvert\xi\rvert^2)^{-t} \le C_{n,t}R^{n-2t}$ for $R \ge 1$.
>
> If $t \le 0$ every term is $\ge 1$, so $\Sigma(t) = \infty$ and $2t \le 0 < n$; both sides of the criterion agree. Assume $t > 0$.
>
> For $x \in Q_\xi := \xi + [-\tfrac12,\tfrac12]^n$ one has $\lvert\lvert x\rvert - \lvert\xi\rvert\rvert \le \tfrac{\sqrt n}2$, whence $1 + \lvert x\rvert^2 \le (1+\tfrac{3n}4)(1+\lvert\xi\rvert^2) =: C_n(1+\lvert\xi\rvert^2)$ always, and $1+\lvert x\rvert^2 \ge \tfrac14(1+\lvert\xi\rvert^2)$ whenever $\lvert\xi\rvert \ge \sqrt n$.
>
> *Convergence, $2t > n$.* Raising the upper bound to $-t$ and integrating over $Q_\xi$ (volume $1$): $(1+\lvert\xi\rvert^2)^{-t} \le C_n^{\,t}\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t}$. Summing over the disjoint tiling, $\Sigma(t) \le C_n^{\,t}\int_{\mathbb{R}^n}(1+\lvert x\rvert^2)^{-t}\,dx = C_n^{\,t}\omega_{n-1}\int_0^\infty(1+r^2)^{-t}r^{n-1}\,dr$; the radial integral is finite because near $\infty$ the integrand is $\le r^{n-1-2t}$ with $n-1-2t < -1$.
>
> *Divergence, $2t \le n$.* Raising the lower bound to $-t$ and integrating over $Q_\xi$ ($\lvert\xi\rvert\ge\sqrt n$): $\int_{Q_\xi}(1+\lvert x\rvert^2)^{-t} \le 4^t(1+\lvert\xi\rvert^2)^{-t}$. Summing over $\lvert\xi\rvert\ge\sqrt n$ and using $\{\lvert x\rvert\ge 2\sqrt n\}\subseteq\bigcup Q_\xi$: $\Sigma(t) \ge 4^{-t}\int_{\lvert x\rvert\ge 2\sqrt n}(1+\lvert x\rvert^2)^{-t}\,dx = 4^{-t}\omega_{n-1}\int_{2\sqrt n}^\infty(1+r^2)^{-t}r^{n-1}\,dr = \infty$, since the integrand is $\ge 2^{-t}r^{n-1-2t}$ with $n-1-2t \ge -1$.
>
> *Tail.* For $R \ge \sqrt n$: $\sum_{\lvert\xi\rvert\ge R}(1+\lvert\xi\rvert^2)^{-t} \le C_n^t\int_{\lvert x\rvert\ge R/2}(1+\lvert x\rvert^2)^{-t}\,dx \le C_n^t\omega_{n-1}\int_{R/2}^\infty r^{n-1-2t}\,dr = C_n^t\omega_{n-1}\tfrac{(R/2)^{n-2t}}{2t-n}$, of the form $C_{n,t}R^{n-2t}$. For $1\le R<\sqrt n$ the tail is $\le\Sigma(t) \le \Sigma(t)(\sqrt n)^{2t-n}R^{n-2t}$. Enlarging $C_{n,t}$ to the max covers all $R\ge1$.
>
> In the model case $n=1,t=1$ ($2 > 1$) the sum equals $\pi\coth\pi$ by the partial-fraction expansion of $\coth$ at $z=1$. $\blacksquare$

> [!warning] Illegal but tempting: comparing term-by-term without the cube volume
> A common slip is to write "$(1+\lvert\xi\rvert^2)^{-t} \approx (1+\lvert x\rvert^2)^{-t}$ for $x$ near $\xi$, so $\Sigma(t) \approx \int f$" without the unit cubes, or to compare the term to the integrand at the *single* point $x = \xi$ (which gives $(1+\lvert\xi\rvert^2)^{-t}$ back, a tautology). The comparison only becomes an inequality between the sum and the *integral* once each term is matched to the integral of $f$ over a set of volume $1$ — that is what the cube $Q_\xi$ supplies, and it is why the disjoint-tiling property (each $x\in\mathbb{R}^n$ lies in exactly one $Q_\xi$) is essential: it prevents double-counting when the per-cube bounds are summed. Dropping the cubes also loses the two-sided nature of the comparison and hence the *divergence* half, which needs a lower bound on the term by a piece of the integral.

> [!note]- Independent sanity check (the integral test in one dimension)
> For $n = 1$ the criterion says $\sum_m(1+m^2)^{-t}$ converges iff $t > \tfrac12$. This matches the classical integral test directly: $(1+m^2)^{-t} \asymp m^{-2t}$ for large $m$, and $\sum m^{-2t}$ converges iff $2t > 1$, i.e. $t > \tfrac12$ — the same threshold, with no cubes needed in dimension one. The cube machinery is what upgrades this one-dimensional integral test to all $n$, where "how many terms have $\lvert\xi\rvert\approx R$" is the volume of a shell, $\sim R^{n-1}$, rather than the two endpoints $\pm R$.

---

# Key Takeaways

**A sum of a positive, radially monotone weight over a lattice converges exactly when the integral of that weight converges, and the proof is a two-sided cube comparison.** The reusable principle is that $\sum_{\xi\in\mathbb{Z}^n} f(\xi)$ and $\int_{\mathbb{R}^n} f$ share the same convergence behaviour whenever $f > 0$ is (eventually) monotone in $\lvert x\rvert$, because attaching a unit cube to each lattice point trades the sum for the integral up to a bounded factor. The trigger to use this is any lattice sum whose summand is a sampled smooth decaying function; the diagnostic is to ask "what is $\int_{\mathbb{R}^n} f$, and does it converge?" — the answer transfers to the sum verbatim. This is the multidimensional integral test, and it is the standard route to the convergence of Epstein zeta functions, Eisenstein series, and every Sobolev-space weight sum in this chapter. The one subtlety to remember for spaced recall is that the two directions need *opposite* comparisons: bound the term above by the cube integral for convergence, below (away from the origin) for divergence.

**The convergence threshold is dimension counting: the number of lattice points in a shell of radius $R$ grows like $R^{n-1}$, so a weight $R^{-2t}$ summed over shells behaves like $\int R^{n-1-2t}\,dR$.** The single inequality $2t > n$ is the statement $n - 1 - 2t < -1$, and it is worth carrying the shell picture rather than the formula: a spherical shell $\{R \le \lvert\xi\rvert < R+1\}$ contains on the order of $R^{n-1}$ lattice points (its volume), each contributing about $R^{-2t}$, so the shell contributes $R^{n-1-2t}$ and the whole sum behaves like the radial integral. This is the exact mechanism by which every embedding in the chapter turns "surplus derivatives beat the dimension" into a convergent series: in the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] the weight is $(1+\lvert\xi\rvert^2)^{r-k}$ and one needs $2(k-r) > n$; in the [[Thm - Rellich Compactness Theorem|Rellich theorem]] the tail estimate of Step 3 is what makes the Fourier truncations converge in operator norm. Whenever a Sobolev exponent inequality appears, it is this shell count in disguise.

**The tail rate $R^{n-2t}$, not merely finiteness, is the quantity the elliptic theory actually consumes.** Statement 1 answers "does it converge?", but the applications need the *rate* at which the tail decays, because that rate controls how fast a Fourier truncation approximates the identity. The tail bound $\sum_{\lvert\xi\rvert\ge R}(1+\lvert\xi\rvert^2)^{-t} \le C_{n,t}R^{n-2t}$ is exactly the estimate that, in the [[Thm - Rellich Compactness Theorem|Rellich compactness proof]], shows $\lVert\iota - T_R\rVert_{H_k\to H_m} \le (1+R^2)^{(m-k)/2} \to 0$ and hence that the inclusion of a higher into a lower Sobolev space is a norm-limit of finite-rank operators, therefore compact. The transferable diagnostic: when a compactness or approximation argument requires a quantitative rate, return to the integral comparison and read the rate off the radial integral $\int_{R}^\infty r^{n-1-2t}\,dr \sim R^{n-2t}$ — finiteness and rate come from the same computation, and it costs nothing extra to keep the rate. The companion exercise [[Ex - Sobolev Embedding on the Circle by Hand]] shows the other face of this sum, where the $n=1$, $t=1$ value $\pi\coth\pi$ is the exact embedding constant $W^{1,2}(S^1)\hookrightarrow C^0(S^1)$.
