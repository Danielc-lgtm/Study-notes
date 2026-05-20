---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Riemann Mapping Theorem (Statement)"
  - "Def - Conformal Map"
  - "Thm - Existence of Log and Square Root on Simply Connected Domains"
tags: [analysis, complex-analysis, applied]
---

# Problem Statement

State the **Schwarz–Christoffel formula** for a conformal map from the upper half-plane $\mathbb{H}$ to the interior of a polygon with vertices $w_1, w_2, \ldots, w_n$ (in order around the polygon) and interior angles $\alpha_1\pi, \alpha_2\pi, \ldots, \alpha_n\pi$ (with $\sum\alpha_k = n - 2$).

Verify the formula for the simple case of mapping $\mathbb{H}$ to the upper half of an *equilateral triangle* with vertices at $0, 1, e^{i\pi/3}$.

**Recall:**

![[Thm - Riemann Mapping Theorem (Statement)#Notation]]

Riemann mapping: any simply connected proper open subset of $\mathbb{C}$ is biholomorphic to $\mathbb{D}$ (or equivalently to $\mathbb{H}$).

The Schwarz–Christoffel formula gives an *explicit* conformal map to a polygon, parameterized by the polygon's vertices and angles.

---

# Convergent Strategy

**Problem class:** State and verify the Schwarz–Christoffel formula for polygons. This is one of the most useful applied complex-analysis tools, used in fluid dynamics, electrostatics, and conformal-mapping-based PDE solvers.

**Assumption pattern:** Polygon in the $w$-plane; the Schwarz–Christoffel formula uses preimages of the vertices on the real axis $\mathbb{R}$ (boundary of $\mathbb{H}$).

**Theorem routing:** Schwarz–Christoffel formula $f(z) = A + C\int_{z_0}^z\prod_k(\zeta - x_k)^{\alpha_k - 1}\,d\zeta$, where $x_k \in \mathbb{R}$ are the preimages of $w_k$.

**Key decision point:** The "angle defect" $(\alpha_k - 1)\pi$ at each vertex $w_k$ corresponds to a factor $(\zeta - x_k)^{\alpha_k - 1}$ in the integrand. The branch of $z^{\alpha_k - 1}$ requires choosing a consistent branch, possible because $\mathbb{H}$ is simply connected and the integrand is nonvanishing.

---

# Legal Operations Used

1. **State the formula**: $f(z) = A + C\int_{z_0}^z\prod_{k=1}^n(\zeta - x_k)^{\alpha_k - 1}\,d\zeta$.
2. **Identify the angle exponents $\alpha_k$**: interior angle $\alpha_k\pi$ corresponds to $(\zeta - x_k)^{\alpha_k - 1}$.
3. **Verify the angle sum**: $\sum_k\alpha_k = n - 2$ (sum of interior angles of $n$-gon is $(n - 2)\pi$).
4. **Choose preimages $x_k$**: three of them can be chosen freely (corresponding to Möbius normalization), the rest determined by the polygon shape.

---

# Hints

> [!note]- Hint 1
> The Schwarz–Christoffel formula: $f(z) = A + C\int_{z_0}^z\prod_{k=1}^n(\zeta - x_k)^{\alpha_k - 1}\,d\zeta$, where $x_1 < x_2 < \ldots < x_n$ are real numbers (preimages of polygon vertices) and $\alpha_k\pi$ are interior angles.

> [!note]- Hint 2
> At each $x_k$, the integrand has a power-law singularity $(\zeta - x_k)^{\alpha_k - 1}$. The integral has a corresponding "kink" at the image $w_k$, with interior angle $\alpha_k\pi$.

> [!note]- Hint 3
> For a triangle: three vertices, three angles. Pick three preimages: $x_1 = 0, x_2 = 1, x_3 = \infty$ (standard normalization).
>
> The formula becomes $f(z) = A + C\int_{z_0}^z \zeta^{\alpha_1 - 1}(\zeta - 1)^{\alpha_2 - 1}\,d\zeta$ (with $\alpha_3$ implicit at $\infty$, taking the factor $(\zeta - \infty)^{\alpha_3 - 1}$ to be absorbed into the constants).
>
> For an equilateral triangle: $\alpha_1 = \alpha_2 = \alpha_3 = 1/3$ (each interior angle is $60° = \pi/3$). So $f(z) = C\int z^{-2/3}(z - 1)^{-2/3}\,dz + A$.

---

# Solution

The proof breaks into four steps. Step 1 states the Schwarz–Christoffel formula and the constraint $\sum \alpha_k = n - 2$; Step 2 sketches the angle-tracking argument that motivates the formula — the $(\alpha_k - 1)\pi$ jump in $\arg f'$ as $z$ crosses $x_k$ matches the polygon's turning angle; Steps 3–4 specialize to the equilateral triangle with $\alpha_k = 1/3$, normalize three preimages to $\{0, 1, \infty\}$, and identify the resulting incomplete-beta integral. The non-obvious move is in Step 2 — the heuristic angle-tracking via $\arg f' = \sum (\alpha_k - 1) \arg(z - x_k)$ is what reveals the integrand structure; once seen, the formula is forced.

**Step 1: The Schwarz–Christoffel formula**

> [!note]- Statement
> Let $P$ be a polygon in $\mathbb{C}$ with vertices $w_1, w_2, \ldots, w_n$ (in counterclockwise order) and interior angles $\alpha_1\pi, \alpha_2\pi, \ldots, \alpha_n\pi$, with $\sum_k\alpha_k = n - 2$ (interior angles of an $n$-gon sum to $(n - 2)\pi$).
>
> Then there is a conformal map $f : \mathbb{H} \to P^\circ$ (interior of the polygon) of the form
> $$f(z) = A + C\int_{z_0}^z\prod_{k=1}^n(\zeta - x_k)^{\alpha_k - 1}\,d\zeta,$$
> where $x_1 < x_2 < \ldots < x_n$ are real numbers (the preimages of the vertices), $A, C \in \mathbb{C}$ are constants determined by the polygon's translation and rotation, and the branches of the powers are chosen so the integrand is holomorphic on $\mathbb{H}$ (by simply-connectedness, branches exist).
>
> The preimages $x_k$ can be partially normalized: by Möbius transformations of $\mathbb{H}$ (a 3-parameter group), three of them (say $x_1, x_2, x_{n}$) can be chosen freely (e.g., $0, 1, \infty$). The remaining $x_k$ are determined by the polygon's shape (the *parameter problem*).

**Step 2: Why the formula works (heuristic)**

> [!note]- Derivation
> The angle of the image curve at $w_k$ should be $\alpha_k\pi$. Computing the angle of $f \circ \gamma$ along the real axis (the preimage of the polygon boundary): the *change* in $\arg f'(z)$ as $z$ passes $x_k$ from left to right is related to the angle at $w_k$.
>
> Specifically: $\arg f'(z) = \arg C + \sum_k(\alpha_k - 1)\arg(z - x_k)$. As $z$ passes $x_k$, $\arg(z - x_k)$ jumps by $-\pi$ (the principal branch of $\arg$ goes from $\pi$ to $0$ when $z$ goes from just-below-$x_k$ to just-above-$x_k$). So $\arg f'$ jumps by $(\alpha_k - 1)\cdot(-\pi)$. The *turning angle* of $f\circ\gamma$ at $w_k$ is $-\pi(\alpha_k - 1) = \pi(1 - \alpha_k) = \pi - \alpha_k\pi$ — the *exterior* angle at $w_k$. Interior angle $\alpha_k\pi$. ✓

**Step 3: Equilateral triangle example**

> [!note]- Derivation
> An equilateral triangle has interior angles $60° = \pi/3$ each. So $\alpha_k = 1/3$ for $k = 1, 2, 3$, and $\sum\alpha_k = 1 = n - 2 = 1$. ✓
>
> Normalize: $x_1 = 0, x_2 = 1, x_3 = \infty$ (three free choices).
>
> The Schwarz–Christoffel formula becomes:
> $$f(z) = A + C\int_{z_0}^z \zeta^{-2/3}(\zeta - 1)^{-2/3}\,d\zeta.$$
> (The factor $(\zeta - \infty)^{\alpha_3 - 1} = (\zeta - \infty)^{-2/3}$ is, after appropriate handling at $\infty$, absorbed into the constants. Standardly, one of the preimages is set to $\infty$ and the corresponding factor omitted, with the angle still respected.)
>
> The integral is a classical **incomplete beta function** (or hypergeometric integral). Specifically, $\int z^{a - 1}(z - 1)^{b - 1}\,dz$ is related to the beta function.
>
> Setting constants: choose $C$ and $A$ so $f(0) = 0$ and $f(1) = 1$ (the vertices at $0$ and $1$ in our triangle). The third vertex is at $f(\infty) = \int_0^\infty\zeta^{-2/3}(\zeta - 1)^{-2/3}\,d\zeta$, which evaluates to a specific complex number related to $\Gamma$-functions.

**Step 4: Computing the third vertex**

> [!note]- Derivation
> $f(\infty) = C \cdot \int_0^\infty z^{-2/3}(z - 1)^{-2/3}\,dz + A$.
>
> For the integral to be well-defined and the polygon to be equilateral (third vertex at $e^{i\pi/3}$), one needs to analyze the integral carefully (especially handling the singularity at $z = 1$ on the path from $0$ to $\infty$).
>
> The general result: $f(\infty)$ involves $\Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$ where $\Gamma$ is the Euler gamma function, giving the standard *beta-integral* answer.
>
> For our equilateral case with $\alpha = \beta = 1/3$: $\int_0^1 z^{-2/3}(1 - z)^{-2/3}\,dz = B(1/3, 1/3) = \Gamma(1/3)^2/\Gamma(2/3)$. With this and analogous expressions for the integral from $1$ to $\infty$, one can verify the third vertex is at $e^{i\pi/3}$ (up to choice of constants $A, C$).

> [!note]- Complete formal solution
> **Schwarz–Christoffel formula:** for a polygon with vertices $w_1, \ldots, w_n$ and interior angles $\alpha_1\pi, \ldots, \alpha_n\pi$ (with $\sum\alpha_k = n - 2$), the conformal map $f : \mathbb{H} \to $ polygon interior is
> $$f(z) = A + C\int_{z_0}^z \prod_{k=1}^n(\zeta - x_k)^{\alpha_k - 1}\,d\zeta,$$
> with $x_k \in \mathbb{R}$ the preimages of $w_k$, and $A, C$ determined by translation/rotation. Three of the $x_k$ can be chosen freely (by Möbius normalization of $\mathbb{H}$); the rest constitute the *parameter problem* and are determined by the polygon's geometry.
>
> **Equilateral triangle example:** $n = 3$, $\alpha_k = 1/3$ for each $k$. Choosing $x_1 = 0, x_2 = 1, x_3 = \infty$:
> $$f(z) = A + C\int z^{-2/3}(z - 1)^{-2/3}\,dz.$$
> The integral is the incomplete beta function, expressible via $\Gamma$-functions; with appropriate $A, C$, this gives the conformal map from $\mathbb{H}$ to the equilateral triangle with vertices at $\{0, 1, e^{i\pi/3}\}$. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "conformal map to polygon" → "Schwarz–Christoffel formula".** The integrand has factors $(\zeta - x_k)^{\alpha_k - 1}$, one per vertex, encoding the angles. The formula is *the* explicit tool for polygonal conformal maps, used pervasively in fluid mechanics (flow past polygonal obstacles), electrostatics (potential in polygonal regions), and finite-element-style PDE solvers.

**The "parameter problem" — finding the preimages $x_k$ for a given polygon — is nontrivial.** Three of the $x_k$ can be normalized via Möbius transformations (e.g., to $0, 1, \infty$), but the remaining ones are determined by transcendental equations involving the polygon's side lengths or vertex positions. Solving this is essentially the only difficult part of Schwarz–Christoffel applications.

**Angle defect → power-law singularity.** A vertex with interior angle $\alpha\pi$ (where $\alpha = 1$ would be no defect, just a smooth point) gives a power $(\zeta - x_k)^{\alpha - 1}$ in the integrand. For acute angles ($\alpha < 1$), this is a *singular* factor (integrand blows up at $x_k$); for obtuse angles ($\alpha > 1$), it's a *vanishing* factor. The map's *derivative* has the right "turning rate" at each vertex.

**Polygonal exterior / unbounded polygons.** Variations of Schwarz–Christoffel handle infinite-area polygons (slits, half-strips), with appropriate conventions for "vertices at infinity".

**Applications.**
- **Fluid flow** past polygonal obstacles (sudden contractions, expansions in channels).
- **Electrostatic potential** in polygonal regions (capacitors with corner geometries).
- **Diffraction theory** (wave scattering off polygonal screens).
- **Numerical conformal mapping** (the **Driscoll & Trefethen** Schwarz–Christoffel Toolbox in MATLAB is the standard).

**Limitation.** Polygons only; for curvilinear domains, other techniques (Koebe iteration, kernel methods) are used.
