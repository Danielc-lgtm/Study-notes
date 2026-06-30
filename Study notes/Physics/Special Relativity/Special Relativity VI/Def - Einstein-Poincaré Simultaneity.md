---
type: definition
subject: special-relativity
prereqs:
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Proper Time"
  - "Def - The Null Cone and the Time Arrow"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the **mostly-minus** metric $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike vector has $X\cdot X > 0$ and a null vector has $X\cdot X = 0$. An observer $\mathcal{O}$ moves on a future-directed timelike unit worldline $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$), reading [[Def - Proper Time|proper time]] $t$ on a carried clock. $A$, $A_1$, $A_2$ are events on $\mathcal{L}_0$ of proper times $t$, $t_1$, $t_2$; $M$ (or $B$) is an event off the worldline; $\overrightarrow{AB}$ denotes the displacement vector from $A$ to $B$. Full registry on [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames]].

> [!warning] Convention
> Gourgoulhon (his §3.2.2) works in mostly-plus signature with $\vec u\cdot\vec u = -1$. The simultaneity criterion he derives, $\vec u(A)\cdot\overrightarrow{AB} = 0$, is a statement of *orthogonality* (equality to zero) and is therefore **signature-independent** — it reads identically in our convention as $U_0\cdot\overrightarrow{AB} = 0$. The intermediate scalar-square formulas pick up sign flips in the translation; these are tracked in the derivation below.

---

# Axiom Motivation

The problem this definition solves is sharp and, at first sight, has no solution. An observer carrying a clock can date events *on* their worldline — just read the clock. But to do physics an observer must date events *off* the worldline: to say "the flash over there happened at noon my time", you must decide which tick of your clock is *simultaneous* with the distant flash. Newtonian physics answered this with absolute time: there is one universal clock, and "simultaneous" needs no observer. Relativity has thrown that away. Minkowski spacetime carries no preferred slicing into "moments"; the only canonical structures it has are the light cones. So simultaneity must be *defined*, by some operational procedure, and the choice of procedure is a genuine convention — Poincaré was the first to see that simultaneity "must result from some convention".

What raw materials does an observer have? A clock, and the ability to emit and receive light. That is all. So any definition of simultaneity must be built from proper-time readings and light signals. The natural construction is radar: emit a photon, let it bounce off the distant event $M$, and receive the reflection. If the photon leaves at proper time $t_1$ and the reflection arrives at $t_2$, the most symmetric possible choice is to declare $M$ simultaneous with the *midpoint* reading,
$$
t \;=\; \tfrac12\,(t_1 + t_2).
$$
The justification is a symmetry one: light is naively imagined to take the same time out as back, so the event "out there" should be dated to the middle of the round trip. The word "naively" is essential — "travel time" itself presupposes a notion of simultaneity, so this is not a derivation but a well-motivated *definition*. Its decisive virtue is that it uses only the light cones (through the photon trajectories), which are the sole canonical structures of Minkowski spacetime, and it is operational: an experimenter can carry it out with a clock and a mirror.

Why this convention and not a nearby variant? Reichenbach proposed the one-parameter family
$$
t \;=\; (1-\varepsilon)\,t_1 + \varepsilon\,t_2, \qquad \varepsilon \in\, ]0, 1[,
$$
which reduces to the Einstein–Poincaré choice exactly at $\varepsilon = \tfrac12$. There is no *logical* inconsistency in choosing $\varepsilon \ne \tfrac12$ — one can build a perfectly consistent description of physics with skewed simultaneity. What goes wrong is everything else: the laws of physics become needlessly complicated, and, decisively for this chapter, the resulting "rest space" is **no longer orthogonal to the worldline**. The whole geometric structure that makes the rest space a clean metric object — the projector, the Euclidean spatial geometry, Synge's distance — works *only* for $\varepsilon = \tfrac12$, because only then does the simultaneity criterion reduce to metric orthogonality. The selection principle is Poincaré's: among consistent conventions, choose the one in which the laws of physics are simplest, and that singles out $\varepsilon = \tfrac12$.

The reward for adopting it is the result that organises the rest of the chapter. Working the radar construction through the null conditions on the two photon legs (done below), the criterion "$M$ is simultaneous with $A$ for $\mathcal{O}$" turns out to be equivalent to the clean metric statement
$$
U_0\cdot\overrightarrow{AM} \;=\; 0 :
$$
$M$ is simultaneous with $A$ exactly when the displacement $\overrightarrow{AM}$ is **orthogonal** to the observer's four-velocity. Simultaneity *is* orthogonality to $U_0$. This is the bridge from a slippery temporal convention to a piece of linear algebra, and it is what lets the observer's "now" be identified with the orthogonal complement $U_0^\perp$ — the [[Def - Observer and Local Rest Space|local rest space]].

---

# The Definition

Let $\mathcal{O}$ be an observer with worldline $\mathcal{L}_0$ and [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$, equipped with an ideal clock and a device for emitting and receiving photons. Let $A$ be an event on $\mathcal{L}_0$ of [[Def - Proper Time|proper time]] $t$, and let $M$ be any event of Minkowski spacetime.

**Einstein–Poincaré simultaneity.** Emit a photon from $\mathcal{O}$'s worldline that reaches $M$ and is immediately reflected back to $\mathcal{O}$; let $t_1$ be the proper time of emission and $t_2$ the proper time of reception. The event $M$ is **simultaneous with $A$ for the observer $\mathcal{O}$** if and only if
$$
\boxed{\,t \;=\; \tfrac12\,(t_1 + t_2)\,},
$$
and the **date of $M$ with respect to $\mathcal{O}$** is this value $t$. This is the **Einstein–Poincaré criterion of simultaneity** (the "$\varepsilon = \tfrac12$" convention).

**Equivalent metric form.** For an event $M$ in the neighbourhood of $\mathcal{L}_0$, the criterion is equivalent to the orthogonality of the displacement to the four-velocity:
$$
\boxed{\,M \text{ is simultaneous with } A \text{ for } \mathcal{O} \quad\Longleftrightarrow\quad U_0\cdot\overrightarrow{AM} \;=\; 0\,}.
$$

**Reichenbach's $\varepsilon$-simultaneity** is the generalisation $t = (1-\varepsilon)t_1 + \varepsilon t_2$ with $\varepsilon\in\,]0,1[$; it is logically consistent for any $\varepsilon$ but reduces to the Einstein–Poincaré criterion (and to metric orthogonality) only at $\varepsilon = \tfrac12$.

> [!note]- Derivation of the metric form from the radar criterion
> Let $A$ be on $\mathcal{L}_0$ at proper time $t$, and $B$ an event close to $\mathcal{L}_0$ (so that the worldline's curvature between the relevant points may be neglected and segments treated as straight). The photon emitted at $A_1$ (proper time $t_1 < t$) reflects at $B$ and is received at $A_2$ (proper time $t_2 > t$). Because $A_1, A, A_2$ all lie on $\mathcal{L}_0$ near $A$, the displacements to $A$ are proper-time multiples of the four-velocity:
> $$\overrightarrow{A_1A} = c\,(t - t_1)\,U_0(A), \qquad \overrightarrow{A_2A} = c\,(t - t_2)\,U_0(A),$$
> which follow from the definition of proper time and $U_0\cdot U_0 = +1$.
>
> The leg $\overrightarrow{A_1B}$ is null (it is a photon path): $\overrightarrow{A_1B}\cdot\overrightarrow{A_1B} = 0$. Using Chasles, $\overrightarrow{A_1B} = \overrightarrow{A_1A} + \overrightarrow{AB}$, so
> $$\overrightarrow{A_1A}\cdot\overrightarrow{A_1A} + 2\,\overrightarrow{A_1A}\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0.$$
> In **our** mostly-minus signature, $\overrightarrow{A_1A}\cdot\overrightarrow{A_1A} = c^2(t-t_1)^2\,(U_0\cdot U_0) = +c^2(t-t_1)^2$ (a sign opposite to Gourgoulhon, whose $\vec u\cdot\vec u = -1$ gives $-c^2(t-t_1)^2$), and $\overrightarrow{A_1A}\cdot\overrightarrow{AB} = c(t-t_1)\,U_0\cdot\overrightarrow{AB}$. Hence
> $$c^2(t-t_1)^2 + 2c(t-t_1)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0. \tag{$\ast$}$$
> The leg $\overrightarrow{A_2B}$ is likewise null, giving
> $$c^2(t-t_2)^2 + 2c(t-t_2)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0. \tag{$\ast\ast$}$$
> Subtract $(\ast\ast)$ from $(\ast)$. Using $(t-t_1)^2 - (t-t_2)^2 = (t_2 - t_1)(2t - t_1 - t_2)$ and $(t-t_1) - (t-t_2) = t_2 - t_1$,
> $$c^2(t_2 - t_1)(2t - t_1 - t_2) + 2c(t_2 - t_1)\,U_0\cdot\overrightarrow{AB} = 0.$$
> Since $B\notin\mathcal{L}_0$, the round-trip is nondegenerate and $t_2 - t_1 \ne 0$; dividing by $c(t_2 - t_1)$,
> $$U_0\cdot\overrightarrow{AB} \;=\; -\,c\Big[t - \tfrac12(t_1 + t_2)\Big].$$
> Therefore $U_0\cdot\overrightarrow{AB} = 0$ if and only if $t = \tfrac12(t_1 + t_2)$, which is exactly the radar simultaneity criterion. (The overall sign of $U_0\cdot\overrightarrow{AB}$ is opposite to Gourgoulhon's because of the signature; the vanishing condition is identical.) $\blacksquare$

---

# Relate to Other Fields / Compression

Operationally, Einstein–Poincaré simultaneity is **clock synchronisation by light**: it is the rule that defines what "set your watches together" means for spatially separated, possibly moving clocks, and it is the foundation of every modern timekeeping and positioning system. The GPS constellation synchronises satellite clocks by precisely this radar logic (corrected for the curved-spacetime and gravitational effects of [[General Relativity I — Einstein's Equations and Schwarzschild|general relativity]]). In the language of the geometry to come, the construction is the choice of a *connection between the time axes of nearby observers* — it tells you which spatial directions count as "equal time", which is the same data as a choice of the spatial hyperplane $U_0^\perp$.

**True name:** simultaneity for $\mathcal{O}$ is *metric orthogonality to the four-velocity* — $M \sim A \Leftrightarrow U_0\cdot\overrightarrow{AM} = 0$ — and the radar midpoint rule $t = \tfrac12(t_1+t_2)$ is the operational procedure that realises it. The first form is what you compute with; the second is what you measure with. Carrying both, you can convert any statement about "now" into a one-line algebraic condition (the first) and into a concrete experimental protocol (the second).

---

# Examples / Corollaries

**Is an instance — synchronising two clocks at rest in an inertial frame.** If $\mathcal{O}$ and a distant clock are both at rest in the same inertial frame, the radar photon takes equal coordinate time each way, the midpoint $\tfrac12(t_1+t_2)$ is the coordinate time of reflection, and the criterion reproduces the ordinary Newtonian-looking synchronisation of that frame. The rest spaces are the usual constant-time hyperplanes, and the simultaneity is the familiar one — the relativistic subtlety is invisible because there is only one frame in play.

**Is an instance — the relativity of simultaneity.** Take $\mathcal{O}$ at rest and $\mathcal{O}'$ moving at velocity $v$, crossing at an event $O$. The criterion $U_0\cdot\overrightarrow{OM} = 0$ defines $\mathcal{O}$'s rest space as the horizontal hyperplane; $U_0'\cdot\overrightarrow{OM} = 0$ defines $\mathcal{O}'$'s rest space as a *tilted* hyperplane (tilted by the same angle as $\mathcal{O}'$'s worldline, toward the light cone). The two hyperplanes differ, so events $\mathcal{O}$ calls simultaneous, $\mathcal{O}'$ does not. This is the relativity of simultaneity, recovered as the statement that orthogonal complements of different four-velocities differ.

**Is NOT an instance — a single universal "now".** A Newtonian absolute-time slicing assigns every event one date independent of the observer; this is *not* an Einstein–Poincaré simultaneity, because no single hyperplane is orthogonal to *every* timelike four-velocity at once (orthogonality to $U_0$ and to a different $U_0'$ are incompatible conditions). The absence of a universal "now" is precisely [[Thm - Nonexistence of Absolute Time|the nonexistence of absolute time]].

**Is NOT an instance — Reichenbach's $\varepsilon\ne\tfrac12$ slicing.** Choosing $\varepsilon = \tfrac13$, say, gives a consistent dating but a "rest space" that is *not* orthogonal to $U_0$ — it is a hyperplane tilted off the orthogonal complement. It cannot be obtained as $U_0\cdot\overrightarrow{AM} = 0$ for any metric, and the Euclidean spatial geometry and Synge distance of this chapter fail for it. It is a legitimate convention, but not the metric one.

**Corollary — the date is the proper time of the orthogonal foot.** The date of $M$ for $\mathcal{O}$ equals the proper time $t$ of the unique event $A\in\mathcal{L}_0$ with $U_0(A)\cdot\overrightarrow{AM} = 0$ — the "orthogonal projection" of $M$ onto the worldline along the rest space. This is what makes the date computation a geometric one: drop a perpendicular from $M$ to $\mathcal{L}_0$.

**Calibration check.** You should be able to: (1) state why the midpoint rule is a *convention* and not a theorem (because "travel time" already presupposes simultaneity); (2) write the two null conditions on the radar legs and recover $U_0\cdot\overrightarrow{AB} = -c[t - \tfrac12(t_1+t_2)]$; and (3) explain in one sentence why two observers in relative motion disagree on simultaneity (their four-velocities have different orthogonal complements).

---

# Unlocked by This

> [!tip] The Local Rest Space and the Orthogonal Projector *(from §6.1)*
> Because simultaneity is orthogonality to $U_0$, the set of events simultaneous with $A$ is the hyperplane $A + U_0^\perp$, and the directions are the [[Def - Observer and Local Rest Space|local rest space]] $E_{U_0} = U_0^\perp$. Resolving any vector into its rest-space part and its $U_0$-part is the job of the [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] $\Pi(X) = X - (X\cdot U_0)U_0$, the workhorse of the whole chapter.

> [!tip] Synge's Distance and Born Rigidity *(from §6.2)*
> The very same radar construction, kept to its scalar-square output $\overrightarrow{AB}\cdot\overrightarrow{AB} = -c^2(t-t_1)(t_2-t)$, yields **Synge's formula** for spatial distance from clock readings alone, and hence **Born's rigidity criterion** (constant round-trip time). Simultaneity and distance are two faces of one light-bouncing experiment.

> [!tip] Clock Synchronisation in Accelerated and Rotating Frames *(from later chapters)*
> Applied to an accelerated observer, the criterion produces a slicing that is only **local** (neighbouring rest spaces intersect at distance $\|A_0\|^{-1}$); applied to a rotating congruence it **cannot be made globally consistent** — going around the disk, the synchronisation fails to close up by the Sagnac time, which is the chronometric heart of the **Sagnac effect** and the **Ehrenfest paradox** in [[Special Relativity XVII — Rotating Observers]].
