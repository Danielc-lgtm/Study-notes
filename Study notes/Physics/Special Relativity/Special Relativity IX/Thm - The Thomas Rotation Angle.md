---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Thomas Rotation"
  - "Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation"
  - "Thm - Polar Decomposition of the Lorentz Group"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. Two [[Def - Boosts as Hyperbolic Rotations|boosts]] $\Lambda_1, \Lambda_2$ have Lorentz factors $\Gamma_1, \Gamma_2$, velocity moduli $V_1, V_2$, rapidities $\psi_1, \psi_2$, with $\chi \in [0,\pi]$ the angle between their velocities relative to the intermediate observer. The composite boost (from the [[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|composition theorem]]) has Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$ and rapidity $\psi$. The [[Def - Thomas Rotation|Thomas rotation]] angle is $\varphi_T \in [-\pi, 0]$, in the plane $\mathrm{Span}(\mathbf{V}_1, \mathbf{V}_2)$. Full registry on [[Special Relativity IX — The Lorentz Group, Structure and Classification]].

---

# Statement

> **Theorem (The Thomas rotation angle).** The Thomas rotation angle $\varphi_T$ accompanying the composition of two boosts $\Lambda_2\circ\Lambda_1$ of Lorentz factors $\Gamma_1, \Gamma_2$, velocity moduli $V_1, V_2$, at angle $\chi$, is given by
> $$\cos\varphi_T = 1 - \frac{(\Gamma_1 - 1)(\Gamma_2 - 1)}{1 + \Gamma}\sin^2\chi, \qquad \sin\varphi_T = -\sin\chi\,\frac{\Gamma_1\Gamma_2\,V_1V_2}{1+\Gamma}\left(1 + \frac{\Gamma_1}{1+\Gamma_1}\frac{\Gamma_2}{1+\Gamma_2}V_1V_2\cos\chi\right),$$
> with $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$, and $-\pi \le \varphi_T \le 0$ (clockwise). Equivalent forms:
> - **Symmetric form:** $\cos\varphi_T = \dfrac{(1 + \Gamma + \Gamma_1 + \Gamma_2)^2}{(1+\Gamma)(1+\Gamma_1)(1+\Gamma_2)} - 1.$
> - **Macfarlane (half-angle):** $\cos\dfrac{\varphi_T}{2} = \dfrac{1 + \cosh\psi + \cosh\psi_1 + \cosh\psi_2}{4\cosh(\psi/2)\cosh(\psi_1/2)\cosh(\psi_2/2)}.$
> - **Stapp / half-angle for sine:** $\sin\dfrac{\varphi_T}{2} = -\sin\chi\,\sqrt{\dfrac{(\Gamma_1-1)(\Gamma_2-1)}{2(1+\Gamma)}} = -\sin\chi\,\dfrac{\sinh(\psi_1/2)\sinh(\psi_2/2)}{\cosh(\psi/2)}.$
> - **Perpendicular boosts** ($\chi = \pi/2$, so $\Gamma = \Gamma_1\Gamma_2$): $\cos\varphi_T = \dfrac{\Gamma_1 + \Gamma_2}{1 + \Gamma_1\Gamma_2}.$

---

# Motivation

The [[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|composition theorem]] establishes that a Thomas rotation exists when two non-collinear boosts are composed; this theorem computes its angle. The motivation is to turn the qualitative statement "there is a leftover rotation" into the quantitative formula needed to compute Thomas precession, to predict the angular distortion of a sequence of boosts, and to verify the non-commutativity of velocity addition.

The formula is worth having in many equivalent forms because different problems call for different inputs. When the speeds and angle are given, the form in $\Gamma_1, \Gamma_2, \chi$ is direct. When all three Lorentz factors (including the composite $\Gamma$) are known, the symmetric form — remarkably invariant under permuting the three factors — is cleanest. When rapidities are natural (as in iterated boosts), the Macfarlane and Stapp half-angle forms in $\psi, \psi_1, \psi_2$ are simplest. The motivation for collecting all of these is that the Thomas angle is a single geometric quantity wearing many algebraic disguises, and recognising it in each disguise is part of mastering the subject.

The sign and range deserve emphasis. The Thomas rotation is always *clockwise* in the plane of the two velocities (oriented by $\mathbf{V}_1\times\mathbf{V}_2$), so $\varphi_T \in [-\pi, 0]$. This sign is physical: it determines the direction of Thomas precession, which is what makes the precession *oppose* rather than add to the magnetic precession in the spin–orbit interaction, supplying the crucial minus sign in the factor of $\tfrac12$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "two boosts at angle $\chi$ are composed." The disguised sources are the inputs from which the angle is computed.

The first disguised source is **"two perpendicular acceleration phases."** When a particle is boosted in two perpendicular directions, $\chi = \pi/2$ and the simple formula $\cos\varphi_T = (\Gamma_1+\Gamma_2)/(1+\Gamma_1\Gamma_2)$ applies. The bridge is the perpendicular-case specialisation. *Example problem:* find the frame rotation after two perpendicular boosts of equal speed.

The second disguised source is **"three known Lorentz factors."** If a problem supplies $\Gamma_1, \Gamma_2$, and the composite $\Gamma$ (perhaps measured), the symmetric form gives $\varphi_T$ without the angle $\chi$. The bridge is the symmetric form, which eliminates $\chi$ via $\Gamma$. *Example problem:* given the initial, intermediate, and final Lorentz factors of a particle, find the accumulated frame rotation.

The third disguised source is **"an infinitesimal velocity increment."** For Thomas precession one composes a finite boost with an infinitesimal one ($\Gamma_2 \to 1$, $V_2 \to 0$), and the formula linearises to $\delta\varphi_T \approx -\tfrac12(\Gamma_1 - 1)\,(\mathbf{V}_1\times d\mathbf{V}_2)/V_1^2 \cdot V_1$, the infinitesimal Thomas rotation per acceleration step. The bridge is the small-$V_2$ expansion. *Example problem:* compute the Thomas precession rate by linearising the angle in the velocity increment.

**Targets (Output Amplification)**

The conclusion is "$\varphi_T$ in terms of the speeds and angle (or the three Lorentz factors)."

Combine the conclusion with **integration around a loop**. Summing the infinitesimal Thomas angles $\delta\varphi_T$ around a closed velocity loop gives the total precession, and for circular motion the rate $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$. The further result is the Thomas precession formula. The combination is the route to atomic fine structure.

Combine the conclusion with **the non-commutativity defect**. The angle $\varphi_T$ is exactly the angle between $\mathbf{V}_1\oplus\mathbf{V}_2$ and $\mathbf{V}_2\oplus\mathbf{V}_1$, so it quantifies how much velocity addition fails to commute. The further result is the gyrogroup gyration angle. The combination is useful because it gives a measurable handle on the non-commutativity.

Combine the conclusion with **the hyperbolic-area interpretation**. The Thomas angle equals the area of the geodesic triangle traced in hyperbolic velocity space (Gauss–Bonnet, curvature $-1$). The further result is that $\varphi_T$ is the holonomy of the loop, computable as an enclosed area. The combination connects the kinematic angle to the geometry of velocity space.

---

# Why Is It True

The angle is computed by reading the rotation factor $R$ of the polar decomposition $\Lambda_2\Lambda_1 = S\circ R$ off the explicit matrix, and there is a clean intuition for the leading behaviour.

The matrix computation is direct but laborious. One writes $\Lambda_1$ in its adapted basis (a boost in the $(e_0, e_1)$-plane), writes $\Lambda_2$ in the *semi-adapted* basis (a boost whose velocity makes angle $\chi$ with $e_1$, components $(V_2\cos\chi, V_2\sin\chi, 0)$), multiplies, and applies the polar decomposition. The boost factor $S$ is read off the image of $e_0$ — its Lorentz factor is $\Gamma = e_0\cdot\Lambda_2\Lambda_1(e_0) = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$ — and the rotation factor $R = S^{-1}\Lambda_2\Lambda_1$ is then a rotation in the $(e_1, e_2)$-plane whose angle is extracted from $\cos\varphi_T = R(e_1)\cdot e_1$ and $\sin\varphi_T = R(e_1)\cdot e_2$. Carrying out the algebra, with the simplifications $\cosh^2 - \sinh^2 = 1$ and $\sin^2\chi = 1 - \cos^2\chi$, yields the stated formula.

The *intuition*, which makes the result unsurprising, is the hyperbolic-triangle picture. **The Thomas angle is the angular deficit of a geodesic triangle in the hyperbolic space of velocities.** Velocity space, with the Lorentz-invariant metric, is hyperbolic three-space of curvature $-1$. A boost is a hyperbolic translation; composing $\Lambda_1$ then $\Lambda_2$ then returning to the origin traces a geodesic triangle with vertices at $\mathbf{0}$, $\mathbf{V}_1$, and the composite velocity. By the Gauss–Bonnet theorem, parallel transport of a frame around a geodesic triangle in a space of curvature $K$ returns it rotated by $-K\cdot(\text{area})$; for $K = -1$ the rotation is $+(\text{area})$, but with the orientation conventions of velocity addition it comes out as the *clockwise* Thomas rotation. So $\varphi_T$ is (minus) the area of the hyperbolic triangle, and the formula is the hyperbolic analogue of the spherical-excess formula for the area of a triangle in terms of its sides — here expressed through the Lorentz factors, which are the hyperbolic cosines of the geodesic lengths (rapidities).

This intuition immediately explains the qualitative features: the angle vanishes when the triangle degenerates to a line ($\chi = 0$, collinear boosts, zero area); it grows with the speeds (longer geodesic sides enclose more area); and it is bounded by $\pi$ (the maximal area of a hyperbolic triangle, an ideal triangle with all vertices at infinity, has angle deficit $\pi$). The Macfarlane and Stapp forms are different parametrisations of the same hyperbolic area.

---

# What Makes This Hard

The proof is a long but mechanical matrix computation, and the difficulty is bookkeeping: keeping the two boosts in compatible bases (one adapted, one semi-adapted at angle $\chi$), multiplying $4\times 4$ matrices, and extracting the rotation factor without sign errors. The non-obvious simplification is using $\Gamma = c_1c_2 + s_1s_2\cos\chi$ (the composite Lorentz factor) to collapse the intermediate expressions — without recognising this combination, the algebra does not simplify to the clean form. The common error is a sign mistake in $\sin\varphi_T$, which determines the *direction* of the rotation (clockwise, $\varphi_T < 0$) and hence the sign of Thomas precession — the very sign that matters for the factor of $\tfrac12$ in fine structure.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write $\Lambda_1$ in its adapted basis and $\Lambda_2$ in a semi-adapted basis with velocity at angle $\chi$; multiply; polar-decompose. Extract $S$ from the image of $e_0$ ($\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$) and read the rotation angle from $\cos\varphi_T = R(e_1)\cdot e_1$ and $\sin\varphi_T = R(e_1)\cdot e_2$, simplifying with $c_i^2 - s_i^2 = 1$.

**Subgoal decomposition:**

1. **Write the two boost matrices in a common basis.** $\Lambda_1$ adapted ($(e_0,e_1)$-plane); $\Lambda_2$ semi-adapted, velocity $(V_2\cos\chi, V_2\sin\chi, 0)$.
   - *Hint:* Use the semi-adapted boost form $\Lambda^0{}_0 = \Gamma_2$, $\Lambda^0{}_j = \Gamma_2 V_{2,j}$, etc., for $\Lambda_2$.
   - *Why needed:* It sets up the matrix product in one frame.

2. **Compute the composite Lorentz factor.** $\Gamma = e_0\cdot\Lambda_2\Lambda_1(e_0) = c_1c_2 + s_1s_2\cos\chi = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$.
   - *Hint:* The time–time component of the product is the velocity-addition expression.
   - *Why needed:* It fixes the boost factor $S$ and supplies the combination that simplifies the rotation.

3. **Extract $\cos\varphi_T$.** Compute $R(e_1)\cdot e_1 = [\Lambda_2\Lambda_1(e_1)]\cdot S(e_1)$ and simplify.
   - *Hint:* Use $c_i^2 - s_i^2 = 1$ and $\sin^2\chi = 1-\cos^2\chi$; the combination $\Gamma = c_1c_2 + s_1s_2\cos\chi$ collapses terms.
   - *Why needed:* It gives $\cos\varphi_T = 1 - \frac{(\Gamma_1-1)(\Gamma_2-1)}{1+\Gamma}\sin^2\chi$.

4. **Extract $\sin\varphi_T$ and fix the sign.** Compute $R(e_1)\cdot e_2$; the sign is negative since $\sin\chi \ge 0$, giving $\varphi_T \in [-\pi, 0]$.
   - *Hint:* The $e_2$-component of $R(e_1)$ carries the overall factor $-\sin\chi$.
   - *Why needed:* It gives the magnitude and the clockwise direction.

---

# Lemma Decomposition

> [!note]- Lemma 1: The composite Lorentz factor
> **Statement:** $\Gamma = e_0\cdot\Lambda_2\Lambda_1(e_0) = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi)$.
>
> **Hint:** The time–time component of the product of the two boost matrices.
>
> **Why needed:** It fixes the boost factor of the polar decomposition and the simplifying combination.
>
> > [!note]- Full proof
> > With $\Lambda_1$ a boost of rapidity $\psi_1$ in $(e_0,e_1)$ and $\Lambda_2$ a boost of rapidity $\psi_2$ with velocity at angle $\chi$, write $c_i = \cosh\psi_i = \Gamma_i$, $s_i = \sinh\psi_i = \Gamma_i V_i$. The intermediate vector is $\Lambda_1(e_0) = c_1 e_0 + s_1 e_1$. Applying $\Lambda_2$ (whose velocity has components $V_2(\cos\chi, \sin\chi, 0)$) and taking the scalar product with $e_0$,
> > $$\Gamma = e_0\cdot\Lambda_2(c_1 e_0 + s_1 e_1) = c_1 c_2 + s_1 s_2\cos\chi = \Gamma_1\Gamma_2 + \Gamma_1V_1\Gamma_2V_2\cos\chi = \Gamma_1\Gamma_2(1 + V_1V_2\cos\chi),$$
> > using that $\Lambda_2$ contributes $c_2$ to the $e_0$ direction and $s_2\cos\chi$ from the component of its velocity along $e_1$. $\blacksquare$

> [!note]- Lemma 2: The cosine of the Thomas angle
> **Statement:** $\cos\varphi_T = 1 - \dfrac{(\Gamma_1-1)(\Gamma_2-1)}{1+\Gamma}\sin^2\chi$.
>
> **Hint:** $\cos\varphi_T = [\Lambda_2\Lambda_1(e_1)]\cdot S(e_1)$; simplify with $c_i^2 - s_i^2 = 1$.
>
> **Why needed:** It is the main result for the angle's cosine.
>
> > [!note]- Full proof
> > By the polar decomposition $\Lambda_2\Lambda_1 = S\circ R$ with $R$ a rotation of $(e_1,e_2)$, the angle satisfies $\cos\varphi_T = R(e_1)\cdot e_1 = [S^{-1}\Lambda_2\Lambda_1(e_1)]\cdot e_1 = [\Lambda_2\Lambda_1(e_1)]\cdot S(e_1)$ (since $S$ preserves the scalar product). Computing $\Lambda_2\Lambda_1(e_1)$ and the relevant component of $S(e_1)$ from the explicit boost matrices, and expanding,
> > $$\cos\varphi_T = \frac{1}{1+\Gamma}\big[c_1 + c_2 + s_1 s_2\cos\chi + (c_1-1)(c_2-1)\cos^2\chi\big].$$
> > Using $\Gamma = c_1c_2 + s_1s_2\cos\chi$ (Lemma 1) to substitute $s_1s_2\cos\chi = \Gamma - c_1c_2$, and the identities $c_i = \Gamma_i$, $\cos^2\chi = 1 - \sin^2\chi$, this collapses to
> > $$\cos\varphi_T = 1 - \frac{(\Gamma_1-1)(\Gamma_2-1)}{1+\Gamma}\sin^2\chi. \qquad\blacksquare$$

> [!note]- Lemma 3: The sine and the sign
> **Statement:** $\sin\varphi_T = -\dfrac{\sin\chi}{1+\Gamma}\big[s_1 s_2 + (c_1-1)(c_2-1)\cos\chi\big] \le 0$.
>
> **Hint:** $\sin\varphi_T = R(e_1)\cdot e_2$; the overall factor $-\sin\chi$ fixes the sign.
>
> **Why needed:** It gives the rotation sense (clockwise) and completes the angle.
>
> > [!note]- Full proof
> > Similarly $\sin\varphi_T = R(e_1)\cdot e_2 = [\Lambda_2\Lambda_1(e_1)]\cdot S(e_2)$. Computing from the matrices and simplifying with Lemma 1,
> > $$\sin\varphi_T = -\frac{\sin\chi}{1+\Gamma}\big[s_1 s_2 + (c_1 - 1)(c_2-1)\cos\chi\big].$$
> > Since $\sin\chi \ge 0$ (as $\chi \in [0,\pi]$) and the bracket is non-negative ($s_1, s_2 > 0$ and $(c_i - 1) \ge 0$, with $\cos\chi$ possibly negative but the leading $s_1s_2$ term dominating in the physical range), $\sin\varphi_T \le 0$, so $\varphi_T \in [-\pi, 0]$: the rotation is clockwise in $\mathrm{Span}(e_1,e_2)$. Rewriting in $\Gamma_i, V_i$ gives the form in the statement. $\blacksquare$

> [!note]- Lemma 4: The symmetric and half-angle forms
> **Statement:** $\cos\varphi_T = \dfrac{(1+\Gamma+\Gamma_1+\Gamma_2)^2}{(1+\Gamma)(1+\Gamma_1)(1+\Gamma_2)} - 1$, and $\cos\dfrac{\varphi_T}{2} = \dfrac{1+\Gamma+\Gamma_1+\Gamma_2}{\sqrt{2(1+\Gamma)(1+\Gamma_1)(1+\Gamma_2)}}$.
>
> **Hint:** Eliminate $\sin^2\chi$ using $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$, then use $\cos\varphi_T = 2\cos^2(\varphi_T/2) - 1$.
>
> **Why needed:** It gives the permutation-symmetric form and the Macfarlane half-angle.
>
> > [!note]- Full proof
> > From Lemma 1, $\cos\chi = (\Gamma - \Gamma_1\Gamma_2)/(\Gamma_1\Gamma_2 V_1V_2)$, and using $\Gamma_iV_i = \sqrt{\Gamma_i^2 - 1}$, one finds $\sin^2\chi = 1 - \cos^2\chi$ in terms of $\Gamma, \Gamma_1, \Gamma_2$. Substituting into Lemma 2 and simplifying (a standard but tedious manipulation) gives
> > $$\cos\varphi_T = 1 - \frac{1}{1+\Gamma}\left[(\Gamma_1-1)(\Gamma_2-1) - \frac{(\Gamma - \Gamma_1\Gamma_2)^2}{(\Gamma_1+1)(\Gamma_2+1)}\right] = \frac{(1+\Gamma+\Gamma_1+\Gamma_2)^2}{(1+\Gamma)(1+\Gamma_1)(1+\Gamma_2)} - 1.$$
> > This form is manifestly symmetric under permuting $\Gamma, \Gamma_1, \Gamma_2$. Applying $\cos\varphi_T = 2\cos^2(\varphi_T/2) - 1$ gives $\cos^2(\varphi_T/2) = \frac{(1+\Gamma+\Gamma_1+\Gamma_2)^2}{2(1+\Gamma)(1+\Gamma_1)(1+\Gamma_2)}$, hence the half-angle form; substituting $\Gamma = \cosh\psi$, $1+\cosh\psi = 2\cosh^2(\psi/2)$ yields the Macfarlane form. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Write $\Lambda_1$ as a boost of rapidity $\psi_1$ in the $(e_0, e_1)$-plane and $\Lambda_2$ as a boost of rapidity $\psi_2$ with velocity at angle $\chi$ to $e_1$, in the semi-adapted basis. Set $c_i = \cosh\psi_i = \Gamma_i$, $s_i = \sinh\psi_i = \Gamma_iV_i$.
>
> By Lemma 1, the polar-decomposition boost factor $S =$ (boost carrying $e_0$ to $\Lambda_2\Lambda_1(e_0)$) has Lorentz factor $\Gamma = \Gamma_1\Gamma_2(1+V_1V_2\cos\chi)$, and the rotation factor $R = S^{-1}\Lambda_2\Lambda_1$ acts in the $(e_1, e_2)$-plane.
>
> By Lemma 2, $\cos\varphi_T = R(e_1)\cdot e_1 = 1 - \frac{(\Gamma_1-1)(\Gamma_2-1)}{1+\Gamma}\sin^2\chi$.
>
> By Lemma 3, $\sin\varphi_T = R(e_1)\cdot e_2 = -\frac{\sin\chi}{1+\Gamma}[s_1s_2 + (c_1-1)(c_2-1)\cos\chi] \le 0$, so $\varphi_T \in [-\pi, 0]$ (clockwise).
>
> By Lemma 4, eliminating $\chi$ via $\Gamma$ gives the symmetric form $\cos\varphi_T = \frac{(1+\Gamma+\Gamma_1+\Gamma_2)^2}{(1+\Gamma)(1+\Gamma_1)(1+\Gamma_2)} - 1$ and the Macfarlane half-angle form.
>
> For perpendicular boosts $\chi = \pi/2$: $\Gamma = \Gamma_1\Gamma_2$ (Lemma 1 with $\cos\chi = 0$), and Lemma 2 gives $\cos\varphi_T = 1 - \frac{(\Gamma_1-1)(\Gamma_2-1)}{1+\Gamma_1\Gamma_2} = \frac{\Gamma_1+\Gamma_2}{1+\Gamma_1\Gamma_2}$, after simplification using $1+\Gamma_1\Gamma_2 - (\Gamma_1-1)(\Gamma_2-1) = \Gamma_1 + \Gamma_2$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Hyperbolic triangle area and the defect formula.** The Thomas angle equals the area of the geodesic triangle in hyperbolic velocity space, and the symmetric form in $\Gamma, \Gamma_1, \Gamma_2$ is the hyperbolic law expressing this area through the (hyperbolic) cosines of the side lengths (the rapidities). The application is to recognise the Thomas-angle formula as a hyperbolic-trigonometry identity, the analogue of the spherical-excess formula; it is out-of-distribution because hyperbolic trigonometry is rarely connected to relativistic kinematics.

**Berry phase for a spin in a rotating field.** A spin-$\tfrac12$ particle whose magnetic field traces a closed loop on the sphere acquires a Berry phase equal to half the solid angle enclosed; the Thomas rotation is the velocity-space analogue, with the hyperbolic area replacing the solid angle. The application maps the half-angle formula $\sin(\varphi_T/2) = -\sin\chi\,\sinh(\psi_1/2)\sinh(\psi_2/2)/\cosh(\psi/2)$ to a geometric-phase computation; it battle-tests the "phase = half enclosed area" pattern across the boundary between relativity and quantum mechanics.

**The defect of a sequence of rotations (spherical excess).** Composing three rotations that return the orientation leaves a net rotation governed by the spherical excess of the axis triangle — the exact Euclidean analogue of the Thomas rotation from three boosts. The application is to compare the perpendicular-boost formula with the spherical-excess formula and recognise both as curvature-induced holonomy, one hyperbolic (boosts) and one spherical (rotations). It is a surprising parallel internal to the structure of the rotation and Lorentz groups.

---

# Bridges

- **[[Def - Thomas Rotation]]** — this theorem computes the angle of the Thomas rotation defined there. The definition introduces $\varphi_T$ as the angle of the rotation factor in the polar decomposition of a product of two boosts; this theorem gives its value through the speeds and angle, and in the symmetric, Macfarlane, Stapp, and perpendicular forms.

- **[[Thm - Composition of Coplanar Boosts gives a Boost times Thomas Rotation|The composition theorem]]** — the composition theorem establishes that the product of two non-collinear boosts is a boost times a Thomas rotation; this theorem supplies the rotation's magnitude. Together they give the complete description of composing two boosts: the velocity-addition law for the boost part, and this angle formula for the rotation part. The two are the kinematic and the geometric content of the same composition.

- **Thomas precession and the spin–orbit factor of one-half** — linearising this angle for an infinitesimal second boost gives the infinitesimal Thomas rotation per acceleration step, $\delta\varphi_T \approx -\tfrac12(\gamma - 1)\,\hat{\mathbf{v}}\times d\hat{\mathbf{v}}$ in the appropriate limit, and integrating around an orbit gives the [[Def - Thomas Precession|Thomas precession]] rate $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$. The clockwise sign ($\varphi_T < 0$) is what makes the precession *oppose* the magnetic precession in the spin–orbit interaction, supplying the factor of $\tfrac12$ that Thomas found in 1926. This theorem's sign convention is therefore not a mathematical nicety but the origin of a measured spectral correction.

---

# Unlocked by This

> [!tip] The Thomas Precession Rate *(from Special Relativity XVI)*
> Integrating the infinitesimal Thomas angle around a closed velocity loop converts this finite-angle formula into the **Thomas precession** rate. For a particle in circular motion with acceleration $\mathbf{a}$ and velocity $\mathbf{v}$, the spin precesses at $\boldsymbol{\Omega}_T = \frac{\gamma^2}{\gamma+1}\mathbf{a}\times\mathbf{v}$, derived by taking the small-$V_2$ limit of this theorem (one finite boost plus an infinitesimal increment) and integrating. The clockwise sign of $\varphi_T$ established here determines the direction of the precession, which is exactly what supplies the relativistic factor of $\tfrac12$ in the spin–orbit coupling of atomic fine structure. See [[Special Relativity XVI — Accelerated Observers]], [[Def - Thomas Precession]], and [[Thm - The Thomas Equation]].
