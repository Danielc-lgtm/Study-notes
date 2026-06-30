---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Born Rigidity Criterion"
  - "Def - Synge World Function and Spatial Distance"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

Consider the **Rindler congruence**: a family of observers labelled by $\xi > 0$, where the observer with label $\xi$ has constant proper acceleration $a(\xi) = 1/\xi$ and worldline (in an inertial frame with $c = 1$)
$$
t(\tau) = \xi\,\sinh(\tau/\xi), \qquad x(\tau) = \xi\,\cosh(\tau/\xi),
$$
with $\tau$ the proper time of that observer, and $y, z$ fixed.

1. Verify that each worldline is timelike unit, with constant proper acceleration $a(\xi) = 1/\xi$, and that the family fills the **Rindler wedge** $x > |t|$.
2. Show that the events of all observers at the *same value of $\tau/\xi =: \eta$* (the "Rindler time") lie on a single straight line through the origin, which is the common [[Def - Observer and Local Rest Space|local rest space]] of the whole congruence at that instant.
3. Compute the **proper distance** between the observer at $\xi$ and the neighbour at $\xi + d\xi$, measured in their common rest space, and show it is **constant in $\eta$** — so the congruence is Born-rigid.
4. Confirm Born's criterion chronometrically: show the photon round-trip time between two neighbouring Rindler observers, *as measured by either observer's proper clock*, is constant in time. Contrast with why a uniformly rotating disk fails the Born criterion globally.

**Recall:**

![[Def - Born Rigidity Criterion#The Definition]]

The proper distance between simultaneous events in an observer's [[Def - Observer and Local Rest Space|rest space]] is the [[Def - Synge World Function and Spatial Distance|spatial length]] $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}}$ ($c=1$, mostly-minus). A worldline has unit four-velocity $U\cdot U = +1$ and four-acceleration $A = dU/d\tau$ with $\|A\| = \sqrt{-A\cdot A}$ ([[Def - Four-Velocity and Four-Acceleration|four-acceleration]]). The **Rindler wedge** is the region $x > |t|$ of Minkowski space.

---

# Convergent Strategy

**Problem class.** A *check-a-congruence-for-rigidity* problem: a specific family of worldlines is given, and the task is to compute its proper inter-observer distance and verify it is constant (Born-rigid). The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] is to find the common rest space, measure the proper distance there with Synge, and demand constancy.

**Assumption pattern.** The hyperbolic worldlines (constant proper acceleration) are the input; the key fact is that their common rest spaces are straight lines through the origin (the Rindler simultaneity surfaces), so neighbouring observers have a well-defined, computable proper separation. The signpost is "uniformly accelerated family / Rindler" — the canonical Born-rigid congruence.

**Theorem routing.** Part 1: differentiate the worldline to get $U$ and $A$, check $U\cdot U = +1$ and $\|A\| = 1/\xi$. Part 2: show the events at fixed $\eta = \tau/\xi$ lie on the line $t/x = \tanh\eta$, orthogonal to each four-velocity ([[Def - Observer and Local Rest Space|rest space]]). Part 3: the proper distance between $\xi$ and $\xi + d\xi$ along this line is $d\xi$ — independent of $\eta$, hence Born-rigid. Part 4: the round-trip time is computed from the null geodesics and shown constant.

**Key decision point.** The crux is recognising that all the Rindler observers *share* a rest space at each Rindler instant $\eta$ — the line through the origin at "angle" $\eta$ — which is what makes "the distance between neighbours" well-defined and time-independent. The non-obvious move is to use the radial coordinate $\xi$ itself as the proper distance: $\xi$ is the metric distance from the origin, so the separation of neighbours is $d\xi$, manifestly constant in $\eta$.

---

# Legal Operations Used

1. **Read the four-acceleration off the worldline** (operation 9 from the topic page). Differentiating twice gives $A = dU/d\tau$, and $\|A\| = 1/\xi$ confirms constant proper acceleration.

2. **Compute a spatial distance (Synge / proper length)** (operation 4 from the topic page). The inter-observer distance is measured in the common rest space as a proper length.

3. **Translate simultaneity into orthogonality** (operation 2 from the topic page). The common rest space is identified as the locus orthogonal to every four-velocity at fixed $\eta$.

---

# Hints

> [!note]- Hint 1
> Differentiate: $U = (dt/d\tau, dx/d\tau, 0, 0) = (\cosh(\tau/\xi), \sinh(\tau/\xi), 0, 0)$. Check $U\cdot U = \cosh^2 - \sinh^2 = 1$. Then $A = dU/d\tau = \tfrac{1}{\xi}(\sinh(\tau/\xi), \cosh(\tau/\xi), 0, 0)$, with $A\cdot A = \tfrac{1}{\xi^2}(\sinh^2 - \cosh^2) = -1/\xi^2$, so $\|A\| = 1/\xi$.

> [!note]- Hint 2
> At fixed $\eta = \tau/\xi$, the event is $(\xi\sinh\eta, \xi\cosh\eta, 0, 0)$. As $\xi$ varies (over the congruence) this traces the ray $t = x\tanh\eta$ through the origin. Check this ray is orthogonal to $U$: $U\cdot(\text{tangent of ray})$. The tangent of the ray (varying $\xi$ at fixed $\eta$) is $(\sinh\eta, \cosh\eta, 0, 0)$; its inner product with $U = (\cosh\eta, \sinh\eta, 0,0)$ is $\sinh\eta\cosh\eta - \cosh\eta\sinh\eta = 0$. Orthogonal — it is the common rest space.

> [!note]- Hint 3
> Along the ray at fixed $\eta$, the separation vector between $\xi$ and $\xi + d\xi$ is $d\xi\,(\sinh\eta, \cosh\eta, 0, 0)$. Its squared length is $(d\xi)^2(\sinh^2\eta - \cosh^2\eta) = -(d\xi)^2$, so the proper distance is $\|\cdot\| = \sqrt{-[-(d\xi)^2]} = d\xi$ — independent of $\eta$. Born-rigid.

> [!note]- Hint 4
> The proper distance $d\xi$ being constant means the radar round-trip time is constant. More directly: a photon between two Rindler observers traverses a fixed proper distance in the (static) Rindler metric $ds^2 = \xi^2 d\eta^2 - d\xi^2$, so the coordinate-time $\Delta\eta$ for a round trip is fixed, and each observer's proper time $\Delta\tau = \xi\,\Delta\eta$ is constant in time. For the rotating disk, the rest spaces do not close up globally (non-integrable), so there is no single rest space in which to measure a constant distance.

---

# Solution

The computation is a hyperbolic-trigonometry exercise with a clean punchline: the radial label $\xi$ *is* the proper distance from the origin, so neighbours are always $d\xi$ apart, at every Rindler instant. Step 1 verifies the worldlines are unit-timelike with constant acceleration. Step 2 finds the common rest spaces (rays through the origin). Step 3 computes the constant proper separation. Step 4 confirms Born's criterion chronometrically and contrasts the rotating disk.

**Step 1: Unit-timelike worldlines with constant proper acceleration.**

> [!note]- Derivation
> Differentiate the worldline $X(\tau) = (\xi\sinh(\tau/\xi), \xi\cosh(\tau/\xi), 0, 0)$:
> $$U = \frac{dX}{d\tau} = \big(\cosh(\tau/\xi), \sinh(\tau/\xi), 0, 0\big), \qquad U\cdot U = \cosh^2(\tau/\xi) - \sinh^2(\tau/\xi) = 1.$$
> So $U$ is future-directed unit timelike. The four-acceleration is
> $$A = \frac{dU}{d\tau} = \frac{1}{\xi}\big(\sinh(\tau/\xi), \cosh(\tau/\xi), 0, 0\big), \qquad A\cdot A = \frac{1}{\xi^2}\big(\sinh^2 - \cosh^2\big) = -\frac{1}{\xi^2}.$$
> Hence $\|A\| = \sqrt{-A\cdot A} = 1/\xi$: **constant** proper acceleration, equal to $1/\xi$, exactly as stated. (Also $A\cdot U = \tfrac{1}{\xi}(\sinh\cosh - \cosh\sinh) = 0$, as required.) Since $x = \xi\cosh(\tau/\xi) \geq \xi > 0$ and $x^2 - t^2 = \xi^2(\cosh^2 - \sinh^2) = \xi^2 > 0$, the worldline lies in the **Rindler wedge** $x > |t|$, and varying $\xi$ fills it.

**Step 2: The common rest spaces are rays through the origin.**

> [!note]- Derivation
> Introduce the **Rindler time** $\eta := \tau/\xi$, so the event of observer $\xi$ at Rindler time $\eta$ is $X(\xi, \eta) = (\xi\sinh\eta, \xi\cosh\eta, 0, 0)$. Fix $\eta$ and vary $\xi$ over the congruence: the events trace the ray
> $$\{(\xi\sinh\eta, \xi\cosh\eta, 0, 0) : \xi > 0\}, \quad\text{i.e. the line } t = x\tanh\eta \text{ through the origin}.$$
> This ray is the **common local rest space** of all Rindler observers at Rindler time $\eta$. To see it, note the four-velocity of observer $\xi$ at this event is $U = (\cosh\eta, \sinh\eta, 0, 0)$, while the tangent to the ray (the direction of increasing $\xi$ at fixed $\eta$) is $S = (\sinh\eta, \cosh\eta, 0, 0)$. Their inner product is
> $$U\cdot S = \cosh\eta\sinh\eta - \sinh\eta\cosh\eta = 0,$$
> so $S\perp U$: the ray lies in the rest space of *every* observer it passes through. The Rindler congruence's rest spaces are these rays, which fan out from the origin — and, crucially, they *do* fit together globally within the wedge (the congruence is irrotational, $\vec\omega = 0$), which is what makes a global "Rindler time" $\eta$ exist.

**Step 3: Constant proper separation — Born rigidity.**

> [!note]- Derivation
> Along the common rest-space ray at fixed $\eta$, the separation between the observer at $\xi$ and the neighbour at $\xi + d\xi$ is
> $$\overrightarrow{AB} = X(\xi + d\xi, \eta) - X(\xi, \eta) = d\xi\,(\sinh\eta, \cosh\eta, 0, 0) = d\xi\,S.$$
> Its squared spatial length is
> $$\overrightarrow{AB}\cdot\overrightarrow{AB} = (d\xi)^2\,(S\cdot S) = (d\xi)^2(\sinh^2\eta - \cosh^2\eta) = -(d\xi)^2,$$
> so the **proper distance** is
> $$\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}} = d\xi.$$
> This is **independent of $\eta$**: the proper distance between neighbouring Rindler observers is the constant $d\xi$ at every Rindler instant. By [[Def - Born Rigidity Criterion|Born's criterion]], the congruence is **Born-rigid**. (Equivalently: the spatial metric of the Rindler frame is $ds^2_{\text{space}} = d\xi^2$, with $\xi$ literally the proper distance from the wedge apex, so the separation $d\xi$ cannot change.) The graded accelerations $a(\xi) = 1/\xi$ — larger at smaller $\xi$, i.e. at the trailing edge — are exactly what is required for rigidity: the rear of a rigidly accelerating rod must accelerate harder.

**Step 4: The chronometric criterion, and why the rotating disk fails.**

> [!note]- Derivation
> The Rindler metric in coordinates $(\eta, \xi)$ is obtained from $t = \xi\sinh\eta$, $x = \xi\cosh\eta$:
> $$ds^2 = \xi^2\,d\eta^2 - d\xi^2,$$
> which is **static** (no $\eta$-dependence in the metric coefficients). A photon travelling radially between the observer at $\xi_1$ and the neighbour at $\xi_2$ satisfies $ds^2 = 0$, i.e. $\xi\,d\eta = \pm d\xi$, so the coordinate Rindler time for a one-way trip is $\Delta\eta = \int_{\xi_1}^{\xi_2}d\xi/\xi = \ln(\xi_2/\xi_1)$, **independent of $\eta$**. The round trip takes $\Delta\eta_{\text{round}} = 2\ln(\xi_2/\xi_1)$, constant in time. Each observer's *proper* time for the round trip is $\Delta\tau = \xi\,\Delta\eta_{\text{round}}$, a fixed multiple of a constant — so the photon round-trip time, measured by either observer's clock, is constant. This is exactly [[Def - Born Rigidity Criterion|Born's chronometric criterion]]: constant round-trip time $\Leftrightarrow$ rigid.
>
> **Contrast — the rotating disk.** A uniformly rotating congruence has nonzero four-rotation $\vec\omega\neq 0$, so its local rest spaces are *not* integrable (they do not fit into a global simultaneity slicing — $\underline{U_0}\wedge d\underline{U_0}\neq 0$). There is then no single global rest space in which to measure a time-independent inter-observer distance: going around the rim, the simultaneity surfaces fail to close up by the Sagnac time. The disk *can* be Born-rigid in *steady* rotation (it is one of the Noether–Herglotz motions), but it cannot be *spun up* rigidly (the **Ehrenfest paradox**: the rim would have to contract while the radius does not). The Rindler congruence succeeds precisely because it is irrotational, so its rest spaces foliate the wedge and the constant proper distance $d\xi$ is well-defined.

> [!note]- Complete formal solution
> Differentiating the Rindler worldline gives $U = (\cosh(\tau/\xi), \sinh(\tau/\xi), 0, 0)$ with $U\cdot U = 1$, and $A = \tfrac1\xi(\sinh, \cosh, 0, 0)$ with $\|A\| = 1/\xi$ — constant proper acceleration; the worldlines fill the wedge $x > |t|$. At fixed Rindler time $\eta = \tau/\xi$, the events $X(\xi,\eta) = (\xi\sinh\eta, \xi\cosh\eta, 0, 0)$ trace the ray $t = x\tanh\eta$, which is orthogonal to every $U$ ($U\cdot S = 0$ for $S = (\sinh\eta, \cosh\eta, 0,0)$) and hence is the common rest space. The neighbour separation is $\overrightarrow{AB} = d\xi\,S$ with $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(d\xi)^2$, so the proper distance is $d\xi$, independent of $\eta$: Born-rigid. Chronometrically, the static Rindler metric $ds^2 = \xi^2 d\eta^2 - d\xi^2$ gives a one-way light Rindler-time $\Delta\eta = \ln(\xi_2/\xi_1)$ independent of $\eta$, so the proper round-trip time $\xi\Delta\eta_{\text{round}}$ is constant — Born's criterion. The rotating disk fails because its rest spaces are non-integrable ($\vec\omega\neq 0$), so no global rest space exists for a constant distance (Ehrenfest). $\blacksquare$

---

# Key Takeaways

**A Born-rigid accelerating congruence needs graded accelerations — harder at the trailing edge — and the radial coordinate is the proper distance.** The Rindler congruence keeps a constant proper distance $d\xi$ between neighbours precisely because the proper acceleration is graded as $a(\xi) = 1/\xi$, larger at smaller $\xi$ (the rear). This is the relativistic statement that the back of a rigidly accelerating rod must push harder than the front, or the rod would stretch. The clean way to see the rigidity is that $\xi$ is literally the proper distance from the wedge apex (the spatial metric is $d\xi^2$), so the inter-observer distance $d\xi$ is frozen by construction. The transferable insight: to build a rigid accelerating reference frame, do not give all parts the same acceleration (that stretches the body — "Bell's spaceship paradox"); grade the acceleration inversely with the distance from a common apex, and the body stays rigid. The Rindler frame is the unique such rigid frame, and its apex is a horizon.

**The Rindler congruence is rigid because it is irrotational — its rest spaces foliate the wedge.** The decisive structural fact is that the common rest spaces are rays through the origin that fit together into a global foliation by the Rindler-time surfaces $\eta = \mathrm{const}$. This works because the congruence has zero four-rotation ($\vec\omega = 0$): an irrotational congruence's orthogonal rest spaces are integrable (Frobenius), so a global notion of "Rindler time" exists, and in each rest space the inter-observer distance is unambiguously defined and time-independent. The contrast with the rotating disk is the whole lesson: a *rotating* congruence ($\vec\omega\neq 0$) has non-integrable rest spaces — they fail to close up globally by the Sagnac time — so there is no global rest space in which to measure a constant distance, and the disk cannot be spun up rigidly (Ehrenfest). The diagnostic to carry forward: a congruence admits a coherent rigid extended frame exactly when its rotation vanishes; nonzero $\vec\omega$ destroys global simultaneity and with it the meaning of "the rigid distance between parts".

**Born rigidity is chronometric: constant proper distance is the same as constant photon round-trip time, and the static metric makes it manifest.** The exercise verifies Born's criterion two ways — geometrically (constant proper distance $d\xi$) and chronometrically (constant photon round-trip proper time) — and they agree because the Rindler metric is static ($\eta$-independent). The static character is what guarantees a photon takes the same Rindler-time $\ln(\xi_2/\xi_1)$ each way at every instant, so each observer's clock reads the same round-trip interval forever. The reusable principle: to test whether an extended accelerating system is rigid, bounce light between its parts and watch the round-trip time — constancy is rigidity, and a drifting round-trip time signals expansion or shear. This is exactly how one would operationally verify the rigidity of a real accelerating structure, and it ties the abstract Noether–Herglotz constraint to a concrete radar measurement that needs no ruler.
