---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Lorentz Factor and Relative Velocity"
  - "Thm - Reciprocity of Relative Velocity"
  - "Def - Einstein-Poincaré Simultaneity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature, $u\cdot u = +1$ for a four-velocity. Two observers $\mathcal{O}, \mathcal{O}'$ have four-velocities $u, u'$, [[Def - Observer and Local Rest Space|local rest spaces]] $E_u, E_{u'}$, and [[Def - Lorentz Factor and Relative Velocity|Lorentz factor]] $\Gamma_0 = u\cdot u' \ge 1$. The velocity of $\mathcal{O}'$ relative to $\mathcal{O}$ is $U \in E_u$, with unit vector $e = U/\lVert U\rVert_g \in E_u$ and magnitude $U = \lVert U\rVert_g$; the corresponding unit vector in $E_{u'}$ is $e' = U'/\lVert U'\rVert_g \in E_{u'}$. A ruler carried by $\mathcal{O}'$ along the direction of motion has **proper length** $\ell'$ (its length measured in $\mathcal{O}'$'s rest space) and **measured length** $\ell$ (its length measured in $\mathcal{O}$'s rest space). The norm of a spacelike vector is $\lVert X\rVert_g = \sqrt{-X\cdot X}$. Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

---

# Statement

> **Length contraction (FitzGerald–Lorentz).** Let a ruler be at rest in observer $\mathcal{O}'$, aligned along the direction of the relative motion of $\mathcal{O}'$ with respect to $\mathcal{O}$, with proper length $\ell'$ (its length in $E_{u'}$). The length $\ell$ measured by $\mathcal{O}$ — the norm of the displacement between the two ends, taken between events that are *simultaneous in $\mathcal{O}$'s rest space* — satisfies
> $$\ell = \frac{\ell'}{\Gamma_0}, \qquad \Gamma_0 = (1 - U^2)^{-1/2} \ge 1,$$
> so $\ell \le \ell'$: the moving ruler is shorter. The contraction occurs only along the direction of motion; a ruler aligned transverse to the motion has $\ell = \ell'$, because $E_u$ and $E_{u'}$ coincide in directions orthogonal to $U$.

---

# Motivation

Time dilation answered "how do two observers compare the *durations* they measure?"; length contraction is the spatial companion: "how do two observers compare the *lengths* they measure?" The two are not independent — both flow from the same tilt between the observers' rest spaces — but length contraction has a subtlety that time dilation lacks, and stating it carefully is the whole point of giving it a frame-free treatment here rather than reciting the textbook one-liner.

The subtlety is what "the length of a moving object" even *means*. For a stationary ruler, length is unambiguous: mark both ends, measure the distance. For a *moving* ruler, you must locate both ends *at the same time* — otherwise the ruler has moved between the two markings and you measure a meaningless mixture. But "at the same time" is observer-dependent (the relativity of simultaneity, [[Def - Einstein-Poincaré Simultaneity]]), so the length of a moving ruler depends on *whose* simultaneity you use to locate its ends. This is not a measurement error to be corrected; it is the definition of the quantity, and it is exactly why two observers disagree.

Once the definition is pinned down — length = norm of the end-to-end displacement, taken between events simultaneous *in the measuring observer's rest space* — the contraction $\ell = \ell'/\Gamma_0$ follows from pure geometry, and the derivation makes transparent that **contraction is the relativity of simultaneity in disguise**. The two ends of the ruler trace two parallel worldlines; $\mathcal{O}'$ slices them with $E_{u'}$ (getting $\ell'$), $\mathcal{O}$ slices them with the tilted $E_u$ (getting the shorter $\ell$); the shortening is entirely the geometric consequence of slicing the same pair of worldlines at a different angle. There is no force, no mechanical compression, no "real" squeezing — just two different spatial cross-sections of one spacetime object. Recognising this dissolves every length-contraction "paradox" (the ladder in the barn, the pole-vaulter): the two observers slice differently, so they disagree, and reciprocity ([[Thm - Reciprocity of Relative Velocity]]) guarantees they disagree *symmetrically*.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a ruler at rest in $\mathcal{O}'$, measured by $\mathcal{O}$, aligned with the motion". Its disguises:

The first disguised source is **"an extended object with a known rest-frame size, moving relative to the lab"**. Anything with a proper size — a rod, the diameter of a spacecraft, the spacing of a crystal lattice, the length of a particle bunch — supplies the proper length $\ell'$, and the lab measurement is $\ell'/\Gamma_0$. The bridge is that "rest-frame size" is exactly the proper length. *Example problem:* a relativistic muon's lifetime lets it traverse the atmosphere; equivalently, in the muon's frame, the atmosphere's thickness is contracted by $\Gamma_0$ so the muon crosses a much thinner layer — the symmetric description of the muon-survival puzzle.

The second disguised source is **"a distance in space, traversed by a moving observer"**. The distance between two points fixed in $\mathcal{O}$ (a track length, an interstellar distance) is a proper length in $\mathcal{O}$'s frame; a traveller $\mathcal{O}'$ measures it contracted. The bridge is reciprocity: the track is "at rest" in $\mathcal{O}$, so to the moving traveller it is the moving object. *Example problem:* a starship travelling at $\Gamma_0 = 10$ measures a $10$-light-year journey as only $1$ light-year, which is how it can be crossed in a short proper time.

The third disguised source is **"a transverse-versus-longitudinal comparison"**. Whenever a problem involves an object with both longitudinal and transverse extent (a moving square, a moving circle), the theorem applies *only* to the longitudinal dimension; the transverse one is unchanged. The bridge is that $E_u$ and $E_{u'}$ share their transverse directions. *Example problem:* a square moving along one edge becomes a rectangle (contracted in the motion direction, unchanged transverse); a moving sphere's *position* (not image!) is an oblate ellipsoid.

**Targets (Output Amplification)**

The conclusion is "$\ell = \ell'/\Gamma_0$, longitudinal only".

Combine the conclusion with **reciprocity**. Since $\Gamma_0$ is symmetric ([[Thm - Reciprocity of Relative Velocity]]), each observer measures the *other's* rulers contracted by the same factor. The further result is the resolution of the ladder-and-barn paradox: the barn sees the ladder fit (ladder contracted), the ladder sees the barn too short (barn contracted), and both are right because "the front and back doors close simultaneously" is frame-dependent. The combination is nonobvious because mutual contraction sounds contradictory until simultaneity is brought in.

Combine the conclusion with **the constancy of transverse lengths**. Because only the longitudinal dimension contracts, the *shape* of a moving object's position-slice distorts anisotropically: a sphere's instantaneous position is an ellipsoid flattened along the motion. The further result, sharpened in [[Def - Apparent Rotation and Images of Moving Objects]], is the crucial caveat that this is the *position*, not the *image* — the photographed sphere is a perfect circle. The combination is useful as the precise input to the image-versus-position discussion: contraction is what the rest-space slice does, and the image undoes it.

Combine the conclusion with **the invariant interval**. The proper length $\ell'$ is the invariant spacelike interval between the two ends taken in $\mathcal{O}'$'s simultaneity, and the contraction can be read as the statement that $\mathcal{O}$'s simultaneity slices a *spacelike* interval at an angle, recovering a shorter spatial projection. The further result is that the contraction factor is geometric (a projection cosine in hyperbolic geometry), not dynamical. The combination is useful for deriving the factor without coordinates, purely from the geometry of slicing.

---

# Why Is It True

The whole effect is one geometric fact: the two ends of the ruler are two parallel worldlines in spacetime, and the two observers cut this pair of worldlines with two *differently tilted* spatial slices. The length each measures is the spatial distance between where their slice meets the two worldlines, and a more-tilted slice meets the parallel worldlines at a shorter spatial separation.

**The one-line mechanism: length contraction is the relativity of simultaneity — $\mathcal{O}$ and $\mathcal{O}'$ locate the two ends of the ruler at events that they each call "simultaneous", but those are different pairs of events, and the moving observer's pair is spatially closer.**

To see it without algebra, draw the ruler's worldsheet: a strip in spacetime bounded by the worldlines of its two ends, both parallel to $u'$ (the ruler is at rest in $\mathcal{O}'$, so its ends move along $\mathcal{O}'$'s time direction). The proper length $\ell'$ is the width of this strip measured *across* it, orthogonally to $u'$ — that is, sliced by $E_{u'}$. Now $\mathcal{O}$ measures the strip's width by slicing with $E_u$, which is tilted relative to $E_{u'}$ by the hyperbolic angle (rapidity) between $u$ and $u'$. Here is the crucial sign, and where the relativistic geometry departs from Euclidean intuition: in *Euclidean* geometry, slicing a strip at an angle gives a *longer* chord (the hypotenuse is longer). In *Minkowski* geometry, because the metric is indefinite and the tilt is a hyperbolic rotation, slicing the strip with the tilted spatial plane gives a *shorter* spatial length — the same sign flip that makes the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] hold. The factor is exactly $1/\Gamma_0 = 1/\cosh\varphi$, the hyperbolic projection.

Why does *only* the longitudinal direction contract? Because the tilt between $E_u$ and $E_{u'}$ is entirely within the plane spanned by time and the direction of motion. Any direction orthogonal to the motion lies in *both* rest spaces — it is fixed by the boost — so a ruler pointing transverse is sliced identically by both observers and has the same length for each. The contraction is a purely longitudinal phenomenon because the boost is a rotation in the time–motion plane and leaves the transverse plane alone.

The deepest way to phrase it: contraction is not something that *happens to* the ruler, it is something that differs between two *descriptions* of the same unchanging spacetime strip. The strip is fixed; the slicing is a choice; and two observers make different choices because their notions of "now" differ.

---

# What Makes This Hard

The conceptual trap is treating contraction as a physical compression of the ruler rather than as a difference in how two observers slice the same spacetime worldsheet — once seen as a slicing, the "paradoxes" evaporate, but the slicing picture is exactly what beginners lack. The non-obvious technical point is that the length of a *moving* object is only defined once you specify *whose* simultaneity locates its ends, and forgetting this is the source of almost every error: people measure the two ends at different times in the measuring frame and get nonsense. The most common concrete mistake is the sign — expecting a tilted slice to give a *longer* length (the Euclidean intuition) instead of a shorter one, because the Minkowski tilt is hyperbolic, not circular.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Set up the ruler as a strip bounded by two worldlines parallel to $u'$, separated by the proper-length displacement $\ell' e'$ in $E_{u'}$. Find the displacement between the two ends as measured by $\mathcal{O}$, i.e. the vector lying in $E_u$ connecting one worldline to the other; its norm is $\ell$. The computation is: express the spatial unit vector $e'$ of $\mathcal{O}'$ in terms of $\mathcal{O}$'s vectors, and project onto $E_u$.

**Subgoal decomposition:**

1. **Express $\mathcal{O}'$'s spatial direction $e'$ in $\mathcal{O}$'s terms.** Show $e' = \Gamma_0(e + U\,u)$ (with $c=1$), the boost of the unit vector.
   - *Hint:* $e'$ is the unit vector along $U'$; use $U' = -\Gamma_0^{-1}\perp_{u'}U$ from reciprocity, or boost the rest-frame unit vector. The result is the spacelike partner of the time-boost.
   - *Why needed:* It relates the ruler's proper-length direction to $\mathcal{O}$'s frame.

2. **Set up the two end-events with $\mathcal{O}$-simultaneity.** The end-to-end displacement measured by $\mathcal{O}$ is the vector $\ell e \in E_u$; the displacement carrying the ruler's proper length is $\ell' e' \in E_{u'}$. Relate them by adding a multiple of $u'$ (sliding along the ruler's worldlines to reach $\mathcal{O}$-simultaneous events).
   - *Hint:* Write $\overrightarrow{OB'} = \ell' e'$ (proper, in $E_{u'}$) and $\overrightarrow{OB} = \ell e$ ($\mathcal{O}$-measured, in $E_u$), differing by a vector along the ruler's worldline direction $u'$: $\ell' e' = \ell e + \alpha u'$ for some scalar $\alpha$.
   - *Why needed:* This encodes "the two ends are located at $\mathcal{O}$-simultaneous events", the crux of the definition.

3. **Match coefficients of independent vectors.** Substitute $e' = \Gamma_0(e + Uu)$ and $u' = \Gamma_0(u + Ue)$ and equate the coefficients of $e$ and $u$ (which are independent), solving for $\ell$.
   - *Hint:* The coefficient of $e$ gives $\Gamma_0\ell' = \ell + \alpha\Gamma_0 U$... arrange so that comparing the $e$-coefficients on both sides yields $\ell = \ell'/\Gamma_0$.
   - *Why needed:* It extracts the contraction factor.

---

# Lemma Decomposition

> [!note]- Lemma 1: The boost of the spatial unit vector
> **Statement:** The unit vector $e' \in E_{u'}$ along the relative motion is $e' = \Gamma_0(e + U\,u)$, where $e \in E_u$ is the unit vector along $U$ and $U = \lVert U\rVert_g$.
>
> **Hint:** $e'$ is the spacelike companion of the time-boost $u' = \Gamma_0(u + Ue)$.
>
> **Why needed:** It is the spatial half of the boost between the two rest frames, needed to compare the ruler's two descriptions.
>
> > [!note]- Full proof
> > Recall $u' = \Gamma_0(u + U) = \Gamma_0(u + Ue)$ (writing $U = Ue$). The vector $e' = U'/\lVert U'\rVert_g$ must satisfy three conditions: it lies in $E_{u'}$ (so $u'\cdot e' = 0$), it is a unit spacelike vector ($e'\cdot e' = -1$), and it lies in the plane of $u, e$ (the boost plane). Try $e' = \Gamma_0(e + Uu)$. Check orthogonality to $u'$: $u'\cdot e' = \Gamma_0^2(u + Ue)\cdot(e + Uu) = \Gamma_0^2(u\cdot e + U\,u\cdot u + U\,e\cdot e + U^2 e\cdot u)$. With $u\cdot e = 0$, $u\cdot u = 1$, $e\cdot e = -1$, $e\cdot u = 0$: $= \Gamma_0^2(0 + U - U + 0) = 0$. Check the norm: $e'\cdot e' = \Gamma_0^2(e\cdot e + 2U\,e\cdot u + U^2 u\cdot u) = \Gamma_0^2(-1 + 0 + U^2) = -\Gamma_0^2(1 - U^2) = -1$, using $\Gamma_0^2(1-U^2) = 1$. So $e' = \Gamma_0(e + Uu)$ is the required unit vector (the sign is fixed by requiring $e'$ to point in the same spatial sense as $e$). $\blacksquare$

> [!note]- Lemma 2: Two ends located simultaneously in $\mathcal{O}$'s frame
> **Statement:** If the ruler's proper end-to-end displacement is $\ell'e' \in E_{u'}$, the displacement between its ends located at $\mathcal{O}$-simultaneous events is $\ell e \in E_u$, with $\ell' e' = \ell e + \alpha u'$ for some scalar $\alpha$.
>
> **Hint:** Both end-events of $\mathcal{O}$'s measurement lie on the ruler's worldlines, which run parallel to $u'$; sliding from $\mathcal{O}'$'s simultaneous events to $\mathcal{O}$'s simultaneous events moves along $u'$.
>
> **Why needed:** It is the precise geometric encoding of "measure both ends at the same $\mathcal{O}$-time".
>
> > [!note]- Full proof
> > Place the crossing event $O$ at one end of the ruler. The far end traces a worldline parallel to $u'$ (the ruler is rigid and at rest in $\mathcal{O}'$). In $\mathcal{O}'$'s simultaneity, the far end at the moment of crossing is the event $B'$ with $\overrightarrow{OB'} = \ell' e'$ (proper length along $e'$). In $\mathcal{O}$'s simultaneity, the far end is located at the event $B$ on the *same* far worldline that is $\mathcal{O}$-simultaneous with $O$, so $\overrightarrow{OB} \in E_u$, i.e. $\overrightarrow{OB} = \ell e$ for some $\ell$ (the $\mathcal{O}$-measured length). Since $B$ and $B'$ both lie on the far worldline, they differ by a displacement along that worldline's direction $u'$: $\overrightarrow{OB'} = \overrightarrow{OB} + \overrightarrow{BB'}$ with $\overrightarrow{BB'} = \alpha u'$. Hence $\ell' e' = \ell e + \alpha u'$. $\blacksquare$

> [!note]- Lemma 3: Coefficient matching gives the factor
> **Statement:** $\ell = \ell'/\Gamma_0$.
>
> **Hint:** Substitute the boost expressions for $e'$ and $u'$ into $\ell' e' = \ell e + \alpha u'$ and compare coefficients of the independent vectors $e$ and $u$.
>
> **Why needed:** It is the conclusion.
>
> > [!note]- Full proof
> > Substitute $e' = \Gamma_0(e + Uu)$ (Lemma 1) and $u' = \Gamma_0(u + Ue)$ into $\ell' e' = \ell e + \alpha u'$:
> > $$\ell'\Gamma_0(e + Uu) = \ell e + \alpha\Gamma_0(u + Ue).$$
> > The vectors $e$ and $u$ are linearly independent, so equate coefficients.
> > Coefficient of $e$: $\ell'\Gamma_0 = \ell + \alpha\Gamma_0 U$.
> > Coefficient of $u$: $\ell'\Gamma_0 U = \alpha\Gamma_0$, hence $\alpha = \ell' U$.
> > Substitute $\alpha = \ell'U$ into the $e$-equation: $\ell'\Gamma_0 = \ell + \ell'U\cdot\Gamma_0 U = \ell + \ell'\Gamma_0 U^2$. Therefore $\ell = \ell'\Gamma_0(1 - U^2) = \ell'\Gamma_0/\Gamma_0^2 = \ell'/\Gamma_0$, using $\Gamma_0^2(1-U^2) = 1$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Place the near end of the ruler at the crossing event $O$ of the two worldlines. The ruler is at rest in $\mathcal{O}'$, so both its ends trace worldlines parallel to $u'$, separated by the proper-length displacement $\ell' e'$ where $e' \in E_{u'}$ is the unit vector along the motion.
>
> *Step 1 (boost of the spatial direction).* By Lemma 1, $e' = \Gamma_0(e + Uu)$, where $e \in E_u$ is the unit vector along $U$, $U = \lVert U\rVert_g$, and $u' = \Gamma_0(u + Ue)$.
>
> *Step 2 (the measurement condition).* $\mathcal{O}$ measures the length by locating both ends at $\mathcal{O}$-simultaneous events; by Lemma 2 the far end is then at $B$ with $\overrightarrow{OB} = \ell e \in E_u$, and $B$ differs from the proper-simultaneous far-end event $B'$ (with $\overrightarrow{OB'} = \ell' e'$) by a displacement $\alpha u'$ along the worldline: $\ell' e' = \ell e + \alpha u'$.
>
> *Step 3 (solve).* Substituting the boost expressions and matching the independent coefficients of $e$ and $u$ (Lemma 3): the $u$-coefficient gives $\alpha = \ell'U$, and the $e$-coefficient then gives $\ell = \ell'\Gamma_0(1 - U^2) = \ell'/\Gamma_0$.
>
> *Transverse case.* If the ruler is aligned along a direction $f$ orthogonal to the motion ($f\cdot e = f\cdot u = f\cdot u' = 0$), then $f$ lies in both $E_u$ and $E_{u'}$, the boost fixes it, and the measurement gives $\ell = \ell'$: no contraction. Since $\Gamma_0 \ge 1$, the longitudinal result $\ell = \ell'/\Gamma_0 \le \ell'$ shows the moving ruler is shortened along the motion only. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Crystallography and channeling of relativistic ions.** A relativistic heavy ion passing through a crystal "sees" the lattice planes contracted along its motion by $\Gamma_0$, which changes the channeling geometry and the effective interplanar spacing. The application is nonobvious because the contraction is usually taught for macroscopic rods, but it has measurable consequences for the trajectories of fast ions in ordered matter.

**Relativistic heavy-ion collisions (pancaking).** At collider energies, a gold nucleus with $\Gamma_0 \sim 100$ is contracted into a thin "pancake" along the beam, a factor of $100$ flatter than its rest-frame sphere; the geometry of the overlap region in a heavy-ion collision is computed from these contracted shapes. The application is out-of-distribution because it treats an entire nucleus as the contracting object and the contraction controls the initial conditions of the quark–gluon plasma.

**Magnetism as relativistic electrostatics.** The magnetic force between a current and a moving charge can be derived purely from length contraction: in the charge's rest frame the moving lattice ions and conduction electrons are contracted by *different* factors (they move at different speeds), producing a net charge density and hence an electric force, which is what the lab calls the magnetic force. The application connects length contraction to the unification of electricity and magnetism, developed in [[Special Relativity XXI — The Electromagnetic Field]].

---

# Bridges

- **[[Thm - Reciprocity of Relative Velocity]]** — the contraction factor $\Gamma_0$ is symmetric by reciprocity, which is what makes *mutual* contraction (each observer shortens the other's rulers) consistent rather than paradoxical. The ladder-and-barn resolution is reciprocity plus the relativity of simultaneity.

- **[[Def - Einstein-Poincaré Simultaneity]]** — length contraction is the relativity of simultaneity made quantitative: the measured length depends on whose simultaneity slices the ruler's ends, and the contraction factor is precisely the geometric effect of slicing the ruler's worldsheet at the tilted angle. Remove the simultaneity disagreement and the contraction vanishes.

- **[[Thm - The Reversed Triangle Inequality]]** — the *sign* of the effect (shorter, not longer, under a tilted slice) is the same indefinite-metric phenomenon that reverses the triangle inequality. In Euclidean geometry a tilted chord is longer; in Minkowski geometry the hyperbolic tilt gives a shorter spatial projection, factor $1/\cosh\varphi$.

- **[[Def - Apparent Rotation and Images of Moving Objects]]** — contraction is a statement about the *position* (rest-space slice) of an object, *not* its *image* (past-light-cone slice). This bridge is the crucial caveat of §8.3: the photographed shape of a moving object is governed by the past light cone, and the naive "it looks contracted" is wrong; a sphere's contracted *position*-ellipsoid still photographs as a circle.

---

# Unlocked by This

> [!tip] The Pancaked Nucleus and the Quark-Gluon Plasma *(from High-Energy Nuclear Physics)*
> At ultrarelativistic energies a nucleus is Lorentz-contracted into a flat disk, and two such disks colliding deposit their energy in a thin sheet that thermalises into a **quark–gluon plasma**. The initial geometry — the overlap area, the energy density — is computed directly from the contracted shapes, so length contraction sets the stage for the hottest matter ever produced. The energy-momentum content of such a system is the subject of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!tip] The Field of a Fast Charge as a Contracted Coulomb Field *(from Electromagnetism)*
> The electric field of a uniformly moving charge is the contracted Coulomb field: the field lines, isotropic in the rest frame, are squashed toward the transverse plane by exactly the FitzGerald factor, so a fast charge's field is concentrated in a pancake perpendicular to its motion. This is the field-theoretic shadow of length contraction and the starting point for the field of a charge in uniform translation in [[Special Relativity XXI — The Electromagnetic Field]].
