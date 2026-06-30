---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Liénard-Wiechert Potential"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

A charge $q$ moves at constant velocity $\mathbf v$ (no acceleration). Find its field and exhibit the relativistic "flattening".

1. Set the four-acceleration $a = 0$ in the Liénard–Wiechert field and show it reduces to $F(M) = \frac{q}{4\pi\varepsilon_0 R^3}\,\underline U\wedge\underline{PM}$ — purely Coulombic, no radiative part.
2. Show that this field, despite being built from the *retarded* position, points along the line from the charge's *present* (instantaneous) position to the field point — a relativistic conspiracy.
3. Compute the electric field relative to the lab observer and show it is the "flattened Coulomb field": $\mathbf E = \frac{q}{4\pi\varepsilon_0}\frac{1 - v^2}{(1 - v^2\sin^2\theta)^{3/2}}\frac{\hat{\mathbf n}_*}{r_*^2}$, where $r_*$, $\hat{\mathbf n}_*$, $\theta$ refer to the present position. Describe how the field is enhanced transverse to the motion and weakened along it.
4. Verify the magnetic field is $\mathbf B = \frac{1}{c}\hat{\mathbf n}\times\mathbf E$ and vanishes in the charge's rest frame, recovering the static Coulomb field.

**Recall:**

![[Thm - The Liénard-Wiechert Potential#Statement]]

The Liénard–Wiechert field is $F = \frac{q}{4\pi\varepsilon_0 R^2}[\underline a + \frac{1 + a\cdot\vec{PM}}{R}\underline U]\wedge\underline{PM}$; the Coulomb part is the $a$-independent term $\frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$. Relative to an observer, $\mathbf E = F(\cdot, U_0)$, $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$; the present position $P_*$ is where the charge is "now" in the observer's frame, with $\vec{P'P_*} = (t - t_P)\mathbf v = (r/c)\mathbf v$ and $\hat{\mathbf n}_*$ the unit vector from $P_*$ to $M$.

---

# Convergent Strategy

**Problem class.** A *characterise-a-field's-structure* problem in the special inertial-motion case, the fourth target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: take a known field, set acceleration to zero, and analyse the resulting structure (Coulombic, flattened). The routine is to specialise the general Liénard–Wiechert field and project onto the observer.

**Assumption pattern.** The given is a charge in inertial motion, $a = 0$. The signpost is "constant velocity" — the radiative part (which carries $a$) vanishes, leaving only the Coulomb part, and the four-velocity $U$ is constant so the retarded structure simplifies. What this unlocks is that the field is purely $\frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$, a wedge of the (constant) four-velocity with the displacement.

**Theorem routing.** The route is: set $a = 0$ in the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]] $\to$ Coulomb part $\frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$ (Step 1); use Chasles' relation to rewrite $\vec{PM}$ in terms of the present position (Step 2); project onto the observer with $\vec{PM}\cdot U_0 = -r$, $U\cdot U_0 = -\Gamma$ to get the flattened field (Step 3); $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$ (Step 4).

**Key decision point.** The crux is the relativistic conspiracy in Step 2: although the field is computed from the *retarded* position $P'$, it points from the *present* position $P_*$ to $M$. This happens because, for *uniform* motion, the displacement $\vec{PM}$ (retarded) and the present-position vector combine via $\vec{PM} = R[U(\tau_P) + \mathbf m]$ so that the field's direction realigns to the present position. The decision is to express the field in present-position variables, where the flattening is manifest, rather than retarded variables.

---

# Legal Operations Used

1. **Operation 8 from the topic page (recognise the exterior product $F = p\wedge q$).** Step 1 uses the wedge $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$ of the Coulomb field.

2. **Operation 7 from the topic page (project onto an observer).** Step 3 projects the field onto the lab observer to get $\mathbf E$ and $\mathbf B$.

3. **Operation 9 from the topic page (restore $c$ to recover the textbook form).** Step 3 restores $c$ to write the flattening factor $(1 - v^2\sin^2\theta)^{-3/2}$ and Step 4 the relation $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$.

---

# Hints

> [!note]- Hint 1
> In the Liénard–Wiechert field, the radiative part carries the four-acceleration $a$. Setting $a = 0$ kills it, and the term $\frac{1 + a\cdot\vec{PM}}{R}\to\frac{1}{R}$, leaving $F = \frac{q}{4\pi\varepsilon_0 R^2}\cdot\frac{1}{R}\underline U\wedge\underline{PM} = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$.

> [!note]- Hint 2
> For uniform motion, the charge's present position $P_*$ (where it is "now") and its retarded position $P'$ are related by $\vec{P'P_*} = (r/c)\mathbf v$ (it moves at $\mathbf v$ during the light-travel time $r/c$). Use Chasles' relation $\vec{PM} = \vec{P'M}$... and the structure $\vec{PM} = R(U_0 + \hat{\mathbf n})$ to show the field's direction aligns with $\hat{\mathbf n}_*$, the present-position direction.

> [!note]- Hint 3
> Project $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$ onto the observer: $\mathbf E = F(\cdot, U_0)$. Using $\vec{PM}\cdot U_0 = -r$, $U\cdot U_0 = -\Gamma$, and $R = r\Gamma(1 - \hat{\mathbf n}\cdot\mathbf v)$, the algebra yields $\mathbf E = \frac{q}{4\pi\varepsilon_0}\frac{1 - v^2}{(1 - v^2\sin^2\theta_*)^{3/2}}\frac{\hat{\mathbf n}_*}{r_*^2}$, where $\theta_*$ is the angle between $\mathbf v$ and $\hat{\mathbf n}_*$.

> [!note]- Hint 4
> The Liénard–Wiechert magnetic field is always $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$. In the charge's rest frame $\mathbf v = 0$, so $\Gamma = 1$, the flattening factor is $1$, and $\mathbf E = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf r}}{r^2}$ (static Coulomb), $\mathbf B = 0$.

---

# Solution

The uniformly moving charge has a purely Coulombic, flattened field that points at its present position. Step 1 sets $a = 0$ to get the Coulomb part; Step 2 exhibits the present-position conspiracy; Step 3 computes the flattening; Step 4 gives the magnetic field. The non-obvious move is in Step 2: the retarded-position field points at the present position for uniform motion.

**Step 1: With $a = 0$, the field is purely Coulombic.**

> [!note]- Derivation
> The [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]] is $F = \frac{q}{4\pi\varepsilon_0 R^2}[\underline a + \frac{1 + a\cdot\vec{PM}}{R}\underline U]\wedge\underline{PM}$. Set $a = 0$ (inertial motion): the term $\underline a$ vanishes, and $\frac{1 + a\cdot\vec{PM}}{R}\to\frac{1}{R}$. So
> $$F(M) = \frac{q}{4\pi\varepsilon_0 R^2}\cdot\frac{1}{R}\,\underline U\wedge\underline{PM} = \frac{q}{4\pi\varepsilon_0 R^3}\,\underline U\wedge\underline{PM}.$$
> This is the **Coulomb part** alone — the radiative part has vanished because there is no acceleration. The field is a wedge of the (now constant) four-velocity $\underline U$ with the displacement $\underline{PM}$, falling off as $1/R^3$ in $R$ (which becomes $1/r^2$ in the spatial distance).

**Step 2: The field points at the present position.**

> [!note]- Derivation
> The field is built from the *retarded* position $P'$ (where the charge was at $\tau_P$), but for uniform motion it points from the *present* position $P_*$ (where the charge is "now", at the observer's time $t$). Here is why. During the light-travel time $t - t_P = r/c$, the charge moves from $P'$ to $P_*$ at velocity $\mathbf v$: $\vec{P'P_*} = (r/c)\mathbf v$. The displacement $\vec{PM} = \vec{P'M}$ decomposes (Gourgoulhon's $\vec{PM} = R[U(\tau_P) + \mathbf m]$, $\mathbf m\perp U$, $|\mathbf m| = 1$) so that the *spatial* part of the field, after projecting onto the observer, aligns not with $\hat{\mathbf n}$ (the retarded direction $P' \to M$) but with $\hat{\mathbf n}_*$ (the present direction $P_* \to M$). Concretely, $r\hat{\mathbf n} = (r/c)\mathbf v + r_*\hat{\mathbf n}_*$, so $r(\hat{\mathbf n} - \mathbf v/c) = r_*\hat{\mathbf n}_*$ — and the combination $\hat{\mathbf n} - \mathbf v/c$ is exactly what appears in the projected field. The field therefore points along $\hat{\mathbf n}_*$, from where the charge *is*, not from where it *was*. This is a relativistic conspiracy special to uniform motion: an observer sees the field of a steadily-moving charge as if it emanated instantaneously from the charge's current position, even though the information travelled at $c$ from the retarded position.

**Step 3: The flattened Coulomb field.**

> [!note]- Derivation
> Project $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$ onto the observer, $\mathbf E = F(\cdot, U_0)$. Using $\vec{PM}\cdot U_0 = -r$, $U\cdot U_0 = -\Gamma$ (Lorentz factor of the charge), and $R = r\Gamma(1 - \hat{\mathbf n}\cdot\mathbf v)$, together with the present-position rewriting of Step 2, the algebra (Gourgoulhon 18.111–18.116) gives
> $$\mathbf E = \frac{q}{4\pi\varepsilon_0}\,\frac{1 - v^2}{(1 - v^2\sin^2\theta_*)^{3/2}}\,\frac{\hat{\mathbf n}_*}{r_*^2},$$
> where $\theta_*$ is the angle between the velocity $\mathbf v$ and the present-position direction $\hat{\mathbf n}_*$, and $r_*$ is the present distance.
>
> **The flattening.** Compare with the static Coulomb field $\frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf r}}{r^2}$. The extra factor $\frac{1 - v^2}{(1 - v^2\sin^2\theta_*)^{3/2}}$ distorts the field:
> - *Along the motion* ($\theta_* = 0$ or $\pi$): the factor is $\frac{1 - v^2}{1} = 1 - v^2 = 1/\Gamma^2$, so the field is **weakened** by $1/\Gamma^2$.
> - *Transverse to the motion* ($\theta_* = \pi/2$): the factor is $\frac{1 - v^2}{(1 - v^2)^{3/2}} = (1 - v^2)^{-1/2} = \Gamma$, so the field is **enhanced** by $\Gamma$.
>
> So a fast-moving charge's field is squashed into a "pancake" perpendicular to its motion: strong in the transverse plane (enhanced by $\Gamma$), weak fore and aft (suppressed by $\Gamma^2$). This is the field of an ultrarelativistic charge — concentrated in a thin transverse sheet, the electromagnetic analogue of length contraction.

**Step 4: The magnetic field and the rest-frame limit.**

> [!note]- Derivation
> The Liénard–Wiechert magnetic field is always $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$ (from $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$, the general relation for a single charge's field). So a uniformly moving charge carries both an electric field (flattened Coulomb) and a magnetic field circling its line of motion — the magnetic field of a current, which is what a moving charge is.
>
> In the charge's **rest frame**, $\mathbf v = 0$, $\Gamma = 1$, the flattening factor is $\frac{1 - 0}{(1 - 0)^{3/2}} = 1$, and $\theta_*$, $r_*$ reduce to the ordinary spherical $\theta$, $r$. The field becomes
> $$\mathbf E = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf r}}{r^2}, \qquad \mathbf B = 0,$$
> the **static Coulomb field** — recovering electrostatics. A charge at rest has no magnetic field; the magnetic field of the moving charge is purely a frame effect, the boosted electric field, exactly as $\mathbf E$ and $\mathbf B$ are frame-dependent slices of the single tensor $F$.

> [!note]- Complete formal solution
> Setting $a = 0$ in the Liénard–Wiechert field gives the Coulomb part $F = \frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$, with no radiative term. For uniform motion the field points at the present position $P_*$ (since $r(\hat{\mathbf n} - \mathbf v/c) = r_*\hat{\mathbf n}_*$), a relativistic conspiracy. Projecting onto the observer gives $\mathbf E = \frac{q}{4\pi\varepsilon_0}\frac{1 - v^2}{(1 - v^2\sin^2\theta_*)^{3/2}}\frac{\hat{\mathbf n}_*}{r_*^2}$: weakened by $1/\Gamma^2$ along the motion ($\theta_* = 0$), enhanced by $\Gamma$ transverse ($\theta_* = \pi/2$) — a pancake field. The magnetic field is $\mathbf B = \frac1c\hat{\mathbf n}\times\mathbf E$. In the rest frame ($\Gamma = 1$) the flattening disappears and $\mathbf E = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf r}}{r^2}$, $\mathbf B = 0$ — the static Coulomb field. $\blacksquare$

---

# Key Takeaways

**An inertially moving charge does not radiate: its field is purely Coulombic, falling off as $1/r^2$.** The defining feature of the uniform-motion case is that the radiative part of the field — the $1/r$ term carrying the acceleration — vanishes identically, because there is no acceleration. What remains is the Coulomb part $\frac{q}{4\pi\varepsilon_0 R^3}\underline U\wedge\underline{PM}$, which dies as $1/r^2$ and carries no energy to infinity. The reusable principle, central to all of radiation theory, is that *acceleration is the source of radiation*: a charge in steady motion (constant velocity) emits no electromagnetic waves, while a charge that accelerates (changes velocity) radiates the $1/r$ field that an antenna broadcasts and a synchrotron emits. The trigger is "is the charge accelerating?"; if not, the field is Coulombic and non-radiating, and the full apparatus of the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert field]] collapses to the boosted Coulomb law. This is why uniformly moving charges (a steady current) produce static fields, and only changing currents radiate.

**The field of a uniformly moving charge points at its present position — a relativistic conspiracy worth understanding.** A subtle and instructive fact is that although causality forces the field to be computed from the *retarded* position (where the charge was when the light left), for *uniform* motion the field nonetheless points from the charge's *present* position to the field point. The reason is geometric: during the light-travel time the charge moves exactly far enough that the retarded-position field direction $\hat{\mathbf n} - \mathbf v/c$ realigns to the present-position direction $\hat{\mathbf n}_*$. The reusable insight is that this conspiracy is special to *unaccelerated* motion — for an accelerating charge it fails, and the field genuinely "remembers" the retarded state, which is what produces radiation. The diagnostic: a steadily moving charge can be treated as if its field emanated instantaneously from its current position (a great computational simplification), but an accelerating charge cannot, and the difference is the radiative field. This distinction is the heart of why acceleration radiates and uniform motion does not.

**The field flattens into a transverse pancake at high speed, the electromagnetic shadow of length contraction.** The flattening factor $\frac{1 - v^2}{(1 - v^2\sin^2\theta)^{3/2}}$ encodes a vivid relativistic distortion: the field of a fast charge is enhanced by $\Gamma$ in the transverse plane and suppressed by $\Gamma^2$ along the motion, so an ultrarelativistic charge carries a thin sheet of field perpendicular to its velocity. The reusable picture is that the spherical Coulomb field of a rest charge gets "squashed" by the boost, exactly as a sphere length-contracts into a pancake — the field lines, which are isotropic at rest, pile up transversely and thin out longitudinally. This flattening is physically important: it is why the field of a passing relativistic particle is a brief, intense transverse pulse (the basis of the Weizsäcker–Williams equivalent-photon method, treating a fast charge's field as a flash of real photons), and it is the electromagnetic manifestation of the same length contraction that shapes all of relativistic kinematics. Recognising "fast charge ⇒ pancake field" connects the moving-charge field to the geometry of Minkowski space.
