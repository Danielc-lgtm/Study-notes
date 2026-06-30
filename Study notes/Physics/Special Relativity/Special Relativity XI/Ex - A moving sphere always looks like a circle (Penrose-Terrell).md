---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)"
tags: [physics, special-relativity]
---

# Problem Statement

A small opaque sphere is at rest in a frame $S$, and an observer in $S'$ moves at speed $\beta$ relative to $S$. Using the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|celestial-sphere]] picture:

1. Show that the silhouette (outline) of the sphere subtends a circle on any observer's celestial sphere, and that under the change of observer this circle maps to another circle — so the moving observer *also* sees a circular outline, not a length-contracted ellipse.
2. Explain the apparent paradox: length contraction is real, yet the sphere does not look contracted. Identify what *does* change (the apparent size and position, and patterns painted on the surface) and what does not (the circular outline).
3. State the closely related **Terrell rotation**: a moving cube appears rotated rather than contracted. Explain qualitatively why, using the celestial-sphere/conformal-map picture, and contrast with the naive expectation.

**Recall:**

![[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)#Statement]]

The outline of a sphere as seen from a point is the boundary of the *cone of tangent lines* from that point to the sphere — a circle on the celestial sphere. A change of observer acts on the celestial sphere by a [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|Möbius transformation]], which is conformal and sends circles to circles. The vault's [[Def - Apparent Rotation and Images of Moving Objects]] (Special Relativity VIII) gives the kinematic Penrose–Terrell treatment.

---

# Convergent Strategy

**Problem class.** A *conceptual application* of the conformality of the celestial-sphere map — the qualitative crown jewel of the chapter, resolving the apparent conflict between length contraction and what is seen. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Sources and Targets|topic target list]] names "compute the action on the celestial sphere" as a goal; this exercise reads the geometric consequence (circles stay circles) rather than a number.

**Assumption pattern.** The input is purely qualitative: the outline of a sphere is a circle on the celestial sphere, and the observer-change is a Möbius map. The signpost is that the question asks about *appearance* (what the sphere looks like) rather than coordinates, which immediately routes to the conformal celestial-sphere picture and away from the bare length-contraction formula.

**Theorem routing.** This is the geometric corollary of [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|the celestial-sphere theorem]] — specifically its circle-preservation lemma — applied to the silhouette of a sphere. It complements the kinematic treatment of [[Def - Apparent Rotation and Images of Moving Objects]].

**Key decision point.** The crux is distinguishing *the outline* of the sphere (a circle on the celestial sphere, governed by the conformal Möbius map, hence circle-preserving) from *the coordinates* of the sphere (genuinely length-contracted along the motion). The naive error is to apply the coordinate contraction to the appearance; the correct move is to recognise that the appearance is a Möbius image of a circle, which is a circle. Identifying that "appearance = conformal map of the sky" while "coordinates = affine Lorentz transformation" is the single decision that resolves the paradox.

---

# Legal Operations Used

1. **Parametrise a null direction by a spinor and project stereographically** (operation 7 from the topic page): the sphere's outline is a circle on the celestial sphere, parametrised by the null directions of its tangent rays.

2. **Use conformality (circle-preservation)** (operation 7 / warning 4 from the topic page): the entire argument rests on Möbius maps sending circles to circles, and on the warning that length contraction must *not* be applied to the apparent shape.

3. **Read the geometry from the celestial-sphere picture, not the coordinate transformation** (the chapter's meta-principle): the resolution comes from separating "what is seen" (conformal) from "what is measured" (affine).

---

# Hints

> [!note]- Hint 1
> The outline of a sphere, seen from any point, is where the lines of sight are *tangent* to the sphere — a cone of null rays whose intersection with the celestial sphere is a circle. This is true for *any* observer at any point, because tangency is a projective condition.

> [!note]- Hint 2
> A change of observer acts on the celestial sphere by a Möbius transformation (the [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|main theorem]]). Möbius maps send circles to circles. So the circular outline seen by $S$ maps to a circular outline seen by $S'$.

> [!note]- Hint 3
> The resolution of the paradox: length contraction is a statement about *simultaneous* coordinates (where the two ends of the object are *at the same time*), but seeing involves light emitted at *different* times from different parts of the object. The two notions differ, and the difference exactly cancels the contraction for the outline of a sphere.

> [!note]- Hint 4
> For the cube: light from the far (trailing) face, emitted earlier, reaches the observer alongside light from the near face. The far face becomes visible "around the side," and the net visual effect is indistinguishable from a *rotation* of the (uncontracted) cube, not a contraction.

---

# Solution

The exercise resolves the appearance-versus-coordinates puzzle. The plan: the sphere's outline is a circle on the celestial sphere; the observer-change is a circle-preserving Möbius map; so the outline stays circular; the contraction lives in the coordinates, not the appearance; and the cube's apparent rotation is the same effect for a non-spherical body.

**Step 1: The outline is a circle, and stays a circle.**

> [!note]- Derivation
> Fix an observer at a point $O$. The outline of the sphere, as $O$ sees it, is the set of directions in which the line of sight is *tangent* to the sphere — the rays from $O$ grazing the sphere form a cone, and this cone of null directions meets the celestial sphere of $O$ in a circle. (Tangency from a point is a projective/conformal condition, so the outline is exactly a circle, for any $O$.)
>
> Now compare two observers $S$ and $S'$ momentarily coincident at $O$ but in relative motion. Both see the *same* set of light rays through $O$ — the rays do not depend on the observer's velocity, only on the geometry at $O$ — but they assign them to *different* celestial spheres (the constant-$t$ versus constant-$t'$ slices). The map between the two celestial spheres is, by [[Thm - What the Observer Actually Observes (the Celestial Sphere and Möbius Transformations)|the main theorem]], a **Möbius transformation**. Since Möbius transformations send circles to circles (they are conformal), the circular outline on $S$'s celestial sphere maps to a circular outline on $S'$'s celestial sphere. Therefore the moving observer $S'$ *also* sees a circular silhouette — never an ellipse.

**Step 2: Resolving the paradox — coordinates contract, appearance does not.**

> [!note]- Derivation
> The puzzle: special relativity insists a moving sphere is length-contracted to an ellipsoid (squashed along the motion by $1/\gamma$), so why does it not *look* squashed?
>
> The resolution is the distinction between *coordinates* and *appearance*. Length contraction is a statement about the sphere's shape at a single instant of the observer's time — the locus of points $\{(\mathbf x) : \text{on the sphere at } t' = \text{const}\}$ — and that locus *is* a contracted ellipsoid. But *seeing* the sphere does not sample it at a single instant: light reaching the observer's eye now was emitted at *different* earlier times from different parts of the sphere (the far side's light left earlier, having farther to travel). The image is built from light emitted across a spread of times, and this spread exactly compensates the contraction for the outline.
>
> Quantitatively this is the content of Step 1: the appearance is governed by the *conformal* Möbius action on the celestial sphere, not the *affine* Lorentz action on coordinates. The conformal map preserves the circular outline; the affine map contracts coordinates. Both are correct — they answer different questions. What *does* change in the appearance: the sphere's *angular size* (it can look larger or smaller, blueshifted ahead or redshifted behind), its *position* on the sky (aberration moves it forward), and any *pattern painted on its surface* (a drawn grid is conformally distorted). What does *not* change: the circular outline. The contraction is real but, for a sphere's silhouette, photographically invisible — the **Penrose–Terrell** effect.

**Step 3: The Terrell rotation of a cube.**

> [!note]- Derivation
> For a non-spherical body the same conformal mechanism produces a different, equally counterintuitive appearance: a fast-moving cube looks *rotated*, not contracted.
>
> Consider a cube moving transversely past the observer at high speed. Naively one expects the cube's leading edge contracted by $1/\gamma$, giving a foreshortened box. Instead, the observer sees the *trailing* (far) face of the cube — which should be hidden behind the cube — because light from that face, emitted *earlier* (when the cube was farther back), reaches the observer at the same moment as light from the near face emitted *later*. The far face thus appears "wrapped around" into view. The combination of the visible far face and the length-contracted near face is, remarkably, *exactly* what one would see if the cube were *not* contracted but instead *rotated* by an angle whose sine is $\beta$. This is the **Terrell rotation** (Terrell 1959, anticipated by Penrose for the sphere): a rapidly moving object appears rotated rather than contracted.
>
> The celestial-sphere explanation unifies the two cases: the change of observer is a conformal map of the sky, which for the sphere preserves the circular outline (no apparent distortion of shape, only size and position) and for the cube rearranges the visible faces into the appearance of a rotation. In neither case does the object *look* squashed; the affine contraction of the coordinates is always reorganised, by the light-travel-time geometry, into a conformal map of the apparent image. The naive expectation — that you can photograph length contraction directly — is wrong precisely because appearance is conformal, not affine.

> [!note]- Complete formal solution
> The outline of a sphere from any point is the circle where the tangent rays meet the celestial sphere. Two observers coincident at that point see the same rays but on different celestial spheres, related by a Möbius transformation; since Möbius maps send circles to circles, the moving observer also sees a circular outline, not an ellipse. The paradox dissolves because length contraction concerns *simultaneous coordinates* while seeing samples light emitted at *different* times; the appearance is the conformal Möbius image of the sky, which preserves the circular outline, whereas the coordinates undergo the affine contraction. What changes in appearance is the angular size, position (aberration), and surface patterns; what does not is the circular outline (Penrose–Terrell). For a cube, the same conformal mechanism makes the earlier-emitted far face visible, and the net appearance is of a *rotated* (uncontracted) cube — the Terrell rotation. $\blacksquare$

---

# Key Takeaways

**"What is measured" and "what is seen" are different questions with different symmetry groups.** The deepest lesson of the chapter, crystallised in this exercise, is that the coordinates an observer *assigns* transform by the full (affine) Lorentz group, while the image an observer *sees* transforms by the conformal Möbius action on the celestial sphere. These are not the same: the first contracts lengths, the second preserves circles. Conflating them produces the false expectation that a sphere looks like an ellipse. The reusable diagnostic is to ask, of any relativistic-appearance problem, "is this about coordinates or about the photograph?" — and to route coordinate questions through the Lorentz transformation and appearance questions through the conformal celestial-sphere map. This single distinction resolves the Penrose–Terrell paradox, the Terrell rotation, and the apparent superluminal motion of jets, all of which are puzzles only if one forgets that seeing is conformal.

**Light-travel-time delay is the physical mechanism that converts affine contraction into conformal appearance.** The reason the appearance is conformal rather than affine is concrete: the image is assembled from light emitted at *different times* from different parts of the object, and this temporal spread is exactly what the celestial-sphere Möbius map encodes. The far side's light left earlier; by the time it arrives alongside the near side's light, the object has moved, and the geometry of "which earlier-emitted rays arrive now" is precisely the conformal transformation. So the cancellation of length contraction in the appearance of a sphere is not a coincidence but a structural consequence of the finite, frame-independent speed of light combined with the extended geometry of the object. The transferable insight: whenever an effect involves *seeing* an extended, rapidly moving object, the light-travel-time across the object is a leading-order effect, not a correction, and ignoring it (computing only the instantaneous contracted shape) gives the wrong picture.

**Conformal maps preserve outlines but distort painted patterns — so the invariant is the silhouette, not the surface.** A subtle but important point is that the Penrose–Terrell invisibility applies to the *outline* of a sphere, not to everything about it. A conformal Möbius map preserves circles (hence the circular silhouette) and angles, but it does *not* preserve, say, the spacing of a grid painted on the sphere's surface, which gets conformally stretched and compressed. So a relativistic sphere photographs with a perfectly circular outline but a distorted surface texture, and a relativistic globe would show its continents conformally deformed even as its limb stays round. The lesson is to be precise about *which* feature is invariant: under a conformal map, circles, angles, and the family of circles-and-lines are preserved, but distances, areas, and affine ratios are not. When applying the circle theorem, the protected object is the outline; the surface detail is fair game for distortion, and recognising exactly what conformality does and does not preserve is what separates the correct statement of Penrose–Terrell from the over-broad claim that "a moving object looks completely undistorted."
