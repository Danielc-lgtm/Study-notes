---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Maxwell Equations in Coordinates"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Def - Charge-Current 3-Form"
tags: [geometry, gauge-theory, electrodynamics, hodge-star]
---

# Problem Statement

We work on **Minkowski space** $M = \mathbb{R}^4$ with standard coordinates $(t, x, y, z)$, the Lorentzian metric of signature $(-, +, +, +)$ (so $\langle \partial_t, \partial_t \rangle = -1$ and $\langle \partial_x, \partial_x \rangle = \langle \partial_y, \partial_y \rangle = \langle \partial_z, \partial_z \rangle = +1$), and the volume form $\mathrm{vol} = dt \wedge dx \wedge dy \wedge dz$. Units are chosen so that the speed of light is $c = 1$. The electromagnetic field is the curvature $F \in \Omega^2(M; \mathbb{R})$ of a connection on a principal $U(1)$-bundle, written in these coordinates as
$$F = E_x\,dx \wedge dt + E_y\,dy \wedge dt + E_z\,dz \wedge dt + B_x\,dy \wedge dz + B_y\,dz \wedge dx + B_z\,dx \wedge dy,$$
with the smooth time-dependent coefficient functions collected into the **electric field** $\vec{E} = (E_x, E_y, E_z)$ and the **magnetic field** $\vec{B} = (B_x, B_y, B_z)$. The **charge-current** source is the $3$-form
$$J = \varrho\,dx \wedge dy \wedge dz - j_x\,dt \wedge dy \wedge dz - j_y\,dt \wedge dz \wedge dx - j_z\,dt \wedge dx \wedge dy,$$
with **charge density** $\varrho$ and **current density** $\vec{j} = (j_x, j_y, j_z)$.

On $2$-forms the Hodge star $\star \colon \Lambda^2 T^*M \to \Lambda^2 T^*M$ in these coordinates is given by the table
$$\star(dt \wedge dx) = dy \wedge dz, \qquad \star(dy \wedge dz) = -\,dt \wedge dx,$$
$$\star(dt \wedge dy) = dz \wedge dx, \qquad \star(dz \wedge dx) = -\,dt \wedge dy,$$
$$\star(dt \wedge dz) = dx \wedge dy, \qquad \star(dx \wedge dy) = -\,dt \wedge dz.$$

**The task has two parts.**

**Part (a).** Starting from this star table, compute $\star F$ and then $d\star F$ in coordinates. Combine $d\star F$ with the source term $J$ and with the already-known expansion of $dF$ to read off all four of **Maxwell's equations** as the two $2$-form equations
$$dF = 0 \qquad \text{and} \qquad d\star F + J = 0,$$
identifying which scalar law each surviving coefficient encodes: Gauss's law for magnetism $\operatorname{div}\vec{B} = 0$, Faraday's law $\partial_t \vec{B} + \operatorname{rot}\vec{E} = 0$, Coulomb's law $\operatorname{div}\vec{E} = \varrho$, and Ampère's law $\operatorname{rot}\vec{B} - \partial_t \vec{E} = \vec{j}$.

**Part (b).** In vacuum ($\varrho = 0$ and $\vec{j} = 0$) verify that the plane wave
$$\vec{E} = E_0 \cos(kz - kt)\,\hat{x}, \qquad \vec{B} = E_0 \cos(kz - kt)\,\hat{y}$$
(with constants $E_0, k \in \mathbb{R}$ and $\hat{x}, \hat{y}$ the coordinate unit vectors) satisfies all four vacuum Maxwell equations, and read off the geometry of the solution.

> [!warning] Convention: the Hodge star and its signs
> The series uses **Bär's Hodge star**: on an oriented $n$-dimensional inner-product space of index $p$ (number of negative directions), $\star$ is the unique linear map with $\omega \wedge \eta = \langle \star\omega, \eta \rangle\,\mathrm{vol}$ for all $\omega \in \Lambda^k$, $\eta \in \Lambda^{n-k}$. Minkowski space has $p = 1$. The table above is exactly the values this defining relation forces on $2$-forms in dimension four; it is derived and verified line by line on **[[Def - Hodge Star in Arbitrary Signature]]**, and we take it here as given. The competing convention $\alpha \wedge \star\beta = \langle \alpha, \beta \rangle\,\mathrm{vol}$ differs by the sign $(-1)^{k(n-k)}$, which is trivial for $k = 2$, $n = 4$, so the two agree on the $2$-forms of this problem.
>
> The sign convention on Maxwell's inhomogeneous equation is $d\star F + J = 0$ (equivalently $d\star F = -J$), fixed by the Euler–Lagrange equation of the electromagnetic action; see **[[Def - Maxwell Equations in Form Language]]**.

**Recall.**

The two results this exercise leans on are the coordinate expansion of the two $2$-form equations and the definition of the Hodge star that produces the table above.

![[Thm - Maxwell Equations in Coordinates#Statement]]

In words: **[[Thm - Maxwell Equations in Coordinates]]** carries out, with a complete coefficient-by-coefficient proof, the computation of $dF$, of $\star F$, and of $d\star F$ on Minkowski space, and shows that $dF = 0$ is equivalent to the homogeneous pair (Gauss for $\vec B$, Faraday) while $d\star F + J = 0$ is equivalent to the inhomogeneous pair (Coulomb, Ampère). Our Part (a) reproduces the star computations directly from the table so that the mechanism is visible, and cites the theorem's expansion of $dF$ for the homogeneous half; Part (b) is a fresh application not contained in that theorem.

![[Def - Hodge Star in Arbitrary Signature#The Definition]]

In words: the **[[Def - Hodge Star in Arbitrary Signature|Hodge star]]** on $\Lambda^2 T^*M$ is the linear map fixed by $\omega \wedge \eta = \langle \star\omega, \eta \rangle\,\mathrm{vol}$; evaluating this relation on the coordinate basis $2$-forms of Minkowski space produces exactly the six-line table stated above.

We also use the standard vector-calculus operators on $\mathbb{R}^3$: for a vector field $\vec{V} = (V_x, V_y, V_z)$,
$$\operatorname{div}\vec{V} = \partial_x V_x + \partial_y V_y + \partial_z V_z, \qquad \operatorname{rot}\vec{V} = \nabla \times \vec{V} = (\partial_y V_z - \partial_z V_y,\ \partial_z V_x - \partial_x V_z,\ \partial_x V_y - \partial_y V_x),$$
and $\vec{U} \times \vec{V}$ for the cross product; these are the operators the surviving coefficients will assemble into.

> [!warning] Source typo (Bär, p. 86)
> Bär's printed formula for $\star F$ ends with "$-B_z\,dz \wedge dt$". The star table gives $\star(dx \wedge dy) = -\,dt \wedge dz = +\,dz \wedge dt$, so the coefficient of $B_z$ is $+B_z\,dz \wedge dt$. We use the corrected sign $+B_z\,dz \wedge dt$ throughout, and Part (a) derives it from the table so the correction is self-checking.

---

# Convergent Strategy

**Problem class.** This is a *translation* problem: a single geometric equation, $d\star F + J = 0$, is unpacked into the familiar scalar laws of classical electrodynamics by writing everything in coordinates. The whole content is a bookkeeping computation with differential forms — no existence, no estimate, no clever construction — but it is the computation that makes the claim "Maxwell's four equations are two form equations" literally true rather than merely suggestive. Part (b) is the companion *verification* problem: plug a candidate field into the scalar laws and check each holds.

**Assumption pattern.** Everything rests on three structural facts, each used exactly once. First, the metric signature $(-, +, +, +)$ and the induced star table — this is where the physics of a Lorentzian (rather than Euclidean) spacetime enters, and it is the sole reason the star of a "time–space" $2$-form is a "space–space" $2$-form with the signs displayed. Second, the exterior derivative $d$ acts on a $2$-form by differentiating each coefficient and wedging on the four coordinate differentials, so that on $2$-forms in four coordinates $d$ *is* the pair (divergence, curl$+\partial_t$) in disguise. Third, the source term $J$ is written so that its coefficients are precisely $\varrho$ and $-\vec{j}$ in the same four $3$-form slots that $d\star F$ populates, so that $d\star F + J = 0$ can be read slot by slot.

**Theorem routing.** The explicit route is: (i) apply the star table monomial by monomial to $F$ to get $\star F$; (ii) apply $d$ to $\star F$ coefficient by coefficient, using **[[Thm - Coordinate Expression for the Exterior Derivative|the coordinate formula for $d$]]**, and reorder every $3$-form to the standard basis to collect coefficients; (iii) add $J$ and set the coefficient of each of the four independent basis $3$-forms to zero, reading Coulomb off the $dx \wedge dy \wedge dz$ slot and the three components of Ampère off the three $dt$-slots; (iv) quote **[[Thm - Maxwell Equations in Coordinates]]** for the parallel expansion of $dF$, whose four slots give Gauss's law for $\vec{B}$ and the three components of Faraday. For Part (b), substitute the plane-wave coefficients into the four scalar laws and differentiate, using only the chain rule for $\cos(kz - kt)$.

**Key decision point.** The one genuinely non-mechanical observation, and the one worth remembering, is that $\star F$ has *exactly the same monomial shape as $F$* but with the coefficient sextuple $(\vec{E}, \vec{B})$ replaced by $(\vec{B}, -\vec{E})$: the $dx^i \wedge dt$ block of $\star F$ carries $\vec{B}$ where $F$ carried $\vec{E}$, and the spatial block of $\star F$ carries $-\vec{E}$ where $F$ carried $\vec{B}$. This is the coordinate face of the electromagnetic duality $F \mapsto \star F$, and it is what lets us obtain $d\star F$ from the known formula for $dF$ by the substitution $\vec{E} \mapsto \vec{B}$, $\vec{B} \mapsto -\vec{E}$ — turning Gauss-for-$\vec B$ into (minus) Coulomb and Faraday into Ampère. Recognising this halves the work and explains why the homogeneous and inhomogeneous pairs look so alike.

---

# Legal Operations Used

The topic page for this chapter, **[[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]]**, records the legal operations of the electromagnetic formalism; this solution uses the following (the numbering will be reconciled with that page's Legal Operations list).

1. **Evaluate the Hodge star on a form monomial by monomial.** Because $\star$ is $\mathbb{R}$-linear, $\star F$ is computed by applying the six-line table to each basis $2$-form appearing in $F$ and summing, with each coefficient function carried along unchanged. This is the operation that turns the abstract $\star$ into an explicit form.

2. **Take the exterior derivative in coordinates by differentiating coefficients and wedging.** For a $2$-form $\sum_I g_I\,\omega_I$ with $\omega_I$ a wedge of two coordinate differentials, $d\big(\sum_I g_I\,\omega_I\big) = \sum_I dg_I \wedge \omega_I = \sum_I \sum_\mu (\partial_\mu g_I)\,dx^\mu \wedge \omega_I$; the terms in which $dx^\mu$ repeats a differential already in $\omega_I$ vanish. This is **[[Thm - Coordinate Expression for the Exterior Derivative|the coordinate expression for $d$]]**.

3. **Reorder a wedge of differentials to the standard basis, tracking the permutation sign.** Every $3$-form produced by operation 2 is brought to one of the four ordered basis monomials $dx \wedge dy \wedge dz$, $dt \wedge dy \wedge dz$, $dt \wedge dz \wedge dx$, $dt \wedge dx \wedge dy$, picking up the sign of the permutation, so that like coefficients can be collected.

4. **Read a form equation slot by slot.** Since the four basis $3$-forms are linearly independent, a $3$-form vanishes if and only if each of its four coefficients vanishes; setting $d\star F + J = 0$ therefore splits into four independent scalar equations. The same principle applied to $dF = 0$ splits it into four more.

5. **Recognise divergence and curl inside the collected coefficients.** The coefficient of $dx \wedge dy \wedge dz$ is a divergence $\partial_x(\cdot) + \partial_y(\cdot) + \partial_z(\cdot)$; the three $dt$-slot coefficients are the three components of a curl combined with a time derivative. This is the vector-calculus dictionary of **[[Def - Frankel Dictionary (Forms vs Vector Calculus)]]**.

6. **Substitute a candidate field into the scalar laws and differentiate (Part (b)).** With the plane-wave coefficients, each scalar law becomes an elementary derivative of $\cos(kz - kt)$ computed by the chain rule, and one checks the two sides cancel.

---

# Hints

> [!note]- Hint 1
> Start with $\star F$. The star is linear, so apply the table to each of the six terms of $F$ separately. Watch the orientation: $F$'s electric terms are written as $dx^i \wedge dt$, whereas the table is phrased for $dt \wedge dx^i$; use $dx^i \wedge dt = -\,dt \wedge dx^i$ before reading off the table value, and remember $\star$ is applied to the reordered monomial, not term-by-term to the letters.

> [!note]- Hint 2
> Once you have $\star F$, look at its shape next to $F$. You should find that $\star F$ is *another* field of the same form as $F$, with $\vec{E}$ and $\vec{B}$ swapped and one of them negated. Identify exactly which substitution $(\vec{E}, \vec{B}) \mapsto (\,?\,,\,?\,)$ carries $F$ to $\star F$. This lets you reuse the formula for $dF$ instead of recomputing $d\star F$ from scratch — though you should verify at least one coefficient directly.

> [!note]- Hint 3
> To differentiate, use $d\big(g\,dx^a \wedge dx^b\big) = \sum_\mu (\partial_\mu g)\,dx^\mu \wedge dx^a \wedge dx^b$; a term dies whenever $dx^\mu$ equals $dx^a$ or $dx^b$. Collect the results into the four ordered basis $3$-forms, being careful with the sign when you reorder, for example $dz \wedge dy \wedge dt = -\,dt \wedge dy \wedge dz$.

> [!note]- Hint 4
> After collecting, the coefficient of $dx \wedge dy \wedge dz$ in $d\star F$ is $-\operatorname{div}\vec{E}$ and the three $dt$-slot coefficients are the components of $\operatorname{rot}\vec{B} - \partial_t \vec{E}$. Now add $J = \varrho\,dx \wedge dy \wedge dz - j_x\,dt \wedge dy \wedge dz - \cdots$ and set each of the four coefficients to zero. Match slots.

> [!note]- Hint 5 (Part (b))
> Write $\phi := kz - kt$. Then $E_x = E_0 \cos\phi$ with all other components zero except $B_y = E_0 \cos\phi$. Because $\phi$ depends only on $z$ and $t$, every $\partial_x$ and $\partial_y$ derivative of a coefficient vanishes; the only surviving derivatives are $\partial_z \cos\phi = -k \sin\phi$ and $\partial_t \cos\phi = +k \sin\phi$. Feed these into the four scalar laws and watch each cancel.

---

# Solution

The plan is direct. In Part (a) we compute $\star F$ from the table (Step 1), differentiate it to obtain $d\star F$ in the standard $3$-form basis (Step 2), and add $J$ and split slot by slot to extract Coulomb's and Ampère's laws, quoting the parallel expansion of $dF$ for Gauss's and Faraday's laws (Step 3). In Part (b) we substitute the plane-wave field into the four scalar laws (Step 4) and read off the physical geometry (Step 5). Throughout, $\phi := kz - kt$ in Part (b), and all coefficient functions are smooth functions of $(t, x, y, z)$.

**Step 1: Compute $\star F$ from the star table.**

Applying the six-line table to the six terms of $F$ and using linearity gives
$$\star F = -E_x\,dy \wedge dz - E_y\,dz \wedge dx - E_z\,dx \wedge dy + B_x\,dx \wedge dt + B_y\,dy \wedge dt + B_z\,dz \wedge dt.$$

> [!note]- Derivation
> The Hodge star is $\mathbb{R}$-linear (operation 1), so $\star F = \sum_i E_i\,\star(dx^i \wedge dt) + \big(B_x\,\star(dy \wedge dz) + B_y\,\star(dz \wedge dx) + B_z\,\star(dx \wedge dy)\big)$, with each coefficient function passing through the star unchanged. We treat the electric and magnetic terms in turn.
>
> **Electric terms.** These are written with the ordering $dx^i \wedge dt$, so we first flip to the ordering used in the table, $dx^i \wedge dt = -\,dt \wedge dx^i$ (one transposition), then apply the table:
> $$\star(dx \wedge dt) = -\,\star(dt \wedge dx) = -\,dy \wedge dz \qquad \text{(reorder, then } \star(dt \wedge dx) = dy \wedge dz\text{)},$$
> $$\star(dy \wedge dt) = -\,\star(dt \wedge dy) = -\,dz \wedge dx \qquad \text{(reorder, then } \star(dt \wedge dy) = dz \wedge dx\text{)},$$
> $$\star(dz \wedge dt) = -\,\star(dt \wedge dz) = -\,dx \wedge dy \qquad \text{(reorder, then } \star(dt \wedge dz) = dx \wedge dy\text{)}.$$
> Hence the electric part of $\star F$ is $-E_x\,dy \wedge dz - E_y\,dz \wedge dx - E_z\,dx \wedge dy$.
>
> **Magnetic terms.** These are already in the orderings appearing on the table's left column, so we read the values off directly and then flip to the ordering $dx^i \wedge dt$ for uniformity:
> $$\star(dy \wedge dz) = -\,dt \wedge dx = +\,dx \wedge dt \qquad \text{(table, then } {-}\,dt \wedge dx = dx \wedge dt\text{)},$$
> $$\star(dz \wedge dx) = -\,dt \wedge dy = +\,dy \wedge dt \qquad \text{(table, then reorder)},$$
> $$\star(dx \wedge dy) = -\,dt \wedge dz = +\,dz \wedge dt \qquad \text{(table, then reorder)}.$$
> Hence the magnetic part of $\star F$ is $B_x\,dx \wedge dt + B_y\,dy \wedge dt + B_z\,dz \wedge dt$. The coefficient of $B_z$ is $+dz \wedge dt$, which is the corrected sign flagged above (Bär's page prints $-B_z\,dz \wedge dt$).
>
> Summing the two parts gives the displayed $\star F$.
>
> **The duality observation.** Compare $\star F$ with $F$. Reading $\star F$ in the two blocks — the $dx^i \wedge dt$ block and the spatial $\{dy \wedge dz,\ dz \wedge dx,\ dx \wedge dy\}$ block — we see
> $$\star F = B_x\,dx \wedge dt + B_y\,dy \wedge dt + B_z\,dz \wedge dt + (-E_x)\,dy \wedge dz + (-E_y)\,dz \wedge dx + (-E_z)\,dx \wedge dy.$$
> This is *exactly the form of $F$* with the coefficient sextuple $(\vec{E}, \vec{B})$ replaced by $(\vec{B}, -\vec{E})$: the electric slots now carry $\vec{B}$ and the magnetic slots now carry $-\vec{E}$. We record this substitution $\sigma \colon (\vec{E}, \vec{B}) \mapsto (\vec{B}, -\vec{E})$ for reuse in Step 2.

**Step 2: Differentiate to obtain $d\star F$.**

Differentiating $\star F$ term by term and collecting into the standard $3$-form basis gives
$$d\star F = (-\operatorname{div}\vec{E})\,dx \wedge dy \wedge dz + (\operatorname{rot}\vec{B} - \partial_t \vec{E})_x\,dt \wedge dy \wedge dz + (\operatorname{rot}\vec{B} - \partial_t \vec{E})_y\,dt \wedge dz \wedge dx + (\operatorname{rot}\vec{B} - \partial_t \vec{E})_z\,dt \wedge dx \wedge dy.$$

> [!note]- Derivation
> By the coordinate formula for $d$ (operation 2), we differentiate each coefficient of $\star F$ against all four coordinates and wedge, discarding any term whose new differential repeats one already present, then reorder each surviving $3$-form to the standard basis (operation 3). We collect the four independent slots one at a time.
>
> **The $dx \wedge dy \wedge dz$ slot.** Only the three spatial terms of $\star F$ can produce $dx \wedge dy \wedge dz$, since every term containing $dt$ would need three further distinct space differentials and only two are available. Differentiating them:
> $$d(-E_x\,dy \wedge dz) = -\partial_x E_x\,dx \wedge dy \wedge dz \qquad \text{(only } dx \text{ survives against } dy \wedge dz\text{)},$$
> $$d(-E_y\,dz \wedge dx) = -\partial_y E_y\,dy \wedge dz \wedge dx = -\partial_y E_y\,dx \wedge dy \wedge dz \qquad \text{(} dy \wedge dz \wedge dx = dx \wedge dy \wedge dz\text{, an even cycle)},$$
> $$d(-E_z\,dx \wedge dy) = -\partial_z E_z\,dz \wedge dx \wedge dy = -\partial_z E_z\,dx \wedge dy \wedge dz \qquad \text{(} dz \wedge dx \wedge dy = dx \wedge dy \wedge dz\text{, an even cycle)}.$$
> Adding, the $dx \wedge dy \wedge dz$ coefficient is $-(\partial_x E_x + \partial_y E_y + \partial_z E_z) = -\operatorname{div}\vec{E}$ (operation 5).
>
> **The $dt \wedge dy \wedge dz$ slot.** The contributions come from the spatial term with letters $\{dy, dz\}$ and from the two $dx^i \wedge dt$ terms whose spatial letter is $x$ absent, i.e. those carrying $dy$ or $dz$:
> $$d(-E_x\,dy \wedge dz) \supset -\partial_t E_x\,dt \wedge dy \wedge dz \qquad \text{(the } dt \text{ term of } dE_x\text{)},$$
> $$d(B_y\,dy \wedge dt) \supset \partial_z B_y\,dz \wedge dy \wedge dt = -\partial_z B_y\,dt \wedge dy \wedge dz \qquad \text{(} dz \wedge dy \wedge dt = -\,dt \wedge dy \wedge dz\text{)},$$
> $$d(B_z\,dz \wedge dt) \supset \partial_y B_z\,dy \wedge dz \wedge dt = +\partial_y B_z\,dt \wedge dy \wedge dz \qquad \text{(} dy \wedge dz \wedge dt = +\,dt \wedge dy \wedge dz\text{)}.$$
> Adding, the coefficient is $\partial_y B_z - \partial_z B_y - \partial_t E_x = (\operatorname{rot}\vec{B})_x - \partial_t E_x = (\operatorname{rot}\vec{B} - \partial_t \vec{E})_x$, since $(\operatorname{rot}\vec{B})_x = \partial_y B_z - \partial_z B_y$.
>
> **The $dt \wedge dz \wedge dx$ slot.** By the same procedure with the letters cycled $x \to y \to z \to x$:
> $$d(-E_y\,dz \wedge dx) \supset -\partial_t E_y\,dt \wedge dz \wedge dx,$$
> $$d(B_z\,dz \wedge dt) \supset \partial_x B_z\,dx \wedge dz \wedge dt = -\partial_x B_z\,dt \wedge dz \wedge dx \qquad \text{(} dx \wedge dz \wedge dt = -\,dt \wedge dz \wedge dx\text{)},$$
> $$d(B_x\,dx \wedge dt) \supset \partial_z B_x\,dz \wedge dx \wedge dt = +\partial_z B_x\,dt \wedge dz \wedge dx \qquad \text{(} dz \wedge dx \wedge dt = +\,dt \wedge dz \wedge dx\text{)}.$$
> Adding, the coefficient is $\partial_z B_x - \partial_x B_z - \partial_t E_y = (\operatorname{rot}\vec{B} - \partial_t \vec{E})_y$, since $(\operatorname{rot}\vec{B})_y = \partial_z B_x - \partial_x B_z$.
>
> **The $dt \wedge dx \wedge dy$ slot.** Cycling once more:
> $$d(-E_z\,dx \wedge dy) \supset -\partial_t E_z\,dt \wedge dx \wedge dy,$$
> $$d(B_x\,dx \wedge dt) \supset \partial_y B_x\,dy \wedge dx \wedge dt = -\partial_y B_x\,dt \wedge dx \wedge dy \qquad \text{(} dy \wedge dx \wedge dt = -\,dt \wedge dx \wedge dy\text{)},$$
> $$d(B_y\,dy \wedge dt) \supset \partial_x B_y\,dx \wedge dy \wedge dt = +\partial_x B_y\,dt \wedge dx \wedge dy \qquad \text{(} dx \wedge dy \wedge dt = +\,dt \wedge dx \wedge dy\text{)}.$$
> Adding, the coefficient is $\partial_x B_y - \partial_y B_x - \partial_t E_z = (\operatorname{rot}\vec{B} - \partial_t \vec{E})_z$, since $(\operatorname{rot}\vec{B})_z = \partial_x B_y - \partial_y B_x$.
>
> Assembling the four slots gives the displayed $d\star F$.
>
> **Consistency with the duality observation.** The formula for $dF$ (recalled in Step 3) reads, slot by slot, $\operatorname{div}\vec{B}$, then $(\operatorname{rot}\vec{E} + \partial_t \vec{B})$. Applying the substitution $\sigma \colon (\vec{E}, \vec{B}) \mapsto (\vec{B}, -\vec{E})$ from Step 1 to that formula sends $\operatorname{div}\vec{B} \mapsto \operatorname{div}(-\vec{E}) = -\operatorname{div}\vec{E}$ and $\operatorname{rot}\vec{E} + \partial_t \vec{B} \mapsto \operatorname{rot}\vec{B} + \partial_t(-\vec{E}) = \operatorname{rot}\vec{B} - \partial_t \vec{E}$, reproducing exactly the four coefficients just computed. The direct computation above and the substitution shortcut therefore agree, as they must, since $d$ acts only on the coefficient functions and the fixed monomials while $\sigma$ only relabels the coefficient functions.

**Step 3: Add $J$ and read off all four Maxwell equations.**

Set $d\star F + J = 0$ and split slot by slot; recall the expansion of $dF$ for the homogeneous pair.

> [!note]- Derivation
> **Inhomogeneous pair from $d\star F + J = 0$.** Write $J$ in the standard basis, $J = \varrho\,dx \wedge dy \wedge dz - j_x\,dt \wedge dy \wedge dz - j_y\,dt \wedge dz \wedge dx - j_z\,dt \wedge dx \wedge dy$, and add it to the $d\star F$ of Step 2:
> $$d\star F + J = (\varrho - \operatorname{div}\vec{E})\,dx \wedge dy \wedge dz + \big((\operatorname{rot}\vec{B} - \partial_t \vec{E})_x - j_x\big)\,dt \wedge dy \wedge dz$$
> $$+ \big((\operatorname{rot}\vec{B} - \partial_t \vec{E})_y - j_y\big)\,dt \wedge dz \wedge dx + \big((\operatorname{rot}\vec{B} - \partial_t \vec{E})_z - j_z\big)\,dt \wedge dx \wedge dy.$$
> The four basis $3$-forms $dx \wedge dy \wedge dz$, $dt \wedge dy \wedge dz$, $dt \wedge dz \wedge dx$, $dt \wedge dx \wedge dy$ are linearly independent, so by operation 4 the form vanishes if and only if each coefficient vanishes:
> $$\operatorname{div}\vec{E} = \varrho \qquad \text{(Coulomb's law, from the } dx \wedge dy \wedge dz \text{ slot)},$$
> $$\operatorname{rot}\vec{B} - \partial_t \vec{E} = \vec{j} \qquad \text{(Ampère's law, from the three } dt \text{-slots, one component each)}.$$
>
> **Homogeneous pair from $dF = 0$.** By **[[Thm - Maxwell Equations in Coordinates]]**, restated: on Minkowski space,
> $$dF = (\operatorname{div}\vec{B})\,dx \wedge dy \wedge dz + (\partial_t \vec{B} + \operatorname{rot}\vec{E})_x\,dt \wedge dy \wedge dz + (\partial_t \vec{B} + \operatorname{rot}\vec{E})_y\,dt \wedge dz \wedge dx + (\partial_t \vec{B} + \operatorname{rot}\vec{E})_z\,dt \wedge dx \wedge dy.$$
> Splitting $dF = 0$ slot by slot in the same way gives
> $$\operatorname{div}\vec{B} = 0 \qquad \text{(Gauss's law for magnetism, from the } dx \wedge dy \wedge dz \text{ slot)},$$
> $$\partial_t \vec{B} + \operatorname{rot}\vec{E} = 0 \qquad \text{(Faraday's law, from the three } dt \text{-slots)}.$$
> The two form equations $dF = 0$ and $d\star F + J = 0$ therefore encode precisely the four classical Maxwell equations, one law per $3$-form slot.

**Step 4: Verify the vacuum plane wave (Part (b)).**

Write $\phi := kz - kt$. The plane wave has $E_x = E_0 \cos\phi$, $E_y = E_z = 0$, and $B_y = E_0 \cos\phi$, $B_x = B_z = 0$. We check the four vacuum equations ($\varrho = 0$, $\vec{j} = 0$) in turn.

> [!note]- Derivation
> Because $\phi = kz - kt$ depends on $z$ and $t$ only, the chain rule gives, for any coefficient of the form $E_0 \cos\phi$,
> $$\partial_x(E_0 \cos\phi) = 0, \qquad \partial_y(E_0 \cos\phi) = 0, \qquad \partial_z(E_0 \cos\phi) = -k E_0 \sin\phi, \qquad \partial_t(E_0 \cos\phi) = +k E_0 \sin\phi,$$
> the last two because $\partial_z \phi = k$ and $\partial_t \phi = -k$. These are the only nonzero derivatives that will occur.
>
> **Gauss's law for magnetism $\operatorname{div}\vec{B} = 0$.** With $\vec{B} = (0, E_0 \cos\phi, 0)$,
> $$\operatorname{div}\vec{B} = \partial_x B_x + \partial_y B_y + \partial_z B_z = 0 + \partial_y(E_0 \cos\phi) + 0 = 0 \qquad \text{(} \partial_y \text{ annihilates a function of } z, t\text{)}.$$
>
> **Faraday's law $\partial_t \vec{B} + \operatorname{rot}\vec{E} = 0$.** First the two pieces:
> $$\partial_t \vec{B} = \big(0,\ \partial_t(E_0 \cos\phi),\ 0\big) = (0,\ k E_0 \sin\phi,\ 0) \qquad \text{(} \partial_t \cos\phi = +k \sin\phi\text{)},$$
> and with $\vec{E} = (E_0 \cos\phi, 0, 0)$,
> $$\operatorname{rot}\vec{E} = \big(\partial_y E_z - \partial_z E_y,\ \partial_z E_x - \partial_x E_z,\ \partial_x E_y - \partial_y E_x\big) = \big(0,\ \partial_z(E_0 \cos\phi),\ 0\big) = (0,\ -k E_0 \sin\phi,\ 0),$$
> where the $x$- and $z$-components vanish because their entries are $\partial_y$ or $\partial_x$ of functions of $(z, t)$ (or of the identically zero components $E_y, E_z$), and the $y$-component is $\partial_z E_x = -k E_0 \sin\phi$. Adding,
> $$\partial_t \vec{B} + \operatorname{rot}\vec{E} = (0,\ k E_0 \sin\phi - k E_0 \sin\phi,\ 0) = 0 \qquad \text{(the } y \text{-components cancel).}$$
>
> **Coulomb's law $\operatorname{div}\vec{E} = 0$.** With $\vec{E} = (E_0 \cos\phi, 0, 0)$,
> $$\operatorname{div}\vec{E} = \partial_x E_x + \partial_y E_y + \partial_z E_z = \partial_x(E_0 \cos\phi) + 0 + 0 = 0 \qquad \text{(} \partial_x \text{ annihilates a function of } z, t\text{)},$$
> which matches the vacuum right-hand side $\varrho = 0$.
>
> **Ampère's law $\operatorname{rot}\vec{B} - \partial_t \vec{E} = 0$.** First the two pieces:
> $$\operatorname{rot}\vec{B} = \big(\partial_y B_z - \partial_z B_y,\ \partial_z B_x - \partial_x B_z,\ \partial_x B_y - \partial_y B_x\big) = \big(-\partial_z(E_0 \cos\phi),\ 0,\ 0\big) = (k E_0 \sin\phi,\ 0,\ 0),$$
> where only the $x$-component survives, equal to $-\partial_z B_y = -(-k E_0 \sin\phi) = k E_0 \sin\phi$; and
> $$\partial_t \vec{E} = \big(\partial_t(E_0 \cos\phi),\ 0,\ 0\big) = (k E_0 \sin\phi,\ 0,\ 0) \qquad \text{(} \partial_t \cos\phi = +k \sin\phi\text{)}.$$
> Subtracting,
> $$\operatorname{rot}\vec{B} - \partial_t \vec{E} = (k E_0 \sin\phi - k E_0 \sin\phi,\ 0,\ 0) = 0 \qquad \text{(the } x \text{-components cancel),}$$
> which matches the vacuum right-hand side $\vec{j} = 0$. All four vacuum equations hold.

**Step 5: Read off the geometry of the plane wave.**

The solution is a transverse electromagnetic wave travelling in the $+z$ direction at unit speed, with $\vec{E}$, $\vec{B}$, and the propagation direction forming a positively oriented orthogonal triple of equal-magnitude fields.

> [!note]- Derivation
> The common phase $\phi = kz - kt = k(z - t)$ is constant on the hyperplanes $z - t = \text{const}$, which advance in the $+z$ direction at $dz/dt = 1$; since $c = 1$, the wave moves at the speed of light. At every point $\vec{E} = E_0 \cos\phi\,\hat{x}$ points along $\hat{x}$ and $\vec{B} = E_0 \cos\phi\,\hat{y}$ points along $\hat{y}$, both perpendicular to the propagation direction $\hat{z}$ (transversality) and to each other, with equal magnitudes $|\vec{E}| = |\vec{B}| = |E_0 \cos\phi|$. Their cross product $\vec{E} \times \vec{B} = E_0^2 \cos^2\phi\,(\hat{x} \times \hat{y}) = E_0^2 \cos^2\phi\,\hat{z}$ points in the propagation direction $\hat{z}$; this is the Poynting vector, and its alignment with $\hat{z}$ says energy flows in the direction the wave travels. This is the archetypal free electromagnetic wave.

> [!note]- Complete formal solution
> **Claim.** On Minkowski space $(\mathbb{R}^4, (-,+,+,+))$ with $\mathrm{vol} = dt \wedge dx \wedge dy \wedge dz$, the form equations $dF = 0$ and $d\star F + J = 0$ are equivalent to the four Maxwell equations $\operatorname{div}\vec{B} = 0$, $\partial_t \vec{B} + \operatorname{rot}\vec{E} = 0$, $\operatorname{div}\vec{E} = \varrho$, $\operatorname{rot}\vec{B} - \partial_t \vec{E} = \vec{j}$; and the plane wave $\vec{E} = E_0 \cos(kz - kt)\,\hat{x}$, $\vec{B} = E_0 \cos(kz - kt)\,\hat{y}$ solves the vacuum case $\varrho = 0$, $\vec{j} = 0$.
>
> *Proof.* **Part (a).** By linearity of the Hodge star and the star table, applying $\star$ to each term of $F = \sum_i E_i\,dx^i \wedge dt + B_x\,dy \wedge dz + B_y\,dz \wedge dx + B_z\,dx \wedge dy$ gives, using $\star(dx^i \wedge dt) = -\star(dt \wedge dx^i)$,
> $$\star F = -E_x\,dy \wedge dz - E_y\,dz \wedge dx - E_z\,dx \wedge dy + B_x\,dx \wedge dt + B_y\,dy \wedge dt + B_z\,dz \wedge dt.$$
> Differentiating by the coordinate formula for $d$, discarding repeated differentials, and reordering each $3$-form to the standard basis (with the permutation sign) collects the four independent coefficients into
> $$d\star F = (-\operatorname{div}\vec{E})\,dx \wedge dy \wedge dz + (\operatorname{rot}\vec{B} - \partial_t \vec{E})_x\,dt \wedge dy \wedge dz + (\operatorname{rot}\vec{B} - \partial_t \vec{E})_y\,dt \wedge dz \wedge dx + (\operatorname{rot}\vec{B} - \partial_t \vec{E})_z\,dt \wedge dx \wedge dy.$$
> Adding $J = \varrho\,dx \wedge dy \wedge dz - j_x\,dt \wedge dy \wedge dz - j_y\,dt \wedge dz \wedge dx - j_z\,dt \wedge dx \wedge dy$ and using linear independence of the four basis $3$-forms, $d\star F + J = 0$ holds if and only if $\operatorname{div}\vec{E} = \varrho$ (Coulomb) and $\operatorname{rot}\vec{B} - \partial_t \vec{E} = \vec{j}$ (Ampère). By **[[Thm - Maxwell Equations in Coordinates]]**, $dF = (\operatorname{div}\vec{B})\,dx \wedge dy \wedge dz + (\partial_t \vec{B} + \operatorname{rot}\vec{E})_x\,dt \wedge dy \wedge dz + (\partial_t \vec{B} + \operatorname{rot}\vec{E})_y\,dt \wedge dz \wedge dx + (\partial_t \vec{B} + \operatorname{rot}\vec{E})_z\,dt \wedge dx \wedge dy$, so $dF = 0$ holds if and only if $\operatorname{div}\vec{B} = 0$ (Gauss) and $\partial_t \vec{B} + \operatorname{rot}\vec{E} = 0$ (Faraday). This establishes the equivalence of the two form equations with the four scalar laws.
>
> **Part (b).** Set $\phi = kz - kt$, so $\partial_x \phi = \partial_y \phi = 0$, $\partial_z \phi = k$, $\partial_t \phi = -k$, whence $\partial_z(E_0 \cos\phi) = -k E_0 \sin\phi$ and $\partial_t(E_0 \cos\phi) = +k E_0 \sin\phi$, all $\partial_x$ and $\partial_y$ derivatives being zero. With $\vec{E} = (E_0 \cos\phi, 0, 0)$ and $\vec{B} = (0, E_0 \cos\phi, 0)$: $\operatorname{div}\vec{B} = \partial_y(E_0 \cos\phi) = 0$; $\operatorname{div}\vec{E} = \partial_x(E_0 \cos\phi) = 0 = \varrho$; $\operatorname{rot}\vec{E} = (0, \partial_z(E_0 \cos\phi), 0) = (0, -k E_0 \sin\phi, 0)$ and $\partial_t \vec{B} = (0, k E_0 \sin\phi, 0)$, so $\partial_t \vec{B} + \operatorname{rot}\vec{E} = 0$; $\operatorname{rot}\vec{B} = (-\partial_z(E_0 \cos\phi), 0, 0) = (k E_0 \sin\phi, 0, 0)$ and $\partial_t \vec{E} = (k E_0 \sin\phi, 0, 0)$, so $\operatorname{rot}\vec{B} - \partial_t \vec{E} = 0 = \vec{j}$. All four vacuum equations hold. The phase is constant on $z - t = \text{const}$, so the wave propagates in $+z$ at unit speed; $\vec{E} \parallel \hat{x}$, $\vec{B} \parallel \hat{y}$, $\vec{E} \times \vec{B} \parallel \hat{z}$ with $|\vec{E}| = |\vec{B}|$. $\blacksquare$

> [!warning] Illegal but tempting: computing $\star F$ with Euclidean signs
> It is tempting to reuse the Euclidean $\mathbb{R}^3$ or $\mathbb{R}^4$ Hodge star, where $\star\star = +1$ on $2$-forms and there are no minus signs in the table. On Lorentzian Minkowski space $\star\star = (-1)^{k(n-k)+p} = (-1)^{2 \cdot 2 + 1} = -1$ on $2$-forms, so the correct table carries a minus sign on exactly the three space–space monomials. Using Euclidean signs flips the sign of every $\vec{E}$-term in $\star F$, which turns Coulomb's law into $-\operatorname{div}\vec{E} = \varrho$ and Ampère's law into $-(\operatorname{rot}\vec{B} - \partial_t \vec{E}) = \vec{j}$ — the wrong physics. The signature is not cosmetic here: it is what distinguishes electrodynamics from a formally similar Euclidean field theory. The extra condition that would make the naive computation legal is simply to be on a Riemannian $4$-manifold ($p = 0$), which is not spacetime.

---

# Key Takeaways

**On $2$-forms in four coordinates, the exterior derivative *is* the pair (divergence, curl-with-time-derivative), and reading a form equation slot by slot recovers the classical vector-calculus laws.** The whole of Part (a) is an instance of a single reusable principle: once a $p$-form is written in a coordinate basis, $d$ acts by differentiating each coefficient and wedging on the coordinate differentials, and the linear independence of the basis $(p+1)$-forms lets one equate coefficients on the two sides of a form equation. The trigger for deploying it is any statement of the form "these coordinate-free equations are equivalent to those component equations": expand, collect into the standard basis tracking permutation signs, and match slots. The transferable diagnostic is that the $dx \wedge dy \wedge dz$ slot always produces a divergence and the three mixed time–space slots always produce the components of a curl combined with a time derivative — so before computing, one already knows the *shape* of the four scalar laws that must emerge, and any answer that does not have this shape signals an algebra error. This is the concrete meaning of **[[Def - Frankel Dictionary (Forms vs Vector Calculus)|the Frankel dictionary]]** between forms and vector calculus, and it recurs verbatim whenever a field theory is rewritten in form language.

**Electromagnetic duality is the substitution $(\vec{E}, \vec{B}) \mapsto (\vec{B}, -\vec{E})$, and it is visible directly in the coordinate shape of $\star F$.** The observation isolated in Step 1 — that $\star F$ has the same monomial pattern as $F$ with electric and magnetic coefficients interchanged and one negated — is not a coincidence of this problem but the coordinate face of the involution $\star$ on $2$-forms of a Lorentzian $4$-manifold, where $\star\star = -1$. Its immediate payoff is computational: the inhomogeneous pair (Coulomb, Ampère) is obtained from the homogeneous pair (Gauss, Faraday) by applying the substitution to the already-known formula for $dF$, so one never has to differentiate twice. The deeper payoff is conceptual: in vacuum, where $J = 0$, the equations become symmetric under $(\vec{E}, \vec{B}) \mapsto (\vec{B}, -\vec{E})$, which is exactly the duality that rotates one vacuum solution into another and that generalises, in the non-abelian setting, to the self-dual and anti-self-dual decomposition driving instanton theory. The trigger to look for this is any Hodge star on middle-degree forms in even dimension; the pattern is that $\star$ then squares to $\pm 1$ and splits the space into duality eigenspaces.

**The metric signature is load-bearing, and the single sign $\star\star = (-1)^{k(n-k)+p}$ is where the physics lives.** The illegal-route warning is worth internalising as a standing caution: the same field $F$ and the same operator name "$\star$" give genuinely different equations on a Riemannian and on a Lorentzian $4$-manifold, and the difference is exactly the index $p = 1$ that puts minus signs on the space–space entries of the star table. The reusable lesson for spaced practice is to state the signature and the value of $\star\star$ before writing any star table, and to sanity-check the resulting laws against known physics (Coulomb's law must read $\operatorname{div}\vec{E} = \varrho$ with a plus sign). When a computation in a semi-Riemannian setting produces the "wrong" sign in a familiar law, the first suspect is always an inadvertently Euclidean star. The companion exercises **[[Ex - Double Star Sign in Arbitrary Signature]]** and **[[Ex - The Hodge Star is an Isometry up to the Sign of the Index]]** drill precisely the sign $\star\star = (-1)^{k(n-k)+p}$ and the failure of the isometry property in Lorentzian signature that this warning depends on.

**A plane-wave verification reduces every field equation to elementary derivatives of a single phase, and the geometry falls out of the surviving components.** Part (b) illustrates a diagnostic that transfers to any wave ansatz: when all field components share a phase $\phi$ depending on a subset of the coordinates, only derivatives with respect to those coordinates survive, so most terms in $\operatorname{div}$ and $\operatorname{rot}$ vanish before any computation, and the equations collapse to one-line cancellations of $\sin\phi$ against $\sin\phi$. The trigger is the phrase "verify this ansatz solves the equations"; the pattern is to name the phase, list its nonzero partial derivatives once, and substitute. The physical reading — transverse fields, mutually orthogonal, equal in magnitude, with $\vec{E} \times \vec{B}$ along the propagation direction at unit speed — is not extra work but a direct reading of which components survived, and it is the same structure that reappears for gravitational waves and for the linearised excitations of any hyperbolic field theory. The takeaway is that a plane-wave check is cheap and diagnostic: it confirms both that the equations are satisfied and that they are genuinely wave equations with light-speed propagation.
