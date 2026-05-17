---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Thm - Fubini's Theorem"
  - "Def - The Riemann Integral in Several Variables"
  - "Def - Jordan Measure"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Evaluate the iterated integral
$$\int_0^1 \int_x^1 e^{y^2} \, dy \, dx.$$

The obstacle is immediate: $e^{y^2}$ has no elementary antiderivative, so the inner integral $\int_x^1 e^{y^2}\,dy$ cannot be written in closed form. Reverse the order of integration.

**Recall:**

![[Thm - Fubini's Theorem#Statement]]

[[Thm - Fubini's Theorem|Fubini's theorem]] asserts that for an integrable function the two iterated integrals are equal:
$$\int\!\!\int f\,dy\,dx = \int\!\!\int f\,dx\,dy,$$
*provided* $f$ is integrable on the region. Here $f(x,y) = e^{y^2}$ is continuous and the region is bounded by line segments (a [[Def - Jordan Measure|Jordan measurable]] triangle), so the hypothesis holds and either order is legal. The value of the integral is order-independent; the *difficulty* is not.

---

# Convergent Strategy

**Problem class.** This is an *evaluation-by-order-reversal* problem: a multiple integral whose inner integral is intractable in the order given. The [[Multivariate Analysis III — Integration in Several Variables#Problem-Solving Strategy|topic strategy]] names this directly — when the inner integral has no elementary antiderivative, redescribe the region from the other variable's standpoint and integrate the other way.

**Assumption pattern.** The recognizable feature is a non-elementary inner integrand — $e^{y^2}$, $\sin(y^2)$, $e^{-y^2}$, $\frac{\sin y}{y}$ — appearing as the *inner* function. Such an integrand can sometimes be integrated elementarily *in the other variable*, because the other variable enters only through the limits.

**Theorem routing.** First read off the region from the given integral: $0 \leq x \leq 1$, $x \leq y \leq 1$ — this is the triangle $\{0 \leq x \leq y \leq 1\}$. Then re-describe the *same* triangle with $y$ as the outer variable: $0 \leq y \leq 1$, $0 \leq x \leq y$. Fubini swaps the order, and now the inner integral is $\int_0^y e^{y^2}\,dx$, in which $e^{y^2}$ is a *constant* — trivially integrated.

**Key decision point.** The non-obvious move is recognizing that the *region* is the fixed object and the two iterated integrals are two descriptions of it. Reversing the order is not a symbolic manipulation of the integral; it is a re-reading of the region's defining inequalities $0 \leq x \leq y \leq 1$ from the other end. The reason the swap helps: after the swap, $y$ becomes the outer variable, so $e^{y^2}$ is constant during the inner ($x$) integration, and the outer integral $\int y\,e^{y^2}\,dy$ is solvable by the substitution $u = y^2$.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|the topic page's Legal Operations]]:

1. **Reverse the order of integration.** The intractable order $dy\,dx$ is swapped to $dx\,dy$ by re-describing the triangular region.

2. **Reduce a multiple integral to iterated single integrals (Fubini).** Both descriptions of the integral are iterated forms; Fubini certifies they are equal.

3. **One-variable substitution.** The surviving outer integral $\int_0^1 y\,e^{y^2}\,dy$ is evaluated by $u = y^2$.

---

# Hints

> [!note]- Hint 1
> You cannot do the inner integral $\int_x^1 e^{y^2}\,dy$ — $e^{y^2}$ has no elementary antiderivative. Do not look for one. The fix is structural: change which variable is integrated first.

> [!note]- Hint 2
> Read the region off the limits as given: $x$ runs from $0$ to $1$, and for each $x$, $y$ runs from $x$ to $1$. So the region is $\{(x,y) : 0 \leq x \leq 1,\ x \leq y \leq 1\}$. Sketch it — it is a triangle. What triangle?

> [!note]- Hint 3
> The region is the triangle $\{0 \leq x \leq y \leq 1\}$. Now describe it the other way: let $y$ be outer. For a fixed $y \in [0,1]$, what range does $x$ cover? (Answer: $0 \leq x \leq y$.) Rewrite the integral as $\int_0^1\int_0^y e^{y^2}\,dx\,dy$.

> [!note]- Hint 4
> In $\int_0^y e^{y^2}\,dx$, the factor $e^{y^2}$ does not involve $x$ — it is a constant for this integration. So the inner integral is just $e^{y^2} \cdot y$. The outer integral $\int_0^1 y\,e^{y^2}\,dy$ then yields to the substitution $u = y^2$.

---

# Solution

The inner integral is impossible in the given order because $e^{y^2}$ has no elementary antiderivative. But the region is a triangle, and described the other way the inner variable $x$ enters $e^{y^2}$ not at all — so after the swap the inner integral is trivial.

**Step 1: Identify the region of integration.**

The limits $0 \leq x \leq 1$, $x \leq y \leq 1$ describe the triangle $T = \{(x,y) : 0 \leq x \leq y \leq 1\}$.

> [!note]- Derivation
> The given integral $\int_0^1\int_x^1 e^{y^2}\,dy\,dx$ has $x$ as the outer variable, running over $[0,1]$, and for each such $x$ the inner variable $y$ runs from $x$ to $1$. The region swept is
> $$T = \{(x,y) : 0 \leq x \leq 1,\ x \leq y \leq 1\} = \{(x,y) : 0 \leq x \leq y \leq 1\}.$$
> This is the triangle with vertices $(0,0)$, $(0,1)$, $(1,1)$ — the points of the unit square on or above the diagonal $y = x$. Its boundary consists of three line segments (graphs of affine functions, content zero), so $T$ is [[Def - Jordan Measure|Jordan measurable]]; the integrand $e^{y^2}$ is continuous; hence the integral is defined and [[Thm - Fubini's Theorem|Fubini's theorem]] permits either order of integration.

**Step 2: Re-describe the region with $y$ outer, and swap the order.**

$T = \{(x,y) : 0 \leq y \leq 1,\ 0 \leq x \leq y\}$, so the integral becomes $\int_0^1\int_0^y e^{y^2}\,dx\,dy$.

> [!note]- Derivation
> The triangle $T = \{0 \leq x \leq y \leq 1\}$ can be described from the $y$-standpoint. Fix $y \in [0,1]$; the horizontal slice $\{x : (x,y) \in T\}$ consists of all $x$ with $0 \leq x \leq y$. So
> $$T = \{(x,y) : 0 \leq y \leq 1,\ 0 \leq x \leq y\},$$
> a region between the graphs $x = 0$ and $x = y$ over the base $[0,1]$ in the $y$-axis. By [[Thm - Fubini's Theorem|Fubini's theorem]] — applicable because $e^{y^2}$ is integrable on the Jordan measurable $T$ — the two iterated integrals are equal:
> $$\int_0^1\int_x^1 e^{y^2}\,dy\,dx = \iint_T e^{y^2}\,dA = \int_0^1\int_0^y e^{y^2}\,dx\,dy.$$

**Step 3: Evaluate the inner integral — now trivial.**

$\displaystyle \int_0^y e^{y^2}\,dx = y\,e^{y^2}$.

> [!note]- Derivation
> In the inner integral $\int_0^y e^{y^2}\,dx$ the variable of integration is $x$, and the integrand $e^{y^2}$ contains no $x$ at all — it is a constant with respect to $x$. Integrating a constant over $[0, y]$ multiplies it by the length $y$:
> $$\int_0^y e^{y^2}\,dx = e^{y^2}\int_0^y dx = e^{y^2}\cdot y = y\,e^{y^2}.$$
> This is the entire point of reversing the order: the obstruction $e^{y^2}$ has been moved *outside* the inner integration, where it needs no antiderivative.

**Step 4: Evaluate the outer integral by substitution.**

$\displaystyle \int_0^1 y\,e^{y^2}\,dy = \frac{e - 1}{2}$.

> [!note]- Derivation
> Substitute $u = y^2$, so $du = 2y\,dy$ and $y\,dy = \tfrac12\,du$; as $y$ runs $0 \to 1$, $u$ runs $0 \to 1$:
> $$\int_0^1 y\,e^{y^2}\,dy = \int_0^1 e^{u}\cdot\frac{1}{2}\,du = \frac{1}{2}\big[ e^u \big]_0^1 = \frac{e - 1}{2}.$$
> Therefore
> $$\int_0^1\int_x^1 e^{y^2}\,dy\,dx = \frac{e - 1}{2}. \qquad \blacksquare$$

> [!note]- Complete formal solution
> The limits $0 \leq x \leq 1$, $x \leq y \leq 1$ describe the triangle $T = \{0 \leq x \leq y \leq 1\}$, which is Jordan measurable; $e^{y^2}$ is continuous, so by [[Thm - Fubini's Theorem|Fubini's theorem]] the order may be reversed. Describing $T$ with $y$ outer gives $\{0 \leq y \leq 1,\ 0 \leq x \leq y\}$, hence
> $$\int_0^1\int_x^1 e^{y^2}\,dy\,dx = \int_0^1\int_0^y e^{y^2}\,dx\,dy = \int_0^1 y\,e^{y^2}\,dy.$$
> With $u = y^2$, $y\,dy = \tfrac12\,du$, this is $\tfrac12\int_0^1 e^u\,du = \tfrac12(e - 1)$. $\blacksquare$

---

# Key Takeaways

**When the inner integral has no elementary antiderivative, reverse the order — the obstruction often vanishes.** The trigger is unmistakable: the inner integrand is one of the famous non-elementary functions ($e^{\pm y^2}$, $\sin y^2$, $\frac{\sin y}{y}$, $e^{y}/y$) and it sits in the *inner* position. Reversing the order moves the troublesome variable to the *outer* position, where it is a constant during the inner integration and needs no antiderivative at all; the inner integral then collapses to (constant)$\times$(slice length). The outer integral that remains typically *does* have an elementary antiderivative, often after a simple substitution, because the slice length supplies exactly the extra factor — here the factor $y$ — that a substitution like $u = y^2$ needs. This is one of the highest-leverage techniques in multivariable integration: a problem that looks impossible becomes routine purely by changing which variable goes first.

**The region is the invariant object; the two iterated integrals are two readings of it.** Reversing the order is not symbolic trickery — it is re-describing one fixed region from the other coordinate axis's point of view. The reliable procedure has three steps: (1) read the region off the *given* limits as a set of inequalities, (2) sketch it, (3) re-solve those same inequalities for the other variable as the outer one. Here $0 \leq x \leq 1,\ x \leq y \leq 1$ and $0 \leq y \leq 1,\ 0 \leq x \leq y$ are the same triangle $\{0 \leq x \leq y \leq 1\}$ read two ways. The error to avoid is to manipulate the limits formally without redrawing the region — the new inner limits must be re-derived from the geometry, not guessed from the old ones.

**Order-reversal is licensed by Fubini, and the hypothesis is genuine.** The equality of the two iterated integrals is exactly [[Thm - Fubini's Theorem|Fubini's theorem]], and it holds here because $e^{y^2}$ is continuous on the Jordan measurable triangle — bounded, integrable. The swap would *not* be automatically legal for an unbounded or non-integrable integrand: the [[Multivariate Analysis III — Integration in Several Variables#Legal Operations|standard counterexample]] $(x^2-y^2)/(x^2+y^2)^2$ has both iterated integrals existing and unequal precisely because it is not integrable. The discipline: before reversing, confirm integrability — here via continuity on a bounded Jordan measurable region — so that the equality you are exploiting is actually true.
