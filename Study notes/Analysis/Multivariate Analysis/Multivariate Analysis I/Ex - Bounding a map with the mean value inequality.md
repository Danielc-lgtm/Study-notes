---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Mean Value Inequality"
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - Continuous Partials Imply Differentiability"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $f : \mathbb{R}^2 \to \mathbb{R}^2$ be the map
$$f(x,y) = \Big(\tfrac14\sin(x+y),\; \tfrac14\cos(x - y)\Big).$$

1. Show that $f$ is differentiable on $\mathbb{R}^2$ and that its Jacobian satisfies the operator-norm bound $\|Jf(x,y)\| \le \tfrac12$ for every $(x,y)$. *(You may bound the operator norm by the Hilbert–Schmidt norm $\|M\|_2 = \big(\sum_{i,j}M_{ij}^2\big)^{1/2}$, which dominates it.)*
2. Conclude that $f$ is a **contraction**: $|f(p) - f(q)| \le \tfrac12\,|p - q|$ for all $p, q \in \mathbb{R}^2$.
3. Deduce that $f$ has at most one fixed point, and that the iteration $p_{k+1} = f(p_k)$ is a Cauchy sequence from any starting point.

**Recall:**

The instrument is the mean value inequality, which converts a bound on the derivative into a bound on the function.

![[Thm - The Mean Value Inequality#Statement]]

The [[Thm - The Mean Value Inequality|mean value inequality]] states that for a differentiable $f : U \to \mathbb{R}^m$ on a convex $U$, if $\|Df_\xi\| \le M$ for all $\xi$, then $|f(x) - f(y)| \le M|x - y|$. For vector-valued $f$ only the *inequality* holds — there is no exact equality.

A map $f$ on a metric space is a **contraction** if $|f(p) - f(q)| \le M|p-q|$ for a constant $M < 1$. The [[Def - Partial Derivatives and the Jacobian Matrix|Jacobian]] $Jf$ is the matrix of the derivative; its operator norm $\|Jf\|$ is the smallest $M$ with $|Jf\cdot v| \le M|v|$. By [[Thm - Continuous Partials Imply Differentiability]], continuous partials make $f$ differentiable.

---

# Convergent Strategy

**Problem class.** This is a *bounding* problem: show a map does not change too fast. As the [[Multivariate Analysis I — Differentiation in Several Variables#Problem-Solving Strategy|topic page strategy]] records, the instrument for any "prove Lipschitz / bound an increment / prove a contraction" problem is the [[Thm - The Mean Value Inequality|mean value inequality]], and the route is: bound the operator norm of $Df$ on the region, then read off the function bound.

**Assumption pattern.** The map is given by an explicit formula whose entries are bounded trigonometric functions scaled by $\tfrac14$. The recognisable feature: an explicit map with a small constant prefactor, signalling that the derivative will be uniformly small — exactly the input the mean value inequality wants. The domain is all of $\mathbb{R}^2$, which is convex, so the convexity hypothesis is automatic.

**Theorem routing.** Part 1: compute $Jf$ by Analysis I rules; the entries are bounded by $\tfrac14$ in absolute value, so the Hilbert–Schmidt norm is at most $\tfrac12$, and since the Hilbert–Schmidt norm dominates the operator norm, $\|Jf\| \le \tfrac12$. Continuity of the entries plus [[Thm - Continuous Partials Imply Differentiability]] gives differentiability. Part 2: feed the uniform bound $M = \tfrac12$ into the [[Thm - The Mean Value Inequality|mean value inequality]] on the convex domain $\mathbb{R}^2$. Part 3: a contraction has at most one fixed point (two fixed points would violate the contraction inequality), and the iterates form a Cauchy sequence by the geometric-series estimate.

**Key decision point.** The non-obvious step is bounding the *operator* norm of the Jacobian. The operator norm is itself defined by a supremum and is awkward to compute directly; the move is to bound it by something easier — the Hilbert–Schmidt norm $\|M\|_2$, which is just the square root of the sum of squared entries and dominates the operator norm. Each entry of $Jf$ is at most $\tfrac14$ in absolute value, so $\|Jf\|_2 \le \sqrt{4\cdot(1/4)^2} = \sqrt{1/4} = \tfrac12$. This "bound the hard norm by the easy norm" move is the technical heart of the exercise.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Compute partials by Analysis I rules.** Differentiate the four trigonometric entries to assemble $Jf$.

2. **Verify differentiability via continuity of the partials.** The entries of $Jf$ are continuous, so [[Thm - Continuous Partials Imply Differentiability]] gives differentiability everywhere.

3. **Bound the operator norm by an easier norm.** Use $\|M\| \le \|M\|_2$ and bound the Hilbert–Schmidt norm by the entries.

4. **Convert a derivative bound into a function bound.** Apply the [[Thm - The Mean Value Inequality|mean value inequality]] with $M = \tfrac12$ on the convex domain $\mathbb{R}^2$.

5. **Run a geometric-series estimate.** From the contraction inequality, bound $|p_{k+1} - p_k| \le (\tfrac12)^k|p_1 - p_0|$ and sum.

---

# Hints

> [!note]- Hint 1
> Compute $Jf$. The component $f_1 = \tfrac14\sin(x+y)$ has $\partial_x f_1 = \tfrac14\cos(x+y)$ and $\partial_y f_1 = \tfrac14\cos(x+y)$. Do the same for $f_2 = \tfrac14\cos(x-y)$. Every entry of $Jf$ is $\pm\tfrac14$ times a cosine or sine, so every entry is at most $\tfrac14$ in absolute value.

> [!note]- Hint 2
> To bound $\|Jf\|$, note the operator norm is dominated by the Hilbert–Schmidt norm $\|M\|_2 = \sqrt{\sum_{i,j}M_{ij}^2}$. There are four entries, each at most $\tfrac14$ in size, so $\sum M_{ij}^2 \le 4\cdot(1/4)^2 = 1/4$, giving $\|Jf\|_2 \le 1/2$. Hence $\|Jf\| \le 1/2$.

> [!note]- Hint 3
> For Part 2: $\mathbb{R}^2$ is convex, and $\|Df\| \le \tfrac12$ everywhere. The mean value inequality says $|f(p) - f(q)| \le (\sup\|Df\|)\,|p-q| \le \tfrac12|p-q|$. Since $\tfrac12 < 1$, this is a contraction.

> [!note]- Hint 4
> For Part 3, uniqueness: if $p$ and $q$ are both fixed points, $|p - q| = |f(p) - f(q)| \le \tfrac12|p-q|$, forcing $|p-q| = 0$. For the Cauchy property: $|p_{k+1}-p_k| = |f(p_k)-f(p_{k-1})| \le \tfrac12|p_k-p_{k-1}|$, so by induction $|p_{k+1}-p_k| \le (\tfrac12)^k|p_1-p_0|$ — a geometric sequence; sum the tail.

---

# Solution

The map has a small constant prefactor $\tfrac14$, which guarantees a uniformly small derivative; the mean value inequality then upgrades "small derivative" to "small change", and a change-factor below $1$ is exactly a contraction. Everything follows from bounding one Jacobian.

**Step 1: $f$ is differentiable everywhere and $\|Jf(x,y)\| \le \tfrac12$.**

> [!note]- Derivation
> Differentiate each component by the Analysis I rules. With $f_1 = \tfrac14\sin(x+y)$ and $f_2 = \tfrac14\cos(x-y)$,
> $$\partial_x f_1 = \tfrac14\cos(x+y), \quad \partial_y f_1 = \tfrac14\cos(x+y),$$
> $$\partial_x f_2 = -\tfrac14\sin(x-y), \quad \partial_y f_2 = +\tfrac14\sin(x-y).$$
> So
> $$Jf(x,y) = \begin{pmatrix} \tfrac14\cos(x+y) & \tfrac14\cos(x+y) \\[1mm] -\tfrac14\sin(x-y) & \tfrac14\sin(x-y) \end{pmatrix}.$$
> Every entry is an elementary continuous function, so by [[Thm - Continuous Partials Imply Differentiability]] $f$ is differentiable everywhere on $\mathbb{R}^2$ and $Jf$ is the matrix of $Df$.
>
> Each entry has absolute value at most $\tfrac14$ (a quarter of a sine or cosine). The Hilbert–Schmidt norm — the square root of the sum of squared entries — is therefore bounded by
> $$\|Jf\|_2 = \Big(\sum_{i,j}(Jf)_{ij}^2\Big)^{1/2} \le \Big(4\cdot\big(\tfrac14\big)^2\Big)^{1/2} = \Big(\tfrac14\Big)^{1/2} = \tfrac12.$$
> The operator norm is dominated by the Hilbert–Schmidt norm, $\|Jf\| \le \|Jf\|_2$. Hence $\|Jf(x,y)\| \le \tfrac12$ for every $(x,y) \in \mathbb{R}^2$.

**Step 2: $f$ is a contraction with constant $\tfrac12$.**

$|f(p) - f(q)| \le \tfrac12\,|p - q|$ for all $p, q \in \mathbb{R}^2$.

> [!note]- Derivation
> The domain $\mathbb{R}^2$ is convex — the segment between any two points lies in it. By Step 1, $f$ is differentiable with $\|Df_\xi\| = \|Jf(\xi)\| \le \tfrac12$ at every point $\xi$. The [[Thm - The Mean Value Inequality|mean value inequality]] for a vector-valued map on a convex domain states
> $$|f(p) - f(q)| \le \Big(\sup_{\xi\in[p,q]}\|Df_\xi\|\Big)\,|p - q| \le \tfrac12\,|p - q|.$$
> Since the change-factor $\tfrac12$ is strictly less than $1$, $f$ is a contraction. (This is exactly the step where the vector-valued mean value *inequality* — not equality — is used: $f$ maps into $\mathbb{R}^2$, so no exact mean value equality is available, but the inequality is all that is needed.)

**Step 3: $f$ has at most one fixed point, and every iteration sequence is Cauchy.**

> [!note]- Derivation
> *At most one fixed point.* Suppose $p$ and $q$ both satisfy $f(p) = p$ and $f(q) = q$. Then
> $$|p - q| = |f(p) - f(q)| \le \tfrac12|p - q|.$$
> Subtracting, $\tfrac12|p-q| \le 0$, so $|p-q| = 0$, i.e. $p = q$. There is at most one fixed point.
>
> *The iterates are Cauchy.* Fix any $p_0 \in \mathbb{R}^2$ and set $p_{k+1} = f(p_k)$. For consecutive iterates,
> $$|p_{k+1} - p_k| = |f(p_k) - f(p_{k-1})| \le \tfrac12|p_k - p_{k-1}|,$$
> so by induction $|p_{k+1} - p_k| \le (\tfrac12)^k|p_1 - p_0|$. For $\ell > k$, the triangle inequality and the geometric series give
> $$|p_\ell - p_k| \le \sum_{j=k}^{\ell-1}|p_{j+1}-p_j| \le |p_1-p_0|\sum_{j=k}^{\ell-1}(\tfrac12)^j \le |p_1-p_0|\cdot\frac{(\tfrac12)^k}{1 - \tfrac12} = 2(\tfrac12)^k|p_1-p_0|.$$
> The right side tends to $0$ as $k \to \infty$, so $(p_k)$ is Cauchy. (Since $\mathbb{R}^2$ is complete, it converges; its limit is the unique fixed point — this is the contraction mapping principle, the engine of the inverse function theorem in **Multivariate Analysis II**.)

> [!note]- Complete formal solution
> **Claim.** $f(x,y) = \big(\tfrac14\sin(x+y), \tfrac14\cos(x-y)\big)$ is a contraction with constant $\tfrac12$; hence it has at most one fixed point and all iteration sequences are Cauchy.
>
> The Jacobian $Jf = \begin{pmatrix}\tfrac14\cos(x+y) & \tfrac14\cos(x+y)\\ -\tfrac14\sin(x-y) & \tfrac14\sin(x-y)\end{pmatrix}$ has continuous entries, so by [[Thm - Continuous Partials Imply Differentiability]] $f$ is differentiable. Each entry has size $\le\tfrac14$, so $\|Jf\| \le \|Jf\|_2 \le \sqrt{4(1/4)^2} = \tfrac12$. The domain $\mathbb{R}^2$ is convex, so by [[Thm - The Mean Value Inequality]], $|f(p)-f(q)| \le \tfrac12|p-q|$ for all $p,q$.
>
> If $f(p)=p$, $f(q)=q$ then $|p-q| = |f(p)-f(q)| \le \tfrac12|p-q|$, forcing $p=q$. For $p_{k+1}=f(p_k)$, $|p_{k+1}-p_k| \le (\tfrac12)^k|p_1-p_0|$, so $|p_\ell-p_k| \le 2(\tfrac12)^k|p_1-p_0| \to 0$ and $(p_k)$ is Cauchy. $\blacksquare$

---

# Key Takeaways

**The mean value inequality is the bridge from a derivative bound to a function bound, and any "prove a contraction / prove Lipschitz" problem routes through it.** The structural shape of this exercise is the canonical one for the entire bounding class: you are asked to control how much a map changes, and the only information you can compute is its derivative. The mean value inequality is the one tool that converts the one into the other — $|f(p)-f(q)| \le \sup\|Df\|\cdot|p-q|$. The recipe never varies: differentiate, bound the operator norm of the Jacobian uniformly on the region, read off the function bound. When the uniform bound comes out below $1$, you have not merely a Lipschitz map but a contraction, and contractions are the gateway to fixed-point theorems. Recognise the trigger: a small constant prefactor in an explicit map, or a derivative you can bound, plus a request to control the map's variation.

**Bound the operator norm by an easier norm — the Hilbert–Schmidt norm is the standard choice.** The operator norm $\|M\| = \sup_{|v|\le1}|Mv|$ is the "correct" norm for the mean value inequality, but it is defined by a supremum and is genuinely awkward to compute — it is the largest singular value of $M$. The reusable trick is never to compute it: bound it above by something mechanical. The Hilbert–Schmidt norm $\|M\|_2 = \sqrt{\sum M_{ij}^2}$ dominates the operator norm and is just a sum of squared entries. So "every entry of $Jf$ is $\le\tfrac14$" instantly yields $\|Jf\| \le \|Jf\|_2 \le \tfrac12$. This domination $\|M\|\le\|M\|_2$ is worth carrying as a permanent tool: whenever a proof needs an operator-norm bound and you have explicit entries, route through the Hilbert–Schmidt norm. The slack is harmless — the mean value inequality only needs *an* upper bound, not the sharpest one.

**A contraction has at most one fixed point and Cauchy iterates — the geometric-series estimate is the mechanism, and completeness finishes the job.** Once a map is shown to be a contraction, two consequences follow with no further input about the map. Uniqueness of fixed points is immediate: two fixed points $p,q$ would give $|p-q| = |f(p)-f(q)| \le M|p-q|$ with $M<1$, an impossibility unless $p=q$. The Cauchy property of the iterates is the geometric-series estimate: consecutive gaps shrink by the factor $M$ each step, $|p_{k+1}-p_k|\le M^k|p_1-p_0|$, and a geometric series has a finite, vanishing tail, so $|p_\ell-p_k|\to0$. In a *complete* space — and $\mathbb{R}^n$ is complete — Cauchy implies convergent, and the limit is the (unique) fixed point. This is the full content of the contraction mapping principle, and it is the analytic engine behind the inverse and implicit function theorems: those theorems manufacture a contraction whose fixed point is the inverse map, and this exact estimate is what produces it.
