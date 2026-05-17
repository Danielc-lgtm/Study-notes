---
type: definition
subject: special-relativity
prereqs: []
tags: [physics, special-relativity]
---

# Notation

We work throughout with $c = 1$ (the speed of light as a pure conversion factor; see [[Special Relativity I — Lorentz Transformations and Minkowski Space]] for the full registry). An **event** is a point of spacetime, specified in a given frame by coordinates $(t, x, y, z)$. Frames are denoted $S, S'$ and the observers carrying them $O, O'$. A relative velocity is $v$, and with $c=1$ all physical speeds satisfy $|v| < 1$.

---

# Axiom Motivation

Before there can be physics there must be a coordinate system to do physics in, and the first thing to pin down is *which* coordinate systems are admissible. Newton's laws do not hold in every coordinate system. In a rotating or accelerating frame, free particles appear to swerve — centrifugal and Coriolis "forces" appear — and the law of inertia visibly fails. So one privileges a class of frames in which a free particle really does move in a straight line at constant velocity: the **inertial frames**. This much is not new; it is the foundation of Newtonian mechanics, and special relativity keeps it unchanged.

What we want from a *postulate* of physics is the minimal set of statements from which the entire theory follows, chosen so that each one is either an irreducible experimental fact or an irreducible principle of symmetry. The desideratum for the first postulate is a symmetry principle: there should be no preferred inertial frame. If the laws of physics looked different in a frame moving at $30\,\mathrm{km\,s^{-1}}$ than in one at rest, then "absolute rest" would be physically detectable, and centuries of failed attempts to detect it — culminating in Michelson and Morley finding no ether wind — say it is not. So the **principle of relativity**: the laws of physics take the same form in every inertial frame. This is Galileo's principle, and on its own it is compatible with Newtonian mechanics.

The desideratum for the second postulate is the one irreducible experimental fact that Newtonian mechanics cannot accommodate. Maxwell's electromagnetism predicts a definite speed for light, $c = 1/\sqrt{\varepsilon_0\mu_0}$, with no mention of any frame. If Newtonian velocity addition were correct, light would travel at $c$ in only one frame and at $c \pm v$ in others — and then the principle of relativity would single that one frame out, contradicting the first postulate. Experiment forces the resolution: light travels at $c$ in *every* inertial frame, independent of the motion of the source. This is the **constancy of the speed of light**, and it is genuinely surprising — it is the one postulate that common sense rejects.

Why these two and not a nearby variant? Drop the first postulate and you readmit a preferred frame, the ether, and the theory becomes Newtonian with a luminiferous medium — a theory experiment has refuted. Drop the second and you keep absolute time and the Galilean transformation, contradicting the constancy of $c$. Weaken the second to "light travels at $c$ in the source's rest frame" and you get an emission theory, also refuted by observation (binary stars would appear to move bizarrely). The two postulates as stated are exactly strong enough to determine the Lorentz transformation uniquely ([[Thm - Invariance of the Spacetime Interval]] and [[Def - The Lorentz Transformation]]) and exactly weak enough to be true. Indeed they are mildly redundant: since Maxwell's equations are among "the laws of physics" and they predict $c$, the first postulate almost implies the second — but until one has seen the link between electromagnetism and relativity it is cleaner to keep both.

---

# The Definition

**Inertial frame.** An **inertial frame** (or inertial coordinate system) is a coordinate system $(t, x, y, z)$ on spacetime, consisting of a set of synchronised clocks and rigid measuring rods, in which a particle subject to no force moves with constant velocity — that is, the law of inertia holds. Any two inertial frames are in uniform (unaccelerated, non-rotating) relative motion. An event observed to have coordinates $(t,x,y,z)$ in one inertial frame has, in general, different coordinates $(t',x',y',z')$ in another, and the relation between them is a coordinate transformation.

**The two postulates of special relativity.**

> **Postulate 1 (Principle of relativity).** The laws of physics take the same form in every inertial frame. No inertial frame is preferred; only relative motion between frames is observable.

> **Postulate 2 (Constancy of the speed of light).** Light propagates in vacuum with the same speed $c$ in every inertial frame, independent of the direction of propagation and of the motion of the source.

With $c = 1$, Postulate 2 says every light ray has a worldline of slope $1$ — at $45^\circ$ — in every inertial frame's spacetime diagram.

---

# Relate to Other Fields / Compression

The structure here is the familiar one of an axiomatic theory: a class of admissible objects (inertial frames) and a list of invariance requirements (the postulates) that constrain how those objects relate. It is the same shape as the definition of a [[Def - Group|group]] — a class of objects plus axioms they must satisfy — and indeed the postulates will shortly be repackaged as a group-theoretic statement, that physics is invariant under the [[Def - The Lorentz Group|Lorentz group]].

The deeper compression is this: Postulate 1 is a statement that a certain group acts by symmetries of physics, and Postulate 2 fixes *which* group. With Galilean velocity addition the group would be the Galilean group and time would be absolute; with the constancy of $c$ the group is the Poincaré group and the invariant is the spacetime interval. The postulates are, in modern language, the specification of the symmetry group of nature — the same role played by gauge symmetry in particle physics and by diffeomorphism invariance in general relativity. Choosing the postulates *is* choosing the symmetry group.

---

# Examples / Corollaries

**Is an instance — a freely-falling laboratory (locally).** A small laboratory in free fall, far from any walls, is an inertial frame: released objects float, and a thrown ball travels in a straight line at constant velocity. (Globally, gravity makes spacetime curved and no single inertial frame covers it — that is the subject of general relativity — but locally, over small regions, free fall is inertial.)

**Is NOT an instance — a rotating carousel.** A coordinate system fixed to a spinning carousel is not inertial: a ball placed at rest on the floor immediately rolls outward, apparently pushed by a centrifugal force, so free particles do not move in straight lines. The law of inertia fails, and the postulates of special relativity do not apply directly in such a frame.

**Is NOT an instance — an accelerating rocket.** The cabin of a rocket firing its engines is not inertial: a released object falls to the back wall. Acceleration is absolute and detectable from inside, unlike uniform velocity, which is not. This asymmetry between uniform velocity (relative, undetectable) and acceleration (absolute, detectable) is exactly what resolves the [[Ex - The twin paradox|twin paradox]].

**Corollary — there is no experiment internal to an inertial frame that detects its velocity.** By Postulate 1, every experiment yields the same result in every inertial frame, so no measurement made inside a sealed inertial laboratory can reveal how fast it is moving. This is Galileo's ship: below decks, all motion looks the same whether the ship is docked or sailing smoothly. If the reader accepts this, the principle of relativity is understood.

**Corollary — running towards a light beam does not increase its measured speed.** By Postulate 2, an observer racing towards an oncoming light ray still measures its speed as $c$, not $c + v$. This is the corollary that defies common sense, and verifying that one finds it genuinely strange is the test of having understood Postulate 2 — it is the seed of every relativistic effect.

**Corollary — the Galilean transformation cannot be correct.** If $x' = x - vt$ and $t' = t$, then a light ray with $x = t$ in $S$ has $x' = t' - vt' = (1-v)t'$ in $S'$, a speed $1 - v \ne 1$. This contradicts Postulate 2, so the Galilean transformation must be replaced — by the [[Def - The Lorentz Transformation|Lorentz transformation]].

---

# Unlocked by This

> [!tip] The Lorentz Transformation *(from §1.1)*
> The two postulates, taken together, determine essentially uniquely the coordinate transformation between inertial frames — the **Lorentz transformation** ([[Def - The Lorentz Transformation]]). Everything in the topic is a logical consequence of these two statements.

> [!tip] The Equivalence Principle *(from General Relativity)*
> Special relativity privileges inertial frames and treats acceleration as absolute. **General relativity** begins by promoting the freely-falling frame to the fundamental object and declaring, via the **equivalence principle**, that gravity is locally indistinguishable from acceleration — so that "inertial" becomes a local, frame-by-frame notion on a curved spacetime.
