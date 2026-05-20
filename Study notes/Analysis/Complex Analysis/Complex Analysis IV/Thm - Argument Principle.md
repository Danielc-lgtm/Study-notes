---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Residue Theorem"
  - "Def - Winding Number"
  - "Def - Removable Singularity, Pole, Essential Singularity"
tags: [analysis, complex-analysis]
---

# Notation

$f$ meromorphic on an open set containing the closed curve $\gamma$ (with no zeros or poles on $\gamma$). $N$ = number of zeros of $f$ inside $\gamma$ (counted with multiplicity); $P$ = number of poles, with multiplicity. $\Gamma = f \circ \gamma$ is the image of $\gamma$ under $f$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Argument Principle).** Let $f$ be meromorphic on an open set $U$, and let $\gamma$ be a closed piecewise $C^1$ curve in $U$ that is null-homotopic in $U$ and avoids the zeros and poles of $f$. Then
> $$\frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = \sum_a I(\gamma; a)\,\operatorname{ord}_a f = I(f\circ\gamma;\, 0),$$
> the sum running over zeros and poles $a$ of $f$ in $U$ (where $\operatorname{ord}_a f$ equals the order of the zero, or minus the order of the pole). In particular, when $\gamma$ bounds a domain $D$ with $I(\gamma; \cdot) = 1$ on $D$ and $0$ outside,
> $$\frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = N - P,$$
> where $N$ and $P$ are the numbers of zeros and poles of $f$ in $D$, each counted with multiplicity.

---

# Motivation

The argument principle says: integrating the logarithmic derivative $f'/f$ around a closed curve $\gamma$ counts the zeros minus poles of $f$ inside $\gamma$, weighted by winding numbers. Stated as a topological identity, it equals the winding number of $f \circ \gamma$ around $0$.

This is the *counting principle* of complex analysis. It converts an algebraic question ("how many zeros does this function have in this region?") into an analytic computation ("integrate $f'/f$"). It is the engine of [[Thm - Rouché's Theorem|Rouché's theorem]] (perturbation arguments for zero counts), [[Thm - Hurwitz's Theorem|Hurwitz's theorem]] (limit-of-nonvanishing), the [[Thm - Open Mapping Theorem|open mapping theorem]], the [[Thm - Local Mapping Degree|local mapping degree]], and many proofs in spectral theory and dynamics.

---

# Sources and Targets

**Sources (Input Broadening)**

**$f$ meromorphic, $\gamma$ closed curve avoiding zeros and poles.** The direct setup. Triggers for: counting zeros/poles, locating roots, comparing functions.

**$f$ holomorphic only (no poles).** Then $P = 0$ and the integral counts zeros only. Common in algebra applications (polynomial root counting).

**$f$ has only poles in a region (no zeros).** Then $N = 0$ and the integral counts $-P$. Used to count poles of meromorphic functions, eigenvalues of operators, etc.

**$f = g(z) - w$ for fixed $w$.** Counts solutions to $g(z) = w$ — preimages of $w$ under $g$. Basis of local mapping degree.

**Targets (Output Amplification)**

Combine with **comparison via Rouché.** Property $D$: have a related function $g$ with known zero count. Amplified result $E$: [[Thm - Rouché's Theorem|Rouché's theorem]] — $f$ and $g$ have same zero count when $|f - g| < |f|$ on the boundary.

Combine with **the residue theorem in reverse.** Property $D$: knowing $\int f'/f$ from contour integration. Amplified result $E$: deduce zero counts.

Combine with **the topological reading $I(f\circ\gamma; 0) = N - P$.** Property $D$: visualize the image curve $f \circ \gamma$. Amplified result $E$: the winding number of the image is the zero/pole count. Used in Nyquist stability criterion.

---

# Why Is It True

The argument principle is a direct application of the residue theorem to $f'/f$.

If $f$ has a zero of order $k$ at $a$, then $f(z) = (z - a)^k g(z)$ with $g$ holomorphic and $g(a) \neq 0$ near $a$. Computing:
$$\frac{f'(z)}{f(z)} = \frac{k(z - a)^{k-1}g(z) + (z - a)^k g'(z)}{(z - a)^k g(z)} = \frac{k}{z - a} + \frac{g'(z)}{g(z)}.$$
The second term is holomorphic at $a$ (since $g(a) \neq 0$); the first term gives a simple pole with residue $k$. So $\operatorname{Res}_a(f'/f) = k = $ order of the zero of $f$ at $a$.

Similarly, if $f$ has a pole of order $k$ at $a$, then $f(z) = (z - a)^{-k}h(z)$ with $h$ holomorphic and $h(a) \neq 0$. Computation gives $\operatorname{Res}_a(f'/f) = -k$.

So $f'/f$ has simple poles at every zero (residue $+$ order) and at every pole (residue $-$ order) of $f$. By the residue theorem,
$$\frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = \sum_a I(\gamma; a) \operatorname{Res}_a(f'/f) = \sum_a I(\gamma; a) \cdot \operatorname{ord}_a f.$$
For $\gamma$ bounding a domain $D$ with $I(\gamma; \cdot) = 1$ on $D$ and $0$ outside, this is $\sum_{\text{zeros in } D}(\text{order}) - \sum_{\text{poles in } D}(\text{order}) = N - P$.

The *topological reading*: $f'/f\,dz = d\log f = d(\log|f|) + i\,d(\arg f)$. The first term is exact (closed loop integral zero); the second integrates to $2\pi i$ times the net change in $\arg f$ around $\gamma$, which is $2\pi i \cdot I(f \circ \gamma; 0)$. So $\frac{1}{2\pi i}\oint f'/f\,dz = I(f \circ \gamma; 0)$ — the winding number of the image curve around $0$.

---

# What Makes This Hard

The non-obvious step is **recognizing $f'/f$ as the logarithmic derivative and computing its residues at zeros and poles of $f$**. The mental move is: $f'/f = (\log f)'$ in a sense, and the residue picks up the "discontinuity of $\log f$" at zeros/poles. A common mistake is to forget that *poles* give *negative* residues, leading to wrong sign in $N - P$. Another error is failing to track the *multiplicity*: $\operatorname{Res}(f'/f) = k$ at a zero of order $k$, not $1$.

---

# Rederivation Scaffold

**High-level strategy:**
Compute residue of $f'/f$ at each zero and pole of $f$. At a zero of order $k$: residue $= +k$. At a pole of order $k$: residue $= -k$. Apply the residue theorem.

**Subgoal decomposition:**

1. **Residue at a zero of order $k$.** Factor $f = (z - a)^k g$ with $g(a) \neq 0$; compute $f'/f = k/(z - a) + g'/g$; identify residue $= k$.

2. **Residue at a pole of order $k$.** Factor $f = (z - a)^{-k} h$ with $h(a) \neq 0$; compute $f'/f = -k/(z - a) + h'/h$; identify residue $= -k$.

3. **Apply residue theorem.** $\frac{1}{2\pi i}\oint_\gamma f'/f\,dz = \sum_a I(\gamma; a)\cdot\operatorname{ord}_a f = N - P$.

4. **Topological interpretation.** Recognize $f'/f\,dz = d\log f$, and the closed integral as the winding number $I(f\circ\gamma; 0)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $f$ be meromorphic on an open set $U$ containing the closed piecewise $C^1$ curve $\gamma$, with no zeros or poles on $\gamma$. Let $\{a_i\}$ be the zeros and poles of $f$ inside $\gamma$ (with respect to a bounding-domain interpretation, or weighted by winding number for the general statement).
>
> **Local analysis.** At a zero of order $k$ at $a$: $f(z) = (z - a)^k g(z)$ near $a$ with $g$ holomorphic, $g(a) \neq 0$. Then
> $$\frac{f'(z)}{f(z)} = \frac{k(z - a)^{k-1} g(z) + (z - a)^k g'(z)}{(z - a)^k g(z)} = \frac{k}{z - a} + \frac{g'(z)}{g(z)}.$$
> The second term is holomorphic at $a$; the first contributes a simple pole with residue $k$. So $\operatorname{Res}_a(f'/f) = k = \operatorname{ord}_a f$.
>
> At a pole of order $k$ at $a$: $f(z) = (z - a)^{-k} h(z)$ with $h$ holomorphic, $h(a) \neq 0$. Analogous computation gives $\operatorname{Res}_a(f'/f) = -k = \operatorname{ord}_a f$ (with the convention $\operatorname{ord}_a f < 0$ for poles).
>
> **Residue theorem.** By [[Thm - Residue Theorem|the residue theorem]]:
> $$\frac{1}{2\pi i}\oint_\gamma \frac{f'(z)}{f(z)}\,dz = \sum_a I(\gamma; a) \operatorname{Res}_a(f'/f) = \sum_a I(\gamma; a) \operatorname{ord}_a f.$$
> When $\gamma$ bounds a domain $D$ with $I(\gamma; \cdot) = 1$ on $D$ and $0$ outside, the sum collapses to $\sum_{\text{zeros in } D}(\text{order}) - \sum_{\text{poles in } D}(\text{order}) = N - P$.
>
> **Topological interpretation.** $\frac{f'(z)}{f(z)} dz = d[\log f(z)]$ on any branch where $\log f$ exists. The closed integral $\oint d[\log f] = $ "net change in $\log f$ around $\gamma$" $= i \cdot \Delta(\arg f) = 2\pi i \cdot I(f \circ \gamma; 0)$. So $\frac{1}{2\pi i}\oint f'/f\,dz = I(f \circ \gamma; 0)$, the winding number of the image curve around $0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Counting eigenvalues of a matrix in a region.** For a matrix $A$, the eigenvalues are zeros of $\det(zI - A)$, a polynomial in $z$. Applying the argument principle to this polynomial counts the eigenvalues in any closed region. This is used in numerical linear algebra for **eigenvalue localization** (Gershgorin discs etc.) and in stability analysis (counting right-half-plane eigenvalues = unstable modes).

**Counting roots of polynomials in a half-plane.** For a polynomial $p(s)$, applying the argument principle on a large semicircle in the right half-plane counts right-half-plane roots (instability count). This is the basis of the **Routh-Hurwitz criterion** for polynomial stability.

**Nyquist stability criterion in control.** For a closed-loop system with open-loop transfer function $L(s)$, stability is determined by counting right-half-plane zeros of $1 + L$. The argument principle on a Nyquist contour (vertical line plus large semicircle) converts this to "encirclements of $-1$ by the Nyquist plot of $L$".

---

# Bridges

- **[[Thm - Residue Theorem]]** — the immediate engine.

- **[[Thm - Rouché's Theorem]]** — perturbation argument using the argument principle.

- **[[Def - Winding Number]]** — the topological reading.

- **[[Thm - Open Mapping Theorem]]** — derived via the local mapping degree.

- **[[Thm - Hurwitz's Theorem]]** — uses the argument principle on the boundary of a small disc.

---

# Unlocked by This

> [!tip] Rouché's Theorem and Counting Arguments *(from §3.5)*
> [[Thm - Rouché's Theorem|Rouché]] is the perturbation version: comparing $f, g$ with $|f - g| < |f|$ on the boundary.

> [!tip] Open Mapping Theorem *(from §3.5)*
> Non-constant holomorphic functions are [[Thm - Open Mapping Theorem|open maps]] — a direct corollary of the argument principle plus local mapping degree.

> [!tip] Nyquist Stability *(from Control Theory)*
> The Nyquist criterion is the argument principle applied in control theory, classifying stability by encirclements of $-1$ in the complex plane.
