---
type: exercise
subject: topology
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Convex Body"
  - "Thm - Compact Convex Body is Homeomorphic to a Disk"
  - "Def - Continuous Map"
tags: [analysis, topology, fixed-point, brouwer]
---

# Problem Statement

**The Brouwer fixed-point theorem.** Every continuous map $f : D^n \to D^n$ has a fixed point — i.e., there exists $x_0 \in D^n$ with $f(x_0) = x_0$.

By [[Thm - Compact Convex Body is Homeomorphic to a Disk]], the same conclusion holds for every continuous self-map of any compact convex body in $\mathbb{R}^n$.

(a) **Prove the case $n = 1$** using only the **intermediate value theorem**.

(b) **Outline the case $n = 2$** using the no-retraction argument: assume $f$ has no fixed point and use this to construct a retraction $D^2 \to S^1$, which is impossible because $S^1$ is not a retract of $D^2$.

(c) **State (without proof) the general case** and note its standard proofs.

**Recall:**

A [[Def - Continuous Map|continuous map]] $f : X \to X$ has a *fixed point* if $f(x_0) = x_0$ for some $x_0 \in X$. A *retraction* $r : X \to A$ is a continuous map fixing $A$ pointwise. $S^{n-1}$ is the boundary of $D^n$.

---

# Convergent Strategy

**Problem class:** Existence proof via a topological obstruction.

**Assumption pattern:** $D^n$ is compact and convex; $f$ is continuous; we want to show there *must* be a fixed point.

**Theorem routing:**
- $n = 1$: direct application of **IVT** to $g(x) = f(x) - x$.
- $n = 2$: assume no fixed point, define a retraction $D^2 \to S^1$ using the "fixed-point–to-boundary projection", derive a contradiction with the (deep) fact that $S^1$ is not a retract of $D^2$ (equivalent to $\pi_1(S^1) = \mathbb{Z} \neq 0$).
- General $n$: same no-retraction argument with $\pi_{n-1}(S^{n-1}) = \mathbb{Z}$, or simplicial approximation, or degree theory.

**Key decision point:** The no-retraction reduction. If $f$ has no fixed point, then for each $x \in D^n$, the ray from $f(x)$ through $x$ continues to a unique boundary point $r(x) \in S^{n-1}$. This $r$ is a retraction: continuous (geometric) and $r|_{S^{n-1}} = 1_{S^{n-1}}$. The existence of such $r$ is the contradiction.

---

# Legal Operations Used

1. **IVT for the 1D case.** A continuous function changing sign on $[a, b]$ has a zero.

2. **Construct a retraction from a fixed-point-free self-map.** If $f$ has no fixed point, define $r(x)$ = the unique exit point of the ray from $f(x)$ through $x$.

3. **Use the obstruction "$S^{n-1}$ is not a retract of $D^n$".** A topological fact (proved via $\pi_{n-1}$ or homology).

---

# Hints

> [!note]- Hint 1
> $n = 1$: $f : [-1, 1] \to [-1, 1]$. Consider $g(x) = f(x) - x$. $g(-1) \geq 0$ (since $f(-1) \geq -1$) and $g(1) \leq 0$ (since $f(1) \leq 1$). IVT gives a zero.

> [!note]- Hint 2
> $n \geq 2$: assume $f(x) \neq x$ for all $x$. For each $x \in D^n$, draw the ray from $f(x)$ through $x$ (well-defined direction since $x \neq f(x)$). This ray exits $D^n$ at a unique boundary point — call this point $r(x)$.

> [!note]- Hint 3
> $r$ is continuous: small perturbations of $x$ (and hence small perturbations of $f(x)$) give small changes in the ray direction and hence in the exit point.

> [!note]- Hint 4
> $r|_{S^{n-1}} = 1_{S^{n-1}}$: if $x \in S^{n-1}$, the ray from $f(x)$ through $x$ exits the disk at $x$ itself (assuming $f(x)$ is interior or differently placed — but in fact $x \in \partial D^n$ means $x$ is the exit point of the ray *from* $f(x)$ *toward* $x$).

> [!note]- Hint 5
> So $r$ is a retraction $D^n \to S^{n-1}$. But $S^{n-1}$ is *not* a retract of $D^n$ — this is the topological obstruction. Conclude: $f$ must have a fixed point.

---

# Solution

**Part (a): The case $n = 1$ via IVT.**

Let $f : [-1, 1] \to [-1, 1]$ be continuous. Define $g : [-1, 1] \to \mathbb{R}$, $g(x) := f(x) - x$. $g$ is continuous.

$g(-1) = f(-1) - (-1) = f(-1) + 1$. Since $f(-1) \in [-1, 1]$, $f(-1) + 1 \in [0, 2]$, so $g(-1) \geq 0$.

$g(1) = f(1) - 1$. Since $f(1) \in [-1, 1]$, $f(1) - 1 \in [-2, 0]$, so $g(1) \leq 0$.

By the Intermediate Value Theorem (continuous $g$ on connected $[-1, 1]$, $g(-1) \geq 0 \geq g(1)$): there exists $x_0 \in [-1, 1]$ with $g(x_0) = 0$, i.e., $f(x_0) = x_0$. Fixed point.

**Part (b): The case $n = 2$ via no-retraction.**

Assume, for contradiction, that $f : D^2 \to D^2$ is continuous with no fixed point: $f(x) \neq x$ for all $x \in D^2$.

> [!note]- Derivation — construction of retraction
> For each $x \in D^2$, the points $x$ and $f(x)$ are distinct. The directed line segment from $f(x)$ to $x$ has a well-defined direction vector, $x - f(x)$, which is nonzero.
>
> Extend this segment past $x$ as a ray: $\rho(x; t) := x + t(x - f(x))$ for $t \geq 0$. At $t = 0$, $\rho(x; 0) = x$. As $t$ increases, the ray moves out from $x$ in the direction away from $f(x)$.
>
> Since $D^2$ is bounded, the ray $\{\rho(x; t) : t \geq 0\}$ exits $D^2$ at a unique value $t = t(x) \geq 0$, with $\rho(x; t(x)) \in S^1$. Call this exit point $r(x) := \rho(x; t(x))$.
>
> *Continuity of $r$:* the exit point depends continuously on $x$ and $f(x)$ (and hence on $x$, since $f$ is continuous). Specifically, $t(x)$ is the unique solution of $\|x + t(x - f(x))\|^2 = 1$ in $[0, \infty)$, which is a continuous quadratic equation in $t$, with continuously-varying coefficients. So $t(x)$ is continuous in $x$ (and we choose the positive root), and $r(x) = x + t(x)(x - f(x))$ is continuous.
>
> *$r|_{S^1} = 1_{S^1}$:* if $x \in S^1$, then $x \in \partial D^2$, so $t = 0$ already gives an exit point (the ray starts at $x \in S^1$). So $r(x) = x$.

> [!note]- Derivation — contradiction
> $r : D^2 \to S^1$ is a continuous map with $r|_{S^1} = 1_{S^1}$. So $r$ is a retraction of $D^2$ onto $S^1$.
>
> But $S^1$ is *not* a retract of $D^2$. This is a deep topological fact, equivalent to:
> - $\pi_1(S^1) = \mathbb{Z} \neq 0 = \pi_1(D^2)$;
> - $H_1(S^1) = \mathbb{Z} \neq 0 = H_1(D^2)$;
> - the inclusion $i : S^1 \hookrightarrow D^2$ induces a zero map on $\pi_1$ (since $D^2$ is contractible), so cannot have a left inverse;
> - degree theory: a retraction would give $\deg(1_{S^1}) = \deg(r \circ i) = 0$, contradiction.
>
> So there is no retraction $D^2 \to S^1$. Contradiction. Hence the original assumption "$f$ has no fixed point" was wrong. $f$ must have a fixed point.

**Part (c): The general case.**

For $n \geq 2$, the same no-retraction argument works: assume $f : D^n \to D^n$ has no fixed point; construct the retraction $r : D^n \to S^{n-1}$ via the ray from $f(x)$ through $x$ to the boundary; derive contradiction from "$S^{n-1}$ is not a retract of $D^n$".

The general fact "$S^{n-1}$ is not a retract of $D^n$" can be proved using:

1. **Higher homotopy groups:** $\pi_{n-1}(S^{n-1}) = \mathbb{Z}$, while $\pi_{n-1}(D^n) = 0$ (since $D^n$ is contractible).
2. **Singular homology:** $H_{n-1}(S^{n-1}; \mathbb{Z}) = \mathbb{Z}$, $H_{n-1}(D^n; \mathbb{Z}) = 0$. A retraction would give a left inverse to the inclusion-induced map $H_{n-1}(S^{n-1}) \to H_{n-1}(D^n) = 0$, impossible.
3. **Sperner's lemma + simplicial subdivision:** an elementary combinatorial argument due to Knaster, Kuratowski, Mazurkiewicz, avoiding algebraic topology.
4. **Smooth approximation + Sard's theorem:** approximate $f$ by smooth maps, use that smooth retractions also fail (a degree-theoretic argument).

> [!note]- Complete formal solution (part (a) + outline)
> *(a)* $g(x) = f(x) - x$ has $g(-1) \geq 0$ and $g(1) \leq 0$. By IVT, $g(x_0) = 0$ for some $x_0$, giving $f(x_0) = x_0$.
>
> *(b)* Assume $f$ has no fixed point. Define $r : D^2 \to S^1$ by extending the ray from $f(x)$ through $x$ to the boundary. $r$ is continuous and $r|_{S^1} = 1_{S^1}$, so $r$ is a retraction. But $S^1$ is not a retract of $D^2$ (since $\pi_1(S^1) = \mathbb{Z} \neq 0 = \pi_1(D^2)$ — a retraction would give a left inverse to $\pi_1(S^1) \to \pi_1(D^2)$, impossible). Contradiction. So $f$ has a fixed point. $\blacksquare$

---

# Key Takeaways

**The no-retraction argument is the canonical proof technique.** The pattern is: "want to show every $f$ has a fixed point on $D^n$ $\Rightarrow$ suppose not, construct a retraction $D^n \to S^{n-1}$, derive contradiction with topology of spheres". This same pattern proves many fixed-point theorems (Schauder, Tychonoff in TVSs, Lefschetz).

**The depth is in the no-retraction fact, not the Brouwer theorem.** The Brouwer theorem itself is a *consequence* of the algebraic-topological fact "$S^{n-1}$ is not a retract of $D^n$". This fact requires nontrivial algebraic topology: a continuous map from $D^n$ to $S^{n-1}$ restricting to the identity on $S^{n-1}$ would induce the identity on $\pi_{n-1}$ via $S^{n-1} \to D^n \to S^{n-1}$, but factors through $\pi_{n-1}(D^n) = 0$. The contradiction is purely algebraic.

**Brouwer extends to convex bodies.** By [[Thm - Compact Convex Body is Homeomorphic to a Disk]], every continuous self-map of a compact convex body in $\mathbb{R}^n$ has a fixed point. Same proof transports via the homeomorphism with $D^n$. This is the form most useful in applications: economic equilibrium theorems, game-theoretic results, Nash equilibrium existence, all use Brouwer on convex bodies.

**Infinite-dimensional analogue: Schauder.** The infinite-dimensional analogue is the Schauder fixed-point theorem: every continuous self-map of a compact convex subset of a Banach space has a fixed point. This is used to prove existence of solutions to nonlinear PDEs (e.g., Leray-Schauder degree theory).

**Caveats.** Brouwer requires *compactness* and *convexity* of the domain. Without compactness: the translation $x \mapsto x + 1$ on $\mathbb{R}$ has no fixed point. Without convexity: the rotation by $\pi$ on $S^1$ has no fixed point. The two assumptions are essential and minimal.
