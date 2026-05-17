---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Higher-Order Derivatives and Ck Maps"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Thm - Schwarz's Theorem on Mixed Partials"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Consider $f : \mathbb{R}^2 \to \mathbb{R}$ defined by
$$f(x,y) = \begin{cases} \dfrac{xy(x^2 - y^2)}{x^2 + y^2} & (x,y) \neq (0,0), \\[2mm] 0 & (x,y) = (0,0). \end{cases}$$

1. Show that both mixed second partial derivatives at the origin **exist**, and compute them: $\partial_x\partial_y f(0,0) = +1$ and $\partial_y\partial_x f(0,0) = -1$.
2. Conclude that $\partial_x\partial_y f(0,0) \neq \partial_y\partial_x f(0,0)$ — the mixed partials disagree.
3. Explain why this does **not** contradict [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]]: identify which hypothesis of the theorem fails.

**Recall:**

The objects in tension are the mixed second partials and the hypothesis of Schwarz's theorem.

The first [[Def - Partial Derivatives and the Jacobian Matrix|partial derivative]] $\partial_x f$ is the one-variable derivative in $x$ with $y$ frozen; the **mixed second partial** $\partial_y\partial_x f$ is $\partial_y(\partial_x f)$ — first differentiate in $x$, then in $y$.

A function is [[Def - Higher-Order Derivatives and Ck Maps|of class $C^2$]] when all its first and second partials exist *and are continuous*.

![[Thm - Schwarz's Theorem on Mixed Partials#Statement]]

[[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] guarantees $\partial_i\partial_j f = \partial_j\partial_i f$ **for $C^2$ functions**. The hypothesis "$C^2$" — continuity of the second partials — is essential; this exercise produces a function violating the conclusion, hence necessarily violating the hypothesis.

---

# Convergent Strategy

**Problem class.** This is a *separating-example* problem: exhibit a function whose mixed partials disagree, demonstrating that the conclusion of [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] genuinely needs its hypothesis. As the [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|topic page]] warns, "reorder partial derivatives without checking $C^2$" is an illegal-but-tempting operation, and this exercise is the counterexample certifying that.

**Assumption pattern.** The function is a degree-$4$ numerator over a degree-$2$ denominator — positively homogeneous of degree $2$. Homogeneity of degree $2$ is the resonance point for *second*-order pathology: the function is smooth enough to have first and second partials everywhere, but its second partials are homogeneous of degree $0$, which means they are *constant along rays* and therefore generically *discontinuous at the origin* (a degree-$0$ homogeneous function takes a fixed value on each ray and the values across rays need not match up). The recognisable feature: degree-$2$ homogeneity with an antisymmetric factor $x^2 - y^2$, which is exactly engineered to make the two mixed partials pick up opposite signs.

**Theorem routing.** The mixed partial $\partial_y\partial_x f(0,0)$ must be computed by *iterated limits*: first find $\partial_x f$ as a function (everywhere, including the origin), then differentiate *that* in $y$ at the origin via the limit definition. There is no shortcut — the second partial at the origin sees the first partial along an axis. Part 1 does this twice, in the two orders, and the answers differ. Part 3 traces the disagreement to its source: the second partials, while existing, are discontinuous at the origin, so $f \notin C^2$ and Schwarz's hypothesis fails.

**Key decision point.** The non-obvious move is the order of operations in computing $\partial_y\partial_x f(0,0)$. One cannot just plug into a formula. The correct procedure: (i) compute $\partial_x f(x,y)$ for *all* $(x,y)$, getting one formula off the origin and the value $0$ at the origin (from the limit definition, since $f \equiv 0$ on the $x$-axis); (ii) then compute $\partial_y$ of this function $\partial_x f$ at the origin, again from the limit definition, which requires the values of $\partial_x f$ along the $y$-axis. The mixed partial is a limit of a limit, and the antisymmetric factor $x^2-y^2$ makes the $x$-axis and $y$-axis values of the first partials come out with opposite signs.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis I — Differentiation in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Compute first partials away from the origin by Analysis I rules.** Differentiate the explicit rational expression with the quotient rule.

2. **Compute partials at the origin from the limit definition.** Since $f$ is defined piecewise, $\partial_x f(0,0)$ and $\partial_y f(0,0)$ — and later the second partials — must be obtained from difference-quotient limits, not from any formula.

3. **Iterate the partial-derivative operation in a fixed order.** Compute $\partial_x f$ as a function, then differentiate it in $y$; separately compute $\partial_y f$, then differentiate in $x$.

4. **Diagnose a theorem's hypothesis by locating its failure.** Trace the disagreement to discontinuity of the second partials, identifying the failed "$C^2$" hypothesis of Schwarz's theorem.

---

# Hints

> [!note]- Hint 1
> First find $\partial_x f$ as a function on all of $\mathbb{R}^2$. Off the origin, differentiate $xy(x^2-y^2)/(x^2+y^2)$ in $x$ by the quotient rule. At the origin, use the limit definition: $\partial_x f(0,0) = \lim_{t\to0}(f(t,0)-f(0,0))/t$, and $f \equiv 0$ on the $x$-axis, so this is $0$.

> [!note]- Hint 2
> A cleaner route to the first partials: a short computation gives, for $(x,y)\neq(0,0)$,
> $$\partial_x f(x,y) = \frac{y(x^4 + 4x^2 y^2 - y^4)}{(x^2+y^2)^2}.$$
> Now you need $\partial_y\partial_x f(0,0) = \partial_y(\partial_x f)(0,0)$. By the limit definition this is $\lim_{t\to0}(\partial_x f(0,t) - \partial_x f(0,0))/t$. So evaluate $\partial_x f$ along the $y$-axis: set $x = 0$.

> [!note]- Hint 3
> Along the $y$-axis, $\partial_x f(0,y) = \dfrac{y(0 + 0 - y^4)}{(y^2)^2} = \dfrac{-y^5}{y^4} = -y$. And $\partial_x f(0,0) = 0$. So $\partial_y\partial_x f(0,0) = \lim_{t\to0}(-t - 0)/t = -1$.

> [!note]- Hint 4
> By the antisymmetry $f(x,y) = -f(y,x)$ (check: swapping $x,y$ negates $xy(x^2-y^2)$ and leaves $x^2+y^2$), the roles of $x$ and $y$ are exchanged with a sign flip. This forces $\partial_y f(x,0) = +x$ along the $x$-axis, hence $\partial_x\partial_y f(0,0) = +1$. The two mixed partials are $-1$ and $+1$. For Part 3: the second partials *exist* at the origin (you just computed two of them) but are they *continuous* there?

---

# Solution

The function is built to break Schwarz's theorem. The antisymmetry $f(x,y) = -f(y,x)$ guarantees that whatever sign $\partial_y\partial_x f(0,0)$ has, $\partial_x\partial_y f(0,0)$ has the opposite — so if the two are non-zero, they disagree. The degree-$2$ homogeneity makes the second partials homogeneous of degree $0$, hence discontinuous at the origin, which is exactly the hypothesis of Schwarz's theorem that fails.

**Step 1: The first partial $\partial_x f$ equals $\dfrac{y(x^4+4x^2y^2-y^4)}{(x^2+y^2)^2}$ off the origin and $0$ at the origin.**

> [!note]- Derivation
> *At the origin.* $f \equiv 0$ on the $x$-axis ($f(t,0) = t\cdot0\cdot(t^2)/(t^2) = 0$), so by the limit definition of the [[Def - Partial Derivatives and the Jacobian Matrix|partial derivative]], $\partial_x f(0,0) = \lim_{t\to0}(f(t,0)-f(0,0))/t = \lim_{t\to0}(0-0)/t = 0$. Likewise $\partial_y f(0,0) = 0$.
>
> *Off the origin.* For $(x,y)\neq(0,0)$, write $f = \dfrac{u}{v}$ with $u = xy(x^2-y^2) = x^3 y - x y^3$ and $v = x^2+y^2$. The quotient rule $\partial_x f = (v\,\partial_x u - u\,\partial_x v)/v^2$ with $\partial_x u = 3x^2 y - y^3$ and $\partial_x v = 2x$ gives
> $$\partial_x f = \frac{(x^2+y^2)(3x^2 y - y^3) - (x^3 y - x y^3)(2x)}{(x^2+y^2)^2}.$$
> Expanding the numerator: $(x^2+y^2)(3x^2y-y^3) = 3x^4 y - x^2 y^3 + 3x^2 y^3 - y^5 = 3x^4 y + 2x^2 y^3 - y^5$, and $(x^3y - xy^3)(2x) = 2x^4 y - 2x^2 y^3$. Subtracting,
> $$\partial_x f = \frac{3x^4 y + 2x^2 y^3 - y^5 - 2x^4 y + 2x^2 y^3}{(x^2+y^2)^2} = \frac{x^4 y + 4x^2 y^3 - y^5}{(x^2+y^2)^2} = \frac{y(x^4 + 4x^2 y^2 - y^4)}{(x^2+y^2)^2}.$$

**Step 2: $\partial_y\partial_x f(0,0) = -1$.**

> [!note]- Derivation
> The mixed partial $\partial_y\partial_x f(0,0)$ is, by definition, $\partial_y$ of the function $\partial_x f$, evaluated at the origin — and by the limit definition,
> $$\partial_y\partial_x f(0,0) = \lim_{t\to0}\frac{\partial_x f(0,t) - \partial_x f(0,0)}{t}.$$
> Evaluate $\partial_x f$ along the $y$-axis: set $x = 0$ in the Step 1 formula,
> $$\partial_x f(0,t) = \frac{t(0 + 0 - t^4)}{(0+t^2)^2} = \frac{-t^5}{t^4} = -t.$$
> And $\partial_x f(0,0) = 0$ from Step 1. Therefore
> $$\partial_y\partial_x f(0,0) = \lim_{t\to0}\frac{-t - 0}{t} = \lim_{t\to0}(-1) = -1.$$

**Step 3: $\partial_x\partial_y f(0,0) = +1$, by the antisymmetry of $f$.**

> [!note]- Derivation
> The function is antisymmetric under swapping the variables: $f(y,x) = yx(y^2-x^2)/(y^2+x^2) = -xy(x^2-y^2)/(x^2+y^2) = -f(x,y)$. Differentiating the identity $f(y,x) = -f(x,y)$, the roles of $x$ and $y$ are exchanged with an overall sign change. Concretely, by the same computation as Steps 1–2 with $x$ and $y$ interchanged, $\partial_y f(x,0) = +x$ along the $x$-axis (the sign flips relative to $\partial_x f(0,y) = -y$ because of the antisymmetry), and so
> $$\partial_x\partial_y f(0,0) = \lim_{t\to0}\frac{\partial_y f(t,0) - \partial_y f(0,0)}{t} = \lim_{t\to0}\frac{t - 0}{t} = +1.$$
> Hence $\partial_x\partial_y f(0,0) = +1$ while $\partial_y\partial_x f(0,0) = -1$: **the mixed partials disagree.**

**Step 4: No contradiction with Schwarz's theorem — $f$ is not $C^2$ at the origin.**

> [!note]- Derivation
> [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]] asserts $\partial_x\partial_y f = \partial_y\partial_x f$ **only for $C^2$ functions** — functions whose second partials exist *and are continuous*. Here the second partials *exist* at the origin (Steps 2–3 computed two of them), so the failure must be in *continuity*.
>
> It is. The function $f$ is positively homogeneous of degree $2$: $f(tx,ty) = t^2 f(x,y)$. Differentiating twice lowers the degree of homogeneity by $2$, so each second partial $\partial_i\partial_j f$ is positively homogeneous of degree $0$ — it is *constant along every ray* from the origin. A non-constant degree-$0$ homogeneous function takes different constant values on different rays, so it cannot have a limit at the origin: approaching along one ray gives one value, along another ray a different value. Concretely, $\partial_y\partial_x f$ takes the value $-1$ approached along the $y$-axis but, by an analogous computation, a different value along the $x$-axis — so $\lim_{(x,y)\to0}\partial_y\partial_x f(x,y)$ does not exist, and $\partial_y\partial_x f$ is discontinuous at the origin.
>
> Therefore $f \notin C^2$ at the origin: the hypothesis of Schwarz's theorem fails, and the theorem makes no claim. The disagreement $\partial_x\partial_y f(0,0) = +1 \neq -1 = \partial_y\partial_x f(0,0)$ is fully consistent with Schwarz's theorem — it is exactly the kind of behaviour the $C^2$ hypothesis is there to exclude.

> [!note]- Complete formal solution
> **Claim.** For $f$ as defined, $\partial_x\partial_y f(0,0) = +1 \neq -1 = \partial_y\partial_x f(0,0)$, with no contradiction to Schwarz's theorem since $f \notin C^2$.
>
> Off the origin the quotient rule gives $\partial_x f(x,y) = y(x^4+4x^2y^2-y^4)/(x^2+y^2)^2$; at the origin $\partial_x f(0,0) = 0$ since $f\equiv0$ on the $x$-axis. Along the $y$-axis $\partial_x f(0,t) = -t^5/t^4 = -t$, so $\partial_y\partial_x f(0,0) = \lim_{t\to0}(-t)/t = -1$. By the antisymmetry $f(x,y) = -f(y,x)$, the analogous computation gives $\partial_y f(t,0) = t$ and $\partial_x\partial_y f(0,0) = \lim_{t\to0}t/t = +1$.
>
> The mixed partials disagree. This does not contradict [[Thm - Schwarz's Theorem on Mixed Partials]], whose hypothesis is $f \in C^2$. Here $f$ is positively homogeneous of degree $2$, so its second partials are homogeneous of degree $0$ — constant on rays, hence discontinuous at the origin. Thus $f \notin C^2$ and Schwarz's theorem does not apply. $\blacksquare$

---

# Key Takeaways

**The equality of mixed partials is a theorem with a hypothesis, not a law of notation — and this function is the permanent reminder.** Multi-index notation writes $\partial^\alpha f$ as though the order of differentiation were irrelevant, and the temptation is to treat that as a definitional truth. It is not: it is the *conclusion* of [[Thm - Schwarz's Theorem on Mixed Partials|Schwarz's theorem]], valid only when $f$ is $C^2$. This exercise exhibits a concrete function — both mixed partials existing, yet equal to $+1$ and $-1$ — for which the conclusion is false. The operational rule that follows is firm: before reordering any string of partial derivatives, before writing a higher derivative in multi-index form, before treating the Hessian as symmetric, confirm the function is $C^2$ (or $C^k$) on the relevant set. For functions given by elementary formulas this is automatic and the check is instant; for piecewise-defined functions at their join points it is exactly where the danger lives.

**Computing a mixed partial at a suspect point is a limit of a limit, performed in a fixed order — there is no formula to plug into.** The single most error-prone part of this exercise is the *procedure* for $\partial_y\partial_x f(0,0)$. It is not "substitute into a second-partial formula". It is: first compute the function $\partial_x f$ — its formula off the origin and its value *at* the origin from the difference-quotient limit — and only then differentiate that function in $y$ at the origin, again from the limit definition, which forces you to know $\partial_x f$ along the $y$-axis. The mixed partial at the origin reaches through the first partial evaluated along an axis. Doing the two orders, $\partial_y\partial_x$ and $\partial_x\partial_y$, means evaluating the *two different* first partials along *two different* axes — and that is precisely how an antisymmetric function can deliver opposite signs. Whenever a piecewise function's higher partial is wanted at the join point, this iterated-limit discipline is mandatory.

**Homogeneity of degree $d$ predicts exactly which order of pathology to expect: degree-$d$ functions have order-$d$ partials that are degree-$0$, hence discontinuous.** The reason this particular function works is structural and reusable. $f$ is positively homogeneous of degree $2$. Each differentiation lowers the homogeneity degree by $1$, so the *first* partials are degree-$1$ homogeneous (continuous at the origin — degree-$1$ homogeneous functions vanish there and are continuous) but the *second* partials are degree-$0$ homogeneous: constant along each ray, generically taking different constants on different rays, hence discontinuous at the origin. Discontinuous second partials are exactly the failure of $C^2$, which is exactly the failure of Schwarz's hypothesis. The general principle: a function homogeneous of degree $d$ at the origin is typically $C^{d-1}$ but not $C^d$ there, because the order-$d$ partials hit degree-$0$ homogeneity and lose continuity. To build a counterexample to "$C^{k-1}$ implies $C^k$" or to the order-independence of order-$k$ partials, reach for a degree-$k$ homogeneous function with a numerator antisymmetric in the relevant variables — the antisymmetry is what makes the two orders of differentiation produce genuinely different answers rather than merely discontinuous ones.
