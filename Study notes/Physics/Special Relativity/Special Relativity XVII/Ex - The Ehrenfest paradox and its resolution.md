---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Ehrenfest Paradox"
  - "Def - Born Rigidity Criterion"
  - "Thm - Length Contraction (General)"
tags: [physics, special-relativity]
---

# Problem Statement

A disk lies at rest with circumference $L_0 = 2\pi R_0$ and is then spun up to angular velocity $\omega$. Working with $c = 1$ where convenient:

1. Compute the circumference $L'$ and radius $R'$ of the rotating disk as measured by corotating observers, and show $L' = \Gamma\,2\pi R' > 2\pi R'$ with $R' = R_0$.
2. State the Ehrenfest paradox precisely: derive the contradiction that follows from assuming the disk remains **Born-rigid** during spin-up.
3. Resolve the paradox. Identify which assumption is false and explain, using the Herglotz–Noether theorem, why a disk cannot be spun up Born-rigidly.
4. Describe physically what happens to the disk material during spin-up — what stretches, what does not, and what stress develops.

**Recall:**

![[Def - The Ehrenfest Paradox#The Definition]]

A motion is [[Def - Born Rigidity Criterion|Born-rigid]] if the proper distance between every pair of neighbouring particles of the body stays constant in time. [[Thm - Length Contraction (General)|Length contraction]] acts only along the direction of motion: a rod moving at speed $v$ along its length is contracted by $\Gamma$, while a rod moving perpendicular to its length is unaffected.

---

# Convergent Strategy

**Problem class.** A *resolve-a-paradox* problem: two correct-looking arguments reach a contradiction, and the job is to locate the false premise. The [[Special Relativity XVII — Rotating Observers#Problem-Solving Strategy|topic strategy]]: the Ehrenfest paradox assumes rigidity, and the resolution is that rigidity fails for spin-up.

**Assumption pattern.** A disk spun up from rest, assumed rigid. The signpost is "rigid disk set into rotation": the assumption of Born rigidity (constant proper distances) clashes with the length-contraction requirement that the circumference grow by $\Gamma$, and the clash is the paradox.

**Theorem routing.** Part 1 applies direction-dependent [[Thm - Length Contraction (General)|length contraction]] to circumference (tangential) and radius (radial); part 2 confronts $L' = \Gamma\,2\pi R_0$ with the Born-rigid requirement $L' = L_0 = 2\pi R_0$ from [[Def - Born Rigidity Criterion]]; part 3 invokes Herglotz–Noether to reject rigidity; part 4 describes the elastic response.

**Key decision point.** The crux is recognizing that *both* halves of the contradiction are individually correct — corotating observers really measure $L' = \Gamma\,2\pi R_0$, and a Born-rigid disk really would keep $L' = 2\pi R_0$ — so the false premise is the *compatibility* of spin-up with rigidity. The natural but wrong instinct is to look for an error in the length-contraction reasoning; the actual resolution is that no rigid spin-up exists.

---

# Legal Operations Used

1. **Operation 6 from the topic page (measure lengths with corotating rulers, accounting for contraction).** The circumference is enhanced by $\Gamma$ (tangential), the radius unchanged (radial).

2. **Operation 2 from the topic page (the rim Lorentz factor).** $\Gamma = (1 - R^2\omega^2/c^2)^{-1/2}$ sets the circumference enhancement and the magnitude of the contradiction.

3. **Illegal operation 2 from the topic page (assuming Born-rigid spin-up).** The exercise is precisely about why this tempting assumption is illegal — no material disk can be spun up while preserving all proper distances.

---

# Hints

> [!note]- Hint 1
> The velocity of a rim point is tangential. A tangential arc is a rod oriented *along* the motion, so corotating observers measure it *longer* than the inertial observer by $\Gamma$: $L' = \Gamma\,2\pi R$. The radius is perpendicular to the motion, so it is uncontracted: $R' = R = R_0$.

> [!note]- Hint 2
> Born rigidity means all proper distances stay constant. The circumference is an internal proper distance of the disk, so if the disk is Born-rigid through spin-up, $L'$ keeps its rest value $L_0 = 2\pi R_0$. But part 1 gives $L' = \Gamma\,2\pi R_0 > 2\pi R_0$. The two are contradictory — that is the paradox.

> [!note]- Hint 3
> Both halves are correct, so the false assumption is that the disk *can* be Born-rigid during spin-up. The Herglotz–Noether theorem classifies all Born-rigid motions; the rotational ones form only a 3-parameter family (isometric rotations of an already-rotating body), and *none* connects rest ($\omega = 0$) to rotation ($\omega\ne 0$). So no rigid spin-up exists.

> [!note]- Hint 4
> Since the circumference must grow from $2\pi R_0$ to $\Gamma\,2\pi R_0$ while the radius stays $R_0$, the disk material must stretch tangentially. This induces hoop (circumferential) tension — the same stress that bursts a real flywheel spun too fast. The radial direction, perpendicular to the motion, is not stretched.

---

# Solution

The route has four steps. Step 1 computes the corotating circumference $\Gamma\,2\pi R_0$ (tangentially enhanced) and radius $R_0$ (unchanged). Step 2 confronts this with the Born-rigid requirement $L' = 2\pi R_0$, exhibiting the contradiction. Step 3 resolves it: rigidity is the false premise, forbidden by Herglotz–Noether. Step 4 describes the tangential stretching and hoop stress. The non-obvious move is recognizing that both contradictory statements are correct, so the resolution lies in rejecting rigidity, not the kinematics.

**Step 1: Corotating observers measure $L' = \Gamma\,2\pi R_0 > 2\pi R_0$, with $R' = R_0$.**

> [!note]- Derivation
> Consider the circumference. The velocity of a rim point is tangent to the rim, so a small arc of the rim is a rod oriented along the direction of motion. By [[Thm - Length Contraction (General)|length contraction]], the inertial observer $\mathcal{O}_*$ sees each such arc contracted by $\Gamma$ relative to its proper (corotating) length; equivalently, the corotating observers measure each arc *longer* than the inertial measurement by $\Gamma$. Summing around the rim,
> $$L' = \Gamma\,L = \Gamma\,2\pi R_0,$$
> using that the inertial observer, for whom the disk is simply a disk of radius $R = R_0$, measures $L = 2\pi R_0$.
>
> Consider the radius. The velocity is tangential, hence perpendicular to the radial direction. A radial rod is oriented across the motion, and there is no length contraction perpendicular to the velocity. So
> $$R' = R = R_0.$$
> Combining,
> $$\frac{L'}{R'} = \frac{\Gamma\,2\pi R_0}{R_0} = \Gamma\,2\pi > 2\pi,$$
> a non-Euclidean ratio. The corotating rest geometry has circumference exceeding $2\pi$ times the radius.

**Step 2: The Ehrenfest paradox — assuming Born rigidity gives a contradiction.**

> [!note]- Derivation
> Suppose the disk remains [[Def - Born Rigidity Criterion|Born-rigid]] throughout spin-up: the proper distance between every pair of its particles stays constant in time. The circumference is an internal proper distance (the total proper length around the rim), so Born rigidity requires it to keep its rest value:
> $$L'_{\text{rigid}} = L_0 = 2\pi R_0.$$
> But Step 1, from length contraction, gives
> $$L' = \Gamma\,2\pi R_0 > 2\pi R_0.$$
> These contradict each other: the rigidity assumption says the circumference is unchanged, while the kinematics says it is enhanced by $\Gamma$. This is the **Ehrenfest paradox** (1909): a rigid disk cannot be consistently spun up, because its circumference would have to be simultaneously $2\pi R_0$ (rigidity) and $\Gamma\,2\pi R_0$ (contraction).

**Step 3: Resolution — Born-rigid spin-up is impossible (Herglotz–Noether).**

> [!note]- Derivation
> Both halves of the contradiction are individually correct. Corotating observers genuinely measure $L' = \Gamma\,2\pi R_0$; and a genuinely Born-rigid disk would keep $L' = 2\pi R_0$. What is false is the *compatibility* of the two — the assumption that the disk *can* be Born-rigid while spinning up. The resolution is:
> $$\textbf{No material disk can be spun up from rest while remaining Born-rigid.}$$
> This is a theorem, the **Herglotz–Noether theorem**, which classifies all Born-rigid motions in special relativity. The rotational rigid motions form only a three-parameter family — the isometric rotations of a body *already* in stationary rotation — and there is *no* Born-rigid motion connecting the state of rest ($\omega = 0$) to a state of rotation ($\omega\ne 0$). The transition necessarily violates rigidity. So the paradox dissolves: during spin-up the disk is *not* Born-rigid, its circumference genuinely grows from $2\pi R_0$ to $\Gamma\,2\pi R_0$, and $L' = \Gamma\,2\pi R_0$ holds with no contradiction. The premise "$L' = L_0$" was the smuggled-in falsehood, justified only by the (impossible) rigidity assumption.

**Step 4: Physically, the rim stretches and develops hoop stress; the radius does not.**

> [!note]- Derivation
> Since the corotating circumference must grow from $2\pi R_0$ to $\Gamma\,2\pi R_0$ while the radius stays $R_0$, the disk material must **stretch tangentially** — the circumferential proper length increases. This tangential stretching induces **hoop tension** (circumferential stress) in the material, exactly the stress that, in a real flywheel spun too fast, causes it to burst. The radial direction, perpendicular to the motion, is *not* stretched ($R' = R_0$ throughout), so the stress is purely circumferential. A real disk accommodates the spin-up by elastic deformation: the atoms at the rim end up farther apart (in proper distance) than they were at rest, the bonds between them are under tension, and if the rotation is too fast the bonds break. The relativistic statement "the circumference must grow by $\Gamma$" is the extreme-speed limit of the everyday hoop stress of a spinning disk.

> [!note]- Complete formal solution
> Corotating observers measure the circumference, tangential to the motion, as $L' = \Gamma\,2\pi R_0$ (length contraction enhances the proper arc length), and the radius, perpendicular to the motion, as $R' = R_0$ (uncontracted), giving $L'/R' = \Gamma\,2\pi > 2\pi$. The Ehrenfest paradox arises from assuming the disk stays Born-rigid through spin-up, which would force $L' = L_0 = 2\pi R_0$, contradicting $L' = \Gamma\,2\pi R_0$. Both statements are correct; the false premise is their compatibility. By the Herglotz–Noether theorem, no Born-rigid motion connects rest to rotation, so the disk cannot be spun up rigidly: the circumference genuinely stretches to $\Gamma\,2\pi R_0$, inducing hoop stress, while the radius stays $R_0$. The paradox dissolves. $\blacksquare$

---

# Key Takeaways

**When two correct arguments contradict, the false premise is their compatibility — here, that spin-up can be rigid.** The Ehrenfest paradox is resolved not by finding an error in either argument (both the length-contraction circumference and the Born-rigid circumference are correctly computed) but by recognizing that the two cannot both apply: no rigid spin-up exists. The trigger for this resolution pattern is any paradox where each side is independently verified — the error is in an unstated assumption that the two situations are compatible. In the [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction|twin paradox]] the smuggled assumption is symmetry (only one twin accelerates); here it is rigidity (no rigid spin-up exists). The general lesson: audit the *bridge* between two correct sub-arguments, not the sub-arguments themselves. Almost every relativistic paradox is manufactured by an illegitimate compatibility assumption.

**Born rigidity is far more restrictive in relativity than the Newtonian rigid body — and spin-up is forbidden.** The Newtonian rigid body, with its implicit infinite speed of sound, does not survive relativity: a disturbance cannot propagate faster than light, so "rigid" must be redefined as "constant proper distances", and the Herglotz–Noether theorem then shows the rigid motions are a meagre family — for rotation, only the isometric rotations of an already-spinning body, with no path from rest to rotation. The trigger is any problem invoking a "rigid" extended body in relativity: check whether the proposed motion is actually Born-rigid, because most are not. This is why relativistic continuum mechanics is genuinely different from Newtonian: elasticity and stress are forced, not optional, and a body set into rotation *must* deform. The impossibility of rigid spin-up is the cleanest example, and it is the relativistic root of the hoop stress that limits real flywheels.

**The disk's non-Euclidean rest geometry is the seed of curved spacetime, and the resolution shows curvature is physical, not paradoxical.** Once one accepts that the circumference genuinely stretches and the rest geometry is genuinely non-Euclidean ($L'/R' = \Gamma\,2\pi > 2\pi$), there is no paradox — only a flat spacetime whose rotating-observer rest space is curved. The trigger to recognize here is that *acceleration produces non-Euclidean geometry within special relativity*, a fact that, by the equivalence principle, suggested to Einstein that *gravity* (equivalent to acceleration) curves spacetime. The Ehrenfest disk is the historically decisive example: it convinced Einstein that the flat metric $\eta_{\mu\nu}$ is inadequate for gravity and that general relativity must be a theory of curved spacetime with a position-dependent metric. The resolution of the paradox — accepting the non-Euclidean geometry as real — is thus also the conceptual opening to general relativity, developed in [[Special Relativity XXV — Toward Relativistic Gravitation]] and realized in [[General Relativity I — Einstein's Equations and Schwarzschild]]. See [[Ex - The line element on the rotating disk]] for the explicit non-Euclidean spatial metric.
