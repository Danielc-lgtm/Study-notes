---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - The Total Derivative and Differentiability"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - Differentiability Implies Continuity"
  - "Thm - Continuous Partials Imply Differentiability"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider $f : \mathbb{R}^2 \to \mathbb{R}$ defined by
$$f(x,y) = \begin{cases} (x^2 + y^2)\,\sin\!\dfrac{1}{\sqrt{x^2+y^2}} & (x,y) \neq (0,0), \\[2mm] 0 & (x,y) = (0,0). \end{cases}$$

1. Show that $f$ is **differentiable** at the origin, with $Df_{(0,0)} = 0$ (the zero linear map).
2. Show that the partial derivative $\partial_x f$ is **not continuous** at the origin.
3. Conclude that $f$ is differentiable everywhere but is **not** of class $C^1$ — so the implication "differentiable $\Rightarrow$ continuous partials" is *false*, and the converse of [[Thm - Continuous Partials Imply Differentiability]] fails.

**Recall:**

The two notions in tension are differentiability and continuity of the partials.

![[Def - The Total Derivative and Differentiability#The Definition]]

A function $f$ is [[Def - The Total Derivative and Differentiability|differentiable]] at $x_\circ$ if a linear map $L$ exists with $f(x_\circ + h) - f(x_\circ) - L(h) = o(|h|)$. The candidate $L$ is forced: its matrix is the Jacobian of partials.

The $j$-th [[Def - Partial Derivatives and the Jacobian Matrix|partial derivative]] $\partial_j f(x_\circ)$ is the one-variable derivative of $f$ along the $j$-th axis. A function is of class $C^1$ when all partials exist *and are continuous*.

![[Thm - Continuous Partials Imply Differentiability#Statement]]

The theorem above is one-directional: continuous partials force differentiability. This exercise produces a function showing the *reverse* implication is false — differentiability does not force the partials to be continuous.

---

# Convergent Strategy

**Problem class.** This is a *separating-example* problem: construct a single function witnessing that two conditions in the regularity hierarchy — "differentiable" and "$C^1$" — are genuinely distinct. As the [[Multivariate Analysis I — Differentiation in Several Variables#Insights|topic page]] records, the three conditions "partials exist", "differentiable", "$C^1$" form a strict ladder, and each strict gap deserves a named witness; this is the witness for the upper gap.

**Assumption pattern.** The function is the two-variable promotion of the classic one-variable example $x^2 \sin(1/x)$. That function is differentiable at $0$ (the $x^2$ factor crushes the bounded oscillation) but has a derivative that oscillates and is discontinuous at $0$ (differentiating produces a $\cos(1/x)$ term with no decaying prefactor). The recognisable feature: a *small even prefactor* multiplying a *bounded but wildly oscillating factor*. The prefactor secures differentiability; the oscillation, once differentiated, destroys continuity of the derivative.

**Theorem routing.** Part 1 is a direct check of the definition of differentiability at the origin: the candidate derivative must be $0$ because the partials at the origin vanish, and the $o(|h|)$ condition holds because $|f(h)| \le |h|^2 = o(|h|)$. Part 2 computes $\partial_x f$ away from the origin by the ordinary product and chain rules, then exhibits a sequence approaching the origin along which $\partial_x f$ fails to approach $\partial_x f(0,0) = 0$. Part 3 assembles: differentiable everywhere (origin by Part 1, elsewhere by [[Thm - Continuous Partials Imply Differentiability]] since the partials are continuous away from $0$), but not $C^1$ (Part 2).

**Key decision point.** The non-obvious move is to *not* be alarmed that $\partial_x f$ has no limit at the origin. One's instinct, having computed a discontinuous partial, is to suspect non-differentiability — but [[Thm - Continuous Partials Imply Differentiability]] only says continuous partials are *sufficient*; their discontinuity is not an obstruction. Differentiability must be checked on its own terms, directly from the definition, and Part 1 does exactly that. The discontinuous partial and the genuine differentiability coexist precisely because the radius-squared prefactor controls the function itself far better than it controls its derivative.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Recover the candidate derivative from the partials.** At the origin, compute $\partial_x f(0,0)$ and $\partial_y f(0,0)$ from the limit definition; both are $0$, so the only possible derivative is $L = 0$.

2. **Verify differentiability directly from the definition.** Check $|f(h) - f(0) - L(h)|/|h| \to 0$ with $L = 0$, using the bound $|f(h)| \le |h|^2$.

3. **Compute partials away from the suspect point by Analysis I rules.** Use the product rule and chain rule to differentiate the explicit formula for $(x,y) \neq (0,0)$.

4. **Disprove continuity by exhibiting a bad sequence.** Produce points $x_k \to (0,0)$ along which $\partial_x f(x_k)$ does not converge to $\partial_x f(0,0)$.

---

# Hints

> [!note]- Hint 1
> For Part 1, what *must* the derivative be? Compute the partial derivatives at the origin from the limit definition: $\partial_x f(0,0) = \lim_{t\to 0} \big(f(t,0) - f(0,0)\big)/t$. The factor $\sin(1/|t|)$ is bounded; the prefactor is $t^2$. The candidate derivative is forced.

> [!note]- Hint 2
> For Part 1, with $L = 0$ the quantity to control is $|f(h) - 0 - 0|/|h| = |f(h)|/|h|$. Bound $|f(h)|$ using $|\sin(\cdots)| \le 1$. You get $|f(h)| \le |h|^2$, so $|f(h)|/|h| \le |h| \to 0$.

> [!note]- Hint 3
> For Part 2, away from the origin differentiate the explicit formula. Write $r = \sqrt{x^2+y^2}$, so $f = r^2 \sin(1/r)$. By the product and chain rules, $\partial_x f$ has a term coming from differentiating $r^2$ (this term has a factor of $r$, so it vanishes at the origin) and a term coming from differentiating $\sin(1/r)$ (this one produces $\cos(1/r)$ with *no* decaying prefactor).

> [!note]- Hint 4
> For Part 2, evaluate $\partial_x f$ along the $x$-axis: set $y = 0$, $x > 0$, so $r = x$. You will find $\partial_x f(x,0) = 2x\sin(1/x) - \cos(1/x)$. Now take $x_k = 1/(2\pi k) \to 0$: the first term vanishes, the second is $-\cos(2\pi k) = -1$. So $\partial_x f(x_k, 0) \to -1 \neq 0 = \partial_x f(0,0)$.

---

# Solution

The radius-squared prefactor makes $f$ vanish to second order at the origin, which is more than enough for differentiability with zero derivative. But differentiating once spends that prefactor down to first order on the "nice" term and leaves a *bare* oscillating $\cos(1/r)$ term — and a bare oscillation has no limit. Differentiable, yes; $C^1$, no.

**Step 1: The partials at the origin are zero, so the only candidate derivative is $L = 0$.**

$\partial_x f(0,0) = \partial_y f(0,0) = 0$.

> [!note]- Derivation
> By symmetry it suffices to compute $\partial_x f(0,0)$. By the limit definition of the [[Def - Partial Derivatives and the Jacobian Matrix|partial derivative]],
> $$\partial_x f(0,0) = \lim_{t \to 0} \frac{f(t,0) - f(0,0)}{t} = \lim_{t \to 0} \frac{t^2 \sin(1/|t|) - 0}{t} = \lim_{t \to 0} t\,\sin(1/|t|).$$
> Since $|\sin(1/|t|)| \le 1$, we have $|t\sin(1/|t|)| \le |t| \to 0$, so the limit is $0$. Identically $\partial_y f(0,0) = 0$. If $f$ is differentiable at the origin its derivative has matrix $\big(\partial_x f(0,0),\, \partial_y f(0,0)\big) = (0,0)$, so the only candidate is the zero linear map $L = 0$.

**Step 2: $f$ is differentiable at the origin with $Df_{(0,0)} = 0$.**

The defining limit holds: $|f(h) - f(0,0) - L(h)|/|h| = |f(h)|/|h| \le |h| \to 0$.

> [!note]- Derivation
> Write $h = (h_1, h_2)$ and $|h| = \sqrt{h_1^2 + h_2^2}$. With $L = 0$ and $f(0,0) = 0$, the quantity in the definition of [[Def - The Total Derivative and Differentiability|differentiability]] is
> $$\frac{|f(h) - f(0,0) - L(h)|}{|h|} = \frac{|f(h)|}{|h|}.$$
> For $h \neq 0$, $f(h) = |h|^2 \sin(1/|h|)$, so $|f(h)| = |h|^2\,|\sin(1/|h|)| \le |h|^2$. Therefore
> $$\frac{|f(h)|}{|h|} \le \frac{|h|^2}{|h|} = |h| \xrightarrow[h \to 0]{} 0.$$
> The defining limit is $0$, so $f$ is differentiable at the origin and $Df_{(0,0)} = L = 0$. (Notice the prefactor $|h|^2$ does the work: $f$ vanishes to *second* order, leaving room to spare against the first-order denominator $|h|$.)

**Step 3: $\partial_x f$ exists away from the origin and equals $\dfrac{2x\,r\sin(1/r) - x\cos(1/r)}{r}$, where $r = \sqrt{x^2+y^2}$.**

> [!note]- Derivation
> For $(x,y) \neq (0,0)$ the function $f(x,y) = r^2 \sin(1/r)$ with $r = (x^2+y^2)^{1/2}$ is a composite of smooth functions, so its partials exist and are computed by the Analysis I product and chain rules. Note $\partial_x r = x/r$. Then
> $$\partial_x f = \partial_x\big(r^2\big)\sin(1/r) + r^2 \cdot \partial_x\big(\sin(1/r)\big).$$
> The first piece: $\partial_x(r^2) = 2r\,\partial_x r = 2r \cdot x/r = 2x$, giving $2x\sin(1/r)$. The second piece: $\partial_x(\sin(1/r)) = \cos(1/r)\cdot\partial_x(1/r) = \cos(1/r)\cdot(-r^{-2})\,\partial_x r = -\cos(1/r)\,r^{-2}\,(x/r) = -x\cos(1/r)/r^3$, so $r^2$ times this is $-\dfrac{x\cos(1/r)}{r}$. Hence
> $$\partial_x f(x,y) = 2x\,\sin(1/r) - \frac{x\cos(1/r)}{r}, \qquad r = \sqrt{x^2+y^2}.$$
> The first term tends to $0$ as $(x,y)\to(0,0)$ (it is bounded by $2|x| \le 2|h|$). The second term is the culprit: $x/r$ stays bounded by $1$ but does not have a limit, and $\cos(1/r)$ oscillates without limit.

**Step 4: $\partial_x f$ is not continuous at the origin.**

Along $x_k = (1/(2\pi k),\, 0)$ one has $\partial_x f(x_k) \to -1 \neq 0 = \partial_x f(0,0)$.

> [!note]- Derivation
> Evaluate $\partial_x f$ along the positive $x$-axis: set $y = 0$, $x > 0$, so $r = x$ and the formula from Step 3 becomes
> $$\partial_x f(x, 0) = 2x\sin(1/x) - \cos(1/x).$$
> Take the sequence $x_k = \dfrac{1}{2\pi k} \to 0^+$. Then $1/x_k = 2\pi k$, so $\sin(1/x_k) = \sin(2\pi k) = 0$ and $\cos(1/x_k) = \cos(2\pi k) = 1$. Hence
> $$\partial_x f(x_k, 0) = 2x_k \cdot 0 - 1 = -1 \quad\text{for every } k.$$
> So $\partial_x f(x_k, 0) \to -1$ as $k \to \infty$, while the point $(x_k, 0) \to (0,0)$ and $\partial_x f(0,0) = 0$. Since the values along this sequence do not converge to the value at the limit, $\partial_x f$ is **not continuous** at the origin. (One could equally take $x_k' = 1/(\pi(2k+1))$ to get the value $+1$, showing $\partial_x f$ has no limit at all at the origin.)

> [!note]- Complete formal solution
> **Claim.** The function $f$ is differentiable on all of $\mathbb{R}^2$, but $\partial_x f$ is discontinuous at the origin; hence $f$ is not $C^1$.
>
> *Differentiability away from the origin.* For $(x,y) \neq (0,0)$, $f = r^2\sin(1/r)$ with $r = (x^2+y^2)^{1/2} > 0$ is a composite of smooth functions; its partials exist and are continuous on $\mathbb{R}^2 \setminus \{0\}$. By [[Thm - Continuous Partials Imply Differentiability]], $f$ is differentiable at every point other than the origin.
>
> *Differentiability at the origin.* The limit definition gives $\partial_x f(0,0) = \lim_{t\to0} t\sin(1/|t|) = 0$ and likewise $\partial_y f(0,0) = 0$, so the only candidate derivative is $L = 0$. For $h \neq 0$, $|f(h) - f(0,0) - L(h)|/|h| = |f(h)|/|h| = |h|\,|\sin(1/|h|)| \le |h| \to 0$. Hence $f$ is differentiable at the origin with $Df_{(0,0)} = 0$. Therefore $f$ is differentiable on all of $\mathbb{R}^2$.
>
> *Failure of $C^1$.* For $(x,y)\neq(0,0)$, the product and chain rules give $\partial_x f(x,y) = 2x\sin(1/r) - x\cos(1/r)/r$. Along $y = 0$, $x > 0$: $\partial_x f(x,0) = 2x\sin(1/x) - \cos(1/x)$. With $x_k = 1/(2\pi k) \to 0$, $\partial_x f(x_k,0) = -\cos(2\pi k) = -1$ for all $k$, while $\partial_x f(0,0) = 0$. So $\partial_x f$ is not continuous at the origin, and $f \notin C^1(\mathbb{R}^2)$.
>
> Thus $f$ is everywhere differentiable but not continuously differentiable: the converse of [[Thm - Continuous Partials Imply Differentiability]] is false. $\blacksquare$

---

# Key Takeaways

**Differentiability and $C^1$ are genuinely distinct, and the standard separating device is "small even prefactor times wild bounded oscillation".** The three regularity conditions — partials exist, differentiable, $C^1$ — form a strict chain, and this exercise nails down the upper gap. The construction is worth memorising as a template: take a factor that vanishes to high order at a point (here $r^2$) and multiply it by a bounded factor that oscillates infinitely fast (here $\sin(1/r)$). The high-order vanishing guarantees the *function* is well-approximated by its linear part — differentiability survives — while differentiating once *spends one order of the prefactor* and exposes a bare, undecorated oscillation in the derivative — continuity of the derivative dies. The same machine in one variable is $x^2\sin(1/x)$; the same machine produces functions that are $C^k$ but not $C^{k+1}$ by raising the prefactor to power $2(k+1)$. Whenever you need a function on a given rung of the regularity ladder but not the next, reach for this construction.

**A discontinuous partial derivative is not, by itself, an obstruction to differentiability.** This is the conceptual trap the exercise is built to spring. [[Thm - Continuous Partials Imply Differentiability]] says continuous partials are *sufficient* for differentiability — it says nothing about necessity, and it is tempting to misremember it as an equivalence. It is not. When you compute a partial derivative and find it discontinuous, you have learned that the *cheap* route to differentiability (invoke the theorem) is unavailable; you have learned *nothing* about whether $f$ is in fact differentiable. That question must then be settled directly from the definition. The correct mental model: continuity of the partials is one *sufficient condition* among possibly others, and its failure throws you back on the definition rather than settling the matter. Routinely, when a partial is discontinuous at a suspect point, the function is still differentiable there exactly when the function itself vanishes fast enough — which is a separate computation.

**The order of vanishing of the remainder is the quantity that controls differentiability.** Differentiability at the origin came down to one inequality, $|f(h)| \le |h|^2$, which says $f$ vanishes to *second* order. The definition of differentiability only needs the remainder to be $o(|h|)$ — first order with room to spare — so a function vanishing to second order clears the bar comfortably, with the candidate derivative forced to be $0$. This is a reusable diagnostic: to test differentiability at a point where the candidate derivative is the obvious one, estimate the order of vanishing of the remainder $f(x_\circ + h) - f(x_\circ) - L(h)$. Strictly better than first order means differentiable; exactly first order or worse means look harder, usually along well-chosen paths. The exercise also shows the asymmetry between $f$ and $\partial f$: $f$ vanishes to order two, but each differentiation drops the order by one, so $\partial f$ vanishes only to order one on its good term and to order zero on its oscillating term — which is exactly why the function is one rung higher on the ladder than its derivative.
