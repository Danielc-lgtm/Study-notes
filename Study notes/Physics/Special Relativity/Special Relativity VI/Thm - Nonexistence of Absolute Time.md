---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Observer and Local Rest Space"
  - "Def - Einstein-Poincaré Simultaneity"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(+1,-1,-1,-1)$. Observers $\mathcal{O}$ and $\mathcal{O}'$ have [[Def - Four-Velocity and Four-Acceleration|four-velocities]] $U_0$ and $U_0'$ ($U_0\cdot U_0 = U_0'\cdot U_0' = +1$, both future-directed). Their [[Def - Observer and Local Rest Space|local rest spaces]] at a common event $O$ are $E_{U_0} = U_0^\perp$ and $E_{U_0'} = U_0'^\perp$. [[Def - Einstein-Poincaré Simultaneity|Simultaneity for 𝒪]] means orthogonality to $U_0$. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

---

# Statement

> **Nonexistence of absolute time.** Let $\mathcal{O}$ and $\mathcal{O}'$ be two observers whose worldlines cross at an event $O$, with four-velocities $U_0\neq U_0'$. Then their local rest spaces at $O$ are different,
> $$U_0^\perp \;\neq\; U_0'^\perp,$$
> and consequently the two observers assign different dates to events: there exist pairs of events simultaneous for $\mathcal{O}$ but not for $\mathcal{O}'$. There is no observer-independent ("absolute") time function on Minkowski spacetime — only times defined relative to observers.

> **Corollary (the rest spaces coincide iff the four-velocities do).** For future-directed unit timelike $U_0, U_0'$, one has $U_0^\perp = U_0'^\perp$ if and only if $U_0 = U_0'$. Hence two observers share a notion of simultaneity at $O$ exactly when they are momentarily co-moving.

---

# Motivation

Newtonian mechanics rests on a hidden axiom so natural it took two centuries to notice: time is absolute. There is one universal clock, "now" is a well-defined slice through all of space, and every observer reads the same date off every event. The [[Def - Einstein-Poincaré Simultaneity|operational definition of simultaneity]] just constructed lets *any* observer date *any* event — so the question becomes urgent: do different observers agree? If they did, absolute time would survive in a new guise. This theorem is the answer, and it is the death certificate of absolute time: different observers genuinely disagree, and there is no slicing of spacetime that all of them accept.

The result is the frame-independent, geometric restatement of "the relativity of simultaneity". On a spacetime diagram one draws two observers' lines of simultaneity and sees them tilted relative to each other. This theorem says *why*, in coordinate-free terms: an observer's "now" is the orthogonal complement of their four-velocity, and different four-velocities have different orthogonal complements. The relativity of simultaneity is not a quirk of how we draw diagrams — it is the statement that "orthogonal to $U_0$" and "orthogonal to $U_0'$" are different conditions whenever $U_0\neq U_0'$. Absolute time would require a single hyperplane orthogonal to *every* four-velocity at once, and no such hyperplane exists.

The theorem also identifies exactly when two observers *do* agree — when their four-velocities coincide, i.e. when they are momentarily at rest relative to each other. This is the precise content of "simultaneity is observer-dependent": it depends on, and only on, the observer's instantaneous four-velocity.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "two observers with $U_0\neq U_0'$ crossing at $O$". The point of input broadening is to recognise the many situations that supply this.

The first disguised source is **"two observers in relative motion"**. Any statement that one observer moves relative to another — a train and a platform, a rocket and a station — supplies $U_0\neq U_0'$, because relative motion means non-parallel four-velocities. The bridge is that two future-directed unit timelike vectors are equal iff there is no relative velocity; any nonzero relative velocity makes them differ. *Example problem:* show that a moving observer and a stationary one disagree about whether two spatially separated lightning strikes were simultaneous (Einstein's train).

The second disguised source is **"an accelerated observer at two different proper times"**. Along a single accelerated worldline, the four-velocity $U_0(t)$ changes with proper time, so $U_0(t_1)\neq U_0(t_2)$ and the rest spaces at the two instants differ. The bridge is that a nonzero [[Def - Four-Velocity and Four-Acceleration|four-acceleration]] $A_0 = dU_0/d\tau$ rotates the four-velocity. *Example problem:* show that an accelerated observer's successive rest spaces tilt relative to one another and intersect at a finite distance — the locality of the rest space, and the seed of the Rindler horizon.

The third disguised source is **"a congruence of observers filling a region"**. A family of observers (a fluid, a rotating disk) has a four-velocity *field* $U_0(x)$; wherever the field is non-constant, neighbouring observers have different rest spaces, and the question of whether they patch into a global slicing is the integrability question. The bridge is that a non-constant unit timelike field has a non-constant orthogonal complement. *Example problem:* show that a rotating congruence has no global simultaneity — the chronometric Sagnac/Ehrenfest phenomenon.

**Targets (Output Amplification)**

The conclusion is "$U_0^\perp\neq U_0'^\perp$, so dates disagree".

Combine the conclusion with **a specific pair of events on one observer's rest space**. Since the two rest spaces differ, two events lying in $\mathcal{O}$'s rest space (simultaneous for $\mathcal{O}$) generically have a nonzero $U_0'$-component of their separation, hence different $\mathcal{O}'$-dates. The further result is a concrete demonstration of disagreement — the lightning-strike paradox — useful because it converts the abstract inequality of subspaces into a checkable statement about two named events.

Combine the conclusion with **the integrability (Frobenius) criterion**. The local rest spaces of a congruence patch into a global foliation iff the orthogonal distribution is integrable, $\underline{U_0}\wedge d\underline{U_0} = 0$. For a single inertial observer this holds and simultaneity is global; for a rotating congruence it fails. The further result is the dichotomy "inertial $\Rightarrow$ global simultaneity; rotating $\Rightarrow$ no global simultaneity", useful because it explains *which* observers can still pretend to an absolute time (only the inertial ones, locally) and which cannot at all.

Combine the conclusion with **the invariance of causal order for timelike separations**. Although dates disagree, the *causal* order of timelike- or null-separated events is observer-independent (the sign of the interval is invariant). The further result reconciles "no absolute time" with "no acausality": observers disagree on the time *coordinate* of events but agree on cause-and-effect, because disagreement is possible only for spacelike-separated events. The combination is nonobvious because it shows the failure of absolute time does not threaten causality.

---

# Why Is It True

The mechanism is a single fact of linear algebra dressed in physics: **the orthogonal complement of a line determines the line, so different four-velocities cannot share a rest space.**

Picture two observers crossing at $O$. Each declares "space" to be the hyperplane orthogonal to their own four-velocity. If these two hyperplanes were the *same* three-plane $H$, then both $U_0$ and $U_0'$ would be orthogonal to all of $H$ — but the orthogonal complement of a three-dimensional subspace (with respect to a non-degenerate metric) is one-dimensional, so $U_0$ and $U_0'$ would both lie on a single line, forcing them parallel; being unit and future-directed, they would be equal. Contrapositive: $U_0\neq U_0'$ forces $U_0^\perp\neq U_0'^\perp$. There is simply not enough room for two different normalised directions to have the same orthogonal hyperplane.

Now the physics. "Same date for an event" means "lies on the same simultaneity slice", and the slices are these hyperplanes. Different hyperplanes through $O$ intersect in a two-plane and diverge away from it, so an event off that intersection lands on different slices for the two observers — different dates. The only way for *all* observers to agree on dates would be a single hyperplane orthogonal to every four-velocity simultaneously, and no hyperplane is orthogonal to two non-parallel timelike vectors, let alone all of them. **Absolute time fails because no single spatial hyperplane can be orthogonal to more than one direction of motion.**

The reason this is special to the indefinite metric is worth a sentence. In a *degenerate* (Galilean) structure, "time" is a single linear functional $dt$ that every observer shares — the simultaneity slices are its level sets, the same for everyone, because the degenerate structure provides a preferred temporal direction. The Minkowski metric is non-degenerate, so there is no preferred temporal functional; each observer must manufacture "time" from their own four-velocity, and the manufactures differ. Non-degeneracy is what kills absolute time.

---

# What Makes This Hard

The conceptual hurdle is not the proof — which is a one-line dimension count — but believing that the disagreement is *real* rather than an artifact of clock errors or signal delays: two observers, having correctly synchronised their own clocks by radar, genuinely assign different dates to the same event, and neither is wrong. The common error is to look for a "true" simultaneity behind the observer-dependent ones (there is none), or to think the disagreement could be removed by better instruments (it cannot — it is geometric). The subtle technical point is that the disagreement is confined to *spacelike*-separated events; for timelike or null separations all observers agree on the order, which is what saves causality.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Show that the orthogonal complement of a timelike line determines the line (a dimension count plus non-degeneracy), so distinct unit future four-velocities have distinct rest spaces; then exhibit two events simultaneous for one observer but not the other to make the date-disagreement concrete.

**Subgoal decomposition:**

1. **The orthogonal complement determines the four-velocity.** Show $U_0^\perp = U_0'^\perp \Rightarrow U_0 = U_0'$.
   - *Hint:* $(U_0^\perp)^\perp = \mathrm{Span}(U_0)$ by non-degeneracy and dimension count; equal complements give equal spans, then normalise and fix the time direction.
   - *Why needed:* This is the entire structural content — distinct four-velocities cannot share a rest space.

2. **Contrapositive gives the theorem.** Conclude $U_0\neq U_0'\Rightarrow U_0^\perp\neq U_0'^\perp$.
   - *Hint:* Logical contrapositive of subgoal 1.
   - *Why needed:* It states the rest spaces differ.

3. **Translate into date-disagreement.** Find two events simultaneous for $\mathcal{O}$ but not $\mathcal{O}'$.
   - *Hint:* Take a nonzero vector in $U_0^\perp\setminus U_0'^\perp$; its endpoints are $\mathcal{O}$-simultaneous but have nonzero $U_0'$-separation.
   - *Why needed:* It turns the inequality of subspaces into a physical statement about dates.

---

# Lemma Decomposition

> [!note]- Lemma 1: The orthogonal complement of a timelike line is three-dimensional and recovers the line
> **Statement:** For a timelike vector $U_0$ in Minkowski space, $\dim U_0^\perp = 3$ and $(U_0^\perp)^\perp = \mathrm{Span}(U_0)$.
>
> **Hint:** Use non-degeneracy of $\eta$: the orthogonal complement of a $k$-dimensional subspace has dimension $4 - k$, and the double complement returns the original.
>
> **Why needed:** It is the linear-algebra fact that two different lines cannot have the same orthogonal hyperplane.
>
> > [!note]- Full proof
> > For a non-degenerate bilinear form on a four-dimensional space, the map $X\mapsto g(X,\cdot)$ is an isomorphism $E\to E^*$, so the orthogonal complement of any subspace $W$ satisfies $\dim W^\perp = 4 - \dim W$ and $(W^\perp)^\perp = W$. Apply with $W = \mathrm{Span}(U_0)$, $\dim W = 1$: then $\dim U_0^\perp = 3$ and $(U_0^\perp)^\perp = \mathrm{Span}(U_0)$. (Non-degeneracy is essential; for a degenerate form the double complement can be larger than $W$.) $\blacksquare$

> [!note]- Lemma 2: Distinct unit future four-velocities have distinct rest spaces
> **Statement:** If $U_0, U_0'$ are future-directed unit timelike and $U_0^\perp = U_0'^\perp$, then $U_0 = U_0'$.
>
> **Hint:** Take $(\cdot)^\perp$ of both sides and use Lemma 1.
>
> **Why needed:** It is the contrapositive engine of the theorem.
>
> > [!note]- Full proof
> > Suppose $U_0^\perp = U_0'^\perp$. Taking orthogonal complements and using Lemma 1, $\mathrm{Span}(U_0) = (U_0^\perp)^\perp = (U_0'^\perp)^\perp = \mathrm{Span}(U_0')$. So $U_0' = \lambda U_0$ for some scalar $\lambda$. Unit norm gives $U_0'\cdot U_0' = \lambda^2(U_0\cdot U_0)$, i.e. $1 = \lambda^2$, so $\lambda = \pm 1$. Future-directedness (both have positive time component in any frame where $U_0$ does) forces $\lambda = +1$, hence $U_0' = U_0$. Contrapositively, $U_0\neq U_0'\Rightarrow U_0^\perp\neq U_0'^\perp$. $\blacksquare$

> [!note]- Lemma 3: Different rest spaces force a date-disagreement
> **Statement:** If $U_0^\perp\neq U_0'^\perp$, there exist two events $P, Q$ simultaneous for $\mathcal{O}$ (i.e. $\overrightarrow{PQ}\cdot U_0 = 0$) but not for $\mathcal{O}'$ (i.e. $\overrightarrow{PQ}\cdot U_0'\neq 0$).
>
> **Hint:** A vector in one complement but not the other does the job.
>
> **Why needed:** It converts the inequality of subspaces into the physical statement that dates disagree.
>
> > [!note]- Full proof
> > Since $U_0^\perp\neq U_0'^\perp$ and both are three-dimensional, neither contains the other (two distinct subspaces of the same dimension), so there is a vector $W\in U_0^\perp$ with $W\notin U_0'^\perp$, i.e. $W\cdot U_0 = 0$ but $W\cdot U_0'\neq 0$. Let $P$ be any event and $Q = P + W$. Then $\overrightarrow{PQ} = W$ is orthogonal to $U_0$, so $P$ and $Q$ are simultaneous for $\mathcal{O}$; but $\overrightarrow{PQ}\cdot U_0'\neq 0$, so they are *not* simultaneous for $\mathcal{O}'$. The $\mathcal{O}'$-dates of $P$ and $Q$ differ by $\overrightarrow{PQ}\cdot U_0'/(U_0'\cdot U_0') = W\cdot U_0'\neq 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathcal{O}$ and $\mathcal{O}'$ cross at $O$ with future-directed unit timelike four-velocities $U_0\neq U_0'$.
>
> By Lemma 1, the orthogonal complement of a timelike line in Minkowski space is three-dimensional and satisfies $(U_0^\perp)^\perp = \mathrm{Span}(U_0)$, using only the non-degeneracy of $\eta$.
>
> By Lemma 2, this forces distinct four-velocities to have distinct rest spaces: if $U_0^\perp = U_0'^\perp$ then $\mathrm{Span}(U_0) = \mathrm{Span}(U_0')$, and unit norm with future-direction gives $U_0 = U_0'$. Contrapositively, $U_0\neq U_0'$ implies $U_0^\perp\neq U_0'^\perp$ — the first conclusion.
>
> By Lemma 3, distinct rest spaces force a date-disagreement: choosing $W\in U_0^\perp\setminus U_0'^\perp$ and $P, Q = P + W$, the events $P, Q$ are simultaneous for $\mathcal{O}$ ($\overrightarrow{PQ}\cdot U_0 = 0$) but not for $\mathcal{O}'$ ($\overrightarrow{PQ}\cdot U_0'\neq 0$), with $\mathcal{O}'$-date difference $W\cdot U_0'\neq 0$ — the second conclusion.
>
> Finally, no observer-independent time can exist: such a time would be a function whose level sets are simultaneity slices for *every* observer, hence a single hyperplane (through each event) orthogonal to every timelike four-velocity at once. But a hyperplane is the orthogonal complement of a single line, which cannot be orthogonal to two non-parallel directions; so no hyperplane is orthogonal to all four-velocities, and no absolute time exists. The corollary ($U_0^\perp = U_0'^\perp\Leftrightarrow U_0 = U_0'$) is Lemma 2 together with the trivial converse. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Foliations and the Frobenius theorem (differential geometry).** A congruence of observers has a four-velocity field $U_0(x)$; the local rest spaces patch into a global simultaneity foliation iff the distribution $\ker\underline{U_0}$ is integrable, $\underline{U_0}\wedge d\underline{U_0} = 0$. Deciding whether a given congruence admits global simultaneity is this theorem's integrable upgrade, and the rotating-disk failure is a vivid non-integrable example. The application is nonobvious because "no absolute time" (a pointwise statement) sharpens into "no global time slicing for this congruence" (an integrability statement).

**Special relativity of the train paradox (physics).** Einstein's thought experiment — lightning strikes the two ends of a moving train, simultaneous in the platform frame — is a direct instance: the two strike events lie in the platform observer's rest space but not the train observer's, so they are not simultaneous for the train. Working it out quantitatively (computing the $\mathcal{O}'$-date difference $W\cdot U_0'$) is the canonical drill. The surprise is that the disagreement is symmetric and real, not a measurement error.

**Cosmic time in cosmology (general relativity).** Although absolute time fails in general, a special family of observers — the comoving observers of a homogeneous, isotropic universe — *does* admit a global simultaneity, "cosmic time", because their four-velocity field is irrotational and the orthogonal distribution integrates. Recognising that cosmic time is the integrable exception, not a return to Newtonian absolute time, is the deep application: even there, the time is relative to a privileged congruence, not observer-independent.

---

# Bridges

- **[[Def - Einstein-Poincaré Simultaneity]]** — this theorem is the immediate consequence of defining simultaneity as orthogonality to $U_0$: once "now" is the orthogonal complement of the four-velocity, distinct four-velocities give distinct "nows", and absolute time is gone. The theorem is the structural payoff of that definition.

- **[[Def - Observer and Local Rest Space]]** — the theorem is a statement about the map $U_0\mapsto U_0^\perp$ being injective on unit future four-velocities. It is precisely why the rest space is "local" and observer-dependent rather than a universal slice.

- **The relativity of simultaneity** — on a spacetime diagram, the tilted lines of simultaneity of two observers are this theorem drawn in two dimensions; the tilt angle is the relative rapidity. The diagram is the mnemonic; the inequality $U_0^\perp\neq U_0'^\perp$ is the content. (See [[Special Relativity II — Simultaneity, Time Dilation and Length Contraction]] for the diagram-based treatment.)

- **The Frobenius integrability of a congruence** — extending from one observer to a four-velocity *field*, the question of whether local rest spaces assemble into global simultaneity surfaces is governed by $\underline{U_0}\wedge d\underline{U_0} = 0$. Inertial congruences integrate (global simultaneity), rotating ones do not (no global simultaneity), which is the deep reason the rotating disk has no consistent clock synchronisation in [[Special Relativity XVII — Rotating Observers]].

---

# Unlocked by This

> [!tip] Global Simultaneity for Inertial Observers *(from the Poincaré group)*
> The one class of observers that *recovers* a global notion of simultaneity is the **inertial** observers: with zero four-acceleration the four-velocity is constant, the rest spaces are parallel, and they foliate all of spacetime into the constant-time hyperplanes of an inertial frame. This is the geometric meaning of an inertial frame's single time coordinate and the subject of [[Special Relativity XII — Inertial Observers and the Poincaré Group]].

> [!tip] Cosmic Time and Preferred Foliations *(from General Relativity)*
> In general relativity the failure of absolute time is total, but special spacetimes admit a preferred congruence whose orthogonal distribution integrates — giving **cosmic time** in homogeneous cosmologies, or the foliations chosen in the $3+1$ formulation. These are not a return to Newtonian absolute time; they are observer-relative times that happen to be globally consistent for a privileged family of observers.
