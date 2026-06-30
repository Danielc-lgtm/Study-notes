---
type: definition
subject: special-relativity
prereqs:
  - "Thm - Length Contraction (General)"
  - "Thm - Aberration of Light"
  - "Def - The Null Cone and the Time Arrow"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, mostly-minus signature, $u\cdot u = +1$. An observer $\mathcal{O}$ at event $O$ has four-velocity $u$ and [[Def - Observer and Local Rest Space|local rest space]] $E_u(O)$. An extended object sweeps out a **worldtube** $\mathcal{W}$ in spacetime — the region filled by the worldlines of all its constituent particles. Two slices of $\mathcal{W}$ matter: the **position** $\mathcal{T}_1 = \mathcal{W}\cap E_u(O)$ (the intersection with $\mathcal{O}$'s rest space — the set of object-events simultaneous with $O$ for $\mathcal{O}$), and the **image** $\mathcal{T}_2 = \mathcal{W}\cap\mathcal{I}^-(O)$ (the intersection with $\mathcal{O}$'s past light cone $\mathcal{I}^-(O)$ — the set of object-events whose emitted photons arrive at $O$). The object moves at velocity $V = V e$ relative to $\mathcal{O}$, with Lorentz factor $\Gamma = (1-V^2)^{-1/2}$. The celestial sphere $\mathscr{S}$ of $\mathcal{O}$ is the unit sphere of light-ray directions in $E_u(O)$. Full registry on [[Special Relativity VIII — Kinematics II, Change of Observer]].

This is a compound page: it defines three interlocking notions — the **image/position distinction**, the **apparent (Penrose–Terrell) rotation**, and the **image of a sphere and apparent superluminal motion** — because they all flow from the single observation that a photograph is a past-light-cone slice, and none is fully usable without that common root.

---

# Axiom Motivation

The naive expectation, after learning length contraction, is irresistible: a fast-moving object *is* contracted by $1/\Gamma$ along its motion, so surely a photograph of it shows it contracted — a moving sphere should look like an ellipsoid squashed in the direction of motion. This is wrong, and understanding precisely *why* it is wrong is the entire motivation for the image/position distinction, which is the foundational definition of this section.

The error is a conflation of two different things. The *position* of an object at an instant $t$ of $\mathcal{O}$'s time is where its parts *are* at that instant — the slice $\mathcal{T}_1$ of the worldtube by $\mathcal{O}$'s simultaneity surface $E_u(O)$. Length contraction is a true statement about $\mathcal{T}_1$: this slice really is contracted. But a camera does not record $\mathcal{T}_1$. A photograph is formed by photons that *arrive at the lens simultaneously*, and these photons were *emitted at different times* — light from the far parts of the object left earlier than light from the near parts, because it had farther to travel. So the image is the set of emission-events whose photons all reach $O$ together: the slice $\mathcal{T}_2$ of the worldtube by the *past light cone* $\mathcal{I}^-(O)$, not the rest space. These are different slices of the same worldtube, and they can look wildly different.

Why must we define the image by the past light cone rather than the rest space? Because *seeing* is the reception of light, and light takes time to travel. The desideratum for "what an object looks like" is "the configuration encoded in the light arriving now", and that configuration is, by the finiteness of the light speed, a snapshot of the object at *retarded* times — earlier for the farther parts. The rest-space slice $\mathcal{T}_1$ would be the right answer only if light were instantaneous; the past-light-cone slice $\mathcal{T}_2$ is the right answer in a world with a finite $c$. If you tried to define "image" as the rest-space position, you would be describing something no observer can ever see — a god's-eye simultaneous snapshot — rather than what a camera records.

Consider what this distinction immediately predicts, and how each prediction would fail under the naive definition. First, an approaching object looks *elongated*, not contracted: its trailing parts emitted light earlier, when the object was farther back, so the image stretches it out — the opposite of the FitzGerald squashing of its position. Second, a transversely moving cube reveals its *back face*: light from the back face, emitted earlier, has had time to swing around into view, so you see a face that is geometrically hidden in the rest-space slice — the object looks *rotated*. Third, and most strikingly, a moving sphere photographs as a *perfect circle*, because (as the aberration analysis shows) the Lorentz transformation acts conformally on the sky and sends the sphere's circular outline to another circle, with no flattening at all. Each of these is incomprehensible from the position picture and immediate from the image picture, and that is the case for taking $\mathcal{T}_2$, not $\mathcal{T}_1$, as the definition of what is seen.

The apparent rotation and the superluminal motion are then two consequences of this single root. The rotation is what the past-light-cone slice does to a *finite* object (it brings hidden faces into view); the apparent superluminal motion is what it does to the *time-separation between two images* of a moving point (it compresses them, because the source chases its own light). Both are "image effects", and both vanish in the instantaneous-light limit where $\mathcal{T}_2 \to \mathcal{T}_1$.

---

# The Definition

**The image/position distinction.** For an observer $\mathcal{O}$ at event $O$ with four-velocity $u$, and an object with worldtube $\mathcal{W}$:
- the **position** of the object (its configuration "now") is $\mathcal{T}_1 = \mathcal{W}\cap E_u(O)$, the slice by $\mathcal{O}$'s [[Def - Observer and Local Rest Space|local rest space]] (simultaneity surface);
- the **image** (its photograph, what is seen at $O$) is $\mathcal{T}_2 = \mathcal{W}\cap\mathcal{I}^-(O)$, the slice by $\mathcal{O}$'s past light cone.

Because $\mathcal{T}_1 \ne \mathcal{T}_2$ in general, the [[Thm - Length Contraction (General)|FitzGerald contraction]] (a property of $\mathcal{T}_1$) is *not* what a camera records.

**Apparent (Penrose–Terrell) rotation.** A cube of proper edge length $a$ moving at velocity $V$ perpendicular to the line of sight of a distant observer is photographed as identical to a cube *at rest* that has been *rotated* by the angle
$$
\theta = \arcsin V \qquad(\text{equivalently } \sin\theta = V,\;\cos\theta = 1/\Gamma).
$$
The image of the face oriented toward the observer has apparent width $a/\Gamma = a\cos\theta$; the (geometrically hidden) back face becomes visible with apparent width $Va = a\sin\theta$. Together these are exactly the projected widths of a rotated cube. The contraction of the front face ($a/\Gamma$) is essential: without it the image would be elongated and would *not* look like a pure rotation.

**Image of a sphere (Penrose's theorem) and apparent superluminal motion.** The image of a moving sphere is a **perfect circular disk**, of unchanged shape (only the angular size may change), for an observer in any state of motion: there is no visible contraction. This follows because the Lorentz transformation acts on the celestial sphere $\mathscr{S}$ by a conformal (circle-preserving) map (the [[Thm - Aberration of Light|aberration]] map, which under stereographic projection is a multiplication of the complex coordinate by a constant), so the sphere's circular outline maps to a circle.

A blob of matter moving at speed $V$ at angle $\theta$ to the line of sight has **apparent transverse velocity** (computed from two successive images, not two positions)
$$
V_{\mathrm{app}} = \frac{V\sin\theta}{1 - V\cos\theta},
$$
which exceeds $c = 1$ — **superluminal** — when $V$ is close to $1$ and $\theta$ is small. There is no contradiction with the speed limit, because $V_{\mathrm{app}}$ is derived from two *images* of the blob (light-arrival-defined) and not from its actual positions; the source partially chases its own emitted light, compressing the apparent travel time.

---

# Categorical / Structural Definition

The unifying structural statement is that *the image is the action of the Lorentz group, via aberration, on the celestial sphere*, and the celestial sphere carries only a **conformal structure**, not a metric. Concretely: each point of the object's outline, as seen by $\mathcal{O}$, is a direction on $\mathcal{O}$'s celestial sphere $\mathscr{S} \cong S^2$. Changing to a moving observer $\mathcal{O}'$ acts on $\mathscr{S}$ by the aberration map, which — projected stereographically to $\mathbb{C}P^1$ — is a **Möbius transformation**, an element of $\mathrm{PSL}(2,\mathbb{C})$. The restricted Lorentz group is isomorphic to this Möbius group, and Möbius transformations are exactly the conformal automorphisms of the sphere.

This is why a sphere stays a sphere: the outline of a sphere is a *circle* on $\mathscr{S}$, conformal maps send circles to circles, so the outline remains a circle for every observer. A metric structure on the sky would single out a "true" angular size and could be distorted by a boost; but only the *conformal* structure (angles and the circle-family) is observer-independent, and the circular outline lives entirely in that observer-independent structure. The apparent rotation of a cube is the same fact for a non-circular outline: the cube's edges, as a configuration of points on $\mathscr{S}$, are moved conformally, and the resulting configuration coincides with that of a rotated cube.

The image/position distinction itself is the statement that the relevant slice of the worldtube is the one selected by the *causal* structure (the past light cone) rather than the *metric/simultaneity* structure (the rest space). Two observers at the same event $O$ share the *same* past light cone $\mathcal{I}^-(O)$ — it is a frame-independent set — so they slice the worldtube identically and *see the same image*, even though they assign different *positions* (different rest-space slices). This frame-independence of the image, against the frame-dependence of the position, is the deep reason the image is the natural observer-independent object, and it is what makes the conformal/Möbius description possible.

---

# Relate to Other Fields / Compression

The image/position distinction is the special-relativistic instance of the general principle that *retarded* (light-cone) data, not instantaneous data, is what is physically accessible — the same principle that makes the [[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert]] fields of electromagnetism depend on the *retarded* position of a charge, not its present position. A photograph and a radiation field are both built from the past light cone, and both exhibit "the source appears where it *was*, not where it *is*". The apparent superluminal motion is the kinematic twin of the relativistic beaming of those retarded fields.

The conformal action on the celestial sphere is the same structure that organises **twistor theory**: Penrose takes the conformal sphere of light rays through a point, rather than the metric, as the primitive object, and the conformal group of compactified Minkowski space as the structure group. The "moving sphere stays a sphere" result is the elementary, observational face of the twistor philosophy that the sky is conformal.

**True name:** the image is *the slice of the worldtube by the observer's past light cone*, and its shape is *the conformal (Möbius) image of the object's outline on the celestial sphere*. The operational content: to find what a moving object looks like, never apply FitzGerald contraction — instead, impose that the photons forming the image arrive simultaneously (solve for the retarded emission events), or equivalently apply the aberration map to the object's outline and use that this map is conformal. The first method is concrete; the second tells you in advance that circles stay circles.

---

# Examples / Corollaries

**Is an instance — the rotated cube.** A cube moving transversely at $V = 0.6$ has $\Gamma = 1.25$, so its front face is photographed with width $a/\Gamma = 0.8a$ and its back face becomes visible with width $Va = 0.6a$; these are $a\cos\theta$ and $a\sin\theta$ for $\theta = \arcsin 0.6 = 37^\circ$, exactly the projected widths of a cube rotated by $37^\circ$. The image is indistinguishable from a stationary, rotated cube.

**Is an instance — the circular image of a relativistic sphere.** A sphere moving at $V = 0.95$ photographs as a perfect circle, not an ellipse, despite its *position* being an oblate ellipsoid contracted by $\Gamma \approx 3.2$ along the motion. The outline is a circle on the sky for every observer because aberration is conformal.

**Is an instance — the M87 jet's apparent $6c$.** Knots in the jet of M87 are observed to move across the sky at apparent speeds up to $\sim 6c$. With $V_{\mathrm{app}} = V\sin\theta/(1-V\cos\theta) \approx 6$, this requires $V \gtrsim 0.986$ ($\Gamma \gtrsim 6$) and a small viewing angle $\theta \lesssim 19^\circ$ — the source moving nearly toward us at nearly $c$.

**Is NOT an instance — a slowly moving object.** A car moving at $30\,\mathrm{m/s}$ ($V \sim 10^{-7}$) has $\mathcal{T}_2$ essentially equal to $\mathcal{T}_1$: the apparent rotation angle is $\arcsin(10^{-7}) \approx 10^{-7}\,\mathrm{rad}$, utterly unobservable, and the image is the position to extraordinary accuracy. The image/position distinction is invisible at everyday speeds, which is exactly why it is so counterintuitive — our entire visual experience is in the regime where seeing equals being.

**Is NOT an instance — the FitzGerald contraction of the position.** The contracted ellipsoid that is the moving sphere's *position* $\mathcal{T}_1$ is a real and correct object, but it is *not* the image; treating it as the image (expecting to photograph an ellipse) is precisely the error this definition exists to correct. The position is contracted; the image is a circle; both are true, of different slices.

**Corollary — the image is frame-independent at a fixed event.** Two observers crossing at $O$ with different velocities slice the worldtube by the *same* past light cone $\mathcal{I}^-(O)$ (a frame-independent set), so they record the *same* image $\mathcal{T}_2$ — though they assign different positions $\mathcal{T}_1$. What differs between them is the *labelling* of directions on the sky (aberration), not the set of emission-events seen.

**Calibration check.** If you have understood the definitions you should be able to: (i) explain in one sentence why an *approaching* rod looks *elongated* rather than contracted (its trailing end emitted its light earlier, from farther back, so the image stretches it); (ii) verify that the front-face width $a/\Gamma$ and back-face width $Va$ of the moving cube satisfy $(a/\Gamma)^2 + (Va)^2 = a^2$, confirming they are the legs of a right triangle with hypotenuse $a$ — the signature of a rotation by $\arcsin V$; and (iii) check that $V_{\mathrm{app}} = V\sin\theta/(1 - V\cos\theta)$ is maximised near $\cos\theta = V$, giving $V_{\mathrm{app}}^{\max} = \Gamma V$, which exceeds $1$ whenever $\Gamma V > 1$, i.e. $V > 1/\sqrt{2}$.

---

# Unlocked by This

> [!tip] Penrose's Theorem and the Conformal Sky *(from Twistor Theory)*
> The result that a moving sphere always photographs as a circle is **Penrose's theorem** (1959): the Lorentz group acts on the celestial sphere by conformal maps, which preserve circles. The deep reading is that an observer's sky carries a **conformal structure**, not a metric — only angles and the circle-family are observer-independent. This is the entry point to **twistor theory**, where the conformal structure of light rays, not the spacetime metric, is the primitive object, and the conformal group of compactified Minkowski space is the structure group.

> [!tip] Retardation and the Liénard-Wiechert Field *(from Electromagnetism)*
> The image/position distinction — that what is observed depends on the *retarded* (past-light-cone) configuration, not the instantaneous one — is the kinematic face of **retardation** in field theory. The field of a moving charge depends on its *retarded* position via the **[[Thm - The Liénard-Wiechert Potential|Liénard–Wiechert potentials]]**, and the apparent superluminal motion of an image has its field-theoretic twin in the beaming and apparent superluminal advance of radiation fronts; developed in [[Special Relativity XXII — Maxwell's Equations]].

> [!tip] Superluminal Jets and Relativistic Beaming in Astrophysics *(from High-Energy Astrophysics)*
> The apparent-superluminal formula, combined with the [[Thm - The Doppler Effect|Doppler]]-beaming of the same source, is the working toolkit of active-galactic-nucleus astrophysics: from the apparent speed one bounds the true bulk Lorentz factor and viewing angle of a jet, and the beaming explains why one sees only the approaching jet. The energy and radiation of such relativistic flows are the subject of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].
