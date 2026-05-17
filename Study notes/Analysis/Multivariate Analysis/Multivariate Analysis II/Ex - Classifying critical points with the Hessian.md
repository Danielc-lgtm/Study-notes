---
type: exercise
subject: multivariate-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Critical Point, Hessian, and Definiteness"
  - "Thm - First-Order Optimality Condition"
  - "Thm - Second-Order Optimality Conditions"
tags: [analysis, multivariate-analysis]
---

# Problem Statement

Let $\alpha \in \mathbb{R}$ be a parameter. Consider the function
$$f : \mathbb{R}^2 \to \mathbb{R}, \qquad f(x,y) = x^3 - y^3 + 3\alpha xy.$$

1. Find all points $(x,y) \in \mathbb{R}^2$ where the gradient of $f$ vanishes, as a function of $\alpha$.
2. For each such critical point, determine whether it is a local minimum, a local maximum, or a saddle point, using the Hessian. Handle every value of $\alpha$, including the cases where the Hessian test is inconclusive.

**Recall:**

The objects in play are the gradient, the critical-point condition, the Hessian matrix, and the second-order test.

![[Def - Critical Point, Hessian, and Definiteness#The Definition]]

A point $(x_0,y_0)$ is a [[Def - Critical Point, Hessian, and Definiteness|critical point]] of $f$ when $\nabla f(x_0,y_0) = 0$. By the [[Thm - First-Order Optimality Condition|first-order optimality condition]], every interior local extremum is a critical point, so the critical points are the complete candidate list. By the [[Thm - Second-Order Optimality Conditions|second-order optimality conditions]], at a critical point a positive definite Hessian gives a strict local minimum, a negative definite Hessian a strict local maximum, an indefinite Hessian a saddle; a degenerate Hessian (one with $0$ as an eigenvalue) makes the test inconclusive.

For a symmetric $2\times 2$ matrix $H = \begin{pmatrix} a & b \\ b & c\end{pmatrix}$, the eigenvalue signs are read off from $\det H = ac - b^2$ and $\operatorname{tr} H = a + c$: if $\det H > 0$ the eigenvalues have the same sign, given by the sign of $a$ (positive definite if $a > 0$, negative definite if $a < 0$); if $\det H < 0$ the eigenvalues have opposite signs (indefinite); if $\det H = 0$ the matrix is degenerate.

---

# Convergent Strategy

**Problem class.** This is an *unconstrained optimization* problem on an open set ($\mathbb{R}^2$), with a parameter. As the [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Problem-Solving Strategy|topic's problem-solving strategy]] records, the route for unconstrained extrema is fixed: solve $\nabla f = 0$ for the candidates, then classify each with the Hessian.

**Assumption pattern.** The function is a polynomial, so $\nabla f = 0$ is a polynomial system — it will have finitely many solutions, and they can be found by elementary algebra. The presence of the parameter $\alpha$ means the *number and nature* of the critical points changes with $\alpha$; the problem is really a small bifurcation analysis.

**Theorem routing.** Step 1 is the [[Thm - First-Order Optimality Condition|first-order condition]]: $\nabla f = (3x^2 + 3\alpha y, -3y^2 + 3\alpha x) = 0$. Step 2 is the [[Thm - Second-Order Optimality Conditions|second-order test]] applied to the Hessian $Hf = \begin{pmatrix} 6x & 3\alpha \\ 3\alpha & -6y\end{pmatrix}$ at each critical point.

**Key decision point.** The non-obvious part is that the *origin* is a critical point for every $\alpha$, and there the Hessian is $\begin{pmatrix} 0 & 3\alpha \\ 3\alpha & 0\end{pmatrix}$, which is *degenerate when $\alpha = 0$* and indefinite when $\alpha \neq 0$. The degenerate case $\alpha = 0$ is exactly where the Hessian test fails and one must look at the function directly — this is the part the problem is testing.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Multivariate Analysis II — Inverse and Implicit Function Theorems#Legal Operations|the topic page's Legal Operations]]:

1. **Set $\nabla f = 0$ to find interior extrema.** Solve the polynomial system $3x^2 + 3\alpha y = 0$, $-3y^2 + 3\alpha x = 0$ for all critical points.

2. **Read the Hessian's sign to classify a critical point.** At each critical point compute $Hf$ and apply the $2\times 2$ determinant test.

3. **Examine the function directly when the Hessian is degenerate.** At $\alpha = 0$ the origin has a zero Hessian; restrict $f$ to lines through the origin to diagnose the behaviour by hand.

---

# Hints

> [!note]- Hint 1
> Compute $\nabla f = (3x^2 + 3\alpha y, \ -3y^2 + 3\alpha x)$ and set both components to zero. From the first equation, $y = -x^2/\alpha$ (when $\alpha \neq 0$); substitute into the second.

> [!note]- Hint 2
> Substituting gives $-y^2 + \alpha x = 0$ with $y = -x^2/\alpha$, i.e. $-x^4/\alpha^2 + \alpha x = 0$, so $x(x^3 - \alpha^3) = 0$. The solutions are $x = 0$ and $x = \alpha$. This yields two critical points (when $\alpha \neq 0$).

> [!note]- Hint 3
> The Hessian is $Hf(x,y) = \begin{pmatrix} 6x & 3\alpha \\ 3\alpha & -6y\end{pmatrix}$, with $\det Hf = -36xy - 9\alpha^2$. Evaluate this at each critical point. At the origin $\det = -9\alpha^2$; at the other point $\det = 27\alpha^2$ — note the *signs*.

> [!note]- Hint 4
> When $\alpha = 0$ the only critical point is the origin and $Hf(0,0)$ is the zero matrix — the test is inconclusive. Look at $f(x,0) = x^3$, which changes sign through $x = 0$: so the origin is *not* an extremum even though the Hessian says nothing. It is a (degenerate) non-extremum.

---

# Solution

The function is a cubic polynomial, so its critical points are the finitely many roots of a polynomial system, and almost all of them are cleanly classified by the determinant of a $2\times 2$ Hessian. The only delicacy is the value $\alpha = 0$, where the Hessian at the origin degenerates and the answer must be read off the function itself.

**Step 1: The critical points.**

The gradient is $\nabla f = (3x^2 + 3\alpha y,\ -3y^2 + 3\alpha x)$. For $\alpha \neq 0$ there are exactly two critical points: the origin $(0,0)$ and the point $(\alpha, -\alpha)$. For $\alpha = 0$ the only critical point is the origin.

> [!note]- Derivation
> Set $\nabla f = 0$:
> $$3x^2 + 3\alpha y = 0 \quad\Longrightarrow\quad x^2 + \alpha y = 0, \tag{1}$$
> $$-3y^2 + 3\alpha x = 0 \quad\Longrightarrow\quad -y^2 + \alpha x = 0. \tag{2}$$
>
> *Case $\alpha = 0$.* Equations (1)–(2) become $x^2 = 0$ and $y^2 = 0$, so $x = y = 0$. The origin is the only critical point.
>
> *Case $\alpha \neq 0$.* From (1), $y = -x^2/\alpha$. Substitute into (2):
> $$-\frac{x^4}{\alpha^2} + \alpha x = 0 \quad\Longrightarrow\quad x\Big(\alpha - \frac{x^3}{\alpha^2}\Big) = 0 \quad\Longrightarrow\quad x(\alpha^3 - x^3) = 0.$$
> Over the reals this gives $x = 0$ or $x = \alpha$. If $x = 0$ then $y = -0/\alpha = 0$: the origin $(0,0)$. If $x = \alpha$ then $y = -\alpha^2/\alpha = -\alpha$: the point $(\alpha, -\alpha)$. So for $\alpha \neq 0$ the critical points are exactly $(0,0)$ and $(\alpha, -\alpha)$.

**Step 2: Classifying $(\alpha, -\alpha)$ for $\alpha \neq 0$.**

The Hessian at $(\alpha,-\alpha)$ has determinant $27\alpha^2 > 0$ and trace $6\alpha + 6\alpha = 12\alpha$. So this critical point is a **strict local minimum when $\alpha > 0$** and a **strict local maximum when $\alpha < 0$**.

> [!note]- Derivation
> The Hessian of $f$ is
> $$Hf(x,y) = \begin{pmatrix} \partial_{xx}f & \partial_{xy}f \\ \partial_{yx}f & \partial_{yy}f\end{pmatrix} = \begin{pmatrix} 6x & 3\alpha \\ 3\alpha & -6y\end{pmatrix},$$
> with determinant $\det Hf = (6x)(-6y) - (3\alpha)^2 = -36xy - 9\alpha^2$.
>
> At $(\alpha, -\alpha)$: $xy = \alpha\cdot(-\alpha) = -\alpha^2$, so
> $$\det Hf(\alpha,-\alpha) = -36(-\alpha^2) - 9\alpha^2 = 36\alpha^2 - 9\alpha^2 = 27\alpha^2 > 0 \quad (\alpha \neq 0).$$
> Since the determinant is positive, the two eigenvalues have the same sign, determined by the top-left entry $6x = 6\alpha$. If $\alpha > 0$ the top-left entry is positive, so the Hessian is positive definite — a strict local minimum by the [[Thm - Second-Order Optimality Conditions|second-order conditions]]. If $\alpha < 0$ the top-left entry is negative, so the Hessian is negative definite — a strict local maximum.

**Step 3: Classifying the origin for $\alpha \neq 0$.**

The Hessian at the origin has determinant $-9\alpha^2 < 0$, so it is indefinite: the origin is a **saddle point** for every $\alpha \neq 0$.

> [!note]- Derivation
> At $(0,0)$, $xy = 0$, so
> $$\det Hf(0,0) = -36\cdot 0 - 9\alpha^2 = -9\alpha^2 < 0 \quad (\alpha \neq 0).$$
> A negative determinant means the two eigenvalues have opposite signs: the Hessian is indefinite. By the [[Thm - Second-Order Optimality Conditions|second-order conditions]], the origin is a saddle point — neither a local maximum nor a local minimum.

**Step 4: The degenerate case $\alpha = 0$.**

When $\alpha = 0$ the only critical point is the origin, and its Hessian is the zero matrix — the test is inconclusive. Direct inspection shows the origin is **not an extremum**: $f(x,0) = x^3$ takes both signs through $x = 0$.

> [!note]- Derivation
> For $\alpha = 0$, $f(x,y) = x^3 - y^3$, and $Hf(0,0) = \begin{pmatrix} 0 & 0 \\ 0 & 0\end{pmatrix}$, which is degenerate (both eigenvalues are $0$). The [[Thm - Second-Order Optimality Conditions|second-order test]] is silent.
>
> Restrict $f$ to the $x$-axis: $\varphi(x) = f(x,0) = x^3$. For small $x > 0$, $\varphi(x) = x^3 > 0 = f(0,0)$, and for small $x < 0$, $\varphi(x) = x^3 < 0 = f(0,0)$. So in every neighbourhood of the origin there are points where $f$ exceeds $f(0,0)$ and points where $f$ is below it. The origin is therefore neither a local maximum nor a local minimum — a degenerate non-extremum. (It is sometimes called a *monkey saddle*-type point, though strictly $x^3 - y^3$ on the line $y = x$ is $0$ identically.)

> [!note]- Complete formal solution
> **Critical points.** $\nabla f = (3x^2 + 3\alpha y, -3y^2 + 3\alpha x)$. Setting this to zero: from $x^2 + \alpha y = 0$ and $-y^2 + \alpha x = 0$. If $\alpha = 0$, the only solution is $(0,0)$. If $\alpha \neq 0$, substitute $y = -x^2/\alpha$ into the second equation to get $x(\alpha^3 - x^3) = 0$, so $x \in \{0, \alpha\}$, giving critical points $(0,0)$ and $(\alpha,-\alpha)$.
>
> **Hessian.** $Hf(x,y) = \begin{pmatrix} 6x & 3\alpha \\ 3\alpha & -6y\end{pmatrix}$, $\det Hf = -36xy - 9\alpha^2$.
>
> *Point $(\alpha,-\alpha)$, $\alpha \neq 0$:* $\det Hf = 36\alpha^2 - 9\alpha^2 = 27\alpha^2 > 0$, top-left entry $6\alpha$. Positive definite (strict local minimum) if $\alpha > 0$; negative definite (strict local maximum) if $\alpha < 0$.
>
> *Point $(0,0)$, $\alpha \neq 0$:* $\det Hf = -9\alpha^2 < 0$. Indefinite — a saddle point.
>
> *Point $(0,0)$, $\alpha = 0$:* $Hf(0,0) = 0$, degenerate, test inconclusive. Since $f(x,0) = x^3$ changes sign through $x = 0$, the origin is not an extremum.
>
> **Summary.** For $\alpha > 0$: $(\alpha,-\alpha)$ is a strict local minimum, $(0,0)$ is a saddle. For $\alpha < 0$: $(\alpha,-\alpha)$ is a strict local maximum, $(0,0)$ is a saddle. For $\alpha = 0$: the origin is the only critical point and is not an extremum. $\blacksquare$

---

# Key Takeaways

**For polynomial functions, finding critical points is solving a polynomial system, and the parameter turns the problem into a bifurcation analysis.** The first-order condition $\nabla f = 0$ here is two polynomial equations, and the elimination move — solve one equation for a variable, substitute into the other — reduces it to a single one-variable polynomial $x(\alpha^3 - x^3) = 0$. The factored form is what makes the parameter dependence visible: the factor $\alpha^3 - x^3$ produces a critical point at $x = \alpha$ that *merges with the origin* as $\alpha \to 0$, and the number of critical points drops from two to one. Whenever a function carries a parameter, expect the critical-point count and their classification to change at special parameter values, and look for those values as the roots of the discriminant-type expressions that appear — here, $\alpha = 0$.

**The $2\times 2$ Hessian is classified by one determinant and one sign, with no eigenvalue computation.** For a symmetric $2\times 2$ matrix the determinant is the product of the eigenvalues and the trace is their sum, so $\det > 0$ forces equal signs (read off from any diagonal entry), $\det < 0$ forces opposite signs (indefinite, a saddle), and $\det = 0$ is the degenerate boundary. This is the fastest classification available in two variables and should be the reflex: compute $\det Hf$ at the critical point and look at its sign before doing anything else. The pattern generalizes — in higher dimensions one uses the *leading principal minors* (Sylvester's criterion), all positive for positive definiteness, alternating in sign for negative definiteness.

**A degenerate Hessian is not a failure of method but a signal to change tools — restrict to lines.** When $\det Hf = 0$ the second-order Taylor term has a flat direction and carries no information; the [[Thm - Second-Order Optimality Conditions|second-order test]] is genuinely silent, and applying it anyway is the characteristic illegal move flagged on the topic page. The correct response is to probe the function directly, and the cheapest probe is to restrict $f$ to lines through the critical point: if even *one* line shows $f$ changing sign (as $f(x,0) = x^3$ does here), the point cannot be an extremum. If all lines show the same sign behaviour, you have evidence — though, in genuinely subtle cases, a line restriction can still mislead and one must examine the function on curves or use the full higher-order expansion. The trigger "$\det Hf = 0$" should immediately summon "restrict to lines and look by hand", never "apply the test anyway".

**The candidate list comes from the first-order condition; the classification comes from the second — and the two must always both be done.** The first-order condition is *necessary but not sufficient*: every critical point found in Step 1 is only a candidate, and Step 2 is what separates the genuine minima and maxima from the saddles. Here, of the (up to) two critical points, one is always a saddle — a critical point that is emphatically not an extremum. Skipping the Hessian classification and reporting all critical points as extrema is the most common error in optimization problems, and this exercise is calibrated to expose it: the origin is a critical point for every $\alpha$, yet it is never an extremum.
