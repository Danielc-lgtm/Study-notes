---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Complex Potential"
  - "Def - Conformal Map"
tags: [analysis, complex-analysis, fluid-dynamics]
---

# Notation

The **Joukowski transformation** is $w = J(z) = z + 1/z$. Complex variables: $z$ in the "circle plane", $w$ in the "aerofoil plane". The Joukowski airfoil parameter family is parameterized by the centre $z_0$ and radius $a$ of a circle in the $z$-plane. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Statement

> **Theorem (Joukowski Aerofoil Construction).** The **Joukowski transformation** $J(z) = z + 1/z$ has the following properties:
>
> 1. $J$ is holomorphic on $\hat{\mathbb{C}} \setminus \{0\}$ and conformal except at the critical points $z = \pm 1$, where $J'(z) = 1 - 1/z^2 = 0$.
> 2. $J$ satisfies the symmetry $J(z) = J(1/z)$ and restricts to a biholomorphism $\{|z| > 1\} \to \hat{\mathbb{C}} \setminus [-2, 2]$ (and likewise $\{|z| < 1\} \to \hat{\mathbb{C}} \setminus [-2, 2]$).
> 3. The unit circle $\{|z| = 1\}$ maps onto the segment $[-2, 2]$ via $J(e^{i\theta}) = 2\cos\theta$.
> 4. For a circle $C$ in the $z$-plane chosen to pass through (or near) $z = 1$ with centre $z_0$ slightly off the origin, the image $J(C)$ is a closed curve in the $\zeta$-plane bounding an **aerofoil-shaped** region — a *Joukowski aerofoil* — with a sharp cusp at $\zeta = J(1) = 2$ (the **trailing edge**).
> 5. Pulling back the cylinder flow with complex potential $w_z(z) = U((z - z_0) + a^2/(z - z_0)) - i(\Gamma/(2\pi))\log((z - z_0)/a)$ via $J^{-1}$ yields the flow past the aerofoil. The **Kutta condition** — that $dw_z/dz$ vanishes at $z = 1$ — uniquely selects the physical circulation $\Gamma$, and the **Kutta–Joukowski theorem** gives the resulting lift per unit span as $L = \rho U \Gamma$.

---

# Motivation

In the early 20th century, the **Joukowski transformation** $w = z + 1/z$ was discovered as a way to construct 2D aerofoil-like shapes from circles. Combined with the known flow past a cylinder (in the $z$-plane), this gave the *first analytical model of flow past an aerofoil*, leading to the **Kutta–Joukowski theorem** relating lift to circulation.

The construction is remarkable for its simplicity:
1. Start with flow past a cylinder of radius $a$ in the $z$-plane: complex potential $w_z(z) = U(z + a^2/z) - i\Gamma/(2\pi)\log z$.
2. Apply the Joukowski transformation $\zeta = z + b^2/z$ (with $b$ a parameter) to get the corresponding flow in the $\zeta$-plane.
3. The unit circle $|z| = a$ in the $z$-plane maps under $\zeta = z + 1/z$ to a curve in the $\zeta$-plane that resembles an aerofoil — sharp trailing edge, blunt leading edge — when the circle is offset and slightly larger than the canonical unit.

The conformal mapping does the heavy lifting. Since $\zeta = z + 1/z$ is conformal away from $z = \pm 1$ (where $\zeta' = 1 - 1/z^2 = 0$), it preserves the flow's harmonic structure. The boundary condition (cylinder is a streamline in $z$-plane) transfers to the boundary condition (aerofoil is a streamline in $\zeta$-plane).

The **Kutta condition** completes the theory: among all possible circulations $\Gamma$ around the aerofoil, choose the one that makes the velocity finite at the trailing edge. This selects a specific $\Gamma$, giving the **lift** $L = \rho U \Gamma$ via the Kutta–Joukowski theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

**A circle in the $z$-plane.** The standard input. Different circles give different aerofoil shapes.

**A circle centred at $z_0 = 0$ with radius $a = 1$.** Degenerate case: $J(\{|z| = 1\}) = [-2, 2]$ on the real axis, a *segment* (degenerate aerofoil, "flat plate").

**A circle centred at $z_0$ with $|z_0|$ small and $a > 1 + |z_0|$ (so the circle passes near but not through $z = -1$ or $+1$).** Standard aerofoil: the image has a sharp trailing edge at $\zeta = 2$ (corresponding to $z = 1$) and a smooth leading edge.

**Targets (Output Amplification)**

Combine with **flow past a cylinder.** Property $D$: $w_z(z) = U(z + a^2/z)$ for flow past a cylinder of radius $a$. Amplified result $E$: flow past the corresponding aerofoil in $\zeta$-plane.

Combine with **the Kutta condition.** Property $D$: choosing $\Gamma$ to make velocity finite at trailing edge. Amplified result $E$: aerofoil **lift** $L = \rho U \Gamma$.

Combine with **Schwarz–Christoffel mapping.** Property $D$: more complicated polygonal aerofoils. Amplified result $E$: explicit conformal maps for various aerofoil profiles.

---

# Why Is It True

The Joukowski transformation $J(z) = z + 1/z$ has the following key properties:

1. **Conformal except at $z = \pm 1$.** $J'(z) = 1 - 1/z^2 = 0$ exactly at $z = \pm 1$.

2. **Maps the unit circle $|z| = 1$ to a segment.** On $|z| = 1$, $z = e^{i\theta}$, $1/z = e^{-i\theta}$, so $J(e^{i\theta}) = e^{i\theta} + e^{-i\theta} = 2\cos\theta \in [-2, 2]$, a real segment. The unit circle becomes the slit $[-2, 2]$.

3. **Two-sheet covering.** $J(z) = J(1/z)$ (substitute: $1/z + z = z + 1/z$ — identical). So the exterior $\{|z| > 1\}$ and interior $\{|z| < 1\}$ of the unit circle both map onto $\hat{\mathbb{C}}\setminus[-2, 2]$. The Joukowski map is two-to-one when restricted to $\{|z| \neq 1\}$.

4. **Behaviour at $z = \infty$.** $J(z) = z + 1/z \approx z$ for $|z|$ large. So the map is asymptotically the identity at infinity, preserving the "flow at infinity" structure.

For an aerofoil construction: offset the circle so its centre is at $z_0$ with $|z_0|$ small, and slightly enlarge so it just touches $z = 1$ (so the trailing edge $\zeta = J(1) = 2$ is at a single point — a *cusp* — giving the sharp trailing edge). The image is then a closed curve in the $\zeta$-plane, looking like a stretched teardrop — the Joukowski aerofoil.

The flow past the aerofoil is obtained by *conformally pulling back* the flow past the original circle. Conformal maps preserve harmonicity, so the velocity potential and stream function transfer cleanly.

---

# What Makes This Hard

The non-obvious step is the **Kutta condition**: among all flows past the aerofoil (parameterized by circulation $\Gamma$), select the one with finite velocity at the trailing edge. In the $z$-plane (the circle), this corresponds to selecting $\Gamma$ such that the rear stagnation point of the cylinder flow is at $z = 1$ (the preimage of the cusp). Without this condition, the velocity would be infinite at the cusp, an unphysical scenario.

A common confusion is between "the Joukowski transformation" (a specific conformal map) and "Joukowski aerofoils" (the resulting shapes). The former is a tool; the latter is the output.

---

# Rederivation Scaffold

**High-level strategy:**
The Joukowski transformation $w = z + 1/z$ maps a circle in the $z$-plane to an aerofoil-shaped curve in the $w$-plane. Combined with cylinder flow in the $z$-plane and conformal pullback, this gives flow past the aerofoil. Kutta condition selects the unique circulation giving finite trailing-edge velocity.

**Subgoal decomposition:**

1. **Verify Joukowski maps unit circle to $[-2, 2]$.** $J(e^{i\theta}) = 2\cos\theta$, real interval.

2. **Verify Joukowski maps the unit-circle exterior conformally to $\mathbb{C}\setminus[-2, 2]$.** Standard verification using $J'(z) = 1 - 1/z^2 \neq 0$ for $|z| \neq 1$ and the two-to-one property.

3. **Apply Joukowski to a slightly off-centred circle.** Image is an aerofoil-shaped curve.

4. **Pull back the cylinder flow.** Complex potential in $z$-plane: $w_z(z) = U(z + a^2/z)$ (cylinder), maybe with added circulation. Transform: the $\zeta$-plane potential is $w_\zeta(\zeta) = w_z(J^{-1}(\zeta))$, where $J^{-1}$ is the appropriate branch on the exterior.

5. **Kutta condition.** Choose $\Gamma$ so that the rear stagnation point of the $z$-plane flow is at $z = 1$ (the preimage of the trailing edge $\zeta = 2$). This makes the velocity bounded at the trailing edge.

---

# Formal Proof

> [!note]- Mathematical content of the Joukowski construction
>
> **The Joukowski transformation** is $J : \hat{\mathbb{C}}\setminus\{0\} \to \hat{\mathbb{C}}$, $J(z) = z + 1/z$.
>
> **Property 1: Conformal except at $z = \pm 1$.** $J'(z) = 1 - 1/z^2$, vanishing only at $z = \pm 1$. Elsewhere, $J$ is conformal.
>
> **Property 2: Unit circle to segment $[-2, 2]$.** On $|z| = 1$: $z = e^{i\theta}$, $J(e^{i\theta}) = e^{i\theta} + e^{-i\theta} = 2\cos\theta \in [-2, 2]$. As $\theta$ varies over $[0, 2\pi)$, $2\cos\theta$ traces $[-2, 2]$ (twice, once for $\theta \in [0, \pi]$, once for $\theta \in [\pi, 2\pi]$).
>
> **Property 3: Symmetry $J(z) = J(1/z)$.** $J(1/z) = 1/z + z = z + 1/z = J(z)$. So the map identifies $z$ with $1/z$, giving a $2$-to-$1$ covering of $\mathbb{C}\setminus[-2, 2]$ from $\{|z| > 1\} \cup \{|z| < 1\}$.
>
> Restricting to the exterior $\{|z| > 1\}$: $J : \{|z| > 1\} \to \mathbb{C}\setminus[-2, 2]$ is a biholomorphism (since the symmetry pairs each $\{|z| > 1\}$ with $\{|z| < 1\}$ to give a $2$-to-$1$ cover, but restricting to one of the two yields a $1$-to-$1$ cover).
>
> **Aerofoil construction (informal).** Let $C$ be a circle in the $z$-plane with centre $z_0$ near $0$ and radius $a$ slightly greater than $|z_0 - 1|$, so $C$ passes very close to (or just touches) $z = 1$. The image $J(C)$ is a closed curve in the $\zeta$-plane that:
> - Has a sharp cusp at $\zeta = J(1) = 2$ (because $J$ has a critical point at $z = 1$, which "pinches" any curve passing through it).
> - Has a rounded leading edge near $\zeta = J(z_0 - a) \approx 2\operatorname{Re}(z_0) - 2a$ (or similar, depending on $z_0$).
> - Is the boundary of a region resembling an aerofoil profile.
>
> **Flow past the aerofoil (informal).** The flow past a cylinder $|z - z_0| = a$ in the $z$-plane is known: complex potential $w_z(z) = U((z - z_0) + a^2/(z - z_0)) - i(\Gamma/(2\pi))\log((z - z_0)/a)$, where $U$ is the uniform stream speed at $\infty$ and $\Gamma$ is the circulation. The boundary of the cylinder is a streamline ($\psi = $ const).
>
> Pulling back via $J^{-1}$ (using the exterior branch): $w_\zeta(\zeta) = w_z(J^{-1}(\zeta))$. This is the complex potential for flow past the Joukowski aerofoil $J(C)$ in the $\zeta$-plane.
>
> **Kutta condition.** The cusp at $\zeta = 2$ corresponds to $z = 1$, where $J$ has a critical point and the velocity $dw_z/dz \cdot 1/J'(z) = (dw_z/dz)/(1 - 1/z^2)$ would generically be infinite. The Kutta condition: choose $\Gamma$ so that $dw_z/dz$ vanishes at $z = 1$ (i.e., $z = 1$ is a stagnation point of the cylinder flow), making the velocity finite at $\zeta = 2$. The unique such $\Gamma$ is determined by the geometry (depends on $z_0, a, U$, and the angle of attack).
>
> **Lift (Kutta–Joukowski).** With this $\Gamma$, the **Kutta–Joukowski theorem** gives the lift per unit span as $L = \rho U \Gamma$, where $\rho$ is the fluid density. $\blacksquare$
>
> *Reference: Acheson, "Elementary Fluid Dynamics", Chapter 4; or any classical aerodynamics text.*

---

# Cross-Field Exercise Suggestions

**Verify $J(\{|z| = 1\}) = [-2, 2]$.** Direct substitution as above.

**Compute the trailing-edge angle.** For a Joukowski aerofoil with centre $z_0 \neq 0$ but radius such that the circle passes through $z = 1$: compute the angle of the cusp at $\zeta = 2$. The cusp angle is the angle subtended by the two tangent lines to $J(C)$ at $\zeta = 2$. For an offset circle, the angle is determined by the offset direction. Standard result: the cusp is a "zero-angle" cusp for the basic Joukowski profile, becoming non-zero with the Kármán–Trefftz modification.

**Kutta condition explicit.** For a circle centred at $z_0 = -\epsilon + i\eta$ (small real and imaginary offsets) with radius $a = |1 - z_0|$, compute the circulation $\Gamma$ that places a stagnation point at $z = 1$. Result: $\Gamma = 4\pi U a \sin(\alpha + \beta)$, where $\alpha$ is the angle of attack and $\beta$ is related to the circle's offset. See classical aerodynamics texts.

**Lift coefficient.** With the Kutta circulation, the lift per unit span is $L = \rho U\Gamma$. The lift coefficient $C_L = L/((1/2)\rho U^2 c) = 2\pi\sin(\alpha + \beta)\cdot$ (geometric factor depending on aerofoil thickness), recovering the classical $C_L = 2\pi\alpha$ formula for thin aerofoils at small angle of attack.

---

# Bridges

- **[[Def - Complex Potential]]** — the framework for 2D flow.

- **[[Def - Conformal Map]]** — Joukowski is a conformal map between the cylinder and aerofoil exteriors.

- **[[Ex - Flow past a cylinder via complex potential]]** — the source flow in the $z$-plane.

- **[[Ex - The Joukowski transformation maps a circle to an aerofoil]]** — exercise verifying the mapping.

---

# Unlocked by This

> [!tip] Kutta–Joukowski Theorem *(from Aerodynamics)*
> Lift on an aerofoil in 2D inviscid flow: $L = \rho U \Gamma$, independent of aerofoil shape (only depends on circulation). Foundational result of classical aerodynamics.

> [!tip] Schwarz–Christoffel Mapping for Polygonal Aerofoils *(from Applied Math)*
> Generalization to more general aerofoil shapes via [[Ex - Schwarz–Christoffel for a polygon|Schwarz–Christoffel transformations]].

> [!tip] Thin Airfoil Theory *(from Aerodynamics)*
> Linearization of the Joukowski-type analysis for thin aerofoils gives the lift coefficient $C_L = 2\pi\alpha$ (for angle of attack $\alpha$), a workhorse of aircraft design.
