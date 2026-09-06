---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Involutive Distribution"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry, frobenius]
---

# Problem Statement

On $\mathbb{R}^4$ with coordinates $(x, y, z, w)$, consider the three vector fields

$$X = \partial_x, \qquad Y = \partial_y + x\,\partial_w, \qquad Z = \partial_z + y\,\partial_w.$$

Show that they span a rank-$3$ smooth distribution $D$ on $\mathbb{R}^4$, and determine whether $D$ is involutive. If it is, find the integral submanifolds explicitly.

**Recall:**

![[Def - Distribution on a Manifold#The Definition]]

![[Def - Involutive Distribution#The Definition]]

The Lie bracket in coordinates: for $X = \sum X^i\partial_i$ and $Y = \sum Y^i\partial_i$,
$$[X, Y]^k = \sum_j (X^j\partial_jY^k - Y^j\partial_jX^k).$$

---

# Convergent Strategy

**Problem class:** Involutivity test for a distribution given by spanning vector fields. Pattern: compute all pairwise Lie brackets, and check whether each is a section of the distribution (i.e., a linear combination of the spanning fields with smooth coefficients).

**Assumption pattern:** Three explicit vector fields on $\mathbb{R}^4$, given in coordinates. The bracket computation is mechanical — each bracket is a vector field in $\mathbb{R}^4$, expressed in terms of $\partial_x, \partial_y, \partial_z, \partial_w$. Then we check whether the answer is a linear combination of $X, Y, Z$.

**Theorem routing:** Direct application of the bracket criterion for involutivity ([[Def - Involutive Distribution]] local-frame criterion). If all $\binom{3}{2} = 3$ brackets are sections of $D$, then $D$ is involutive; if any bracket is *not* a section, $D$ is non-involutive.

**Key decision point:** The crucial computation is whether $[Y, Z]$ — the bracket of the two non-coordinate fields — lies in $\mathrm{span}(X, Y, Z)$. The brackets $[X, Y]$ and $[X, Z]$ are easier because $X = \partial_x$ has constant coefficient, so the brackets reduce to partial derivatives along $x$.

---

# Legal Operations Used

1. **Test involutivity by Lie brackets on a local frame** (operation 4 from the topic page). Compute the three brackets $[X, Y]$, $[X, Z]$, $[Y, Z]$ and check membership in $\mathrm{span}(X, Y, Z)$.

2. **Generate a [[Def - Subgroup|subgroup]]/[[Def - Subspace|subspace]] from elements you possess** (analogous to operation 8). The frame $\{X, Y, Z\}$ generates the distribution $D = \mathrm{span}(X, Y, Z)$ at every point.

3. **Invoke Frobenius to manufacture integral manifolds** (operation 6 from the topic page). If $D$ is involutive, [[Thm - The Frobenius Theorem|Frobenius]] guarantees a flat chart; we then find functions whose level sets are the integral manifolds.

---

# Hints

> [!note]- Hint 1
> First verify that $X, Y, Z$ are linearly independent at every point of $\mathbb{R}^4$. Then $D = \mathrm{span}(X, Y, Z)$ is a smooth rank-$3$ distribution.

> [!note]- Hint 2
> Compute the three pairwise Lie brackets: $[X, Y]$, $[X, Z]$, $[Y, Z]$.

> [!note]- Hint 3
> Check if each bracket lies in $\mathrm{span}(X, Y, Z)$. A useful test: a vector field $W$ lies in $D$ iff $W$ has no $\partial_w$-component that is independent of the $\partial_w$-contributions of $X, Y, Z$ — i.e. iff the $\partial_w$-part can be matched by an appropriate combination of $X$ (no $\partial_w$), $Y$ ($x\partial_w$), $Z$ ($y\partial_w$).

> [!note]- Hint 4
> Alternative test: find an annihilating $1$-form $\omega$ for $D$ — a $1$-form with $\omega(X) = \omega(Y) = \omega(Z) = 0$. Then $W \in D$ iff $\omega(W) = 0$.

> [!note]- Hint 5
> If $D$ is involutive, by Frobenius there is a function $f$ whose level sets are the integral manifolds. Look for $f$ depending on $w$ minus a polynomial in $x, y, z$ — the involutivity condition $\omega \wedge d\omega = 0$ for $\omega = df$ is automatic.

---

# Solution

The plan: verify the three fields are linearly independent, compute the three pairwise brackets, check involutivity, and (if involutive) identify integral submanifolds.

**Step 1: $X, Y, Z$ are linearly independent at every point.**

> [!note]- Derivation
> In the standard frame $(\partial_x, \partial_y, \partial_z, \partial_w)$, the coordinate representations are:
> $$X = (1, 0, 0, 0), \qquad Y = (0, 1, 0, x), \qquad Z = (0, 0, 1, y).$$
> Forming the matrix with these as columns:
> $$\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & x & y \end{pmatrix}.$$
> The top three rows are the identity, so the columns are linearly independent at every point — for any $(x, y, z, w)$.
>
> Hence $D = \mathrm{span}(X, Y, Z)$ is a smooth rank-$3$ [[Def - Subbundle|subbundle]] of $T\mathbb{R}^4$.

**Step 2: Compute the three Lie brackets.**

> [!note]- Derivation
> *Compute $[X, Y]$.* By definition $[X, Y]f = X(Yf) - Y(Xf)$. In coordinates:
> $$[X, Y] = [\partial_x, \partial_y + x\partial_w].$$
> Distribute: $[\partial_x, \partial_y] = 0$ (coordinate vector fields commute) and $[\partial_x, x\partial_w]$ — use the formula $[\partial_x, fW] = (\partial_x f)W + f[\partial_x, W]$ for $f = x$, $W = \partial_w$: $[\partial_x, x\partial_w] = (\partial_x x)\partial_w + x[\partial_x, \partial_w] = 1\cdot\partial_w + 0 = \partial_w$.
> So $[X, Y] = 0 + \partial_w = \partial_w$.
>
> *Compute $[X, Z]$.* Similarly:
> $$[X, Z] = [\partial_x, \partial_z + y\partial_w] = [\partial_x, \partial_z] + [\partial_x, y\partial_w].$$
> $[\partial_x, \partial_z] = 0$. $[\partial_x, y\partial_w] = (\partial_x y)\partial_w + y[\partial_x, \partial_w] = 0 + 0 = 0$.
> So $[X, Z] = 0$.
>
> *Compute $[Y, Z]$.*
> $$[Y, Z] = [\partial_y + x\partial_w, \partial_z + y\partial_w].$$
> Distribute:
> - $[\partial_y, \partial_z] = 0$.
> - $[\partial_y, y\partial_w] = (\partial_y y)\partial_w + y[\partial_y, \partial_w] = 1\cdot\partial_w + 0 = \partial_w$.
> - $[x\partial_w, \partial_z] = -[\partial_z, x\partial_w] = -((\partial_z x)\partial_w + x[\partial_z, \partial_w]) = 0$.
> - $[x\partial_w, y\partial_w]$: use $[fW, gV] = fg[W, V] + f(Wg)V - g(Vf)W$ for $W = V = \partial_w$, $f = x$, $g = y$. Get $xy[\partial_w, \partial_w] + x(\partial_w y)\partial_w - y(\partial_w x)\partial_w = 0 + 0 - 0 = 0$.
>
> Sum: $[Y, Z] = 0 + \partial_w + 0 + 0 = \partial_w$.

**Step 3: Check involutivity.**

> [!note]- Derivation
> The three brackets are $[X, Y] = \partial_w$, $[X, Z] = 0$, $[Y, Z] = \partial_w$.
>
> We need each to lie in $\mathrm{span}(X, Y, Z) = D$. Is $\partial_w \in D$? In coordinates, $\partial_w = (0, 0, 0, 1)$ — and from the column matrix above, the span $D$ at any point $(x, y, z, w)$ consists of all vectors of the form $aX + bY + cZ = (a, b, c, bx + cy)$ for $a, b, c \in \mathbb{R}$. The fourth component of any vector in $D$ is $bx + cy$, which is *determined* by the first three components (specifically $b$ and $c$). So a vector with first three components zero must have $b = c = 0$, hence fourth component zero. The vector $\partial_w = (0, 0, 0, 1)$ has first three components zero but fourth component $1 \neq 0$, so $\partial_w \notin D$.
>
> Therefore $[X, Y] = \partial_w \notin D$. Similarly $[Y, Z] = \partial_w \notin D$. So $D$ is **not involutive**.

**Step 4: Apply Frobenius.**

Because $D$ is not involutive, [[Thm - The Frobenius Theorem|Frobenius's theorem]] implies that $D$ is not integrable. Thus there is no $3$-dimensional immersed submanifold through any point whose tangent spaces equal $D$. The conditional request “if it is involutive” therefore has no further case to solve.

> [!note]- Complete formal solution
> The three vector fields are linearly independent at every point of $\mathbb{R}^4$ (the $3 \times 3$ minor of the coefficient matrix in $\partial_x, \partial_y, \partial_z$ is the identity, hence non-singular). So $D = \mathrm{span}(X, Y, Z)$ is a rank-$3$ smooth distribution.
>
> Compute the three pairwise Lie brackets:
> - $[X, Y] = [\partial_x, \partial_y + x\partial_w] = (\partial_x x)\partial_w = \partial_w$.
> - $[X, Z] = [\partial_x, \partial_z + y\partial_w] = 0$.
> - $[Y, Z] = [\partial_y + x\partial_w, \partial_z + y\partial_w] = (\partial_y y)\partial_w = \partial_w$.
>
> Now check $\partial_w \in D$. At any point $(x, y, z, w)$, $D$ consists of vectors $aX + bY + cZ = (a, b, c, bx + cy)$. The vector $(0, 0, 0, 1)$ representing $\partial_w$ requires $a = b = c = 0$ (from the first three components), but then $bx + cy = 0 \neq 1$. So $\partial_w \notin D$, and the brackets $[X, Y], [Y, Z]$ are not in $D$.
>
> Therefore $D$ is **not involutive**, and by [[Thm - The Frobenius Theorem|Frobenius]] $D$ is not integrable: no $3$-dimensional integral submanifold of $D$ exists through any point of $\mathbb{R}^4$. $\blacksquare$

---

# Key Takeaways

**The local-frame criterion for involutivity reduces an infinite check (every pair of sections) to a finite computation.** The original definition of involutivity requires checking $[X, Y] \in \Gamma(D)$ for *every* pair of smooth sections — uncountably many. The local-frame criterion (Lemma 19.4 in Lee) says it suffices to check this for a chosen local frame, which has only $\binom{k}{2}$ pairs at rank $k$. For rank $3$, that's three pairs; for rank $2$, just one. This is the practical computational tool — without it, involutivity checks would be infeasible. The trigger to recognize: any time you need to test involutivity, first pick a convenient local frame and compute its brackets.

**The bracket of vector fields measures non-commutativity of their flows.** Computing $[X, Y]$ for two vector fields $X, Y$ tells you whether their flows commute: $[X, Y] = 0$ iff the flows commute. For involutivity, we don't need exact commutativity — we just need the bracket to stay inside $D$, which is a weaker condition. In our example, $[X, Y] = \partial_w$ escapes $D$, so the flow of $X$ does not preserve the $D$-directions of $Y$ — geometrically, flowing along $X$ and then $Y$ doesn't trace out a $3$-dimensional surface, but instead acquires a $w$-component drift. The trigger: whenever you see a non-zero bracket, ask "where is it in the tangent space, relative to $D$?" — the answer reveals the integrability obstruction.

**A distribution defined by spanning fields with non-trivial bracket terms is the typical non-involutive example.** Coordinate vector fields commute, so a distribution spanned by them is automatically involutive (with explicit integral manifolds — the coordinate planes). The interesting non-involutive examples involve fields that combine coordinate derivatives with multiplicative coordinates, like $\partial_y + x\partial_w$ — the *coupling* between coordinates is precisely what generates non-trivial brackets and breaks involutivity. The trigger to recognize: any distribution given by fields that look like "coordinate vector field plus a coordinate-dependent component in another direction" should be tested for involutivity by computing the relevant cross-derivative bracket.

**Negative Frobenius applications: certifying *non*-integrability is just as important as certifying integrability.** Sometimes the answer to "is this distribution integrable?" is "no" — and Frobenius gives a clean, computational route to certifying this. The standard contact distribution on $\mathbb{R}^3$ ([[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]]) is the prototype. In mechanics, nonholonomic constraints are not integrable; in PDE theory, overdetermined systems without compatibility conditions are not solvable. The trigger to recognize: any time involutivity fails, the answer is "no integral submanifold," and this is a *meaningful* statement, often the key to understanding the geometric obstruction at hand.
