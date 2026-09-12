---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Maxwell Equations in Form Language"
  - "Def - Charge-Current 3-Form"
  - "Thm - d-Squared-is-Zero"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Manifold with Boundary and Induced Orientation"
tags: [geometry, gauge-theory, electrodynamics]
---

# Notation

Throughout, $M$ is an oriented four-dimensional [[Def - Lorentzian Manifold|Lorentzian manifold]] modelling spacetime; for every explicit computation we take $M$ to be **Minkowski space** $\mathbb{R}^{1,3}$, that is $\mathbb{R}^4$ with standard coordinates $(t, x, y, z)$, the metric of signature $(-,+,+,+)$ in which $\partial_t$ is timelike and $\partial_x, \partial_y, \partial_z$ are spacelike, and the volume form
$$\mathrm{vol} = dt \wedge dx \wedge dy \wedge dz.$$
The electromagnetic field is the [[Def - U(1) Gauge Field and Electromagnetic Connection|field strength]] $F \in \Omega^2(M; \mathbb{R})$, a real-valued $2$-form; on a $U(1)$-bundle it is the curvature of the electromagnetic connection, descended to the base, and it satisfies the homogeneous Maxwell equation $dF = 0$ identically by the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]]. The symbol $\star$ denotes the [[Def - Hodge Star in Arbitrary Signature|Hodge star]] in the sense fixed below, so $\star F \in \Omega^2(M; \mathbb{R})$. The source of the field is the [[Def - Charge-Current 3-Form|charge–current 3-form]]
$$J = \varrho\, dx \wedge dy \wedge dz - j_x\, dt \wedge dy \wedge dz - j_y\, dt \wedge dz \wedge dx - j_z\, dt \wedge dx \wedge dy \;\in\; \Omega^3(M; \mathbb{R}),$$
whose coefficient $\varrho = \varrho(t, x, y, z)$ is the **electric charge density** and whose remaining coefficients assemble into the time-dependent **electric current density** $\vec{j} = (j_x, j_y, j_z)$, a vector field on the spatial slices. The symbol $d$ is the [[Def - Exterior Derivative on a Manifold|exterior derivative]]; $\operatorname{div}\vec{j} = \partial_x j_x + \partial_y j_y + \partial_z j_z$ is the ordinary Euclidean divergence on $\mathbb{R}^3$; $\operatorname{rot}$ is the curl.

For the integrated statement, $B \subseteq \mathbb{R}^3$ is a compact three-dimensional submanifold with smooth boundary $\partial B$, sitting inside a single spatial slice; $\nu$ is the outward-pointing unit normal field of $\partial B$ in $\mathbb{R}^3$; $\mathrm{dvol}_{\partial B}$ is the induced area form on $\partial B$; and $\langle\,\cdot\,,\cdot\,\rangle$ on $\mathbb{R}^3$ is the standard Euclidean inner product, so $\langle \vec{j}, \nu\rangle$ is the outward normal component of the current — the current flowing out through the surface per unit area. We fix two times $t_0 < t_1$ and write $\Omega := [t_0, t_1] \times B \subseteq \mathbb{R}^4$ for the spacetime cylinder over $B$, oriented by the restriction of $\mathrm{vol}$. The full symbol registry is on the parent page [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]].

> [!warning] Convention: the Hodge star and the sign of the inhomogeneous Maxwell equation
> This series uses **Bär's Hodge star** $\star = \star_B$, defined on an oriented $n$-dimensional inner-product space of index $p$ by the relation $\omega \wedge \eta = \langle \star\omega, \eta\rangle\, \mathrm{vol}$ for all $\omega \in \Lambda^k$, $\eta \in \Lambda^{n-k}$ (see [[Def - Hodge Star in Arbitrary Signature]]). The inhomogeneous Maxwell equation is written throughout the series as
> $$d\star F + J = 0,$$
> which is the sign delivered by the Euler–Lagrange equation of the electromagnetic action (see [[Thm - Euler-Lagrange Equation of the Electromagnetic Action]]). Bär's text prints this equation with this sign on p. 86 but, at p. 95, misprints it as "$d\star F = J$"; we use $d\star F + J = 0$ everywhere, and the proof below turns on it. The special-relativity chapters write the same law as $d\star_V F = \mu_0 \star_V j$ in signature $(+,-,-,-)$ with SI units (see [[Thm - Electric Charge Conservation and the Gauss Theorem]]); the dictionary to those pages is $g_B = -g_{\mathrm{SR}}$, hence $\star_B = -\star_V$ on Minkowski, together with the $J$-versus-$j$ sign recorded on [[Def - Charge-Current 3-Form]]. Under that dictionary the continuity equation $\partial_t\varrho + \operatorname{div}\vec{j} = 0$ is the same statement in both conventions.

---

# Statement

> **Theorem (Continuity equation and conservation of charge).** Let $M$ be an oriented Lorentzian four-manifold, $F \in \Omega^2(M; \mathbb{R})$ a field strength, and $J \in \Omega^3(M; \mathbb{R})$ a charge–current $3$-form satisfying the inhomogeneous Maxwell equation
> $$d\star F + J = 0.$$
>
> **(i) Local form (the continuity equation).** Then $J$ is closed:
> $$dJ = 0.$$
> On Minkowski space with the coordinates and $J$ of the Notation section,
> $$dJ = \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\, dt \wedge dx \wedge dy \wedge dz,$$
> so $dJ = 0$ is equivalent to the **continuity equation**
> $$\partial_t \varrho + \operatorname{div}\vec{j} = 0. \tag{3.11}$$
>
> **(ii) Integrated form (conservation of charge).** Let $B \subseteq \mathbb{R}^3$ be a compact three-dimensional submanifold with smooth boundary, and $t_0 < t_1$. Then
> $$\int_B \varrho(t_1, \cdot)\; -\; \int_B \varrho(t_0, \cdot)\; +\; \int_{t_0}^{t_1}\!\!\int_{\partial B} \langle \vec{j}, \nu\rangle \, \mathrm{dvol}_{\partial B}\, dt \;=\; 0.$$
> In words: the change in the total charge inside $B$ between the two times equals minus the total current that has flowed out through the boundary $\partial B$ in that interval. Charge is neither created nor destroyed; it only moves.

Part (i) is Bär's Remark 3.2.6 and equation (3.11); part (ii) is his Example 3.2.2, which asserts the boundary orientation without computing it. The proof below computes it.

---

# Motivation

Conservation of electric charge is one of the most securely established facts in physics, and the theorem says something striking about its status: it is not an independent postulate that must be added to electrodynamics, nor an experimental input, but a *mathematical consequence* of the field equations together with the single identity $d^2 = 0$. Maxwell's inhomogeneous law $d\star F + J = 0$ says how the field is produced by its sources; conservation of the sources then follows automatically, whether we want it or not. This is the pattern by which gauge theories enforce conservation laws, and it is worth seeing in its cleanest instance before it recurs, dressed in more machinery, in Yang–Mills theory and in general relativity.

The role of the theorem in the chapter is therefore twofold. Read forwards, it is a consistency check: any current $\vec{j}$ and density $\varrho$ that we propose as a source for an electromagnetic field are constrained — they must satisfy $\partial_t\varrho + \operatorname{div}\vec{j} = 0$, or no field can source them, because the left-hand side of Maxwell's equation is automatically closed. Read as a template, it is the abelian model for a much more general phenomenon. The inhomogeneous field equation puts the source equal to $d$ of something ($J = -d\star F$), and $d$ of an exact form vanishes; that is the whole content, and it survives verbatim into the non-abelian setting once "$d$" is replaced by the exterior covariant derivative and "closed" by "covariantly closed". The theorem is short, but it is the first place in the series where a conservation law is *derived* rather than imposed.

There is a third thing the theorem answers, which the local form alone does not make visible: *what is conserved, and with respect to what?* The differential statement $\partial_t\varrho + \operatorname{div}\vec{j} = 0$ is a purely local balance — at each point, the rate of change of density is accounted for by the current spreading out. Part (ii) integrates this balance over a region and a time interval and turns it into a bookkeeping identity for a *number*, the total charge in $B$. The passage from the pointwise law to the global tally is exactly a use of Stokes's theorem on the spacetime cylinder $[t_0, t_1] \times B$, and the only subtlety is orienting the three faces of that cylinder correctly — a subtlety Bär waves past and we do not.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal hypothesis is $d\star F + J = 0$, but its usable engine is more general: *whenever a $3$-form $J$ is exact, it is closed, and its integral over any closed hypersurface is a homological invariant.* The interesting question is which situations hand you an exact — or otherwise closed — current $3$-form without saying so.

The first disguised source is **a current that arises as the source term of any first-order field equation of the form $d(\text{something}) + J = 0$.** The bridge is immediate but worth naming: if $J = -d\Theta$ for some $2$-form $\Theta$ (here $\Theta = \star F$), then $dJ = -d^2\Theta = 0$ by [[Thm - d-Squared-is-Zero|the nilpotence of the exterior derivative]]. The non-obvious part in practice is recognising that the object multiplying the derivative *is* globally a form — for the Maxwell field this requires that $F$, hence $\star F$, be a genuine global $2$-form on $M$, which for a $U(1)$-bundle follows because the curvature of an abelian connection descends to the base. *Example problem:* given a proposed pair $(\varrho, \vec{j})$ on spacetime, decide whether it can be the source of *any* electromagnetic field; the answer is yes if and only if $\partial_t\varrho + \operatorname{div}\vec{j} = 0$, because that is precisely the closedness of the $3$-form it defines.

The second disguised source is **a Noether current attached to a continuous symmetry of a gauge-invariant action.** Noether's theorems produce, for each symmetry, a current whose divergence vanishes on solutions of the field equations; for a *gauge* symmetry the current is conserved identically, off shell, which is a differential-form statement $dJ = 0$ in disguise. The bridge is that the field equations of a gauge theory are exactly of the exact-source form above, so the gauge current is exact. The non-obviousness is that gauge symmetry — a redundancy, not a physical symmetry — nevertheless forces a conservation law. *Example problem:* the electric charge is the Noether charge of the global part of the $U(1)$ gauge symmetry; recovering $\partial_t\varrho + \operatorname{div}\vec{j} = 0$ from that symmetry is this theorem read backwards.

The third disguised source is **a $3$-form whose de Rham class is known to vanish, or whose ambient cohomology group is trivial.** If $H^3_{\mathrm{dR}}(M) = 0$ then every closed $3$-form is exact, so "closed" and "exact" coincide, and any argument that produces one produces the other. The bridge runs through [[Thm - The Poincaré Lemma on a Star-Shaped Region|the Poincaré lemma]] on contractible pieces of $M$: on Minkowski space, which is star-shaped, closedness of $J$ already yields a global potential $\Theta$ with $J = d\Theta$. The non-obvious step is that the *local* balance law upgrades to the *global* existence of a potential precisely because the underlying space is topologically trivial. *Example problem:* on $\mathbb{R}^{1,3}$, reconstruct a candidate $\star F$ from a conserved current.

**Targets (Output Amplification).** The bare output is $dJ = 0$. Combined with other ingredients it yields more.

Combine $dJ = 0$ with **Stokes's theorem on a spacetime cylinder**. Integrating the closed $3$-form over the oriented boundary of $\Omega = [t_0, t_1]\times B$ gives, term by term, the integrated conservation law of part (ii): the boundary splits into two spatial caps and one lateral wall, and the caps carry the total charge at the two times while the wall carries the flux. The extra ingredient is the correct induced orientation on each face, and the payoff is that a pointwise identity becomes a statement about a measurable quantity, the charge of a region.

Combine $dJ = 0$ with **the closedness of two spatial slices in a slabless region**. If $\vec{j}$ vanishes on $\partial B$ throughout $[t_0, t_1]$ — no current crosses the wall — the lateral term drops and $\int_B \varrho(t_1) = \int_B \varrho(t_0)$: the total charge in $B$ is *constant in time*. The extra ingredient is a boundary condition, and the payoff is a genuine conserved number, the total charge $Q_B = \int_B\varrho$, which becomes the electric charge of the universe when $B$ is taken to exhaust a Cauchy slice with fields decaying at infinity.

Combine $dJ = 0$ with **the de Rham theorem and Poincaré duality on a closed spatial slice**. On a compact boundaryless spatial slice $S$, integrating the continuity equation shows $\frac{d}{dt}\int_S \varrho = -\int_S \operatorname{div}\vec{j} = 0$, so the total charge is again constant; more sharply, the total charge is the pairing of the cohomology class of the restricted current with the fundamental class $[S]$, hence a topological invariant insensitive to how the charge is distributed. The extra ingredient is the homology of the slice, and the payoff is that global charge is quantised or constrained by topology, the entry point to Dirac's monopole quantisation later in the chapter.

---

# Why Is It True

Strip away the coordinates and the theorem is one line of algebra. The inhomogeneous Maxwell equation $d\star F + J = 0$ can be read as a *definition* of $J$: it says $J = -d\star F$. So the current $3$-form is, up to sign, the exterior derivative of the $2$-form $\star F$ — it is **exact**. And an exact form is closed, because applying $d$ again lands you on $d^2(\star F)$, which is zero by [[Thm - d-Squared-is-Zero|the nilpotence of the exterior derivative]]. Hence $dJ = -d^2(\star F) = 0$. There is nothing more to the local law than this.

> **The mechanism in one sentence: $J$ is exact — it equals $d$ of $\star F$ up to sign — and $d$ of an exact form vanishes, so $J$ is closed; in Minkowski coordinates "closed" reads off as $\partial_t\varrho + \operatorname{div}\vec{j} = 0$.**

Why does "closed" translate into the familiar continuity equation? Because the exterior derivative of the specific $3$-form $J$ is a $4$-form, and on four-dimensional spacetime a $4$-form has a single component, the coefficient of $dt\wedge dx\wedge dy\wedge dz$. Computing that coefficient, each term of $J$ contributes exactly one derivative that does not annihilate: the density term $\varrho\, dx\wedge dy\wedge dz$ can only be differentiated in $t$ (any spatial derivative repeats an existing $dx, dy$, or $dz$ and dies), giving $\partial_t\varrho$; each current term $-j_i\, dt\wedge(\cdots)$ can only be differentiated in its missing spatial direction, and the three of them assemble into $\operatorname{div}\vec{j}$. The sum of the surviving derivatives is the total coefficient, and setting it to zero is the continuity equation. The four-dimensionality is doing real work: it is what makes $dJ$ a top form with one component, so that a single scalar equation captures the whole of $dJ = 0$.

The global law is what you get by adding up the local law over a region of spacetime. Think of the solid spacetime cylinder $\Omega = [t_0, t_1]\times B$: a stack of copies of the spatial region $B$, one for each instant between $t_0$ and $t_1$. Its boundary has three parts — the top cap $\{t_1\}\times B$, the bottom cap $\{t_0\}\times B$, and the lateral wall $[t_0, t_1]\times\partial B$. Integrating the closed form $J$ over this boundary must give zero, because by Stokes the boundary integral equals the integral of $dJ = 0$ over the interior. On the caps only the density part of $J$ survives (they are surfaces of constant time, so $dt$ pulls back to zero), giving the charge inside $B$ at each time; on the wall only the current part survives (it is a surface of constant spatial position on $\partial B$, so the pure-space $3$-form dies), giving the flux through $\partial B$. The bottom cap comes with a *reversed* orientation — its outward normal points into the past — which is exactly why the two charges enter with opposite signs. The identity is then charge-at-$t_1$ minus charge-at-$t_0$ plus outward flux equals zero, which is the accountant's statement that the charge that left the region is the charge that is no longer inside it.

---

# What Makes This Hard

Two things. First, the local law is deceptively trivial *as algebra* but rests on $J$ being a globally defined $3$-form and $\star F$ a globally defined $2$-form; the sleight one must not commit is to write "$J = -d\star F$ so $dJ = 0$" while quietly assuming the potential $\star F$ exists globally — it does here because $F$ is the descended curvature of an abelian connection, but the same words applied to a merely *closed* $J$ on a topologically nontrivial space would be wrong, since a closed form need not be exact. Second, the entire difficulty of the integrated law is orientation bookkeeping. The spacetime cylinder is a manifold *with corners* (the edges where the caps meet the wall), so one must either invoke Stokes in its corner version or reduce to Fubini; and the induced orientation of each of the three faces must be computed from the outward-normal-first convention, not guessed. The single most common error is to give the bottom cap $\{t_0\}\times B$ the standard orientation of $B$; its induced orientation is the *opposite*, because the outward normal there is $-\partial_t$, and getting this wrong flips the sign of the initial charge and destroys the conservation law.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For part (i), apply $d$ to the field equation and use $d^2 = 0$ to get $dJ = 0$; then compute $dJ$ in Minkowski coordinates and read off the continuity equation. For part (ii), integrate the closed form $J$ over the boundary of the spacetime cylinder $\Omega = [t_0, t_1]\times B$ using Stokes; evaluate the three face integrals by determining each face's induced orientation and restricting $J$ to it; the interior integral is zero because $dJ = 0$, so the three face contributions sum to zero.

**Subgoal decomposition:**

1. **Closedness of $J$.** Show $dJ = 0$ directly from $d\star F + J = 0$.
   - *Hint:* Apply $d$ to both sides and use that $d\circ d = 0$ on the $\star F$ term.
   - *Why needed:* This is the entire content of the local law; the coordinate identity and the global law both rest on it.

2. **Coordinate form of $dJ$.** Compute $dJ$ for the explicit $J$ and reduce $dJ = 0$ to $\partial_t\varrho + \operatorname{div}\vec{j} = 0$.
   - *Hint:* Only one derivative survives per term because wedging a repeated differential kills it; track the sign of each reordering to $dt\wedge dx\wedge dy\wedge dz$.
   - *Why needed:* It identifies the abstract statement $dJ = 0$ with the physical continuity equation (3.11).

3. **The flux $2$-form identity.** Show that the spatial $2$-form $\Phi = j_x\, dy\wedge dz + j_y\, dz\wedge dx + j_z\, dx\wedge dy$ restricts on $\partial B$ to $\langle\vec{j}, \nu\rangle\, \mathrm{dvol}_{\partial B}$, and that $J$ restricts on the lateral wall to $-dt\wedge\Phi$.
   - *Hint:* $\Phi = \iota_{\vec{j}}(dx\wedge dy\wedge dz)$; decompose $\vec{j}$ into normal and tangential parts on $\partial B$ and use that a top form on a surface kills three tangent vectors.
   - *Why needed:* It turns the abstract lateral face integral into the physical outward flux.

4. **Induced orientations of the three faces.** Determine, from the outward-normal-first convention, the induced orientation of the top cap ($+B$), the bottom cap ($-B$), and the lateral wall.
   - *Hint:* The outward normal is $+\partial_t$ on the top, $-\partial_t$ on the bottom, and the spatial $\nu$ on the wall; apply the convention "$(\nu, E_1, \ldots)$ positive in $M$ iff $(E_1, \ldots)$ positive in the face".
   - *Why needed:* The relative signs of the three boundary terms — in particular the minus on the initial charge — are exactly these orientations.

5. **Assembly by Stokes.** Combine: $0 = \int_\Omega dJ = \int_{\partial\Omega} J = (\text{top}) + (\text{bottom}) + (\text{wall})$, and substitute the three evaluated integrals.
   - *Hint:* Handle the corners of $\Omega$ by Stokes for manifolds with corners, or cross-check the whole thing by Fubini (subgoal 5 alternative).
   - *Why needed:* It produces the integrated conservation law and shows the three physical quantities balance.

---

# Lemma Decomposition

> [!note]- Lemma 1: An exact form is closed; hence $d\star F + J = 0$ forces $dJ = 0$
> **Statement:** Let $\Theta$ be a smooth $2$-form on a manifold $M$ and $J$ a smooth $3$-form with $d\Theta + J = 0$. Then $dJ = 0$.
>
> **Hint:** Solve for $J$ and apply $d$ once more; the nilpotence of $d$ kills the resulting $d^2\Theta$.
>
> **Why needed:** With $\Theta = \star F$ this is exactly the abstract local law $dJ = 0$, the heart of the theorem.
>
> > [!note]- Full proof
> > **Goal.** We are given $d\Theta + J = 0$ and must show $dJ = 0$.
> >
> > **Solve for $J$.** From $d\Theta + J = 0$ we have $J = -d\Theta$ (adding $-d\Theta$ to both sides).
> >
> > **Apply $d$.** Since $d$ is linear,
> > $$dJ = d(-d\Theta) = -d(d\Theta) = -d^2\Theta \qquad \text{(linearity of the exterior derivative).}$$
> > By [[Thm - d-Squared-is-Zero|the nilpotence of the exterior derivative]] — for every smooth form $\alpha$ on a smooth manifold, $d(d\alpha) = 0$ — applied to $\alpha = \Theta$, we have $d^2\Theta = 0$. Therefore
> > $$dJ = -d^2\Theta = 0 \qquad \text{(by } d^2 = 0\text{).}$$
> >
> > **Conclusion.** $J$ is closed. In the theorem, $\Theta = \star F$, and the hypothesis $d\star F + J = 0$ is precisely $d\Theta + J = 0$, so $dJ = 0$. $\blacksquare$

> [!note]- Lemma 2: Coordinate computation of $dJ$ on Minkowski space
> **Statement:** For $J = \varrho\, dx\wedge dy\wedge dz - j_x\, dt\wedge dy\wedge dz - j_y\, dt\wedge dz\wedge dx - j_z\, dt\wedge dx\wedge dy$ on $\mathbb{R}^{1,3}$,
> $$dJ = \big(\partial_t\varrho + \partial_x j_x + \partial_y j_y + \partial_z j_z\big)\, dt\wedge dx\wedge dy\wedge dz = \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\,\mathrm{vol}.$$
>
> **Hint:** For each term, only the one partial derivative whose differential is not already present survives; carefully reorder each surviving $4$-form to the standard $dt\wedge dx\wedge dy\wedge dz$ and record the permutation sign.
>
> **Why needed:** It identifies the abstract $dJ = 0$ with the continuity equation (3.11), and supplies the top-form coefficient used again in the Fubini cross-check of part (ii).
>
> > [!note]- Full proof
> > **Goal.** Compute $dJ$ term by term. We use that for a coordinate function $u \in \{t, x, y, z\}$ and a coordinate $p$-form $\alpha_I = du^{i_1}\wedge\cdots\wedge du^{i_p}$, the exterior derivative of $f\,\alpha_I$ is $df\wedge\alpha_I = \sum_u (\partial_u f)\, du\wedge\alpha_I$, and that $du\wedge\alpha_I = 0$ whenever $du$ already appears in $\alpha_I$ (a repeated differential; [[Thm - Wedge Product Properties|the wedge product is alternating]]).
> >
> > **Term 1: the density term $\varrho\, dx\wedge dy\wedge dz$.** Here $\alpha = dx\wedge dy\wedge dz$ already contains $dx, dy, dz$, so of the four terms $\partial_u\varrho\, du\wedge\alpha$ only $u = t$ survives:
> > $$d(\varrho\, dx\wedge dy\wedge dz) = \partial_t\varrho\; dt\wedge dx\wedge dy\wedge dz \qquad \text{(the } dx, dy, dz \text{ derivatives give repeated differentials, hence } 0\text{).}$$
> >
> > **Term 2: the current term $-j_x\, dt\wedge dy\wedge dz$.** Here $\alpha = dt\wedge dy\wedge dz$ contains $dt, dy, dz$, so only $u = x$ survives:
> > $$d(-j_x\, dt\wedge dy\wedge dz) = -\partial_x j_x\; dx\wedge dt\wedge dy\wedge dz.$$
> > Reordering $dx\wedge dt\wedge dy\wedge dz$ to standard order costs one transposition ($dx \leftrightarrow dt$): $dx\wedge dt\wedge dy\wedge dz = -\,dt\wedge dx\wedge dy\wedge dz$. Hence
> > $$d(-j_x\, dt\wedge dy\wedge dz) = +\,\partial_x j_x\; dt\wedge dx\wedge dy\wedge dz \qquad \text{(one sign flip from the transposition).}$$
> >
> > **Term 3: the current term $-j_y\, dt\wedge dz\wedge dx$.** Here $\alpha = dt\wedge dz\wedge dx$ contains $dt, dz, dx$, so only $u = y$ survives:
> > $$d(-j_y\, dt\wedge dz\wedge dx) = -\partial_y j_y\; dy\wedge dt\wedge dz\wedge dx.$$
> > The reordering of $dy\wedge dt\wedge dz\wedge dx = (y, t, z, x)$ to $(t, x, y, z)$ is the permutation $(3,1,4,2)$ of the standard positions, which has three inversions $\{(3,1),(3,2),(4,2)\}$, hence sign $-1$: $dy\wedge dt\wedge dz\wedge dx = -\,dt\wedge dx\wedge dy\wedge dz$. Therefore
> > $$d(-j_y\, dt\wedge dz\wedge dx) = +\,\partial_y j_y\; dt\wedge dx\wedge dy\wedge dz \qquad \text{(odd permutation, one net sign flip).}$$
> >
> > **Term 4: the current term $-j_z\, dt\wedge dx\wedge dy$.** Here $\alpha = dt\wedge dx\wedge dy$ contains $dt, dx, dy$, so only $u = z$ survives:
> > $$d(-j_z\, dt\wedge dx\wedge dy) = -\partial_z j_z\; dz\wedge dt\wedge dx\wedge dy.$$
> > The reordering of $dz\wedge dt\wedge dx\wedge dy = (z, t, x, y) = (4,1,2,3)$ to $(t,x,y,z)$ has three inversions $\{(4,1),(4,2),(4,3)\}$, hence sign $-1$: $dz\wedge dt\wedge dx\wedge dy = -\,dt\wedge dx\wedge dy\wedge dz$. Therefore
> > $$d(-j_z\, dt\wedge dx\wedge dy) = +\,\partial_z j_z\; dt\wedge dx\wedge dy\wedge dz \qquad \text{(odd permutation, one net sign flip).}$$
> >
> > **Sum.** Adding the four contributions (each already a multiple of $dt\wedge dx\wedge dy\wedge dz$),
> > $$dJ = \big(\partial_t\varrho + \partial_x j_x + \partial_y j_y + \partial_z j_z\big)\, dt\wedge dx\wedge dy\wedge dz = \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\,\mathrm{vol}.$$
> >
> > **Conclusion.** Since $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$ is nowhere vanishing, $dJ = 0$ holds if and only if its coefficient vanishes identically, i.e. $\partial_t\varrho + \operatorname{div}\vec{j} = 0$. $\blacksquare$

> [!note]- Lemma 3: The flux $2$-form and the restriction of $J$ to the lateral wall
> **Statement:** Let $\Phi := j_x\, dy\wedge dz + j_y\, dz\wedge dx + j_z\, dx\wedge dy$ on $\mathbb{R}^3$. Then $\Phi = \iota_{\vec{j}}(dx\wedge dy\wedge dz)$, and on the boundary surface $\partial B$ with outward unit normal $\nu$ and induced area form $\mathrm{dvol}_{\partial B}$,
> $$\iota^*_{\partial B}\Phi = \langle\vec{j}, \nu\rangle\, \mathrm{dvol}_{\partial B}.$$
> Moreover, the pullback of $J$ to the lateral wall $[t_0, t_1]\times\partial B$ equals $-\,dt\wedge\Phi$ (and the density term $\varrho\, dx\wedge dy\wedge dz$ pulls back to $0$ there).
>
> **Hint:** For the identity on $\partial B$, split $\vec{j} = \langle\vec{j},\nu\rangle\,\nu + \vec{j}_{\mathrm{tan}}$ and note the tangential part contributes a top form evaluated on three vectors tangent to a $2$-surface. For the restriction of $J$, note $dx\wedge dy\wedge dz$ vanishes on a domain constrained to a $2$-surface in space.
>
> **Why needed:** It converts the abstract lateral face integral $\int_{[t_0,t_1]\times\partial B} J$ into the physical outward flux $\int_{t_0}^{t_1}\!\int_{\partial B}\langle\vec{j},\nu\rangle$.
>
> > [!note]- Full proof
> > **Goal.** Establish the three claims: (a) $\Phi = \iota_{\vec{j}}(dx\wedge dy\wedge dz)$; (b) $\iota^*_{\partial B}\Phi = \langle\vec{j},\nu\rangle\,\mathrm{dvol}_{\partial B}$; (c) $\iota^*_{\mathrm{wall}} J = -dt\wedge\Phi$.
> >
> > **Step 0 — set-up.** Write $\mathrm{vol}_3 = dx\wedge dy\wedge dz$ for the Euclidean volume form on $\mathbb{R}^3$, and recall the [[Def - Interior Product (Contraction with a Vector Field)|interior product]] $\iota_X$: for a $p$-form $\alpha$, $(\iota_X\alpha)(Y_1,\ldots,Y_{p-1}) = \alpha(X, Y_1,\ldots,Y_{p-1})$.
> >
> > **Part (a): $\Phi = \iota_{\vec{j}}\mathrm{vol}_3$.** Using $\iota_X(\beta\wedge\gamma) = (\iota_X\beta)\wedge\gamma + (-1)^{\deg\beta}\beta\wedge(\iota_X\gamma)$ and $\iota_{\vec j}\,dx = j_x$ (likewise $dy, dz$),
> > $$\iota_{\vec{j}}(dx\wedge dy\wedge dz) = j_x\, dy\wedge dz - j_y\, dx\wedge dz + j_z\, dx\wedge dy \qquad \text{(interior product is an antiderivation).}$$
> > Rewriting $-\,dx\wedge dz = +\,dz\wedge dx$ (one transposition) gives $\iota_{\vec{j}}(dx\wedge dy\wedge dz) = j_x\, dy\wedge dz + j_y\, dz\wedge dx + j_z\, dx\wedge dy = \Phi$, as claimed.
> >
> > **Part (b): restriction to $\partial B$.** At a point of $\partial B$, decompose $\vec{j} = \langle\vec{j},\nu\rangle\,\nu + \vec{j}_{\mathrm{tan}}$, where $\vec{j}_{\mathrm{tan}} \in T_p\partial B$ is tangent to the surface. By linearity of $\iota_X$ in $X$,
> > $$\iota_{\vec{j}}\mathrm{vol}_3 = \langle\vec{j},\nu\rangle\,\iota_\nu\mathrm{vol}_3 + \iota_{\vec{j}_{\mathrm{tan}}}\mathrm{vol}_3 \qquad \text{(linearity of the interior product in the vector slot).}$$
> > Pull back by the inclusion $\iota_{\partial B}: \partial B \hookrightarrow \mathbb{R}^3$ and evaluate on any pair of tangent vectors $w_1, w_2 \in T_p\partial B$. For the tangential term,
> > $$(\iota_{\vec{j}_{\mathrm{tan}}}\mathrm{vol}_3)(w_1, w_2) = \mathrm{vol}_3(\vec{j}_{\mathrm{tan}}, w_1, w_2) = 0,$$
> > because $\vec{j}_{\mathrm{tan}}, w_1, w_2$ all lie in the two-dimensional space $T_p\partial B$ and are therefore linearly dependent, so the alternating $3$-form $\mathrm{vol}_3$ vanishes on them ([[Def - Alternating Tensor and Lambda k V Dual|an alternating form vanishes on linearly dependent arguments]]). For the normal term, the induced area form on $\partial B$ is by definition $\mathrm{dvol}_{\partial B} = \iota^*_{\partial B}(\iota_\nu\mathrm{vol}_3)$ with $\nu$ the outward normal (this is the [[Def - Manifold with Boundary and Induced Orientation|orientation-form-by-contraction construction]] with the boundary of $B$). Hence
> > $$\iota^*_{\partial B}\Phi = \langle\vec{j},\nu\rangle\,\iota^*_{\partial B}(\iota_\nu\mathrm{vol}_3) = \langle\vec{j},\nu\rangle\,\mathrm{dvol}_{\partial B}.$$
> >
> > **Part (c): restriction of $J$ to the wall.** The lateral wall is $[t_0, t_1]\times\partial B$, on which the spatial coordinates are constrained to the $2$-surface $\partial B$. The density term $\varrho\, dx\wedge dy\wedge dz$ pulls back to $0$: it is a purely spatial $3$-form, and its restriction to the (at most) two-dimensional spatial directions of the wall vanishes by the same linear-dependence argument as in part (b). For the current terms, group them:
> > $$-\,j_x\, dt\wedge dy\wedge dz - j_y\, dt\wedge dz\wedge dx - j_z\, dt\wedge dx\wedge dy = -\,dt\wedge\big(j_x\, dy\wedge dz + j_y\, dz\wedge dx + j_z\, dx\wedge dy\big) = -\,dt\wedge\Phi \qquad \text{(factoring the common } dt \text{ to the left).}$$
> > Pulling this back to the wall leaves $-dt\wedge\iota^*_{\partial B}\Phi$ intact (the $dt$ direction survives; the spatial part restricts to $\partial B$). Therefore $\iota^*_{\mathrm{wall}} J = -\,dt\wedge\Phi$.
> >
> > **Conclusion.** All three claims hold. $\blacksquare$

> [!note]- Lemma 4: Induced orientations of the three faces of the spacetime cylinder
> **Statement:** Orient $\Omega = [t_0, t_1]\times B \subseteq \mathbb{R}^4$ by $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$. Under the outward-normal-first convention, the boundary faces carry these induced orientations: the top cap $\{t_1\}\times B$ carries the standard orientation of $B$ (that of $dx\wedge dy\wedge dz$); the bottom cap $\{t_0\}\times B$ carries the *opposite* of the standard orientation of $B$; and the lateral wall $[t_0, t_1]\times\partial B$ is oriented so that integration of a form $-dt\wedge\Phi$ over it, with $\Phi$ a spatial $2$-form, equals $+\int_{t_0}^{t_1}\!\int_{\partial B}\iota^*_{\partial B}\Phi\, dt$.
>
> **Hint:** The outward normals are $+\partial_t$ (top), $-\partial_t$ (bottom), and the spatial outward normal $\nu$ of $\partial B$ (wall). Apply "$(N, E_1,\ldots,E_{n-1})$ positive in $\Omega$ iff $(E_1,\ldots,E_{n-1})$ positive in the face".
>
> **Why needed:** These three orientations are precisely the relative signs of the three boundary terms in the conservation law — in particular the minus sign on the initial charge.
>
> > [!note]- Full proof
> > **Goal.** Determine the induced orientation on each of the three codimension-one faces of $\Omega$, using the [[Def - Manifold with Boundary and Induced Orientation|outward-normal-first convention]]: a basis $(E_1, E_2, E_3)$ of a face is positively oriented if and only if $(N, E_1, E_2, E_3)$ is positively oriented in $\Omega$, where $N$ is any outward-pointing vector and $\Omega$ carries the orientation of $dt\wedge dx\wedge dy\wedge dz$, i.e. the standard order $(\partial_t, \partial_x, \partial_y, \partial_z)$ is positive.
> >
> > **Top cap $\{t_1\}\times B$.** The outward normal points in the direction of increasing $t$, so $N = +\partial_t$. The candidate basis $(\partial_x, \partial_y, \partial_z)$ of the cap is positive if and only if $(\partial_t, \partial_x, \partial_y, \partial_z)$ is positive in $\Omega$ — which it is, being the standard order. Hence the top cap carries the standard orientation of $B$.
> >
> > **Bottom cap $\{t_0\}\times B$.** The outward normal points toward decreasing $t$ (out of $\Omega$, into the past), so $N = -\partial_t$. The candidate basis $(\partial_x, \partial_y, \partial_z)$ is positive if and only if $(-\partial_t, \partial_x, \partial_y, \partial_z)$ is positive in $\Omega$. But
> > $$(-\partial_t, \partial_x, \partial_y, \partial_z) = -\,(\partial_t, \partial_x, \partial_y, \partial_z),$$
> > which is *negatively* oriented (scaling one basis vector by $-1$ reverses orientation). Hence $(\partial_x, \partial_y, \partial_z)$ is negatively oriented for the bottom cap: the bottom cap carries the orientation *opposite* to the standard orientation of $B$.
> >
> > **Lateral wall $[t_0, t_1]\times\partial B$.** At an interior point of the wall (with $t_0 < t < t_1$) the outward normal is the spatial outward normal $\nu$ of $\partial B$ (it is purely spatial, since moving in $t$ stays inside $\Omega$). Let $(w_1, w_2)$ be a positively oriented basis of $\partial B$ for its induced (outward-normal-first) orientation, so that $(\nu, w_1, w_2)$ is positive in $\mathbb{R}^3$ with order $(\partial_x, \partial_y, \partial_z)$; equivalently $\mathrm{dvol}_{\partial B}(w_1, w_2) > 0$. Test the ordered basis $(\partial_t, w_1, w_2)$ of the wall: it is positively oriented for the wall if and only if $(\nu, \partial_t, w_1, w_2)$ is positive in $\Omega$. Now
> > $$(\nu, \partial_t, w_1, w_2) = -\,(\partial_t, \nu, w_1, w_2) \qquad \text{(one transposition } \nu \leftrightarrow \partial_t\text{)},$$
> > and $(\partial_t, \nu, w_1, w_2)$ is positive in $\Omega$ if and only if the spatial triple $(\nu, w_1, w_2)$ is positive in $\mathbb{R}^3$ (the leading $\partial_t$ contributes no sign), which holds by the choice of $(w_1, w_2)$. Therefore $(\partial_t, \nu, w_1, w_2)$ is positive and $(\nu, \partial_t, w_1, w_2)$ is negative, so $(\partial_t, w_1, w_2)$ is a *negatively* oriented basis of the wall.
> >
> > **Consequence for the wall integral.** The last computation says the wall's induced orientation is the *opposite* of the product orientation $dt\wedge\mathrm{dvol}_{\partial B}$ determined by $(\partial_t, w_1, w_2)$. Hence, for any spatial $2$-form $\Phi$, integrating $-dt\wedge\Phi$ over the wall with its induced orientation flips the sign relative to the product orientation:
> > $$\int_{[t_0,t_1]\times\partial B,\, \mathrm{induced}} \big(-dt\wedge\Phi\big) = -\int_{[t_0,t_1]\times\partial B,\, dt\wedge\mathrm{dvol}_{\partial B}} \big(-dt\wedge\Phi\big) = +\int_{t_0}^{t_1}\!\!\int_{\partial B} \iota^*_{\partial B}\Phi\, dt,$$
> > where the last equality is Fubini for the product orientation. This is the claimed formula.
> >
> > **Conclusion.** Top: $+B$; bottom: $-B$; wall: the sign that makes $\int_{\mathrm{wall}}(-dt\wedge\Phi) = +\int_{t_0}^{t_1}\!\int_{\partial B}\iota^*_{\partial B}\Phi\, dt$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M$ be an oriented Lorentzian four-manifold, $F \in \Omega^2(M;\mathbb{R})$, $J \in \Omega^3(M;\mathbb{R})$, and assume the inhomogeneous Maxwell equation $d\star F + J = 0$.
>
> ## Part (i): the continuity equation
>
> **Step 1 — $J$ is closed.** The hypothesis $d\star F + J = 0$ has the form $d\Theta + J = 0$ with $\Theta = \star F \in \Omega^2(M;\mathbb{R})$. By Lemma 1 (an exact form is closed), $dJ = 0$. Explicitly, $J = -d\star F$, so $dJ = -d(d\star F) = -d^2(\star F) = 0$ by [[Thm - d-Squared-is-Zero|the nilpotence of the exterior derivative]], $d\circ d = 0$.
>
> **Step 2 — coordinate form on Minkowski space.** Take $M = \mathbb{R}^{1,3}$ with the coordinates and the explicit $J$ of the Notation section. By Lemma 2,
> $$dJ = \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\, dt\wedge dx\wedge dy\wedge dz = \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\,\mathrm{vol}.$$
>
> **Step 3 — read off (3.11).** By Step 1, $dJ = 0$. Since $\mathrm{vol}$ is nowhere vanishing, a multiple $c\,\mathrm{vol}$ vanishes if and only if the scalar coefficient $c$ vanishes identically. Combining with the expression of Step 2,
> $$0 = dJ = \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\,\mathrm{vol} \quad\Longleftrightarrow\quad \partial_t\varrho + \operatorname{div}\vec{j} = 0.$$
> This is the continuity equation (3.11). Part (i) is proved.
>
> ## Part (ii): conservation of charge
>
> Fix a compact three-dimensional submanifold $B \subseteq \mathbb{R}^3$ with smooth boundary and times $t_0 < t_1$; set $\Omega = [t_0, t_1]\times B$, oriented by $\mathrm{vol}$.
>
> **Step 0 — $\Omega$ is a compact oriented manifold with corners.** As a product of the compact manifold-with-boundary $[t_0, t_1]$ and the compact manifold-with-boundary $B$, the set $\Omega$ is a compact oriented four-manifold with corners; its codimension-one boundary faces are the top cap $\{t_1\}\times B$, the bottom cap $\{t_0\}\times B$, and the lateral wall $[t_0, t_1]\times\partial B$, meeting along the codimension-two corner set $\{t_0, t_1\}\times\partial B$, which has three-dimensional measure zero inside $\partial\Omega$. [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] holds on manifolds with corners, the boundary integral being the sum of the integrals over the codimension-one faces, each with its induced orientation.
>
> **Step 1 — apply Stokes.** By [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] — for an oriented compact $n$-manifold with corners $\Omega$ and a smooth $(n-1)$-form $\omega$, $\int_\Omega d\omega = \int_{\partial\Omega}\omega$ with $\partial\Omega$ carrying the induced orientation — applied to the $3$-form $J$ on the four-manifold $\Omega$,
> $$\int_\Omega dJ = \int_{\partial\Omega} J = \int_{\{t_1\}\times B} J + \int_{\{t_0\}\times B} J + \int_{[t_0,t_1]\times\partial B} J.$$
> By Part (i), $dJ = 0$, so the left-hand side is $\int_\Omega 0 = 0$:
> $$0 = \int_{\{t_1\}\times B} J + \int_{\{t_0\}\times B} J + \int_{[t_0,t_1]\times\partial B} J. \tag{$\ast$}$$
>
> **Step 2 — the two caps.** On a cap $\{t_*\}\times B$ ($t_* \in \{t_0, t_1\}$), the coordinate $t$ is constant, so $dt$ pulls back to $0$; every current term of $J$ contains a factor $dt$ and hence pulls back to $0$, leaving only the density term:
> $$\iota^*_{\mathrm{cap}} J = \varrho(t_*, \cdot)\, dx\wedge dy\wedge dz.$$
> By Lemma 4, the top cap carries the standard orientation of $B$ and the bottom cap the opposite. Therefore
> $$\int_{\{t_1\}\times B} J = +\int_B \varrho(t_1, \cdot)\, dx\wedge dy\wedge dz = \int_B \varrho(t_1, \cdot), \qquad \int_{\{t_0\}\times B} J = -\int_B \varrho(t_0, \cdot)\, dx\wedge dy\wedge dz = -\int_B \varrho(t_0, \cdot),$$
> the minus sign on the second integral being exactly the reversed orientation of the bottom cap established in Lemma 4.
>
> **Step 3 — the lateral wall.** By Lemma 3, on the wall $J$ pulls back to $-dt\wedge\Phi$ with $\Phi = j_x\,dy\wedge dz + j_y\,dz\wedge dx + j_z\,dx\wedge dy$, and $\iota^*_{\partial B}\Phi = \langle\vec{j},\nu\rangle\,\mathrm{dvol}_{\partial B}$. By Lemma 4, integrating $-dt\wedge\Phi$ over the wall with its induced orientation gives
> $$\int_{[t_0,t_1]\times\partial B} J = \int_{[t_0,t_1]\times\partial B} \big(-dt\wedge\Phi\big) = +\int_{t_0}^{t_1}\!\!\int_{\partial B} \iota^*_{\partial B}\Phi\, dt = \int_{t_0}^{t_1}\!\!\int_{\partial B} \langle\vec{j}, \nu\rangle\, \mathrm{dvol}_{\partial B}\, dt.$$
>
> **Step 4 — combine.** Substituting the three evaluated integrals of Steps 2–3 into $(\ast)$,
> $$0 = \int_B \varrho(t_1, \cdot) - \int_B \varrho(t_0, \cdot) + \int_{t_0}^{t_1}\!\!\int_{\partial B} \langle\vec{j}, \nu\rangle\, \mathrm{dvol}_{\partial B}\, dt,$$
> which is the integrated conservation of charge. Part (ii) is proved.
>
> **Step 5 — independent cross-check by Fubini (rigour at the corners).** To confirm the corner handling of Step 0, evaluate $\int_\Omega dJ$ directly, without appeal to the corner version of Stokes. Using Lemma 2, $dJ = (\partial_t\varrho + \operatorname{div}\vec{j})\,\mathrm{vol}$, and by Fubini's theorem on the product $\Omega = [t_0, t_1]\times B$,
> $$\int_\Omega dJ = \int_{t_0}^{t_1}\!\!\int_B \big(\partial_t\varrho + \operatorname{div}\vec{j}\big)\, dx\,dy\,dz\, dt.$$
> Split the integrand. For the density part, the fundamental theorem of calculus in $t$ gives, for each fixed spatial point, $\int_{t_0}^{t_1}\partial_t\varrho\, dt = \varrho(t_1, \cdot) - \varrho(t_0, \cdot)$, so
> $$\int_{t_0}^{t_1}\!\!\int_B \partial_t\varrho\; dV\, dt = \int_B \big(\varrho(t_1, \cdot) - \varrho(t_0, \cdot)\big)\, dV = \int_B \varrho(t_1, \cdot) - \int_B \varrho(t_0, \cdot) \qquad \text{(Fubini, then FTC in } t\text{).}$$
> For the current part, at each fixed $t$ apply [[Thm - The Divergence Theorem|the divergence theorem]] — for a smooth vector field $\vec{j}$ on a neighbourhood of a compact $B \subseteq \mathbb{R}^3$ with smooth boundary, $\int_B \operatorname{div}\vec{j}\, dV = \int_{\partial B}\langle\vec{j},\nu\rangle\, \mathrm{dvol}_{\partial B}$ with $\nu$ the outward normal — to obtain
> $$\int_{t_0}^{t_1}\!\!\int_B \operatorname{div}\vec{j}\; dV\, dt = \int_{t_0}^{t_1}\!\!\int_{\partial B} \langle\vec{j}, \nu\rangle\, \mathrm{dvol}_{\partial B}\, dt \qquad \text{(divergence theorem at each fixed } t\text{).}$$
> Adding the two and using $\int_\Omega dJ = 0$ reproduces the identity of Step 4. (The divergence theorem is itself the case $n = 3$ of Stokes combined with Lemma 3, so this cross-check is Stokes on $\Omega$ unpacked coordinate-wise; the two routes agree, confirming the corner book-keeping.) $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fluid dynamics: mass conservation.** In an incompressible or compressible fluid with mass density $\varrho$ and velocity field $\vec{v}$, the mass current is $\vec{j} = \varrho\vec{v}$, and the same continuity equation $\partial_t\varrho + \operatorname{div}(\varrho\vec{v}) = 0$ expresses conservation of mass. The theorem applies verbatim once one packages $(\varrho, \varrho\vec{v})$ into a spacetime $3$-form $J$; the exercise is to show that this $J$ is closed, and to interpret the integrated law as "the mass in a control volume changes only through flux across its walls". What is non-obvious is that the *same* mathematics — an exact source form on a four-dimensional spacetime — governs a situation with no electromagnetic field at all; the conservation is a property of the divergence structure, not of electromagnetism.

**Probability and continuous Markov processes: the Fokker–Planck equation.** For a diffusion with probability density $\varrho(t, x)$ and probability current $\vec{j} = \vec{b}\varrho - D\nabla\varrho$ (drift minus diffusion), the Fokker–Planck equation is exactly $\partial_t\varrho + \operatorname{div}\vec{j} = 0$. The exercise is to verify that total probability $\int_{\mathbb{R}^n}\varrho\, dV = 1$ is conserved by integrating the continuity equation and using decay of $\vec{j}$ at infinity, precisely the boundary-flux argument of part (ii) with $\partial B$ pushed to infinity. It is non-obvious that normalisation of a probability distribution over time is *the same theorem* as conservation of electric charge; both are the statement that a closed current $3$-form has vanishing net flux through a closed hypersurface.

**Topology: the degree of a map and homological invariance of flux.** On a closed oriented spatial slice $S$, a closed $3$-form (or its lower-dimensional analogue) has an integral over $S$ that depends only on its de Rham class, by Stokes. The exercise is to show that if the current on two homologous cycles differs by an exact form, the total charge measured on them is equal — so global charge is a homological pairing $\langle[J], [S]\rangle$, not a geometric quantity. This is non-obvious because it says the *number* of units of charge is rigid under any continuous redistribution, which is the seed of charge quantisation and the reason Dirac's monopole argument can succeed later in the chapter.

---

# Bridges

- **The Yang–Mills current and covariant conservation.** The abelian argument here — $J = -d\star F$ is exact, hence $dJ = 0$ — has a non-abelian copy. For a Yang–Mills field with a source, the field equation reads $d^A\star F_A + J = 0$ with $d^A$ the [[Def - Exterior Covariant Derivative on a Vector Bundle|exterior covariant derivative]], and applying $d^A$ again gives $d^A J = -\,(d^A)^2\star F_A = -[F_A\wedge\star F_A]$, which vanishes by the antisymmetry of the bracket paired against the symmetry of $\star$; the conclusion is *covariant* conservation $d^A J = 0$ rather than ordinary conservation. The construction to hold onto is that the same "$d$ of the field equation" move works, with $(d^A)^2 = [F_A\wedge\,\cdot\,]$ replacing $d^2 = 0$.

- **Stress–energy conservation in general relativity.** The identical pattern — a differential identity forcing a conservation law — recurs for the energy–momentum tensor: the [[Thm - Bianchi Identity for a Principal Connection|contracted Bianchi identity]] forces $\operatorname{div} T = 0$ on solutions of the Einstein equations, exactly as $d^2 = 0$ forces $dJ = 0$ here. The bridge is that both are cases of "a geometric identity, applied to a field equation, yields conservation of the source"; conservation of energy–momentum is the gravitational analogue of conservation of charge, and this theorem is the toy model in which the mechanism is visible without curvature getting in the way.

- **De Rham cohomology and the potential for a conserved current.** On a spacetime where $H^3_{\mathrm{dR}} = 0$ — Minkowski space, by [[Thm - The Poincaré Lemma on a Star-Shaped Region|the Poincaré lemma]] — the closedness $dJ = 0$ established here is equivalent to the *existence* of a global $2$-form potential with $J = d\Theta$. The bridge is that the field equation $d\star F + J = 0$ furnishes one such potential explicitly, $\Theta = -\star F$; the general statement is that the obstruction to writing a conserved current as $d$ of something is measured by a cohomology class, and it vanishes on topologically trivial spacetimes.

---

# Unlocked by This

> [!tip] Total charge as a homological invariant *(from Algebraic Topology)*
> Once $J$ is known to be closed, its integral over a closed oriented spatial hypersurface $S$ depends only on the de Rham class $[J|_S]$ and the fundamental class $[S]$, by [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance]] and Stokes. The total charge is the pairing $\langle[J], [S]\rangle$, an integer-scaled topological quantity when charge is quantised — the mechanism behind Dirac's monopole quantisation. See [[Def - de Rham Cohomology]].

> [!tip] The integrated conservation law as a drill *(within Gauge Theory VII)*
> The orientation computation of Part (ii) is isolated as a practice problem in [[Ex - Charge Conservation on a Spacetime Cylinder]], where the three faces of $[t_0, t_1]\times B$ and their induced orientations are re-derived from scratch, and the classic error — giving the initial-time cap the standard orientation instead of the reversed one — is flagged as the illegal-but-tempting route.
