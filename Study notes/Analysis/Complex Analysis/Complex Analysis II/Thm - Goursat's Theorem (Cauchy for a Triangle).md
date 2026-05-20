---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Contour Integral"
  - "Thm - ML Estimate"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ open; $f : U \to \mathbb{C}$ holomorphic on $U$. $T \subseteq U$ a *closed* triangle (the convex hull of three points, including its interior). $\partial T$ denotes the boundary, traversed counterclockwise. $L = L(\partial T)$, the perimeter. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Motivation

Goursat's theorem is the *building block* of Cauchy's theorem. The most basic possible closed curve is a triangle, and the most basic statement of "the integral of a holomorphic function around a closed curve is zero" is the one for triangles. Once Goursat is proved, Cauchy's theorem on more general domains follows by approximating closed curves with polygonal paths and decomposing into triangles.

The remarkable feature of Goursat is that it requires only *complex differentiability* of $f$ (no further regularity), and the proof is purely topological-combinatorial: subdivide the triangle, find one with $\geq 1/4$ the integral, iterate, shrink to a point. There is no use of Stokes' theorem, no use of $C^1$ partial derivatives — just the linearization of $f$ at a point.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$f$ holomorphic on an open set containing the closed triangle $T$".

The first disguised source is **$f$ continuous on $U$, holomorphic except at finitely many isolated points**: the theorem extends (Theorem 2.2.2 in Cambridge IB) to this case. The proof handles isolated bad points by shrinking sub-triangles. *Example:* $1/z$ is holomorphic on $\mathbb{C}^\times$, and any triangle not containing $0$ has $\int_{\partial T} dz/z = 0$.

**Targets (Output Amplification)**

The conclusion is "$\int_{\partial T} f\,dz = 0$".

Combine with **the existence of primitives on star-shaped domains.** Property $D$: $U$ star-shaped. The amplified result: by the construction in Lemma 2.1.6, $f$ has a primitive on $U$. This bootstraps Goursat to [[Thm - Cauchy's Theorem for a Star-Shaped Domain]].

Combine with **bootstrapping to closed curves.** Property $D$: an arbitrary closed curve in a star-shaped domain. The amplified result: $\int_\gamma f\,dz = 0$ (since a primitive exists).

---

# Why Is It True

Bisect $T$ into four sub-triangles by joining the midpoints of the sides. The integrals along the *interior* edges cancel (each edge is traversed twice, in opposite directions), so the integral around $\partial T$ equals the sum of integrals around the four sub-boundaries:
$$\int_{\partial T} f\,dz = \sum_{i=1}^4 \int_{\partial T^{(i)}} f\,dz.$$
By the triangle inequality, *some* sub-triangle has $|\int_{\partial T^{(i)}} f\,dz| \geq |I|/4$ where $I = \int_{\partial T} f\,dz$. Pick that one, call it $T_1$; iterate to get $T_2$ (a sub-sub-triangle with $|\int_{\partial T_2}| \geq |I|/16$); and so on.

The nested triangles $T \supseteq T_1 \supseteq T_2 \supseteq \ldots$ have perimeters $L(\partial T_n) = L/2^n$ and shrink to a single point $w \in T$ (by compactness: nested non-empty closed sets in a metric space with diameters $\to 0$ have a unique common point).

Near $w$, the local linearization of $f$: $f(z) = f(w) + f'(w)(z - w) + g(z)$ where $g(z) = o(|z - w|)$ as $z \to w$ — i.e., for any $\varepsilon > 0$, $|g(z)| \leq \varepsilon |z - w|$ for $z$ close enough to $w$.

The integrals around closed triangles of the *linear* terms vanish:
$$\int_{\partial T_n} f(w)\,dz = 0 \quad (\text{primitive of constant}: f(w)z),$$
$$\int_{\partial T_n} f'(w)(z - w)\,dz = 0 \quad (\text{primitive}: f'(w)(z - w)^2/2).$$
So only the $g$-contribution remains:
$$\int_{\partial T_n} f\,dz = \int_{\partial T_n} g(z)\,dz.$$
By ML and $|g(z)| \leq \varepsilon|z - w| \leq \varepsilon L(\partial T_n) = \varepsilon L/2^n$:
$$\left|\int_{\partial T_n} f\,dz\right| \leq \varepsilon \cdot \frac{L}{2^n} \cdot \frac{L}{2^n} = \frac{\varepsilon L^2}{4^n}.$$

So $|I|/4^n \leq |\int_{\partial T_n} f\,dz| \leq \varepsilon L^2 / 4^n$, hence $|I| \leq \varepsilon L^2$. Since $\varepsilon$ is arbitrary, $|I| = 0$. $\blacksquare$

The deep observation: holomorphicity at $w$ provides a *quadratic* (in length scale) estimate of $|f(z) - f(w) - f'(w)(z - w)|$, which beats the linear (in length scale) growth of the contour. The factor $4^n$ in the iteration is exactly matched by the factor $L^2/4^n$ in the estimate.

---

# What Makes This Hard

The non-obvious step is the *subdivision-iteration argument* with the factor $\geq 1/4$ trick, combined with the *quadratic* error estimate from holomorphicity. The trick is to extract a small region where the linearization holds with arbitrary precision, then use ML on a shrinking contour with arbitrarily good error to push the integral to zero. The common error is to expect the proof to use $C^1$ partials (it does not — it uses only complex differentiability).

---

# Rederivation Scaffold

**High-level strategy:**
Bisect, pick the sub-triangle with $\geq 1/4$ the integral, iterate. The nested triangles shrink to a point $w$. Near $w$, use the holomorphic linearization to bound the integral by $\varepsilon L^2/4^n$. Conclude $|I| \leq \varepsilon L^2$ for any $\varepsilon$.

**Subgoal decomposition:**

1. **Bisection step.** Show $\int_{\partial T} f\,dz = \sum \int_{\partial T^{(i)}} f\,dz$ (interior edges cancel).
2. **Iteration.** Build nested $T = T_0 \supseteq T_1 \supseteq T_2 \supseteq \ldots$ with $|\int_{\partial T_n} f| \geq |I|/4^n$ and $L(\partial T_n) = L/2^n$.
3. **Shrinking to a point.** $\bigcap T_n = \{w\}$.
4. **Holomorphic estimate at $w$.** $|f(z) - f(w) - f'(w)(z - w)| \leq \varepsilon|z - w|$ on $T_n$ for $n$ large.
5. **Apply ML and conclude.** $|\int_{\partial T_n} f\,dz| \leq \varepsilon L^2/4^n$; hence $|I| \leq \varepsilon L^2$; hence $|I| = 0$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Bisection identity
> **Statement:** Subdividing $T$ into four sub-triangles via the midpoints, $\int_{\partial T} f\,dz = \sum_{i=1}^4 \int_{\partial T^{(i)}} f\,dz$.
>
> **Hint:** Interior edges are traversed twice, in opposite directions, and cancel.
>
> > [!note]- Full proof
> > The four sub-triangles share three interior edges: the segments connecting the midpoints. Each interior edge is part of two sub-boundaries, traversed once each, in opposite directions (by the counterclockwise orientation of all four sub-triangles). So the line integrals of $f$ along the interior edges cancel pairwise in the sum, leaving only the integrals along the original outer boundary $\partial T$. $\blacksquare$

> [!note]- Lemma 2: Holomorphic linearization
> **Statement:** If $f$ is holomorphic at $w$, then for any $\varepsilon > 0$ there is $\delta > 0$ such that $|f(z) - f(w) - f'(w)(z - w)| \leq \varepsilon |z - w|$ for $|z - w| < \delta$.
>
> > [!note]- Full proof
> > By definition of $f'(w)$: $(f(z) - f(w))/(z - w) \to f'(w)$ as $z \to w$. So for $\varepsilon > 0$, there is $\delta > 0$ with $|(f(z) - f(w))/(z - w) - f'(w)| < \varepsilon$ for $0 < |z - w| < \delta$. Multiplying by $|z - w|$: $|f(z) - f(w) - f'(w)(z - w)| \leq \varepsilon |z - w|$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Set $I = \int_{\partial T} f\,dz$. We show $I = 0$.
>
> **Iteration.** Apply Lemma 1: $I = \sum_{i=1}^4 I_i$ where $I_i = \int_{\partial T^{(i)}} f\,dz$. By the triangle inequality, $|I| \leq 4 \max_i |I_i|$, so some $i$ has $|I_i| \geq |I|/4$. Call that sub-triangle $T_1$. Iterating: $T \supseteq T_1 \supseteq T_2 \supseteq \ldots$ with $|\int_{\partial T_n} f\,dz| \geq |I|/4^n$ and $L(\partial T_n) = L(\partial T)/2^n = L/2^n$.
>
> **Shrinking.** Since each $T_n$ is closed and nonempty, and diameters tend to zero ($\leq L/2^n \to 0$), by compactness (e.g., Cantor's nested intervals applied in $\mathbb{R}^2$), $\bigcap_n T_n = \{w\}$ for some $w \in T$. $f$ is holomorphic at $w$.
>
> **Linearization.** Apply Lemma 2: for $\varepsilon > 0$, there is $\delta > 0$ such that $|f(z) - f(w) - f'(w)(z - w)| \leq \varepsilon |z - w|$ for $|z - w| < \delta$. Pick $n$ large enough that $T_n \subseteq D(w, \delta)$.
>
> **Reducing the integrand.** On $\partial T_n$:
> $$\int_{\partial T_n} f\,dz = \int_{\partial T_n} [f(w) + f'(w)(z - w) + g(z)]\,dz$$
> where $g(z) = f(z) - f(w) - f'(w)(z - w)$, $|g(z)| \leq \varepsilon |z - w|$. The first two terms have primitives ($f(w) z, f'(w)(z - w)^2/2$) and integrate to zero around the closed triangle. So $\int_{\partial T_n} f\,dz = \int_{\partial T_n} g\,dz$.
>
> **ML bound.** On $\partial T_n$, $|z - w| \leq L(\partial T_n) = L/2^n$, so $|g(z)| \leq \varepsilon L/2^n$. By [[Thm - ML Estimate]]:
> $$\left|\int_{\partial T_n} f\,dz\right| = \left|\int_{\partial T_n} g\,dz\right| \leq \frac{\varepsilon L}{2^n} \cdot \frac{L}{2^n} = \frac{\varepsilon L^2}{4^n}.$$
>
> **Conclude.** $|I|/4^n \leq |\int_{\partial T_n} f\,dz| \leq \varepsilon L^2/4^n$, so $|I| \leq \varepsilon L^2$. Since $\varepsilon$ was arbitrary, $|I| = 0$. $\blacksquare$
>
> **Extension to continuous on $U$, holomorphic on $U \setminus S$ for finite $S$.** If $T$ contains a single bad point $a$, subdivide $T$ so $a$ is in a tiny sub-triangle $T'$ with arbitrarily small perimeter; on $T \setminus T'$, $f$ is holomorphic and Goursat gives $0$; on $T'$, ML gives $|f| \cdot L(\partial T') \leq M \cdot \text{tiny}$, which goes to zero. Multiple bad points by repeated subdivision.

---

# Cross-Field Exercise Suggestions

**Goursat with finite singular set.** $f$ continuous on $U$, holomorphic on $U \setminus S$ for finite $S \subseteq U$. The theorem still gives $\int_{\partial T} f\,dz = 0$ for any triangle $T \subseteq U$. Application: to prove Cauchy integral formula, one writes $g(z) = (f(z) - f(w))/(z - w)$ which has a removable singularity at $w$; Goursat applied to $g$ (continuous at $w$, holomorphic elsewhere) gives the integral evaluation.

**Stokes' theorem as the conceptual parent.** Goursat is the elementary version of "the integral of a closed 1-form over the boundary of a region equals the integral of $d\omega$ over the region — which is zero for closed $\omega$". The hypothesis "f holomorphic" is the closedness of $f\,dz$ as a 1-form, and the conclusion is the special case of Stokes for triangles. Goursat does *not* use Stokes (the proof is elementary), but it captures the same content.

---

# Bridges

- **[[Thm - ML Estimate]]** — the bounding tool in the proof.

- **[[Thm - Cauchy's Theorem for a Star-Shaped Domain]]** — the natural upgrade. Goursat is the triangle case; the star-shaped case is built by using Goursat to verify a primitive.

- **[[Thm - Cauchy Integral Formula]]** — uses Goursat (in the continuous-except-at-a-point form) to evaluate.

- **[[Thm - Morera's Theorem]]** — the partial converse: vanishing of triangle integrals implies holomorphicity.
