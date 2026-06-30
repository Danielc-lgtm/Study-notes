---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Apparent Rotation and Images of Moving Objects"
  - "Thm - Length Contraction (General)"
tags: [physics, special-relativity]
---

# Problem Statement

Reconstruct the photographic image of a moving object from the requirement that the photons forming it arrive at the observer simultaneously, and show it differs sharply from the FitzGerald-contracted position. Working with $c = 1$:

1. A rod of proper length $L_0$ moves directly *toward* a distant observer at speed $V$. By imposing that the light from its two ends arrives together, show that the rod's *image* has length $L_{\mathrm{img}} = L_0\sqrt{(1+V)/(1-V)}$ — *longer* than $L_0$, not contracted.
2. A cube of proper edge $a$ moves *transversely* (perpendicular to the line of sight) at speed $V$, the observer being distant. Show that the image shows the front face with apparent width $a/\Gamma$ *and* the normally-hidden back face with apparent width $Va$.
3. Setting $\theta = \arcsin V$, show $a/\Gamma = a\cos\theta$ and $Va = a\sin\theta$, so the image is identical to that of a stationary cube *rotated* by $\theta$ — the **Penrose–Terrell rotation** of a cube.
4. Explain the role of the FitzGerald contraction: show that without it the image would be elongated and would *not* look like a pure rotation.

**Recall:**

This exercise drills the image-versus-position distinction for finite objects.

![[Def - Apparent Rotation and Images of Moving Objects#The Definition]]

The image is the slice of the worldtube by the past light cone (photons arriving together, emitted at *different* times), distinct from the position (rest-space slice). The front face of the moving cube is [[Thm - Length Contraction (General)|contracted]] to $a/\Gamma$; the back face becomes visible because its light, emitted earlier, swings into view. The apparent rotation angle is $\theta = \arcsin V$.

---

# Convergent Strategy

**Problem class.** A *predict-an-image* problem for finite objects, exhibiting both the elongation of an approaching rod and the rotation of a transverse cube. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] for appearance problems is to impose simultaneous photon arrival and solve for the emission events.

**Assumption pattern.** A finite object (rod or cube) with a distant observer (parallel rays). The defining condition is that the photons forming the image *arrive together* but were *emitted at different retarded times*, because the farther parts of the object are farther away. This retardation, combined with the object's motion, produces the elongation/rotation.

**Theorem routing.** The arrival-simultaneity condition routes to a retarded-time difference between the near and far parts, which (times the object's velocity) gives the apparent displacement. For the cube, this displacement reveals the back face (width $Va$) while [[Thm - Length Contraction (General)|contraction]] sets the front face (width $a/\Gamma$); the identity $(a/\Gamma)^2 + (Va)^2 = a^2$ routes to the rotation $\theta = \arcsin V$.

**Key decision point.** The crux is imposing *simultaneous arrival*, not simultaneous emission — the photons that form one snapshot left the object at different times, earlier from the farther parts. The natural error is to take a simultaneous-emission snapshot (the position) and apply contraction; the correct image uses simultaneous *arrival*, which brings in the retardation that elongates the rod and rotates the cube. The decision to track *when each part emitted its light*, given when it all arrives, is the whole method.

---

# Legal Operations Used

1. **Build an image from the past light cone** (operation 7 from the topic page). The image is the set of emission events whose photons arrive at the observer simultaneously — a retarded-time construction, not a simultaneity slice.

2. **Use length contraction for the position, then correct for retardation** (operation 6 from the topic page). The front face's apparent width is the contracted $a/\Gamma$; the back face's visibility and width come from the retardation, not from contraction.

---

# Hints

> [!note]- Hint 1
> For the approaching rod, let the far end (length $L$ behind the near end in the *contracted* position, $L = L_0/\Gamma$) emit its photon earlier, when it was farther back. Actually, work directly: the image length is the apparent separation of the two ends in the arriving light. The near end emits later; in the time difference, the rod advances, *adding* to the apparent length. The result is $L_0\sqrt{(1+V)/(1-V)}$ — a Doppler-like elongation. (One clean route: the image length scales by the radial Doppler factor.)

> [!note]- Hint 2
> For the transverse cube, consider a photon from the *back* corner of the side face (the face pointing away from the observer's forward direction), emitted at $t = 0$, and photons from the *front* face emitted at $t = a$ (one edge-length later, the light-crossing time of the cube). In that time $a$, the cube moves $Va$ transversely. All these photons arrive together. So the image shows the back face displaced sideways by $Va$ — it becomes visible — while the front face is contracted to $a/\Gamma$.

> [!note]- Hint 3
> The image has a front-face width $a/\Gamma = a\sqrt{1-V^2}$ and a back-face (now visible) width $Va$. Set $\sin\theta = V$, so $\cos\theta = \sqrt{1-V^2} = 1/\Gamma$. Then the two widths are $a\cos\theta$ and $a\sin\theta$ — exactly the projected widths of a cube rotated by $\theta$ about the vertical axis.

> [!note]- Hint 4
> If there were *no* contraction, the front face would have apparent width $a$ (not $a/\Gamma$), and the image would have widths $a$ and $Va$ — which do *not* satisfy $a^2 + (Va)^2 = (\text{const})^2$ for a rotation. The image would be elongated, not a clean rotation. The contraction $a \to a/\Gamma = a\cos\theta$ is exactly what makes the front-face width equal $a\cos\theta$, completing the rotation.

---

# Solution

The image of a moving object is built from simultaneously-arriving, differently-emitted photons, and it elongates an approaching rod and rotates a transverse cube. Step 1 gets the rod's elongation; Step 2 reconstructs the cube's image with its visible back face; Step 3 identifies it as a rotation; Step 4 shows contraction is essential to the rotation. The non-obvious move is imposing simultaneous *arrival*, bringing in the retardation that distinguishes image from position.

**Step 1: The approaching rod is elongated.**

> [!note]- Derivation
> A rod of proper length $L_0$ approaches a distant observer at speed $V$ along the line of sight. Its *position* (rest-space slice) is the contracted length $L_0/\Gamma$. But the *image* is built from photons arriving together. The far end (trailing) is farther from the observer, so its image-forming photon was emitted *earlier*; in the interval between the far-end and near-end emissions, the rod advances toward the observer, and this advance *adds* to the apparent end-to-end separation.
>
> Quantitatively, the image length is the position length boosted by the radial approach factor: each part of the rod is seen at its retarded position, and the systematic retardation stretches the approaching rod. The clean result is that the image length is the proper length times the radial Doppler factor,
> $$L_{\mathrm{img}} = L_0\sqrt{\frac{1+V}{1-V}} > L_0,$$
> an *elongation*, the opposite of contraction. (Equivalently: the contracted position $L_0/\Gamma$ times the arrival-compression $1/(1-V)$ gives $L_0/[\Gamma(1-V)] = L_0\sqrt{(1+V)/(1-V)}$.) An approaching rod looks *longer* than its rest length, dramatically so as $V \to 1$.

**Step 2: The transverse cube reveals its back face.**

> [!note]- Derivation
> A cube of proper edge $a$ moves transversely (perpendicular to the line of sight) at speed $V$; the observer is far away, so the light rays reaching it are parallel. Consider the face of the cube pointing *away* from the direction of motion — call it the back face — which is geometrically hidden from a static observer. A photon leaving the back edge of this face at time $t = 0$ must travel one extra cube-depth $a$ (the light-crossing time of the cube) to reach the same wavefront as a photon leaving the front face. So the front-face photons that arrive *together* with the back-edge photon were emitted at $t = a$ (one edge-length later).
>
> In that interval $\Delta t = a$, the cube moves transversely by $V\Delta t = Va$. Therefore, in the image:
> - the **back face**, hidden in the static view, is displaced sideways into view by $Va$, appearing with apparent width $Va$;
> - the **front face** (toward the observer) is seen at one instant, contracted by [[Thm - Length Contraction (General)|length contraction]] to apparent width $a/\Gamma$.
>
> The image thus shows *two* faces — the front and the normally-hidden back — side by side, with widths $a/\Gamma$ and $Va$.

**Step 3: The image is a rotated cube.**

> [!note]- Derivation
> Set $\theta := \arcsin V$, so $\sin\theta = V$ and $\cos\theta = \sqrt{1 - V^2} = 1/\Gamma$. Then the two apparent widths are
> $$\text{front face: } \frac{a}{\Gamma} = a\cos\theta, \qquad \text{back face: } Va = a\sin\theta.$$
> These are *exactly* the projected widths of a cube of edge $a$, at rest, rotated by the angle $\theta$ about the vertical axis: a rotation by $\theta$ presents the front face foreshortened to $a\cos\theta$ and brings the side face into view with projected width $a\sin\theta$. The moving cube's image is therefore **indistinguishable from a stationary cube rotated by $\theta = \arcsin V$** — the **Penrose–Terrell rotation**. One checks the consistency $(a/\Gamma)^2 + (Va)^2 = a^2(1-V^2) + a^2V^2 = a^2$, confirming the two widths are the legs of a right triangle with hypotenuse $a$, the geometric signature of a rotation.

**Step 4: The role of contraction.**

> [!note]- Derivation
> Suppose there were *no* FitzGerald contraction (a purely Newtonian finite-light-speed theory). Then the front face would appear at its full width $a$, not $a/\Gamma$, and the image would show widths $a$ (front) and $Va$ (back). But $a^2 + (Va)^2 = a^2(1 + V^2) \ne a^2$, so these are *not* the legs of a right triangle with hypotenuse $a$ — the image would be *elongated* (total apparent extent larger than $a$) and would *not* coincide with any pure rotation of the cube. It would look like a sheared or stretched cube, not a rotated one.
>
> It is precisely the contraction $a \to a/\Gamma = a\cos\theta$ that shrinks the front face to the value a rotation requires, completing the illusion of a rigid rotation. So the apparent rotation is a *combination* of two effects: the finite-light-speed retardation (which reveals the back face, width $Va$ — present even in Newtonian optics) and the relativistic contraction (which trims the front face to $a\cos\theta$ — without which the image would not be a clean rotation). The retardation provides the rotation's "sine"; the contraction provides its "cosine".

> [!note]- Complete formal solution
> The image is built from photons arriving together but emitted at different retarded times. An approaching rod's far end emits earlier, and the rod's advance in the interim elongates the image to $L_{\mathrm{img}} = L_0\sqrt{(1+V)/(1-V)} > L_0$ (the contracted position $L_0/\Gamma$ times the arrival compression $1/(1-V)$). For a transversely moving cube, photons from the hidden back face (emitted a light-crossing time $a$ earlier) arrive with the front-face photons; in that time the cube moves $Va$, so the back face appears with width $Va$ while the front face is contracted to $a/\Gamma$. Setting $\sin\theta = V$ ($\cos\theta = 1/\Gamma$), these widths are $a\sin\theta$ and $a\cos\theta$ — the projection of a cube rotated by $\theta = \arcsin V$, with $(a/\Gamma)^2 + (Va)^2 = a^2$. Without contraction the front face would be $a \ne a\cos\theta$, and the image would be elongated, not a rotation; the contraction is what makes the apparent motion a clean rotation. $\blacksquare$

---

# Key Takeaways

**The image is built from simultaneously-arriving, differently-emitted photons — impose arrival simultaneity, not emission simultaneity.** The method that unlocks every image problem is to remember that one photographic snapshot is formed by photons that *arrive* together but *left* the object at different (retarded) times — earlier from the farther parts. This is the operational content of "the image is the past-light-cone slice". Taking instead a simultaneous-*emission* snapshot gives the position (and length contraction), which is *not* what a camera records. The reusable procedure: to find an image, fix the arrival time, trace each photon back to find when and where each part of the object emitted it, and assemble those retarded emission points — the retardation is what produces the elongation, the rotation, and the apparent superluminal motion. The trigger to apply this: any "what is photographed / seen / observed" question, as opposed to "where is it" — the former needs arrival-simultaneity, the latter emission-simultaneity.

**Apparent rotation is retardation (the back face) plus contraction (the front face), and both are needed for a clean rotation.** The Penrose–Terrell rotation of a cube is not a single relativistic effect but a conspiracy of two: the *finite light speed* reveals the hidden back face (apparent width $Va = a\sin\theta$), an effect present even in Newtonian optics; and the *relativistic contraction* trims the front face to $a/\Gamma = a\cos\theta$, which is what a genuine rotation requires. Without the contraction, the image would be elongated and would not look like a rotation at all. The transferable insight is that relativistic appearances often combine a classical light-travel-time piece with a relativistic length-contraction piece, and only their specific combination produces the clean geometric illusion (here, a rigid rotation). Recognising which part of an apparent effect is retardation and which is contraction is essential to understanding why the illusion is so perfect — the contraction is precisely tuned to complete the rotation. This is the finite-object version of the [[Ex - The Penrose-Terrell rotation of a moving sphere|sphere result]], where the same conspiracy keeps a sphere's outline circular.

**An approaching object looks longer, a receding one shorter — the image elongation is the opposite of the position contraction.** One of the most counterintuitive results is that an approaching rod's *image* is *elongated* by the Doppler-like factor $\sqrt{(1+V)/(1-V)}$, the exact opposite of the FitzGerald contraction of its *position*. The mechanism is that the trailing end's light, emitted earlier from farther back, combined with the rod's approach, stretches the apparent length. The diagnostic to carry forward: never assume a fast object looks contracted — for radial motion the image elongates (approach) or shrinks (recession) by the radial Doppler factor, and for transverse motion it rotates, but in no case is the photographed shape simply the contracted position. The position is contracted; the image is a retardation-distorted projection, and the two can even have opposite signs (image longer, position shorter). This is the sharpest possible illustration that relativistic *seeing* and relativistic *being* are different, related only through the past-light-cone construction.
