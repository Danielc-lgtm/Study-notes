---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Inertial Observer"
  - "Def - Observer and Local Rest Space"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\mathcal{O}$ is an [[Def - Inertial Observer|inertial observer]] of worldline $\mathscr{L}$, constant four-velocity $U$ ($U\cdot U = 1$), and proper time $t$. The event of $\mathscr{L}$ at proper time $t$ is $O(t)$. The **local rest space** $\mathscr{E}_u(t)$ is the hyperplane through $O(t)$ orthogonal to $U$ (the set of displacements $X$ from $O(t)$ with $X \cdot U = 0$); the **simultaneity hypersurface** $\Sigma_u(t)$ is the set of events Einstein–Poincaré simultaneous to $O(t)$ for $\mathcal{O}$. See [[Def - Observer and Local Rest Space]]. Full registry on [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

---

# Statement

> **Globality of the rest space for an inertial observer.** Let $\mathcal{O}$ be an inertial observer with constant four-velocity $U$. Then at every proper time $t$ the simultaneity hypersurface coincides with the local rest space,
> $$\Sigma_u(t) = \mathscr{E}_u(t),$$
> and these hyperplanes are mutually **parallel** for different $t$, hence pairwise disjoint:
> $$\mathscr{E}_u(t_1) \cap \mathscr{E}_u(t_2) = \varnothing \quad\text{for } t_1 \neq t_2.$$
> Consequently the family $\{\mathscr{E}_u(t)\}_{t\in\mathbb{R}}$ foliates the whole of Minkowski spacetime $\mathscr{E}$, the rest space and frame are **global** objects (the qualifier "local" may be dropped), and the observer's coordinates
> $$\overrightarrow{O(0)M} = ct\,U + x^i e_i, \qquad (ct, x^1, x^2, x^3),$$
> form a global affine (inertial) coordinate system on $\mathscr{E}$, centred at $O(0)$.

---

# Motivation

For a *general* observer the rest space is an irreducibly *local* object. The hyperplane orthogonal to the four-velocity at one event is the observer's instantaneous "space", but as the observer accelerates this hyperplane tilts from event to event, and two such hyperplanes at different proper times generically *intersect* — the observer's notion of "now here" and "now there" become inconsistent at a distance. Worse, the simultaneity hypersurface (the events the observer actually judges simultaneous, by exchanging light signals) and the local rest space (the geometric orthogonal hyperplane) need not even coincide for an accelerated observer; they are tangent at the observer but curve apart away from the worldline. This is why, for an accelerated observer, one cannot in general build a single global spatial coordinate grid — the local rest spaces refuse to stack up into a foliation.

The theorem says that for an *inertial* observer all of these obstructions vanish at once. The simultaneity hypersurface and the rest space coincide everywhere; the rest spaces at different times are parallel and never meet; and they stack into a clean foliation of all of spacetime by parallel hyperplanes. This is exactly what licenses the Newtonian picture — within a single inertial frame — of one universal "now" sweeping uniformly through space, and it is what makes the global inertial coordinate system $(ct, x^i)$ exist. The theorem is the precise statement of what is special about inertial observers among all observers: not merely that their worldlines are straight, but that their *space* is global.

The result matters because it is the foundation of every coordinate computation in special relativity. When one writes "the coordinates of event $M$ in frame $S$", one is using the global inertial chart whose existence this theorem guarantees. It also marks, by its failure, the entry of gravity: in a curved spacetime the freely-falling (locally inertial) observer recovers this picture only along a single worldline, to first order, and the global foliation does not exist — that failure *is* the gravitational field.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "$\mathcal{O}$ is inertial", i.e. $U$ is constant. The point of input broadening is to recognise the disguises of that hypothesis.

The first disguised source is **"the observer's four-acceleration vanishes"**. Vanishing four-acceleration, $a = \mathrm{d}U/\mathrm{d}\tau = 0$, *is* the constancy of $U$, which is the only input the theorem actually uses (the four-rotation $\omega$ plays no role in the globality of the rest space — it concerns the spatial frame, not the hyperplane). So even a non-inertial observer with $a = 0$ but $\omega \neq 0$ has global, parallel rest spaces; the theorem's geometric conclusion needs only straightness of the worldline. The bridge is that the rest space depends on $U$ alone, not on the spatial triad. *Example problem:* show that an unaccelerated but spinning observer still has a global rest space, even though its frame is not inertial.

The second disguised source is **"the worldline is a straight line of $\mathscr{E}$"**. A straight worldline has constant tangent, hence constant $U$ up to normalisation. So any problem that hands you a straight timelike worldline, however described — as a solution of $\ddot{x}^\alpha = 0$, as the orbit of a translation subgroup, as a geodesic of flat spacetime — supplies the hypothesis. The bridge is the integration $\mathrm{d}U/\mathrm{d}\tau = 0 \Rightarrow x^\alpha = U^\alpha\tau + x_0^\alpha$. *Example problem:* given that a particle's worldline satisfies the free equation of motion, conclude its rest spaces foliate spacetime.

The third disguised source is **"two events are simultaneous for an inertial observer"**. Because $\Sigma_u(t) = \mathscr{E}_u(t)$, "simultaneous for $\mathcal{O}$" is equivalent to "lying in a common hyperplane orthogonal to $U$", a purely geometric condition $X \cdot U = \mathrm{const}$. So a hypothesis phrased in terms of the observer's simultaneity judgments can be converted to the orthogonality condition. The bridge is the coincidence of the two hypersurfaces, which is the first half of the theorem. *Example problem:* characterise the locus of events an inertial observer calls simultaneous to a given event as the level set $U \cdot \overrightarrow{O(0)M} = ct$.

**Targets (Output Amplification)**

The conclusion is "the rest spaces are global, parallel, and foliate $\mathscr{E}$".

Combine the conclusion with **the constancy of the spatial frame**. An inertial observer carries a constant triad $(e_i)$, and laying it down at each event of the foliation produces a global field of spatial axes. The further result is the full global inertial coordinate system $(ct, x^i)$: not just a foliation by "nows" but a complete affine chart with time and space coordinates. The combination is what turns the geometric foliation into a usable coordinate grid. *Example:* every coordinate computation of special relativity uses this chart.

Combine the conclusion with **a second inertial observer in relative motion**. The second observer has its *own* global foliation, by hyperplanes orthogonal to its (different) four-velocity $U'$. The two foliations are *not* parallel to each other — they intersect at an angle set by the relative velocity — and the further result is the relativity of simultaneity: the two observers' "nows" are different slicings of the same spacetime. The combination is the geometric origin of all the disagreement-about-simultaneity phenomena. *Example:* two inertial frames disagree on which events are simultaneous precisely because their global foliations are tilted relative to one another.

Combine the conclusion with **the failure of parallelism for accelerated observers**. An accelerated observer's rest spaces are *not* parallel and *do* intersect (forming a caustic, the Rindler horizon for uniform acceleration). The further result, by contrast, sharpens what is special about the inertial case and previews the coordinate breakdown of accelerated frames. The combination is the bridge to the accelerated-observer chapter. *Example:* the Rindler coordinate system covers only a wedge of spacetime because the accelerated rest spaces pivot about a common edge.

---

# Why Is It True

There are two things to see, and both are consequences of a single fact: the four-velocity is *constant*.

First, why the simultaneity hypersurface coincides with the rest space. For a general observer these differ because of the *curvature* of the worldline: the events the observer judges simultaneous (by the Einstein–Poincaré radar procedure) lie on a hypersurface that is tangent to the orthogonal rest space at the observer's location but bends away from it, and the bending is controlled by how fast the four-velocity is turning — by the four-acceleration. When the worldline is straight the four-velocity does not turn, there is no bending, and the simultaneity hypersurface *is* the flat orthogonal hyperplane. The radar definition and the geometric definition give the same hyperplane precisely because there is no acceleration to make them diverge. **The gap between "simultaneous" and "orthogonal" is curvature of the worldline, and a straight worldline has none.**

Second, why the hyperplanes at different times are parallel. The rest space at proper time $t$ is the set of points $M$ with $\overrightarrow{O(t)M} \cdot U = 0$ — the hyperplane through $O(t)$ with normal $U$. The normal $U$ is the *same vector* at every $t$, because $U$ is constant. Two hyperplanes with the same normal vector are parallel by definition. And as $t$ varies, $O(t) = O(0) + ct\,U$ slides *along* the normal direction $U$, so the hyperplanes are successive parallel translates, stacked along $U$ like the pages of a book — they never intersect, and they sweep out all of spacetime exactly once. The whole picture is: a single hyperplane shape, translated uniformly along its own normal. Contrast an accelerated observer, whose normal $U(t)$ rotates as $t$ varies, so the hyperplanes pivot and cross.

The deeper unifying point is that *both* facts come from $U = \mathrm{const}$. Constancy of $U$ kills the curvature (giving coincidence of the hypersurfaces) and fixes the normal direction (giving parallelism). The whole theorem is the geometric content of "the four-velocity is one fixed vector": a fixed normal vector slid along itself foliates the affine space by parallel hyperplanes, and that foliation is the global space of the inertial observer.

---

# What Makes This Hard

The conceptual hurdle is appreciating that the result is *special* — that it genuinely fails for accelerated observers, and that the failure is not a coordinate artifact but a real geometric obstruction (intersecting rest spaces, a horizon). Most people, schooled on the single global inertial frame, take the global foliation for granted and miss that it is a theorem requiring the constancy of $U$. The non-obvious step is recognising that *two distinct things* are being asserted — coincidence of simultaneity with orthogonality, and parallelism across times — and that both, though they look like one statement, are separate consequences of straightness. The common error is to conflate them or to assume parallelism is automatic for any observer; it is not, and the accelerated observer is the counterexample to keep in mind.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the constancy of $U$ twice. Write the rest space at time $t$ as the hyperplane through $O(t)$ with normal $U$; since $U$ is constant the normal is the same for all $t$, giving parallelism, and since the worldline slides along $U$ the hyperplanes are translates that tile $\mathscr{E}$. For the coincidence of simultaneity and rest space, invoke that the difference between them is induced by the worldline's curvature, which vanishes for a straight line.

**Subgoal decomposition:**

1. **Coincidence $\Sigma_u(t) = \mathscr{E}_u(t)$.** Show the simultaneity hypersurface equals the orthogonal hyperplane.
   - *Hint:* The difference between the two is controlled by the four-acceleration; for $a = 0$ it vanishes, so the radar-simultaneous events are exactly the orthogonal ones.
   - *Why needed:* It identifies the observer's "space" with a flat hyperplane, the object whose parallelism we then prove.

2. **The hyperplanes have a common normal.** Show $\mathscr{E}_u(t) = \{M : \overrightarrow{O(t)M}\cdot U = 0\}$ with $U$ independent of $t$.
   - *Hint:* $U$ is constant for an inertial observer; the rest space is by definition the orthogonal complement of $U$.
   - *Why needed:* Common normal $\Rightarrow$ parallel hyperplanes.

3. **The hyperplanes are translates along $U$, hence disjoint and space-filling.** Show $O(t) = O(0) + ct\,U$ and that the level sets $U\cdot\overrightarrow{O(0)M} = ct$ partition $\mathscr{E}$.
   - *Hint:* The function $M \mapsto U\cdot\overrightarrow{O(0)M}$ is a non-constant affine function (since $U \neq 0$), so its level sets are parallel hyperplanes foliating $\mathscr{E}$, one for each value $ct \in \mathbb{R}$.
   - *Why needed:* It is the foliation statement and gives the global time coordinate.

4. **Assemble the global chart.** Lay the constant triad $(e_i)$ on each leaf to get $(ct, x^i)$.
   - *Hint:* $\overrightarrow{O(0)M} = ct\,U + x^i e_i$ with $ct = U\cdot\overrightarrow{O(0)M}$ and $x^i$ the components along the constant spatial axes.
   - *Why needed:* It produces the global inertial coordinate system, the usable output.

---

# Lemma Decomposition

> [!note]- Lemma 1: Simultaneity equals orthogonality for a straight worldline
> **Statement:** For an inertial observer, $\Sigma_u(t) = \mathscr{E}_u(t)$: the events Einstein–Poincaré simultaneous to $O(t)$ are exactly those in the hyperplane through $O(t)$ orthogonal to $U$.
>
> **Hint:** The discrepancy between the simultaneity hypersurface and the orthogonal rest space is induced by the curvature (four-acceleration) of the worldline; a straight worldline has none.
>
> **Why needed:** It identifies the observer's physical "now" with a flat geometric hyperplane, which is the object whose parallelism Lemmas 2–3 establish.
>
> > [!note]- Full proof
> > The Einstein–Poincaré simultaneity hypersurface $\Sigma_u(t)$ is constructed by the radar procedure: $M \in \Sigma_u(t)$ if a light signal sent from the worldline at proper time $t - \delta$ reaches $M$ and returns at $t + \delta$, so that $\mathcal{O}$ assigns $M$ the time $t$. For a general observer this hypersurface is tangent at $O(t)$ to the orthogonal hyperplane $\mathscr{E}_u(t) = \{M : \overrightarrow{O(t)M}\cdot U = 0\}$ but deviates from it at second order, the deviation being governed by the worldline's four-acceleration $a$ (this is the content of the simultaneity analysis of [[Def - Observer and Local Rest Space]]: the two hypersurfaces share their tangent hyperplane at $O(t)$, and their difference is induced by the curvature of $\mathscr{L}$). For an inertial observer $a = 0$, so the worldline is straight and there is no curvature to produce a deviation: the radar-simultaneous events coincide with the orthogonal ones at all distances, $\Sigma_u(t) = \mathscr{E}_u(t)$, even for events arbitrarily far from $\mathscr{L}$. $\blacksquare$

> [!note]- Lemma 2: The rest-space hyperplanes share a common normal
> **Statement:** For an inertial observer, every rest space is a hyperplane with normal vector $U$, the same vector for all $t$: $\mathscr{E}_u(t) = \{M : \overrightarrow{O(t)M}\cdot U = 0\}$ with $U$ constant.
>
> **Hint:** Use $a = 0 \Rightarrow U$ constant, and the definition of the rest space as $U^\perp$.
>
> **Why needed:** Two hyperplanes with the same normal are parallel; this is the parallelism statement.
>
> > [!note]- Full proof
> > By [[Def - Inertial Observer|inertiality]], $a = \mathrm{d}U/\mathrm{d}\tau = 0$, so $U(t) = U$ is one fixed vector of the displacement space $E$, independent of $t$. The local rest space at proper time $t$ is by definition the orthogonal complement of $U$ through $O(t)$: $\mathscr{E}_u(t) = \{M \in \mathscr{E} : \overrightarrow{O(t)M}\cdot U = 0\}$. Since $U$ is the same for every $t$, all these hyperplanes have the *same* normal direction. Two affine hyperplanes with a common normal vector are parallel. $\blacksquare$

> [!note]- Lemma 3: The hyperplanes are level sets of one affine function, foliating spacetime
> **Statement:** The function $\phi(M) = U\cdot\overrightarrow{O(0)M}$ is affine and non-constant, its level set $\{\phi = ct\}$ is exactly $\mathscr{E}_u(t)$, and the level sets partition $\mathscr{E}$ into parallel disjoint hyperplanes, one for each $ct \in \mathbb{R}$.
>
> **Hint:** $O(t) = O(0) + ct\,U$ and $U\cdot U = 1$, so $\phi(O(t)) = ct$; a non-constant affine function on an affine space has parallel hyperplanes as level sets, foliating the space.
>
> **Why needed:** This is the global-foliation conclusion and supplies the global time coordinate $ct = \phi$.
>
> > [!note]- Full proof
> > Fix the origin $O(0)$ and define $\phi : \mathscr{E} \to \mathbb{R}$ by $\phi(M) = U\cdot\overrightarrow{O(0)M}$. This is an affine function (linear in the displacement $\overrightarrow{O(0)M}$), and it is non-constant because $U \neq 0$. The worldline event at proper time $t$ is $O(t) = O(0) + ct\,U$ (the straight-line worldline, [[Def - Inertial Observer]]), so $\phi(O(t)) = U\cdot(ct\,U) = ct\,(U\cdot U) = ct$ using $U\cdot U = 1$. For $M \in \mathscr{E}_u(t)$ we have $\overrightarrow{O(t)M}\cdot U = 0$, i.e. $\overrightarrow{O(0)M}\cdot U = \overrightarrow{O(0)O(t)}\cdot U = ct$, so $\phi(M) = ct$; conversely $\phi(M) = ct$ gives $\overrightarrow{O(t)M}\cdot U = 0$. Hence $\mathscr{E}_u(t) = \{\phi = ct\}$. The level sets of a non-constant affine function are parallel affine hyperplanes, pairwise disjoint and covering $\mathscr{E}$ (every $M$ has exactly one value $\phi(M) = ct$). Therefore $\{\mathscr{E}_u(t)\}_{t\in\mathbb{R}}$ foliates $\mathscr{E}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{O}$ be an [[Def - Inertial Observer|inertial observer]], so its four-velocity $U$ is constant ($a = \mathrm{d}U/\mathrm{d}\tau = 0$) and $U\cdot U = 1$, and its worldline is the straight line $O(t) = O(0) + ct\,U$.
>
> *Coincidence.* By Lemma 1, since the worldline is straight (zero four-acceleration), the Einstein–Poincaré simultaneity hypersurface coincides with the orthogonal rest space at every proper time: $\Sigma_u(t) = \mathscr{E}_u(t)$.
>
> *Parallelism.* By Lemma 2, every $\mathscr{E}_u(t) = \{M : \overrightarrow{O(t)M}\cdot U = 0\}$ is a hyperplane with the *same* normal $U$ (constant), so the hyperplanes for different $t$ are mutually parallel.
>
> *Foliation.* By Lemma 3, defining $\phi(M) = U\cdot\overrightarrow{O(0)M}$, one has $\mathscr{E}_u(t) = \{\phi = ct\}$, and the level sets of this non-constant affine function partition $\mathscr{E}$ into parallel disjoint hyperplanes, one per value $ct \in \mathbb{R}$. In particular $\mathscr{E}_u(t_1)\cap\mathscr{E}_u(t_2) = \varnothing$ for $t_1 \neq t_2$, and $\bigcup_t \mathscr{E}_u(t) = \mathscr{E}$.
>
> *Global chart.* Lay the constant spatial triad $(e_1, e_2, e_3)$ (which exists because the frame is constant) along each leaf. Any event $M$ has a unique decomposition
> $$\overrightarrow{O(0)M} = ct\,U + x^i e_i, \qquad ct = \phi(M) = U\cdot\overrightarrow{O(0)M},\quad x^i = -\,e_i\cdot\overrightarrow{O(0)M}$$
> (the sign from $e_i\cdot e_i = -1$ in mostly-minus), giving a global affine coordinate system $(ct, x^1, x^2, x^3)$ on all of $\mathscr{E}$, centred at $O(0)$. Since this chart is global, the qualifier "local" may be dropped: the rest space and frame of an inertial observer are global. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Foliations of manifolds by level sets (differential geometry).** The statement "the level sets of a non-constant affine function foliate the affine space by parallel hyperplanes" is the flat, trivial case of the general theory of foliations by submersions: a submersion $\phi : M \to \mathbb{R}$ foliates $M$ by the connected components of its level sets, and the leaves are codimension-one submanifolds. The inertial observer's time function $\phi(M) = U\cdot\overrightarrow{O(0)M}$ is the simplest such submersion. The application is nonobvious because the relativistic "global time" of an inertial frame is, structurally, just a foliation by a level function — and in curved spacetime the obstruction to such a global time function is exactly what makes the chronology and causal structure subtle.

**Parallel hyperplanes and the kernel of a linear functional (linear algebra).** The rest spaces are the affine translates of the single linear hyperplane $U^\perp = \ker(X \mapsto U\cdot X)$. That a linear functional partitions a vector space into parallel affine hyperplanes (its level sets) is a basic linear-algebra fact, here carrying the physical meaning of "the inertial observer's family of simultaneous-event surfaces". The application illuminates why the relativity of simultaneity is geometric: a second observer's functional $U'\cdot X$ has a *different* kernel, so a different family of parallel hyperplanes, tilted relative to the first.

**Geodesic foliations and the failure of global time in general relativity.** In general relativity a freely-falling observer's local rest spaces foliate spacetime globally only in special (e.g. static or homogeneous) cases; generically the geodesic congruence has nonzero shear, expansion, or vorticity, and no global synchronous foliation exists. The flat-spacetime theorem here is the baseline against which those obstructions are measured: the inertial observer's congruence is shear-free, expansion-free, and vorticity-free, the unique maximally trivial case. The application is surprising because it shows that the existence of a global "now" — taken for granted in special relativity — is a fragile, curvature-sensitive property.

---

# Bridges

- **[[Def - Inertial Observer]]** — this theorem is the payoff of the definition: the property that genuinely distinguishes inertial observers among all observers is not the straightness of the worldline (which only encodes $a = 0$) but the *globality of the rest space*, which this theorem derives from the constancy of $U$. The definition supplies the hypothesis; the theorem supplies the structural consequence that makes inertial frames usable.

- **[[Def - Rigid Array of Inertial Observers]]** — the global foliation established here is exactly what allows a rigid array of inertial observers to be synchronised: the array's clocks all read the same value on each leaf $\mathscr{E}_u(t)$, and the leaves never intersect, so the synchronisation is globally consistent. Without parallelism the synchronisation would be obstructed, as it is for rotating arrays.

- **The relativity of simultaneity** — a second inertial observer in relative motion has its own global foliation by hyperplanes orthogonal to its four-velocity $U'$. These are *not* parallel to the first observer's leaves (the normals $U$ and $U'$ differ), so the two foliations are tilted, and that tilt is the geometric origin of the relativity of simultaneity: the two observers slice spacetime into different families of "nows". This theorem, applied to each observer separately, is what makes the disagreement precise.

- **Accelerated observers and the Rindler horizon** — the theorem fails for accelerated observers, and its failure is informative: when $U$ is not constant, the normal $U(t)$ rotates, the rest-space hyperplanes pivot rather than translate, and they intersect along a caustic. For uniform acceleration the caustic is the **Rindler horizon**, and the accelerated coordinate system covers only the wedge of spacetime where the pivoting hyperplanes do not yet cross. This is the bridge to the accelerated-observer chapter, where the loss of globality is the central phenomenon.

---

# Unlocked by This

> [!tip] Global Inertial Coordinates and the Change of Frame *(from §12.2)*
> The global chart $(ct, x^i)$ established here is the inertial coordinate system used throughout special relativity, and the relation between two such charts — for two inertial observers — is the passive [[Def - The Poincaré Group|Poincaré transformation]] $x'^\alpha = \Lambda^\alpha{}_\beta x^\beta + x_0'^\alpha$.

> [!tip] The Equivalence Principle and the Local-Only Inertial Frame *(from General Relativity)*
> In a curved spacetime this theorem holds only *locally*: a freely-falling observer's rest space coincides with its simultaneity surface and foliates a neighbourhood, but the foliation cannot in general be extended globally — neighbouring freely-falling worldlines converge or diverge (geodesic deviation), tilting the rest spaces relative to one another. The obstruction to the global foliation is the **Riemann curvature tensor**, and its presence is the invariant signature of a gravitational field. The global inertial frame of special relativity is the one luxury that curvature removes. See [[General Relativity I — Einstein's Equations and Schwarzschild]].
