---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Inner Product Space"
  - "Def - Norm Induced by an Inner Product"
  - "Thm - Cauchy-Schwarz Inequality"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be an inner product space over $\mathbf{F} \in \{\mathbb{R}, \mathbb{C}\}$. Show that for $u, v \in V$,
$$
|\langle u, v\rangle| = \|u\|\,\|v\|
$$
if and only if one of $u, v$ is a scalar multiple of the other (allowing the scalar to be $0$, so $u = 0$ or $v = 0$ trivially counts).

**Recall:**

The Cauchy-Schwarz inequality gives the bound; this exercise concerns its **equality case**.

![[Thm - Cauchy-Schwarz Inequality#Statement]]

The norm is induced from the inner product by $\|v\| = \sqrt{\langle v, v\rangle}$ (see [[Def - Norm Induced by an Inner Product]]). "Scalar multiple" means $u = \alpha v$ for some $\alpha \in \mathbf{F}$ (or symmetrically $v = \alpha u$).

---

# Convergent Strategy

**Problem class.** This is a *characterise equality* problem — a routine task once the proof of Cauchy-Schwarz has been understood. The strategy is to trace through the steps of the proof of Cauchy-Schwarz and identify which step admits equality only under a specific structural condition.

**Assumption pattern.** The hypothesis $|\langle u, v\rangle| = \|u\|\,\|v\|$ is an equality in an inequality whose proof involves *one* genuine inequality step: a norm-squared $\|w\|^2 \geq 0$ becoming $\|w\|^2 = 0$. So equality in Cauchy-Schwarz forces the norm-zero condition on some specific vector $w$, and $w = 0$ then gives the structural condition.

**Theorem routing.** The route is via the orthogonal-projection proof of Cauchy-Schwarz: write $u = (\langle u, v\rangle/\|v\|^2)v + w$ where $w \perp v$. Apply Pythagoras: $\|u\|^2 = |\langle u, v\rangle|^2/\|v\|^2 + \|w\|^2$. Cauchy-Schwarz equality forces $\|w\|^2 = 0$, hence $w = 0$, hence $u = (\langle u, v\rangle/\|v\|^2) v$ — a scalar multiple of $v$.

**Key decision point.** Whether to handle the case $v = 0$ separately and the case $v \neq 0$ via the orthogonal-projection construction. The case $v = 0$ is trivial: both sides of $|\langle u, v\rangle| = \|u\|\,\|v\|$ are $0$, and "$v = 0\cdot u$" is a (vacuous) scalar-multiple relationship. The non-trivial case $v \neq 0$ is what the orthogonal-projection construction handles. The decision point is whether to symmetrize ("one of $u, v$ is a scalar multiple of the other" requires checking both directions) — and the answer is "the construction is symmetric in $u, v$, so handling one direction suffices".

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VI — §6 Inner Product Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Project orthogonally to find the closest point** (operation 3). The construction $u = (\langle u, v\rangle/\|v\|^2)v + w$ is the orthogonal projection of $u$ onto $\operatorname{span}(v)$ plus the residual; this is the standard decomposition that powers the proof of Cauchy-Schwarz.

2. **Use Pythagoras to break a norm into orthogonal pieces** (operation 4). Applied to the decomposition above: $\|u\|^2 = \|(\langle u, v\rangle/\|v\|^2) v\|^2 + \|w\|^2$. Cauchy-Schwarz equality forces the second term to be zero.

3. **Use the orthogonal decomposition $V = U \oplus U^\perp$** (operation 8), specialised to $U = \operatorname{span}(v)$. The decomposition $u = t^*v + w$ with $w \perp v$ is the case where $U$ is one-dimensional.

---

# Hints

> [!note]- Hint 1
> Recall the proof of Cauchy-Schwarz: decompose $u$ along $\operatorname{span}(v)$ and its orthogonal complement, then apply Pythagoras. The inequality in the proof comes from one specific norm-squared term being non-negative. What does it mean for this term to be zero?

> [!note]- Hint 2
> Write $u = (\langle u, v\rangle / \|v\|^2)v + w$ where $w = u - (\langle u, v\rangle/\|v\|^2)v$. Check that $w \perp v$ by direct calculation. Apply Pythagoras to get $\|u\|^2 = |\langle u, v\rangle|^2/\|v\|^2 + \|w\|^2$.

> [!note]- Hint 3
> Equality in Cauchy-Schwarz $|\langle u, v\rangle|^2 = \|u\|^2 \|v\|^2$ means $\|w\|^2 = 0$, hence $w = 0$. This forces $u = (\langle u, v\rangle/\|v\|^2)v$, a scalar multiple of $v$.

> [!note]- Hint 4
> For the converse direction (scalar multiple $\Rightarrow$ equality): suppose $u = \alpha v$. Compute $\langle u, v\rangle$, $\|u\|$, $\|v\|$ explicitly and verify $|\langle u, v\rangle| = \|u\|\,\|v\|$ from the calculation. Handle the case $v = 0$ separately.

---

# Solution

The strategy is to use the orthogonal-projection proof of Cauchy-Schwarz: the inequality's only non-trivial step is the inequality $\|w\|^2 \geq 0$ for the residual, and equality forces $w = 0$.

**Plan:** The proof has two directions. The forward direction ($\Leftarrow$): if $u, v$ are linearly dependent, direct calculation gives the equality. The reverse direction ($\Rightarrow$): if $|\langle u, v\rangle| = \|u\|\,\|v\|$, trace through the orthogonal-projection construction to extract a linear-dependence relation. We handle the trivial case $v = 0$ separately, then assume $v \neq 0$.

**Step 1: The ($\Leftarrow$) direction — scalar multiple implies equality.**

If $u = \alpha v$ for some $\alpha \in \mathbf{F}$, direct calculation gives $|\langle u, v\rangle| = \|u\|\,\|v\|$.

> [!note]- Derivation
> Assume $u = \alpha v$ for some $\alpha \in \mathbf{F}$ (the case $v = \beta u$ is symmetric; if both are zero the equality is $0 = 0$).
>
> Compute:
> - $\langle u, v\rangle = \langle \alpha v, v\rangle = \alpha \langle v, v\rangle = \alpha \|v\|^2$.
> - $|\langle u, v\rangle| = |\alpha|\,\|v\|^2$.
> - $\|u\| = \|\alpha v\| = |\alpha|\,\|v\|$.
> - $\|u\|\,\|v\| = |\alpha|\,\|v\|^2$.
>
> Hence $|\langle u, v\rangle| = \|u\|\,\|v\|$, equality.

**Step 2: The ($\Rightarrow$) direction, case $v = 0$.**

If $v = 0$, both sides of $|\langle u, v\rangle| = \|u\|\,\|v\|$ are $0$, and "$v = 0 \cdot u$" is a scalar-multiple relationship (vacuously).

> [!note]- Derivation
> $v = 0$ gives $\langle u, v\rangle = \langle u, 0\rangle = 0$ and $\|v\| = 0$, so $|\langle u, v\rangle| = 0 = \|u\| \cdot 0 = \|u\|\,\|v\|$ — equality holds. The condition "$v$ is a scalar multiple of $u$" is satisfied by $v = 0 \cdot u$, the trivial scalar multiple.

**Step 3: The ($\Rightarrow$) direction, case $v \neq 0$ — equality implies $u$ is a scalar multiple of $v$.**

Assume $v \neq 0$ and $|\langle u, v\rangle| = \|u\|\,\|v\|$. Using the orthogonal-projection decomposition, we will show $u = (\langle u, v\rangle/\|v\|^2) v$.

> [!note]- Derivation
> Define $t^* = \langle u, v\rangle / \|v\|^2 \in \mathbf{F}$ and decompose
> $$u = t^* v + w, \qquad w = u - t^* v.$$
> By direct calculation,
> $$\langle w, v\rangle = \langle u, v\rangle - t^*\langle v, v\rangle = \langle u, v\rangle - \frac{\langle u, v\rangle}{\|v\|^2}\|v\|^2 = 0,$$
> so $w \perp v$. The vectors $t^* v$ and $w$ are orthogonal.
>
> By the [[Thm - Pythagorean Theorem|Pythagorean theorem]],
> $$\|u\|^2 = \|t^* v\|^2 + \|w\|^2 = |t^*|^2 \|v\|^2 + \|w\|^2 = \frac{|\langle u, v\rangle|^2}{\|v\|^2} + \|w\|^2.$$
> Multiplying by $\|v\|^2$:
> $$\|u\|^2 \|v\|^2 = |\langle u, v\rangle|^2 + \|w\|^2 \|v\|^2.$$
> By hypothesis, $|\langle u, v\rangle|^2 = \|u\|^2 \|v\|^2$. Substituting:
> $$\|u\|^2 \|v\|^2 = \|u\|^2 \|v\|^2 + \|w\|^2 \|v\|^2.$$
> Cancelling, $\|w\|^2 \|v\|^2 = 0$. Since $v \neq 0$, $\|v\|^2 > 0$, so $\|w\|^2 = 0$, hence $w = 0$ by definiteness of the norm.
>
> Therefore $u = t^* v = (\langle u, v\rangle/\|v\|^2)\, v$, a scalar multiple of $v$.

> [!note]- Complete formal solution
> Let $V$ be an inner product space and $u, v \in V$.
>
> **($\Leftarrow$):** Suppose $u = \alpha v$ for some $\alpha \in \mathbf{F}$ (the symmetric case is identical). Then $\langle u, v\rangle = \alpha \|v\|^2$ and $|\langle u, v\rangle| = |\alpha|\,\|v\|^2$. Also $\|u\| = |\alpha|\,\|v\|$ and $\|u\|\,\|v\| = |\alpha|\,\|v\|^2$. Hence $|\langle u, v\rangle| = \|u\|\,\|v\|$. The case $u = 0$ or $v = 0$ is included with $\alpha = 0$.
>
> **($\Rightarrow$):** Suppose $|\langle u, v\rangle| = \|u\|\,\|v\|$. If $v = 0$, both sides are $0$, and $v = 0 \cdot u$ is a (trivial) scalar multiple relationship. Otherwise, $v \neq 0$ and we use the orthogonal-projection decomposition.
>
> Set $t^* = \langle u, v\rangle / \|v\|^2$ and $w = u - t^* v$. Compute $\langle w, v\rangle = \langle u, v\rangle - t^* \|v\|^2 = \langle u, v\rangle - \langle u, v\rangle = 0$, so $w \perp v$. By the [[Thm - Pythagorean Theorem|Pythagorean theorem]] applied to $u = t^* v + w$,
> $$\|u\|^2 = |t^*|^2 \|v\|^2 + \|w\|^2 = \frac{|\langle u, v\rangle|^2}{\|v\|^2} + \|w\|^2.$$
> Multiplying by $\|v\|^2$: $\|u\|^2\|v\|^2 = |\langle u, v\rangle|^2 + \|w\|^2 \|v\|^2$. By hypothesis $\|u\|^2 \|v\|^2 = |\langle u, v\rangle|^2$, so $\|w\|^2 \|v\|^2 = 0$. Since $\|v\| \neq 0$, $\|w\|^2 = 0$, hence $w = 0$. Thus $u = t^* v$, a scalar multiple of $v$. $\blacksquare$

---

# Key Takeaways

**Equality in an inequality forces the residual norm to vanish.** This is a deeply general pattern: any inequality proved by "$\|X\|^2 \geq 0$" with equality iff $X = 0$ has its equality case characterised by $X = 0$. The skill is identifying the *specific residual* $X$ that appears in the proof. For Cauchy-Schwarz via orthogonal projection, the residual is $w = u - (\langle u, v\rangle/\|v\|^2)v$ — the part of $u$ orthogonal to $v$. Equality forces $w = 0$, hence $u$ has no orthogonal component, hence $u$ lies entirely on the line through $v$. The transferable lesson: when you need the equality case of a Cauchy-Schwarz-style inequality, trace back to the proof and locate the term that was non-negative with $\geq$ replaced by $=$.

**The orthogonal-projection construction is universally applicable.** The decomposition $u = t^* v + w$ with $w \perp v$, $t^* = \langle u, v\rangle/\|v\|^2$, is the workhorse of Cauchy-Schwarz, the proof of the best-approximation theorem, and the construction of orthogonal projections in general. Whenever you have a vector and a one-dimensional subspace (or more generally a finite-dimensional subspace), this decomposition is available — and applying the Pythagorean theorem to it converts joint geometric statements into separate algebraic ones. The pattern generalizes to higher-dimensional projections in the [[Thm - Best Approximation by Orthogonal Projection|best-approximation theorem]].

**Strict inequality is generic; equality is structural.** Cauchy-Schwarz is strict ($|\langle u, v\rangle| < \|u\|\,\|v\|$) for *most* pairs of vectors — specifically, for any pair that is not collinear. Equality requires the special structural condition of linear dependence. This pattern recurs throughout mathematics: most inequalities have strict inequality for generic inputs, with equality occurring only on a thin set characterised by a degenerate structural condition. The skill of identifying these conditions is the skill of understanding the inequality. For Cauchy-Schwarz, the equality condition is "collinearity", which (in $\mathbb{R}^2$) is the condition that the vectors lie on the same line through the origin — a one-dimensional condition in a two-dimensional space.

**The complex case has subtleties hidden in the scalar.** Over $\mathbb{C}$, "$u$ is a scalar multiple of $v$" means $u = \alpha v$ for some $\alpha \in \mathbb{C}$, which includes phase factors. So in $\mathbb{C}^2$, $u = (1, i) = i \cdot (1, i)$... wait, that gives $u = i (-i, 1) = (1, i)$, but $i \cdot (1, i) = (i, -1) \neq (1, i)$. So the scalar must be chosen carefully. The general statement: $|\langle u, v\rangle| = \|u\|\,\|v\|$ iff $u = \alpha v$ for some complex $\alpha$ (which may include both magnitude and phase). The equality case of the triangle inequality is *stricter*: it requires $\alpha$ to be non-negative real (so the vectors point in the same direction, not just collinear). This is the precise sense in which "equality in Cauchy-Schwarz" is weaker than "equality in the triangle inequality" over $\mathbb{C}$ — the first allows arbitrary scalar multiples, the second requires non-negative real multiples.
