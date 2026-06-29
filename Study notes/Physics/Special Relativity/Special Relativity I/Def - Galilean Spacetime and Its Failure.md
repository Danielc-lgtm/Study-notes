---
type: definition
subject: special-relativity
prereqs: []
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ throughout, restoring $c$ where a formula is more recognisable with it. An **event** is a point of spacetime; in a frame it has coordinates $(t, x, y, z)$. Two inertial frames $S$ and $S'$ move with relative velocity $\mathbf{v} = (v, 0, 0)$ along their common $x$-axis, with origins coinciding at $t = t' = 0$. Spatial three-vectors are bold. Full registry on [[Special Relativity I — Postulates and Lorentz Transformations]].

This page defines the structure special relativity replaces, so that the replacement is intelligible: the **Galilean transformation**, **Galilean spacetime** as a geometric object, the precise sense in which a fixed speed of light breaks it, and the $c \to \infty$ limit in which it is recovered.

---

# Axiom Motivation

Before relativity there was a picture of space and time so natural that for two centuries it was never stated as an assumption, only used. Time is a single universal river: there is one clock, every observer reads the same time from it, and "now" is a well-defined slice through all of space, the same slice for everybody. Space at each instant is ordinary Euclidean three-space, and the distance between two simultaneous events is absolute. The job of this page is to make that picture explicit enough to see exactly where it fails, because special relativity is the theory you are forced into once you locate the failure.

The picture is encoded in the **Galilean transformation**. Two frames in relative motion at velocity $v$ along $x$ relate their coordinates by $x' = x - vt$ (the moving origin slides along), $y' = y$, $z' = z$, and — the load-bearing clause — $t' = t$. That last equation *is* the assumption of absolute time: it says the two observers' clocks agree at every event, that simultaneity is shared, that duration is the same for all. Everything Newtonian flows from it. In particular, velocities add: differentiate $x' = x - vt$ to get $u' = u - v$, so a particle moving at $u$ in $S$ moves at $u - v$ in $S'$, and a signal you chase at $v$ approaches you slower by exactly $v$. This is the common-sense law that running towards an oncoming train makes it close faster.

The desideratum, then, is to understand Galilean spacetime *as a geometry* — because relativity will replace it with a different geometry, and the contrast is the clearest way to learn the new one. Here is the first surprise: Galilean spacetime is **not** four-dimensional Euclidean space. One might guess that $\mathbb{R}^4$ with the Euclidean distance $\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$ is the right structure, but it is not, because that distance is *not* invariant under the Galilean transformation — a boost $x' = x - vt$ changes it. The Galilean structure is instead a *degenerate* one: there is an absolute time function $t$ (so the "temporal distance" $\Delta t$ between any two events is well-defined and frame-independent), and on each slice of constant $t$ there is a Euclidean metric (so spatial distance is defined *only* between simultaneous events). There is no single non-degenerate metric fusing them; time and space are separate absolutes, glued along the slicing. The degeneracy is the whole character of the Newtonian world, and it is exactly what relativity removes.

Now the failure. Suppose, as Maxwell's electromagnetism asserts and Michelson–Morley confirmed, that light moves at a fixed speed $c$ in *every* inertial frame, independent of the source. Trace a light ray in $S$: it obeys $x = ct$, i.e. $x/t = c$. Feed this through the Galilean transformation: in $S'$ its trajectory is $x'/t' = (x - vt)/t = c - v$. So the Galilean transformation predicts the light ray travels at $c - v$ in the chasing frame — the velocities have added, as they must when $t' = t$. But this contradicts the premise that light travels at $c$ in $S'$ too. The contradiction is sharp and unavoidable: a frame-independent light speed is *logically incompatible* with absolute time. One of them is wrong, and the experiments are unanimous that it is absolute time. The clause $t' = t$ is the casualty.

What exactly must be weakened? Not linearity (the law of inertia still demands straight lines map to straight lines), not the form $x' = \gamma(x - vt)$ of the spatial part (the origin of $S'$ still moves as $x = vt$). Only $t' = t$ — the assumption that the time coordinate is untouched by a change of frame. Once you allow $t'$ to depend on $x$ as well as $t$, simultaneity becomes frame-dependent and the contradiction dissolves; the unique replacement is the [[Def - The Lorentz Transformation|Lorentz transformation]]. The Galilean transformation is not *wrong* so much as *approximate*: it is the correct law to first order in $v/c$, and it is recovered exactly in the formal limit $c \to \infty$, where light is infinitely fast and the addition of velocities has no upper ceiling to respect.

---

# The Definition

**Galilean spacetime** is the spacetime of Newtonian mechanics: the set of events, equipped with two pieces of structure that are *not* combined into a single metric —

1. an **absolute time function** $t$, well-defined up to choice of origin and units, so that the temporal separation $\Delta t$ between any two events is frame-independent; and
2. on each simultaneity slice $\{t = \text{const}\}$, a **Euclidean metric**, so that the spatial distance between two *simultaneous* events is frame-independent, while the spatial distance between non-simultaneous events is not defined invariantly.

Topologically it is $\mathbb{R}^3 \times \mathbb{R}_t \cong \mathbb{R}^4$, but it carries no invariant Euclidean (or any non-degenerate) inner product on $\mathbb{R}^4$.

The transformations between inertial frames are the **Galilean transformations**. For a boost of velocity $\mathbf{v} = (v,0,0)$ with coincident origins,
$$
x' = x - vt, \qquad y' = y, \qquad z' = z, \qquad t' = t.
$$
The defining feature is $t' = t$: time is untouched. The associated velocity-addition law is
$$
u' = u - v \qquad (\text{equivalently } u = u' + v),
$$
obtained by differentiating the spatial equation, with no restriction on the magnitudes — Galilean velocities are unbounded.

> [!warning] Where Galilean spacetime fails
> A light ray with $x = ct$ in $S$ has, by the Galilean transformation, speed $x'/t' = c - v$ in $S'$. This contradicts [[Def - Inertial Frame and the Postulates of Special Relativity|Postulate 2]] (light travels at $c$ in every inertial frame). The incompatibility is between the constancy of $c$ and the clause $t' = t$; special relativity keeps the former and abandons the latter.

---

# Categorical / Structural Definition

Galilean spacetime is a **fibred** structure rather than a metric one, and that is the structural heart of the matter. The absolute time function is a surjection $t : \mathcal{E} \to \mathbb{R}$ (events to instants); its fibres $t^{-1}(\tau)$ are the simultaneity slices, each an affine Euclidean three-space. The total space is the bundle of these Euclidean fibres over the time line $\mathbb{R}_t$. Crucially, there is no canonical way to identify points in different fibres — no absolute notion of "the same place at a later time" — because that identification is exactly what a choice of inertial frame (a choice of which worldlines count as "at rest") provides, and the principle of relativity forbids a preferred choice. The Galilean group acts by bundle automorphisms covering translations and rescalings of the base $\mathbb{R}_t$.

Special relativity replaces this fibred structure with a single non-degenerate object: it glues the separate time-line and space-fibres into one four-dimensional affine space carrying one indefinite metric, [[Def - Minkowski Space and the Metric|Minkowski space]] with $\eta = \mathrm{diag}(+1,-1,-1,-1)$. The transition is precisely the *de-degeneration* of the metric: the degenerate pair (absolute $\Delta t$, fibrewise Euclidean distance) is replaced by the single non-degenerate interval $\Delta s^2 = \Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$. The minus signs are what fuse time and space into one geometry; in the limit $c \to \infty$ the metric degenerates back and the fibration reappears.

---

# Relate to Other Fields / Compression

Galilean spacetime is the **contraction** of Minkowski spacetime in the sense of Lie-group contraction: the Galilean group is the $c \to \infty$ limit of the [[Def - The Poincaré Group|Poincaré group]], with Lorentz boosts degenerating into Galilean boosts. In the boost generator, the term mixing time into space is suppressed by $1/c^2$; sending $c \to \infty$ kills it, leaving the rigid time-slice shear $t' = t$. This is the precise sense in which Newtonian mechanics is a limit, not a competitor, of relativity, and it is the same contraction that takes the relativistic energy $E = \gamma m c^2$ to the Newtonian $\tfrac12 m v^2 + mc^2$.

**True name:** Galilean spacetime is *"absolute time plus per-slice Euclidean space, with no glue between slices"* — a degenerate, fibred geometry — and the Galilean transformation is *"the Lorentz transformation with the $vx/c^2$ correction to the clock thrown away."* The single equation that names the whole structure, and the single equation special relativity deletes, is $t' = t$.

---

# Examples / Corollaries

**Is an instance — everyday velocity addition.** A passenger walks forward at $1.5\ \mathrm{m/s}$ in a train moving at $30\ \mathrm{m/s}$; relative to the ground they move at $31.5\ \mathrm{m/s}$. This is $u = u' + v$, the Galilean law, and it is correct to fantastic precision because $v/c \sim 10^{-7}$. Galilean spacetime is not a historical error; it is the working geometry of all non-relativistic engineering.

**Is an instance — the failure of Maxwell to be Galilean-invariant.** The wave equation for light has a fixed propagation speed $c$ baked in; substituting the Galilean transformation $x' = x - vt$, $t' = t$ produces a wave equation with speed $c \pm v$, a *different* equation. So Maxwell's equations are not Galilean-invariant — they single out a frame — which is exactly the nineteenth-century puzzle that the postulates resolved.

**Is NOT an instance — $\mathbb{R}^4$ with the Euclidean metric.** The space $\mathbb{R}^4$ with distance $\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$ is *not* Galilean spacetime: that Euclidean distance is not preserved by Galilean boosts (a boost changes $\Delta x$ while fixing $\Delta t$, so the sum of squares changes). Galilean spacetime has no invariant four-dimensional metric at all; this is a common and instructive error, and the same warning recurs for [[Def - Minkowski Space and the Metric|Minkowski space]] (which is also *not* Euclidean $\mathbb{R}^4$, for the opposite reason — it has an indefinite metric, not no metric).

**Is NOT an instance — Minkowski spacetime.** [[Def - Minkowski Space and the Metric|Minkowski space]] is *not* a Galilean spacetime: it has a single non-degenerate indefinite metric fusing time and space, no absolute simultaneity, and a finite invariant speed $c$. The two are related only by the $c \to \infty$ limit.

**Corollary — simultaneity is absolute in Galilean spacetime, relative in Minkowski.** Because $t' = t$, two events simultaneous in $S$ ($\Delta t = 0$) are simultaneous in $S'$ ($\Delta t' = 0$) — absolute simultaneity. Deleting $t' = t$ in favour of the Lorentz clock $t' = \gamma(t - vx)$ makes $\Delta t' = \gamma(\Delta t - v\,\Delta x)$ depend on the spatial separation, so simultaneous-in-$S$ events are generally not simultaneous in $S'$. This single change is the source of essentially every relativistic surprise.

**Calibration check.** You have understood the page if you can: (1) write the Galilean transformation from memory and circle the clause that fails ($t' = t$); (2) show in one line that a light ray $x = ct$ becomes $x' = (c-v)t'$ under it, and say why that contradicts Postulate 2; and (3) explain why Galilean spacetime is *not* $\mathbb{R}^4$ with the Euclidean metric, by exhibiting a Galilean boost that changes the Euclidean four-distance between two non-simultaneous events.

---

# Unlocked by This

> [!tip] The Lorentz Transformation as the Unique Repair *(from §1.2)*
> Identifying the failure — a fixed light speed is incompatible with $t' = t$ — tells you exactly what to change and what to keep. Keep linearity and the spatial form $x' = \gamma(x - vt)$; replace $t' = t$ by a clock that mixes in position. The unique result compatible with both postulates is the [[Def - The Lorentz Transformation|Lorentz transformation]], derived in [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|the uniqueness theorem]].

> [!tip] Group Contraction and the Newtonian Limit *(from SR XII and beyond)*
> The relationship "Galilean = limit of relativistic" is a precise instance of **İnönü–Wigner group contraction**: the Galilean group is the $c \to \infty$ contraction of the [[Def - The Poincaré Group|Poincaré group]]. The same limit takes every relativistic formula to its Newtonian counterpart, and recognising a contraction is the standard way to check that a new theory reduces correctly to the old one.
