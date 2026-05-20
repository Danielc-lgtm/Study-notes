---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Argument Principle"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$f : D(a, R) \to \mathbb{C}$ holomorphic; $k = \operatorname{ord}_a(f - f(a))$ is the order of the zero of $f(z) - f(a)$ at $z = a$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Local Mapping Degree).** Let $f$ be holomorphic on $D(a, R)$, set $w_0 := f(a)$, and let $k \geq 1$ be the order of the zero of $f - w_0$ at $a$ (so $f(z) - w_0 = (z - a)^k g(z)$ with $g$ holomorphic and $g(a) \neq 0$). Then there exist $r, \delta > 0$ such that for every $w$ with $0 < |w - w_0| < \delta$, the equation $f(z) = w$ has exactly $k$ solutions in $D(a, r)$, and all of them are simple (i.e., $f'(z) \neq 0$ at each solution).
>
> Equivalently, on a small punctured neighbourhood, $f$ is a $k$-to-$1$ covering of a punctured neighbourhood of $w_0$.

---

# Motivation

How does a holomorphic function look locally near a point? If $f'(a) \neq 0$, the holomorphic inverse function theorem says $f$ is locally a biholomorphism — a neighborhood of $a$ is mapped bijectively to a neighborhood of $f(a)$. But what if $f'(a) = 0$?

The local mapping degree theorem handles this case. It says: even at critical points (where $f'(a) = 0$), the function $f$ has a well-defined *local degree* $k$, equal to the order of the zero of $f - f(a)$ at $a$. Locally, $f$ behaves like the map $w \mapsto w^k$ near $0$: it covers a small punctured neighborhood of $f(a)$ exactly $k$ times.

This gives a complete local classification of holomorphic functions: at every point, $f$ is locally either a biholomorphism (if $k = 1$) or a degree-$k$ covering of a small disc (if $k \geq 2$). There is no "folding back" or wilder behaviour — holomorphic functions are locally surprisingly tame.

The local mapping degree is also the key input to the open mapping theorem (a non-constant holomorphic function is an open map) and the maximum modulus principle.

---

# Sources and Targets

**Sources (Input Broadening)**

**$f$ holomorphic with $f'(a) \neq 0$.** Property $B$: $k = 1$. Bridge: by the [[Thm - Holomorphic Inverse Function Theorem|inverse function theorem]], $f$ is locally a biholomorphism near $a$, hence $1$-to-$1$ near $a$.

**$f$ holomorphic with $f - f(a) = (z - a)^k g(z), g(a) \neq 0$.** Property $B$: explicit factorization shows $k$. Bridge: directly read off the local degree.

**$f = z^n$ near $z = 0$.** Property $B$: $k = n$. Bridge: prototypical case.

**Targets (Output Amplification)**

Combine with **the open mapping theorem.** Property $D$: open subset of $U$. Amplified result $E$: image is open ([[Thm - Open Mapping Theorem|open mapping]]).

Combine with **counting preimages.** Property $D$: $f$ holomorphic, $w$ a regular value. Amplified result $E$: counting preimages of $w$ via the local degree at each preimage. Used in Riemann surface theory and the *Riemann–Hurwitz formula*.

Combine with **branched coverings.** Property $D$: $f : X \to Y$ holomorphic between Riemann surfaces. Amplified result $E$: the local degree pattern is the "branching profile" — used to compute global topological invariants.

---

# Why Is It True

The argument uses the argument principle applied to $f(z) - w$ for $w$ near $f(a)$.

Write $f(z) - f(a) = (z - a)^k g(z)$ with $g(a) \neq 0$. Choose a small disc $|z - a| \leq r$ where $g \neq 0$ (so the zero of $f - f(a)$ at $a$ is the only zero in this disc, of order $k$). Also choose $r$ small enough that $f'(z) \neq 0$ for $0 < |z - a| \leq r$ — possible because $f'$ is holomorphic with isolated zeros.

On the boundary circle $|z - a| = r$, $|f(z) - f(a)| \geq m > 0$ for some constant $m$. For $w$ with $|w - f(a)| < m$, the function $f(z) - w$ has no zeros on the boundary circle, and we can count its zeros in $|z - a| < r$ by the argument principle.

By Rouché-like reasoning: $|f - w - (f - f(a))| = |w - f(a)| < m \leq |f - f(a)|$ on the boundary. So $f - w$ has the same number of zeros as $f - f(a)$ in $|z - a| < r$, which is $k$.

Moreover, since $f' \neq 0$ on the punctured disc $0 < |z - a| \leq r$, the $k$ zeros are *simple* (each has multiplicity $1$): no two collide, no higher-order zero exists. So the $k$ solutions are distinct.

The conceptual content: *the local mapping degree is the order of the zero of $f - f(a)$ at $a$, and this many distinct solutions exist for $w$ near (but not equal to) $f(a)$*.

---

# What Makes This Hard

The non-obvious step is **using the argument principle (or Rouché) for the equation $f(z) = w$**, treating $w$ as a variable. The trick is to fix a small disc, compare $f - w$ to $f - f(a)$ on the boundary, and conclude the zero counts agree. Common mistakes: forgetting that the $k$ solutions are distinct simple zeros (this requires $f' \neq 0$ on the punctured disc); confusing the "local degree" with the order of $f' = 0$ (these differ by $1$: $\operatorname{ord}_a(f - f(a)) = k$ corresponds to $\operatorname{ord}_a f' = k - 1$).

---

# Rederivation Scaffold

**High-level strategy:**
On a small disc around $a$, the function $f - f(a)$ has exactly one zero (at $a$, of order $k$). For $w$ near $f(a)$, Rouché-type comparison shows $f - w$ has the same zero count, namely $k$. The non-vanishing of $f'$ on the punctured disc makes these $k$ zeros distinct simple.

**Subgoal decomposition:**

1. **Local factorization.** $f(z) - f(a) = (z - a)^k g(z)$ with $g$ holomorphic and $g(a) \neq 0$.

2. **Choose small disc $|z - a| \leq r$.** Such that: (a) $g \neq 0$ on the disc; (b) $f'$ has no zeros on the *punctured* disc $0 < |z - a| \leq r$.

3. **Bound $|f - f(a)|$ on the boundary.** $|f(z) - f(a)| = |z - a|^k|g(z)| \geq r^k \min|g| > 0$ on $|z - a| = r$. Let $m = r^k\min|g|$.

4. **For $|w - f(a)| < m$, apply Rouché.** $|f - w - (f - f(a))| = |w - f(a)| < m \leq |f - f(a)|$ on $|z - a| = r$. So $f - w$ has the same number of zeros as $f - f(a)$ in the disc, namely $k$ (counted with multiplicity).

5. **Simple zeros.** For $w \neq f(a)$, the zeros of $f - w$ avoid $a$ (where $f(a) - w \neq 0$), so they are in the punctured disc where $f' \neq 0$, hence simple.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : D(a, R) \to \mathbb{C}$ be holomorphic, $f(a) = w_0$, and let $k = \operatorname{ord}_a(f - w_0) \geq 1$ be the order of the zero. So $f(z) - w_0 = (z - a)^k g(z)$ for some $g$ holomorphic with $g(a) \neq 0$.
>
> **Step 1.** By continuity of $g$, choose $r > 0$ such that:
> - $g(z) \neq 0$ on $D(a, r)$;
> - $f'(z) \neq 0$ for $0 < |z - a| \leq r$ (possible because $f'$ is holomorphic and its zeros are isolated — including the zero at $a$ if $k \geq 2$).
>
> **Step 2.** Set $m := \min_{|z - a| = r}|f(z) - w_0| = r^k \min_{|z - a| = r}|g(z)| > 0$.
>
> **Step 3.** For any $w$ with $0 < |w - w_0| < m$: on the boundary $|z - a| = r$,
> $$|(f - w) - (f - w_0)| = |w_0 - w| < m \leq |f - w_0|.$$
> By [[Thm - Rouché's Theorem|Rouché's theorem]], $f - w$ and $f - w_0$ have the same number of zeros in $|z - a| < r$. The latter has a zero of order $k$ at $a$, so $f - w$ has $k$ zeros (counted with multiplicity) in $D(a, r)$.
>
> **Step 4.** For $w \neq w_0$, the $k$ zeros of $f - w$ are not at $a$ (since $f(a) - w = w_0 - w \neq 0$), so they lie in the punctured disc $0 < |z - a| < r$. There $f' \neq 0$, so the zeros are simple (no multiple zeros). Hence $f - w$ has exactly $k$ *distinct* zeros in $D(a, r)$.
>
> **Conclusion.** For $w$ near (but not equal to) $w_0$, the equation $f(z) = w$ has exactly $k$ solutions in $D(a, r)$, all simple. The map $f$ is locally $k$-to-$1$ near $a$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Open mapping consequence.** For any $w$ in the image of $f$ on a small disc, $f$ takes $k$ different values near $a$ — confirming the image contains a neighborhood of $f(a)$.

**Branched coverings of Riemann surfaces.** A holomorphic map between compact Riemann surfaces is a *branched cover*: away from finitely many critical points, it is locally a biholomorphism; at critical points, it has local degree $k > 1$. The branching profile (the distribution of local degrees at critical points) determines the topology of the cover via the *Riemann–Hurwitz formula*.

**$z \mapsto z^n$ on the unit disc.** Local degree at $z = 0$ is $n$; everywhere else (where $z \neq 0$), the local degree is $1$. So the unit disc maps to itself, $n$-to-$1$ over each nonzero point, with a single critical point at the origin of degree $n$.

---

# Bridges

- **[[Thm - Argument Principle]]** — used to count zeros of $f - w$.

- **[[Thm - Rouché's Theorem]]** — for the comparison argument.

- **[[Thm - Open Mapping Theorem]]** — direct consequence.

- **[[Thm - Holomorphic Inverse Function Theorem]]** — the $k = 1$ case.

---

# Unlocked by This

> [!tip] Riemann–Hurwitz Formula *(from Algebraic Geometry)*
> The **Riemann–Hurwitz formula** relates the genera of two Riemann surfaces connected by a branched holomorphic map, in terms of the degree and branching. Local mapping degree is the local input; Riemann–Hurwitz is the global topological output.

> [!tip] Holomorphic Dynamics *(from Complex Dynamics)*
> In iterated holomorphic dynamics, the **critical orbit** (the orbit of points where $f' = 0$) controls the dynamics, via the local mapping degree at the critical points.
