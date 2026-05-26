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

# Statement

> **Theorem (Goursat).** Let $U \subseteq \mathbb{C}$ be open and $f : U \to \mathbb{C}$ holomorphic. Then for every closed triangle $T \subseteq U$ (the convex hull of three points, lying in $U$ together with its interior):
> $$\int_{\partial T} f(z)\,dz = 0,$$
> where $\partial T$ is the boundary of $T$ traversed once counterclockwise.
>
> **(Extended form.)** The conclusion still holds under the weaker hypothesis that $f$ is continuous on $U$ and holomorphic on $U \setminus S$ for some finite set $S \subseteq U$.

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

Let $T = T_0$ have vertices $A, B, C \in \mathbb{C}$ in counterclockwise order, and define the three midpoints
$$M_{AB} = \tfrac{A+B}{2}, \qquad M_{BC} = \tfrac{B+C}{2}, \qquad M_{CA} = \tfrac{C+A}{2}.$$
The medial subdivision splits $T$ into four congruent sub-triangles (each with sides half as long):
$$T^{(1)} = \mathrm{conv}\{A,\, M_{AB},\, M_{CA}\}, \quad T^{(2)} = \mathrm{conv}\{M_{AB},\, B,\, M_{BC}\},$$
$$T^{(3)} = \mathrm{conv}\{M_{CA},\, M_{BC},\, C\}, \quad T^{(4)} = \mathrm{conv}\{M_{AB},\, M_{BC},\, M_{CA}\}\text{ (central, reversed orientation).}$$
With each $\partial T^{(i)}$ traversed counterclockwise, every edge of $T^{(4)}$ — namely $\overline{M_{AB} M_{BC}}$, $\overline{M_{BC} M_{CA}}$, $\overline{M_{CA} M_{AB}}$ — also appears as an edge of exactly one of $T^{(1)}, T^{(2)}, T^{(3)}$, but parametrised in the *opposite* direction. The three outer edges of $\partial T$ are split by the midpoints into the six edges $\overline{A\,M_{AB}}, \overline{M_{AB}\,B}, \overline{B\,M_{BC}}, \overline{M_{BC}\,C}, \overline{C\,M_{CA}}, \overline{M_{CA}\,A}$, each appearing once. Summing the four sub-boundary integrals, interior edges cancel pairwise by the orientation reversal $\int_{\overline{pq}} f \,dz = -\int_{\overline{qp}} f\,dz$, leaving only the original outer edges:
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
> **Statement:** For $T = \mathrm{conv}\{A, B, C\}$ with midpoints $M_{AB}, M_{BC}, M_{CA}$ and the four sub-triangles $T^{(1)}, \ldots, T^{(4)}$ defined above, $\int_{\partial T} f\,dz = \sum_{i=1}^4 \int_{\partial T^{(i)}} f\,dz$.
>
> **Hint:** Each interior edge appears in two sub-boundaries with opposite parametrisations and cancels.
>
> > [!note]- Full proof
> > Parametrise the segment $\overline{pq}$ by $\gamma_{pq}(t) = p + t(q-p)$, $t \in [0,1]$, so that $\int_{\overline{pq}} f\,dz = (q - p)\int_0^1 f(p + t(q-p))\,dt = -\int_{\overline{qp}} f\,dz$ (substitution $t \mapsto 1 - t$). Write each $\int_{\partial T^{(i)}} f\,dz$ as a sum of three segment integrals:
> > $$\int_{\partial T^{(1)}} = \int_{\overline{A M_{AB}}} + \int_{\overline{M_{AB} M_{CA}}} + \int_{\overline{M_{CA} A}},$$
> > $$\int_{\partial T^{(2)}} = \int_{\overline{M_{AB} B}} + \int_{\overline{B M_{BC}}} + \int_{\overline{M_{BC} M_{AB}}},$$
> > $$\int_{\partial T^{(3)}} = \int_{\overline{M_{CA} M_{BC}}} + \int_{\overline{M_{BC} C}} + \int_{\overline{C M_{CA}}},$$
> > $$\int_{\partial T^{(4)}} = \int_{\overline{M_{AB} M_{BC}}} + \int_{\overline{M_{BC} M_{CA}}} + \int_{\overline{M_{CA} M_{AB}}}.$$
> > The three interior edges $\overline{M_{AB} M_{BC}}$, $\overline{M_{BC} M_{CA}}$, $\overline{M_{CA} M_{AB}}$ each appear once in this list with one orientation and once with the opposite, so cancel pairwise. The remaining six terms are the six halves of $\partial T$ in counterclockwise order:
> > $$\int_{\overline{A M_{AB}}} + \int_{\overline{M_{AB} B}} + \int_{\overline{B M_{BC}}} + \int_{\overline{M_{BC} C}} + \int_{\overline{C M_{CA}}} + \int_{\overline{M_{CA} A}} = \int_{\partial T} f\,dz. \;\blacksquare$$

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

> [!note]- Axis-aligned rectangle variant (coordinate-explicit alternative)
> The same nesting-and-quadratic-estimate proof works for an axis-aligned rectangle $R_0 = [a, b] \times [c, d] \subseteq U$ in place of a triangle, with strictly coordinate arithmetic and no medial geometry. State $\int_{\partial R_0} f\,dz = 0$ for any closed rectangle in $U$ — this version of Goursat suffices to upgrade to all later Cauchy theorems via primitive constructions on rectangle-decomposable domains.
>
> **Subdivision.** Set $m = (a+b)/2$, $n = (c+d)/2$, and define the four congruent closed sub-rectangles
> $$R^{(1)} = [a, m] \times [c, n], \quad R^{(2)} = [m, b] \times [c, n], \quad R^{(3)} = [m, b] \times [n, d], \quad R^{(4)} = [a, m] \times [n, d].$$
> Each $\partial R^{(i)}$ is traversed counterclockwise. The interior horizontal segment $[a, b] \times \{n\}$ decomposes as $[a, m] \times \{n\}$ (shared by $R^{(1)}$ top and $R^{(4)}$ bottom — opposite parametrisations) and $[m, b] \times \{n\}$ (shared by $R^{(2)}$ top and $R^{(3)}$ bottom). The interior vertical segment $\{m\} \times [c, d]$ similarly decomposes into two halves with opposite parametrisations. So all four interior segments cancel pairwise and
> $$\int_{\partial R_0} f\,dz = \sum_{i=1}^4 \int_{\partial R^{(i)}} f\,dz.$$
>
> **Iteration.** Pick the sub-rectangle $R^{(i)}$ with $|\int_{\partial R^{(i)}} f\,dz| \geq |I|/4$ and call it $R_1$. Iterating, get nested $R_0 \supseteq R_1 \supseteq R_2 \supseteq \cdots$ with perimeters $L(\partial R_n) = L(\partial R_0)/2^n$ and $|\int_{\partial R_n} f\,dz| \geq |I|/4^n$.
>
> **Shrinking.** $\bigcap_n R_n$ is a single point $w$ by the nested-interval theorem applied separately to the $x$- and $y$-coordinates: the $x$-intervals $[a_n, b_n]$ shrink to a point because $b_n - a_n = (b-a)/2^n \to 0$, and likewise the $y$-intervals.
>
> **Linearisation.** Identical to the triangle case: $|f(z) - f(w) - f'(w)(z - w)| \leq \varepsilon|z - w|$ on $R_n$ for large $n$, and the linear part has a primitive so integrates to zero around the closed $\partial R_n$. ML gives $|\int_{\partial R_n} f\,dz| \leq \varepsilon \cdot L(\partial R_n) \cdot (\text{diam}\, R_n) \leq \varepsilon L(\partial R_0)^2 / 4^n$, hence $|I| \leq \varepsilon L(\partial R_0)^2$ for any $\varepsilon$, so $I = 0$.
>
> The rectangle version is strictly more convenient when $U$ is decomposed in coordinate language (intersections of half-planes, products of intervals); the triangle version is more convenient when the natural subdivision is barycentric. The two are equivalent statements about complex differentiability.

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
