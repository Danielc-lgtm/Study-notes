---
type: definition
subject: special-relativity
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, restoring $c$ where useful. A spacetime diagram is drawn in a fixed inertial frame $S$ with the time axis (labelled $ct$, or $t$ when $c = 1$) **vertical** and one spatial axis $x$ **horizontal**; an event is a point, with coordinates written $(ct, x)$ — vertical coordinate first. A particle's history is its **worldline**. A second frame $S'$ moves at velocity $v$ along $x$. Slopes are measured from the horizontal $x$-axis, so a vertical line has infinite slope and a $45^\circ$ line has slope $1$ (in $c=1$ units, $\Delta(ct)/\Delta x = 1$). Full registry on [[Special Relativity I — Postulates and Lorentz Transformations]].

> [!warning] The diagram is a mnemonic, not a proof
> Every statement read off a spacetime diagram below has an exact algebraic counterpart in the [[Def - The Lorentz Transformation|Lorentz transformation]], and the algebra is the real content. The diagram is a memory aid and a sanity check — never a load-bearing step in a derivation. When a diagram and a calculation seem to disagree, the calculation wins.

---

# Axiom Motivation

Why draw a picture at all, when the [[Def - The Lorentz Transformation|Lorentz transformation]] already says everything? Because the transformation is a formula, and a formula does not show you at a glance whose clock is slow, whose rod is short, or which of two events happens first for a moving observer. The spacetime diagram is engineered so that those questions become *visual*: the answer is read off the geometry of lines on a page. The design goal is a drawing in which (i) the worldline of a particle records its entire history as a single curve, (ii) light has a fixed, frame-independent slope, and (iii) the axes of a boosted frame can be drawn on the *same* diagram so that "what $S'$ calls simultaneous" and "what $S'$ calls staying still" are themselves lines you can see.

The one nontrivial design choice is to plot $ct$ on the vertical axis rather than $t$. The reason is the second postulate. If the vertical axis were $t$ and the horizontal $x$ in mismatched units, a light ray $x = ct$ would have slope $c$ — some steep, unit-dependent number with no special status. Rescale the vertical axis to $ct$ (equivalently, measure time in light-seconds, the distance light travels in that time) and the light ray becomes $x = ct \Rightarrow$ slope $1$, a clean $45^\circ$ line. This is not cosmetic: because the second postulate makes light travel at $c$ in *every* frame, the $45^\circ$ light lines are the one feature all inertial observers agree on, and they become the fixed scaffolding around which every frame's axes are arranged. A diagram whose light cones are at $45^\circ$ is a diagram in which the constancy of $c$ is manifest.

The deeper motivation is what the diagram makes *possible* that prose struggles to: drawing two frames at once. In the Newtonian picture, "now" is a horizontal line shared by everyone, and only "here" (a vertical line) depends on your velocity. The Lorentz transformation breaks this symmetry's asymmetry — it makes "now" velocity-dependent too. On the diagram this shows up as the $S'$ simultaneity lines being *tilted* relative to the $S$ simultaneity lines, by exactly the amount that the $S'$ worldlines are tilted from vertical. The picture in which both axes tilt symmetrically toward the light ray is the picture in which the relativity of simultaneity is obvious, and that is the chief payoff: a confusion that takes paragraphs to untangle in words ("but from $B$'s point of view, isn't $A$ the one moving?") becomes a matter of looking at which line is which.

---

# The Definition

A **spacetime diagram** is a plot of a region of spacetime in a fixed inertial frame $S$, with the time coordinate $ct$ on the vertical axis and a spatial coordinate $x$ on the horizontal axis, units chosen so that $ct$ and $x$ have the same scale (years and light-years, or seconds and light-seconds). A point is an **event**, written $(ct, x)$. The continuous curve traced by a particle is its **worldline**.

The diagram has the following standing features, each a direct consequence of the [[Def - Inertial Frame and the Postulates of Special Relativity|postulates]]:

- **Light rays travel at $45^\circ$.** A light ray has $x = \pm\,ct$, slope $\pm 1$, and — because the speed of light is the same in every frame — *every* inertial observer agrees these lines are light paths. The set of $45^\circ$ lines through an event forms its light cone.
- **Massive worldlines are steeper than $45^\circ$.** A particle of speed $|u| < c$ has worldline slope $c/|u| > 1$ (steeper than the light line); since nothing exceeds $c$, no physical worldline is ever drawn flatter than $45^\circ$. A particle at rest in $S$ traces a vertical line.

For a second inertial frame $S'$ moving at velocity $v$ along $x$, its coordinate axes are drawn on the *same* diagram:

- **The $ct'$-axis** is the locus $x' = 0$ — the worldline of the $S'$ spatial origin — which in $S$ is the line $x = vt$, i.e. $ct = (c/v)\,x$, of slope $c/v > 1$. It tilts *off the vertical toward the light ray* by the angle $\alpha$ with $\tan\alpha = v/c$.
- **The $x'$-axis** is the locus $t' = 0$ — the events $S'$ calls simultaneous with its origin — which from the [[Def - The Lorentz Transformation|Lorentz transformation]] $t' = \gamma(t - vx/c^2) = 0$ is the line $ct = (v/c)\,x$, of slope $v/c < 1$. It tilts *off the horizontal toward the light ray* by the same angle $\alpha$.

Thus **the two boosted axes scissor symmetrically toward the $45^\circ$ light line**: the $ct'$-axis rotates down toward it from the vertical, the $x'$-axis rotates up toward it from the horizontal, each by $\alpha = \arctan(v/c)$. The symmetry about the light ray is the geometric expression of the second postulate (light has slope $1$ in both frames). The axes are **pseudo-orthogonal**: where ordinary perpendicular axes make angles $\theta$ and $\theta + \pi/2$ with the horizontal, the $S'$ axes make angles $\alpha$ and $\pi/2 - \alpha$ — they close up toward the diagonal rather than staying square. A light line, at $\alpha = \pi/4$, is pseudo-orthogonal to *itself*, a phenomenon with no Euclidean analogue.

Lines of constant $t'$ (parallel to the $x'$-axis) are the **simultaneity lines** of $S'$; lines of constant $x'$ (parallel to the $ct'$-axis) are its **lines of constant position**. Because the $x'$-axis is tilted, events simultaneous in $S'$ are generally *not* simultaneous in $S$ — the relativity of simultaneity, read directly off the tilt.

---

# Relate to Other Fields / Compression

A spacetime diagram is the indefinite-signature analogue of an ordinary $x$–$y$ plot under rotation, and the analogy is exact except for one sign. In the Euclidean plane, rotating the axes by $\theta$ sends $(x, y)$-axes to new axes that both turn the *same way* by $\theta$, staying perpendicular, and preserving $x^2 + y^2$ (circles are the invariant curves). On a spacetime diagram, a boost sends the $(ct, x)$-axes to axes that turn *toward each other* (the scissoring), no longer Euclidean-perpendicular, preserving $ct^2 - x^2$ (hyperbolae are the invariant curves). The boost is a hyperbolic rotation through [[Def - Rapidity|rapidity]] $\varphi$ — with $\tanh\varphi = v/c$ — exactly as the Euclidean rotation is through angle $\theta$, and the scissoring instead of co-rotation is the single visible consequence of the metric's minus sign.

**True name:** a spacetime diagram is *a picture of the affine plane $(ct, x)$ on which the second postulate is enforced by fixing light at $45^\circ$, so that a boost appears as the two axes scissoring symmetrically toward the diagonal.* Its true purpose is not to compute but to make simultaneity, ordering, and causal connection *visible* — it is to special relativity what the free-body diagram is to Newtonian mechanics, the standard diagnostic drawing of the subject.

---

# Examples / Corollaries

**Is an instance — the worldline of an inertial particle.** A particle moving at constant velocity $u$ in $S$ has worldline $x = u t$, a straight line through the origin of slope $c/u$ (steeper than $45^\circ$ since $|u| < c$). Its straightness is the law of inertia; its steepness is the speed limit. An accelerating particle has a curved worldline, always steeper than $45^\circ$ at every point.

**Is an instance — a light pulse and its cone.** A flash emitted at the origin traces the two $45^\circ$ lines $x = \pm ct$; the region above them ($ct > |x|$) is the future light cone, reachable from the origin by a sub-light signal, and every inertial observer draws the same cone because all agree light is at $45^\circ$.

**Is NOT a faithful instance — naive Euclidean intuition about the tilted axes.** It is tempting to read the tilted $S'$ axes with a Euclidean ruler and protractor — to say the unit length along the $x'$-axis is the same physical length as along the $x$-axis because "they look the same length on the page". This is *wrong*: the page is Euclidean but the geometry is Minkowskian, so equal physical (interval) lengths along the $x$- and $x'$-axes appear *different* on the page (the $S'$ unit is stretched by a hyperbola-calibration factor). The diagram faithfully shows *which* events are which, but lengths and angles on the paper are not the physical lengths and angles — those are computed from the [[Def - The Spacetime Interval|interval]], not measured with a ruler.

**Is NOT an instance — a worldline flatter than $45^\circ$.** A line of slope less than $1$ (closer to horizontal than the light ray) would represent motion faster than light; it is not the worldline of any physical particle. Such a line *is* a legitimate $S'$ simultaneity line (the $x'$-axis), but as a *worldline* it is forbidden — the same line means a permissible "now-slice" or an impermissible trajectory depending on whether you read it as a set of simultaneous events or as a history.

**Corollary — "now" depends on velocity, just as "here" does.** In the Galilean picture only lines of constant position (vertical lines, "here") tilt with velocity, while lines of constant time (horizontal, "now") are shared. On the spacetime diagram the $x'$-axis tilts too, so "now" — the simultaneity slice — is velocity-dependent. This single extra tilt, absent in [[Def - Galilean Spacetime and Its Failure|Galilean spacetime]], is the geometric source of the relativity of simultaneity (worked through in [[Ex - The boosted axes scissor toward the light ray]]).

**Corollary — the light cone partitions the diagram.** The two $45^\circ$ lines through an event divide the plane into the future cone (above), the past cone (below), and the spacelike "elsewhere" (left and right). Because light is at $45^\circ$ in every frame, this partition is frame-independent: all observers agree which events lie in your future, your past, and your elsewhere — the seed of the invariant causal structure made precise in [[Ex - Why nothing can be drawn flatter than 45 degrees]].

**Calibration check.** You have understood the diagram if you can: (1) draw the $ct'$- and $x'$-axes for a frame moving at $v = c/2$ and state their slopes ($2$ and $1/2$ respectively) and the common tilt angle $\alpha = \arctan(1/2)$; (2) explain why the two boosted axes are symmetric about the $45^\circ$ light line, citing the second postulate; and (3) say why a unit length marked on the $x'$-axis with a Euclidean ruler is *not* the physical unit length, pointing to the interval as the true measure.

---

# Unlocked by This

> [!tip] The Invariant Interval and Calibration Hyperbolae *(from SR III / SR IV)*
> The curves of constant [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \mathrm{const}$ are hyperbolae asymptotic to the light cone, and they are what *calibrate* the tilted axes: the unit tick on the $x'$-axis is where it meets the hyperbola $x^2 - ct^2 = 1$, not where a ruler would put it. These hyperbolae are the Minkowski analogue of the circles that calibrate rotated Euclidean axes, and they make the diagram a quantitative tool.

> [!tip] The Causal Structure and the Light Cone *(from SR III)*
> Because the $45^\circ$ light cone is frame-independent, the diagram's partition into future, past, and elsewhere is an *invariant* — the **causal structure** of spacetime. Two events are causally connectible exactly when one lies in the other's light cone (a worldline steeper than $45^\circ$ joins them); this is the geometric content of the [[Def - Classification of Four-Vectors|timelike/spacelike/null classification]] and the foundation of why nothing outruns light.
