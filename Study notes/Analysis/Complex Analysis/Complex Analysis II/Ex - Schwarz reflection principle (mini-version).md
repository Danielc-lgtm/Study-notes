---
type: exercise
subject: complex-analysis
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Morera's Theorem"
  - "Thm - Identity Theorem (Uniqueness of Analytic Continuation)"
tags: [analysis, complex-analysis]
---

# Problem Statement

Let $D^+ = \{z \in D(0, 1) : \operatorname{Im} z > 0\}$ — the upper half of the unit disc. Suppose $f : D^+ \to \mathbb{C}$ is holomorphic on $D^+$, continuous up to the real diameter $(-1, 1) \subseteq \partial D^+$, and *real-valued* on this real diameter:
$$f(x) \in \mathbb{R} \quad \text{for all } x \in (-1, 1).$$

Show that $f$ extends to a holomorphic function $\tilde f$ on the whole unit disc $D(0, 1)$ via the formula
$$\tilde f(z) = \begin{cases} f(z) & \operatorname{Im} z \geq 0, z \in D(0, 1) \\ \overline{f(\bar z)} & \operatorname{Im} z < 0, z \in D(0, 1)\end{cases}.$$

**Recall:**

[[Thm - Morera's Theorem]]: a continuous $f$ with $\int_\Delta f\,dz = 0$ for every triangle is holomorphic.

The conjugate of a holomorphic function is *anti-holomorphic*; but $z \mapsto \overline{f(\bar z)}$ *is* holomorphic — this is the **Schwarz reflection** of $f$.

---

# Convergent Strategy

**Problem class:** Extend a holomorphic function across a boundary line via reflection.

**Assumption pattern:** $f$ holomorphic in the upper half, continuous on the real axis where it is real-valued. The reflection $\bar f(\bar z)$ extends to the lower half.

**Theorem routing:** Define $\tilde f$ by reflection in the lower half. Check it is continuous across the real axis (using $f$ real-valued there). Verify $\tilde f$ has vanishing triangle integrals — split a triangle crossing the real axis into upper and lower halves. Apply Morera.

**Key decision point:** The reflection $\overline{f(\bar z)}$ is *holomorphic* in $z$ (one composition of conjugation and one of $f$, both of which flip orientation, so two flips cancel). The continuity on the real axis uses $f(x) \in \mathbb{R}$, which means $f(x) = \overline{f(\bar x)} = \overline{f(x)} = f(x)$ — consistent.

---

# Legal Operations Used

1. **Define $\tilde f$** on $D(0, 1)$ by reflection in the lower half.
2. **Check $\tilde f$ holomorphic in the lower half** $D^- = \{\operatorname{Im} z < 0\} \cap D(0, 1)$ via the chain rule (composition of conjugation, holomorphic $f$, and conjugation).
3. **Check continuity across the real axis** using $f$ real-valued on $(-1, 1)$.
4. **Apply Morera** with triangle integrals across the real axis.

---

# Hints

> [!note]- Hint 1
> The reflection $g(z) := \overline{f(\bar z)}$ is holomorphic in the lower half: $\bar z$ conjugates first (anti-holomorphic), $f$ is holomorphic (holomorphic), and outer conjugation (anti-holomorphic). The two anti's compose to holomorphic.

> [!note]- Hint 2
> On the real axis $x \in (-1, 1)$: $\overline{f(\bar x)} = \overline{f(x)} = f(x)$ (since $f(x)$ is real). So $\tilde f$ is continuous across the real axis.

> [!note]- Hint 3
> For Morera: any triangle $\Delta \subseteq D(0, 1)$ either lies entirely in the upper, lower, or crosses the real axis. In the first two cases, holomorphicity gives $0$. In the third, split the triangle by the real axis into upper and lower polygons; each integrates to $0$, and the shared real-axis edges cancel.

---

# Solution

The proof breaks into four steps that build the extension by reflection and verify holomorphy via Morera. Step 1 shows the reflection $g(z) = \overline{f(\bar z)}$ is holomorphic on the lower half-disc (the double-conjugation trick); Step 2 defines $\tilde f$ piecewise; Step 3 checks continuity across the real diameter using $f(x) \in \mathbb{R}$; Step 4 applies Morera by analysing triangles that lie in one half versus triangles that cross the axis. The non-obvious move is in Step 4 — for triangles crossing the axis, splitting into upper and lower polygons and using boundary-continuity limits is what closes the argument, because Goursat alone only handles the interior.

**Step 1: Check the reflection $g(z) := \overline{f(\bar z)}$ is holomorphic on $D^-$.**

Let $z \in D^-$. Then $\bar z \in D^+$, so $f(\bar z)$ is defined. Compute:
$$g(z + h) - g(z) = \overline{f(\bar z + \bar h)} - \overline{f(\bar z)} = \overline{f(\bar z + \bar h) - f(\bar z)}.$$
By holomorphicity of $f$ at $\bar z$: $f(\bar z + \bar h) - f(\bar z) = f'(\bar z)\bar h + o(|\bar h|)$. Conjugating:
$$\overline{f(\bar z + \bar h) - f(\bar z)} = \overline{f'(\bar z)} \cdot h + o(|h|).$$
So $(g(z + h) - g(z))/h \to \overline{f'(\bar z)}$ as $h \to 0$. So $g'(z) = \overline{f'(\bar z)}$, and $g$ is holomorphic on $D^-$.

**Step 2: Define $\tilde f$.**

$$\tilde f(z) = \begin{cases} f(z) & z \in D^+ \cup [(-1, 1)] \\ g(z) = \overline{f(\bar z)} & z \in D^- \end{cases}.$$

(I'm using the closed upper half-disc-with-boundary $D^+ \cup (-1, 1)$ for the first case.)

**Step 3: Continuity across $(-1, 1)$.**

For $x \in (-1, 1)$:
- $f(x)$ is the value from $D^+$ (by continuity of $f$ up to the real diameter).
- $g(x) = \overline{f(\bar x)} = \overline{f(x)}$ — by hypothesis $f(x) \in \mathbb{R}$, so $\overline{f(x)} = f(x)$.

So $f(x) = g(x)$ on the real diameter, and $\tilde f$ is continuous across $(-1, 1)$.

**Step 4: Morera's theorem.**

$\tilde f$ is continuous on $D(0, 1)$ (Step 3) and holomorphic on $D(0, 1) \setminus (-1, 1)$ (Step 1 + the original holomorphicity of $f$ on $D^+$).

For any triangle $\Delta \subseteq D(0, 1)$:

*Case 1:* $\Delta$ lies entirely in $D^+$ or entirely in $D^-$. Then $\tilde f$ is holomorphic on $\Delta$, and by [[Thm - Goursat's Theorem (Cauchy for a Triangle)|Goursat]], $\int_{\partial \Delta} \tilde f\,dz = 0$.

*Case 2:* $\Delta$ crosses the real axis. The intersection of $\Delta$ with the real axis is a line segment (since the triangle is convex). Split $\Delta$ into an upper polygon and a lower polygon by the real-axis cut. Each is contained in a slightly enlarged neighbourhood of $D^+$ or $D^-$ respectively (using continuity up to the boundary). By a limiting argument (approaching the real axis from above and below), $\int = 0$ on each polygon. The shared real-axis edges cancel (traversed once in each direction). So $\int_{\partial \Delta} \tilde f\,dz = 0$.

By [[Thm - Morera's Theorem]], $\tilde f$ is holomorphic on $D(0, 1)$. $\blacksquare$

> [!note]- Complete formal solution
> Define $\tilde f(z) = f(z)$ on closed upper half-disc, $\tilde f(z) = \overline{f(\bar z)}$ on open lower half. The reflection is holomorphic on the lower half (by the conjugation-chain-rule). Continuity on real axis from $f(x)$ real. For triangle integrals: holomorphic case trivial; cross-axis case splits into polygons, each $0$ by holomorphicity-up-to-boundary limit, shared edges cancel. Morera gives $\tilde f$ holomorphic on $D(0, 1)$. $\blacksquare$

---

# Key Takeaways

**Schwarz reflection: a model analytic continuation argument.**

The reflection principle extends a function across a boundary line by reflecting (anti-)holomorphically. The standard setup: $f$ holomorphic on the upper half-plane, continuous on the real axis where it is real-valued — the reflection $\overline{f(\bar z)}$ gives the extension. This pattern recurs for:
- Reflecting across other lines (compose with a rotation/translation to standard real axis).
- Reflecting across circles (compose with a Möbius transformation).
- Extending $\Gamma(z)$ across the real axis (in some forms of analytic continuation).

The structural requirement is that *the boundary be real-analytic* (a line or circle) and that the function take *suitable values* there (real-valued, or unitary, depending on the reflection).

**Morera as the universal "extend and check" tool.**

When we glue two functions across a curve and want to confirm the result is holomorphic, Morera is the natural tool. The argument: continuity is verified directly; triangle integrals on triangles not crossing the curve are zero by the individual holomorphicities; triangle integrals crossing the curve split into pieces, each having zero integral (by limit arguments using continuity-up-to-boundary).

**Conjugation as anti-holomorphic.**

The conjugation $z \mapsto \bar z$ is *anti-holomorphic* — its differential is the complex-conjugate-of-multiplication-by-$1$ map, which is *not* $\mathbb{C}$-linear. But the composition $z \mapsto \overline{f(\bar z)}$ is holomorphic, because *two* anti-holomorphic operations compose to holomorphic. This is the basis of the reflection principle.

The pattern: holomorphic $\circ$ anti-holomorphic = anti-holomorphic; anti-holomorphic $\circ$ holomorphic = anti-holomorphic; anti-holomorphic $\circ$ anti-holomorphic = holomorphic. The reflection $z \to \bar z \to f \to \overline{f(\bar z)}$ has *two* conjugations, so it's holomorphic in $z$.
