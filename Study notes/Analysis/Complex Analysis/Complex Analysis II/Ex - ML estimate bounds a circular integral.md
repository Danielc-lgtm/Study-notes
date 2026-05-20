---
type: exercise
subject: complex-analysis
difficulty: "⭐"
prereqs:
  - "Thm - ML Estimate"
  - "Def - Contour Integral"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $C_R = \{z : |z| = R\}$ be the positively oriented circle of radius $R$ centred at $0$, and define
$$f(z) = \frac{z^2 + 1}{z^4 + z + 1}.$$
Show that there is a constant $C > 0$ and an $R_0 > 0$ such that
$$|f(z)| \;\leq\; \frac{C}{R^2} \qquad \text{for every } z \text{ with } |z| = R \geq R_0,$$
and use the ML estimate to deduce
$$\left|\oint_{C_R} f(z)\,dz\right| \;\xrightarrow[R \to \infty]{}\; 0.$$

Apply the same reasoning to show that for every integer $k \geq 2$,
$$\oint_{C_R} \frac{dz}{z^k} \;\xrightarrow[R \to \infty]{}\; 0,$$
and explain why this is consistent with — indeed, gives an independent proof of — the vanishing of $\int_{|z|=1} z^{-k}\,dz$ for $k \geq 2$ (the *non*-residue exponents of [[Ex - Computing zn dz on a circle]]).

**Recall:**

![[Thm - ML Estimate#Statement]]

The contour $C_R$ is a closed piecewise $C^1$ curve of length $L(C_R) = 2\pi R$; parametrising $\gamma(t) = R e^{it}$ for $t \in [0, 2\pi]$ gives $|\gamma'(t)| = R$ and $\int_0^{2\pi}R\,dt = 2\pi R$.

![[Def - Contour Integral#The Definition]]

The function $f(z) = (z^2 + 1)/(z^4 + z + 1)$ is a rational function: a ratio of two polynomials. Its only singularities in $\mathbb{C}$ are the (at most four) zeros of the denominator $z^4 + z + 1$, which lie inside some bounded disc by the fundamental theorem of algebra. For $R$ large enough, all denominator zeros are *inside* the disc of radius $R$, so $f$ is continuous on the circle $|z| = R$ and the contour integral $\oint_{C_R} f\,dz$ is well-defined.

---

# Convergent Strategy

**Problem class.** This is the *vanishing-at-infinity* problem for a rational integrand: bound a contour integral on a growing circle and prove it goes to zero. The class is identified by the prompt "$|\text{integral}| \to 0$ as $R \to \infty$" together with an integrand that decays at infinity — exactly the input pattern named in the [[Complex Analysis II — Cauchy's Theorem and its Consequences#Problem-Solving Strategy|topic-page problem-solving strategy]] for the ML estimate. The reusable shape of this problem class is: *given a rational integrand whose denominator has degree at least 2 more than the numerator, the integral around a large circle vanishes in the limit.*

**Assumption pattern.** Two structural features make this routine. First, $f$ is rational with $\deg(\text{numerator}) = 2$ and $\deg(\text{denominator}) = 4$, so $|f(z)|$ behaves like $|z|^{-2}$ for large $|z|$. Second, the contour $C_R$ has length $L = 2\pi R$, growing only *linearly* in $R$. The decisive arithmetic is then $L \cdot M(R) \sim R \cdot R^{-2} = R^{-1} \to 0$ — the denominator's degree gap wins against the linear growth of the path length. The hypothesis "$\deg(\text{denominator}) \geq \deg(\text{numerator}) + 2$" is the precise condition for this asymptotic to favour vanishing.

**Theorem routing.** The route is a single application of the [[Thm - ML Estimate|ML estimate]] with carefully chosen $M(R)$ and $L(C_R)$. Step (a): produce a polynomial-style bound $|f(z)| \leq C/R^2$ on $|z| = R$ by separately bounding the numerator from above by a power of $R$ and the denominator from below by a power of $R$ — both bounds are reverse triangle inequalities ($|z^4 + z + 1| \geq |z|^4 - |z| - 1$ for large $|z|$). Step (b): combine with $L(C_R) = 2\pi R$ via ML to get $|\oint f\,dz| \leq (C/R^2)(2\pi R) = 2\pi C/R$. Step (c): let $R \to \infty$. The same routing applies to $1/z^k$ for $k \geq 2$, with the bound $|1/z^k| = 1/R^k$ on $|z| = R$.

**Key decision point.** The non-obvious choice is *which* bound to apply to the denominator. The bound $|z^4 + z + 1| \leq |z|^4 + |z| + 1$ is the wrong direction — it bounds the numerator-style quantity, not what we need. To bound $1/|z^4 + z + 1|$ from above we must bound $|z^4 + z + 1|$ from *below*, and the reverse triangle inequality $|a + b| \geq |a| - |b|$ delivers $|z^4 + z + 1| \geq |z|^4 - |z| - 1$. For this lower bound to be positive (and dominated by $|z|^4$) we need $|z|$ large enough — hence the threshold $R_0$. Recognising that "lower bound on a denominator" needs reverse triangle inequality and a size threshold is the reusable insight; the same move appears whenever a rational integrand must be bounded on a circle.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Complex Analysis II — Cauchy's Theorem and its Consequences#Legal Operations|the topic page's Legal Operations]]:

1. **Apply the ML estimate to bound an integral** (operation 3 from the topic page). The ML estimate gives $|\oint_{C_R} f\,dz| \leq M(R) \cdot L(C_R)$, where $M(R) = \sup_{|z|=R}|f(z)|$ and $L(C_R) = 2\pi R$. The art of this exercise is in producing a tight upper bound on $M(R)$ and watching it beat the linear growth of $L(C_R)$ to give a vanishing product.

2. **Bound a rational function by polynomial inequalities on a circle**. To bound $M(R)$, bound the numerator $|z^2 + 1|$ from above by $R^2 + 1$ (forward triangle inequality) and the denominator $|z^4 + z + 1|$ from below by $R^4 - R - 1$ (reverse triangle inequality). For $R \geq R_0$ large enough, $R^4 - R - 1 \geq \tfrac{1}{2}R^4$, so $|f| \leq (R^2 + 1)/(\tfrac{1}{2}R^4) \leq C/R^2$ with $C = 4$ (a uniform constant once $R \geq R_0$).

3. **Take the limit $R \to \infty$.** With the bound $|\oint f\,dz| \leq 2\pi C/R$, sending $R \to \infty$ gives a vanishing right-hand side, hence a vanishing left-hand side.

---

# Hints

> [!note]- Hint 1
> Identify what the [[Thm - ML Estimate|ML estimate]] needs: a uniform bound on $|f|$ over the path, and the length of the path. The length is easy: a circle of radius $R$ has length $2\pi R$. The work is in bounding $|f|$ on the circle.

> [!note]- Hint 2
> To bound the rational function $f(z) = (z^2 + 1)/(z^4 + z + 1)$ on $|z| = R$: bound the numerator *from above* by the forward triangle inequality $|z^2 + 1| \leq |z|^2 + 1 = R^2 + 1$, and the denominator *from below* by the reverse triangle inequality $|z^4 + z + 1| \geq |z|^4 - |z| - 1 = R^4 - R - 1$.

> [!note]- Hint 3
> For $R$ large enough, $R^4 - R - 1 \geq \tfrac{1}{2}R^4$ (any sub-quartic correction is dominated). So $|f| \leq (R^2 + 1)/(\tfrac{1}{2}R^4) \leq 2 \cdot 2 R^2/R^4 = 4/R^2$ for $R$ large. ML then gives $|\oint f\,dz| \leq (4/R^2)(2\pi R) = 8\pi/R$, which tends to $0$.

> [!note]- Hint 4
> For $1/z^k$ with $k \geq 2$: $|1/z^k| = 1/R^k$ on $|z| = R$, so $|\oint dz/z^k| \leq (1/R^k)(2\pi R) = 2\pi/R^{k-1} \to 0$ as $R \to \infty$. The vanishing requires $k - 1 \geq 1$, i.e., $k \geq 2$. The borderline case $k = 1$ is the residue case and *cannot* be killed this way — and indeed the integral is $2\pi i$, not zero.

---

# Solution

The plan is to package the ML estimate around a careful polynomial bound: Step 1 produces an upper bound for the numerator and a lower bound for the denominator using triangle inequalities, combining to $|f(z)| \leq C/R^2$ on $|z| = R$ for $R$ large; Step 2 multiplies by the length $L(C_R) = 2\pi R$ and passes to the limit; Step 3 specialises to $1/z^k$, exhibiting the same routing as a sanity check.

**Step 1: Polynomial bound $|f(z)| \leq C/R^2$ on $|z| = R$ for $R \geq R_0$.**

There is an $R_0 > 0$ (concretely $R_0 = 2$ works) and a constant $C = 4$ such that
$$|f(z)| \;\leq\; \frac{C}{R^2} \qquad \text{whenever } |z| = R \geq R_0.$$

> [!note]- Derivation
> Fix $z$ with $|z| = R$. The numerator satisfies the *forward* triangle inequality
> $$|z^2 + 1| \;\leq\; |z|^2 + 1 \;=\; R^2 + 1.$$
>
> The denominator requires a *lower* bound, since it appears in the denominator of $|f|$. By the reverse triangle inequality $|a + b + c| \geq |a| - |b| - |c|$:
> $$|z^4 + z + 1| \;\geq\; |z|^4 - |z| - 1 \;=\; R^4 - R - 1.$$
>
> For this lower bound to be positive, we need $R^4 \geq R + 1$. For $R \geq 2$, $R^4 \geq 16$ and $R + 1 \leq 3$, comfortably so. In fact for $R \geq 2$:
> $$R^4 - R - 1 \;\geq\; R^4 - R^4/4 - R^4/4 \;=\; \tfrac{1}{2}R^4,$$
> because $R \leq R^4/4$ and $1 \leq R^4/4$ both hold for $R \geq 2$ (the first from $R^3 \geq 8 > 4$, the second from $R^4 \geq 16 > 4$).
>
> Combining:
> $$|f(z)| \;=\; \frac{|z^2 + 1|}{|z^4 + z + 1|} \;\leq\; \frac{R^2 + 1}{\tfrac{1}{2}R^4} \;=\; \frac{2(R^2 + 1)}{R^4}.$$
> For $R \geq 2$, $R^2 + 1 \leq 2R^2$, so
> $$|f(z)| \;\leq\; \frac{2 \cdot 2R^2}{R^4} \;=\; \frac{4}{R^2}.$$
>
> Setting $C = 4$ and $R_0 = 2$ completes Step 1. (The constants are not sharp; any $C, R_0$ with the stated form work.)

**Step 2: Apply ML and let $R \to \infty$.**

By the [[Thm - ML Estimate|ML estimate]] with $M = C/R^2 = 4/R^2$ and $L = 2\pi R$:
$$\left|\oint_{C_R} f(z)\,dz\right| \;\leq\; M \cdot L \;=\; \frac{4}{R^2} \cdot 2\pi R \;=\; \frac{8\pi}{R} \;\xrightarrow[R \to \infty]{}\; 0.$$

> [!note]- Derivation
> Apply the [[Thm - ML Estimate|ML estimate]] to the closed curve $C_R$ of length $L(C_R) = 2\pi R$ (parametrise $\gamma(t) = R e^{it}$, $t \in [0, 2\pi]$, so $|\gamma'(t)| = R$ and $\int_0^{2\pi} R\,dt = 2\pi R$). The bound $|f| \leq 4/R^2$ on $C_R$ is uniform from Step 1, so
> $$\left|\oint_{C_R} f\,dz\right| \;\leq\; \sup_{|z|=R}|f(z)| \cdot L(C_R) \;\leq\; \frac{4}{R^2} \cdot 2\pi R \;=\; \frac{8\pi}{R}.$$
>
> The right-hand side tends to $0$ as $R \to \infty$. By the squeeze theorem (the modulus is nonnegative and is bounded above by something tending to zero):
> $$\left|\oint_{C_R} f(z)\,dz\right| \;\longrightarrow\; 0.$$

**Step 3: The corresponding result for $1/z^k$ with $k \geq 2$.**

For every integer $k \geq 2$ and every $R > 0$, $\left|\oint_{C_R} z^{-k}\,dz\right| \leq 2\pi/R^{k-1}$, hence tends to zero as $R \to \infty$.

> [!note]- Derivation
> On the circle $|z| = R$, $|z^{-k}| = R^{-k}$ pointwise, so $M = R^{-k}$. The length is again $L(C_R) = 2\pi R$. The [[Thm - ML Estimate|ML estimate]] gives
> $$\left|\oint_{C_R} \frac{dz}{z^k}\right| \;\leq\; R^{-k} \cdot 2\pi R \;=\; \frac{2\pi}{R^{k-1}}.$$
> For $k \geq 2$, $k - 1 \geq 1$, so $R^{-(k-1)} \to 0$ as $R \to \infty$, and the integral vanishes in the limit.
>
> This is consistent with the direct computation in [[Ex - Computing zn dz on a circle]]: for $n = -k$ with $k \geq 2$, $\int_{|z|=1} z^{-k}\,dz = 0$ (because $z^{-k}$ has the primitive $z^{-k+1}/(-k+1)$ on $\mathbb{C}^\times$ when $-k + 1 \neq 0$, i.e., $k \neq 1$). In fact, by the [[Thm - Fundamental Theorem of Contour Integration|fundamental theorem of contour integration]] the integral is the *same* (= $0$) for every $R > 0$, not just in the limit. The ML route is *not* the most efficient computation; it is, however, the most *transferable*, because it does not rely on knowing a primitive — only on the decay of the integrand and the length of the path.
>
> The borderline case $k = 1$ is the *residue* case. Here $|1/z| = 1/R$ on $|z| = R$ and $L(C_R) = 2\pi R$, so the ML bound is $|1/R \cdot 2\pi R| = 2\pi$ — a *constant*, not a vanishing quantity. The ML estimate is too weak to detect cancellation, and indeed $\oint_{|z|=R} dz/z = 2\pi i \neq 0$. The ML route therefore *correctly* fails to certify vanishing in the one case where vanishing actually fails.

> [!note]- Complete formal solution
> Fix $R \geq 2$. On the circle $|z| = R$:
> - $|z^2 + 1| \leq R^2 + 1 \leq 2R^2$ (forward triangle inequality plus $R \geq 1$).
> - $|z^4 + z + 1| \geq R^4 - R - 1 \geq \tfrac{1}{2}R^4$ (reverse triangle inequality; the second step uses $R \geq 2$, which gives $R \leq R^4/4$ and $1 \leq R^4/4$).
>
> Therefore on $|z| = R$ with $R \geq 2$,
> $$|f(z)| \;=\; \frac{|z^2 + 1|}{|z^4 + z + 1|} \;\leq\; \frac{2R^2}{\tfrac{1}{2}R^4} \;=\; \frac{4}{R^2}.$$
>
> By the [[Thm - ML Estimate|ML estimate]] applied to the closed curve $C_R$ of length $2\pi R$,
> $$\left|\oint_{C_R} f(z)\,dz\right| \;\leq\; \frac{4}{R^2} \cdot 2\pi R \;=\; \frac{8\pi}{R} \;\xrightarrow[R \to \infty]{}\; 0.$$
>
> The same routing for $1/z^k$ ($k \geq 2$) gives $|1/z^k| = 1/R^k$ on $|z| = R$ and $|\oint dz/z^k| \leq 2\pi/R^{k-1} \to 0$. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to bound $|z^4 + z + 1|$ from below by the *forward* triangle inequality, writing $|z^4 + z + 1| \leq R^4 + R + 1$. This is the wrong direction: bounding the denominator from above and the numerator from above gives a bound on $|f|$ that goes the wrong way — it is *useless* for bounding $|f|$ from above. The correct direction for a denominator is always the *reverse* triangle inequality. The trigger is precise: any time a quantity appears in a denominator and you want to control $|f|$ from above, you bound the denominator from *below*, hence reverse triangle inequality.

---

# Key Takeaways

**The denominator-degree-gap heuristic for vanishing on large circles.**

The result you have just proved is a special case of a general pattern: *if $f$ is a rational function with $\deg(\text{denominator}) \geq \deg(\text{numerator}) + 2$, then $\oint_{|z| = R} f\,dz \to 0$ as $R \to \infty$.* The asymptotic $|f(z)| \sim C |z|^{\deg n - \deg d}$ for large $|z|$ combines with the path length $L = 2\pi R$ via ML to give $|\text{integral}| \lesssim R^{1 + \deg n - \deg d}$, which vanishes exactly when $\deg d - \deg n \geq 2$. The borderline case $\deg d - \deg n = 1$ is the residue case: the ML estimate alone is too weak, and the integral might or might not vanish (it does *not* for $1/z$; it does for $1/(z - a)$ when the contour does not enclose $a$). This rule of thumb is the *first thing* to check whenever a real or complex integral is being computed by closing a contour at infinity — half-disc, large semicircle, full circle — and the question is whether the closing contour contributes anything in the limit. Real-variable applications include computing $\int_{-\infty}^\infty x^{-2}/(1 + x^2)\,dx$ by closing the real line with an upper semicircle; the semicircle vanishes because the denominator beats the numerator by two degrees.

**ML is the bound-and-let-it-go-to-zero machine.**

The ML estimate has one job: convert a uniform bound on the integrand and a length of the path into a bound on the integral. It is *not* the tool for computing exact values — that is what the [[Thm - Cauchy Integral Formula|CIF]] and residues are for. ML is the tool for showing an integral *vanishes in a limit*: as the path shrinks (small-circle bounds in CIF proofs), as the path grows (large-circle bounds in real-integral computations), or as a parameter degrades the integrand. The recognition trigger is structural: any time you see "show that this integral $\to 0$ as some scale goes to a limit," reach for ML, identify what bounds $|f|$ on the limiting family of paths, and compute $M \cdot L$ — the answer is usually obvious once both pieces are in hand. This is the *single most reusable* analytical move in §2, and recognising the trigger pattern is what makes a problem like the one above feel routine.

**Reverse triangle inequality for denominators, forward for numerators.**

The reverse triangle inequality $|a + b| \geq |a| - |b|$ (equivalently $||a| - |b|| \leq |a + b|$) is the indispensable companion of the forward inequality $|a + b| \leq |a| + |b|$ in any estimate involving a rational integrand. The trigger-reaction pattern is concrete: numerator appearing in $|f|$ from above $\Rightarrow$ forward triangle (over-estimate); denominator appearing in $|f|$ from above $\Rightarrow$ reverse triangle on the denominator (under-estimate the denominator $\Rightarrow$ over-estimate its reciprocal). The size threshold $|z| \geq R_0$ is the price of using the reverse triangle inequality: the lower bound $|z|^n - \text{lower-order corrections}$ is only positive (and only dominant) once $|z|$ is large enough. Whenever this threshold appears in a proof, the reason is the reverse triangle inequality on a denominator polynomial; recognising the pattern saves time both in reading and in writing such estimates.

**Why the residue case escapes this argument.**

The ML estimate's inability to certify vanishing for $1/z$ is structurally informative: it tells us that the vanishing of contour integrals on large circles is *not* simply a consequence of integrand decay. Real cancellation is doing work, and the residue case $1/z$ is precisely where no cancellation occurs over a closed loop around the singularity. This is why §2 progresses from ML (a coarse, pointwise bound) through Cauchy's theorem (a topological vanishing statement) to residues in [[Complex Analysis III — Winding, Laurent, Residues|CA III]] (a fine, cancellation-detecting tool). The hierarchy of strength is: ML detects asymptotic decay; Cauchy detects holomorphicity-and-topology; residues detect singularity-by-singularity contribution. Each new tool exists precisely because the previous one is too weak in a specific structural situation — and the present exercise lives at the level where ML suffices, with the boundary $k = 1$ marking exactly where the next tool becomes necessary.
