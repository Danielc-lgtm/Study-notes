---
type: definition
subject: special-relativity
prereqs:
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
  - "Def - Classification of Four-Vectors"
  - "Def - The Four-Momentum of a Photon"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] $\mathcal{O}$ has proper acceleration $a$, worldline the hyperbola $(ax_*+1)^2 - (act_*)^2 = 1$ in the inertial coordinates $(ct_*, x_*, y_*, z_*)$ of the reference inertial observer $\mathcal{O}_*$. The hyperbola has centre $A = (ct_*, x_*) = (0, -a^{-1})$ and asymptotes $\Delta_1: ct_* = x_* + a^{-1}$ and $\Delta_2: ct_* = -x_* - a^{-1}$. A vector $N$ is **null** if $N\cdot N = 0$; light rays are null geodesics, straight $45^\circ$ lines in inertial coordinates. Full registry on [[Special Relativity XVI — Accelerated Observers]].

---

# Axiom Motivation

The motivation is a single startling observation: an observer who accelerates forever can permanently outrun light. We want to make precise the region of spacetime from which no signal ever reaches such an observer, and to name its boundary.

Start from the picture. The uniformly accelerated observer's worldline is a hyperbola that, in the far future, hugs its asymptote $\Delta_1$ — the null line $ct_* = x_* + a^{-1}$ — approaching it but never crossing it, because the observer's speed approaches $c$ without reaching it. Now consider a photon emitted from some event behind the observer. The photon travels on a straight $45^\circ$ line. If it is emitted from far enough back, its worldline runs *parallel* to the asymptote $\Delta_1$, or below it, and the hyperbola — forever staying above $\Delta_1$ — is forever just out of the photon's reach. The photon chases the accelerating observer but the gap, measured along the observer's ever-tilting rest spaces, never closes. The observer never sees the photon, never sees the emission event, never sees anything in the region the photon came from.

This is genuinely surprising and worth dwelling on, because nothing physical blocks the light. There is no obstacle, no absorber, no curvature. The light is emitted, travels at $c$ in a straight line, and simply never arrives, purely because the observer keeps accelerating away. The instant the observer *stops* accelerating — levels off to constant velocity — their worldline becomes a straight line that the photon immediately catches, and the hidden region becomes visible. So the inaccessibility is a feature of the *observer's* eternal acceleration, not of spacetime.

What we want to define, then, is the boundary between the events that can send light to the observer and the events that cannot. The desideratum is a clean characterisation of this boundary as a surface in spacetime. Working out the condition (the exercise [[Ex - The Rindler horizon and the light that never catches up]] does the computation) shows that an event $M$ with inertial coordinates $(ct_*^{\mathrm{em}}, x_*^{\mathrm{em}}, \ldots)$ can send a photon to the observer if and only if $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} > -a^{-1}$, and cannot if $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} \le -a^{-1}$. The boundary is the hyperplane $ct_* = x_* + a^{-1}$ — exactly the asymptote $\Delta_1$, promoted from a line in the plane to a hyperplane in spacetime.

The choice to call this a *horizon* is motivated by analogy with black holes, and the analogy is precise enough to be the reason the construction matters. A black hole's **event horizon** is the boundary of the region from which light cannot escape to infinity; the Rindler horizon is the boundary of the region from which light cannot reach the accelerating observer. Both are null surfaces, both hide a region forever, and both are the locus where the relevant worldlines (escaping light; the accelerating observer) asymptote to the speed of light. The crucial *disanalogy*, which the definition must keep in view, is that the black-hole horizon is **intrinsic** — fixed by the spacetime geometry, the same for everyone — whereas the Rindler horizon is **observer-dependent**, an artifact of one observer's choice to accelerate, vanishing if they stop. The Rindler horizon is the toy model; the black-hole horizon is the real thing the toy model teaches.

---

# The Definition

Let $\mathcal{O}$ be a [[Def - Uniformly Accelerated Observer (Hyperbolic Motion)|uniformly accelerated observer]] of proper acceleration $a$, with worldline the hyperbola $(ax_*+1)^2 - (act_*)^2 = 1$ in the inertial coordinates of $\mathcal{O}_*$. The **Rindler horizon** of $\mathcal{O}$ is the hyperplane $\mathcal{H}$ separating the events that can send a light signal to $\mathcal{O}$ from those that cannot:
$$
\mathcal{H}:\qquad ct_* = x_* + a^{-1},
$$
equivalently the set of events with $x_* - ct_* = -a^{-1}$ in the plane $\Pi$, extended over all $y_*, z_*$. An event $M$ can send a photon that reaches $\mathcal{O}$ if and only if it lies on the accessible side, $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} > -a^{-1}$; events with $x_*^{\mathrm{em}} - ct_*^{\mathrm{em}} \le -a^{-1}$ are forever invisible to $\mathcal{O}$.

$\mathcal{H}$ is a **null hyperplane**: the metric induced on it by $\eta$ is degenerate. Concretely, a normal vector to $\mathcal{H}$ — found from the gradient of $x_* - ct_* + a^{-1}$ — is proportional to $e_0^* + e_1^*$, which satisfies $(e_0^* + e_1^*)\cdot(e_0^* + e_1^*) = 1 - 1 = 0$ and is therefore **null**. A null normal is also *tangent* to the hyperplane (it is orthogonal to itself), so $\mathcal{H}$ contains its own normal direction; this is the defining feature of a null hyperplane, the three-dimensional analogue of a null line.

In the $1+1$-dimensional plane $\Pi$, $\mathcal{H}$ reduces to the asymptote $\Delta_1$ of the hyperbola. All observers fixed in $\mathcal{O}$'s accelerated frame (the comoving observers of [[Thm - Clock Synchronization and Desynchronization in an Accelerated Frame]]) share the *same* Rindler horizon $\mathcal{H}$, since their worldlines are hyperbolae with the same asymptotes.

---

# Relate to Other Fields / Compression

The Rindler horizon is the flat-spacetime, observer-dependent prototype of the **event horizon** of a black hole. The dictionary is exact at the level of the local geometry: the proper acceleration $a$ corresponds to the **surface gravity** $\kappa$ of the black hole, the Rindler wedge $x_* > |ct_*|$ corresponds to the exterior of the hole, and the bifurcation event $A = (0, -a^{-1})$ where the two asymptotes cross corresponds to the bifurcation surface where the past and future horizons meet. Near the horizon, the Schwarzschild metric in the appropriate coordinates *is* the Rindler metric to leading order, which is why the Rindler observer is the standard local model of an observer hovering just outside a black hole.

**True name:** the Rindler horizon is *the boundary of the causal past of the accelerated observer's entire worldline* — the set of events that, even given infinite time, can never send a signal to the observer. It is a causal boundary, not a physical barrier.

The single most important distinction to compress and remember is **intrinsic versus observer-dependent**. The event horizon of a black hole is a property of the spacetime: it is there whether or not anyone is watching, and an observer must take drastic action (fire engines outward forever, or fall in) to interact with it. The Rindler horizon is a property of the *observer*: it exists only because they accelerate, and they dissolve it by coasting. Tong's gloss is the memorable one — if an accelerated observer wants to see behind their horizon, they just stop accelerating; an observer who wants to see behind a black hole's horizon must be considerably braver.

---

# Examples / Corollaries

**Is an instance — the asymptote of the worldline hyperbola.** In the plane $\Pi$, the Rindler horizon is precisely the null line $\Delta_1: ct_* = x_* + a^{-1}$ that the observer's hyperbola approaches in the infinite future. The horizon is "where the observer is heading but never arrives".

**Is an instance — the light cone of the bifurcation event.** The Rindler horizon, together with its mirror $\Delta_2$, is the light cone of the centre event $A = (0, -a^{-1})$. Events inside the future light cone of $A$ can reach the observer; the future horizon $\mathcal{H}$ is the future light cone's boundary.

**Is NOT an instance — the rest space of the observer.** It is tempting to confuse the horizon with one of the observer's local rest spaces $\mathcal{E}_u(t)$ (the straight lines through $A$ of slope $\tanh(act)$). They are different: the rest spaces are *spacelike* hyperplanes that pivot about $A$ and sweep up to but never reach the slope $\pm 1$, whereas the horizon is the *null* hyperplane of slope exactly $1$ that is the limit of the rest spaces as $t\to+\infty$. The horizon is the limiting rest space, not any actual one.

**Is NOT an instance — a black-hole event horizon.** Although the local geometry matches, the Rindler horizon is not an event horizon: it carries no curvature, hides nothing from an inertial observer, and disappears when the accelerated observer stops accelerating. Treating it as a real, intrinsic horizon is the standard conceptual error the definition exists to forestall.

**Corollary — the horizon is a one-way membrane for the family of comoving observers.** Signals can cross $\mathcal{H}$ from the accessible side to the observer, but no signal the observer sends ever crosses back to the hidden side within the wedge: the hidden region is causally disconnected from the observer's future as well as their past. This one-way character is exactly the property that makes it the model for a black-hole horizon.

**Calibration check.** If the definition is understood, the reader should be able to: (i) state the equation of the horizon and verify its normal $e_0^* + e_1^*$ is null; (ii) explain why a photon emitted from $(b, 0)$ with $b > a^{-1}$ reaches the observer while one from $b < -a^{-1}$ does not, by drawing the $45^\circ$ line and the hyperbola; and (iii) name the two features that distinguish the Rindler horizon from a black-hole event horizon (observer-dependence; absence of curvature).

---

# Unlocked by This

> [!tip] The Unruh Effect *(from quantum field theory in curved spacetime)*
> The existence of the Rindler horizon is what makes the **Unruh effect** possible. A quantum field has degrees of freedom on both sides of $\mathcal{H}$, but the accelerated observer can only access the modes on their side; tracing out the modes hidden behind the horizon turns the pure Minkowski vacuum into a *mixed*, thermal state. The accelerated observer therefore perceives a thermal bath at the **Unruh temperature** $T = \hbar a/(2\pi c k_B)$. The horizon is essential — without a hidden region there is nothing to trace out, and no temperature. This is the cleanest illustration that horizons and thermodynamics are linked, and it is the special-relativistic template for **Hawking radiation**, where the black-hole event horizon plays the role of $\mathcal{H}$ and the surface gravity plays the role of $a$.

> [!tip] Black-Hole Thermodynamics and the Membrane Paradigm *(from General Relativity)*
> Promoting the Rindler horizon to a black-hole **event horizon** opens the whole of black-hole thermodynamics: the horizon has an entropy proportional to its area (Bekenstein–Hawking), a temperature proportional to its surface gravity, and obeys laws formally identical to the laws of thermodynamics. The near-horizon Rindler approximation is the technical device by which a hovering observer's local physics — including the temperature they measure — is computed, and the **membrane paradigm** treats the horizon as a physical membrane with electrical and viscous properties, all built on the Rindler model of the horizon as a null surface that hides a region.
