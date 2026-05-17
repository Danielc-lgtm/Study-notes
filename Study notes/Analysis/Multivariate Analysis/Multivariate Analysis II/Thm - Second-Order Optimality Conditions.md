---
type: theorem
subject: multivariate-analysis
prereqs:
  - "Def - Critical Point, Hessian, and Definiteness"
  - "Thm - First-Order Optimality Condition"
  - "Thm - Taylor's Theorem in Several Variables"
tags: [analysis, multivariate-analysis]
---

# Notation

$U \subseteq \mathbb{R}^n$ is open, $f : U \to \mathbb{R}$ is of class $C^2$ (or $C^3$ where stated), and $x_0 \in U$ is a [[Def - Critical Point, Hessian, and Definiteness|critical point]], $\nabla f(x_0) = 0$. The **Hessian** $Hf(x_0)$ is the symmetric matrix of second partials $\partial_i\partial_j f(x_0)$. A symmetric matrix is **positive definite** if all eigenvalues are positive, **negative definite** if all negative, **indefinite** if of mixed sign, **degenerate** if $0$ is an eigenvalue. We write $h^T Hf(x_0) h$ for the associated quadratic form, $\lambda_{\min}, \lambda_{\max}$ for the extreme eigenvalues, and $o(|h|^2)$ for a remainder with $o(|h|^2)/|h|^2 \to 0$. The full registry is on [[Multivariate Analysis II — Inverse and Implicit Function Theorems]].

---

# Statement

> **Second-order optimality conditions.** Let $U \subseteq \mathbb{R}^n$ be open, $f \in C^2(U)$, and $x_0 \in U$ a critical point of $f$ (so $\nabla f(x_0) = 0$). Let $Hf(x_0)$ be the [[Def - Critical Point, Hessian, and Definiteness|Hessian]] of $f$ at $x_0$.
>
> 1. If $Hf(x_0)$ is **positive definite**, then $f$ has a strict local minimum at $x_0$.
> 2. If $Hf(x_0)$ is **negative definite**, then $f$ has a strict local maximum at $x_0$.
> 3. If $Hf(x_0)$ is **indefinite** (and hence nondegenerate), then $f$ has neither a local maximum nor a local minimum at $x_0$; the point is called a **saddle point**.
>
> If $Hf(x_0)$ is **degenerate**, the test is inconclusive: $f$ may have a strict minimum, a strict maximum, or a saddle, and no statement follows from the Hessian alone.

---

# Motivation

The [[Thm - First-Order Optimality Condition|first-order condition]] produces a list of candidates — the critical points — but it cannot tell a valley bottom from a mountain pass. In one variable the second derivative finishes the job: $f''(x_0) > 0$ is a cup, $f''(x_0) < 0$ a cap. This theorem is the several-variable version, and the question it answers is: *given a critical point, which of the three local pictures is it?*

The reason the answer is subtler than in one variable is the existence of the saddle, a phenomenon with no one-dimensional analogue. At a critical point $f$ may curve upward in some directions and downward in others — a mountain pass curves up across the ridge and down along the trail. A single number cannot record this; you need the curvature in *every* direction, and that is the quadratic form $h \mapsto h^T Hf(x_0) h$. The theorem says this quadratic form, through its definiteness type, *completely* decides the local picture — provided it is nondegenerate.

The value of the theorem is that it reduces a question about the function $f$ to a question of pure linear algebra: compute the Hessian, find the signs of its eigenvalues. The honest limitation, stated as the fourth clause, is the degenerate case: when the quadratic form vanishes in some direction, the second-order Taylor term carries no information there, and the answer escapes to higher order. Knowing precisely *when* the test is silent is as important as knowing what it says.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$x_0$ is a critical point and the Hessian has a definite or indefinite (nondegenerate) sign type". The skill is recognizing the Hessian's sign type without diagonalizing.

The first disguised source is **a $2\times 2$ Hessian with a known determinant and trace.** Property $B$: in two variables, $\det Hf(x_0) = \lambda_1\lambda_2$ and $\operatorname{tr} Hf(x_0) = \lambda_1 + \lambda_2$. The bridge: $\det > 0$ with the top-left entry positive means positive definite; $\det > 0$ with top-left negative means negative definite; $\det < 0$ means indefinite (one eigenvalue of each sign); $\det = 0$ means degenerate. So in two variables the entire classification is one determinant and one sign, no eigenvalue computation. *Example:* classifying critical points of a polynomial in two variables.

The second disguised source is **a diagonally dominant or sign-structured matrix.** Property $B$: a symmetric matrix with positive diagonal and off-diagonal entries small relative to the diagonal (strict diagonal dominance) is positive definite. The bridge is Gershgorin's theorem — every eigenvalue lies within a disc centred at a diagonal entry of radius the off-diagonal row sum, so positive diagonal and dominance keep all eigenvalues positive. *Example:* Hessians arising from sums of nearly-independent quadratic terms.

The third disguised source is **a function known to be convex or strictly convex near $x_0$.** Property $B$: $f$ is convex on a neighbourhood. The bridge: convexity is exactly $Hf \succeq 0$, so a critical point of a strictly convex function has positive definite Hessian and is a minimum. The non-obviousness: a *global* shape hypothesis (convexity) supplies the *local* definiteness this theorem needs, and moreover upgrades the conclusion from local to global minimum. *Example:* least-squares problems, where $f$ is a convex quadratic.

**Targets (Output Amplification)**

The conclusion is "$x_0$ is a strict local minimum / maximum / saddle".

Combine the conclusion with **compactness of the domain.** Property $D$: $f$ is continuous on a compact $K$, so its global extrema exist and are among the critical points (in the interior) and boundary points. The amplified result $E$: once every interior critical point is classified by this theorem, comparing $f$-values across the candidate list *solves* the global optimization problem. This theorem is the filter that turns the candidate list into a classified list ready for comparison.

Combine the conclusion with **convexity of the function.** Property $D$: $f$ is convex on all of $U$. The amplified result $E$: a strict local minimum of a convex function is the *global* minimum, and it is *unique*. The combination is non-obvious because this theorem is purely local — convexity is the extra hypothesis that propagates the local conclusion to a global one, exactly the local-to-global upgrade discussed in the topic's Insights.

Combine the conclusion with **the count of negative eigenvalues (the Morse index).** Property $D$: the Hessian is nondegenerate with exactly $k$ negative eigenvalues. The amplified result $E$: $x_0$ is a saddle of "index $k$", and in suitable coordinates $f$ looks like $f(x_0) - y_1^2 - \dots - y_k^2 + y_{k+1}^2 + \dots + y_n^2$ (the Morse lemma). This refines clause (3) from "not an extremum" to a precise normal form, and it is the entry point to Morse theory.

---

# Why Is It True

Near a critical point the function *is* its Hessian, to leading order. That single sentence is the whole intuition, and it is worth unpacking.

Taylor's theorem expands $f$ around $x_0$ as
$$f(x_0 + h) = f(x_0) + \underbrace{\nabla f(x_0)\cdot h}_{=\,0} + \tfrac12\, h^T Hf(x_0)\, h + o(|h|^2).$$
The first-order term is gone — that is what "critical point" buys. So the increment $f(x_0+h) - f(x_0)$ is the quadratic form $\tfrac12 h^T Hf(x_0) h$ plus an error that is *smaller than quadratic*. The behaviour of $f$ near $x_0$ is therefore the behaviour of the quadratic form, *as long as the quadratic form is itself robustly nonzero* — robust enough to dominate its own error term.

Now, what does a quadratic form do? Diagonalize the symmetric matrix $Hf(x_0)$ in an orthonormal eigenbasis; in eigencoordinates the form is $\sum_i \lambda_i w_i^2$. If every $\lambda_i > 0$, this is a genuine bowl — positive in every direction, with the smallest growth rate $\lambda_{\min}|w|^2$. The bowl grows like $|h|^2$, and the error $o(|h|^2)$ is by definition eventually negligible compared to $|h|^2$, so close enough to $x_0$ the bowl wins and $f$ has a strict minimum. If every $\lambda_i < 0$ it is a dome, by the mirror argument a maximum. If the $\lambda_i$ have mixed sign, then along the eigendirection of a positive eigenvalue $f$ goes up, and along the eigendirection of a negative one $f$ goes down — so $x_0$ beats some neighbours and is beaten by others, a saddle.

The crucial point is the role of *nondegeneracy*. The argument "the quadratic form dominates its error" needs the form to grow at a *definite* rate — $\lambda_{\min}|h|^2$ with $\lambda_{\min} \neq 0$. If $0$ is an eigenvalue, then along that eigendirection the quadratic form is *exactly zero*, the leading-order picture is flat, and the $o(|h|^2)$ error — which could be a third- or fourth-order term of either sign — is now the *dominant* term. The Hessian has handed control to higher order and fallen silent. This is not a defect of the proof; it is the honest truth, witnessed by $x^4 + y^4$, $-x^4-y^4$, $x^4 - y^4$, which share the zero Hessian and exhibit all three behaviours.

So one should expect the theorem because optimization near a critical point is a competition between the quadratic Taylor term and everything smaller; a definite Hessian makes the quadratic term win that competition decisively, and the sign of the win is the sign of the eigenvalues.

---

# What Makes This Hard

The non-obvious step is the quantitative domination: one must produce the spectral bound $h^T Hf(x_0) h \geq \lambda_{\min}|h|^2$ and then argue that for $|h|$ small enough the *quadratic* term $\tfrac{\lambda_{\min}}{2}|h|^2$ strictly exceeds the *cubic-or-smaller* error $o(|h|^2)$ — it is the comparison of growth rates, not the Taylor expansion itself, that does the work. The most common error is to apply the test mechanically when the Hessian is degenerate; the theorem is genuinely silent there, and a second frequent slip is to forget that the bound $h^T H h \geq \lambda_{\min}|h|^2$ requires $H$ symmetric (so that an orthonormal eigenbasis exists), which holds only because $f$ is $C^2$ and Schwarz's theorem applies.

---

# Rederivation Scaffold

**High-level strategy:**
Write the second-order Taylor expansion at the critical point; the linear term vanishes. Bound the quadratic form below (above) by the smallest (largest) eigenvalue times $|h|^2$. For $|h|$ small the quadratic term dominates the $o(|h|^2)$ remainder, fixing the sign of $f(x_0+h) - f(x_0)$.

**Subgoal decomposition:**

1. **Taylor-expand at the critical point.** Show $f(x_0+h) - f(x_0) = \tfrac12 h^T Hf(x_0) h + o(|h|^2)$.
   - *Hint:* Apply [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] to second order and drop the first-order term, which is $\nabla f(x_0)\cdot h = 0$.
   - *Why needed:* It exposes the quadratic form as the leading-order behaviour.

2. **Bound the quadratic form by an eigenvalue.** Show $h^T Hf(x_0) h \geq \lambda_{\min}|h|^2$ when the Hessian is positive definite, with $\lambda_{\min} > 0$.
   - *Hint:* Diagonalize $Hf(x_0) = O^T D O$ with $O$ orthogonal; set $w = Oh$ and use $h^T H h = \sum\lambda_i w_i^2 \geq \lambda_{\min}\sum w_i^2 = \lambda_{\min}|w|^2 = \lambda_{\min}|h|^2$.
   - *Why needed:* It gives a *definite quadratic growth rate* for the form to outrun the error.

3. **Dominate the remainder.** Show that for $|h|$ small, $\tfrac{\lambda_{\min}}{2}|h|^2 > |o(|h|^2)|$, hence $f(x_0+h) > f(x_0)$.
   - *Hint:* By definition of $o(|h|^2)$, the remainder divided by $|h|^2$ tends to $0$, so it is eventually less than $\lambda_{\min}/4$ in absolute value.
   - *Why needed:* It concludes the strict minimum (clause 1); clause 2 is the mirror image, clause 3 tests two opposite directions.

---

# Lemma Decomposition

> [!note]- Lemma 1: A positive definite symmetric matrix obeys a coercivity bound
> **Statement:** If $A$ is symmetric with smallest eigenvalue $\lambda_{\min} > 0$, then $h^T A h \geq \lambda_{\min}|h|^2$ for all $h$.
>
> **Hint:** Diagonalize $A$ by an orthogonal change of basis and read the quadratic form off the eigenvalues.
>
> **Why needed:** It supplies the definite quadratic growth rate that lets the Taylor quadratic term beat the remainder.
>
> > [!note]- Full proof
> > Since $A$ is real symmetric, the spectral theorem gives an orthogonal matrix $O$ with $O^T A O = D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$. For any $h$, set $w = O^T h$; then $|w| = |h|$ because $O$ is orthogonal, and
> > $$h^T A h = h^T O D O^T h = w^T D w = \sum_{i=1}^n \lambda_i w_i^2 \geq \lambda_{\min}\sum_{i=1}^n w_i^2 = \lambda_{\min}|w|^2 = \lambda_{\min}|h|^2.$$
> > The mirror statement, $h^T A h \leq \lambda_{\max}|h|^2$, follows identically. In particular a negative definite matrix satisfies $h^T A h \leq \lambda_{\max}|h|^2$ with $\lambda_{\max} < 0$.

> [!note]- Lemma 2: An indefinite Hessian gives both an ascent and a descent direction
> **Statement:** If $Hf(x_0)$ has a positive eigenvalue with eigenvector $u$ and a negative eigenvalue with eigenvector $v$, then along the line $t \mapsto x_0 + tu$ the function $f$ has a strict local minimum at $t = 0$, and along $t \mapsto x_0 + tv$ a strict local maximum.
>
> **Hint:** Restrict $f$ to each line and apply the one-variable second-derivative test; the second derivative of the restriction is $u^T Hf(x_0) u$.
>
> **Why needed:** It proves clause (3): $x_0$ cannot be a local extremum, since some neighbours are higher and some lower.
>
> > [!note]- Full proof
> > Let $u$ be a unit eigenvector with eigenvalue $\mu > 0$. The restriction $\varphi(t) = f(x_0 + tu)$ has $\varphi'(0) = \nabla f(x_0)\cdot u = 0$ and $\varphi''(0) = u^T Hf(x_0) u = \mu|u|^2 = \mu > 0$. By the one-variable second-derivative test $\varphi$ has a strict local minimum at $0$, so $f(x_0 + tu) > f(x_0)$ for small $t \neq 0$ — there are nearby points where $f$ is strictly larger. Symmetrically, for a unit eigenvector $v$ with eigenvalue $\nu < 0$, the restriction has second derivative $\nu < 0$, a strict local maximum, so $f(x_0 + tv) < f(x_0)$ for small $t \neq 0$ — nearby points where $f$ is strictly smaller. A point with neighbours strictly above and neighbours strictly below is neither a local maximum nor a local minimum.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $x_0$ be a critical point of $f \in C^2(U)$, write $H = Hf(x_0)$.
>
> By [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] to second order, since $\nabla f(x_0) = 0$,
> $$f(x_0 + h) - f(x_0) = \tfrac12\, h^T H h + R(h), \qquad \text{where } \frac{R(h)}{|h|^2} \to 0 \text{ as } h \to 0. \tag{$\ast$}$$
>
> **Clause 1 — $H$ positive definite.** Let $\lambda_{\min} > 0$ be the smallest eigenvalue of $H$. By Lemma 1, $h^T H h \geq \lambda_{\min}|h|^2$. By ($\ast$) there is $\delta > 0$ such that $|R(h)| < \tfrac{\lambda_{\min}}{4}|h|^2$ whenever $0 < |h| < \delta$. Then for such $h$,
> $$f(x_0+h) - f(x_0) = \tfrac12 h^T H h + R(h) \geq \tfrac{\lambda_{\min}}{2}|h|^2 - \tfrac{\lambda_{\min}}{4}|h|^2 = \tfrac{\lambda_{\min}}{4}|h|^2 > 0.$$
> So $f(x_0 + h) > f(x_0)$ for all $h$ with $0 < |h| < \delta$: a strict local minimum.
>
> **Clause 2 — $H$ negative definite.** Apply Clause 1 to $-f$, whose Hessian $-H$ is positive definite. Then $-f$ has a strict local minimum at $x_0$, so $f$ has a strict local maximum.
>
> **Clause 3 — $H$ indefinite.** By Lemma 2 there are directions along which $f$ has a strict local minimum and others along which it has a strict local maximum at $x_0$. Hence every neighbourhood of $x_0$ contains points with $f$ strictly greater than $f(x_0)$ and points with $f$ strictly less. Therefore $x_0$ is neither a local maximum nor a local minimum.
>
> **Degenerate case.** If $0$ is an eigenvalue of $H$, no conclusion follows. The functions $f(x,y) = x^4 + y^4$, $-x^4-y^4$, $x^4-y^4$ all have $Hf(0) = 0$ at the critical point $0$, yet exhibit a strict minimum, a strict maximum, and a saddle respectively — so the Hessian cannot distinguish them. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Stability of mechanical equilibria.** A mechanical system rests at a critical point of its potential energy $V$. This theorem says the equilibrium is *stable* exactly when $HV$ is positive definite (a true energy minimum) and *unstable* when $HV$ is indefinite. The eigenvalues of $HV$ are the squared frequencies of the normal modes of small oscillation. The application is nonobvious because a dynamical question — does the system return when nudged? — is decided by the static definiteness of a Hessian.

**Phase transitions via the Landau free energy.** In statistical physics one expands a free energy $F$ in an order parameter; the equilibrium phase is the minimum of $F$. As a control parameter (temperature) varies, the Hessian of $F$ at the symmetric critical point can pass through *degeneracy* — and that degeneracy is precisely a continuous phase transition. The application battle-tests the degenerate clause: the physics lives exactly where this theorem falls silent.

**Saddle points in min-max problems.** In game theory and optimization, a saddle point of $f(x,y)$ — a minimum in $x$, a maximum in $y$ — is an equilibrium. This theorem's clause (3), refined by the count of negative eigenvalues, characterizes such points. The application is out-of-distribution because the "saddle" is now the *desired* object rather than a degenerate case to avoid.

---

# Bridges

- **[[Thm - First-Order Optimality Condition]]** — the prerequisite. The first-order condition supplies the critical points; this theorem classifies them. Neither is useful alone for a complete optimization.

- **[[Thm - Taylor's Theorem in Several Variables]]** — the engine. The entire proof is the second-order Taylor expansion plus a spectral bound; the Hessian is meaningful as a *test* only because Taylor's theorem identifies it as the leading-order behaviour at a critical point.

- **[[Def - Critical Point, Hessian, and Definiteness]]** — the definiteness classification was set up precisely so that this theorem's three clauses could be stated.

- **The Morse lemma** — the refinement of clause (3). At a nondegenerate critical point, $f$ has, in suitable local coordinates, the exact normal form $f(x_0) \pm y_1^2 \pm \dots \pm y_n^2$, with the number of minus signs the Morse index. This upgrades "saddle" to a precise picture and is the foundation of Morse theory.

---

# Unlocked by This

> [!tip] Morse Theory *(from Differential Topology)*
> A function whose critical points are all nondegenerate is a **Morse function**. The Morse index — the number of negative Hessian eigenvalues — at each critical point determines the topology of the underlying manifold through the **Morse inequalities**. This theorem's nondegenerate classification is the local data Morse theory globalizes.

> [!tip] Second-Order Conditions in Optimization *(from Convex and Nonlinear Optimization)*
> The positive-definite Hessian is the **second-order sufficient condition** for a local minimum, and its semidefinite version is the second-order *necessary* condition. With constraints, the Hessian is replaced by the Hessian of the [[Thm - The Method of Lagrange Multipliers|Lagrangian]] restricted to the tangent space of the constraint set — the bordered-Hessian test.
