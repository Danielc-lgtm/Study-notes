---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Local Mapping Degree"
  - "Thm - Argument Principle"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ is open (a domain), $f : U \to \mathbb{C}$ is holomorphic and non-constant. An **open map** sends open sets to open sets. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

The open mapping theorem says: a non-constant holomorphic function on a domain $U$ is an **open map** — it sends open sets in $U$ to open sets in $\mathbb{C}$. This means images of holomorphic functions are *not flattened*: they have full 2-dimensional "thickness" wherever they are defined.

This is in stark contrast to real differentiable functions: $f(x) = x^2$ on $\mathbb{R}$ maps the open interval $(-1, 1)$ to the half-closed interval $[0, 1)$, *not* an open set. The squaring "folds back" the real line, and the image loses dimension at the fold point.

The open mapping theorem says this folding cannot happen for holomorphic functions. Geometrically, a holomorphic function — being locally conformal except where $f' = 0$ — preserves the 2D "thickness" everywhere. Even at points where $f' = 0$, the function locally looks like $z^k$, which is *still* an open map on $\mathbb{C}$ (it wraps a small disc around $0$ to a larger disc covered $k$ times, but the image is still open).

This is one of the deepest structural facts in complex analysis. It underlies the **maximum modulus principle** (a non-constant holomorphic function cannot have a local max of $|f|$ in the interior, because the image is open and thus has nearby points with larger modulus). It is the source of the **identity theorem** in many cases. It is the geometric reason why holomorphic functions are *qualitatively* different from real differentiable functions.

---

# Sources and Targets

**Sources (Input Broadening)**

**Non-constant holomorphic $f$ on a domain.** Property $B$: standard hypothesis.

**Holomorphic $f$ with $f'(z) \neq 0$ at one point.** Property $B$: weaker hypothesis (just at one point). Bridge: $f$ non-constant; by the [[Thm - Holomorphic Inverse Function Theorem|inverse function theorem]], $f$ is locally a biholomorphism near that point, hence open.

**Holomorphic $f$ with isolated critical points.** Property $B$: $f' = 0$ at isolated points only. Bridge: even at critical points, $f$ has a power-series expansion $f(z) - f(a) = (z - a)^k g(z)$ with $g(a) \neq 0$, and is locally $k$-to-$1$ — still open.

**Targets (Output Amplification)**

Combine with **boundary values constraint.** Property $D$: $|f|$ has a local max in the interior. Amplified result $E$: contradiction (open image must have nearby points with larger modulus), so $f$ is constant. This is the **maximum modulus principle**.

Combine with **isolated singularities of $1/(f - w_0)$.** Property $D$: $w_0$ not in the image of $f$. Amplified result $E$: by openness of the image, $w_0$ is on the boundary of $f(U)$, with specific structural implications.

Combine with **the Riemann mapping theorem proof.** Property $D$: extremal $f : U \to \mathbb{D}$ with $|f'(z_0)|$ maximal. Amplified result $E$: $f$ is surjective onto $\mathbb{D}$ (open mapping plus the extremality argument).

---

# Why Is It True

The intuition is captured by the local mapping degree. At any $z_0 \in U$, write the Taylor expansion of $f - f(z_0)$ as $f(z) - f(z_0) = (z - z_0)^k g(z)$ with $g(z_0) \neq 0$ and $k \geq 1$ (the order of the zero of $f - f(z_0)$ at $z_0$).

Locally, $f$ behaves like the map $w \mapsto w^k$ near $0$: it takes a small disc $|z - z_0| < r$ to a region covering a disc around $f(z_0)$, with each interior point covered $k$ times. The image is open because $w \mapsto w^k$ on a small disc around $0$ produces an open disc image (it's a $k$-to-$1$ covering of the disc image).

More formally, the [[Thm - Local Mapping Degree|local mapping degree theorem]] says: for $w$ sufficiently close to $f(z_0)$, the equation $f(z) = w$ has *exactly* $k$ solutions near $z_0$. So for every $w$ near $f(z_0)$, there is at least one $z$ near $z_0$ with $f(z) = w$. This means $f(U)$ contains a neighborhood of $f(z_0)$ — exactly the definition of "openness".

For the global statement: take any open $V \subseteq U$ and $w_0 \in f(V)$. Choose $z_0 \in V$ with $f(z_0) = w_0$. By the local argument, $f$ contains a neighborhood of $w_0$ in $f(V \cap (\text{small disc around } z_0)) \subseteq f(V)$. So every point of $f(V)$ has a neighborhood in $f(V)$, i.e., $f(V)$ is open.

---

# What Makes This Hard

The non-obvious step is the **local mapping degree** at critical points. At points where $f' \neq 0$, openness follows from the inverse function theorem trivially. The interesting case is $f'(z_0) = 0$, where the inverse function theorem doesn't apply directly. The trick is to factor $f - f(z_0) = (z - z_0)^k g(z)$ and recognize this as locally $z \mapsto z^k$ behavior. A common mistake is to assume $f'$ must be nonzero everywhere; the open mapping theorem holds even at critical points, just by a more subtle argument.

---

# Rederivation Scaffold

**High-level strategy:**
For any $z_0 \in U$ and the corresponding $w_0 = f(z_0)$, apply the local mapping degree theorem: $f$ is locally $k$-to-$1$ near $z_0$, so $f$ covers a neighborhood of $w_0$. Hence $f(U)$ contains a neighborhood of $w_0$. Since $w_0$ was arbitrary in $f(U)$, $f(U)$ is open. Apply to any open $V \subseteq U$.

**Subgoal decomposition:**

1. **Take $V \subseteq U$ open, $w_0 \in f(V)$.** Choose $z_0 \in V$ with $f(z_0) = w_0$.

2. **Apply local mapping degree.** Near $z_0$, $f(z) - w_0$ has a zero of order $k \geq 1$. By [[Thm - Local Mapping Degree|local mapping degree]], for $w$ near $w_0$, the equation $f(z) = w$ has $k$ solutions near $z_0$. So $f$ maps a small open neighborhood of $z_0$ surjectively onto a small open neighborhood of $w_0$.

3. **Conclude $f(V)$ contains a neighborhood of $w_0$.** Since $V$ is open, the small neighborhood of $z_0$ is inside $V$ (for $V$ sufficiently small around $z_0$), and the image contains a neighborhood of $w_0$.

4. **$w_0$ arbitrary ⟹ $f(V)$ open.**

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f : U \to \mathbb{C}$ be non-constant holomorphic on a domain $U$. Let $V \subseteq U$ be open; we show $f(V)$ is open.
>
> Take any $w_0 \in f(V)$ and choose $z_0 \in V$ with $f(z_0) = w_0$. Since $f$ is non-constant and holomorphic, $f - w_0$ is a non-constant holomorphic function with $f(z_0) - w_0 = 0$. The zero at $z_0$ has some finite order $k \geq 1$.
>
> By the [[Thm - Local Mapping Degree|local mapping degree theorem]], there exists $r > 0$ such that for every $w$ with $|w - w_0|$ sufficiently small, the equation $f(z) = w$ has exactly $k$ solutions in $D(z_0, r)$ (counted with multiplicity). For $w \neq w_0$ in this small disc, the solutions are distinct simple zeros (provided $r$ is small enough that $f' \neq 0$ on $D(z_0, r) \setminus \{z_0\}$).
>
> So there exists $\epsilon > 0$ such that $D(w_0, \epsilon) \subseteq f(D(z_0, r))$. Choosing $r$ small enough that $D(z_0, r) \subseteq V$, we have $D(w_0, \epsilon) \subseteq f(V)$.
>
> Since $w_0$ was an arbitrary point of $f(V)$, $f(V)$ is open. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Maximum modulus principle.** If $f$ is holomorphic and non-constant on a domain $D$, and $|f|$ has a local maximum at $z_0 \in D$, then... wait, this should be a contradiction. Suppose $|f|$ has a local max at $z_0$. By open mapping, $f(D)$ contains a neighborhood of $f(z_0)$, hence points $w$ with $|w| > |f(z_0)|$. But these are images of points in $D$ near $z_0$, contradicting the local max. So $f$ must be constant on $D$.

**Holomorphic functions $\mathbb{C} \to \mathbb{R}$ are constant.** Suppose $f : \mathbb{C} \to \mathbb{C}$ is holomorphic and all values are real. Then $f(\mathbb{C}) \subseteq \mathbb{R}$, which is not open in $\mathbb{C}$. By open mapping, $f$ must be constant.

**Schwarz reflection principle.** A holomorphic function on the upper half-plane, continuous up to the real boundary and real-valued there, extends to a holomorphic function on $\mathbb{C}$ by reflection across $\mathbb{R}$. The open mapping theorem rules out wild boundary behaviour.

---

# Bridges

- **[[Thm - Local Mapping Degree]]** — provides the local structure used in the proof.

- **[[Thm - Argument Principle]]** — underlies local mapping degree.

- **[[Thm - Holomorphic Inverse Function Theorem]]** — the case $k = 1$ (no critical point).

- **Maximum modulus principle** (in CA II) — a direct corollary.

---

# Unlocked by This

> [!tip] Maximum Modulus Principle *(from §3.5+)*
> Open mapping ⟹ non-constant holomorphic functions have no interior maximum of $|f|$.

> [!tip] Schwarz Lemma and Bounds on $|f|$ *(from §3.5+)*
> [[Thm - Schwarz Lemma|Schwarz's lemma]] uses the open mapping theorem indirectly (via maximum modulus on $f(z)/z$).

> [!tip] Riemann Mapping Theorem *(from §3.5+)*
> The proof of [[Thm - Riemann Mapping Theorem (Statement)|Riemann mapping]] uses open mapping for the surjectivity argument.
