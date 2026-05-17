---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. The interval between two events with separation $(\Delta t, \Delta x, \Delta y, \Delta z)$ is $\Delta s^2 = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ (see [[Def - The Spacetime Interval]]). A primed frame $S'$ moves at velocity $v$ along the $x$-axis of $S$, with $\gamma = (1-v^2)^{-1/2}$, and the coordinates are related by the [[Def - The Lorentz Transformation|Lorentz transformation]]. Full registry on [[Special Relativity I — Lorentz Transformations and Minkowski Space]].

---

# Statement

> **Invariance of the spacetime interval.** Let $S$ and $S'$ be inertial frames related by a Lorentz transformation. For any two events, with separation $(\Delta t, \Delta x, \Delta y, \Delta z)$ in $S$ and $(\Delta t', \Delta x', \Delta y', \Delta z')$ in $S'$, the spacetime interval is the same in both frames:
> $$\Delta s^2 \;=\; \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2 \;=\; \Delta t'^2 - \Delta x'^2 - \Delta y'^2 - \Delta z'^2.$$
> Conversely, the linear maps of spacetime that preserve $\Delta s^2$ for every pair of events are exactly the Lorentz transformations (composed with translations).

---

# Motivation

The [[Def - The Lorentz Transformation|Lorentz transformation]] has dismantled the Newtonian absolutes: the elapsed time $\Delta t$ between two events and the spatial distance between them are now frame-dependent, different for different observers. This is unsettling, and it raises an urgent question — is there *anything* about the relationship between two events that all observers agree on, or is everything up for grabs?

This theorem is the answer, and it is reassuring: one quantity survives. The particular combination $\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ is the same in every inertial frame. Time and space are individually relative, but this specific blend of them is absolute. The theorem is the foundation stone of the geometric viewpoint: it says spacetime carries a genuine, observer-independent notion of "interval", and that interval is what the geometry of §1.3 is built on.

One should *expect* a result like this from the rotation analogy. An ordinary rotation scrambles the coordinates of a point but leaves the distance from the origin invariant — indeed that is the defining property of a rotation. The Lorentz transformation is a rotation between space and time, so it too ought to leave some quadratic quantity invariant. The theorem says exactly which one, and the surprise is only in the minus signs: the invariant blends time and space with *opposite* sign, $+\Delta t^2 - \Delta x^2$, not the same sign.

The converse half of the statement is the deeper one. It says the interval is not merely *an* invariant of the Lorentz transformation — it is strong enough to *characterise* it. The Lorentz transformations are precisely the linear maps that preserve the interval. This is what licenses the reorganisation of §1.2: instead of deriving the boost from the postulates, declare the interval primary and *define* the Lorentz group as its symmetry group ([[Def - The Lorentz Group]]).

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$S$ and $S'$ are related by a Lorentz transformation". The point of input broadening is to recognise the many disguises that hypothesis wears.

The first disguised source is **"$S$ and $S'$ are any two inertial frames"**. By the [[Def - Inertial Frame and the Postulates of Special Relativity|postulates]], any two inertial frames are related by a Lorentz transformation (a boost, possibly composed with a rotation). So whenever a problem mentions two inertial observers — without ever writing down a transformation matrix — the theorem applies. The bridge is the derivation of the Lorentz transformation from the postulates; once you trust that derivation, "two inertial frames" *is* "related by a Lorentz transformation". *Example problem:* show that two observers in arbitrary relative motion agree on whether two given events can be connected by a light ray.

The second disguised source is **"a quantity is the squared norm of a separation four-vector"**. If a calculation produces $\Delta X \cdot \Delta X$ for a [[Def - Four-Vector|four-vector]] $\Delta X$, that is the interval, and the theorem makes it invariant. The bridge is the identification of the interval with the Minkowski norm-squared, $\Delta s^2 = \eta_{\mu\nu}\Delta X^\mu\Delta X^\nu$. The nonobviousness is that many quantities in relativistic kinematics — a particle's rest mass, a relative speed — are secretly four-vector norms, hence secretly intervals, hence invariant. *Example problem:* show that the rest mass of a particle, $m^2 = P\cdot P$, is the same in every frame.

The third disguised source is **"a worldline segment is given"**. The interval along an infinitesimal step of any timelike worldline is $ds^2 > 0$, and the theorem makes $ds$ frame-independent — which is what allows proper time to be *defined* by integrating $ds$. The bridge is that proper time is the accumulated interval. *Example problem:* compute the age of the travelling twin by integrating $ds$ along the bent worldline ([[Ex - The twin paradox]]).

**Targets (Output Amplification)**

The conclusion is "$\Delta s^2$ is the same in $S$ and $S'$".

Combine the conclusion with **the freedom to choose the frame**. Since the interval has the same value everywhere, you may compute it in whichever frame makes it trivial — typically a frame where one of $\Delta t, \Delta x$ vanishes. The further result is the single most powerful labour-saving technique in the subject: any invariant is evaluated in its most convenient frame and the answer transported everywhere. The combination is useful because it converts a hard cross-frame comparison into an easy one-frame computation. *Example:* the proper time between two timelike-separated events is most easily found in the frame where they happen at the same place, where $\Delta s^2 = \Delta t^2$.

Combine the conclusion with **the sign of $\Delta s^2$**. Since the interval is invariant, so is its sign, and the sign is the [[Def - Classification of Four-Vectors|causal classification]] — timelike, spacelike, null. The further result is that causal structure is observer-independent: all observers agree on whether two events can influence each other. The combination is nonobvious because the *time order* of events is frame-dependent, yet the *causal class* is not — the invariance of the sign is exactly what reconciles these. *Example:* [[Ex - Causal structure and the light cone]].

Combine the conclusion with **two events both on a light ray**. For such events $\Delta s^2 = 0$, and invariance forces $\Delta s^2 = 0$ in every frame, i.e. they lie on a light ray in every frame. The further result is the constancy of the speed of light, recovered as a *theorem* rather than a postulate. The combination closes the logical loop: the postulates imply the interval is invariant, and the invariance of the interval implies the postulate about light.

---

# Why Is It True

The deep reason is the rotation analogy, and it is worth taking slowly.

Picture first the Euclidean situation. Two points in a plane are separated by $(\Delta x, \Delta y)$. Rotate the coordinate axes: the separation becomes $(\Delta x', \Delta y')$, two different numbers. But the distance $\Delta x^2 + \Delta y^2$ is unchanged, because a rotation is *defined* to be a linear map that preserves it. The two coordinates trade their values back and forth — one grows as the other shrinks — in exactly the way that keeps the sum of squares fixed. $\cos^2\theta + \sin^2\theta = 1$ is the bookkeeping that makes this work.

Now the Minkowski situation. Two events are separated by $(\Delta t, \Delta x)$. A boost is, structurally, a "rotation" mixing the time axis into the space axis. It changes $\Delta t$ and $\Delta x$ separately — that is time dilation and length contraction. But it is the *kind* of mixing that keeps a particular quadratic combination fixed, and one should expect such a combination to exist for the same reason it exists for rotations: a boost is a one-parameter family of linear maps, the identity is in the family, and a family like that generically preserves some quadratic form. The only question is *which* form, and the answer is dictated by the one physical input — the constancy of light.

Here is the cleanest way to see *which* form, without any algebra. A light ray has $\Delta s^2 = \Delta t^2 - \Delta x^2 = 0$ in $S$. By the second postulate it is still a light ray in $S'$, so $\Delta t'^2 - \Delta x'^2 = 0$ there too. Thus the boost maps the cone $\Delta s^2 = 0$ to itself. Now, a linear map that preserves a quadratic form's *zero set* must multiply the form by a scalar: $\Delta s'^2 = \kappa(v)\,\Delta s^2$ for some factor $\kappa$ depending on the velocity. (A linear change of variables sends a quadratic form to another quadratic form with the same zero locus; two quadratic forms in two variables with the same zero locus are proportional.) Finally $\kappa$ must equal $1$: by the principle of relativity the relation between $S$ and $S'$ is symmetric, so applying the boost and then its inverse gives $\kappa(v)\kappa(-v) = 1$; and $\kappa$ depends only on $|v|$, so $\kappa(v) = \kappa(-v)$, forcing $\kappa^2 = 1$ and $\kappa = +1$ (it is $+1$, not $-1$, since $\kappa = 1$ at $v = 0$). Hence $\Delta s'^2 = \Delta s^2$.

So the chain of intuition is: a boost is a rotation, hence preserves *some* quadratic form; the constancy of light forces that form to have the light cone as its zero set, which pins it to $\Delta t^2 - \Delta x^2$ up to scale; and the relativity principle's left–right symmetry kills the scale. The minus sign — the whole of Minkowski geometry — enters because the invariant zero set is a *cone* ($\Delta t = \pm\Delta x$), not the single point $\Delta x = \Delta y = 0$ of the Euclidean case.

---

# What Makes This Hard

The direct proof is a short algebraic substitution, and the place people stumble is not the algebra but believing it: the cross term $\Delta t\,\Delta x$, which is present in both $\Delta t'^2$ and $\Delta x'^2$, must cancel *exactly* between them, and it is easy to drop a sign and conclude the interval is not invariant. The non-obvious conceptual step is the converse direction — recognising that interval-preservation does not merely follow from being a Lorentz transformation but *characterises* it — and the most common error there is to forget the scale factor $\kappa$ in the "preserves the light cone" argument and assume the cone determines the form outright rather than up to a positive multiple.

---

# Rederivation Scaffold

**High-level strategy:**
Substitute the boost formulas $\Delta t' = \gamma(\Delta t - v\Delta x)$, $\Delta x' = \gamma(\Delta x - v\Delta t)$ directly into $\Delta t'^2 - \Delta x'^2$, expand, watch the cross terms cancel, and collect using $\gamma^2(1-v^2) = 1$. The $y, z$ directions are untouched and contribute trivially.

**Subgoal decomposition:**

1. **Reduce to $1+1$ dimensions.** Show the $y, z$ contribution is automatically invariant, so only $\Delta t^2 - \Delta x^2$ need be checked.
   - *Hint:* The boost has $\Delta y' = \Delta y$, $\Delta z' = \Delta z$.
   - *Why needed:* It isolates the one nontrivial computation.

2. **Expand the two squares.** Compute $\Delta t'^2 = \gamma^2(\Delta t - v\Delta x)^2$ and $\Delta x'^2 = \gamma^2(\Delta x - v\Delta t)^2$.
   - *Hint:* Each is $\gamma^2$ times a perfect square; write out all three terms of each.
   - *Why needed:* It exposes the cross terms that must cancel.

3. **Subtract and cancel the cross terms.** Form $\Delta t'^2 - \Delta x'^2$; the $-2v\,\Delta t\,\Delta x$ terms cancel.
   - *Hint:* Both squares contain $\mp 2v\gamma^2\Delta t\Delta x$; with the overall minus sign on $\Delta x'^2$ they cancel.
   - *Why needed:* Cancellation of the cross term is the heart of the proof.

4. **Collect with $\gamma^2(1-v^2) = 1$.** What remains is $\gamma^2(1-v^2)\Delta t^2 - \gamma^2(1-v^2)\Delta x^2 = \Delta t^2 - \Delta x^2$.
   - *Hint:* $\gamma^2 = (1-v^2)^{-1}$, so $\gamma^2(1-v^2) = 1$.
   - *Why needed:* It is the final identification with the unprimed interval.

---

# Lemma Decomposition

> [!note]- Lemma 1: The transverse directions are invariant
> **Statement:** Under a boost along $x$, $\Delta y' = \Delta y$ and $\Delta z' = \Delta z$, so $\Delta y'^2 + \Delta z'^2 = \Delta y^2 + \Delta z^2$.
>
> **Hint:** This is immediate from the form of the boost.
>
> **Why needed:** It reduces the theorem to the $(t,x)$-plane, where the only real computation lives.
>
> > [!note]- Full proof
> > The standard Lorentz boost along the $x$-axis acts as $y' = y$, $z' = z$ (see [[Def - The Lorentz Transformation]]); transverse directions are untouched. Hence the differences satisfy $\Delta y' = \Delta y$ and $\Delta z' = \Delta z$, and squaring and adding gives $\Delta y'^2 + \Delta z'^2 = \Delta y^2 + \Delta z^2$. $\blacksquare$

> [!note]- Lemma 2: The $(1+1)$-dimensional interval is invariant
> **Statement:** With $\Delta t' = \gamma(\Delta t - v\Delta x)$ and $\Delta x' = \gamma(\Delta x - v\Delta t)$, one has $\Delta t'^2 - \Delta x'^2 = \Delta t^2 - \Delta x^2$.
>
> **Hint:** Expand both squares; the cross terms cancel; use $\gamma^2(1-v^2)=1$.
>
> **Why needed:** This is the whole content of the theorem in $1+1$ dimensions; with Lemma 1 it gives the full result.
>
> > [!note]- Full proof
> > Expand:
> > $$\Delta t'^2 = \gamma^2\big(\Delta t^2 - 2v\,\Delta t\,\Delta x + v^2\Delta x^2\big),$$
> > $$\Delta x'^2 = \gamma^2\big(\Delta x^2 - 2v\,\Delta x\,\Delta t + v^2\Delta t^2\big).$$
> > Subtract:
> > $$\Delta t'^2 - \Delta x'^2 = \gamma^2\Big[\Delta t^2 - 2v\Delta t\Delta x + v^2\Delta x^2 - \Delta x^2 + 2v\Delta x\Delta t - v^2\Delta t^2\Big].$$
> > The two cross terms $-2v\Delta t\Delta x$ and $+2v\Delta x\Delta t$ cancel. Grouping the rest by $\Delta t^2$ and $\Delta x^2$:
> > $$\Delta t'^2 - \Delta x'^2 = \gamma^2\Big[(1 - v^2)\Delta t^2 - (1 - v^2)\Delta x^2\Big] = \gamma^2(1-v^2)\big(\Delta t^2 - \Delta x^2\big).$$
> > Since $\gamma^2 = (1-v^2)^{-1}$, the factor $\gamma^2(1-v^2) = 1$, leaving $\Delta t'^2 - \Delta x'^2 = \Delta t^2 - \Delta x^2$. $\blacksquare$

> [!note]- Lemma 3: Interval-preservation characterises the Lorentz transformations
> **Statement:** A linear map of spacetime that preserves $\Delta s^2$ for every pair of events satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$, hence is a Lorentz transformation.
>
> **Hint:** Write $\Delta s^2 = \Delta X^{\mathsf T}\eta\,\Delta X$ and demand equality for all $\Delta X$.
>
> **Why needed:** It is the converse half of the theorem and the bridge to the group-theoretic definition of §1.2.
>
> > [!note]- Full proof
> > Write the separation as a column vector $\Delta X$ and the interval as the quadratic form $\Delta s^2 = \Delta X^{\mathsf T}\eta\,\Delta X$, with $\eta = \mathrm{diag}(1,-1,-1,-1)$. A linear map $\Delta X' = \Lambda\,\Delta X$ preserves the interval iff
> > $$\Delta X^{\mathsf T}\eta\,\Delta X = \Delta X'^{\mathsf T}\eta\,\Delta X' = (\Lambda\Delta X)^{\mathsf T}\eta\,(\Lambda\Delta X) = \Delta X^{\mathsf T}\big(\Lambda^{\mathsf T}\eta\,\Lambda\big)\Delta X$$
> > for *every* $\Delta X$. A symmetric bilinear form is determined by its quadratic form (polarisation), so this holds for all $\Delta X$ iff $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. That equation is precisely the defining condition of a [[Def - The Lorentz Group|Lorentz transformation]]. (Allowing also a constant shift $\Delta X \mapsto \Lambda\Delta X$ of the events themselves accounts for translations, giving the full Poincaré group.) $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Consider two events with separation $(\Delta t, \Delta x, \Delta y, \Delta z)$ in $S$ and $(\Delta t', \Delta x', \Delta y', \Delta z')$ in $S'$, where $S'$ moves at velocity $v$ along the $x$-axis of $S$. By the [[Def - The Lorentz Transformation|Lorentz transformation]], applied to the (linear, hence difference-respecting) coordinate change,
> $$\Delta t' = \gamma(\Delta t - v\Delta x), \quad \Delta x' = \gamma(\Delta x - v\Delta t), \quad \Delta y' = \Delta y, \quad \Delta z' = \Delta z,$$
> with $\gamma = (1-v^2)^{-1/2}$.
>
> By Lemma 1, $\Delta y'^2 + \Delta z'^2 = \Delta y^2 + \Delta z^2$.
>
> By Lemma 2,
> $$\Delta t'^2 - \Delta x'^2 = \gamma^2(1-v^2)(\Delta t^2 - \Delta x^2) = \Delta t^2 - \Delta x^2,$$
> using $\gamma^2(1-v^2) = 1$.
>
> Adding,
> $$\Delta s'^2 = \Delta t'^2 - \Delta x'^2 - \Delta y'^2 - \Delta z'^2 = (\Delta t^2 - \Delta x^2) - (\Delta y^2 + \Delta z^2) = \Delta s^2.$$
> A general Lorentz transformation is a composition of such boosts with spatial rotations; rotations preserve $\Delta x^2 + \Delta y^2 + \Delta z^2$ and fix $\Delta t$, hence preserve $\Delta s^2$, and a composition of interval-preserving maps preserves the interval. Therefore $\Delta s^2$ is invariant under every Lorentz transformation.
>
> For the converse, Lemma 3 shows that any linear map preserving $\Delta s^2$ for all separations satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$, the defining condition of a Lorentz transformation; allowing constant shifts of the events gives the Poincaré transformations. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The invariant mass of a composite particle.** In relativistic kinematics the total [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$ of a system has $P\cdot P = M^2$ with $M$ the system's invariant mass. Computing $P\cdot P$ in one frame and equating to its value in the centre-of-momentum frame is the interval-invariance theorem applied to a four-momentum rather than a separation; see [[Ex - The invariant mass of a system of particles]]. The application is nonobvious because "mass" does not look like a "spacetime interval" until one sees that both are Minkowski norms.

**Conservation laws survive Lorentz boosts.** If total four-momentum is conserved in one inertial frame, it is conserved in all — because the *difference* of total four-momenta before and after is a four-vector, and a four-vector that is zero in one frame is zero in all (its norm and all components vanish, an instance of interval/norm invariance). The application is out-of-distribution because conservation is usually argued dynamically, yet here it is pure invariance.

**Hyperbolic geometry and the velocity space.** The set of physical four-velocities, all with $V\cdot V = c^2$, is one sheet of a hyperboloid — a model of three-dimensional hyperbolic space, and the Lorentz group acts on it as the isometry group. The invariance of $V\cdot V$ is the invariance of the interval restricted to that hyperboloid. The application is surprising because it connects relativity to pure non-Euclidean geometry: rapidity is hyperbolic distance.

---

# Bridges

- **[[Def - The Lorentz Group]]** — the converse half of this theorem *is* the definition of the Lorentz group: the interval-preserving linear maps are exactly $O(1,3)$. This theorem is the bridge from the postulate-based §1.1 to the group-based §1.2.

- **[[Def - Four-Vector]]** — the interval is the norm-squared of the separation four-vector, and this theorem, generalised, says *every* four-vector inner product $X\cdot Y$ is Lorentz invariant. Interval invariance is the prototype of four-vector invariance.

- **Euclidean rotations preserve distance** — the exact analogue: $O(3)$ is defined by preserving $\Delta x^2 + \Delta y^2 + \Delta z^2$, as $O(1,3)$ is defined by preserving $\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$. The proof structure (quadratic form, $\Lambda^{\mathsf T}\eta\Lambda = \eta$) is identical with $\eta$ replaced by the identity.

- **[[Thm - The Reversed Triangle Inequality]]** — the geometry the invariant interval supports; the reversed triangle inequality is a theorem *about* the interval, the way the ordinary triangle inequality is a theorem about Euclidean distance.

---

# Unlocked by This

> [!tip] Proper Time as an Invariant *(from Relativistic Kinematics)*
> Because the infinitesimal interval $ds$ is frame-independent, its integral along a worldline — the **proper time** ([[Def - Proper Time]]) — is a genuine invariant, the time a clock actually accumulates. Four-velocity and four-acceleration are then defined by differentiating with respect to this invariant parameter.

> [!tip] Lorentz Invariance as a Design Principle *(from QFT and Gauge Theory)*
> The demand that a physical law be unchanged under all Lorentz transformations — **Lorentz invariance** — is the central constraint in building relativistic field theories. Every term in a Lagrangian must be a Lorentz scalar, built by contracting four-vectors and tensors so that all interval-like quantities are invariant.
