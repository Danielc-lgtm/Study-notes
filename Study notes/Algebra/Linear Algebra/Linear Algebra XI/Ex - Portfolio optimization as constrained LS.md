---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Constrained Least Squares"
  - "Def - KKT System"
  - "Thm - Constrained Least Squares via KKT System"
tags: [algebra, linear-algebra, applied, finance, portfolio-optimization]
---

# Problem Statement

You are given a $T \times n$ matrix $R$ whose entries $R_{tj}$ are the (realized) return of asset $j$ in period $t$, for $T$ periods and $n$ assets. You want to choose an *allocation vector* $w \in \mathbb{R}^n$ — with $w_j$ being the fraction of total portfolio value invested in asset $j$ — to achieve high portfolio return with low risk.

Specifically, define:
- *Portfolio return* in period $t$: $r_t = \sum_j R_{tj} w_j = (R w)_t$.
- *Mean portfolio return*: $\mathrm{avg}(r) = (1/T) \mathbf{1}^T R w = \mu^T w$, where $\mu = R^T \mathbf{1}/T$ is the vector of mean asset returns.
- *Risk* (standard deviation of portfolio return): $\mathrm{std}(r) = \|r - \mathrm{avg}(r) \mathbf{1}\|/\sqrt{T}$.

The *Markowitz portfolio optimization problem* fixes a target mean return $\rho$ and minimizes risk subject to two constraints: the *budget constraint* $\mathbf{1}^T w = 1$ (weights sum to 1) and the *target-return constraint* $\mu^T w = \rho$ (achieve mean return $\rho$).

1. Show this is a constrained LS problem.
2. Write down the KKT system.
3. Show that the solution $\hat{w}(\rho)$ is an affine function of $\rho$, deriving the *two-fund theorem*: every Pareto-optimal portfolio is an affine combination of any two other Pareto-optimal portfolios.

**Recall:**

A [[Def - Constrained Least Squares|constrained LS problem]] is $\min \|Ax - b\|^2$ s.t. $Cx = d$, with KKT system from [[Def - KKT System]]:
$$\begin{pmatrix} 2 A^T A & C^T \\ C & 0 \end{pmatrix} \begin{pmatrix} x \\ \nu \end{pmatrix} = \begin{pmatrix} 2 A^T b \\ d \end{pmatrix}.$$
The constrained LS solution is linear in the data $(b, d)$ — see [[Thm - Constrained Least Squares via KKT System]].

---

# Convergent Strategy

**Problem class:** This is a *constrained quadratic optimization* problem in finance. The class is "minimize a quadratic risk function (variance) subject to linear constraints (budget, target return)." This reduces to constrained LS via the identification of "minimize realized variance" with "minimize $\|Rw - \rho \mathbf{1}\|^2$" (the squared norm of deviations from the target return).

**Assumption pattern:** Given the realized return matrix $R$, the mean return vector $\mu$, a target return $\rho$. The implicit assumption — and a deep one — is that "future returns are similar to past returns" (Boyd assumption (17.4)). Without this assumption, the optimization is meaningless: we cannot optimize for unknown future returns. With the assumption, the problem becomes a backward-looking constrained LS.

**Theorem routing:** Identify the LS objective as $\|R w - \rho \mathbf{1}\|^2$ (the sum of squared deviations of realized returns from the target $\rho$, equal to $T$ times the realized variance — the constant factor doesn't change the minimizer). The constraint matrix is $C = \binom{\mathbf{1}^T}{\mu^T}$ with right-hand side $d = \binom{1}{\rho}$. Apply [[Thm - Constrained Least Squares via KKT System]] to write down the KKT system. Verify existence-uniqueness: rows of $C$ are independent iff $\mu \neq c \mathbf{1}$ for any scalar $c$ (i.e., not all assets have the same mean return), which is the typical case; the joint column-rank condition is also generic. Solve the KKT system to get $\hat{w}(\rho)$ as a function of $\rho$, and derive the two-fund theorem from the linearity in $\rho$.

**Key decision point:** The non-obvious step is recognizing that the *realized variance* $\mathrm{std}(r)^2 = (1/T)\|r - \mathrm{avg}(r) \mathbf{1}\|^2$ can be replaced by $(1/T) \|Rw - \rho \mathbf{1}\|^2$ when the target-return constraint $\mu^T w = \rho$ holds — the two are equal under the constraint. This identification is what turns the variance-minimization problem into a (squared-error) LS problem, making the constrained-LS machinery applicable.

---

# Legal Operations Used

1. **Build the KKT system for an equality-constrained problem.** (Operation 5 from the topic page.) Form the constrained-LS problem $\min \|Rw - \rho \mathbf{1}\|^2$ s.t. $\mathbf{1}^T w = 1, \mu^T w = \rho$. Apply the KKT framework with $A = R, b = \rho \mathbf{1}, C = \binom{\mathbf{1}^T}{\mu^T}, d = \binom{1}{\rho}$. The KKT matrix is $(n + 2) \times (n + 2)$.

2. **Recognize linearity in the data $(b, d)$.** (Targeted use of [[Thm - Constrained Least Squares via KKT System]] point 5.) The KKT solution is a linear function of $(b, d)$, hence of $\rho$. This linearity is what gives the two-fund theorem.

3. **Sweep $\rho$ to trace the efficient frontier.** Solve the KKT system for many $\rho$ values; the resulting $(\mathrm{std}(r), \mu^T w)$ points trace the Pareto-optimal curve in risk-return space.

---

# Hints

> [!note]- Hint 1
> Note that the realized variance under the constraint $\mu^T w = \rho$ is
> $$\mathrm{std}(r)^2 = (1/T) \sum_t (r_t - \mathrm{avg}(r))^2 = (1/T) \sum_t (r_t - \rho)^2 = (1/T) \|Rw - \rho \mathbf{1}\|^2.$$
> So minimizing variance (under the constraint) is the same as minimizing $\|Rw - \rho \mathbf{1}\|^2$.

> [!note]- Hint 2
> The constraint $\mathbf{1}^T w = 1$ (budget) and $\mu^T w = \rho$ (target return) can be stacked: $C w = d$ with $C = \binom{\mathbf{1}^T}{\mu^T}$ and $d = \binom{1}{\rho}$.

> [!note]- Hint 3
> The KKT system has $n + 2$ equations (in $n$ portfolio weights + 2 Lagrange multipliers).

> [!note]- Hint 4 (for two-fund theorem)
> Since the KKT solution is linear in $d = \binom{1}{\rho}$, and only $\rho$ changes (the budget constraint $\binom{1}{0}$ part is fixed), the solution decomposes as $\hat{w}(\rho) = w_0 + \rho v$ for fixed vectors $w_0, v$ that can be computed by solving the KKT system at $\rho = 0$ and $\rho = 1$.

---

# Solution

The proof has three steps. Step 1 sets up the LS objective and identifies the constraint structure. Step 2 writes down the KKT system explicitly. Step 3 exploits the linearity of the solution in $\rho$ to derive the two-fund theorem.

**Step 1: Set up the constrained LS problem.**

Under the constraint $\mu^T w = \rho$, the realized portfolio mean is $\mathrm{avg}(r) = \mu^T w = \rho$. The realized variance is
$$\mathrm{std}(r)^2 = (1/T)\|r - \rho \mathbf{1}\|^2 = (1/T)\|Rw - \rho \mathbf{1}\|^2.$$
Minimizing $\mathrm{std}(r)^2$ over $w$ subject to the constraints is the constrained LS problem
$$\min_w \|Rw - \rho \mathbf{1}\|^2 \quad \text{subject to} \quad \mathbf{1}^T w = 1, \quad \mu^T w = \rho.$$
(The factor of $1/T$ doesn't change the minimizer.)

> [!note]- Derivation
> The portfolio return time series is $r = Rw$, an $n$-vector. Its mean is $\mu^T w$ and its variance is $\mathrm{std}(r)^2 = (1/T)(r - \mu^T w \mathbf{1})^T (r - \mu^T w \mathbf{1}) = (1/T)\|r - \mu^T w \mathbf{1}\|^2$. Under the constraint $\mu^T w = \rho$, this becomes $(1/T) \|r - \rho \mathbf{1}\|^2 = (1/T) \|Rw - \rho \mathbf{1}\|^2$.

**Step 2: Write down the KKT system.**

Apply [[Thm - Constrained Least Squares via KKT System]] with $A = R, b = \rho \mathbf{1}, C = \binom{\mathbf{1}^T}{\mu^T}, d = \binom{1}{\rho}$. The KKT system is

> [!note]- Derivation
> $A^T A = R^T R$, $A^T b = \rho R^T \mathbf{1} = \rho T \mu$ (since $\mu = R^T \mathbf{1}/T$). The KKT system:
> $$\begin{pmatrix} 2 R^T R & \mathbf{1} & \mu \\ \mathbf{1}^T & 0 & 0 \\ \mu^T & 0 & 0 \end{pmatrix} \begin{pmatrix} w \\ z_1 \\ z_2 \end{pmatrix} = \begin{pmatrix} 2 \rho T \mu \\ 1 \\ \rho \end{pmatrix}.$$
> Here $z_1$ is the Lagrange multiplier for the budget constraint, $z_2$ for the target-return constraint. The matrix is $(n + 2) \times (n + 2)$, symmetric, indefinite (saddle-point structure). Under the conditions of [[Thm - Constrained Least Squares via KKT System]] — rows of $C$ independent (i.e., $\mu \neq c\mathbf{1}$) and columns of $\binom{A}{C}$ independent — the KKT matrix is invertible and the solution is unique.

**Step 3: Two-fund theorem from linearity in $\rho$.**

The KKT system right-hand side is $\binom{2 \rho T \mu, 1, \rho}^T$, which is *affine* in $\rho$:
$$\binom{2 \rho T \mu, 1, \rho}^T = \binom{0, 1, 0}^T + \rho \binom{2 T \mu, 0, 1}^T.$$
Since the KKT matrix is fixed (doesn't depend on $\rho$) and the right-hand side is affine in $\rho$, the solution $(w, z_1, z_2)$ is also affine in $\rho$:
$$\binom{w}{z_1, z_2}(\rho) = \binom{w_0}{z_{1,0}, z_{2,0}} + \rho \binom{v}{v_1, v_2}.$$
Extracting the $w$ part: $\hat{w}(\rho) = w_0 + \rho v$ for fixed vectors $w_0, v$. These can be computed by solving the KKT system at two specific $\rho$ values (e.g., $\rho = 0$ and $\rho = 1$) and taking the affine combination.

> [!note]- Derivation
> Specifically, $w_0$ is the first $n$ components of the KKT solution at $\rho = 0$ (giving the minimum-risk portfolio with mean return 0); $v$ is the first $n$ components of the directional derivative of the KKT solution with respect to $\rho$, computable as the difference between the KKT solutions at $\rho = 1$ and $\rho = 0$.
>
> The *two-fund theorem* follows: every Pareto-optimal portfolio $\hat{w}(\rho)$ is an affine combination of any two other Pareto-optimal portfolios $\hat{w}(\rho_1), \hat{w}(\rho_2)$ (with $\rho_1 \neq \rho_2$):
> $$\hat{w}(\rho) = \frac{\rho - \rho_2}{\rho_1 - \rho_2} \hat{w}(\rho_1) + \frac{\rho - \rho_1}{\rho_2 - \rho_1} \hat{w}(\rho_2).$$
> This is the classical statement: any investor's efficient portfolio is a linear combination of two "funds" — specifically, in the version with a risk-free asset, one fund is the risk-free asset and the other is the *market portfolio* (the unique risky-asset Pareto-optimal portfolio).

> [!note]- Complete formal solution
> *Step 1:* Recognize the variance-minimization problem as a constrained LS problem with $A = R, b = \rho \mathbf{1}, C = \binom{\mathbf{1}^T}{\mu^T}, d = \binom{1}{\rho}$, using the identity $(1/T) \|Rw - \rho \mathbf{1}\|^2 = \mathrm{std}(r)^2$ under the target-return constraint.
>
> *Step 2:* Apply [[Thm - Constrained Least Squares via KKT System]] to write the KKT system as above. Verify existence-uniqueness by checking that rows of $C$ are linearly independent (iff $\mu \neq c\mathbf{1}$ — generic) and that columns of $\binom{R}{C}$ are independent (generic for $n$ assets observed over $T$ periods).
>
> *Step 3:* The KKT right-hand side is affine in $\rho$:
> $$\binom{2 \rho T \mu, 1, \rho}^T = \binom{0, 1, 0}^T + \rho \binom{2 T \mu, 0, 1}^T.$$
> Since the KKT matrix doesn't depend on $\rho$, the solution $\hat{w}(\rho), (\hat{z}_1(\rho), \hat{z}_2(\rho))$ is affine in $\rho$:
> $$\hat{w}(\rho) = w_0 + \rho v,$$
> for fixed vectors $w_0, v$ obtained from the KKT solution at any two $\rho$ values. Hence every Pareto-optimal portfolio is an affine combination of any two: the two-fund theorem. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to solve the portfolio problem by *Lagrangian relaxation*: convert the constraints to soft penalties $\mu^T w \approx \rho$ and $\mathbf{1}^T w \approx 1$, then solve a multi-objective LS problem. This *approximately* satisfies the constraints but not *exactly* — for any finite penalty weight, the realized portfolio has $\mathbf{1}^T w \neq 1$ in general (e.g., off by a fraction of a percent). For real portfolios this is sometimes acceptable (we re-balance approximately), but for theoretical analysis we want the constraints exactly satisfied. The KKT-based exact approach is the right one. **Becomes legal when:** you intentionally use soft constraints to model real-world trading frictions (e.g., transaction costs as approximate penalties), or in the limit of large penalty weights converging to the constrained solution.

---

# Key Takeaways

**Variance-minimization with linear constraints is constrained LS in disguise.**

The Markowitz problem is the *paradigmatic* application of constrained LS to finance, and it works because the *realized variance* under a target-return constraint can be rewritten as a squared norm of the form $\|Rw - \rho \mathbf{1}\|^2$. The constraints (budget, target return) are linear in $w$, fitting the constrained-LS framework exactly. This identification generalizes: any *variance minimization with linear constraints* problem is constrained LS. The trigger for using this framework: "minimize the standard deviation of some linear combination of variables, subject to linear constraints on the combination weights."

**The two-fund theorem is a structural consequence of KKT linearity.**

The two-fund theorem — every Pareto-optimal portfolio is an affine combination of any two Pareto-optimal portfolios — is *not* a coincidence; it follows directly from the *linearity of the KKT solution in the right-hand side $\rho$*. This in turn follows from the constraint structure: there is *one* parameter ($\rho$) that varies, and the KKT matrix is fixed, so the solution traces a *line* in parameter space. This pattern transfers to other constrained-LS problems where one parameter is swept: the solution traces a line, and any two points on the line determine the whole line. In LQR, sweeping the cost-tradeoff parameter $\rho$ gives an analogous *two-policy theorem*; in tomographic reconstruction, sweeping the smoothness parameter gives an analogous *two-reconstruction theorem*.

**The KKT multipliers have financial interpretation as shadow prices.**

The Lagrange multipliers $z_1, z_2$ from the budget and target-return constraints have direct financial meaning. $z_1$ is the *shadow price of the budget constraint* — the marginal value of an additional dollar in the budget, measured in units of risk-squared. $z_2$ is the *shadow price of the target-return constraint* — the marginal cost in risk-squared of requiring an extra unit of return. These shadow prices are diagnostic: $z_2$ large means "achieving more return is costly in risk"; $z_1$ tells you what one more dollar buys you. In real portfolio management, monitoring these multipliers across the efficient frontier informs decisions about whether to relax constraints.

This exercise is the entry point to a vast literature on quantitative finance, including CAPM (Capital Asset Pricing Model — adds a risk-free asset to derive the *market portfolio*), factor models (extending Markowitz with multiple risk factors), and modern portfolio theory in the presence of transaction costs and constraints. The next exercises in §XI.4 — [[Ex - Linear quadratic control via constrained LS]] and [[Ex - Kalman state estimation as constrained LS]] — show that the same KKT structure underlies LQR control and Kalman filtering, three "different" applications united by one mathematical framework.
