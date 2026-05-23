---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Möbius Transformation"
  - "Def - Conformal Map"
  - "Thm - Möbius Transformations Preserve Generalized Circles"
tags: [analysis, complex-analysis]
---

# Problem Statement

Show that $T(z) = (z - i)/(z + i)$ is a biholomorphism from the upper half-plane $\mathbb{H} = \{\operatorname{Im} z > 0\}$ to the unit disc $\mathbb{D} = \{|w| < 1\}$. Verify: (a) $T(i) = 0$, (b) the real line $\mathbb{R}$ maps to the unit circle $S^1$, and (c) $T(\infty) = 1$ (in the Riemann-sphere sense).

**Recall:**

![[Def - Conformal Map#The Definition]]

A biholomorphism is a holomorphic bijection with holomorphic inverse.

Möbius transformations $T(z) = (az + b)/(cz + d)$ with $ad - bc \neq 0$ are biholomorphisms $\hat{\mathbb{C}} \to \hat{\mathbb{C}}$.

---

# Convergent Strategy

**Problem class:** Verify a specific Möbius transformation maps one canonical domain to another. The Cayley transform is the standard biholomorphism $\mathbb{H} \to \mathbb{D}$.

**Assumption pattern:** $T(z) = (z - i)/(z + i)$, $\mathbb{H}$ source, $\mathbb{D}$ target. Use Möbius properties to verify the mapping.

**Theorem routing:** Three verifications: (a) compute $T(i)$ directly; (b) show $|T(x)| = 1$ for $x \in \mathbb{R}$; (c) compute $T(\infty)$ by limit or by the formula $a/c$.

**Key decision point:** Use Möbius "preserves generalized circles" to know the boundary $\mathbb{R}$ maps to a circle (in $\hat{\mathbb{C}}$). The image is then either inside-of-circle or outside-of-circle; check one interior point to determine which.

---

# Legal Operations Used

1. **Compute $T(i)$** directly: $(i - i)/(i + i) = 0$.
2. **Compute $|T(x)|$ for $x \in \mathbb{R}$**: $|x - i|/|x + i| = \sqrt{x^2 + 1}/\sqrt{x^2 + 1} = 1$.
3. **Apply [[Thm - Möbius Transformations Preserve Generalized Circles|Möbius preserves circles]]** to conclude $T(\mathbb{R})$ is a generalized circle. Combined with $|T(x)| = 1$ on $\mathbb{R}$, $T(\mathbb{R}) = S^1$.
4. **Determine $T(\mathbb{H})$**: it must be one of $\mathbb{D}$ or $\mathbb{C}\setminus\overline{\mathbb{D}}$ (the two complementary regions of $S^1$). Test $z = i \in \mathbb{H}$: $T(i) = 0 \in \mathbb{D}$. So $T(\mathbb{H}) \subseteq \mathbb{D}$.
5. **Verify surjectivity** via the inverse Möbius transformation.

---

# Hints

> [!note]- Hint 1
> Direct: $T(i) = (i - i)/(i + i) = 0/2i = 0$.

> [!note]- Hint 2
> For $x \in \mathbb{R}$: $|T(x)|^2 = |x - i|^2/|x + i|^2 = (x^2 + 1)/(x^2 + 1) = 1$. So $T(\mathbb{R}) \subseteq S^1$.

> [!note]- Hint 3
> By [[Thm - Möbius Transformations Preserve Generalized Circles|Möbius preserving generalized circles]], $T(\mathbb{R})$ is a generalized circle in $\hat{\mathbb{C}}$. Combined with $|T(x)| = 1$ on $\mathbb{R}$, $T(\mathbb{R})$ is a subset of $S^1$. Since $T(\mathbb{R} \cup \{\infty\})$ is a closed curve (generalized circle), and contains the line $S^1$ except possibly one point, $T(\mathbb{R}\cup\{\infty\}) = S^1$.

> [!note]- Hint 4
> $T$ maps the boundary of $\mathbb{H}$ (namely $\mathbb{R}\cup\{\infty\}$) to the boundary of one of the two regions determined by $S^1$. Test which region $\mathbb{H}$ maps to: $i \in \mathbb{H}$ goes to $T(i) = 0 \in \mathbb{D}$.

---

# Solution

The proof breaks into six short verification steps that confirm the Cayley transform $T(z) = (z-i)/(z+i)$ is a biholomorphism $\mathbb{H} \to \mathbb{D}$. Steps 1–4 verify the explicit boundary behaviour — $T(i) = 0$, $|T(x)| = 1$ for real $x$, $T(\infty) = 1$, and $T(\mathbb{R} \cup \{\infty\}) = S^1$ via the Möbius "preserves generalized circles" theorem; Step 5 nails down the target region as the disc rather than its complement by testing one interior point ($T(i) = 0 \in \mathbb{D}$); Step 6 invokes the explicit inverse to confirm biholomorphy. The non-obvious move is in Step 5 — Möbius theory plus connectedness gives "boundary maps to boundary, interior to one of the two components" but doesn't say *which*, so a single sample point is what closes the argument.

**Step 1: $T(i) = 0$**

$T(i) = (i - i)/(i + i) = 0/(2i) = 0$. ✓

**Step 2: $T(\mathbb{R}) \subseteq S^1$**

> [!note]- Derivation
> For $x \in \mathbb{R}$:
> $$|T(x)|^2 = \frac{|x - i|^2}{|x + i|^2} = \frac{x^2 + 1}{x^2 + 1} = 1.$$
> So $|T(x)| = 1$, meaning $T(x) \in S^1$ for every $x \in \mathbb{R}$.

**Step 3: $T(\mathbb{R}\cup\{\infty\}) = S^1$**

> [!note]- Derivation
> By [[Thm - Möbius Transformations Preserve Generalized Circles|Möbius theorem]], $T(\mathbb{R}\cup\{\infty\})$ is a generalized circle in $\hat{\mathbb{C}}$. Combined with $T(x) \in S^1$ for $x \in \mathbb{R}$ and $T(\infty) = 1 \in S^1$ (computed below), this generalized circle is contained in $S^1$. Since a generalized circle contained in another generalized circle and not just a point must equal it (both are closed curves on the sphere), $T(\mathbb{R}\cup\{\infty\}) = S^1$.

**Step 4: $T(\infty) = 1$**

> [!note]- Derivation
> $T(\infty) =$ limit of $T(z)$ as $|z| \to \infty$ $= \lim_{|z| \to \infty}(z - i)/(z + i) = \lim 1 \cdot (1 - i/z)/(1 + i/z) = 1$.
>
> Alternatively, by the Möbius formula $T(\infty) = a/c$ with $a = 1, c = 1$: $T(\infty) = 1$. ✓

**Step 5: $T(\mathbb{H}) = \mathbb{D}$**

> [!note]- Derivation
> $T$ is a Möbius transformation, hence a bijection of $\hat{\mathbb{C}}$ to itself. The complement of $S^1$ in $\hat{\mathbb{C}}$ has two components: $\mathbb{D}$ (open unit disc) and $\mathbb{C}\setminus\overline{\mathbb{D}}$ (exterior, including $\infty$). $T$ maps $\hat{\mathbb{C}}\setminus(\mathbb{R}\cup\{\infty\}) = \mathbb{H}\cup(-\mathbb{H})$ (where $-\mathbb{H} = \{\operatorname{Im} z < 0\}$ is the lower half-plane) to $\hat{\mathbb{C}}\setminus S^1 = \mathbb{D} \cup (\mathbb{C}\setminus\overline{\mathbb{D}})$. By continuity (and connectedness of $\mathbb{H}$ and $-\mathbb{H}$), each half-plane maps to one of the components.
>
> Test: $i \in \mathbb{H}$, $T(i) = 0 \in \mathbb{D}$. So $T(\mathbb{H}) \subseteq \mathbb{D}$, hence $T(\mathbb{H}) = \mathbb{D}$ (by surjectivity).
>
> By symmetry, $T(-\mathbb{H}) = \mathbb{C}\setminus\overline{\mathbb{D}}$.

**Step 6: Biholomorphism**

> [!note]- Derivation
> $T$ is a Möbius transformation (the inverse $T^{-1}(w) = i(1 + w)/(1 - w)$ is also Möbius), so $T$ is biholomorphic from $\hat{\mathbb{C}}\setminus\{-i\}$ (where the original $T$ has a pole) to $\hat{\mathbb{C}}\setminus\{1\}$. Restricted to $\mathbb{H}$ (which avoids $-i$), $T : \mathbb{H} \to \mathbb{D}$ is biholomorphic.

> [!note]- Complete formal solution
> Define $T(z) = (z - i)/(z + i)$.
>
> **$T(i) = 0$:** $T(i) = (i - i)/(i + i) = 0$.
>
> **$|T(x)| = 1$ for $x \in \mathbb{R}$:** $|T(x)|^2 = |x - i|^2/|x + i|^2 = (x^2 + 1)/(x^2 + 1) = 1$.
>
> **$T(\infty) = 1$:** $\lim_{|z| \to \infty} T(z) = \lim (z - i)/(z + i) = 1$, or by the formula $a/c = 1/1 = 1$.
>
> **$T(\mathbb{R}\cup\{\infty\}) = S^1$:** By [[Thm - Möbius Transformations Preserve Generalized Circles|Möbius preserves generalized circles]], $T(\mathbb{R}\cup\{\infty\})$ is a generalized circle. It is contained in $S^1$ by the previous calculations, so equals $S^1$.
>
> **$T(\mathbb{H}) = \mathbb{D}$:** $\mathbb{H}$ is one of two components of $\hat{\mathbb{C}}\setminus(\mathbb{R}\cup\{\infty\})$; by continuity, $T(\mathbb{H})$ is one of two components of $\hat{\mathbb{C}}\setminus S^1$. Since $T(i) = 0 \in \mathbb{D}$, $T(\mathbb{H}) = \mathbb{D}$.
>
> **Biholomorphism:** $T$ is Möbius with inverse $T^{-1}(w) = i(1 + w)/(1 - w)$, also Möbius. Restricted to $\mathbb{H}$ (avoiding the pole $z = -i$), $T : \mathbb{H} \to \mathbb{D}$ is biholomorphic. $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "biholomorphism between half-plane and disc" → "Cayley transform $(z - i)/(z + i)$".** This is the canonical map, used pervasively in complex analysis. Variants include rotated or scaled versions: $z \mapsto (z - a)/(z - \bar a)$ for any $a$ in the upper half-plane gives a biholomorphism $\mathbb{H} \to \mathbb{D}$.

**Möbius preserves generalized circles + checking one interior point determines the target region.** This is the standard technique for verifying Möbius transformations of canonical domains. The boundary maps to a generalized circle by the theorem; the interior maps to one of the two components, identified by checking a single point.

**Inverse Cayley:** $T^{-1}(w) = i(1 + w)/(1 - w) = i + 2i w/(1 - w)$. Sends $0 \mapsto i$, $1 \mapsto \infty$, $-1 \mapsto 0$. Used to map disc problems back to half-plane problems.

**Combine with rotations and Blaschke factors for general $\mathbb{H} \to \mathbb{D}$ biholomorphisms.** $\operatorname{Aut}(\mathbb{H}) \cong \operatorname{PSL}_2(\mathbb{R})$ is a 3-parameter group. Composing Cayley with a Blaschke factor in $\mathbb{D}$ gives the most general biholomorphism $\mathbb{H} \to \mathbb{D}$: $T \circ B_a \circ \text{rotate}$, with $B_a$ a Blaschke factor in $\mathbb{D}$.

**Applications.** Solving Dirichlet problems on $\mathbb{H}$ via conformal mapping to $\mathbb{D}$ (Poisson on $\mathbb{D}$, pullback by $T$). The Cayley transform is the bridge — see [[Ex - Solving Dirichlet on a half-plane via conformal mapping]].
