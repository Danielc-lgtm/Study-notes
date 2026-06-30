---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Apparent Rotation and Images of Moving Objects"
  - "Thm - Aberration of Light"
  - "Thm - Length Contraction (General)"
tags: [physics, special-relativity]
---

# Problem Statement

Prove the **Penrose–Terrell theorem**: the image of a relativistically moving sphere is a perfect circular disk, with no visible flattening, for an observer in any state of motion. Working with $c = 1$:

1. State precisely what is to be shown, distinguishing the *image* (past-light-cone slice) from the *position* (rest-space slice). Explain why the naive expectation — that the image is FitzGerald-contracted into an ellipse — is wrong.
2. Set up the celestial sphere $\mathscr{S}$ of the observer and the **stereographic projection** from the pole $P$ opposite to the direction of motion onto the tangent plane $\Pi$ at the antipode $Q$. Show that a light ray arriving at angle $\theta$ to the direction $PQ$ maps to a point at radius $\rho = 2\tan(\theta/2)$ in $\Pi$.
3. Show that the aberration formula $\tan(\theta'/2) = \sqrt{(1-U)/(1+U)}\tan(\theta/2)$ becomes, on $\Pi$, a *dilation by the constant factor* $k = \sqrt{(1-U)/(1+U)}$, hence a conformal map.
4. Use the fact that stereographic projection maps circles on $\mathscr{S}$ to circles on $\Pi$ (and conversely), together with the conformal dilation, to conclude that the circular outline of a sphere remains a circle for every observer — so a moving sphere photographs as a disk.

**Recall:**

This exercise proves the headline result of §8.3.

![[Def - Apparent Rotation and Images of Moving Objects#The Definition]]

The [[Thm - Aberration of Light|aberration]] law in half-angle form is $\tan(\theta'/2) = \sqrt{(1-U)/(1+U)}\tan(\theta/2)$. **Stereographic projection** from a pole $P$ of a sphere onto the tangent plane at the antipode $Q$ is the map sending a point $A \ne P$ to the intersection of the line $PA$ with the plane; it is a classical fact that it is *conformal* (angle-preserving) and *circle-preserving* (circles not through $P$ map to circles, circles through $P$ to lines).

---

# Convergent Strategy

**Problem class.** A *predict-an-image* problem of the deepest kind: show that the photographed shape of a moving object is governed by the conformal action on the celestial sphere, overturning the naive contraction expectation. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] for appearance problems is to use the past light cone and the aberration map, never FitzGerald contraction.

**Assumption pattern.** A spherical object, so its outline is a *circle* on the observer's sky. The decisive structural facts are: (i) aberration acts on the sky, (ii) stereographic projection turns the sky into a plane on which aberration is a dilation, (iii) dilations and stereographic projections both preserve circles. The shape of the *outline*, not the body, is what matters.

**Theorem routing.** The [[Thm - Aberration of Light|aberration]] formula in half-angle form routes, via stereographic projection ($\rho = 2\tan(\theta/2)$), to a real dilation $\rho \mapsto k\rho$. The circle-preservation of stereographic projection routes "circular outline on the sky" to "circle on the plane", and the dilation keeps it a circle, which maps back to a circle on the new observer's sky.

**Key decision point.** The crux is realising that the *shape* of the image is determined by the *outline* of the sphere (a circle on the sky), and that the Lorentz transformation acts on the sky *conformally* — so circles map to circles. The naive approach computes the contracted *position* ellipsoid and projects it, getting an ellipse; the correct approach recognises that the image is the conformal map of the *outline*, and conformal maps preserve circles. The decision to work with the outline on the celestial sphere, via stereographic projection, rather than with the body in space, is what makes the proof clean and reveals *why* the result holds (conformality), not just *that* it holds.

---

# Legal Operations Used

1. **Build an image from the past light cone, not the rest space** (operation 7 from the topic page). The image is the set of directions on the sky from which the sphere's outline is seen, a past-light-cone construction; FitzGerald contraction (a rest-space statement) is explicitly *not* used.

2. **Convert between angle and stereographic coordinate** (operation 8 from the topic page). Mapping the sky direction $\theta$ to the plane radius $\rho = 2\tan(\theta/2)$ turns aberration into a dilation and exposes its conformality.

3. **Use the conformality (circle-preservation) of the maps** (operation 8 from the topic page), combining the circle-preservation of stereographic projection with that of the dilation to conclude circles map to circles.

---

# Hints

> [!note]- Hint 1
> The image is the slice of the sphere's worldtube by the observer's *past light cone* — the directions from which photons arriving now were emitted. This is *not* the rest-space slice (the position), which is a contracted ellipsoid. To find the image's shape, find the shape of the sphere's *outline* on the observer's celestial sphere, and how it transforms.

> [!note]- Hint 2
> Set up stereographic projection from the pole $P$ (opposite the motion) onto the tangent plane $\Pi$ at the antipode $Q$. For a ray at angle $\theta$ to $PQ$, the projected point $B$ lies on line $PA$; the triangle $POA$ is isosceles, so the angle $OPA = \theta/2$, and in the right triangle $PQB$ with $PQ = 2$ (diameter), $QB = PQ\tan(\theta/2) = 2\tan(\theta/2)$. So $\rho = 2\tan(\theta/2)$.

> [!note]- Hint 3
> The aberration formula $\tan(\theta'/2) = k\tan(\theta/2)$ with $k = \sqrt{(1-U)/(1+U)}$, translated via $\rho = 2\tan(\theta/2)$ and $\rho' = 2\tan(\theta'/2)$, reads $\rho' = k\rho$ — a dilation of the plane $\Pi$ by the *constant* factor $k$ (and the azimuth $\varphi$ is unchanged). A dilation about the pole is a conformal map.

> [!note]- Hint 4
> Stereographic projection sends circles on $\mathscr{S}$ (not through $P$) to circles on $\Pi$. The sphere's outline is a circle on $\mathscr{S}_{\mathcal{O}}$; project it to a circle on $\Pi$; dilate by $k$ (still a circle); project back via the inverse stereographic projection of $\mathcal{O}'$ to a circle on $\mathscr{S}_{\mathcal{O}'}$. A circular outline on the sky is the image of a disk. Only the radius (angular size) changes.

---

# Solution

The Penrose–Terrell theorem is proved by recognising aberration as a conformal (circle-preserving) map of the celestial sphere. Step 1 sets up image vs. position; Step 2 builds stereographic projection; Step 3 shows aberration is a dilation on the projected plane; Step 4 chains the circle-preservations to conclude the sphere's outline stays circular. The non-obvious move is to work with the *outline on the sky* via stereographic projection, exposing the conformality that makes circles map to circles.

**Step 1: Image versus position, and why the naive answer is wrong.**

> [!note]- Derivation
> We must show: the photographed outline of a moving sphere is a perfect circle for every observer. The *image* of the sphere is the set of directions on the observer's celestial sphere $\mathscr{S}$ from which photons, arriving simultaneously at the observer, were emitted — the slice of the sphere's worldtube by the observer's [[Def - Apparent Rotation and Images of Moving Objects|past light cone]]. This is distinct from the *position*, the slice by the rest space, which for a moving sphere is an oblate ellipsoid contracted by $\Gamma$ along the motion ([[Thm - Length Contraction (General)|length contraction]]).
>
> The naive expectation — "the sphere is contracted, so its image is a flattened ellipse" — conflates image with position. The contraction is real but it describes where the sphere *is*, not how it *looks*; the photograph is built from the past light cone, and (as we will show) the past-light-cone outline is a circle, not an ellipse. The contraction is exactly compensated by the differing light-travel times from different parts of the sphere.

**Step 2: Stereographic projection and $\rho = 2\tan(\theta/2)$.**

> [!note]- Derivation
> Take the observer's celestial sphere $\mathscr{S}$ of unit radius, centred at the observer $O$. Let $Q \in \mathscr{S}$ be the point in the direction of motion of the other observer, and $P$ the antipodal point. Let $\Pi$ be the plane tangent to $\mathscr{S}$ at $Q$. **Stereographic projection** from $P$ maps each $A \in \mathscr{S}\setminus\{P\}$ to the intersection $B$ of the line $PA$ with $\Pi$.
>
> For a ray arriving at angle $\theta$ to the axis $PQ$ (so $A$ is at colatitude $\theta$ from $Q$): the central angle $\angle QOA = \theta$. The triangle $POA$ has $OP = OA = 1$ (radii), so it is isosceles, and its apex angle at $O$ is $\angle POA = \pi - \theta$; hence the base angles are $\angle OPA = \angle OAP = \theta/2$. Now consider the right triangle $PQB$: $PQ$ is a diameter of length $2$, the angle at $P$ is $\angle QPB = \angle OPA = \theta/2$, and the angle at $Q$ is a right angle (since $\Pi \perp OQ$). Therefore
> $$\rho := QB = PQ\,\tan(\angle QPB) = 2\tan\frac{\theta}{2}.$$
> So the sky-direction at colatitude $\theta$ maps to the plane-point at radius $\rho = 2\tan(\theta/2)$ (and azimuth $\varphi$, unchanged).

**Step 3: Aberration is a dilation on $\Pi$.**

> [!note]- Derivation
> The [[Thm - Aberration of Light|aberration]] law in half-angle form relates the colatitudes $\theta$ (for $\mathcal{O}$) and $\theta'$ (for $\mathcal{O}'$) of the same ray:
> $$\tan\frac{\theta'}{2} = \sqrt{\frac{1 - U}{1 + U}}\;\tan\frac{\theta}{2}.$$
> Translate to stereographic radii via $\rho = 2\tan(\theta/2)$ and $\rho' = 2\tan(\theta'/2)$:
> $$\rho' = 2\tan\frac{\theta'}{2} = 2\,k\,\tan\frac{\theta}{2} = k\,\rho, \qquad k = \sqrt{\frac{1-U}{1+U}}.$$
> The azimuth is unchanged ($\varphi' = \varphi$, since the boost is axially symmetric about $PQ$). So on the plane $\Pi$, the change of observer acts as
> $$(\rho, \varphi) \mapsto (k\rho, \varphi),$$
> a **dilation by the constant factor $k$** centred at $Q$. A dilation is a conformal (angle-preserving) map, and crucially it maps circles to circles.

**Step 4: Circles to circles — the sphere stays a sphere.**

> [!note]- Derivation
> The sphere, seen by $\mathcal{O}$, has a circular *outline* on $\mathscr{S}_{\mathcal{O}}$: the set of tangent rays forms a circle (a "small circle") on the celestial sphere, not passing through $P$ (assuming the observer is outside the sphere and not looking exactly backward). Now chain three circle-preserving maps:
> 1. **Stereographic projection** $\mathscr{S}_{\mathcal{O}} \to \Pi$ sends this outline-circle to a *circle* $C$ on $\Pi$ (classical property: circles not through the pole $P$ map to circles).
> 2. **Aberration** acts on $\Pi$ as the dilation $\rho \mapsto k\rho$ (Step 3), sending the circle $C$ to another *circle* $C' = kC$ (a dilation of a circle is a circle).
> 3. **Inverse stereographic projection** $\Pi \to \mathscr{S}_{\mathcal{O}'}$ sends $C'$ to a *circle* on $\mathcal{O}'$'s celestial sphere (the inverse map is also circle-preserving).
>
> Therefore the outline of the sphere, seen by $\mathcal{O}'$, is again a **circle**. A circular outline on the sky is exactly the image of a *disk*. Hence the moving sphere photographs as a perfect circular disk for $\mathcal{O}'$, with no flattening — only the radius (angular size) changes, by the dilation factor. This is the **Penrose–Terrell theorem**. The FitzGerald contraction of the *position* (the ellipsoid) is entirely invisible in the *image*; the differing light-travel times from the near and far parts of the sphere conspire with the contraction to keep the outline circular.

> [!note]- Complete formal solution
> The image of the sphere is the slice of its worldtube by the observer's past light cone — equivalently, the sphere's outline on the celestial sphere $\mathscr{S}$, a circle. Set up stereographic projection from the pole $P$ (opposite the motion) onto the tangent plane $\Pi$ at the antipode $Q$: a ray at colatitude $\theta$ maps to radius $\rho = 2\tan(\theta/2)$ (from the isosceles triangle $POA$ giving $\angle QPB = \theta/2$ and the right triangle $PQB$ with $PQ = 2$). The aberration law $\tan(\theta'/2) = k\tan(\theta/2)$, $k = \sqrt{(1-U)/(1+U)}$, becomes $\rho' = k\rho$ on $\Pi$ — a dilation, hence conformal. Chaining the circle-preserving maps (stereographic projection, dilation, inverse stereographic projection), the sphere's circular outline maps to a circle on every observer's sky. Thus a moving sphere photographs as a perfect disk, only its angular size changing; the position-ellipsoid's FitzGerald contraction is invisible in the image. $\blacksquare$

---

# Key Takeaways

**Aberration is conformal, and conformality — not contraction — governs the appearance of moving objects.** The deepest content of the Penrose–Terrell theorem is that the Lorentz group acts on the celestial sphere by *conformal* (angle- and circle-preserving) maps, realised concretely as the dilation $\rho \mapsto k\rho$ on the stereographic plane. Conformal maps preserve circles, so a circular outline stays circular and a sphere stays a sphere. This is the trigger to recognise in any "how does a moving object look" problem: the relevant transformation of the sky is conformal, so any feature defined by *angles and circles* (an outline, a circular boundary, the shape of a stellar disk) is preserved up to size, while features defined by *metric distances* (the actual contracted positions) are not what is seen. The reusable principle: for appearance, think conformal geometry of the sky, not metric geometry of the body. This single fact organises all of §8.3 and is the observational root of the conformal viewpoint that underlies [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map|the spinor map]] and twistor theory.

**Work with the outline on the celestial sphere, not the body in space — the stereographic-projection method turns a hard image problem into circle-preservation.** The proof's power comes from refusing to track the contracted body in three-space (which would give an ellipsoid and a hard projection integral) and instead tracking the *outline as a circle on the sky*, then using that aberration is a dilation on the stereographically projected plane. This reduces the entire theorem to the elementary facts "stereographic projection preserves circles" and "dilations preserve circles". The transferable method: when an image or appearance must be computed, project the problem onto the observer's celestial sphere, identify the relevant feature as a curve on the sky, and use the conformal/Möbius action there — this is almost always far cleaner than working with the spatial geometry of the object. The same stereographic technique computes the aberrated appearance of constellations, the distortion of the CMB sky, and the lensed image of a source near a black hole.

**The image hides the contraction: differing light-travel times exactly compensate the FitzGerald squashing.** The most counterintuitive aspect — that the sphere's *position* is a contracted ellipsoid yet its *image* is a perfect circle — is resolved by the fact that the photons forming the image were emitted at *different times* from different parts of the sphere, and this retardation precisely cancels the contraction for the outline. This illustrates a general and important caution: relativistic *appearance* and relativistic *configuration* are different things, related by the past-light-cone construction, and effects that are real in the configuration (contraction) can be completely invisible in the appearance. The diagnostic to carry forward: never report what a fast object "looks like" by applying length contraction; always go through the image (past-light-cone) construction, because the light-travel-time differences can — as here — exactly undo the contraction, or — as for the [[Ex - Why a moving ruler is photographed elongated or rotated|moving cube]] — convert it into an apparent rotation. The position is contracted; the image is something else, and only the image is seen.
