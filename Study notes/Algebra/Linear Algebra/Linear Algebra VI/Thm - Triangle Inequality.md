---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Norm Induced by an Inner Product"
  - "Thm - Cauchy-Schwarz Inequality"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. $\|v\| = \sqrt{\langle v, v\rangle}$ is the inner-product norm. The notation registry is on the parent topic page [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Triangle Inequality).** For any vectors $u, v$ in an inner product space,
> $$\|u + v\| \leq \|u\| + \|v\|.$$
> Equality holds if and only if one of $u, v$ is a non-negative real multiple of the other.

> **Corollary (Reverse Triangle Inequality).** For any $u, v$ in an inner product space,
> $$\bigl|\|u\| - \|v\|\bigr| \leq \|u - v\|.$$

The triangle inequality is the geometric fact that the length of one side of a triangle does not exceed the sum of the other two sides. The reverse triangle inequality is the dual statement that the difference of lengths is bounded by the length of the difference.

---

# Motivation

The triangle inequality is what turns the inner-product norm into a *norm* in the abstract sense. A function on a vector space taking values in $[0, \infty)$ with the four properties — non-negativity, definiteness, absolute homogeneity, and the triangle inequality — is, by definition, a norm. The first three are immediate from the inner-product axioms; the triangle inequality is the only one that requires real work, and it is the one whose proof requires [[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz]].

This matters because the triangle inequality is what makes the distance function $d(u, v) = \|u - v\|$ a *metric* (specifically, it implies $d(u, w) \leq d(u, v) + d(v, w)$). Without the triangle inequality, $V$ is not a metric space, and the entire apparatus of convergence, continuity, completeness, and compactness is unavailable. The triangle inequality is the gateway from algebra to analysis on $V$.

Geometrically, the triangle inequality says: if you walk from the origin to $u$, then from $u$ to $u + v$, you have walked at least as far as walking directly from the origin to $u + v$. The shortest path between two points is the straight line. This is the most basic of geometric statements about Euclidean space, and the fact that it survives in any inner product space is the precise sense in which "inner product spaces inherit Euclidean geometry".

The role of Cauchy-Schwarz in the proof is exactly to bound the **cross-term** $\langle u, v\rangle$ in the expansion $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$. Without that bound, the expansion would be uncontrolled — the cross-term could in principle be as positive as $\|u\|\,\|v\|$ but no more, and Cauchy-Schwarz gives exactly that maximum. The triangle inequality is, in this sense, Cauchy-Schwarz "exponentiated to the norm level".

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: any two vectors in an inner product space. The skill is recognising disguised triangle-inequality-form inequalities.

The first source is **a question about bounding the norm of a sum**. Property $B$: "show $\|u + v\| \leq C$" for some constant $C$. Bridge: write $C = \|u\| + \|v\|$ when the right-hand side is the natural bound, and triangle inequality applies. The non-obvious part is recognising when "sum of norms" is the right $C$ — often the problem asks for $C$ explicitly and the route via triangle inequality is mechanical.

The second source is **bounding a difference of norms**. Property $B$: "show $|\,\|u\| - \|v\|\,| \leq C$". Bridge: this is the reverse triangle inequality $|\,\|u\| - \|v\|\,| \leq \|u - v\|$, which follows from the forward triangle inequality applied to $u = (u - v) + v$ (giving $\|u\| \leq \|u - v\| + \|v\|$, hence $\|u\| - \|v\| \leq \|u - v\|$, and symmetrically).

The third source is **a sum or path inequality in optimization/geometry**. Property $B$: "show that the total length of a piecewise-linear path is at least the length of the direct connection". Bridge: triangle inequality applied iteratively gives $\|v_1 + v_2 + \dots + v_n\| \leq \|v_1\| + \|v_2\| + \dots + \|v_n\|$ (the $n$-fold triangle inequality), which is the bound on path length. This is the source behind shortest-path arguments in computational geometry and optimization.

The fourth source is **convergence of a series**. Property $B$: "show $\sum_k v_k$ converges in norm" in a Hilbert space (or more generally, in a Banach space). Bridge: if $\sum_k \|v_k\| < \infty$ (absolute convergence), the triangle inequality gives $\|\sum_{k=m}^n v_k\| \leq \sum_{k=m}^n \|v_k\| \to 0$ as $m \to \infty$, so the partial sums form a Cauchy sequence and (in a Hilbert space) converge. This is the source behind every convergence-by-absolute-convergence argument.

**Targets (Output Amplification)**

The conclusion is $\|u + v\| \leq \|u\| + \|v\|$. Combined with other structure:

The first target is **the metric-space distance** $d(u, v) = \|u - v\|$. Property $D$: write $d(u, w) = \|u - w\| = \|(u - v) + (v - w)\|$. Combination: triangle inequality on $u - v$ and $v - w$ gives $d(u, w) \leq d(u, v) + d(v, w)$ — the metric-space triangle inequality. This is the entire content of "the inner-product norm induces a metric".

The second target is the **continuity of the norm and inner product**. Property $D$: the reverse triangle inequality $|\,\|u\| - \|v\|\,| \leq \|u - v\|$ says the norm function is $1$-Lipschitz. Combination: $1$-Lipschitz functions are continuous. So the norm is continuous as a map $V \to \mathbb{R}$, and (by a similar argument using Cauchy-Schwarz) the inner product is jointly continuous as a map $V \times V \to \mathbf{F}$. Continuity of these basic operations is what lets the entire analysis machinery (limits, derivatives, integrals) be applied to vector-valued objects.

The third target is **bounding the operator norm of a sum**. Property $D$: for operators $S, T \in \mathcal{L}(V)$, the operator norm is $\|T\| = \sup_{\|v\| = 1} \|Tv\|$. Combination: triangle inequality gives $\|(S + T)v\| \leq \|Sv\| + \|Tv\|$ for each $v$, hence $\|S + T\| \leq \|S\| + \|T\|$ — the operator-norm version of triangle inequality. This is what makes operator-norm-distance-on-$\mathcal{L}(V)$ a metric, and what gives the Banach-algebra structure to operator algebras.

The fourth target is **the AM-QM inequality** for $n$ vectors. Property $D$: iterate the triangle inequality, then apply Cauchy-Schwarz to the right-hand side. Combination: $\|\sum_{k=1}^n v_k\| \leq \sum_{k=1}^n \|v_k\| \leq \sqrt{n} \cdot \sqrt{\sum \|v_k\|^2}$ (Cauchy-Schwarz applied to $(1, \dots, 1)$ and $(\|v_1\|, \dots, \|v_n\|)$). This bound shows that the norm of a sum is controlled both by the sum of norms (triangle) and by the root-sum-of-squares (Cauchy-Schwarz, after triangle), with the better bound depending on the problem.

---

# Why Is It True

The intuition is simple: **the norm of the sum is controlled by the sum of norms because the cross-term in the expansion cannot exceed the product of norms**.

Expanding $\|u + v\|^2$ using sesquilinearity:
$$
\|u + v\|^2 = \langle u + v, u + v\rangle = \|u\|^2 + \langle u, v\rangle + \langle v, u\rangle + \|v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.
$$
Compare this to the squared right-hand side of what we want to prove:
$$
(\|u\| + \|v\|)^2 = \|u\|^2 + 2\|u\|\,\|v\| + \|v\|^2.
$$
The two differ only in the middle term: $2\operatorname{Re}\langle u, v\rangle$ versus $2\|u\|\,\|v\|$. The triangle inequality (squared) holds if and only if $\operatorname{Re}\langle u, v\rangle \leq \|u\|\,\|v\|$, which follows immediately from Cauchy-Schwarz: $\operatorname{Re}\langle u, v\rangle \leq |\langle u, v\rangle| \leq \|u\|\,\|v\|$.

**The one-liner mechanism: the triangle inequality is Cauchy-Schwarz applied to the cross-term in $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$, turning a quadratic identity into a linear inequality by taking square roots.**

Geometrically, here is the picture in $\mathbb{R}^2$. The three vectors $0$, $u$, $u + v$ form a triangle. The side from $0$ to $u + v$ has length $\|u + v\|$. The path $0 \to u \to u + v$ has length $\|u\| + \|v\|$. The triangle inequality says the direct path is no longer than the indirect path, which is the basic Euclidean fact "the shortest distance between two points is a straight line". The reason this fact carries over to any inner product space is that all the relevant geometry — lengths, angles, perpendicularity — is determined by the inner product, and the inner product makes the inequality $\operatorname{Re}\langle u, v\rangle \leq \|u\|\,\|v\|$ true (via Cauchy-Schwarz).

The equality case clarifies what makes the inequality tight. Equality $\|u + v\| = \|u\| + \|v\|$ requires both equality in $\operatorname{Re}\langle u, v\rangle = \|u\|\,\|v\|$ (which is Cauchy-Schwarz with equality, hence one vector a scalar multiple of the other) **and** $\langle u, v\rangle$ being real and non-negative (so that $\operatorname{Re}\langle u, v\rangle = \langle u, v\rangle$, not just its real part). Combining: one vector is a *non-negative real* multiple of the other, i.e., the two vectors point in the same direction. In Euclidean intuition, this is the degenerate case where the "triangle" collapses to a line segment.

---

# What Makes This Hard

The proof of the triangle inequality, *given* Cauchy-Schwarz, is two lines. The hard part is recognising the proof structure: **prove the inequality at the squared-norm level, where sesquilinearity is available, then take square roots**. A common mistake is to try to prove the inequality directly at the norm level, which is harder because the norm is non-linear. Another common mistake is to forget that the cross-term in the expansion is $2\operatorname{Re}\langle u, v\rangle$ (not $2\langle u, v\rangle$) over $\mathbb{C}$, which silently makes the proof work for $\mathbb{R}$ but break for $\mathbb{C}$. A third source of difficulty is the equality case: equality in triangle inequality is *stricter* than equality in Cauchy-Schwarz — it requires the scalar to be non-negative real, not arbitrary.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Square both sides, expand using sesquilinearity, apply Cauchy-Schwarz to bound the cross-term, and take square roots.

**Subgoal decomposition:**

1. **Expand $\|u + v\|^2$.** Compute $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.
   - *Hint:* sesquilinear expansion of $\langle u + v, u + v\rangle$; remember $\langle v, u\rangle = \overline{\langle u, v\rangle}$, so the cross-terms sum to $2\operatorname{Re}\langle u, v\rangle$.
   - *Why needed:* turns the inequality (about norms) into an equivalent inequality (about real parts of inner products), where Cauchy-Schwarz applies.

2. **Apply Cauchy-Schwarz to the cross-term.** Conclude $\operatorname{Re}\langle u, v\rangle \leq |\langle u, v\rangle| \leq \|u\|\,\|v\|$.
   - *Hint:* real part of any complex number is $\leq$ its absolute value; Cauchy-Schwarz then bounds the absolute value by the product of norms.
   - *Why needed:* this is the *only* genuine inequality step; everything else is algebra.

3. **Combine.** Conclude $\|u + v\|^2 \leq \|u\|^2 + 2\|u\|\,\|v\| + \|v\|^2 = (\|u\| + \|v\|)^2$, then take square roots.
   - *Hint:* square roots preserve the order on $[0, \infty)$.
   - *Why needed:* this is the statement of the theorem.

4. **Track the equality case.** Equality requires both $|\langle u, v\rangle| = \|u\|\,\|v\|$ (Cauchy-Schwarz equality, so $u$ and $v$ are linearly dependent) and $\operatorname{Re}\langle u, v\rangle = |\langle u, v\rangle|$ (so $\langle u, v\rangle$ is real non-negative). Together: one of $u, v$ is a non-negative real multiple of the other.
   - *Hint:* trace through the two inequalities in step 2, identifying when each is sharp.
   - *Why needed:* completes the "if and only if" claim.

---

# Lemma Decomposition

> [!note]- Lemma 1: Squared-norm expansion
> **Statement:** For $u, v$ in an inner product space, $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.
>
> **Hint:** Expand $\langle u + v, u + v\rangle$ via additivity in both slots; use $\langle v, u\rangle = \overline{\langle u, v\rangle}$ to combine the two cross-terms.
>
> **Why needed:** Reduces the triangle inequality (a statement about norms) to a statement about $\operatorname{Re}\langle u, v\rangle$, where Cauchy-Schwarz is directly applicable.
>
> > [!note]- Full proof
> > By additivity of the inner product in both slots,
> > $$\langle u + v, u + v\rangle = \langle u, u\rangle + \langle u, v\rangle + \langle v, u\rangle + \langle v, v\rangle.$$
> > By conjugate symmetry, $\langle v, u\rangle = \overline{\langle u, v\rangle}$, so $\langle u, v\rangle + \langle v, u\rangle = \langle u, v\rangle + \overline{\langle u, v\rangle} = 2\operatorname{Re}\langle u, v\rangle$. Hence $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.

> [!note]- Lemma 2: Real part bounded by absolute value, bounded by norm product
> **Statement:** For $u, v$ in an inner product space, $\operatorname{Re}\langle u, v\rangle \leq |\langle u, v\rangle| \leq \|u\|\,\|v\|$.
>
> **Hint:** The real part of any complex number is at most its absolute value (with equality when the number is real non-negative). The absolute-value bound is [[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz]].
>
> **Why needed:** This is the genuine inequality step in the proof of the triangle inequality.
>
> > [!note]- Full proof
> > For any complex number $z$, write $z = a + bi$ with $a, b \in \mathbb{R}$. Then $\operatorname{Re} z = a$ and $|z| = \sqrt{a^2 + b^2} \geq |a| \geq a = \operatorname{Re} z$. Apply to $z = \langle u, v\rangle$ to get $\operatorname{Re}\langle u, v\rangle \leq |\langle u, v\rangle|$. Equality iff $\langle u, v\rangle$ is real and non-negative ($b = 0, a \geq 0$).
> >
> > Cauchy-Schwarz (proved separately, see [[Thm - Cauchy-Schwarz Inequality]]) gives $|\langle u, v\rangle| \leq \|u\|\,\|v\|$, with equality iff $u, v$ are linearly dependent.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** For $u, v$ in an inner product space, $\|u + v\| \leq \|u\| + \|v\|$, with equality iff one of $u, v$ is a non-negative real multiple of the other.
>
> *Proof.* Using sesquilinearity,
> $$\|u + v\|^2 = \langle u + v, u + v\rangle = \|u\|^2 + \langle u, v\rangle + \overline{\langle u, v\rangle} + \|v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.$$
> Now $\operatorname{Re}\langle u, v\rangle \leq |\langle u, v\rangle|$ (the real part is at most the absolute value), and by [[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz]], $|\langle u, v\rangle| \leq \|u\|\,\|v\|$. Therefore
> $$\|u + v\|^2 \leq \|u\|^2 + 2\|u\|\,\|v\| + \|v\|^2 = (\|u\| + \|v\|)^2.$$
> Taking square roots (legitimate since both sides are non-negative) gives $\|u + v\| \leq \|u\| + \|v\|$.
>
> **Equality case:** equality in the chain above requires:
> - **Equality in Cauchy-Schwarz** $|\langle u, v\rangle| = \|u\|\,\|v\|$: this forces one of $u, v$ to be a scalar multiple of the other.
> - **Equality in $\operatorname{Re}\langle u, v\rangle = |\langle u, v\rangle|$**: this forces $\langle u, v\rangle$ to be real and non-negative.
>
> Combining: one of $u, v$ is a scalar multiple of the other, and the scalar must be non-negative real for $\langle u, v\rangle = \alpha \|v\|^2$ (where $u = \alpha v$) to be real non-negative. Conversely, if $u = \alpha v$ with $\alpha \geq 0$ real, direct calculation gives $\|u + v\| = (\alpha + 1)\|v\| = \|u\| + \|v\|$. $\qquad\blacksquare$

> [!note]- Corollary: Reverse Triangle Inequality
> **Corollary.** For $u, v$ in an inner product space, $|\,\|u\| - \|v\|\,| \leq \|u - v\|$.
>
> *Proof.* Apply the triangle inequality to $u = (u - v) + v$: $\|u\| \leq \|u - v\| + \|v\|$, hence $\|u\| - \|v\| \leq \|u - v\|$. By symmetry (swapping $u$ and $v$), $\|v\| - \|u\| \leq \|v - u\| = \|u - v\|$. Combining, $|\,\|u\| - \|v\|\,| \leq \|u - v\|$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Probability: subadditivity of expectations.** For random variables $X_k$, $|E[\sum X_k]| = |E[\sum X_k]| \leq E[\sum |X_k|] = \sum E[|X_k|]$. This is the triangle inequality for the $L^1$ norm $\|X\|_1 = E[|X|]$ (which is not the inner-product norm, but a related norm). The inner-product version applies to $L^2$: $\|\sum X_k\|_2 \leq \sum \|X_k\|_2$ where $\|X\|_2 = \sqrt{E[X^2]}$. Both are special cases of "norm of sum $\leq$ sum of norms".

**Functional analysis: convergence of operator series.** For operators $T_k$ on a Hilbert space, if $\sum \|T_k\| < \infty$ (operator norm), then $\sum T_k$ converges in operator norm, because the partial sums $\sum_{k \leq N} T_k$ form a Cauchy sequence: $\|\sum_{k=N+1}^M T_k\| \leq \sum_{k=N+1}^M \|T_k\| \to 0$ by triangle inequality. This is the convergence criterion behind the **Neumann series** $(I - T)^{-1} = \sum_{k=0}^\infty T^k$ when $\|T\| < 1$, foundational in iterative algorithms and perturbation theory.

**Geometric optimisation: shortest-path arguments.** A path consisting of straight-line segments $v_1, v_2, \dots, v_n$ has total length $\sum \|v_k\|$, while the direct route from start to end has length $\|\sum v_k\|$. The triangle inequality iterated gives $\|\sum v_k\| \leq \sum \|v_k\|$, the precise statement that the broken path is at least as long as the direct one. This is the foundation of every shortest-path proof, every minimum-energy variational argument, and the Bellman optimality principle.

**Numerical analysis: error accumulation in iterative methods.** When you iterate a numerical map $x_{k+1} = T x_k$, the propagated error at step $n$ is bounded by triangle inequality: $\|x_n - x_n^{\text{exact}}\| \leq \sum_{k=0}^{n-1} \|T\|^k \|\epsilon_k\|$, where $\epsilon_k$ is the per-step error. This is the bedrock of error analysis: triangle inequality lets you trade joint error analysis (hard) for term-by-term error analysis (easy).

---

# Bridges

- **[[Thm - Cauchy-Schwarz Inequality|Cauchy-Schwarz Inequality]]** — Cauchy-Schwarz is the inequality on the cross-term that powers the triangle inequality. Specifically, the triangle inequality reduces (after squaring) to $\operatorname{Re}\langle u, v\rangle \leq \|u\|\,\|v\|$, which is Cauchy-Schwarz combined with $\operatorname{Re} z \leq |z|$. The two inequalities are intimately related: the triangle inequality is "the geometric face" of Cauchy-Schwarz, applied to norms rather than to the inner product itself.

- **General norms and the parallelogram law** *(see [[Def - Norm Induced by an Inner Product]])* — every inner-product norm satisfies the triangle inequality, but not every norm comes from an inner product. The norms that do are characterised by the [[Thm - Parallelogram Law|parallelogram law]]. Norms like $\ell^1$ and $\ell^\infty$ satisfy the triangle inequality but fail the parallelogram law, so they are genuine norms but not inner-product norms. The triangle inequality is therefore the *weaker* condition; the parallelogram law is the inner-product-specific strengthening.

- **Metric-space triangle inequality** — the metric induced by a norm satisfies $d(u, w) \leq d(u, v) + d(v, w)$ for all $u, v, w$. This is the metric-space triangle inequality, and it is the foundation of every limit, continuity, and compactness argument in $V$. The route from "the norm satisfies the triangle inequality" to "the metric satisfies the triangle inequality" is one line: $d(u, w) = \|u - w\| = \|(u - v) + (v - w)\| \leq \|u - v\| + \|v - w\| = d(u, v) + d(v, w)$.

- **[[Def - Minkowski Space and the Metric|Minkowski space]] and the reversal of the triangle inequality** *(Special Relativity)* — in Minkowski space with the indefinite metric, the triangle inequality *reverses direction* for timelike vectors. Specifically, for two future-pointing timelike vectors $u, v$, the proper-time interval satisfies $\tau(u + v) \geq \tau(u) + \tau(v)$, where $\tau = \sqrt{|\langle\cdot,\cdot\rangle|}$ — the *opposite* direction. This is the algebraic content of the **twin paradox**: among all worldlines connecting two timelike-separated events, the straight one has the *longest* proper time. The reversal is exactly what positive-vs-indefinite signature changes, and it makes intuitive sense in physics (the "moving twin" experiences less proper time than the "stationary twin").

- **Hölder's inequality and the Minkowski inequality** *(Analysis)* — the generalization of the triangle inequality to $L^p$ spaces is the **Minkowski inequality**: $\|f + g\|_p \leq \|f\|_p + \|g\|_p$ for $1 \leq p \leq \infty$. The $p = 2$ case follows from the inner-product triangle inequality via Cauchy-Schwarz. For general $p$, Minkowski's inequality follows from Hölder's inequality (the $L^p$ generalization of Cauchy-Schwarz). So the triangle-inequality-from-Cauchy-Schwarz proof structure generalizes from Hilbert to Banach $L^p$ spaces.
