---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Penalty Algorithm"
  - "Def - Constrained Nonlinear Least Squares"
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
tags: [algebra, linear-algebra, applied, optimization]
---

# Problem Statement

Consider the equality-constrained quadratic problem
$$\min_{x_1, x_2} \; (x_1 - 1)^2 + (x_2 - 1)^2 \quad \text{subject to} \quad x_1 + x_2 = 1.$$
This is a *linear* equality-constrained least squares problem (with $f$ affine and $g$ linear), so the constrained minimum can be computed in closed form via the [[Def - KKT System|KKT system]]; the answer is $\hat x = (1/2, 1/2)$ with Lagrange multiplier $\hat z = -1$.

**(a)** Solve the problem in closed form using the linear KKT system from [[Linear Algebra XI — Applied II — Least Squares|Topic XI]]. Identify $\hat x$ and $\hat z$ explicitly.

**(b)** Apply the **penalty algorithm** with $\mu^{(1)} = 1$, $\mu^{(k+1)} = 2 \mu^{(k)}$, starting from $x^{(1)} = (0, 0)$. Compute the iterates $x^{(2)}, x^{(3)}, x^{(4)}$ explicitly (note: each inner subproblem is a *linear* least squares, solvable in closed form). Track the implicit multiplier $z^{(k+1)} = 2 \mu^{(k)} g(x^{(k+1)})$ and compare to $\hat z$.

**(c)** Verify the rate $\|g(x^{(k+1)})\| = O(1/\mu^{(k)})$ predicted by [[Thm - Convergence of Penalty Algorithm]] from the explicit iterates.

**(d)** Discuss in one paragraph why this problem is a useful pedagogical baseline despite being "trivial" (because the inner subproblem is linear and can be solved exactly).

**Recall:**

For a linear LS problem $\min \|Ax - b\|^2$ s.t. $Cx = d$, the [[Def - KKT System|KKT system]] is
$$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} \hat x \\ \hat z \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix}.$$

![[Def - Penalty Algorithm#The Definition]]

By [[Thm - Convergence of Penalty Algorithm]], the iterates satisfy $\|g(x^{(k+1)})\| = O(1/\mu^{(k)})$ and the implicit multiplier $2\mu^{(k)} g(x^{(k+1)})$ converges to $\hat z$.

For this problem $A = I$, $b = (1, 1)$, $C = (1, 1)$ (as a $1 \times 2$ matrix), $d = 1$.

---

# Convergent Strategy

**Problem class.** This is a *pedagogical demonstration* of the penalty algorithm on a problem where every step can be done by hand. The constrained problem is a linear LS with linear equality constraint — exactly the [[Def - Constrained Least Squares|equality-constrained linear LS]] of Topic XI, solvable by the [[Def - KKT System|KKT system]] in one step. We then apply the penalty algorithm (designed for general nonlinear problems) and verify its convergence behavior on this benchmark. The exercise drills (a) the linear KKT system as ground truth, (b) the penalty algorithm's inner-subproblem-by-subproblem structure, (c) the rate-of-convergence theorem [[Thm - Convergence of Penalty Algorithm]].

**Assumption pattern.** This is the simplest possible setup: $f, g$ both affine, so the inner penalty subproblems are *linear* LS and solvable in closed form by [[Def - Normal Equations|normal equations]]. The closed-form solvability of the inner subproblem lets us study the *outer-loop* behavior — the only thing the penalty algorithm contributes that linear KKT does not — in isolation.

**Theorem routing.** The route is straightforward: (a) Set up and solve the KKT system once. (b) Write down the penalty objective $\phi_\mu(x) = (x_1 - 1)^2 + (x_2 - 1)^2 + \mu (x_1 + x_2 - 1)^2$, set its gradient to zero, solve the resulting $2 \times 2$ linear system in closed form, giving an explicit formula for $x^{(k+1)}$ as a function of $\mu^{(k)}$. (c) Substitute the iterates into the formula and verify the rate. (d) Reflect on the pedagogical value.

**Key decision point.** The decision is whether to *trust* the closed-form solution of the inner subproblem or instead simulate the inner LM iteration. For this problem the closed-form is exact (no iteration needed at the inner level), and using it isolates the outer-loop convergence theorem. In general nonlinear problems the inner solve is itself iterative, but this exercise drills the *outer* loop in pure form.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra XII — Applied III — Nonlinear Least Squares#Legal Operations|the topic page's Legal Operations]]:

1. **Convert an equality constraint into a quadratic penalty** (operation 7). The constrained problem becomes the penalty objective $\|f(x)\|^2 + \mu \|g(x)\|^2$ with $\mu$ growing.

2. **Warm-start from a related problem's solution** (operation 4). Each outer-loop iteration starts the inner solve from the previous outer iterate $x^{(k)}$, which is close to the new minimum at $\mu^{(k+1)} = 2\mu^{(k)}$. For this linear problem the inner solve is one-step, so warm-starting is trivial; for nonlinear problems it would matter substantially.

---

# Hints

> [!note]- Hint 1
> Set up the KKT system: $A = I$, $b = (1, 1)$, $C = (1, 1)$, $d = 1$. The block matrix is $\begin{pmatrix} 2I & C^T \\ C & 0 \end{pmatrix} = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 1 \\ 1 & 1 & 0 \end{pmatrix}$, with right-hand side $(2, 2, 1)$.

> [!note]- Hint 2
> Solve the KKT system: from the first two equations $2\hat x_1 + \hat z = 2$, $2\hat x_2 + \hat z = 2$, so $\hat x_1 = \hat x_2$. From the constraint $\hat x_1 + \hat x_2 = 1$, $\hat x_1 = \hat x_2 = 1/2$. Substituting, $\hat z = 2 - 2 \cdot 1/2 = 1$. Wait — the Lagrangian convention differs slightly. Boyd's setup has $L = \|f\|^2 + g^T z$, so the gradient is $2 A^T (Ax - b) + C^T z = 0$, giving $2 \hat x_i - 2 + \hat z = 0$, hence $\hat z = 2 - 2 \hat x_i = 2 - 1 = 1$. Comparing to [[Def - Penalty Algorithm]]'s implicit multiplier $z = 2\mu g$: the sign convention is consistent (we'll verify $z \to 1$, not $-1$, in part (b)).

> [!note]- Hint 3
> The penalty objective $\phi_\mu(x) = (x_1 - 1)^2 + (x_2 - 1)^2 + \mu (x_1 + x_2 - 1)^2$. Setting $\partial \phi_\mu/\partial x_1 = 0$ gives $2(x_1 - 1) + 2\mu (x_1 + x_2 - 1) = 0$, i.e., $(1 + \mu) x_1 + \mu x_2 = 1 + \mu$. By symmetry the second equation is $\mu x_1 + (1 + \mu) x_2 = 1 + \mu$.

> [!note]- Hint 4
> Solving this $2 \times 2$ linear system (the unique minimizer at $\mu$): by symmetry $x_1 = x_2 = a$ for some $a$, and $(1 + \mu) a + \mu a = 1 + \mu$, i.e., $(1 + 2\mu) a = 1 + \mu$, so $a = (1 + \mu)/(1 + 2\mu)$. Thus $x^{(k+1)} = ((1 + \mu^{(k)})/(1 + 2\mu^{(k)}), (1 + \mu^{(k)})/(1 + 2\mu^{(k)}))$.

> [!note]- Hint 5
> The implicit multiplier is $z^{(k+1)} = 2\mu^{(k)} (x_1^{(k+1)} + x_2^{(k+1)} - 1) = 2 \mu^{(k)} \cdot (2(1+\mu^{(k)})/(1+2\mu^{(k)}) - 1) = 2\mu^{(k)} \cdot (1/(1+2\mu^{(k)})) = 2\mu^{(k)}/(1+2\mu^{(k)})$. As $\mu \to \infty$, $z \to 1$ — matching $\hat z = 1$.

---

# Solution

The plan is to (i) solve the KKT system once for the ground truth, (ii) derive the explicit penalty-algorithm iterate formula, (iii) tabulate the first few iterates and verify the rate, (iv) reflect on pedagogical value.

**Step 1: Closed-form solution via KKT system.**

The constrained problem $\min \|x - (1, 1)\|^2$ s.t. $x_1 + x_2 = 1$ has the KKT system
$$\begin{pmatrix} 2I & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} \hat x \\ \hat z \end{pmatrix} = \begin{pmatrix} 2b \\ d \end{pmatrix},$$
with $C = (1, 1)$, $b = (1, 1)$, $d = 1$. Solving gives $\hat x = (1/2, 1/2)$ and $\hat z = 1$.

> [!note]- Derivation
> The KKT system in expanded form is
> $$\begin{pmatrix} 2 & 0 & 1 \\ 0 & 2 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} \hat x_1 \\ \hat x_2 \\ \hat z \end{pmatrix} = \begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}.$$
> Row 1: $2 \hat x_1 + \hat z = 2$, so $\hat x_1 = 1 - \hat z/2$.
> Row 2: $2 \hat x_2 + \hat z = 2$, so $\hat x_2 = 1 - \hat z/2$. By symmetry $\hat x_1 = \hat x_2 = a$.
> Row 3: $\hat x_1 + \hat x_2 = 1$, i.e., $2a = 1$, so $a = 1/2$.
> Substituting back: $\hat z = 2 - 2 \cdot 1/2 = 1$.
>
> So the constrained minimum is $\hat x = (1/2, 1/2)$ with Lagrange multiplier $\hat z = 1$.
>
> **Check:** $f(\hat x) = \hat x - (1, 1) = (-1/2, -1/2)$, $\|f(\hat x)\|^2 = 1/2$. The constraint $g(\hat x) = 1/2 + 1/2 - 1 = 0$ ✓.

**Step 2: Closed-form penalty algorithm iterates.**

The penalty objective at $\mu$ is $\phi_\mu(x) = (x_1 - 1)^2 + (x_2 - 1)^2 + \mu (x_1 + x_2 - 1)^2$. Setting its gradient to zero gives
$$x_1^{(k+1)} = x_2^{(k+1)} = \frac{1 + \mu^{(k)}}{1 + 2\mu^{(k)}},$$
and the implicit multiplier is
$$z^{(k+1)} = 2 \mu^{(k)} g(x^{(k+1)}) = \frac{2 \mu^{(k)}}{1 + 2\mu^{(k)}}.$$

> [!note]- Derivation
> Setting $\partial \phi_\mu/\partial x_1 = 0$:
> $$2(x_1 - 1) + 2\mu (x_1 + x_2 - 1) = 0,$$
> rearranging:
> $$(1 + \mu) x_1 + \mu x_2 = 1 + \mu.$$
>
> Similarly from $\partial \phi_\mu/\partial x_2 = 0$:
> $$\mu x_1 + (1 + \mu) x_2 = 1 + \mu.$$
>
> Subtracting the two equations: $((1 + \mu) - \mu)(x_1 - x_2) = 0$, so $x_1 = x_2$. Let $x_1 = x_2 = a$. Substituting into the first equation:
> $$(1 + \mu) a + \mu a = (1 + 2\mu) a = 1 + \mu,$$
> so $a = (1 + \mu)/(1 + 2\mu)$.
>
> The constraint residual is
> $$g(x) = x_1 + x_2 - 1 = 2a - 1 = \frac{2(1 + \mu)}{1 + 2\mu} - 1 = \frac{2 + 2\mu - 1 - 2\mu}{1 + 2\mu} = \frac{1}{1 + 2\mu}.$$
> So $\|g(x^{(k+1)})\| = 1/(1 + 2\mu^{(k)})$ — exactly $O(1/\mu^{(k)})$ as predicted by [[Thm - Convergence of Penalty Algorithm]].
>
> The implicit multiplier is $z^{(k+1)} = 2 \mu^{(k)} g(x^{(k+1)}) = 2\mu^{(k)}/(1 + 2\mu^{(k)})$, which $\to 1$ as $\mu \to \infty$, matching $\hat z = 1$ from Step 1.

**Step 3: Iterate table.**

| $k$ | $\mu^{(k)}$ | $x^{(k+1)} = (a, a)$ with $a = (1 + \mu)/(1 + 2\mu)$ | $g(x^{(k+1)}) = 1/(1 + 2\mu)$ | $z^{(k+1)} = 2\mu/(1 + 2\mu)$ |
| --- | --- | --- | --- | --- |
| 1 | 1 | $(2/3, 2/3) \approx (0.667, 0.667)$ | $1/3 \approx 0.333$ | $2/3 \approx 0.667$ |
| 2 | 2 | $(3/5, 3/5) = (0.6, 0.6)$ | $1/5 = 0.2$ | $4/5 = 0.8$ |
| 3 | 4 | $(5/9, 5/9) \approx (0.556, 0.556)$ | $1/9 \approx 0.111$ | $8/9 \approx 0.889$ |
| 4 | 8 | $(9/17, 9/17) \approx (0.529, 0.529)$ | $1/17 \approx 0.059$ | $16/17 \approx 0.941$ |

As predicted, $\|g\|$ halves roughly each iteration (rate $1/\mu^{(k)}$ with $\mu$ doubling, so $\|g\| = 1/(1 + 2\mu)$ halves each iteration), and $z \to 1 = \hat z$.

> [!note]- Derivation
> Substitute $\mu^{(k)} = 2^{k-1}$ into the closed forms:
>
> - $k=1$: $\mu = 1$. $a = 2/3$, $g = 1/3$, $z = 2/3$.
> - $k=2$: $\mu = 2$. $a = 3/5$, $g = 1/5$, $z = 4/5$.
> - $k=3$: $\mu = 4$. $a = 5/9$, $g = 1/9$, $z = 8/9$.
> - $k=4$: $\mu = 8$. $a = 9/17$, $g = 1/17$, $z = 16/17$.
>
> The constraint residual $g = 1/(1 + 2\mu)$ shrinks as $\mu$ grows; explicitly, $g^{(k+1)}/g^{(k)} = (1 + 2\mu^{(k-1)})/(1 + 2\mu^{(k)}) = (1 + \mu^{(k)})/(1 + 2\mu^{(k)}) \to 1/2$ as $\mu \to \infty$. So $\|g\|$ halves per outer iteration in the asymptotic regime — matching the doubling of $\mu$ and the predicted $\|g\| = O(1/\mu)$ rate.
>
> The iterate $x^{(k+1)} = (a, a)$ approaches $(1/2, 1/2) = \hat x$ from *above* (since $a = (1 + \mu)/(1 + 2\mu) > 1/2$ for all $\mu$): the algorithm visits *infeasible* points that progressively become closer to feasibility. This is the **exterior** character of the penalty method.

**Step 4: Rate verification.**

[[Thm - Convergence of Penalty Algorithm]] predicts $\|g(x^{(k+1)})\| = O(1/\mu^{(k)})$. The explicit formula gives $\|g\| = 1/(1 + 2\mu^{(k)})$, which for large $\mu$ is approximately $1/(2\mu^{(k)})$ — exactly $O(1/\mu^{(k)})$ with constant $1/2$. The rate matches the theorem prediction precisely.

> [!note]- Derivation
> Numerical verification:
> - $\mu = 1$: $1/(1 + 2 \cdot 1) = 1/3 = 0.333$; $1/(2 \cdot 1) = 0.5$. Within factor of 2.
> - $\mu = 8$: $1/(1 + 16) = 1/17 \approx 0.059$; $1/(2 \cdot 8) = 0.0625$. Within factor of 1.07.
> - $\mu = 1000$: $1/2001 \approx 0.0005$; $1/2000 = 0.0005$. Essentially equal.
>
> The leading-order asymptotic $\|g\| \sim 1/(2\mu)$ is the theorem's $O(1/\mu)$ with the explicit constant $1/2$ for this problem (the constant depends on the specific objective curvature and constraint structure).

**Step 5: Pedagogical reflection.**

> [!note]- Derivation
> Despite being a "trivial" linear-LS problem with a one-step KKT-system solution, this problem is a *useful pedagogical baseline* for the penalty algorithm because:
>
> 1. **Closed-form inner solve** — the inner subproblem at each $\mu$ is a 2×2 linear system, exactly solvable. So all error comes from the *outer loop*, isolating the part of the algorithm we're studying.
>
> 2. **Closed-form iterates** — the explicit formula $x^{(k+1)} = (a, a)$ with $a = (1 + \mu)/(1 + 2\mu)$ lets us compute *exact* iterate values for any $\mu$, verifying the $O(1/\mu)$ rate prediction.
>
> 3. **Closed-form ground truth** — the constrained optimum $\hat x = (1/2, 1/2)$ with $\hat z = 1$ is known exactly. The convergence $x^{(k+1)} \to \hat x$ and $z^{(k+1)} \to \hat z$ is verifiable to arbitrary precision.
>
> 4. **Pure outer-loop behavior** — with no inner-loop error, the apparent slow convergence of the penalty method ($\|g\| = 1/(1+2\mu)$) is *entirely* due to the outer loop, not inner-LM convergence issues. This separates the *algorithmic* slowness (which the augmented Lagrangian fixes) from the *numerical* slowness (which is shared between penalty and augmented Lagrangian when the inner LM is the bottleneck).
>
> The problem is therefore an *[[Def - Ideal|ideal]]* unit test for any constrained-NLS solver: given this problem, the solver should compute $x^{(\infty)} = (0.5, 0.5)$ and $z^{(\infty)} = 1$ with predictable convergence rate. Any deviation flags an implementation bug.

> [!note]- Complete formal solution
> **(a)** The KKT system gives $\hat x = (1/2, 1/2)$ and $\hat z = 1$.
>
> **(b)** The penalty algorithm's inner subproblem at $\mu$ has closed-form minimizer $x^{(k+1)} = (a, a)$ where $a = (1 + \mu^{(k)})/(1 + 2\mu^{(k)})$. Computed for $\mu^{(k)} = 1, 2, 4, 8$: $a = 2/3, 3/5, 5/9, 9/17$ respectively. The implicit multiplier is $z^{(k+1)} = 2\mu^{(k)}/(1 + 2\mu^{(k)}) = 2/3, 4/5, 8/9, 16/17$ — converging to $\hat z = 1$.
>
> **(c)** $\|g(x^{(k+1)})\| = 1/(1 + 2\mu^{(k)}) \sim 1/(2\mu^{(k)})$ for large $\mu$, exactly the $O(1/\mu^{(k)})$ rate predicted by [[Thm - Convergence of Penalty Algorithm]].
>
> **(d)** This trivial problem is a useful baseline because (i) the inner subproblem solves in closed form, isolating outer-loop behavior; (ii) the iterates are computable analytically, allowing exact rate verification; (iii) the constrained optimum is known, enabling unit-test-style verification of any constrained-NLS solver implementation. $\blacksquare$

> [!warning] Illegal but tempting alternative route — skip the KKT system and use the closed-form $\hat x$ directly
> A reader might object: "We know $\hat x = (1/2, 1/2)$ from inspection — why bother with the KKT system or the penalty algorithm?" Two reasons. First, the *KKT system* is the standard machinery for linear equality-constrained LS and generalizes to multivariate problems where inspection fails; pedagogically it must be applied here even when overkill. Second, the *penalty algorithm* is being studied for its own sake, as a baseline for nonlinear-equality-constrained problems where no closed form exists; verifying it on a trivial problem builds confidence that the implementation is correct before tackling problems where the answer is unknown.

---

# Key Takeaways

**Trivial benchmarks reveal algorithmic structure.** This exercise's value is *not* in the answer (everyone can see $\hat x = (1/2, 1/2)$ by inspection) but in the *process* — running the penalty algorithm on a fully-explicit problem to observe its iterate sequence, multiplier convergence, and rate of feasibility approach. This kind of unit-test problem is essential when *implementing* a constrained-NLS solver: every component (Jacobian computation, inner solver, multiplier update, penalty growth) can be verified in isolation against the closed-form solution. When a complex production problem misbehaves, the diagnostic move is to apply the *same code* to this trivial benchmark and check that it produces $(1/2, 1/2)$ — any deviation flags an implementation bug rather than a problem-specific subtlety.

**The exterior character of the penalty method is geometrically transparent here.** The penalty iterates $x^{(k+1)} = (a, a)$ with $a = (1 + \mu)/(1 + 2\mu) > 1/2$ approach $\hat x = (1/2, 1/2)$ from *above*, with $g(x^{(k+1)}) = 2a - 1 > 0$ at every iterate — the algorithm visits *infeasible* points throughout, becoming feasible only in the limit. This is the defining feature of *exterior* penalty methods, distinguishing them from *interior* (barrier) methods that stay strictly inside the feasible region. The takeaway: in any application where an iterate's infeasibility matters (e.g., trajectory optimization where a violated dynamics constraint corresponds to a physically impossible state), the penalty method's mid-iteration infeasibility is a structural issue, not a numerical one — it cannot be eliminated by tighter tolerances. For applications where each iterate's physical reasonability matters, choose a method that maintains feasibility (e.g., projected gradient, interior-point) over the penalty method.

**The $O(1/\mu)$ rate from [[Thm - Convergence of Penalty Algorithm]] is exact for this problem.** The convergence-rate theorem is *asymptotic* — it says $\|g\| = O(1/\mu)$ with an unspecified constant. For this problem we have explicitly $\|g\| = 1/(1 + 2\mu)$, exact agreement with the asymptotic $1/(2\mu)$ with constant $1/2$. This is a check on the theorem: not just is the rate right, but the rate is *tight* — no nontrivial improvement is possible for the penalty algorithm with this growth rule. The same problem solved by augmented Lagrangian achieves *exponential* (linear) convergence of $\|g\|$ to zero with $\mu$ kept constant — a strict improvement that this exercise's penalty result lets us appreciate. The trigger to switch from penalty to augmented Lagrangian is the observation that "the penalty method's optimal rate is no better than $O(1/\mu)$, requiring $\mu \to \infty$, requiring ill-conditioned inner solves" — exactly the structural fault that augmented Lagrangian repairs by tracking the multiplier explicitly.
