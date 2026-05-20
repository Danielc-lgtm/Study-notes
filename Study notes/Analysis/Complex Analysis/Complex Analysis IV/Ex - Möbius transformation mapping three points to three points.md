---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐"
prereqs:
  - "Def - Möbius Transformation"
  - "Thm - Möbius Transformations Preserve Generalized Circles"
tags: [analysis, complex-analysis]
---

# Problem Statement

Find the Möbius transformation $T$ that maps $\{0, 1, \infty\}$ to $\{1, i, -1\}$ in order: $T(0) = 1, T(1) = i, T(\infty) = -1$.

**Recall:**

![[Def - Möbius Transformation#The Definition]]

Triple transitivity: the Möbius group acts transitively on triples of distinct points — given any two such triples, there is a *unique* Möbius transformation mapping one to the other.

---

# Convergent Strategy

**Problem class:** Construct an explicit Möbius transformation with prescribed action on three points. The standard tool is the *cross-ratio*, which is the unique Möbius-invariant of four points.

**Assumption pattern:** Three input points $\{0, 1, \infty\}$ and three output points $\{1, i, -1\}$. The Möbius group acts triply transitively, so a unique $T$ exists.

**Theorem routing:** Use the **cross-ratio**: $(z, 0, 1, \infty) = (z - 1)/(z - \infty)\cdot(0 - \infty)/(0 - 1) = (z - 1)/(\text{informally})$ ... Actually the cleanest formulation: send each triple to $\{0, 1, \infty\}$, then compose.

**Key decision point:** Set up the Möbius map directly as $(az + b)/(cz + d)$ and solve four equations (three point-conditions + normalization).

---

# Legal Operations Used

1. **Write $T(z) = (az + b)/(cz + d)$** with unknowns $a, b, c, d$ (modulo scalar; 3 essential parameters).
2. **Apply $T(0) = 1$**: $b/d = 1$, so $b = d$.
3. **Apply $T(\infty) = -1$**: $a/c = -1$, so $a = -c$.
4. **Apply $T(1) = i$**: $(a + b)/(c + d) = i$, i.e., $(-c + d)/(c + d) = i$ (substituting from above).
5. **Solve for the ratio $c/d$**: $(-c + d)/(c + d) = i$ gives $d - c = i(c + d) = ic + id$, so $d - id = c + ic$, $d(1 - i) = c(1 + i)$, $c/d = (1 - i)/(1 + i) = -i$.
6. **Normalize**: pick $d = 1$, so $c = -i$, $a = -c = i$, $b = d = 1$. So $T(z) = (iz + 1)/(-iz + 1)$.

Alternative via cross-ratio: see solution.

---

# Hints

> [!note]- Hint 1
> Set $T(z) = (az + b)/(cz + d)$ and use $T(0), T(1), T(\infty)$ to get equations.

> [!note]- Hint 2
> $T(0) = b/d$, $T(\infty) = a/c$, $T(1) = (a + b)/(c + d)$.

> [!note]- Hint 3
> Cross-ratio approach: the cross-ratio $(z, z_1, z_2, z_3)$ is Möbius-invariant. So $(T(z), T(z_1), T(z_2), T(z_3)) = (z, z_1, z_2, z_3)$ defines $T(z)$ implicitly.

---

# Solution

**Method 1: Direct equations**

**Step 1: Set up**

$T(z) = (az + b)/(cz + d)$ with $ad - bc \neq 0$. We have 4 unknowns, but scalar multiples of $(a, b, c, d)$ give the same Möbius map, so 3 essential parameters.

**Step 2: Apply the three conditions**

> [!note]- Derivation
> - $T(0) = b/d = 1$, so $b = d$.
> - $T(\infty) = a/c = -1$, so $a = -c$.
> - $T(1) = (a + b)/(c + d) = i$.
>
> Substituting from the first two: $a = -c, b = d$. So $(a + b)/(c + d) = (-c + d)/(c + d) = i$.

**Step 3: Solve for the ratio $c/d$**

> [!note]- Derivation
> From $(-c + d)/(c + d) = i$: $-c + d = i(c + d) = ic + id$, so $d - id = c + ic$, giving $d(1 - i) = c(1 + i)$, hence $c/d = (1 - i)/(1 + i)$.
>
> Rationalize: $(1 - i)/(1 + i) = (1 - i)^2/((1 + i)(1 - i)) = (1 - 2i + i^2)/(1 - i^2) = (1 - 2i - 1)/(1 + 1) = -2i/2 = -i$.
>
> So $c/d = -i$.

**Step 4: Normalize**

> [!note]- Derivation
> Set $d = 1$, then $b = d = 1$, $c = -i$, $a = -c = i$. The Möbius transformation:
> $$T(z) = \frac{iz + 1}{-iz + 1}.$$

**Step 5: Verify**

> [!note]- Derivation
> - $T(0) = (0 + 1)/(0 + 1) = 1$ ✓
> - $T(\infty) = i/(-i) = -1$ ✓
> - $T(1) = (i + 1)/(-i + 1) = (1 + i)/(1 - i)$. Rationalize: $(1 + i)(1 + i)/((1 - i)(1 + i)) = (1 + 2i + i^2)/(1 - i^2) = (2i)/(2) = i$ ✓

**Method 2: Cross-ratio**

> [!note]- Derivation
> The cross-ratio $(z, z_1, z_2, z_3) := \frac{(z - z_2)(z_1 - z_3)}{(z - z_3)(z_1 - z_2)}$ is Möbius-invariant. So if $T(z_i) = w_i$ for $i = 1, 2, 3$, then $T(z)$ satisfies $(T(z), w_1, w_2, w_3) = (z, z_1, z_2, z_3)$.
>
> With $(z_1, z_2, z_3) = (0, 1, \infty)$ and $(w_1, w_2, w_3) = (1, i, -1)$:
> $(z, 0, 1, \infty)$ simplifies (using limit conventions for $\infty$): the cross-ratio with $z_3 = \infty$ is $(z - z_2)/(z_1 - z_2) = (z - 1)/(0 - 1) = -(z - 1) = 1 - z$.
> Similarly $(w, 1, i, -1) = (w - i)(1 - (-1))/((w - (-1))(1 - i)) = 2(w - i)/((w + 1)(1 - i))$.
>
> Setting equal: $2(T(z) - i)/((T(z) + 1)(1 - i)) = 1 - z$, then solve for $T(z)$. (After algebra, recovers $T(z) = (iz + 1)/(1 - iz)$, same as Method 1.)

> [!note]- Complete formal solution
> Set $T(z) = (az + b)/(cz + d)$. The conditions $T(0) = 1, T(\infty) = -1, T(1) = i$ give:
> - $b/d = 1$, so $b = d$.
> - $a/c = -1$, so $a = -c$.
> - $(a + b)/(c + d) = i$. Substituting: $(d - c)/(c + d) = i$, so $d - c = i(c + d)$, $d(1 - i) = c(1 + i)$, $c/d = (1 - i)/(1 + i) = -i$.
>
> Normalize $d = 1$: $b = 1, c = -i, a = i$. So
> $$T(z) = \frac{iz + 1}{-iz + 1} = \frac{1 + iz}{1 - iz}.$$
>
> Verification: $T(0) = 1, T(1) = (1 + i)/(1 - i) = i, T(\infty) = i/(-i) = -1$. ✓ $\blacksquare$

---

# Key Takeaways

**Trigger-reaction pattern — "Möbius transformation specified by three point images" → "solve the linear system in $(a, b, c, d)$".** The four parameters of $(az + b)/(cz + d)$ modulo scalar give 3 essential parameters, exactly matched by 3 point conditions. So the Möbius transformation is uniquely determined by its action on three points.

**The cross-ratio is the Möbius-invariant.** $(z, z_1, z_2, z_3)$ is preserved by every Möbius transformation. This is the conceptual organizing principle for Möbius theory: the cross-ratio classifies four-point configurations up to Möbius equivalence.

**The standard normalization is $\{0, 1, \infty\}$.** The Möbius transformation $M_{z_1, z_2, z_3}(z) := $ unique Möbius sending $(z_1, z_2, z_3)$ to $(0, 1, \infty)$ is the "canonical" Möbius for any triple. Composing with another such normalization gives the answer to any "three to three" problem.

**Verify with a fourth point.** A common error in Möbius problems is to mishandle the $\infty$ point or sign conventions. Always verify your $T$ against a known correspondence — for instance, in this case, check that the unit interval $[0, 1]$ on the real axis maps to a specific arc (an arc of the unit circle, by Möbius preservation of generalized circles).

**Generalization — the conformal-equivalence question.** Two triples of points in $\hat{\mathbb{C}}$ are conformally equivalent (via a Möbius map) iff their cross-ratios are equal. The cross-ratio is the unique conformal invariant of four points; for three points, any two triples are conformally equivalent.
