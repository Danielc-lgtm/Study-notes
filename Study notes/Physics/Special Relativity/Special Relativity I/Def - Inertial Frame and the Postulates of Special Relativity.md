---
type: definition
subject: special-relativity
prereqs:
  - "Def - Galilean Spacetime and Its Failure"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ throughout (the speed of light is a conversion factor between time units and length units; choosing to measure time in metres makes it disappear — see the topic page registry). Where a formula reads more naturally with $c$ restored, both forms are given. Points of spacetime are **events**; in a frame an event carries coordinates $(t, x, y, z)$, written collectively $x^\mu$ with $\mu = 0,1,2,3$ and $x^0 = t$. Spatial three-vectors are bold, $\mathbf{v} = (v_x, v_y, v_z)$; their Euclidean length is $|\mathbf{v}|$. We write $S, S'$ for inertial frames and $O, O'$ for the inertial observers who carry them. Full registry on [[Special Relativity I — Postulates and Lorentz Transformations]].

This is a compound page: it defines three interlocking notions — the **inertial frame**, the **principle of relativity**, and the **constancy of the speed of light** — because the two postulates are stated *relative to* the inertial frame and none of the three is usable without the others.

---

# Axiom Motivation

Newtonian mechanics already contains the seed of relativity, and naming that seed precisely is the first job. A free particle — one subject to no force — moves in a straight line at constant velocity. This is the law of inertia, and it is not true in every coordinate system: on a spinning carousel a free particle appears to curve, and a passenger feels a centrifugal push that no force put there. So the law of inertia picks out a privileged class of coordinate systems — the ones in which free particles really do go straight — and these are the **inertial frames**. The whole of mechanics is written in them. The first design decision is therefore forced: relativity must be a statement about inertial frames specifically, not about arbitrary coordinates, because only inertial frames carry the law of inertia that makes "velocity" and "force" mean what we expect.

Why elevate "the laws are the same in every inertial frame" to a postulate, rather than deriving it? Because the alternative is a preferred frame — a cosmic rest frame against which all velocity is measured absolutely — and every experiment ever done says there is no such thing. Galileo's fish swimming in a bowl below decks cannot tell whether the ship is moving; no mechanical experiment performed inside a smoothly-moving cabin reveals its velocity. If some inertial frame were genuinely special, a sufficiently careful experiment would find it. None ever has. The **principle of relativity** is the formal renunciation of a preferred frame: only *relative* velocity between inertial frames is observable, and the laws of physics take the *same form* in all of them. Drop this postulate and you must explain which frame is special and why nothing detects it; that is a worse theory.

The second postulate is the bombshell, and the motivation for it is empirical and reluctant. The first postulate alone is satisfied by Newtonian mechanics with its **Galilean transformation** $x' = x - vt$, $t' = t$ (see [[Def - Galilean Spacetime and Its Failure|Galilean spacetime]]), in which velocities simply add: run towards a signal at speed $u$ and it approaches you at $u + v$. Apply this to light and you predict that a beam approaching at $c$ in one frame approaches at $c - v$ in a frame chasing it. Maxwell's electromagnetism, however, hands down a single definite speed $c = 1/\sqrt{\varepsilon_0 \mu_0}$ with no reference to any frame, and the Michelson–Morley experiment — searching for the motion of the Earth through the supposed medium of light — found exactly nothing: light travels at $c$ regardless of the laboratory's motion. So the speed of light is the same in every inertial frame. This is the **constancy of the speed of light**, and it is flatly incompatible with the Galilean velocity-addition rule. One of the two must go, and the experiments insist it is the Galilean rule, hence (since $t' = t$ is what makes velocities add) absolute time itself.

It is worth stressing what would break if either postulate were weakened. Drop the principle of relativity, keeping a preferred ether frame, and you are back to nineteenth-century physics — internally consistent, but contradicted by Michelson–Morley and by the absence of any detectable ether wind. Drop the constancy of light, keeping the Galilean transformation, and Maxwell's equations are no longer valid in every inertial frame (a light wave would travel at $c \pm v$, and the wave equation is simply not Galilean-invariant), so electromagnetism would have to be rewritten with a preferred frame — again contradicted by experiment. Weaken "same speed independent of the source" to "same speed only for a source at rest in the frame" and you re-import an ether by the back door. The two postulates are exactly the minimal pair: the first is the old Galilean principle kept intact, the second is the one new experimental fact, and the entire content of [[Special Relativity I — Postulates and Lorentz Transformations|special relativity]] is the logical consequence of holding both at once. The price — extracted in [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|the uniqueness theorem]] — is that the clause $t' = t$ must be abandoned: clocks in relative motion no longer agree.

One subtlety deserves a sentence, because it is the hinge of the [[Ex - The operational synchronisation of clocks|twin paradox]] and of every "but isn't it symmetric?" objection. Uniform velocity is relative and undetectable; **acceleration is absolute and detectable**. An observer who accelerates feels it — an accelerometer reads nonzero, coffee spills — and no appeal to a frame is needed to decide who accelerated. Inertial observers are precisely the non-accelerating ones, and only between *inertial* observers does the principle of relativity assert equivalence. This is why "inertial" is in the definition and not a throwaway adjective.

---

# The Definition

An **inertial frame** (or inertial reference frame, equivalently *inertial coordinate system*, ICS) is a coordinate system $(t, x, y, z)$ on spacetime in which the **law of inertia** holds: every free particle (one subject to no net force) moves with constant velocity, tracing a straight line in the coordinates. An inertial frame is fixed by a choice of spatial origin, a right-handed orthonormal set of spatial axes, and a choice of zero for time; two inertial frames are in uniform relative motion (constant relative velocity, no rotation, no acceleration).

**Special relativity** rests on two postulates, both asserted for inertial frames:

> **Postulate 1 (Principle of Relativity).** The laws of physics take the same form in every inertial frame. Equivalently, no inertial frame is preferred: only the relative velocity between inertial frames is physically meaningful.

> **Postulate 2 (Constancy of the Speed of Light).** Light propagates in vacuum with the same speed $c$ in every inertial frame, independent of the direction of propagation and independent of the motion of the source.

With $c = 1$ the second postulate says every light ray has $|\mathbf{v}| = 1$ in every frame. The two postulates together determine the coordinate transformation relating any two inertial frames uniquely — it is the [[Def - The Lorentz Transformation|Lorentz transformation]], derived in [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|§1.2]] — and force the abandonment of the absolute time $t' = t$ of [[Def - Galilean Spacetime and Its Failure|Galilean spacetime]].

An equivalent, more operational characterisation of an inertial frame (Einstein's own, 1905) does not assume rods and a universal clock a priori but *constructs* the coordinates: an inertial observer carries a single clock and a source of light, assigns to a distant event the time and position obtained by the **radar method** — bounce a light signal off the event, record the round-trip time $\Delta t$, assign time $\Delta t / 2$ and distance $c\,\Delta t / 2$ — and synchronises distant clocks by light signals (see [[Ex - The operational synchronisation of clocks]]). The two definitions agree, and the operational one makes manifest that simultaneity is a *choice of synchronisation* and hence frame-dependent.

---

# Categorical / Structural Definition

The structural content of "inertial frame plus the two postulates" is that the set of inertial frames carries a transitive action of a single transformation group, and the postulates pin down which group. An inertial frame is a choice of affine coordinates on spacetime; passing from one inertial frame to another is a coordinate change; the principle of relativity says the *family* of allowed changes is the symmetry group of the laws of physics, and the constancy of light says that group must fix the speed of light. The group that results is the [[Def - The Poincaré Group|Poincaré group]] (the [[Def - The Lorentz Group|Lorentz group]] together with spacetime translations), and "physics is the same in all inertial frames" becomes the precise statement that the laws are **Poincaré-invariant**.

This is exactly parallel to the Galilean case, and the parallel is the cleanest way to see what changed. Newtonian mechanics is invariant under the **Galilean group**; special-relativistic physics is invariant under the **Poincaré group**; the two groups differ in their boost subgroup — Galilean boosts shear time-slices rigidly ($t' = t$), Lorentz boosts rotate time into space. The choice of postulates is the choice of invariance group, and every later structure of the subject (four-vectors, tensors, the metric) is built to make Poincaré-invariance manifest. A reader who knows Lie groups should hold onto this: choosing the postulates is choosing $\mathrm{ISO}(1,3)$ over the Galilean group, and the rest is representation theory.

---

# Relate to Other Fields / Compression

In the language of symmetry and group actions, an inertial frame is a point in the homogeneous space on which the [[Def - The Poincaré Group|Poincaré group]] acts simply transitively, and the postulates are the assertion that this group — not the larger group of all smooth coordinate changes, and not the smaller Galilean group — is the symmetry of physics. This is the same move made throughout physics: identify the invariance group, and the dynamics must be built from its invariants. Newtonian mechanics uses the Galilean group; non-relativistic quantum mechanics uses its central extension; field theory uses Poincaré; general relativity enlarges the group to all diffeomorphisms (general covariance) and the inertial frame survives only locally.

**True name:** an inertial frame is *the rest frame of a non-accelerating observer* — equivalently, the frame in which a free particle's worldline is straight — and the postulates are *"there is no preferred such frame, and light is one of the things they all agree on."* The operational true name is sharper still: an inertial frame is *what you build with one clock and a flashlight by the radar method*, which is why simultaneity is a synchronisation convention and not a fact about the world.

---

# Examples / Corollaries

**Is an instance — a freely-coasting spaceship.** A ship with its engines off, far from any mass, carries an inertial frame: a ball released inside floats in a straight line, an accelerometer reads zero, and no experiment inside reveals the ship's velocity relative to anything. Two such ships passing at constant relative velocity are related by a [[Def - The Lorentz Transformation|Lorentz transformation]].

**Is an instance — a laboratory in free fall (locally).** A windowless lift in free fall is, over a small enough region and time, an inertial frame: everything inside floats, and special relativity holds. This is the seed of the **equivalence principle**, and the qualifier "locally" is the entire difference between special and general relativity — gravity cannot be transformed away everywhere at once, only at one event.

**Is NOT an instance — a rotating turntable.** A coordinate system fixed to a spinning carousel is *not* inertial: a free puck appears to spiral outward, a passenger feels a centrifugal force with no agent, and a Foucault pendulum precesses. The law of inertia fails, so the postulates do not apply in these coordinates; one must transform to a non-rotating frame first.

**Is NOT an instance — an accelerating rocket.** A frame fixed to a rocket firing its engines is not inertial: released objects fall to the back, an accelerometer reads nonzero, and the acceleration is absolute and felt. This is precisely the asymmetry that resolves the [[Ex - The operational synchronisation of clocks|twin]] puzzle — the accelerating observer is physically distinguished.

**Corollary — the Galilean transformation is the only survivor at low speed.** Setting the second postulate aside and demanding $t' = t$ forces the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]] $x' = x - vt$; the two postulates together instead force the Lorentz transformation, which *reduces* to the Galilean one when $|v| \ll 1$ (see [[Ex - Recovering the Galilean transformation in the low-speed limit]]). The postulates do not overturn Newton; they correct him by terms of order $v^2/c^2$.

**Corollary — light rays are the calibration of every frame.** Because the second postulate fixes light at $c$ in all frames, a light ray is the one worldline every inertial observer agrees about; on a [[Def - Spacetime Diagram|spacetime diagram]] it is the $45^\circ$ line, and the axes of every frame scissor symmetrically about it. The light ray is the shared scaffolding from which the operational coordinates are built.

**Calibration check.** If you have understood the definitions you should be able to: (1) explain why a frame fixed to the surface of the Earth is only *approximately* inertial, and name the two effects that spoil it (rotation and gravity); (2) state which postulate the Galilean transformation violates (the second) and which it satisfies (the first); and (3) say, for two observers who disagree about whether two distant events are simultaneous, why neither is wrong — because simultaneity is a synchronisation convention fixed by the radar method *within* each frame.

---

# Unlocked by This

> [!tip] The Lorentz and Poincaré Groups *(from §1.2 and SR IV / SR XII)*
> The set of transformations between inertial frames, forced by these postulates, is the [[Def - The Lorentz Transformation|Lorentz transformation]]; the collection of all of them forms the [[Def - The Lorentz Group|Lorentz group]], and adjoining translations gives the [[Def - The Poincaré Group|Poincaré group]]. "Physics is the same in all inertial frames" becomes "the laws are Poincaré-invariant", the organising principle of all relativistic physics.

> [!tip] Local Inertial Frames and the Equivalence Principle *(from General Relativity)*
> The inertial frame survives gravity only locally. Einstein's **equivalence principle** asserts that at any one event one can choose a freely-falling frame — a *locally inertial frame* — in which the laws of physics are exactly those of special relativity and gravity disappears. The impossibility of doing this *globally* is curvature, and the failure of a single inertial frame to cover all of spacetime is the entire content of **general relativity**. Special relativity is the theory of the one global inertial frame that exists only when gravity is absent.

> [!tip] Lorentz Invariance as a Design Principle *(from QFT)*
> The demand that a physical law take the same form in every inertial frame — **Lorentz invariance** — becomes, in relativistic quantum field theory, the rule that every term in a Lagrangian must be a Lorentz scalar. The postulates here are the physical origin of that constraint, and the classification of particles by mass and spin is the classification of the irreducible representations of the group these postulates single out.
