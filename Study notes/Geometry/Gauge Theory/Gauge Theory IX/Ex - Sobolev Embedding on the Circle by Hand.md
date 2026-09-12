---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Sobolev Embedding Theorem"
  - "Def - Sobolev Space of Sections"
  - "Thm - Cauchy-Schwarz Inequality"
  - "Thm - Convergence of the Lattice Sum"
tags: [geometry, gauge-theory, analysis]
---

# Problem Statement

Let $S^1 = \mathbb{R}/2\pi\mathbb{Z}$ be the circle of circumference $2\pi$, with the standard coordinate $\theta$ and the flat metric $d\theta^2$. For a smooth real-valued function $u \in C^\infty(S^1;\mathbb{R})$ write
$$\lVert u \rVert_{C^0} := \sup_{\theta \in S^1} \lvert u(\theta)\rvert, \qquad \lVert u \rVert_{W^{1,2}}^2 := \int_0^{2\pi}\big(u(\theta)^2 + u'(\theta)^2\big)\,d\theta,$$
and set $\bar u := \tfrac{1}{2\pi}\int_0^{2\pi} u(\theta)\,d\theta$ for the mean value of $u$.

Prove the following three statements, **entirely by hand** — that is, using only the fundamental theorem of calculus, the intermediate value theorem, and the Cauchy–Schwarz inequality, with no appeal to the general Sobolev machinery.

1. **(Pointwise bound.)** For every $u \in C^\infty(S^1;\mathbb{R})$,
$$\lVert u \rVert_{C^0} \;\le\; \sqrt{2\pi}\,\lVert u \rVert_{W^{1,2}} + \frac{1}{2\pi}\left\lvert \int_0^{2\pi} u\,d\theta \right\rvert \;\le\; \Big(\sqrt{2\pi} + \tfrac{1}{\sqrt{2\pi}}\Big)\lVert u \rVert_{W^{1,2}}.$$
In particular the identity inclusion $C^\infty(S^1) \hookrightarrow C^0(S^1)$ is bounded for the $W^{1,2}$ norm, and hence extends to a continuous embedding $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$.

2. **(Hölder-$\tfrac12$ modulus of continuity.)** For every $u \in C^\infty(S^1;\mathbb{R})$ and all $\theta_1, \theta_2 \in S^1$,
$$\lvert u(\theta_1) - u(\theta_2)\rvert \;\le\; \lVert u \rVert_{W^{1,2}}\,\operatorname{dist}(\theta_1,\theta_2)^{1/2},$$
where $\operatorname{dist}(\theta_1,\theta_2) = \min\{\lvert \theta_1 - \theta_2\rvert,\, 2\pi - \lvert\theta_1 - \theta_2\rvert\} \le \pi$ is the geodesic distance on $S^1$. Consequently a sequence bounded in $W^{1,2}(S^1)$ is uniformly bounded and equicontinuous.

3. **(Comparison with the Fourier proof.)** Give the second, independent proof of statement 1 through the Fourier expansion $u = \sum_{m\in\mathbb{Z}} c_m e^{im\theta}$, obtaining the explicit constant
$$\lVert u \rVert_{C^0} \;\le\; \Big(\tfrac{\coth\pi}{2}\Big)^{1/2}\lVert u \rVert_{W^{1,2}},$$
and identify precisely where the convergence of the lattice sum $\sum_{m\in\mathbb{Z}}(1+m^2)^{-1} < \infty$ enters, and what the Fourier proof reveals that the hand proof conceals.

This is Haydys's Remark 138, the one-dimensional model case that stands in for the omitted proof of the general Sobolev embedding theorem. The point of the exercise is to see, in the smallest possible dimension, exactly why one derivative in $L^2$ buys continuity — and to watch the same fact reappear as a convergence condition on a lattice sum once the argument is transported to the Fourier side.

> [!warning] Source correction
> Haydys's Remark 138 (his estimate (139)) states the Hölder bound with the constant $\sqrt{2\pi}$: $\lvert u(\theta_1)-u(\theta_2)\rvert \le \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}}\operatorname{dist}(\theta_1,\theta_2)^{1/2}$. That constant is not tight. Cauchy–Schwarz applied on the arc between $\theta_1$ and $\theta_2$ yields the arc-length factor $\operatorname{dist}(\theta_1,\theta_2)^{1/2}$ **and no more**; the extra $\sqrt{2\pi}$ arises only if one first over-bounds the arc length by the full circumference $2\pi$ (which is the right move for the *uniform* pointwise bound in statement 1, but double-counts here). The corrected constant is $1$, as proved below. The looser constant $\sqrt{2\pi}$ is of course also valid and suffices for every qualitative consequence (uniform boundedness, equicontinuity, compactness).

**Recall.**

The three named objects are the Sobolev space $W^{1,2}(S^1)$, the Sobolev embedding theorem whose one-dimensional shadow we are reconstructing, and the Cauchy–Schwarz inequality that does all the analytic work.

![[Def - Sobolev Space of Sections#The Definition]]

For the circle with its single chart, the space $W^{1,2}(S^1;\mathbb{R})$ is the completion of $C^\infty(S^1;\mathbb{R})$ in the norm $\lVert u\rVert_{W^{1,2}}^2 = \int_0^{2\pi}(u^2 + (u')^2)\,d\theta$; equivalently, the space of $u \in L^2(S^1)$ whose distributional derivative $u'$ is also in $L^2(S^1)$. Here $n = \dim S^1 = 1$, the bundle $E$ is the trivial real line bundle, and $k = 1$, $p = 2$.

![[Thm - Sobolev Embedding Theorem#Statement]]

The one-dimensional instance we reprove is: with $n = 1$, $k = 1$, $r = 0$, the condition $k - \tfrac n2 = \tfrac12 > 0 = r$ holds, so the [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] predicts a continuous injection $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$. This exercise proves exactly that inclusion, twice, without invoking the theorem itself.

![[Thm - Cauchy-Schwarz Inequality#Statement]]

We use the [[Thm - Cauchy-Schwarz Inequality|Cauchy–Schwarz inequality]] in two of its incarnations. On the inner-product space $L^2(I)$ of square-integrable functions on an interval $I$, with inner product $\langle f,g\rangle = \int_I fg$, it reads $\big\lvert\int_I fg\big\rvert \le \big(\int_I f^2\big)^{1/2}\big(\int_I g^2\big)^{1/2}$. On the inner-product space $\ell^2(\mathbb{Z})$ of square-summable sequences, with inner product $\langle a,b\rangle = \sum_m a_m \overline{b_m}$, it reads $\big\lvert\sum_m a_m \overline{b_m}\big\rvert \le \big(\sum_m \lvert a_m\rvert^2\big)^{1/2}\big(\sum_m \lvert b_m\rvert^2\big)^{1/2}$. Both are instances of the single inequality proved on the linked page.

![[Thm - Convergence of the Lattice Sum#Statement]]

The Fourier proof needs one numerical input: that $\sum_{m\in\mathbb{Z}}(1+m^2)^{-1} < \infty$. This is the [[Thm - Convergence of the Lattice Sum|lattice-sum theorem]] in dimension $n = 1$ with exponent $t = 1$, where the convergence criterion $2t > n$ becomes $2 > 1$. The companion drill [[Ex - The Lattice Sum Converges iff 2t Exceeds n]] proves this criterion in full and evaluates the $n=1$, $t=1$ sum exactly.

---

# Convergent Strategy

**Problem class.** This is a *reconstruct-an-a-priori-estimate* problem: we are given a smooth function and must bound its supremum norm — a $C^0$ quantity — by a norm involving only its $L^2$ size and the $L^2$ size of one derivative. The signature of the class is that the target is a pointwise supremum while the data is an integral, so the whole game is to *convert an integral of a derivative into a pointwise increment*, which is exactly what the fundamental theorem of calculus does. Every Sobolev embedding, in every dimension, is at bottom this conversion; dimension one lets us do it with a single integral rather than through the Fourier transform or a Green's-function representation.

**Assumption pattern.** The hypothesis $u \in C^\infty(S^1)$ is used only to make the fundamental theorem of calculus and the intermediate value theorem available on the nose; the final inequalities involve only $\lVert u\rVert_{W^{1,2}}$, so they survive the passage to the completion $W^{1,2}(S^1)$ by density. The compactness of $S^1$ enters twice and must not be overlooked: it gives the finite total length $2\pi$ that bounds the arc-length factor, and it lets the intermediate value theorem produce a point where the mean-zero part vanishes. On a non-compact domain — the real line — both of these fail, and indeed the embedding $W^{1,2}(\mathbb{R}) \hookrightarrow C^0(\mathbb{R})$ still holds but the *compactness* of the inclusion into $L^2$ does not (this is the subject of the companion exercise [[Ex - Rellich Fails on Non-Compact Domains]]).

**Theorem routing.** The route for statements 1 and 2 is: split $u = \bar u + u_0$ into its mean and its mean-zero part; use the **intermediate value theorem** to find a zero $\theta_0$ of $u_0$; use the **fundamental theorem of calculus** to write $u_0(\theta) = \int_{\theta_0}^\theta u_0'$; bound that integral by **Cauchy–Schwarz** in $L^2$, once with the arc-length factor over-estimated by $2\pi$ (giving the uniform bound) and once with it kept sharp (giving the Hölder modulus). The route for statement 3 is entirely different: expand in the Fourier basis, apply **Parseval** to turn the $W^{1,2}$ norm into the weighted sum $2\pi\sum(1+m^2)\lvert c_m\rvert^2$, bound $\sup\lvert u\rvert$ by $\sum\lvert c_m\rvert$, and split $\lvert c_m\rvert = (1+m^2)^{-1/2}\cdot(1+m^2)^{1/2}\lvert c_m\rvert$ so that **Cauchy–Schwarz on $\ell^2$** produces the convergent factor $\sum(1+m^2)^{-1}$ — the [[Thm - Convergence of the Lattice Sum|lattice sum]].

**Key decision point.** The one non-obvious move in the hand proof is the split $u = \bar u + u_0$ into mean and mean-zero part. Without it the fundamental theorem of calculus has no natural base point: a general smooth function has no distinguished zero. Subtracting the mean manufactures one, because a continuous function with zero average must — by the intermediate value theorem on the connected circle — take the value zero somewhere. In the Fourier proof the analogous decisive move is the *insertion of the weight* $1 = (1+m^2)^{-1/2}(1+m^2)^{1/2}$ before applying Cauchy–Schwarz: this is the discrete counterpart of the same idea, apportioning "one power of the derivative" to control the summability of the tail.

---

# Legal Operations Used

This solution uses the following operations, named descriptively (the §9.2 topic page's numbered Legal Operations register will subsume them).

1. **Split off the mean (orthogonal decomposition against the constants).** Write $u = \bar u + u_0$ with $\bar u = \tfrac1{2\pi}\int u$ constant and $\int_{S^1} u_0 = 0$. This is the $L^2$-orthogonal projection onto the one-dimensional space of constants and its complement; it isolates the part of $u$ that the derivative controls.

2. **Manufacture a base point with the intermediate value theorem.** A continuous mean-zero function on the connected circle attains the value $0$; use this to locate $\theta_0$ with $u_0(\theta_0) = 0$, so that the fundamental theorem of calculus has somewhere to start.

3. **Represent an increment as an integral of the derivative (fundamental theorem of calculus).** Write $u_0(\theta) - u_0(\theta_0) = \int_{\theta_0}^\theta u_0'\,d\varphi$; this converts the pointwise value into an integral to which Cauchy–Schwarz applies.

4. **Bound an integral of a product by Cauchy–Schwarz in $L^2$.** Estimate $\int_{\theta_0}^\theta 1\cdot u_0'$ by $(\int 1^2)^{1/2}(\int (u_0')^2)^{1/2}$, controlling the derivative factor by $\lVert u_0'\rVert_{L^2} \le \lVert u\rVert_{W^{1,2}}$ and the length factor by the arc length.

5. **Insert a weighted unit and apply Cauchy–Schwarz on $\ell^2$ (the Fourier route).** Write $\lvert c_m\rvert = (1+m^2)^{-1/2}\cdot(1+m^2)^{1/2}\lvert c_m\rvert$ and split by Cauchy–Schwarz to separate a convergent weight sum from the $W^{1,2}$ Fourier norm.

6. **Extend a bounded operator from a dense subspace to its completion.** Having proved the inequality on the dense subspace $C^\infty(S^1) \subset W^{1,2}(S^1)$, extend the inclusion into the Banach space $C^0(S^1)$ by uniform continuity.

---

# Hints

> [!note]- Hint 1
> The target $\sup\lvert u\rvert$ is pointwise, the data $\lVert u\rVert_{W^{1,2}}$ is integral. The only elementary bridge from "the integral of the derivative" to "the value at a point" is the fundamental theorem of calculus, $u(\theta) - u(\theta_0) = \int_{\theta_0}^\theta u'$. But this needs a base point $\theta_0$. Where would a smooth function on the circle have a *distinguished* point at which its value is under control?

> [!note]- Hint 2
> Subtract the mean: $u_0 := u - \bar u$ has $\int_{S^1} u_0 = 0$. A continuous function on the connected circle with zero average cannot be everywhere positive or everywhere negative, so by the intermediate value theorem it vanishes somewhere: there is $\theta_0$ with $u_0(\theta_0) = 0$. Now the fundamental theorem of calculus gives $u_0(\theta) = \int_{\theta_0}^\theta u_0'$ with a known base value.

> [!note]- Hint 3
> Apply Cauchy–Schwarz to $\int_{\theta_0}^\theta 1\cdot u_0'\,d\varphi$: it is at most $(\int_{\theta_0}^\theta 1^2)^{1/2}(\int_{\theta_0}^\theta (u_0')^2)^{1/2}$. The second factor is at most $\lVert u_0'\rVert_{L^2(S^1)} = \lVert u'\rVert_{L^2(S^1)} \le \lVert u\rVert_{W^{1,2}}$. For statement 1 bound the first factor by $\sqrt{2\pi}$ (the whole circle); for statement 2 keep it as $\operatorname{dist}(\theta_1,\theta_2)^{1/2}$ by integrating only along the shorter arc between the two points.

> [!note]- Hint 4
> For the mean term, $\lvert\bar u\rvert = \tfrac1{2\pi}\lvert\int u\rvert \le \tfrac1{2\pi}(\int 1^2)^{1/2}(\int u^2)^{1/2} = \tfrac1{\sqrt{2\pi}}\lVert u\rVert_{L^2}$, again by Cauchy–Schwarz. Add the two contributions and use $\lVert u\rVert_{L^2}, \lVert u'\rVert_{L^2} \le \lVert u\rVert_{W^{1,2}}$.

> [!note]- Hint 5
> For the Fourier proof, expand $u = \sum_m c_m e^{im\theta}$. Parseval turns $\lVert u\rVert_{W^{1,2}}^2$ into $2\pi\sum_m(1+m^2)\lvert c_m\rvert^2$. Bound $\sup\lvert u\rvert \le \sum_m\lvert c_m\rvert$, then write $\lvert c_m\rvert = (1+m^2)^{-1/2}\cdot(1+m^2)^{1/2}\lvert c_m\rvert$ and Cauchy–Schwarz on $\ell^2(\mathbb{Z})$. One factor is $\big(\sum(1+m^2)^{-1}\big)^{1/2}$ — a lattice sum that converges because $2\cdot1 > 1$.

---

# Solution

The plan is to prove the two hand estimates from a single mechanism — decompose, locate a zero, integrate the derivative, apply Cauchy–Schwarz — and then to redo statement 1 through Fourier series so the two proofs can be compared. In the hand proof the compactness of $S^1$ shows up as the finite length $2\pi$; in the Fourier proof it shows up as the discreteness of the frequency lattice $\mathbb{Z}$ and the convergence of $\sum(1+m^2)^{-1}$. The final discussion draws out what each proof sees that the other hides.

**Step 1: Decompose $u$ into its mean and its mean-zero part, and locate a zero of the latter.**

Write $u = \bar u + u_0$ with $\bar u = \tfrac1{2\pi}\int_0^{2\pi} u\,d\theta$ and $u_0 = u - \bar u$. Then $u_0 \in C^\infty(S^1;\mathbb{R})$, $\int_{S^1} u_0 = 0$, and there exists $\theta_0 \in S^1$ with $u_0(\theta_0) = 0$.

> [!note]- Derivation
> The number $\bar u \in \mathbb{R}$ is a constant, and $u_0 := u - \bar u$ is smooth because $u$ is. Its integral is
> $$\int_0^{2\pi} u_0\,d\theta = \int_0^{2\pi} u\,d\theta - 2\pi\,\bar u = \int_0^{2\pi} u\,d\theta - \int_0^{2\pi} u\,d\theta = 0 \qquad \text{(definition of } \bar u\text{)}.$$
> **Locate a zero of $u_0$.** Suppose, for contradiction, that $u_0(\theta) \ne 0$ for every $\theta \in S^1$. Since $u_0$ is continuous and $S^1$ is connected, its image $u_0(S^1) \subset \mathbb{R}\setminus\{0\}$ is a connected subset of $\mathbb{R}\setminus\{0\}$; the two connected components of $\mathbb{R}\setminus\{0\}$ are $(-\infty,0)$ and $(0,\infty)$, so $u_0(S^1)$ lies entirely in one of them (**by the intermediate value theorem**, in the form that a continuous function on a connected set omitting a value cannot change sign). Hence $u_0 > 0$ everywhere or $u_0 < 0$ everywhere, and in either case $\int_{S^1} u_0 \ne 0$ (the integral of a strictly signed continuous function on a set of positive measure is strictly signed), contradicting $\int_{S^1} u_0 = 0$ just shown. Therefore there exists $\theta_0 \in S^1$ with $u_0(\theta_0) = 0$.

**Step 2: Represent $u_0(\theta)$ as an integral of $u_0'$ and bound it by Cauchy–Schwarz.**

For every $\theta \in S^1$,
$$\lvert u_0(\theta)\rvert \le \sqrt{2\pi}\,\lVert u'\rVert_{L^2(S^1)} \le \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}}.$$

> [!note]- Derivation
> Fix $\theta \in S^1$ and lift both $\theta_0$ and $\theta$ to representatives in $\mathbb{R}$ with $\lvert\theta - \theta_0\rvert \le 2\pi$ (possible since the circle has circumference $2\pi$). Since $u_0 \in C^\infty$, the **fundamental theorem of calculus** gives
> $$u_0(\theta) = u_0(\theta_0) + \int_{\theta_0}^{\theta} u_0'(\varphi)\,d\varphi = \int_{\theta_0}^{\theta} u_0'(\varphi)\,d\varphi \qquad \text{(since } u_0(\theta_0) = 0 \text{ by Step 1)}.$$
> Taking absolute values and applying the **Cauchy–Schwarz inequality** in $L^2$ to the product $1 \cdot u_0'$ over the interval from $\theta_0$ to $\theta$,
> $$\lvert u_0(\theta)\rvert = \left\lvert \int_{\theta_0}^\theta 1\cdot u_0'\,d\varphi\right\rvert \le \left(\int_{\theta_0}^\theta 1^2\,d\varphi\right)^{1/2}\left(\int_{\theta_0}^\theta \lvert u_0'\rvert^2\,d\varphi\right)^{1/2} \qquad \text{(Cauchy–Schwarz in } L^2\text{)}.$$
> The first factor is $\lvert\theta - \theta_0\rvert^{1/2} \le \sqrt{2\pi}$ (bounding the interval length by the full circumference). The second factor is at most $\big(\int_0^{2\pi}\lvert u_0'\rvert^2\,d\varphi\big)^{1/2} = \lVert u_0'\rVert_{L^2(S^1)}$ (enlarging the domain of integration to all of $S^1$; the integrand is non-negative). Finally $u_0' = (u - \bar u)' = u'$ because $\bar u$ is constant, so $\lVert u_0'\rVert_{L^2} = \lVert u'\rVert_{L^2} \le \big(\int (u^2 + (u')^2)\big)^{1/2} = \lVert u\rVert_{W^{1,2}}$. Combining,
> $$\lvert u_0(\theta)\rvert \le \sqrt{2\pi}\,\lVert u'\rVert_{L^2} \le \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}}. \qquad \text{(combining the two factor bounds)}$$
> The bound is uniform in $\theta$, so $\lVert u_0\rVert_{C^0} \le \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}}$.

**Step 3: Restore the mean and assemble the pointwise bound (statement 1).**

$$\lVert u\rVert_{C^0} \le \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}} + \frac{1}{2\pi}\left\lvert\int_0^{2\pi} u\,d\theta\right\rvert \le \Big(\sqrt{2\pi} + \tfrac1{\sqrt{2\pi}}\Big)\lVert u\rVert_{W^{1,2}}.$$

> [!note]- Derivation
> Since $u = \bar u + u_0$ and $\bar u$ is constant, the triangle inequality for the supremum norm gives, for every $\theta$,
> $$\lvert u(\theta)\rvert \le \lvert\bar u\rvert + \lvert u_0(\theta)\rvert \le \lvert\bar u\rvert + \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}} \qquad \text{(by Step 2)},$$
> hence $\lVert u\rVert_{C^0} \le \lvert\bar u\rvert + \sqrt{2\pi}\,\lVert u\rVert_{W^{1,2}}$. Now $\lvert\bar u\rvert = \tfrac1{2\pi}\lvert\int_0^{2\pi} u\,d\theta\rvert$ by definition, which is the first displayed inequality. To reach the second, bound the mean by **Cauchy–Schwarz in $L^2$** applied to $1\cdot u$:
> $$\lvert\bar u\rvert = \frac{1}{2\pi}\left\lvert\int_0^{2\pi} 1\cdot u\,d\theta\right\rvert \le \frac{1}{2\pi}\left(\int_0^{2\pi} 1^2\,d\theta\right)^{1/2}\left(\int_0^{2\pi} u^2\,d\theta\right)^{1/2} = \frac{1}{2\pi}\sqrt{2\pi}\,\lVert u\rVert_{L^2} = \frac{1}{\sqrt{2\pi}}\,\lVert u\rVert_{L^2} \qquad \text{(Cauchy–Schwarz; } \int_0^{2\pi}1\,d\theta = 2\pi\text{)}.$$
> Since $\lVert u\rVert_{L^2} \le \lVert u\rVert_{W^{1,2}}$, we obtain $\lvert\bar u\rvert \le \tfrac1{\sqrt{2\pi}}\lVert u\rVert_{W^{1,2}}$, and adding to the Step-2 contribution gives the claimed constant $\sqrt{2\pi} + \tfrac1{\sqrt{2\pi}}$.

**Step 4: Extend the inclusion to $W^{1,2}(S^1)$ by density.**

The bounded inclusion $\big(C^\infty(S^1),\lVert\cdot\rVert_{W^{1,2}}\big) \hookrightarrow \big(C^0(S^1),\lVert\cdot\rVert_{C^0}\big)$ extends uniquely to a bounded linear injection $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$.

> [!note]- Derivation
> By definition $W^{1,2}(S^1)$ is the completion of $C^\infty(S^1)$ in the $\lVert\cdot\rVert_{W^{1,2}}$ norm, so $C^\infty(S^1)$ is a dense subspace. Step 3 shows the identity map $\iota : C^\infty(S^1) \to C^0(S^1)$ satisfies $\lVert\iota u\rVert_{C^0} \le C\lVert u\rVert_{W^{1,2}}$ with $C = \sqrt{2\pi} + \tfrac1{\sqrt{2\pi}}$; in particular $\iota$ is Lipschitz, hence uniformly continuous, on the dense subspace. The target $C^0(S^1)$ with the supremum norm is a **complete** normed space (a uniform limit of continuous functions is continuous). A uniformly continuous map from a dense subspace of a metric space into a complete metric space extends uniquely to a continuous map on the whole space, and the extension of a bounded linear map is bounded linear with the same bound. This produces $\bar\iota : W^{1,2}(S^1) \to C^0(S^1)$ with $\lVert\bar\iota u\rVert_{C^0} \le C\lVert u\rVert_{W^{1,2}}$ for all $u \in W^{1,2}$.
>
> **Injectivity.** If $\bar\iota u = 0$ in $C^0(S^1)$, take smooth $u_j \to u$ in $W^{1,2}$; then $u_j \to \bar\iota u = 0$ uniformly, hence $u_j \to 0$ in $L^2$ (uniform convergence on the finite-measure space $S^1$ implies $L^2$ convergence), and also $u_j \to u$ in $L^2$ (since $W^{1,2}$ convergence implies $L^2$ convergence). By uniqueness of $L^2$ limits $u = 0$. Thus $\bar\iota$ is injective, and $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$ is a continuous embedding.

**Step 5: The Hölder-$\tfrac12$ modulus of continuity (statement 2).**

For all $\theta_1,\theta_2 \in S^1$,
$$\lvert u(\theta_1) - u(\theta_2)\rvert \le \lVert u'\rVert_{L^2(S^1)}\,\operatorname{dist}(\theta_1,\theta_2)^{1/2} \le \lVert u\rVert_{W^{1,2}}\,\operatorname{dist}(\theta_1,\theta_2)^{1/2}.$$

> [!note]- Derivation
> Let $\gamma$ be the shorter of the two arcs of $S^1$ joining $\theta_1$ to $\theta_2$; its length is $\operatorname{dist}(\theta_1,\theta_2) = \min\{\lvert\theta_1-\theta_2\rvert, 2\pi - \lvert\theta_1-\theta_2\rvert\} \le \pi$. Since $u = \bar u + u_0$ with $\bar u$ constant, $u(\theta_1) - u(\theta_2) = u_0(\theta_1) - u_0(\theta_2)$, and the **fundamental theorem of calculus** along $\gamma$ gives
> $$u(\theta_1) - u(\theta_2) = \int_\gamma u'(\varphi)\,d\varphi \qquad \text{(FTC along the arc } \gamma; u_0' = u'\text{)}.$$
> Applying **Cauchy–Schwarz in $L^2(\gamma)$** to the product $1\cdot u'$,
> $$\lvert u(\theta_1) - u(\theta_2)\rvert \le \left(\int_\gamma 1^2\,d\varphi\right)^{1/2}\left(\int_\gamma \lvert u'\rvert^2\,d\varphi\right)^{1/2} \le \operatorname{dist}(\theta_1,\theta_2)^{1/2}\,\lVert u'\rVert_{L^2(S^1)} \qquad \text{(Cauchy–Schwarz; } \int_\gamma 1 = \operatorname{dist},\ \int_\gamma \lvert u'\rvert^2 \le \int_{S^1}\lvert u'\rvert^2\text{)},$$
> which is the sharp Hölder bound with constant $1$; since $\lVert u'\rVert_{L^2} \le \lVert u\rVert_{W^{1,2}}$ it dominates the stated form. Here the arc-length factor is kept exactly as $\operatorname{dist}^{1/2}$ rather than over-estimated by $\sqrt{2\pi}$, which is why the constant is $1$ and not Haydys's $\sqrt{2\pi}$ (see the source-correction callout).
>
> **Uniform boundedness and equicontinuity.** Suppose $(u_j) \subset W^{1,2}(S^1)$ with $\lVert u_j\rVert_{W^{1,2}} \le M$ for all $j$. By statement 1, $\lVert u_j\rVert_{C^0} \le CM$, so the family is uniformly bounded. By statement 2, $\lvert u_j(\theta_1) - u_j(\theta_2)\rvert \le M\,\operatorname{dist}(\theta_1,\theta_2)^{1/2}$ for all $j$: given $\varepsilon > 0$, the single choice $\delta = (\varepsilon/M)^2$ makes $\operatorname{dist}(\theta_1,\theta_2) < \delta \Rightarrow \lvert u_j(\theta_1) - u_j(\theta_2)\rvert < \varepsilon$ simultaneously for every $j$, which is equicontinuity of the family. (By the Arzelà–Ascoli theorem this yields a $C^0$-convergent subsequence, the route by which Haydys's Remark 138 deduces compactness of $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$; the series instead proves Rellich compactness through the Fourier tail estimate on the general [[Thm - Rellich Compactness Theorem|Rellich compactness]] page, and this exercise only supplies the uniform boundedness and equicontinuity.)

**Step 6: The Fourier proof of statement 1 (statement 3).**

Expanding $u = \sum_{m\in\mathbb{Z}} c_m e^{im\theta}$,
$$\lVert u\rVert_{C^0} \le \Big(\sum_{m\in\mathbb{Z}}(1+m^2)^{-1}\Big)^{1/2}\Big(\tfrac1{2\pi}\lVert u\rVert_{W^{1,2}}^2\Big)^{1/2} = \Big(\tfrac{\coth\pi}{2}\Big)^{1/2}\lVert u\rVert_{W^{1,2}}.$$

> [!note]- Derivation
> **Fourier coefficients and Parseval.** For $u \in C^\infty(S^1;\mathbb{R})$ define $c_m = \tfrac1{2\pi}\int_0^{2\pi} u(\theta)e^{-im\theta}\,d\theta \in \mathbb{C}$; smoothness makes $(c_m)$ rapidly decreasing (proved on [[Ex - Fourier Coefficients of Smooth Functions Decay Rapidly]]), so every series below converges absolutely. The functions $\{e^{im\theta}\}_{m\in\mathbb{Z}}$ are orthogonal in $L^2(S^1)$ with $\int_0^{2\pi} e^{im\theta}\overline{e^{im\theta}}\,d\theta = 2\pi$, so **Parseval's identity** reads $\int_0^{2\pi}\lvert u\rvert^2\,d\theta = 2\pi\sum_m\lvert c_m\rvert^2$. Termwise differentiation gives $u' = \sum_m im\,c_m e^{im\theta}$ with coefficients $im\,c_m$, whence $\int_0^{2\pi}\lvert u'\rvert^2\,d\theta = 2\pi\sum_m m^2\lvert c_m\rvert^2$. Adding,
> $$\lVert u\rVert_{W^{1,2}}^2 = \int_0^{2\pi}(u^2 + (u')^2)\,d\theta = 2\pi\sum_{m\in\mathbb{Z}}(1+m^2)\lvert c_m\rvert^2 \qquad \text{(Parseval, applied to } u \text{ and to } u'\text{)}.$$
> **Bound the supremum by the coefficient sum.** For every $\theta$, $\lvert u(\theta)\rvert = \lvert\sum_m c_m e^{im\theta}\rvert \le \sum_m\lvert c_m\rvert$ (triangle inequality, $\lvert e^{im\theta}\rvert = 1$), so $\lVert u\rVert_{C^0} \le \sum_m\lvert c_m\rvert$.
> **Insert the weight and apply Cauchy–Schwarz on $\ell^2(\mathbb{Z})$.** Write $\lvert c_m\rvert = (1+m^2)^{-1/2}\cdot(1+m^2)^{1/2}\lvert c_m\rvert$ and apply **Cauchy–Schwarz on $\ell^2(\mathbb{Z})$** to the two factors:
> $$\sum_{m}\lvert c_m\rvert \le \Big(\sum_m (1+m^2)^{-1}\Big)^{1/2}\Big(\sum_m (1+m^2)\lvert c_m\rvert^2\Big)^{1/2} \qquad \text{(Cauchy–Schwarz in } \ell^2\text{)}.$$
> The second factor equals $\big(\tfrac1{2\pi}\lVert u\rVert_{W^{1,2}}^2\big)^{1/2}$ by the Parseval identity. The first factor is finite: this is precisely the [[Thm - Convergence of the Lattice Sum|lattice-sum theorem]] $\sum_{\xi\in\mathbb{Z}^n}(1+\lvert\xi\rvert^2)^{-t} < \infty \iff 2t > n$ in dimension $n = 1$ with exponent $t = 1$, where $2t = 2 > 1 = n$. Its exact value is $\sum_{m\in\mathbb{Z}}(1+m^2)^{-1} = \pi\coth\pi$ (evaluated in [[Ex - The Lattice Sum Converges iff 2t Exceeds n]]). Combining,
> $$\lVert u\rVert_{C^0} \le (\pi\coth\pi)^{1/2}\Big(\tfrac1{2\pi}\Big)^{1/2}\lVert u\rVert_{W^{1,2}} = \Big(\tfrac{\coth\pi}{2}\Big)^{1/2}\lVert u\rVert_{W^{1,2}} \qquad \text{(combining the two factors; } \tfrac{\pi}{2\pi} = \tfrac12\text{)}.$$
> Numerically $\big(\tfrac{\coth\pi}{2}\big)^{1/2} \approx (1.0037/2)^{1/2} \approx 0.708$, a smaller constant than the hand proof's $\sqrt{2\pi} + \tfrac1{\sqrt{2\pi}} \approx 2.90$, illustrating that the Fourier method is quantitatively sharper here.

> [!note]- Complete formal solution
> **Claim.** For $u \in C^\infty(S^1;\mathbb{R})$: (1) $\lVert u\rVert_{C^0} \le (\sqrt{2\pi} + \tfrac1{\sqrt{2\pi}})\lVert u\rVert_{W^{1,2}}$; (2) $\lvert u(\theta_1) - u(\theta_2)\rvert \le \lVert u\rVert_{W^{1,2}}\operatorname{dist}(\theta_1,\theta_2)^{1/2}$; and (3) the same bound holds with the Fourier constant $(\tfrac{\coth\pi}2)^{1/2}$. Consequently $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$ is a continuous embedding.
>
> Set $\bar u = \tfrac1{2\pi}\int_0^{2\pi}u$, $u_0 = u - \bar u$. Then $\int_{S^1}u_0 = 0$; since $u_0$ is continuous and $S^1$ connected, $u_0$ cannot be everywhere of one sign, so by the intermediate value theorem there is $\theta_0$ with $u_0(\theta_0) = 0$.
>
> *(1).* For any $\theta$, the fundamental theorem of calculus and $u_0(\theta_0) = 0$ give $u_0(\theta) = \int_{\theta_0}^\theta u_0'$, so by Cauchy–Schwarz $\lvert u_0(\theta)\rvert \le (\int_{\theta_0}^\theta 1)^{1/2}(\int_{\theta_0}^\theta (u_0')^2)^{1/2} \le \sqrt{2\pi}\,\lVert u'\rVert_{L^2}$ (using $u_0' = u'$ and enlarging the integration domain). Also $\lvert\bar u\rvert = \tfrac1{2\pi}\lvert\int 1\cdot u\rvert \le \tfrac1{\sqrt{2\pi}}\lVert u\rVert_{L^2}$ by Cauchy–Schwarz. Hence $\lVert u\rVert_{C^0} \le \lvert\bar u\rvert + \lVert u_0\rVert_{C^0} \le (\sqrt{2\pi} + \tfrac1{\sqrt{2\pi}})\lVert u\rVert_{W^{1,2}}$, using $\lVert u\rVert_{L^2},\lVert u'\rVert_{L^2} \le \lVert u\rVert_{W^{1,2}}$.
>
> *(2).* Let $\gamma$ be the shorter arc from $\theta_1$ to $\theta_2$, of length $\operatorname{dist}(\theta_1,\theta_2)$. Then $u(\theta_1)-u(\theta_2) = \int_\gamma u'$, and Cauchy–Schwarz on $L^2(\gamma)$ gives $\lvert u(\theta_1)-u(\theta_2)\rvert \le (\int_\gamma 1)^{1/2}(\int_\gamma (u')^2)^{1/2} \le \operatorname{dist}(\theta_1,\theta_2)^{1/2}\lVert u'\rVert_{L^2} \le \lVert u\rVert_{W^{1,2}}\operatorname{dist}(\theta_1,\theta_2)^{1/2}$.
>
> *(3).* With $c_m = \tfrac1{2\pi}\int u e^{-im\theta}$, Parseval gives $\lVert u\rVert_{W^{1,2}}^2 = 2\pi\sum_m(1+m^2)\lvert c_m\rvert^2$. Then $\lVert u\rVert_{C^0} \le \sum_m\lvert c_m\rvert \le (\sum_m(1+m^2)^{-1})^{1/2}(\sum_m(1+m^2)\lvert c_m\rvert^2)^{1/2} = (\pi\coth\pi)^{1/2}(\tfrac1{2\pi})^{1/2}\lVert u\rVert_{W^{1,2}} = (\tfrac{\coth\pi}2)^{1/2}\lVert u\rVert_{W^{1,2}}$, the middle factor finite by the lattice-sum theorem at $n=1$, $t=1$.
>
> *(Embedding.)* $C^\infty(S^1)$ is dense in $W^{1,2}(S^1)$ and the estimate (1) makes the inclusion into the complete space $C^0(S^1)$ bounded, hence it extends to a bounded injection $W^{1,2}(S^1) \hookrightarrow C^0(S^1)$; injectivity follows because uniform convergence forces $L^2$ convergence and $L^2$ limits are unique. $\blacksquare$

> [!warning] Illegal but tempting: dropping the mean-subtraction
> It is tempting to apply the fundamental theorem of calculus directly to $u$ from an arbitrary base point, say $u(\theta) = u(0) + \int_0^\theta u'$, and try to bound $\lvert u(0)\rvert$ separately. This does not close: $u(0)$ is a single pointwise value, and there is no bound on $\lvert u(0)\rvert$ by $\lVert u'\rVert_{L^2}$ alone (add a large constant to $u$: $\lVert u'\rVert_{L^2}$ is unchanged while $\lvert u(0)\rvert$ grows without bound). One genuinely needs a base point whose value is controlled by the *data*, and the only such point available for free is a zero of the mean-zero part $u_0$, produced in Step 1. The extra condition that would rescue the naive route is a hypothesis like $u(0) = 0$ or $\int u = 0$ — that is, one must either be told a zero or manufacture one, and manufacturing it is exactly the mean subtraction.

> [!note]- Independent sanity check
> Test the bounds on $u(\theta) = \cos\theta$. Then $\lVert u\rVert_{C^0} = 1$, $\int_0^{2\pi}\cos^2 = \pi$, $\int_0^{2\pi}\sin^2 = \pi$, so $\lVert u\rVert_{W^{1,2}}^2 = 2\pi$ and $\lVert u\rVert_{W^{1,2}} = \sqrt{2\pi} \approx 2.507$. The hand bound gives $1 \le (\sqrt{2\pi}+\tfrac1{\sqrt{2\pi}})\sqrt{2\pi} = 2\pi + 1 \approx 7.28$ ✓, and the Fourier bound $1 \le (\tfrac{\coth\pi}2)^{1/2}\sqrt{2\pi} \approx 0.708\cdot2.507 \approx 1.78$ ✓ — visibly tighter. The Fourier computation is transparent here: $\cos\theta = \tfrac12(e^{i\theta} + e^{-i\theta})$, so $c_{\pm1} = \tfrac12$ and all other $c_m = 0$; then $\sum_m\lvert c_m\rvert = 1 = \lVert u\rVert_{C^0}$ exactly (the supremum $1$ is attained at $\theta = 0$ where all present modes are in phase), confirming that the only slack in the Fourier proof is the Cauchy–Schwarz step against the lattice weight.

---

# Key Takeaways

**One derivative in $L^2$ controls the supremum in dimension one, and the mechanism is the fundamental theorem of calculus feeding Cauchy–Schwarz.** The transferable principle is that a pointwise bound on a function follows from an integral bound on its derivative *as soon as one has a base point of controlled value*, because the increment from the base point is an integral of the derivative and Cauchy–Schwarz converts that integral into (length)$^{1/2}\times\lVert u'\rVert_{L^2}$. The trigger to reach for this argument is any estimate whose left side is a supremum or a pointwise value and whose right side is an $L^2$ norm of a derivative; the diagnostic question is "what is my base point, and is its value controlled by the data?" On the circle the base point is manufactured by subtracting the mean and invoking the intermediate value theorem — a move that recurs whenever one needs a controlled anchor for the fundamental theorem of calculus, for instance in Poincaré and Wirtinger inequalities, where subtracting the mean is again the enabling step.

**The exponent count $k - \tfrac n2 > r$ of the Sobolev embedding is, in one dimension, the length factor $\operatorname{dist}^{1/2}$, and on the Fourier side it is the convergence of a lattice sum.** The number that decides whether $W^{k,2} \hookrightarrow C^r$ is the same number in both proofs, wearing two costumes. In the hand proof, one derivative ($k=1$) produces exactly one factor of length$^{1/2}$, giving a Hölder-$\tfrac12$ modulus and hence continuity ($r=0$); the surplus regularity $k - \tfrac n2 = \tfrac12$ is literally the Hölder exponent. In the Fourier proof, the same surplus appears as the requirement $2(k - r) > n$ that makes $\sum(1+m^2)^{r-k}$ converge — for us $2(1-0) = 2 > 1$. Recognising that the embedding exponent and the lattice-sum exponent are the same quantity is the key to seeing why the general [[Thm - Sobolev Embedding Theorem|Sobolev embedding theorem]] is, at heart, dimension counting: the [[Thm - Convergence of the Lattice Sum|lattice sum]] converges exactly when the leftover weight is summable, which is a statement about how many lattice points sit in a shell of radius $R$.

**The two proofs are complementary: the hand proof is robust and coordinate-free, the Fourier proof is sharp and diagnostic.** The fundamental-theorem-of-calculus argument uses nothing but the manifold structure and works verbatim on any compact one-manifold (an interval with boundary conditions, a graph), and it generalises to higher dimensions through line integrals along geodesics and the coarea formula — at the cost of losing sharp constants. The Fourier argument is available only because $S^1$ is a group with a known character theory, but in exchange it delivers the *exact* dependence of the constant on the geometry ($(\tfrac{\coth\pi}2)^{1/2}$, with $\coth\pi$ the value of the lattice sum) and it isolates the single inequality — Cauchy–Schwarz against the lattice weight — where all the slack lives. When one needs qualitative results on general manifolds, one reaches for the hand-style argument transported through charts; when one needs quantitative constants or the precise borderline behaviour (as in the failure case $2k = n$ studied in [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]]), one reaches for the Fourier expansion. The companion drills [[Ex - The Lattice Sum Converges iff 2t Exceeds n]] and [[Ex - An Unbounded Function in W-1-2 of the Two-Torus]] complete the picture: the first supplies the lattice-sum input this proof used as a black box, the second shows what goes wrong precisely when the surplus exponent reaches zero.
