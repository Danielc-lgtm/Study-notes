---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Exterior Derivative on a Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Thm - Coordinate Expression for the Exterior Derivative"
tags: [geometry, differential-geometry, computation]
---

# Problem Statement

Compute $d\omega$ for each of the following differential forms, working in the indicated coordinates. Verify that $d^2\omega = 0$ in part (c) by computing $d(d\omega)$ directly.

(a) $f(x, y, z) = x^2 y z + e^{xz}$ on $\mathbb{R}^3$. Compute $df$.

(b) $\omega = e^{xy}\,dx + (x + y^2)\,dy$ on $\mathbb{R}^2$. Compute $d\omega$.

(c) $\omega = x\,dy \wedge dz + y\,dz \wedge dx + z\,dx \wedge dy$ on $\mathbb{R}^3$. Compute $d\omega$ and verify $d(d\omega) = 0$ directly.

(d) $\omega = f(x, y)\,dx + g(x, y)\,dy$ on $\mathbb{R}^2$, with $f, g$ smooth. Compute $d\omega$ and describe the condition for $\omega$ to be closed.

(e) $\omega = u\,dx + v\,dy + w\,dz$ on $\mathbb{R}^3$, with $u, v, w$ smooth functions. Compute $d\omega$.

**Recall:**

![[Thm - Coordinate Expression for the Exterior Derivative#Statement]]

The chart formula: $d(\sum'_I \omega_I\,dx^I) = \sum'_I d\omega_I \wedge dx^I = \sum'_I \sum_j (\partial_j \omega_I)\,dx^j \wedge dx^I$.

---

# Convergent Strategy

**Problem class:** Mechanical computation of the exterior derivative on specific forms. The problem drills the coordinate formula and the rules for simplifying wedge products with repeated indices and sign-flips from reordering.

**Assumption pattern:** Each part gives an explicit form in $\mathbb{R}^n$ (with $n = 2$ or $3$). The route is the chart formula $d\omega = \sum d\omega_I \wedge dx^I$, with each $d\omega_I$ computed by partial differentiation and the resulting wedge reduced.

**Theorem routing:** All five parts reduce to [[Thm - Coordinate Expression for the Exterior Derivative|the coordinate formula]]. The verification of $d^2\omega = 0$ in (c) uses [[Thm - d-Squared-is-Zero]].

**Key decision point:** The bookkeeping when wedge products require reordering. For instance, $dy \wedge dx = -dx \wedge dy$, and computing $d(P\,dx) = (\partial_y P)\,dy \wedge dx + (\partial_z P)\,dz \wedge dx$ requires sign-flipping to put the wedge into increasing-multi-index form $-(\partial_y P)\,dx \wedge dy - (\partial_z P)\,dx \wedge dz$. Beginners often forget these signs.

---

# Legal Operations Used

1. **Expand a form in coordinates and apply $d$ mechanically** (operation 1) — the primary tool for every part of this exercise.

2. **Use $d^2 = 0$ as a one-line shortcut** (operation 4) — verifies the answer in (c) without redoing the computation.

---

# Hints

> [!note]- Hint 1
> For (a): use $df = (\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz$. Compute each partial derivative by the product rule and exponential rule.

> [!note]- Hint 2
> For (b): $d\omega = d(e^{xy}) \wedge dx + d(x + y^2) \wedge dy$. Compute each differential, then wedge with $dx$ or $dy$, and simplify using $dx \wedge dx = 0$, etc.

> [!note]- Hint 3
> For (c): each term contributes via $d(x) \wedge dy \wedge dz = dx \wedge dy \wedge dz$ (and similarly for $y, z$); the other partial-derivative terms vanish by repeated indices.

> [!note]- Hint 4
> For the closedness in (d): $\omega$ is closed when $\partial_y f - \partial_x g = 0$, equivalently $\partial f / \partial y = \partial g / \partial x$ — the exactness condition from elementary ODE.

---

# Solution

The general strategy is mechanical: expand each $d\omega$ via the chart formula and simplify by combining terms with the same basic wedge form, using $dx^i \wedge dx^j = -dx^j \wedge dx^i$ and $dx^i \wedge dx^i = 0$.

**Step 1: Compute $df$ for (a).**

$df = (\partial_x f)\,dx + (\partial_y f)\,dy + (\partial_z f)\,dz$. Computing each partial:
- $\partial_x f = 2xyz + ze^{xz}$
- $\partial_y f = x^2 z$
- $\partial_z f = x^2 y + xe^{xz}$

So $df = (2xyz + ze^{xz})\,dx + x^2 z\,dy + (x^2 y + xe^{xz})\,dz$.

> [!note]- Derivation
> $f(x, y, z) = x^2 yz + e^{xz}$. By the chain rule on $e^{xz}$: $\partial_x(e^{xz}) = z e^{xz}$, $\partial_y(e^{xz}) = 0$, $\partial_z(e^{xz}) = x e^{xz}$. By the product rule on $x^2 yz$: $\partial_x(x^2 yz) = 2xyz$, $\partial_y(x^2 yz) = x^2 z$, $\partial_z(x^2 yz) = x^2 y$. Combining gives the three partials above. The differential is the $1$-form with these as coefficients.

**Step 2: Compute $d\omega$ for (b).**

$\omega = e^{xy}\,dx + (x + y^2)\,dy$. By the chart formula:
$d\omega = d(e^{xy}) \wedge dx + d(x + y^2) \wedge dy = (y e^{xy}\,dx + x e^{xy}\,dy) \wedge dx + (1 \cdot dx + 2y\,dy) \wedge dy$.

Simplify each term:
- $(y e^{xy}\,dx) \wedge dx = 0$ (repeated $dx$).
- $(x e^{xy}\,dy) \wedge dx = x e^{xy}\,dy \wedge dx = -x e^{xy}\,dx \wedge dy$.
- $(1 \cdot dx) \wedge dy = dx \wedge dy$.
- $(2y\,dy) \wedge dy = 0$.

So $d\omega = -x e^{xy}\,dx \wedge dy + dx \wedge dy = (1 - x e^{xy})\,dx \wedge dy$.

> [!note]- Derivation
> $de^{xy} = (\partial_x e^{xy})\,dx + (\partial_y e^{xy})\,dy = y e^{xy}\,dx + x e^{xy}\,dy$ (by chain rule on $e^{xy}$).
>
> $d(x + y^2) = 1\,dx + 2y\,dy$ (by linearity).
>
> Wedge each with the corresponding $1$-form (the second factor of the original $\omega$):
> $de^{xy} \wedge dx = (y e^{xy}\,dx) \wedge dx + (x e^{xy}\,dy) \wedge dx$. The first is zero (repeated $dx$), the second is $-x e^{xy}\,dx \wedge dy$ (flip sign to put into increasing form).
>
> $d(x + y^2) \wedge dy = dx \wedge dy + 2y\,dy \wedge dy = dx \wedge dy + 0 = dx \wedge dy$.
>
> Summing: $d\omega = -x e^{xy}\,dx \wedge dy + dx \wedge dy = (1 - x e^{xy})\,dx \wedge dy$.

**Step 3: Compute $d\omega$ for (c).**

$\omega = x\,dy \wedge dz + y\,dz \wedge dx + z\,dx \wedge dy$. By the chart formula:
$d\omega = dx \wedge dy \wedge dz + dy \wedge dz \wedge dx + dz \wedge dx \wedge dy$.

All three terms simplify to $dx \wedge dy \wedge dz$ by cyclic permutation (which costs no sign for an even number of transpositions). So $d\omega = 3\,dx \wedge dy \wedge dz$.

Verify $d(d\omega) = 0$: since $d\omega$ is a top-degree form ($3$-form on $\mathbb{R}^3$), the next exterior derivative would be a $4$-form on $\mathbb{R}^3$, which is zero. Done.

> [!note]- Derivation
> $\omega = x\,dy \wedge dz + y\,dz \wedge dx + z\,dx \wedge dy$. Apply $d$:
>
> $d(x\,dy \wedge dz) = dx \wedge dy \wedge dz + x \cdot d(dy \wedge dz) = dx \wedge dy \wedge dz + 0$ (using $d(dy \wedge dz) = 0$ by Lemma 1 of [[Thm - d-Squared-is-Zero]]).
>
> $d(y\,dz \wedge dx) = dy \wedge dz \wedge dx$. By cyclic permutation $dy \wedge dz \wedge dx = dx \wedge dy \wedge dz$ (two transpositions, even).
>
> $d(z\,dx \wedge dy) = dz \wedge dx \wedge dy = dx \wedge dy \wedge dz$ (two transpositions).
>
> Summing: $d\omega = 3\,dx \wedge dy \wedge dz$.
>
> $d(d\omega)$: since $d\omega$ is a $3$-form on $\mathbb{R}^3$, $d(d\omega)$ would be a $4$-form on $\mathbb{R}^3$. Since $\Omega^4(\mathbb{R}^3) = 0$, $d(d\omega) = 0$ trivially. This is consistent with $d^2 = 0$.

**Step 4: Compute $d\omega$ for (d).**

$\omega = f(x, y)\,dx + g(x, y)\,dy$. By the chart formula:
$d\omega = df \wedge dx + dg \wedge dy$.

Compute $df = (\partial_x f)\,dx + (\partial_y f)\,dy$ and $dg = (\partial_x g)\,dx + (\partial_y g)\,dy$. Wedge:
$df \wedge dx = (\partial_x f)\,dx \wedge dx + (\partial_y f)\,dy \wedge dx = -(\partial_y f)\,dx \wedge dy$.
$dg \wedge dy = (\partial_x g)\,dx \wedge dy + (\partial_y g)\,dy \wedge dy = (\partial_x g)\,dx \wedge dy$.

Summing: $d\omega = (\partial_x g - \partial_y f)\,dx \wedge dy$.

$\omega$ is closed if and only if $\partial_x g = \partial_y f$, i.e., $\partial f/\partial y = \partial g/\partial x$.

> [!note]- Derivation
> Mechanical application of the chart formula and the wedge anticommutativity to put each term into the standard $dx \wedge dy$ form.

**Step 5: Compute $d\omega$ for (e).**

$\omega = u\,dx + v\,dy + w\,dz$. By the chart formula:
$d\omega = du \wedge dx + dv \wedge dy + dw \wedge dz$.

Each differential is a $1$-form; wedge each with the appropriate $1$-form and simplify.

$du \wedge dx = (\partial_x u\,dx + \partial_y u\,dy + \partial_z u\,dz) \wedge dx = -(\partial_y u)\,dx \wedge dy - (\partial_z u)\,dx \wedge dz$ (sign-flipping to increasing form, and $dx \wedge dx = 0$).

$dv \wedge dy = (\partial_x v\,dx + \partial_z v\,dz) \wedge dy = (\partial_x v)\,dx \wedge dy - (\partial_z v)\,dy \wedge dz$ (the $\partial_y v\,dy \wedge dy = 0$ term drops; the $\partial_z v\,dz \wedge dy = -\partial_z v\,dy \wedge dz$ flips).

Wait, let me redo this more carefully. $dv \wedge dy = (\partial_x v)\,dx \wedge dy + (\partial_y v)\,dy \wedge dy + (\partial_z v)\,dz \wedge dy = (\partial_x v)\,dx \wedge dy + 0 + (\partial_z v)\,dz \wedge dy$. Now $dz \wedge dy = -dy \wedge dz$, so $dv \wedge dy = (\partial_x v)\,dx \wedge dy - (\partial_z v)\,dy \wedge dz$.

$dw \wedge dz = (\partial_x w)\,dx \wedge dz + (\partial_y w)\,dy \wedge dz + (\partial_z w)\,dz \wedge dz = (\partial_x w)\,dx \wedge dz + (\partial_y w)\,dy \wedge dz$. To normalize, $dx \wedge dz = -dz \wedge dx$, so this becomes $-(\partial_x w)\,dz \wedge dx + (\partial_y w)\,dy \wedge dz$.

Hmm, let me write things in the standard increasing basis $\{dy \wedge dz, dz \wedge dx, dx \wedge dy\}$ (which is the orientation-respecting basis for $\Omega^2(\mathbb{R}^3)$).

$du \wedge dx$: $(\partial_y u)\,dy \wedge dx = -(\partial_y u)\,dx \wedge dy$. And $(\partial_z u)\,dz \wedge dx$ — already in the $dz \wedge dx$ form, but we want to express in the dual basis. Let me use the basis $\{dy\wedge dz, dz\wedge dx, dx\wedge dy\}$ (cyclic). Then $dy \wedge dx = -dx \wedge dy$, contribution to $dx \wedge dy$ is $-(\partial_y u)$.

$dv \wedge dy$: $(\partial_x v)\,dx \wedge dy$ + $(\partial_z v)\,dz \wedge dy = -(\partial_z v)\,dy \wedge dz$, contributions: $(\partial_x v)$ to $dx \wedge dy$, $-(\partial_z v)$ to $dy \wedge dz$.

$dw \wedge dz$: $(\partial_x w)\,dx \wedge dz = -(\partial_x w)\,dz \wedge dx$, contribution $-(\partial_x w)$ to $dz \wedge dx$. And $(\partial_y w)\,dy \wedge dz$, contribution $(\partial_y w)$ to $dy \wedge dz$.

Summing coefficients in the basis $\{dy\wedge dz, dz\wedge dx, dx\wedge dy\}$:
- $dy \wedge dz$: $-(\partial_z v) + (\partial_y w) = (\partial_y w - \partial_z v)$.
- $dz \wedge dx$: $-(\partial_x w) + (\partial_z u) = (\partial_z u - \partial_x w)$. 

Hmm wait. The $du \wedge dx$ contributed $(\partial_z u)\,dz \wedge dx$ — yes positive. So $dz \wedge dx$ coefficient is $(\partial_z u) - (\partial_x w) = (\partial_z u - \partial_x w)$.

- $dx \wedge dy$: $-(\partial_y u) + (\partial_x v) = (\partial_x v - \partial_y u)$.

So
$$d\omega = (\partial_y w - \partial_z v)\,dy \wedge dz + (\partial_z u - \partial_x w)\,dz \wedge dx + (\partial_x v - \partial_y u)\,dx \wedge dy.$$

This is the curl of $(u, v, w)$, in the $2$-form representation. Consistent with [[Ex - The Exterior Derivative on R^3 Recovers Grad-Curl-Div]].

> [!note]- Derivation
> Expand each differential and wedge:
>
> $du \wedge dx = \sum_j(\partial_j u)\,dx^j \wedge dx$. The only nonzero terms are $j = y$ and $j = z$: $(\partial_y u)\,dy \wedge dx + (\partial_z u)\,dz \wedge dx$.
>
> $dv \wedge dy = (\partial_x v)\,dx \wedge dy + (\partial_z v)\,dz \wedge dy$.
>
> $dw \wedge dz = (\partial_x w)\,dx \wedge dz + (\partial_y w)\,dy \wedge dz$.
>
> Now reorganize to the standard increasing-multi-index basis $\{dy \wedge dz, dx \wedge dz, dx \wedge dy\}$ (or to the cyclic basis $\{dy \wedge dz, dz \wedge dx, dx \wedge dy\}$):
>
> $(\partial_y u)\,dy \wedge dx = -(\partial_y u)\,dx \wedge dy$.
>
> $(\partial_z u)\,dz \wedge dx$: cyclic basis $dz \wedge dx$, coefficient $\partial_z u$.
>
> $(\partial_z v)\,dz \wedge dy = -(\partial_z v)\,dy \wedge dz$.
>
> $(\partial_x w)\,dx \wedge dz = -(\partial_x w)\,dz \wedge dx$.
>
> Summing in the cyclic basis $\{dy \wedge dz, dz \wedge dx, dx \wedge dy\}$:
> - $dy \wedge dz$: $-(\partial_z v) + (\partial_y w) = (\partial_y w - \partial_z v)$.
> - $dz \wedge dx$: $(\partial_z u) - (\partial_x w) = (\partial_z u - \partial_x w)$.
> - $dx \wedge dy$: $(\partial_x v) - (\partial_y u) = (\partial_x v - \partial_y u)$.
>
> Net: $d\omega = (\partial_y w - \partial_z v)\,dy \wedge dz + (\partial_z u - \partial_x w)\,dz \wedge dx + (\partial_x v - \partial_y u)\,dx \wedge dy$. This is $\operatorname{curl}(u, v, w)$ in $2$-form representation.

> [!note]- Complete formal solution
> **(a)** $df = (2xyz + ze^{xz})\,dx + x^2 z\,dy + (x^2 y + xe^{xz})\,dz$.
>
> **(b)** $d\omega = (1 - x e^{xy})\,dx \wedge dy$.
>
> **(c)** $d\omega = 3\,dx \wedge dy \wedge dz$. $d^2\omega = 0$ trivially since $d\omega$ is top-degree on $\mathbb{R}^3$ and $\Omega^4(\mathbb{R}^3) = 0$.
>
> **(d)** $d\omega = (\partial_x g - \partial_y f)\,dx \wedge dy$. Closed iff $\partial_x g = \partial_y f$.
>
> **(e)** $d\omega = (\partial_y w - \partial_z v)\,dy\wedge dz + (\partial_z u - \partial_x w)\,dz\wedge dx + (\partial_x v - \partial_y u)\,dx\wedge dy$, which is the curl of $(u, v, w)$ in $2$-form representation.
>
> $\blacksquare$

---

# Key Takeaways

**Computing $d\omega$ is mechanical bookkeeping, but the bookkeeping matters.** The two error sources are (1) forgetting that $dx^i \wedge dx^i = 0$ — leaving repeated-index terms in the answer — and (2) failing to reorder wedge products into increasing-multi-index form. Each reordering can flip a sign, and a missed sign is a wrong answer. The discipline is: as you compute each $d\omega_I \wedge dx^I$, immediately put the wedge into increasing form, tracking signs. This habit pays off in higher-dimensional or higher-degree computations where the bookkeeping explodes.

**The closedness test for a $1$-form on $\mathbb{R}^2$ is "$\partial_x g = \partial_y f$".** This is the exactness condition from elementary ODE for the form $f\,dx + g\,dy = dF$: it is equivalent to the mixed partials of $F$ being equal, which is Schwarz's theorem. Beginners learning ODE recognize this as "the integrability condition for $\omega = 0$"; the differential-geometer recognizes it as "closedness of the $1$-form $\omega$"; the de Rham theorist recognizes it as "the test for whether $\omega$ represents a nonzero class in $H^1_{dR}$". All three are the same condition.

**Top-degree forms on $\mathbb{R}^n$ always have $d = 0$, automatically.** Since $\Omega^{n+1}(\mathbb{R}^n) = 0$, the exterior derivative of any $n$-form on $\mathbb{R}^n$ is zero — for trivial reasons, not because of any cancellation. So every $n$-form on an $n$-manifold is closed; the question of whether it is exact is non-trivial and depends on the topology of the manifold (the top de Rham cohomology $H^n_{dR}(M)$). On a compact connected oriented $n$-manifold, $H^n_{dR}(M) \cong \mathbb{R}$ by de Rham's theorem, so exactness fails for any nonzero $n$-form. This is what makes the integral $\int_M\omega$ a meaningful cohomological invariant.

**Curl is $d$ on $1$-forms in $\mathbb{R}^3$ — and the cyclic permutation of $dy, dz, dx$ in the answer is built into the structure.** When computing $d$ of a $1$-form $u\,dx + v\,dy + w\,dz$ on $\mathbb{R}^3$, the answer naturally appears in the basis $\{dy \wedge dz, dz \wedge dx, dx \wedge dy\}$ — the cyclic permutations of $(x, y, z)$. The coefficients are $(\partial_y w - \partial_z v, \partial_z u - \partial_x w, \partial_x v - \partial_y u)$, exactly the components of the curl. The cyclic pattern is what makes the curl "look like a vector field", and it is also the source of the right-hand-rule convention. This pattern generalizes to any [[Def - Dimension|dimension]]: in $\mathbb{R}^n$, $d$ on $1$-forms produces a $2$-form with $\binom{n}{2}$ components, indexed by pairs of coordinates, with the appropriate cyclic sign pattern.
