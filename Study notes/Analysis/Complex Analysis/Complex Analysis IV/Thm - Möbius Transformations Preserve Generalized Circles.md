---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Möbius Transformation"
tags: [analysis, complex-analysis, geometry]
---

# Notation

A **generalized circle** in $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ is either a circle in $\mathbb{C}$ or a line in $\mathbb{C}$ (which corresponds to a circle through $\infty$ on the Riemann sphere). Möbius transformation $T(z) = (az + b)/(cz + d)$ with $ad - bc \neq 0$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

Möbius transformations have a beautiful geometric property: they map **generalized circles** (circles and lines) to generalized circles. So a circle gets sent to either a circle or a line; a line gets sent to either a circle or a line. The class of circle-or-line is preserved as a single class.

This is the geometric content of Möbius transformations. Combined with triple transitivity (any three points map to any three points), it explains why Möbius transformations are *the* natural way to map between simple domains: a domain bounded by a generalized circle can be mapped via Möbius to any other domain bounded by a generalized circle, with the boundary mapping preserved.

The proof has a clean structure: every Möbius transformation factors as compositions of three simpler maps — translations, scalings, and inversions $z \mapsto 1/z$. Each of these preserves generalized circles individually, so the composition does too.

This theorem is used constantly in applied complex analysis: mapping the upper half-plane to the unit disc (boundaries are line and circle, both generalized circles), constructing conformal maps between half-planes and discs, etc.

---

# Sources and Targets

**Sources (Input Broadening)**

**Any Möbius transformation.** Property $B$: the standard form $(az + b)/(cz + d)$, $ad - bc \neq 0$.

**Composition of Möbius transformations.** Property $B$: a series of Möbius operations. Bridge: each preserves generalized circles, so the composition does too.

**Inversion in a circle.** Property $B$: not exactly a Möbius transformation, but related. Bridge: the geometric inversion (preserving the generalized-circle class) and the Möbius transformation $z \mapsto 1/z$ are closely related.

**Targets (Output Amplification)**

Combine with **specific Möbius transformations.** Property $D$: an explicit map (e.g., $z \mapsto (z - i)/(z + i)$). Amplified result $E$: identify which generalized circle the boundary of the source domain maps to. The boundary of $\mathbb{H}$ is $\mathbb{R}$ (a line); the image is the circle $|w| = 1$ (the unit circle, since $|w| = |(z-i)/(z+i)| = |z-i|/|z+i| = 1$ for $z$ real).

Combine with **classification of domains by their boundary type.** Property $D$: a domain bounded by a generalized circle. Amplified result $E$: the conformal type of the domain is one of three (interior of a generalized circle, exterior of a generalized circle, or "between" two generalized circles).

---

# Why Is It True

The proof factors the Möbius transformation into elementary pieces. Every $T(z) = (az + b)/(cz + d)$ with $c \neq 0$ can be written as
$$T(z) = \frac{a}{c} + \frac{bc - ad}{c^2}\cdot\frac{1}{z + d/c},$$
a composition of: translation by $d/c$, inversion $z \mapsto 1/z$, scaling by $(bc - ad)/c^2$, translation by $a/c$.

If $c = 0$: $T(z) = (a/d) z + b/d$, just a scaling-and-translation.

So every Möbius transformation is a composition of:
- Translations $z \mapsto z + b$
- Scalings $z \mapsto az$ (including rotations when $|a| = 1$)
- Inversion $z \mapsto 1/z$

Each of these preserves the class of generalized circles:
- **Translations**: clearly preserve circles (as circles) and lines (as lines).
- **Scalings**: same (scale by $|a|$, rotate by $\arg a$).
- **Inversion**: maps circles through $0$ to lines (not through $0$), lines not through $0$ to circles through $0$, and other circles/lines to other circles/lines. Specifically: a generalized circle can be written algebraically as $A|z|^2 + Bz + \bar B \bar z + C = 0$ for real $A, C$ and complex $B$, with $A \neq 0$ for circles and $A = 0$ for lines. Substituting $z \mapsto 1/z$ and clearing denominators gives an equation of the same form, with $A$ and $C$ swapped.

Composing these elementary preservations gives the full theorem.

---

# What Makes This Hard

The non-obvious step is **representing generalized circles by the unified algebraic equation** $A|z|^2 + Bz + \bar B\bar z + C = 0$. This single equation captures both circles ($A \neq 0$, the equation becomes $|z - z_0|^2 = r^2$ after completing the square) and lines ($A = 0$, becomes $Bz + \bar B \bar z + C = 0$, a real equation in $\operatorname{Re} z, \operatorname{Im} z$). Once the unified representation is in hand, checking preservation under each elementary Möbius is mechanical.

A common confusion: lines are "circles through $\infty$" on the Riemann sphere — they really do close up at the point $\infty$, so the unified concept of "generalized circle" includes both. This is what makes Möbius transformations, which can send finite points to $\infty$, preserve the class.

---

# Rederivation Scaffold

**High-level strategy:**
Factor every Möbius transformation as a composition of translations, scalings, and inversions. Each elementary type preserves generalized circles (verify case-by-case). Compose.

**Subgoal decomposition:**

1. **Unified equation for generalized circles.** Both circles and lines have the form $A|z|^2 + Bz + \bar B\bar z + C = 0$ with $A, C \in \mathbb{R}$, $B \in \mathbb{C}$.

2. **Translation $z \mapsto z + \beta$ preserves the form.** Substituting and re-arranging.

3. **Scaling $z \mapsto \lambda z$ preserves the form.** Substituting and re-arranging.

4. **Inversion $z \mapsto 1/z$ preserves the form.** Substitute $z \mapsto 1/z$ (replacing $|z|^2$ with $1/|z|^2$ etc.), multiply through by $|z|^2$.

5. **Factor Möbius as a composition of these.** $T = T_4 \circ T_3 \circ T_2 \circ T_1$ where each $T_i$ is one of translation, scaling, inversion.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **Step 1: Unified representation.** A generalized circle in $\mathbb{C}$ is a circle $|z - z_0|^2 = r^2$ (with $z_0 \in \mathbb{C}, r > 0$) or a line $\operatorname{Re}(\bar\beta(z - z_0)) = 0$ (with normal $\beta$). Expanding $|z - z_0|^2 = (z - z_0)(\bar z - \bar z_0) = |z|^2 - z\bar z_0 - \bar z z_0 + |z_0|^2$, the circle equation becomes
> $$|z|^2 - z\bar z_0 - \bar z z_0 + (|z_0|^2 - r^2) = 0.$$
> So with $A = 1, B = -\bar z_0, C = |z_0|^2 - r^2$, this fits the form $A|z|^2 + Bz + \bar B\bar z + C = 0$.
>
> Similarly, lines $az + \bar a\bar z + c = 0$ (with $a \in \mathbb{C}, c \in \mathbb{R}$) have $A = 0, B = a, C = c$.
>
> So generalized circles are exactly the sets $\{z : A|z|^2 + Bz + \bar B\bar z + C = 0\}$ with $A, C \in \mathbb{R}$, $B \in \mathbb{C}$, and $|B|^2 - AC > 0$ (the discriminant ensures the set is nonempty and a "proper" circle/line; degenerate cases are points or empty).
>
> **Step 2: Translation $z \mapsto z + \beta$.** Substituting $z = w - \beta$:
> $$A|w - \beta|^2 + B(w - \beta) + \bar B(\bar w - \bar\beta) + C = 0,$$
> $$A|w|^2 + (-A\bar\beta + B)w + (-A\beta + \bar B)\bar w + (A|\beta|^2 - B\beta - \bar B\bar\beta + C) = 0.$$
> Same form with new coefficients $A' = A, B' = B - A\bar\beta, C' = A|\beta|^2 - 2\operatorname{Re}(B\beta) + C$ — all real $A', C'$ and complex $B'$. So a generalized circle is mapped to a generalized circle.
>
> **Step 3: Scaling $z \mapsto \lambda z$.** Substituting $z = w/\lambda$ (assume $\lambda \neq 0$):
> $$A|w|^2/|\lambda|^2 + Bw/\lambda + \bar B\bar w/\bar\lambda + C = 0.$$
> Multiply by $|\lambda|^2 = \lambda\bar\lambda$:
> $$A|w|^2 + B\bar\lambda w + \bar B\lambda \bar w + C|\lambda|^2 = 0,$$
> same form. So scaling preserves generalized circles.
>
> **Step 4: Inversion $z \mapsto 1/z$.** Substituting $z = 1/w$:
> $$A/|w|^2 + B/w + \bar B/\bar w + C = 0.$$
> Multiply by $|w|^2 = w\bar w$:
> $$A + B\bar w + \bar B w + C|w|^2 = 0,$$
> i.e., $C|w|^2 + \bar B w + B\bar w + A = 0$ — same form with $A$ and $C$ swapped, and $B \to \bar B$. (Or: $A' = C, B' = \bar B, C' = A$.) Same shape. So inversion preserves generalized circles, *swapping the role of circles ($A \neq 0$) and lines through origin ($A = 0$)*: a circle through the origin (where $|z_0|^2 = r^2$, hence $C = 0$) maps under inversion to a line ($C' = A = 1 \neq 0$, $A' = C = 0$, so the new $A$-coefficient is zero — it's a line).
>
> **Step 5: Factor Möbius.** For $c \neq 0$:
> $$T(z) = \frac{az + b}{cz + d} = \frac{a}{c} + \frac{b - ad/c}{cz + d} = \frac{a}{c} + \frac{(bc - ad)/c}{cz + d} = \frac{a}{c} + \frac{(bc - ad)/c^2}{z + d/c}.$$
> So $T = (\text{translate by } a/c) \circ (\text{scale by } (bc - ad)/c^2) \circ (\text{inversion}) \circ (\text{translate by } d/c)$.
>
> For $c = 0$: $T(z) = (a/d)z + b/d$ is just a scaling followed by translation.
>
> Composing transformations that each preserve generalized circles, $T$ preserves them. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Upper half-plane to unit disc.** The Cayley transform $z \mapsto (z - i)/(z + i)$ maps $\mathbb{H}$ to $\mathbb{D}$. The boundary $\mathbb{R}$ (a line, a generalized circle) maps to the boundary of $\mathbb{D}$, which by this theorem must be a generalized circle. Direct computation: $z = x \in \mathbb{R}$, $|T(x)| = |x - i|/|x + i| = \sqrt{x^2 + 1}/\sqrt{x^2 + 1} = 1$. So the image is the unit circle.

**Inversion in a circle versus the Möbius map $1/z$.** The inversion in the unit circle (geometric: $z \mapsto z/|z|^2$) and the Möbius map $z \mapsto 1/z$ differ by complex conjugation: $1/z = \bar z/|z|^2$. Both preserve generalized circles, with the second being holomorphic and the first anti-holomorphic.

**Cross-ratio.** The cross-ratio $(z_1, z_2; z_3, z_4) = (z_1 - z_3)(z_2 - z_4)/((z_1 - z_4)(z_2 - z_3))$ is preserved by Möbius transformations. Four points lie on a generalized circle iff their cross-ratio is *real*. This connects the preservation of generalized circles to the algebraic invariance of the cross-ratio.

---

# Bridges

- **[[Def - Möbius Transformation]]** — the object.

- **[[Def - Conformal Map]]** — Möbius transformations are conformal (preserve angles), of which preserving circles/lines is a corollary (locally, angles preserve generalized circles).

- **[[Ex - Conformal map from upper half-plane to disc]]** — uses this theorem.

---

# Unlocked by This

> [!tip] Riemann Sphere as Compactification *(from Algebraic Topology)*
> The view of $\hat{\mathbb{C}}$ as $S^2$ makes circles and lines unified: stereographic projection maps a circle on $S^2$ not through the north pole to a circle in $\mathbb{C}$, and a circle through the north pole to a line in $\mathbb{C}$. Möbius transformations are the conformal automorphisms of $S^2$ in this picture.

> [!tip] Apollonius Problems in Geometry *(from Plane Geometry)*
> Many classical geometry problems involving circles (Apollonius's problem: find circles tangent to three given circles) become tractable by mapping via Möbius to a position where one of the circles is at infinity (a line).
