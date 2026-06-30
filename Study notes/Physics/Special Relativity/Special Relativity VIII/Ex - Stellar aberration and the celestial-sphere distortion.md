---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Aberration of Light"
  - "Def - Apparent Rotation and Images of Moving Objects"
tags: [physics, special-relativity]
---

# Problem Statement

Stellar aberration is the apparent yearly motion of every star caused by the Earth's orbital velocity. Working with $c = 1$ except where restoring $c$ aids recognition:

1. The Earth orbits the Sun at speed $U = 30\,\mathrm{km/s} \approx 10^{-4}c$. For a star at the ecliptic *pole* — so that its light arrives perpendicular ($\theta = \pi/2$) to the Earth's instantaneous velocity — use the aberration formula to find the apparent angular displacement $\alpha = \pi/2 - \theta'$ of the star from its true direction, and show $\sin\alpha = U/c$ to leading order. Evaluate $\alpha$ in arcseconds.
2. Show that over one year, as the Earth's velocity direction rotates through $360^\circ$, the star's image traces a small *circle* of angular radius $\alpha \approx 20''$ about its true position.
3. Distinguish aberration from *parallax* (the apparent yearly motion due to the Earth's changing *position*): state two qualitative differences (amplitude dependence on distance; phase of the ellipse).
4. For a fast observer ($U$ comparable to $c$), describe how a *uniform grid* on the celestial sphere appears distorted, and show that as $U \to c$ the entire sky bunches into a forward spot. Show that for $U = 0.9c$ even the backward pole comes within the forward $90^\circ$ field of view.

**Recall:**

The exercise drills the aberration formula and its celestial-sphere consequences.

![[Thm - Aberration of Light#Statement]]

For a photon arriving perpendicular to the motion in $\mathcal{O}$'s frame ($\theta = \pi/2$), the aberration formula gives $\cos\theta' = U$, so the moving observer sees the light tilted forward by $\alpha = \pi/2 - \theta'$ with $\sin\alpha = \cos\theta' = U$. The [[Def - Apparent Rotation and Images of Moving Objects|celestial-sphere distortion]] is the global picture: a moving observer sees every direction swept toward the forward pole, with $\theta' \le \theta$.

---

# Convergent Strategy

**Problem class.** A *transform-a-direction* problem applied to starlight, plus a global *appearance* problem (the grid distortion). The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] for light problems is to feed the unit propagation direction into the aberration law.

**Assumption pattern.** A star at the ecliptic pole gives the clean perpendicular geometry $\theta = \pi/2$; the smallness $U \approx 10^{-4}$ means the leading-order $\sin\alpha = U$ suffices. For the grid distortion, the assumption is a *uniform* angular grid in $\mathcal{O}$'s sky, whose image under aberration is computed direction-by-direction.

**Theorem routing.** The [[Thm - Aberration of Light|aberration]] formula $\cos\theta' = (\cos\theta + U)/(1 + U\cos\theta)$, at $\theta = \pi/2$, gives $\cos\theta' = U$, hence $\sin\alpha = U$. For the grid, the same formula applied to every $\theta$ gives the global compression; the forward-pole image of the backward direction is the $\theta = \pi$ case.

**Key decision point.** The crux for parts 1–2 is recognising that the Earth's *velocity* (not position) is what aberration depends on, so the effect is the same for *all* stars regardless of distance — sharply distinguishing it from parallax, which depends on the Earth's *position* and hence on the star's distance. For part 4, the decision is to apply the formula across the whole sphere and observe that the *fixed points* are only the exact forward and backward poles, so everything else migrates forward.

---

# Legal Operations Used

1. **Specialise the composition law to light** (operation 5 from the topic page), here directly via the aberration formula with the perpendicular geometry $\theta = \pi/2$.

2. **Take a low-speed limit** (operation 9 from the topic page) to reduce $\sin\alpha = U/c$ to the small angle $\alpha \approx U/c \approx 20''$ for the Earth.

3. **Build the global image from the per-ray map** (operation 7/8 from the topic page), applying the aberration formula to every direction to obtain the celestial-sphere distortion.

---

# Hints

> [!note]- Hint 1
> A star at the ecliptic pole sends light perpendicular to the Earth's orbital velocity, so $\theta = \pi/2$ in the Sun's frame. Aberration gives $\cos\theta' = (\cos(\pi/2) + U)/(1 + U\cos(\pi/2)) = U$. The displacement from the perpendicular is $\alpha = \pi/2 - \theta'$, so $\sin\alpha = \cos\theta' = U$. With $U = 10^{-4}$, $\alpha \approx 10^{-4}\,\mathrm{rad} = 10^{-4}\times 206265'' \approx 20''$.

> [!note]- Hint 2
> The displacement is always *toward* the instantaneous direction of the Earth's velocity. Over a year that direction sweeps through $360^\circ$ in the orbital plane, so the apparent star position is displaced by a constant $\alpha \approx 20''$ toward a direction that rotates once per year — tracing a circle of radius $20''$ about the true position (an ellipse for stars not at the pole).

> [!note]- Hint 3
> Parallax depends on the Earth's *position* (baseline is the orbital radius), so it is largest for nearby stars and *decreases with distance* ($\le 0.77''$ for the nearest star). Aberration depends on the Earth's *velocity*, the same for all stars, so it is a fixed $20''$ *independent of distance*. Also, the parallactic ellipse and the aberration ellipse are $90^\circ$ out of phase as functions of the Earth's orbital position.

> [!note]- Hint 4
> For the grid: every direction $\theta$ maps to $\theta' \le \theta$, with equality only at $\theta = 0, \pi$. So the forward pole and backward pole are fixed, but everything in between is pulled forward. As $U \to 1$, $\cos\theta' = (\cos\theta + U)/(1 + U\cos\theta) \to 1$ for all $\theta < \pi$, crushing the sky to the forward pole. For $U = 0.9$, the backward direction $\theta = \pi$ stays at $\theta' = \pi$, but a direction just short of backward, e.g. $\theta$ with $\cos\theta' = 0$ (the $90^\circ$ boundary): solve $\cos\theta = -U = -0.9$, i.e. $\theta \approx 154^\circ$ — so directions from $0$ up to $154^\circ$ all land within the forward $90^\circ$.

---

# Solution

Stellar aberration is the aberration formula applied to the Earth's orbital motion. Step 1 gets the $\sin\alpha = U/c \approx 20''$ displacement; Step 2 traces the yearly circle; Step 3 distinguishes it from parallax; Step 4 scales up to a fast observer and the dramatic forward-bunching of the whole sky. The non-obvious point is that aberration depends on velocity (hence is distance-independent), unlike parallax.

**Step 1: The aberration angle for a polar star.**

> [!note]- Derivation
> A star at the ecliptic pole sends light perpendicular to the Earth's orbital velocity, so in the Sun's rest frame the incidence angle is $\theta = \pi/2$. The [[Thm - Aberration of Light|aberration]] formula gives the angle in the Earth's frame:
> $$\cos\theta' = \frac{\cos(\pi/2) + U}{1 + U\cos(\pi/2)} = \frac{0 + U}{1 + 0} = U.$$
> The star is displaced from the perpendicular by $\alpha = \pi/2 - \theta'$, so $\sin\alpha = \sin(\pi/2 - \theta') = \cos\theta' = U$, i.e.
> $$\boxed{\sin\alpha = \frac{U}{c}.}$$
> For the Earth, $U = 30\,\mathrm{km/s}$, $U/c = 10^{-4}$, so $\alpha \approx 10^{-4}\,\mathrm{rad}$. Converting, $1\,\mathrm{rad} = 206265''$, so
> $$\alpha \approx 10^{-4}\times 206265'' \approx 20.6''.$$
> This is the *constant of aberration*, measured by Bradley in 1728 (who got $\approx 20''$ and used it to estimate $c$).

**Step 2: The yearly aberration circle.**

> [!note]- Derivation
> The displacement is always directed toward the Earth's instantaneous velocity (the direction of motion is where rays bunch). As the Earth orbits, its velocity vector rotates through a full $360^\circ$ in the ecliptic plane over one year. For the polar star, the displacement has constant magnitude $\alpha \approx 20''$ and points toward this rotating velocity direction, so the apparent position traces a *circle* of angular radius $20''$ centred on the true position. For a star at an arbitrary ecliptic latitude, the displacement is still $\sim 20''$ toward the velocity, but the projection onto the sky is foreshortened in one direction, so the figure is an *ellipse* with semi-major axis $20''$ (the "aberration ellipse"). Bradley's discovery of this universal yearly ellipse was the first direct proof that the Earth moves.

**Step 3: Aberration versus parallax.**

> [!note]- Derivation
> Both produce a yearly apparent motion, but they have different origins and signatures:
>
> *Amplitude and distance.* Parallax arises from the Earth's *position* changing by the orbital diameter, so the parallactic displacement is (orbital radius)/(star distance) — it *decreases with distance*, reaching at most $0.77''$ for the nearest star (Proxima Centauri) and dropping below measurability for distant stars. Aberration arises from the Earth's *velocity*, which is the same wherever the star is, so the aberration displacement is a fixed $\approx 20''$ *independent of the star's distance* — and $20''$ is about $26$ times larger than even the largest parallax.
>
> *Phase.* The parallactic ellipse is traced such that the star's displacement is toward the Earth's *position* relative to the Sun, while the aberration ellipse has the displacement toward the Earth's *velocity*. Since velocity leads position by $90^\circ$ in a circular orbit, the two ellipses are $90^\circ$ out of phase: at the moment the parallactic displacement is maximal in one direction, the aberration displacement is maximal in the perpendicular direction. This phase difference is how the two effects are observationally separated.

**Step 4: The fast-observer celestial-sphere distortion.**

> [!note]- Derivation
> For an observer moving at $U$ comparable to $c$, apply the aberration formula to *every* direction. Since $\theta' \le \theta$ with equality only at $\theta = 0$ (forward) and $\theta = \pi$ (backward), every other direction is pulled toward the forward pole. A uniform angular grid in the rest observer's sky appears, to the moving observer, *compressed toward the forward direction and stretched near the backward direction*: the forward hemisphere's grid squares shrink and crowd together, while the backward hemisphere's expand.
>
> As $U \to 1$, for any $\theta < \pi$,
> $$\cos\theta' = \frac{\cos\theta + U}{1 + U\cos\theta} \to \frac{\cos\theta + 1}{1 + \cos\theta} = 1,$$
> so $\theta' \to 0$: the entire sky (except the exact backward point) is crushed into a tiny bright spot at the forward pole — the extreme headlight effect. A relativistic spacecraft would see all the stars crowd ahead of it.
>
> For $U = 0.9$, find which rest-frame directions land within the forward $90^\circ$ (i.e. $\theta' \le \pi/2$, $\cos\theta' \ge 0$): solve $\cos\theta' = 0$, i.e. $\cos\theta + U = 0$, $\cos\theta = -0.9$, giving $\theta \approx 154^\circ$. So rest-frame directions from $\theta = 0$ all the way to $\theta = 154^\circ$ — including directions well *behind* the perpendicular — are seen by the moving observer within its forward $90^\circ$ cone. In particular, objects that were $64^\circ$ behind the moving observer's "side" now appear ahead of it. Even the backward pole ($\theta = \pi$) remains at $\theta' = \pi$, but the field just short of it is dramatically swept forward. (This is the content of the Riazuelo celestial-grid images: for $U = 0.9c$, the two coordinate poles of the rest sky both appear within the forward $90^\circ$ field.)

> [!note]- Complete formal solution
> For a polar star, $\theta = \pi/2$ gives $\cos\theta' = U$, so the aberration displacement is $\alpha = \pi/2 - \theta'$ with $\sin\alpha = U/c$; for the Earth, $U/c = 10^{-4}$ gives $\alpha \approx 20.6''$. Over a year the Earth's velocity direction rotates through $360^\circ$, so the displacement (always toward the velocity) traces a $20''$ circle (an ellipse off the pole). Aberration depends on the Earth's velocity, hence is the same $20''$ for all stars regardless of distance, and its ellipse is $90^\circ$ out of phase with the distance-dependent parallactic ellipse ($\le 0.77''$). For a fast observer, every direction maps to $\theta' \le \theta$, crushing the sky toward the forward pole; as $U \to 1$ all directions but the backward pole collapse forward, and for $U = 0.9c$ rest-frame directions up to $\theta \approx 154^\circ$ fall within the forward $90^\circ$ field. $\blacksquare$

---

# Key Takeaways

**Aberration depends on velocity, parallax on position — and that single distinction separates two superficially identical yearly star-motions.** The reason aberration and parallax can be told apart, despite both producing a yearly elliptical wobble of every star, is that aberration is a function of the Earth's *velocity* while parallax is a function of its *position*. Velocity is the same for all stars, so aberration is a universal, distance-independent $20''$; position gives a baseline that subtends a smaller angle for more distant stars, so parallax shrinks with distance. The reusable diagnostic, valid far beyond astronomy: when two effects look alike, ask which *kinematic quantity* (position, velocity, acceleration) each depends on, because their differing dependence on the source's distance, speed, or geometry is usually what discriminates them experimentally. Here it also explains the $90^\circ$ phase offset (velocity leads position by a quarter cycle in circular motion), which is the practical handle observers use to disentangle the two.

**Forward-bunching is universal: every direction maps toward the direction of motion, so a fast observer sees the whole sky crowd ahead.** The inequality $\theta' \le \theta$ is not a statement about a single ray but about the *entire* aberration map — every direction except the exact forward and backward poles is pulled forward, and as the speed approaches $c$ the sky collapses into a forward spot. This is the trigger to recognise the *headlight effect* in any setting: a fast-moving observer (or, by reciprocity, a fast-moving source) concentrates the apparent or emitted radiation into a forward cone of half-angle $\sim 1/\Gamma$. The same map governs the appearance of the sky from a relativistic spacecraft, the forward-beaming of synchrotron radiation, and the angular distribution of decay products of fast particles. The conceptual content is that aberration is a *global* compression of the celestial sphere toward the velocity, not merely a small shift of individual stars.

**A clean perpendicular geometry turns a messy transformation into a one-line answer.** The reason the polar-star calculation collapses to $\sin\alpha = U/c$ is the deliberate choice of the $\theta = \pi/2$ geometry, where the aberration formula's denominator $1 + U\cos\theta$ becomes simply $1$. Choosing the configuration that trivialises the formula is a recurring move in relativistic problems: the perpendicular case isolates the leading effect with no clutter, and the general case can then be understood as a deformation of it. The transferable habit is to look, in any direction- or velocity-transformation problem, for the special geometry (perpendicular, collinear, or rest-frame) where the transformation simplifies, solve there first, and use that solution as the anchor for the general configuration. For aberration the perpendicular case gives the constant of aberration directly; the collinear case ($\theta = 0, \pi$) gives the no-aberration fixed points; and everything else interpolates.
