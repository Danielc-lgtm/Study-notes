---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Argument Principle"
  - "Def - Winding Number"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$D \subseteq \mathbb{C}$ is a bounded domain with closed curve boundary $\gamma$; $f, g$ are holomorphic on $\overline{D}$. $N(h, D)$ is the number of zeros of $h$ in $D$, counted with multiplicity. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Rouché).** Let $D \subseteq \mathbb{C}$ be a bounded domain whose boundary $\gamma$ is a closed piecewise $C^1$ curve, and let $f, g$ be holomorphic on an open set containing $\overline{D}$. If
> $$|f(z) - g(z)| < |f(z)| \qquad\text{for every } z \in \gamma,$$
> then $f$ and $g$ have no zeros on $\gamma$ and the same number of zeros in $D$, counted with multiplicity:
> $$N(f, D) = N(g, D).$$

---

# Motivation

How do you count the zeros of a complicated function without finding them explicitly? Rouché's theorem provides a powerful technique: if you have a *simpler* function $f$ whose zeros you know how to count, and the difference $|f - g|$ is small enough on the boundary, then $g$ has the same number of zeros as $f$ in the region.

This is the workhorse of *zero-counting* in complex analysis. The classical application is the fundamental theorem of algebra: a polynomial $p(z) = z^n + (\text{lower order})$ has the same number of zeros as $z^n$ on a large circle (which is $n$). Rouché extends this to vast classes of perturbation problems: location of roots of polynomials in specific regions, stability of dynamical systems under small perturbations, location of eigenvalues, comparison of zero counts of related functions.

The geometric intuition: if $|f - g| < |f|$ on $\gamma$, the image curves $f \circ \gamma$ and $g \circ \gamma$ never cross $0$ on $\gamma$ (since $|g| \geq |f| - |f - g| > 0$), and the homotopy $h(t, z) = (1 - t)f(z) + tg(z)$ between them stays away from $0$ too. So the winding numbers of $f \circ \gamma$ and $g \circ \gamma$ around $0$ are equal (homotopy invariance). By the argument principle, these winding numbers count the zeros — so the zero counts agree.

---

# Sources and Targets

**Sources (Input Broadening)**

**Dominant-term comparison.** Property $B$: $f$ is a simple "dominant term" of $g$. Bridge: $|f - g|$ is the "lower-order" part of $g$, small on a region where the dominant term is large. Examples: polynomial $z^n + (\text{lower})$ compared to $z^n$ on $|z| = R$ large; polynomial dominated by constant term on small $|z|$.

**Convex combination homotopy.** Property $B$: $h(t, z) = (1 - t)f + tg$ doesn't vanish on $\gamma$ for any $t \in [0, 1]$. Bridge: equivalent to $|f - g| < |f|$ on $\gamma$ (by Rouché's hypothesis), so the homotopy stays nonzero, hence winding numbers agree.

**Perturbation theory.** Property $B$: $g = f + \epsilon\cdot$(other terms), with $\epsilon$ small. Bridge: for $\epsilon$ small enough, $|f - g| = \epsilon|h| < |f|$ on bounded regions where $f$ doesn't vanish. So small perturbations preserve zero count locally.

**Targets (Output Amplification)**

Combine with **a dominant-term polynomial.** Property $D$: $f = z^n$, $g$ is any monic polynomial of degree $n$. Amplified result $E$: the fundamental theorem of algebra — every degree-$n$ polynomial has exactly $n$ zeros (counted with multiplicity).

Combine with **stability under small perturbations.** Property $D$: a polynomial $p$ has all zeros in some region. Amplified result $E$: small perturbations $p + \epsilon q$ also have zeros in (slightly larger) regions. Used in dynamical systems for robust stability analysis.

Combine with **the argument principle applied to $f + tg$.** Property $D$: the curve $t \mapsto N(f + tg, D)$ is continuous integer-valued, hence constant if the curve doesn't hit a zero. Amplified result $E$: zero counts are robust to deformations.

---

# Why Is It True

The proof is a clean application of the argument principle and homotopy invariance.

Consider the homotopy $h(t, z) := (1 - t)f(z) + tg(z)$ for $t \in [0, 1]$. At $t = 0$, $h(0, \cdot) = f$; at $t = 1$, $h(1, \cdot) = g$.

On $\gamma$, the function $h(t, z)$ never vanishes for any $t$: if $h(t, z) = 0$ then $(1 - t) f(z) = -t g(z)$, so $|f(z)| = (t/(1 - t))|g(z) - f(z)|$ for $t < 1$ (and $g(z) = 0$ for $t = 1$, which is excluded by $|f - g| < |f|$ forcing $|g| > 0$ on $\gamma$). The hypothesis $|f - g| < |f|$ rules this out (with care for the boundary cases $t = 0, 1$).

So the integral $\frac{1}{2\pi i}\oint_\gamma h'/h\,dz$ — which counts zeros of $h(t, \cdot)$ inside $\gamma$ by the argument principle — is an integer-valued continuous function of $t$ (continuous because $h$ depends continuously on $t$ with nonvanishing on the boundary; integer-valued because of the argument principle). Therefore it is constant on $[0, 1]$.

Evaluating at $t = 0$: gives $N(f, D)$, the zero count of $f$ inside $\gamma$. Evaluating at $t = 1$: gives $N(g, D)$. Since these are equal, the zero counts agree.

The conceptual content: zero counts are *homotopy invariants* of holomorphic functions. The hypothesis $|f - g| < |f|$ is precisely what guarantees that the homotopy between $f$ and $g$ doesn't hit zero on the boundary, preserving the zero count.

---

# What Makes This Hard

The non-obvious step is **constructing the homotopy and showing it stays nonzero on the boundary**. The hypothesis $|f - g| < |f|$ on $\gamma$ might look bizarre at first: why a strict inequality, why one-sided ($|f|$ on the right but not symmetric in $f, g$)? The reason is the homotopy argument: $(1 - t)f + tg$ vanishing implies $|f| = (t/(1 - t))|g - f|$, which requires $|g - f| \geq |f|$ (some scaled equality), so the strict $|f - g| < |f|$ rules it out. A common mistake is to swap the inequality to $|f - g| < |g|$ — this is *not* equivalent; Rouché requires comparison against the *known* function $f$, not the function we're studying.

---

# Rederivation Scaffold

**High-level strategy:**
The homotopy $h(t, z) = (1 - t)f + tg$ stays nonzero on $\gamma$ (by hypothesis), so the zero count of $h(t, \cdot)$ inside $\gamma$ — given by the argument principle — is continuous in $t$, integer-valued, hence constant. Equate the counts at $t = 0$ and $t = 1$.

**Subgoal decomposition:**

1. **Construct the homotopy.** $h(t, z) = (1 - t)f(z) + tg(z)$ for $t \in [0, 1]$.

2. **Verify $h(t, z) \neq 0$ on $\gamma$ for every $t$.** Use $|f - g| < |f|$ to rule out $h(t, z) = 0$.

3. **Apply the argument principle.** $N(h(t, \cdot), D) = \frac{1}{2\pi i}\oint_\gamma h'(t, z)/h(t, z)\,dz$, well-defined and integer-valued.

4. **Use continuity in $t$.** The integral is continuous in $t$ (uniform convergence of integrand on the compact $\gamma$). Integer-valued + continuous on connected $[0, 1]$ = constant.

5. **Equate endpoints.** $N(f, D) = N(g, D)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The homotopy stays nonzero on the boundary
> **Statement:** If $|f(z) - g(z)| < |f(z)|$ on $\gamma$, then $h(t, z) := (1 - t)f(z) + tg(z) \neq 0$ for all $t \in [0, 1]$ and $z \in \gamma$.
>
> **Hint:** If $h(t, z) = 0$, rearrange to relate $|f|, |g|$, and use the hypothesis.
>
> > [!note]- Full proof
> > Suppose $h(t, z) = (1 - t)f(z) + tg(z) = 0$ for some $z \in \gamma, t \in [0, 1]$.
> > - $t = 0$: then $f(z) = 0$, contradicting $|f(z)| > |f(z) - g(z)| \geq 0$ on $\gamma$.
> > - $t = 1$: then $g(z) = 0$, and $|f(z) - g(z)| = |f(z)|$, contradicting strict inequality.
> > - $0 < t < 1$: $(1 - t) f(z) = -t g(z)$, so $|f(z)|/|g(z)| = t/(1 - t)$, i.e., $|f(z) - g(z)| = |f(z) + (g(z) - f(z))| \geq$ wait, more carefully: $|f - g| \geq |f| - |g| = |f| - (1-t)|f|/t = |f|(1 - (1-t)/t) = |f|(2t - 1)/t$, which for $t > 1/2$ is non-negative. The cleaner argument: at $h(t, z) = 0$, $|f(z)| = (t/(1-t))|g(z) - f(z)| \leq (t/(1-t)) \cdot$ something. Easier: at $h(t,z) = 0$ with $0 < t < 1$: $-tg = (1-t)f$, so $tg + (1-t)f = 0$, hence $g - f = (g \cdot t + g (1-t)) - f = g - f$, ugh. Let me redo: $h = 0 \Rightarrow (1-t)f = -tg \Rightarrow f - g = f + tg/(1-t) - g = ...$.
> >
> > Cleaner: if $h(t, z) = 0$ for $0 < t < 1$, then $|(1-t)f(z)| = |tg(z)|$, so $(1-t)|f| = t|g|$. The triangle inequality gives $|g| \geq |f| - |f - g| > 0$ on $\gamma$, so $|g| > 0$. Now, $|f - g| < |f|$ becomes (using $|g| = (1-t)|f|/t$): $|f - g| < |f|$. But also $|f - g| \geq |f| - |g| = |f| - (1-t)|f|/t = |f|(2t - 1)/t$ for $t > 1/2$. Combined with $|g - f| < |f|$, ok this is getting messy. Let me give the standard one-line proof.
> >
> > **Standard proof:** If $h(t, z) = 0$, then $|f(z)| = |(1 - t)f(z)| / (1 - t) = |tg(z)|/(1 - t) = t|g(z)|/(1 - t)$. Also $|g(z)| = |g(z) - f(z) + f(z)| \leq |f(z) - g(z)| + |f(z)| < |f(z)| + |f(z)| = 2|f(z)|$ (by hypothesis $|f - g| < |f|$). So $|f(z)| < 2t|f(z)|/(1 - t)$, giving $1 < 2t/(1-t)$, i.e., $t > 1/3$. Hmm, doesn't quite finish.
> >
> > **Cleanest proof:** Suppose $h(t, z) = 0$ for some $t \in [0, 1], z \in \gamma$. Then $|(1-t)f(z) + tg(z)| = 0$, so $(1-t)f(z) = -tg(z)$, i.e., $f(z)/g(z) = -t/(1-t) \leq 0$ (assuming $t < 1$). But then $f(z) = -(t/(1-t))g(z)$, so $|f - g| = |f + (-g)| =$... ah, the key insight: $f$ and $g$ are then antiparallel (in $\mathbb{C}$). So $|f - g| = |f| + |g|$ (triangle inequality, equality case). Now $|f - g| < |f|$ forces $|g| < 0$, impossible. So $h(t, z) = 0$ leads to contradiction for $t \in (0, 1)$. For $t = 0$: $f(z) = 0$ but $|f| > |f-g| \geq 0$, contradiction. For $t = 1$: $g(z) = 0$, but $|f - g| < |f|$ means $|f - 0| < |f|$, i.e., $|f| < |f|$, contradiction. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Define $h(t, z) := (1 - t)f(z) + tg(z)$ for $t \in [0, 1], z \in \overline{D}$.
>
> By Lemma 1, $h(t, z) \neq 0$ for any $z \in \gamma, t \in [0, 1]$. So $h(t, \cdot)$ is holomorphic on $\overline{D}$ with no zeros on $\gamma$, and the argument principle applies:
> $$N(h(t, \cdot), D) = \frac{1}{2\pi i}\oint_\gamma \frac{h_z(t, z)}{h(t, z)}\,dz,$$
> where $h_z$ denotes the $z$-derivative.
>
> This integral is continuous in $t$: the integrand $h_z(t, z)/h(t, z)$ is jointly continuous in $(t, z)$ on the compact $[0, 1] \times \gamma$ (using non-vanishing of $h$ for the denominator), so the integral varies continuously in $t$.
>
> The integral is integer-valued (by the argument principle). Continuous + integer-valued on the connected interval $[0, 1]$ ⟹ constant. So $N(h(0, \cdot), D) = N(h(1, \cdot), D)$, i.e., $N(f, D) = N(g, D)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fundamental Theorem of Algebra.** For a monic polynomial $p(z) = z^n + a_{n-1}z^{n-1} + \ldots + a_0$, compare with $z^n$ on the circle $|z| = R$. For $R$ large enough, $|p(z) - z^n| \leq R^{n-1}(|a_{n-1}| + |a_{n-2}|/R + \ldots) < R^n = |z^n|$. So by Rouché, $p$ and $z^n$ have the same number of zeros in $|z| < R$, which is $n$ (counting the $n$-fold zero of $z^n$ at $0$). Hence $p$ has exactly $n$ zeros in $|z| < R$, and (since $R$ was arbitrary and large) in all of $\mathbb{C}$.

**Locating roots of $p(z) = z^4 + z^3 + 1$ in the unit disc.** Compare with $g(z) = z^3 + 1$ on $|z| = 1$: $|p - g| = |z^4| = 1$. And $|g(z)| = |z^3 + 1|$, which has minimum $|g(e^{i\theta})| = |e^{3i\theta} + 1|$. At $\theta = \pi/3$: $e^{i\pi} + 1 = 0$. So $g$ has a zero on the unit circle, and the inequality fails. Need different comparison. (This shows Rouché requires care in choosing the comparison.)

**Counting roots of stable polynomials.** For a polynomial $p$ to be **Hurwitz stable** (all roots in left half-plane), one can compare with a known stable polynomial via Rouché on a contour bounding the right half-plane. This connects to the Routh-Hurwitz criterion.

---

# Bridges

- **[[Thm - Argument Principle]]** — the engine.

- **[[Def - Winding Number]]** — the homotopy invariance is what makes the zero count constant under deformation.

- **[[Thm - Fundamental Theorem of Algebra via Rouché]]** — the canonical application.

- **[[Thm - Hurwitz's Theorem]]** — a sibling result for sequences of nonvanishing functions.

---

# Unlocked by This

> [!tip] Fundamental Theorem of Algebra *(from §3.5)*
> The one-line proof of FTA via [[Thm - Fundamental Theorem of Algebra via Rouché|Rouché]].

> [!tip] Stability of Polynomial Roots *(from Control Theory)*
> Small perturbations of stable polynomials remain stable, by Rouché's continuity. This is the basis of *robust stability* in control.
