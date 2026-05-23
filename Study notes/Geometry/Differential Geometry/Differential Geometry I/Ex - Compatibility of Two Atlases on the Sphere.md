---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Transition Function"
  - "Thm - Smooth Structure from Maximal Atlas"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that two natural atlases on $S^n$ — the **stereographic atlas** with two charts (from [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]) and the **graph-coordinate atlas** with $2(n+1)$ charts (from Lee Example 1.4) — determine the *same* smooth structure on $S^n$.

The two atlases are:

**Stereographic atlas:** $\mathcal{A}_{\text{stereo}} = \{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$, with
$$\sigma_N(x) = \frac{1}{1 - x^{n+1}}(x^1, \dots, x^n), \quad \sigma_S(x) = \frac{1}{1 + x^{n+1}}(x^1, \dots, x^n).$$

**Graph-coordinate atlas:** $\mathcal{A}_{\text{graph}} = \{(U_i^\pm, \varphi_i^\pm) : i = 1, \dots, n+1\}$, where $U_i^\pm = \{x \in S^n : \pm x^i > 0\}$ and
$$\varphi_i^\pm(x^1, \dots, x^{n+1}) = (x^1, \dots, \widehat{x^i}, \dots, x^{n+1}) \in \mathbb{B}^n,$$
where the hat indicates omission of the $i$-th coordinate.

Show that $\mathcal{A}_{\text{stereo}} \cup \mathcal{A}_{\text{graph}}$ is a smooth atlas (equivalently, by [[Thm - Smooth Structure from Maximal Atlas]] part (b), the two atlases determine the same smooth structure).

**Recall:**

The criterion for two atlases to determine the same smooth structure:

![[Thm - Smooth Structure from Maximal Atlas#Statement]]

The stereographic atlas was constructed in [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]; the graph-coordinate atlas is in Lee Example 1.4.

---

# Convergent Strategy

**Problem class:** Showing two atlases determine the same smooth structure — a *compatibility verification* problem. By [[Thm - Smooth Structure from Maximal Atlas]] part (b), this reduces to showing that every chart of one atlas is smoothly compatible with every chart of the other. Symmetry-of-the-cross-pairs makes this tractable: only finitely many distinct chart types need to be checked.

**Assumption pattern:** Both atlases live on the same topological manifold $S^n$, and we've already shown each is independently a smooth atlas (in [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]] and Lee Example 1.4). The technical task is computing $4(n+1)$ transition functions: each of the 2 stereographic charts overlaps with each of the $2(n+1)$ graph charts.

**Theorem routing:** Two atlases determine the same smooth structure ⟺ their union is smooth (Lee 1.17 part (b)). The route: (i) compute a representative transition function, e.g., $\varphi_i^+ \circ \sigma_N^{-1}$; (ii) verify smoothness by direct substitution and inspection; (iii) by symmetry, all $4(n+1)$ pairs of transitions are smooth.

**Key decision point:** Choosing the representative transition function to compute. The cleanest choice is $\varphi_{n+1}^+ \circ \sigma_N^{-1}$ (a graph chart's $n+1$-th-positive coordinate vs. the north-pole stereographic chart), because both involve the last coordinate of the sphere — and the algebraic identities relating them are simplest.

---

# Legal Operations Used

1. **Operation 2 from the topic page (compute transition functions explicitly).** We compute representative transition functions between graph charts and stereographic charts, and verify smoothness.

2. **Operation 9 from the topic page (replace one atlas by an equivalent one).** This exercise verifies the equivalence of the two atlases; once verified, one may freely use either atlas (or any chart smoothly compatible with either) in working with the smooth structure on $S^n$.

---

# Hints

> [!note]- Hint 1
> Compute $\sigma_N^{-1}$ from [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]]: 
> $$\sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}(2u^1, \dots, 2u^n, |u|^2 - 1).$$
> Apply $\varphi_{n+1}^+$ to this (which drops the last coordinate); this gives the transition function $\varphi_{n+1}^+ \circ \sigma_N^{-1}$ from $\sigma_N(U_{n+1}^+ \cap (S^n \setminus N))$ to $\varphi_{n+1}^+(U_{n+1}^+) = \mathbb{B}^n$.

> [!note]- Hint 2
> The domain of $\varphi_{n+1}^+ \circ \sigma_N^{-1}$ is $\sigma_N(U_{n+1}^+)$. Compute: $x \in U_{n+1}^+$ iff $x^{n+1} > 0$ iff (via $x^{n+1} = (|u|^2 - 1)/(|u|^2 + 1)$) $|u|^2 > 1$. So the domain is $\mathbb{R}^n \setminus \overline{\mathbb{B}^n}$ (the exterior of the closed unit ball).

> [!note]- Hint 3
> Compute the resulting transition: $\varphi_{n+1}^+ \circ \sigma_N^{-1}(u) = \frac{2u}{|u|^2 + 1}$, defined for $|u|^2 > 1$. Both components are smooth functions of $u$ on the open domain.

> [!note]- Hint 4
> By symmetry, every other pairing — say $\varphi_i^\pm \circ \sigma_N^{-1}$ for $i \neq n+1$ — gives a similar rational expression in $u$, smooth on its domain. The cases for $\sigma_S$ are obtained by sign-changes.

---

# Solution

The proof breaks into three steps. Step 1 computes a representative transition function $\varphi_{n+1}^+ \circ \sigma_N^{-1}$ and verifies its smoothness. Step 2 computes the inverse transition (and similarly verifies smoothness). Step 3 argues that all $4(n+1)$ pairwise transitions are smooth by the same method, and concludes via [[Thm - Smooth Structure from Maximal Atlas]] part (b).

**Step 1: Compute the transition $\varphi_{n+1}^+ \circ \sigma_N^{-1}$.**

For $u \in \mathbb{R}^n$ with $|u|^2 > 1$ (so that $\sigma_N^{-1}(u) \in U_{n+1}^+$),
$$\varphi_{n+1}^+(\sigma_N^{-1}(u)) = \frac{2u}{|u|^2 + 1} \in \mathbb{B}^n.$$

> [!note]- Derivation
> *Determine the domain.* We need $\sigma_N^{-1}(u) \in U_{n+1}^+ \cap (S^n \setminus \{N\})$, i.e., the $(n+1)$-th coordinate of $\sigma_N^{-1}(u)$ is positive. From [[Ex - The Sphere as a Smooth Manifold via Stereographic Projection]], the $(n+1)$-th coordinate is $\frac{|u|^2 - 1}{|u|^2 + 1}$, which is positive iff $|u|^2 > 1$. So the domain of the transition is $\{u \in \mathbb{R}^n : |u|^2 > 1\}$, an open subset of $\mathbb{R}^n$.
>
> *Compute the transition.* Apply $\varphi_{n+1}^+$ to $\sigma_N^{-1}(u)$; recall $\varphi_{n+1}^+$ drops the last coordinate. The first $n$ coordinates of $\sigma_N^{-1}(u)$ are $\frac{2u^j}{|u|^2 + 1}$ for $j = 1, \dots, n$. So $\varphi_{n+1}^+ \circ \sigma_N^{-1}(u) = \frac{2u}{|u|^2 + 1}$, a smooth vector-valued function on the domain.
>
> *Smoothness.* Each component $\frac{2u^j}{|u|^2 + 1}$ is a rational function of $u$ with denominator $|u|^2 + 1 \geq 1 > 0$, hence smooth on $\mathbb{R}^n$ (and in particular on the subdomain $|u|^2 > 1$).
>
> *Image in $\mathbb{B}^n$.* The squared norm of $\frac{2u}{|u|^2 + 1}$ is $\frac{4|u|^2}{(|u|^2 + 1)^2}$. By AM-GM or direct check, this is less than $1$ iff $4|u|^2 < (|u|^2 + 1)^2$, i.e., $(|u|^2 - 1)^2 > 0$, i.e., $|u|^2 \neq 1$. Since we are on $|u|^2 > 1$, this holds. So the image lies in $\mathbb{B}^n$, as required.

**Step 2: Compute the inverse transition $\sigma_N \circ (\varphi_{n+1}^+)^{-1}$.**

The inverse chart $(\varphi_{n+1}^+)^{-1} : \mathbb{B}^n \to U_{n+1}^+$ is $(\varphi_{n+1}^+)^{-1}(y) = (y^1, \dots, y^n, \sqrt{1 - |y|^2})$. Compose with $\sigma_N$ to get
$$\sigma_N \circ (\varphi_{n+1}^+)^{-1}(y) = \frac{y}{1 - \sqrt{1 - |y|^2}} \in \mathbb{R}^n,$$
defined for $|y| < 1$ (i.e., $y \in \mathbb{B}^n$).

> [!note]- Derivation
> *Inverse chart.* $\varphi_{n+1}^+$ drops the last coordinate; its inverse fills it back in. For $x \in S^n$, $x^{n+1} = \sqrt{1 - \sum_{j=1}^n (x^j)^2}$ (positive root, since $U_{n+1}^+$ has $x^{n+1} > 0$). So $(\varphi_{n+1}^+)^{-1}(y) = (y^1, \dots, y^n, \sqrt{1 - |y|^2})$.
>
> *Apply $\sigma_N$.* The image $(\varphi_{n+1}^+)^{-1}(y)$ has $(n+1)$-th coordinate $\sqrt{1 - |y|^2}$. So $\sigma_N$ divides the first $n$ coordinates by $1 - \sqrt{1 - |y|^2}$:
> $$\sigma_N \circ (\varphi_{n+1}^+)^{-1}(y) = \frac{(y^1, \dots, y^n)}{1 - \sqrt{1 - |y|^2}}.$$
>
> *Smoothness.* The denominator $1 - \sqrt{1 - |y|^2}$ is positive for $|y| > 0$ (since $\sqrt{1 - |y|^2} < 1$ when $|y| > 0$); however, $|y| > 0$ does *not* include $y = 0$, and at $y = 0$ we have $\sqrt{1 - |y|^2} = 1$, so the denominator vanishes. This singularity at $y = 0$ corresponds to the south pole $\sigma_N(0) \notin S^n \setminus \{N\}$ — but wait, $\sigma_N(S) = 0$, so $\sigma_N \circ (\varphi_{n+1}^+)^{-1}(0)$ would be $\sigma_N(S) = 0$, and indeed the formula gives $0/0$.
>
> So actually we need to be careful about the domain of the inverse transition. The inverse transition is defined on $\varphi_{n+1}^+(U_{n+1}^+ \cap (S^n \setminus \{N\})) = \mathbb{B}^n \setminus \{y : (\varphi_{n+1}^+)^{-1}(y) = N\}$. Since $N = (0, \dots, 0, 1)$ has $(\varphi_{n+1}^+)^{-1}(N) = (0, 1)$, we have $(\varphi_{n+1}^+)^{-1}(y) = N$ iff $(y, \sqrt{1 - |y|^2}) = (0, 1)$ iff $y = 0$ and $|y| = 0$. So the inverse transition is defined on $\mathbb{B}^n \setminus \{0\}$.
>
> On $\mathbb{B}^n \setminus \{0\}$, the denominator $1 - \sqrt{1 - |y|^2}$ is positive (since $|y| > 0$), so the transition is smooth (square root of a positive smooth function is smooth, and quotient with nonzero denominator is smooth).

**Step 3: All transitions are smooth; conclude same smooth structure.**

By symmetry (the same computation with sign changes), all $4(n+1)$ pairwise transitions between stereographic charts and graph charts are smooth on their respective open domains. So $\mathcal{A}_{\text{stereo}} \cup \mathcal{A}_{\text{graph}}$ is a smooth atlas. By [[Thm - Smooth Structure from Maximal Atlas]] part (b), the two atlases determine the same smooth structure on $S^n$.

> [!note]- Derivation
> *Other transitions.* The other transitions to compute are: $\varphi_i^\pm \circ \sigma_N^{-1}$ for $i \neq n+1$, and $\varphi_i^\pm \circ \sigma_S^{-1}$ for $i = 1, \dots, n+1$, and the inverses.
>
> For $\varphi_i^+ \circ \sigma_N^{-1}$ with $i \neq n+1$, we drop the $i$-th coordinate from $\sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}(2u^1, \dots, 2u^n, |u|^2 - 1)$; the result is
> $$\varphi_i^+ \circ \sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}(2u^1, \dots, \widehat{2u^i}, \dots, 2u^n, |u|^2 - 1),$$
> on the domain where $u^i > 0$ (so the $i$-th sphere coordinate $\sigma_N^{-1}(u)^i = 2u^i/(|u|^2 + 1)$ is positive). Each component is a rational function with nonvanishing denominator, hence smooth. Similarly for $\varphi_i^- \circ \sigma_N^{-1}$ (with the constraint $u^i < 0$).
>
> For $\varphi_i^\pm \circ \sigma_S^{-1}$: replace $\sigma_N^{-1}$ with $\sigma_S^{-1}(v) = \frac{1}{|v|^2 + 1}(2v^1, \dots, 2v^n, 1 - |v|^2)$. Same form, same conclusion: rational with nonvanishing denominator, smooth.
>
> *Inverse transitions.* Each inverse transition $\sigma_N \circ (\varphi_i^\pm)^{-1}$ or $\sigma_S \circ (\varphi_i^\pm)^{-1}$ involves the square root $\sqrt{1 - |y|^2}$ (for the missing coordinate), which is smooth on $\mathbb{B}^n$. The resulting expression is a quotient of smooth functions; potential singularities occur only at the omitted points (the pole one is projecting from), which lie outside the relevant domain.
>
> All $4(n+1)$ pairwise transitions are smooth. So $\mathcal{A}_{\text{stereo}} \cup \mathcal{A}_{\text{graph}}$ is a smooth atlas. By Lee 1.17 part (b), $\mathcal{A}_{\text{stereo}}$ and $\mathcal{A}_{\text{graph}}$ determine the same smooth structure.

> [!note]- Complete formal solution
> **Claim.** The stereographic atlas $\mathcal{A}_{\text{stereo}} = \{(S^n \setminus \{N\}, \sigma_N), (S^n \setminus \{S\}, \sigma_S)\}$ and the graph-coordinate atlas $\mathcal{A}_{\text{graph}} = \{(U_i^\pm, \varphi_i^\pm) : i = 1, \dots, n+1\}$ determine the same smooth structure on $S^n$.
>
> *Proof.* By [[Thm - Smooth Structure from Maximal Atlas]] part (b), it suffices to show $\mathcal{A}_{\text{stereo}} \cup \mathcal{A}_{\text{graph}}$ is a smooth atlas. We have already shown each atlas is internally smooth, so we need only check smooth compatibility between every stereographic chart and every graph chart.
>
> **Compute the forward transition $\varphi_i^+ \circ \sigma_N^{-1}$ for $i \leq n$.** On its domain (a subset of $\mathbb{R}^n$ where $u^i > 0$), we have
> $$\sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}\left(2u^1, \dots, 2u^n, |u|^2 - 1\right).$$
> Applying $\varphi_i^+$ (drop the $i$-th coordinate):
> $$\varphi_i^+ \circ \sigma_N^{-1}(u) = \frac{1}{|u|^2 + 1}\left(2u^1, \dots, \widehat{2u^i}, \dots, 2u^n, |u|^2 - 1\right),$$
> a vector of rational functions of $u$ with denominator $|u|^2 + 1 \geq 1$, hence smooth on $\{u^i > 0\}$.
>
> **Compute the forward transition $\varphi_{n+1}^+ \circ \sigma_N^{-1}$.** Drop the last coordinate from $\sigma_N^{-1}(u)$:
> $$\varphi_{n+1}^+ \circ \sigma_N^{-1}(u) = \frac{2u}{|u|^2 + 1},$$
> on the domain $\{u^{n+1} > 0\}$ which translates to $|u|^2 > 1$. Each component is rational with denominator $|u|^2 + 1$, smooth.
>
> **Inverse transitions $\sigma_N \circ (\varphi_i^+)^{-1}$.** For $i \leq n$, the inverse chart $(\varphi_i^+)^{-1}$ inserts $\sqrt{1 - |y|^2}$ in the $i$-th position; applying $\sigma_N$ divides through by $1 - $ (the $(n+1)$-th coordinate). This is a quotient of smooth functions with nonzero denominator on the relevant domain (the omitted pole $N$ lies outside the chart $\varphi_i^+$). Smooth.
>
> **The $\sigma_S$ cases and the $\varphi_i^-$ cases** are obtained by sign reflections and follow the same pattern.
>
> All $4(n+1)$ pairwise transitions between $\mathcal{A}_{\text{stereo}}$ and $\mathcal{A}_{\text{graph}}$ are smooth, so $\mathcal{A}_{\text{stereo}} \cup \mathcal{A}_{\text{graph}}$ is a smooth atlas. By Lee 1.17 part (b), $\mathcal{A}_{\text{stereo}}$ and $\mathcal{A}_{\text{graph}}$ determine the same smooth structure on $S^n$ — the **standard smooth structure**. $\blacksquare$

> [!warning] Sanity-check: alternative parametrizations also lie in the standard smooth structure
> Many other natural charts on $S^n$ are compatible with both atlases — and hence belong to the standard smooth structure. Examples: spherical coordinates $(\theta_1, \dots, \theta_n)$ on $S^n$ (well-defined on the open subset avoiding the polar singularities); rotation-induced charts (transport stereographic charts by rotations of $\mathbb{R}^{n+1}$, giving charts centered anywhere). Each of these has a smooth transition with both $\sigma_N$/$\sigma_S$ and the $\varphi_i^\pm$, hence lies in the standard smooth structure. The smooth structure on $S^n$ is rich, and any of these atlases can serve as a representative.

---

# Key Takeaways

**Compatibility of two atlases is the practical test for "same smooth structure."** Whenever two different constructions produce smooth atlases on the same topological manifold, the question is whether they describe the same smooth manifold. Lee 1.17 part (b) reduces this to checking the union is a smooth atlas — equivalently, pairwise smooth compatibility of charts from the two atlases. For finitely many charts in each, this is a finite computation; for infinitely many, it reduces by symmetry. The whole exercise is a finite computation.

**The general principle: a single smooth atlas determines the entire smooth structure.** Once an atlas is recognized as smooth, every chart smoothly compatible with it is in the smooth structure. So the smooth structure on $S^n$ is determined by either of the two atlases above, and one is free to use any other chart smoothly compatible with either. This is the operational consequence of [[Thm - Smooth Structure from Maximal Atlas]] part (a).

**Transition computations: rational functions are smooth on their domain of definition.** The transitions in this exercise are *rational functions* in the coordinates, with denominators that are either constants ($|u|^2 + 1 \geq 1$, never zero) or coordinates ($u^i > 0$, ensured by the domain). Rational functions with nonvanishing denominators are smooth — a basic fact of multivariable calculus. This makes transition-smoothness verifications routine once the algebraic form is computed.

**The cocycle structure: $4(n+1)$ transitions, but only one needs explicit computation by symmetry.** The full atlas $\mathcal{A}_{\text{stereo}} \cup \mathcal{A}_{\text{graph}}$ has $2 + 2(n+1) = 2(n+2)$ charts and $\binom{2(n+2)}{2}$ pairs. Most of these are already smoothly compatible (the internal pairs within each atlas are smooth by hypothesis); the new ones to check are the cross-pairs, $2 \cdot 2(n+1) = 4(n+1)$. By the symmetry of the construction (rotational symmetry of $S^n$, sign symmetry of $\pm$), only one is essentially distinct: $\varphi_i^+ \circ \sigma_N^{-1}$ for some fixed $i$. Once that is shown smooth, all others follow by symmetry.

**Geometric interpretation: stereographic projection is "graph coordinates from a curved chart-target."** Stereographic projection from $N$ sends $S^n \setminus \{N\}$ to $\mathbb{R}^n$ via a *conformal* map (preserves angles); the graph-coordinate atlas uses a *flat* chart-target ($\mathbb{B}^n$) with discontinuous projections at the equator. Both atlases describe the same smooth structure but reflect different geometric perspectives: the conformal/circular structure (stereographic) and the Cartesian/decomposition structure (graph). The fact that the smooth structure is the *same* but the *atlases* differ illustrates how the smooth-structure-as-maximal-atlas viewpoint absorbs all such differences.
