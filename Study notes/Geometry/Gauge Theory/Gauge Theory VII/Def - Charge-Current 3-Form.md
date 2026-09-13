---
type: definition
subject: gauge-theory
prereqs:
  - "Def - U(1) Gauge Field and Electromagnetic Connection"
  - "Def - The Electric Four-Current"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Def - Musical Isomorphism (Flat and Sharp)"
  - "Def - Lorentzian Manifold"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is an oriented [[Def - Lorentzian Manifold|Lorentzian]] $4$-manifold, the mathematical model of spacetime, and we work in a system of **standard local coordinates** $(t, x, y, z)$ adapted to the metric $g = \langle\cdot,\cdot\rangle$, meaning
$$\Big\langle \tfrac{\partial}{\partial t}, \tfrac{\partial}{\partial t} \Big\rangle < 0, \qquad \Big\langle \tfrac{\partial}{\partial x}, \tfrac{\partial}{\partial x} \Big\rangle, \Big\langle \tfrac{\partial}{\partial y}, \tfrac{\partial}{\partial y} \Big\rangle, \Big\langle \tfrac{\partial}{\partial z}, \tfrac{\partial}{\partial z} \Big\rangle > 0,$$
with the four coordinate vector fields mutually orthogonal; on Minkowski space these are inertial coordinates with $\langle\partial_t,\partial_t\rangle = -1$ and $\langle\partial_x,\partial_x\rangle = \langle\partial_y,\partial_y\rangle = \langle\partial_z,\partial_z\rangle = +1$, and the oriented volume form is $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$. We follow the series signature convention $(-,+,+,+)$ with $c = 1$ and unit charge. The symbol $\Omega^k(M;\mathbb{R})$ denotes the space of smooth real-valued [[Def - Differential k-Form on a Manifold|differential k-forms]] on $M$, and $\varrho, j_x, j_y, j_z$ are smooth real functions on $M$ (in general time-dependent). We write $\vec{j} := (j_x, j_y, j_z)$ for the spatial vector field assembled from the last three, and $\varrho$ for the fourth function. The [[Def - Hodge Star in Arbitrary Signature|Hodge star]] $\star$ used on this page is Bär's star $\star_B$, characterised in §7.1 by $\omega\wedge\eta = \langle\star\omega,\eta\rangle\,\mathrm{vol}$; the induced inner product on $1$-forms is diagonal in the coframe, $\langle dt, dt\rangle = -1$ and $\langle dx, dx\rangle = \langle dy, dy\rangle = \langle dz, dz\rangle = +1$. The flat operator $\flat : T_pM \to T_p^*M$, $X^\flat = \langle X, \cdot\rangle$, is the [[Def - Musical Isomorphism (Flat and Sharp)|musical isomorphism]] for $g$. The full symbol registry for the chapter is on [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]].

> [!warning] Convention: signature, star, and the letter $J$
> The chapter on special relativity ([[Def - The Electric Four-Current]]) works in the opposite metric signature $(+,-,-,-)$, still with $c = 1$, and there the four-current is the **vector field** written $J$ with components $J^\mu = (\varrho, \vec{j})$ and metric-dual $1$-form $\underline{J}$. On this page $J$ names the **charge-current $3$-form** of Bär's Lorentzian convention $(-,+,+,+)$; to avoid a clash of letters we write the four-current *vector* as $j$ and its lowered $1$-form as $j^\flat$. The dictionary between the two conventions is $g_B = -g_{\mathrm{SR}}$, the field strength $F$ is the same $2$-form, the fields $\vec{E}, \vec{B}$ are the same, and the two Hodge stars are related on Minkowski space by $\star_B = -\star_V^{\mathrm{SR}}$. Every identity on this page is derived inside Bär's convention; the special-relativity cross-reference is translated through this dictionary and never re-derived.

---

# Axiom Motivation

The electromagnetic field $F$ introduced on [[Def - U(1) Gauge Field and Electromagnetic Connection|the previous page]] is the curvature of a $U(1)$-connection, and its homogeneous law $dF = 0$ came for free from the Bianchi identity. But a field with no sources is inert: to write the *inhomogeneous* Maxwell equations — the ones that say charge produces electric flux and moving charge produces magnetic circulation — we must first give the sources a home on spacetime. Elementary electromagnetism hands us two objects, a scalar **charge density** $\varrho$ (charge per unit volume) and a vector **current density** $\vec{j}$ (charge crossing unit area per unit time). The question this definition answers is: *what single geometric object on the $4$-manifold $M$ packages $(\varrho, \vec{j})$ so that Maxwell's inhomogeneous law and the conservation of charge both become clean, coordinate-free statements?*

The desiderata are sharp, and there are three of them. First, the object must sit on the same side of a differential-form equation as $d\star F$, because the law we are heading toward is $d\star F + J = 0$; since $F \in \Omega^2(M)$ and $\star F \in \Omega^2(M)$ on a $4$-manifold, $d\star F$ is a $3$-form, so the source must be a **$3$-form**. Second, the total charge in a region of space at a fixed instant must be recoverable by integration, and the natural thing to integrate over a $3$-dimensional region is a $3$-form; so the charge density had better be the "spatial-volume" part of the object. Third — and this is what fixes every sign — the exterior derivative of the source must reproduce the physical continuity equation $\partial_t\varrho + \operatorname{div}\vec{j} = 0$, so that charge conservation is nothing more than $dJ = 0$, which will follow from $d(d\star F) = 0$.

These three requirements already dictate the shape of the object completely. Its four independent components as a $3$-form on a $4$-manifold must be filled by the four functions $\varrho, j_x, j_y, j_z$. The purely spatial basis $3$-form $dx\wedge dy\wedge dz$ is the one that survives restriction to a constant-time slice — the slice on which $dt$ pulls back to zero — so its coefficient must be the charge density $\varrho$, the quantity whose spatial integral is the enclosed charge. The three mixed basis $3$-forms, each containing a single $dt$, are the ones that measure flux of charge through a spatial surface across a time interval, so their coefficients must be the components of the current $\vec{j}$. That is the entire structural content of the definition; the remaining freedom is a choice of signs on the three current terms, and those signs are pinned by the third desideratum.

We now perform the per-clause failure analysis, treating the coefficient assignments and their signs as the "clauses". **The charge-density clause** ($+\varrho$ on $dx\wedge dy\wedge dz$): if we dropped this term, the source would have no component surviving on a constant-time slice, and the enclosed charge $\int_{\{t = t_0\}} J$ would be identically zero — the theory would have currents but no charges, and Coulomb's law $\operatorname{div}\vec{E} = \varrho$ would read $\operatorname{div}\vec{E} = 0$ always, forbidding a point charge. If instead we kept the term but flipped its sign, the charge of every configuration would come out negated, an internally consistent but perverse relabelling; we keep the sign that makes a positive $\varrho$ a positive charge, matching $\int_{\{t=t_0\}} J = \int \varrho\, dx\, dy\, dz$. **The current clauses** (the coefficient $-j_x$ on $dt\wedge dy\wedge dz$ and its two cyclic companions): here the signs are not conventional but forced. The continuity equation is obtained by computing $dJ$ and reading off the coefficient of $\mathrm{vol}$; with the signs as written, one gets $dJ = (\partial_t\varrho + \operatorname{div}\vec{j})\,\mathrm{vol}$, so that $dJ = 0$ is exactly $\partial_t\varrho + \operatorname{div}\vec{j} = 0$. Were the current terms given the *opposite* sign, the same computation would yield $dJ = (\partial_t\varrho - \operatorname{div}\vec{j})\,\mathrm{vol}$, and $dJ = 0$ would assert the physically wrong law $\partial_t\varrho = \operatorname{div}\vec{j}$, under which charge would accumulate exactly where it flows outward. The relative minus sign between the charge term and the current terms is therefore the whole point: it is the sign that turns the topological identity $d^2 = 0$ into the physical conservation of charge. Dropping any one current component, say the $j_z$ term, removes the $z$-flux from the divergence and breaks conservation for any configuration in which charge moves along $z$.

A reader could reconstruct this definition from the desiderata alone: demand a $3$-form source whose spatial part is the charge density and whose derivative is the continuity equation, and the coefficients and their signs are the only assignment that works. The definition is not a convention imposed from outside; it is the unique packaging of $(\varrho, \vec{j})$ compatible with $d\star F + J = 0$ and $dJ = 0$.

---

# The Definition

Let $M$ be an oriented [[Def - Lorentzian Manifold|Lorentzian]] $4$-manifold with standard local coordinates $(t, x, y, z)$ as fixed in the Notation, and let $\varrho, j_x, j_y, j_z \in C^\infty(M)$. The **charge-current $3$-form** (Bär, Definition 3.2.2) is
$$
J \;:=\; \varrho\; dx\wedge dy\wedge dz \;-\; j_x\; dt\wedge dy\wedge dz \;-\; j_y\; dt\wedge dz\wedge dx \;-\; j_z\; dt\wedge dx\wedge dy \;\in\; \Omega^3(M;\mathbb{R}).
$$
The function $\varrho$ is the **charge density** and the spatial vector field $\vec{j} = (j_x, j_y, j_z)$ is the **current density**; both are, in general, time-dependent, and — like the fields $\vec{E}, \vec{B}$ of the electromagnetic $2$-form — their split into a scalar and a spatial vector depends on the choice of coordinate system, whereas the $3$-form $J$ itself does not.

The four basis $3$-forms of $\Lambda^3 T^*M$ in these coordinates are $dx\wedge dy\wedge dz$ (the purely spatial one) and the three containing exactly one $dt$, written here in the cyclic orderings $dt\wedge dy\wedge dz$, $dt\wedge dz\wedge dx$, $dt\wedge dx\wedge dy$; the definition assigns $+\varrho$ to the first and $-j_x, -j_y, -j_z$ to the latter three. In the smallest concrete case, a single static point charge of magnitude $q$ smeared into a small spatial region has $\vec{j} = 0$ and $J = \varrho\, dx\wedge dy\wedge dz$ with $\int \varrho\, dx\,dy\,dz = q$; the $3$-form is then literally "$q$ times a unit of spatial volume", and its integral over any spatial region counts the charge inside.

**The smearing convention for point sources.** A mathematical point charge would need $\varrho$ to be a Dirac distribution, which is not a smooth function; throughout this chapter we model a point source by a smooth **bump function**, that is, a nonnegative $\chi \in C_c^\infty(\mathbb{R}^3)$ supported in a ball of radius $\varepsilon$ about a point and normalised by $\int_{\mathbb{R}^3}\chi\, dx\,dy\,dz = 1$, so that $\varrho = q\,\chi$ carries total charge exactly $q$. This keeps $J$ inside $\Omega^3(M;\mathbb{R})$ while approximating the idealised point charge as $\varepsilon\to 0$.

## Equivalent formulation: the Hodge dual of the four-current

The charge-current $3$-form is, up to a single explicit sign, the [[Def - Hodge Star in Arbitrary Signature|Hodge dual]] of the four-current $1$-form. Let $j$ be the **four-current vector field**, the spacetime vector assembled from the same four functions,
$$
j \;=\; \varrho\,\partial_t + j_x\,\partial_x + j_y\,\partial_y + j_z\,\partial_z,
$$
which is the object written $J^\mu = (\varrho, \vec{j})$ in the special-relativity chapter (see the convention callout). Then
$$
\boxed{\,J \;=\; -\,\star_B\, j^\flat\,.}
$$
This is a claim about specific forms, so we prove it clause by clause, computing $j^\flat$ from the metric and $\star_B$ from its defining relation; both steps are carried out in full in the Examples / Corollaries section below, where the sign is shown to be $-1$ and not $+1$.

---

# Relate to Other Fields / Compression

**True name.** The official definition writes $J$ in coordinates, but its coordinate-free identity is the boxed formula: $J$ is the negative Hodge dual of the four-current $1$-form, $J = -\star_B j^\flat$. Equivalently, and this is the operational characterisation that makes $J$ memorable, $J$ is **the flux $3$-form of charge-current**: for any oriented $3$-dimensional region $\Sigma \subset M$, the number $\int_\Sigma J$ is the net charge-current flux through $\Sigma$. When $\Sigma$ is a piece of a constant-time slice, $\int_\Sigma J$ is the electric charge contained in it (only the $\varrho$-term survives, because $dt$ restricts to zero on the slice); when $\Sigma$ is a "spatial tube swept out in time", $\int_\Sigma J$ measures the charge that has crossed it. This is the same relationship that ties a flux density to its flux integral throughout physics, and it is why the source of electromagnetism is naturally a $3$-form rather than a scalar-plus-vector: a codimension-one form is exactly what one integrates over the hypersurfaces on which charge is counted.

**Connection to de Rham cohomology.** Once the theory is in place, the continuity equation makes $J$ a **closed** $3$-form, $dJ = 0$ (this is proved on [[Thm - Continuity Equation and Conservation of Charge]]). On a closed spatial slice its integral is therefore a period of a de Rham class, and the total charge becomes a topological pairing rather than a coordinate computation; the invariance of total charge under deformation of the slice is Stokes' theorem applied to a closed form. This is the differential-forms shadow of the fact that conserved charges are cohomological.

**Connection to fluid dynamics and probability.** The same $3$-form appears wherever a conserved scalar flows on spacetime. For a fluid with mass density $\varrho$ and mass flux $\varrho\vec{v}$, the identical construction produces a mass-current $3$-form whose closedness is the continuity equation of fluid mechanics; for a probability current in a diffusion or a quantum theory, it is the probability-current $3$-form whose closedness is the conservation of total probability. In every case the pattern is: a conserved density and its flux are the two kinds of coefficient of a single $3$-form, and conservation is the vanishing of its exterior derivative.

---

# Examples / Corollaries

**The $1$-form star table on Minkowski space (used below).** We first record the action of $\star = \star_B$ on the coordinate $1$-forms, since the boxed identity depends on it. The star is defined by $\omega\wedge\eta = \langle\star\omega,\eta\rangle\,\mathrm{vol}$ for $\omega\in\Lambda^1$, $\eta\in\Lambda^3$, with $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$ and the induced inner product on $\Lambda^3$ diagonal in the basis monomials, $\langle\alpha,\alpha\rangle = \epsilon_{i}\epsilon_{j}\epsilon_{k}$ for $\alpha = dx^i\wedge dx^j\wedge dx^k$ where $\epsilon_t = -1$, $\epsilon_x = \epsilon_y = \epsilon_z = +1$ (see [[Def - Hodge Star in Arbitrary Signature]] and [[Thm - Properties of the Hodge Star in Arbitrary Signature]]). We compute $\star dx$ in full as a template. For each basis $3$-form $\eta$, the wedge $dx\wedge\eta$ is nonzero only when $\eta$ omits $dx$, that is only for $\eta = dt\wedge dy\wedge dz$; testing that one,
$$dx\wedge(dt\wedge dy\wedge dz) = -\,dt\wedge dx\wedge dy\wedge dz = -\,\mathrm{vol} \qquad \text{(one transposition moves } dx \text{ past } dt\text{).}$$
Writing $\star dx = c\, dt\wedge dy\wedge dz$, the defining relation gives $-\mathrm{vol} = \langle c\, dt\wedge dy\wedge dz,\; dt\wedge dy\wedge dz\rangle\,\mathrm{vol} = c\,\epsilon_t\epsilon_y\epsilon_z\,\mathrm{vol} = -c\,\mathrm{vol}$ (since $\epsilon_t\epsilon_y\epsilon_z = -1$), so $c = 1$ and $\star dx = dt\wedge dy\wedge dz$. The identical procedure on the other three coordinate $1$-forms gives
$$
\star dt = dx\wedge dy\wedge dz, \qquad \star dx = dt\wedge dy\wedge dz, \qquad \star dy = dt\wedge dz\wedge dx, \qquad \star dz = dt\wedge dx\wedge dy,
$$
each with coefficient $+1$ in the orderings shown. (For $\star dt$: only $\eta = dx\wedge dy\wedge dz$ gives $dt\wedge\eta = \mathrm{vol}$, and $\langle dx\wedge dy\wedge dz, dx\wedge dy\wedge dz\rangle = \epsilon_x\epsilon_y\epsilon_z = +1$, so the coefficient is $+1$. For $\star dy$: only $\eta = dt\wedge dz\wedge dx$ gives $dy\wedge\eta \neq 0$, with $dy\wedge dt\wedge dz\wedge dx = -\mathrm{vol}$ after counting three inversions in $(y,t,z,x)$, and $\langle dt\wedge dz\wedge dx, dt\wedge dz\wedge dx\rangle = \epsilon_t\epsilon_z\epsilon_x = -1$, giving coefficient $+1$. For $\star dz$: only $\eta = dt\wedge dx\wedge dy$ contributes, with $dz\wedge dt\wedge dx\wedge dy = -\mathrm{vol}$ after three inversions and $\langle dt\wedge dx\wedge dy, dt\wedge dx\wedge dy\rangle = \epsilon_t\epsilon_x\epsilon_y = -1$, again coefficient $+1$.)

**Corollary — the sign in $J = -\star_B j^\flat$, verified.** We now check the boxed identity clause by clause. First lower the index on the four-current vector. Since $\partial_t^\flat = \langle\partial_t,\cdot\rangle = -dt$ and $\partial_x^\flat = dx$, $\partial_y^\flat = dy$, $\partial_z^\flat = dz$ (the [[Def - Musical Isomorphism (Flat and Sharp)|flat]] of $g$, using $\langle\partial_t,\partial_t\rangle = -1$ and $\langle\partial_i,\partial_i\rangle = +1$ for the spatial directions),
$$
j^\flat = \varrho\,\partial_t^\flat + j_x\,\partial_x^\flat + j_y\,\partial_y^\flat + j_z\,\partial_z^\flat = -\varrho\, dt + j_x\, dx + j_y\, dy + j_z\, dz \qquad \text{(lowering each index by } g\text{).}
$$
Now apply $\star_B$ term by term, using the table just established:
$$
\star_B j^\flat = -\varrho\,\star dt + j_x\,\star dx + j_y\,\star dy + j_z\,\star dz
$$
$$
= -\varrho\, dx\wedge dy\wedge dz + j_x\, dt\wedge dy\wedge dz + j_y\, dt\wedge dz\wedge dx + j_z\, dt\wedge dx\wedge dy \qquad \text{(by the star table, line by line).}
$$
Comparing with the definition
$$
J = \varrho\, dx\wedge dy\wedge dz - j_x\, dt\wedge dy\wedge dz - j_y\, dt\wedge dz\wedge dx - j_z\, dt\wedge dx\wedge dy,
$$
every one of the four coefficients of $\star_B j^\flat$ is the negative of the corresponding coefficient of $J$; therefore $\star_B j^\flat = -J$, that is $J = -\star_B j^\flat$. The sign is $-1$, and it arises precisely because the timelike direction contributes $\langle\partial_t,\partial_t\rangle = -1$ to the flat while the spatial directions contribute $+1$; the mismatch between the single minus sign in $j^\flat$ and the pattern of the star table is what produces the uniform overall sign.

**Is an instance — a static point charge.** Take $\varrho = q\,\chi(x, y, z)$ for a normalised spatial bump function $\chi \in C_c^\infty(\mathbb{R}^3)$ with $\int\chi\, dx\,dy\,dz = 1$, and $\vec{j} = 0$; nothing depends on $t$. Then
$$
J = q\,\chi\, dx\wedge dy\wedge dz \in \Omega^3(M;\mathbb{R}),
$$
which is a genuine smooth $3$-form (its single coefficient $q\chi$ is smooth and compactly supported in space). We verify it is a legitimate charge-current $3$-form and check its physics. Its charge-density coefficient is $\varrho = q\chi \geq 0$ and its current coefficients vanish, so $\vec{j} = 0$, a charge at rest. The enclosed charge at any instant $t_0$ is
$$
\int_{\{t = t_0\}} J = \int_{\mathbb{R}^3} q\chi\, dx\, dy\, dz = q \qquad \text{(the } dt\text{-free coefficient integrated over the slice; } \int\chi = 1\text{),}
$$
independent of $t_0$, as a static charge should be. Finally we verify consistency with conservation: since $\chi$ depends only on the spatial variables, $d\chi = \partial_x\chi\, dx + \partial_y\chi\, dy + \partial_z\chi\, dz$ has no $dt$-component, so
$$
dJ = q\, d\chi \wedge dx\wedge dy\wedge dz = 0 \qquad \text{(every spatial } dx^i \text{ already appears in } dx\wedge dy\wedge dz\text{; no } \partial_t\chi \text{ term because } \chi \text{ is static),}
$$
which is $\partial_t\varrho + \operatorname{div}\vec{j} = 0 + 0 = 0$, the continuity equation for a charge that neither moves nor changes. This is the electrostatics configuration, and $J$ passes every clause.

**Is an instance — a steady line current.** Model an infinite straight wire along the $z$-axis carrying steady current $I$: put $\varrho = 0$, $j_x = j_y = 0$, and $j_z = I\,\psi(x, y)$ where $\psi \in C_c^\infty(\mathbb{R}^2)$ is a normalised transverse bump, $\int_{\mathbb{R}^2}\psi\, dx\, dy = 1$, independent of $z$ and $t$. Then only the $j_z$ term survives,
$$
J = -\,I\,\psi(x, y)\; dt\wedge dx\wedge dy \in \Omega^3(M;\mathbb{R}),
$$
a smooth $3$-form. Its charge density is $\varrho = 0$ (no $dx\wedge dy\wedge dz$-part), its current is $\vec{j} = (0, 0, I\psi)$, purely along the wire, and the total current through a cross-sectional plane $\{z = z_0\}$ is $\int_{\mathbb{R}^2} j_z\, dx\, dy = I$. We check conservation: because $\psi = \psi(x, y)$ is independent of $z$ and $t$,
$$
dJ = -\,I\, d\psi \wedge dt\wedge dx\wedge dy = -\,I\,(\partial_z\psi)\, dz\wedge dt\wedge dx\wedge dy = 0 \qquad \text{(only a } dz \text{-derivative could survive, and } \partial_z\psi = 0\text{),}
$$
which reads $\partial_t\varrho + \operatorname{div}\vec{j} = 0 + \partial_z(I\psi) = 0$, the continuity equation for a steady current with no charge accumulating anywhere. A steady line current is thus a valid charge-current $3$-form with $\varrho = 0$.

**Is NOT an instance of a charge-carrying source — a $3$-form with no spatial-volume part.** Consider the pure $3$-form
$$
\beta = dt\wedge dy\wedge dz \in \Omega^3(M;\mathbb{R}),
$$
which is a perfectly good $3$-form and even has the shape of one of the current terms (it is $J$ for the choice $\varrho = 0$, $j_x = -1$, $j_y = j_z = 0$, a uniform $x$-current). The point of the non-example is the general principle it isolates: a $3$-form whose $dx\wedge dy\wedge dz$-coefficient is identically zero **carries no charge density**, and hence measures zero charge on every spatial slice. We verify this. The charge density is by definition the coefficient of $dx\wedge dy\wedge dz$, which for $\beta$ is $0$, so $\varrho \equiv 0$. Equivalently, restricting $\beta$ to a constant-time slice $\Sigma_{t_0} = \{t = t_0\}$ via the inclusion $\iota : \Sigma_{t_0}\hookrightarrow M$, we have $\iota^*(dt) = 0$ (the coordinate $t$ is constant on the slice), so
$$
\iota^*\beta = \iota^*(dt)\wedge\iota^*(dy\wedge dz) = 0, \qquad \text{hence} \qquad \int_{\Sigma_{t_0}}\beta = 0 \quad\text{for every } t_0.
$$
Thus $\beta$ describes a current but contributes nothing to any enclosed charge; only the $dx\wedge dy\wedge dz$-part of a charge-current $3$-form ever survives on a constant-time slice, so the charge density truly lives in that one component. A $3$-form built entirely from $dt$-containing monomials is a pure-current source with $\varrho = 0$, and no amount of such terms can produce a nonzero charge. This is the sense in which "a $3$-form with a $dx\wedge dy\wedge dz$-free part cannot carry charge density": the missing component is precisely the charge.

**Calibration check.** Three verifications a reader can carry out from what is on this page. First, recompute $\star dt$ from the defining relation and confirm the coefficient is $+1$ (unlike $\star dx$, whose test wedge produced $-\mathrm{vol}$, the test wedge $dt\wedge dx\wedge dy\wedge dz = +\mathrm{vol}$ and the metric factor is $\epsilon_x\epsilon_y\epsilon_z = +1$, so no sign appears). Second, take the moving point charge $\varrho = q\chi(x - vt, y, z)$, $\vec{j} = (qv\chi(x - vt, y, z), 0, 0)$ describing a bump drifting along $x$ at speed $v$, and verify $dJ = 0$ by checking $\partial_t\varrho + \partial_x j_x = -qv\,\chi' + qv\,\chi' = 0$. Third, confirm from the boxed identity that a purely spatial four-current $j = \varrho\,\partial_t$ (a charge at rest, $\vec{j} = 0$) has $j^\flat = -\varrho\, dt$ and $-\star_B j^\flat = -(-\varrho)\,\star dt = \varrho\, dx\wedge dy\wedge dz$, matching $J$ for the rest charge — the single minus signs from the timelike flat and from the boxed formula cancel to give the positive charge density.

---

# Unlocked by This

> [!tip] The inhomogeneous Maxwell equation *(from §7.2)*
> With the source in hand, the two remaining Maxwell equations collapse into the single form statement $d\star F + J = 0$ (see [[Def - Maxwell Equations in Form Language]]): the charge-current $3$-form is exactly the object that sits beside $d\star F$, and in coordinates this one equation unpacks into Coulomb's law $\operatorname{div}\vec{E} = \varrho$ and Ampère's law $\operatorname{rot}\vec{B} - \partial_t\vec{E} = \vec{j}$.

> [!tip] Conservation of charge *(from §7.2)*
> Because $J = -\star_B j^\flat$ satisfies $d\star F + J = 0$, applying $d$ and using $d^2 = 0$ gives $dJ = 0$, which in coordinates is the continuity equation $\partial_t\varrho + \operatorname{div}\vec{j} = 0$ and, integrated over a spacetime slab by Stokes, the conservation of total charge (see [[Thm - Continuity Equation and Conservation of Charge]]). The topological identity $d^2 = 0$ becomes a law of physics.

> [!tip] The matter coupling term *(from §7.2)*
> The charge-current $3$-form is one of the two ingredients of the electromagnetic action: the coupling term $A\wedge J$ in the Lagrangian (see [[Def - Electromagnetic Lagrangian and Action]]) is what makes the field respond to its sources, and its variation is precisely what produces $J$ in the Euler–Lagrange equation.
