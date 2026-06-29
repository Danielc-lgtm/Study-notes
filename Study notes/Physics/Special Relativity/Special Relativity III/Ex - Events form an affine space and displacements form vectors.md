---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Four-Vector"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\mathcal{E}$ be Minkowski spacetime, an affine space whose points are events. Fix two inertial coordinate systems related by a **Poincaré transformation** — a Lorentz transformation $\Lambda$ followed by a translation $a^\mu$:
$$
x'^\mu = \Lambda^\mu{}_\nu\, x^\nu + a^\mu.
$$

1. Show that the coordinate tuple $x^\mu$ of a single event does **not** transform as a four-vector (i.e. not by $\Lambda$ alone), but that the difference $\Delta x^\mu = x_Q^\mu - x_P^\mu$ of the coordinates of two events $P, Q$ **does**.
2. Verify Chasles' relation $\overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR}$ for displacements, and explain why it expresses the consistency of "going from $P$ to $R$ via $Q$".
3. Conclude that the [[Def - The Spacetime Interval|interval]] $\Delta s^2 = \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$ between two events is well-defined (independent of the choice of origin), whereas "the interval of a single event from nowhere" is not.

**Recall:**

An **affine space** is a set of points $\mathcal{E}$ with an associated vector space $E$ of displacements, such that fixing any origin $O$ makes $M \mapsto \overrightarrow{OM}$ a bijection and $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ (Chasles). A [[Def - Four-Vector|four-vector]] is an element of $E$, equivalently a quantity whose components transform by $\Lambda$:

![[Def - Four-Vector#The Definition]]

A **Poincaré transformation** is a [[Def - The Lorentz Transformation|Lorentz transformation]] composed with a translation; the translation is the shift of origin that the affine structure permits.

---

# Convergent Strategy

**Problem class.** A *structural verification* — confirm that the objects of the theory (events, displacements) have the affine structure claimed, and that the four-vector transformation law is exactly what distinguishes displacements from points. The [[Special Relativity III — Minkowski Spacetime and the Metric#Problem-Solving Strategy|topic strategy]] places this at the foundation: knowing what is and is not a four-vector is prerequisite to every later computation.

**Assumption pattern.** The transformation between frames is *Poincaré*, not merely Lorentz — it carries an additive constant $a^\mu$. That additive constant is the entire content of the problem: it is what an origin shift adds to event coordinates, and what cancels in a difference. Spotting that the inhomogeneous term $a^\mu$ is present is the whole recognition step.

**Theorem routing.** Direct computation. Apply the Poincaré law to $x_P^\mu$ and $x_Q^\mu$ separately and subtract; the constant $a^\mu$ cancels, leaving $\Delta x'^\mu = \Lambda^\mu{}_\nu\Delta x^\nu$, the [[Def - Four-Vector|four-vector transformation law]]. Then invariance of the [[Def - The Spacetime Interval|interval]] follows because $\Delta x^\mu$ transforms by $\Lambda$ and $\Lambda^{\mathsf T}\eta\Lambda = \eta$.

**Key decision point.** The crux is recognising that "transforms as a four-vector" means transforms *homogeneously* (by $\Lambda$ alone, no additive constant), and that the additive constant in the Poincaré law is precisely what disqualifies single-event coordinates while sparing differences. The natural but wrong alternative is to treat $x^\mu$ as a vector because it "is a list of four numbers"; the affine structure is exactly the warning against this.

---

# Legal Operations Used

1. **Operation 2 (compute the scalar product by the Minkowski matrix):** used in part 3 to write the interval $\Delta s^2 = \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$ and confirm its invariance.

2. **Operation 5 (evaluate an invariant in a convenient frame):** the interval, being built from the four-vector $\Delta x^\mu$, is frame-independent — the conclusion of part 3.

3. **Illegal-but-tempting operation 2 (treating an event as a four-vector):** this exercise is the explicit demonstration of why that operation is illegal, and the repair (use differences).

---

# Hints

> [!note]- Hint 1
> Apply the Poincaré law to a single event: $x'^\mu = \Lambda^\mu{}_\nu x^\nu + a^\mu$. The presence of $a^\mu$ means $x^\mu$ does not transform by $\Lambda$ alone — it picks up the constant. So the tuple of one event is not a four-vector.

> [!note]- Hint 2
> Now apply the law to *two* events $P$ and $Q$ and subtract: $x_Q'^\mu - x_P'^\mu = (\Lambda^\mu{}_\nu x_Q^\nu + a^\mu) - (\Lambda^\mu{}_\nu x_P^\nu + a^\mu)$. Watch the $a^\mu$ terms cancel.

> [!note]- Hint 3
> For Chasles: write $\overrightarrow{PQ} = x_Q - x_P$, $\overrightarrow{QR} = x_R - x_Q$, $\overrightarrow{PR} = x_R - x_P$ (in any one frame). Add the first two and the $x_Q$ terms cancel. The relation says the net displacement is path-independent.

> [!note]- Hint 4
> For part 3: the interval is $\eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$, built entirely from the difference $\Delta x^\mu$, which transforms by $\Lambda$. Since $\Lambda^{\mathsf T}\eta\Lambda = \eta$, the interval is unchanged. A "single event's interval" would require $\eta_{\mu\nu}x^\mu x^\nu$, which changes under the origin shift $a^\mu$ — not well-defined.

---

# Solution

The additive constant $a^\mu$ in the Poincaré law is the affine structure made visible: it shifts single-event coordinates (disqualifying them as four-vectors) but cancels in differences (qualifying displacements). Step 1 shows single events fail and differences succeed; Step 2 verifies Chasles; Step 3 concludes the interval is well-defined because it is built from a difference.

**Step 1: single-event coordinates pick up $a^\mu$; differences do not.**

> [!note]- Derivation
> Under the Poincaré transformation, a single event transforms as
> $$x'^\mu = \Lambda^\mu{}_\nu x^\nu + a^\mu,$$
> which contains the additive constant $a^\mu$. The [[Def - Four-Vector|four-vector transformation law]] is $X'^\mu = \Lambda^\mu{}_\nu X^\nu$, *homogeneous* — no additive term. Since $x^\mu$ acquires $a^\mu$, it does **not** transform as a four-vector. Now take two events $P, Q$:
> $$x_Q'^\mu - x_P'^\mu = \big(\Lambda^\mu{}_\nu x_Q^\nu + a^\mu\big) - \big(\Lambda^\mu{}_\nu x_P^\nu + a^\mu\big) = \Lambda^\mu{}_\nu\big(x_Q^\nu - x_P^\nu\big).$$
> The constants $a^\mu$ cancel, leaving $\Delta x'^\mu = \Lambda^\mu{}_\nu\Delta x^\nu$ — the homogeneous four-vector law. So the displacement $\overrightarrow{PQ} = \Delta x^\mu$ **is** a four-vector, while the position of a single event is not. The affine structure is exactly this: points carry an origin-dependent label, displacements between points do not.

**Step 2: Chasles' relation holds and expresses path-independence.**

> [!note]- Derivation
> In any one frame, with $\overrightarrow{PQ} = x_Q - x_P$, $\overrightarrow{QR} = x_R - x_Q$, $\overrightarrow{PR} = x_R - x_P$:
> $$\overrightarrow{PQ} + \overrightarrow{QR} = (x_Q - x_P) + (x_R - x_Q) = x_R - x_P = \overrightarrow{PR}.$$
> The $x_Q$ terms cancel — the intermediate event $Q$ drops out. This is Chasles' relation, and it says the total displacement from $P$ to $R$ is the same whether computed directly or via $Q$: displacement is additive and path-independent, the defining compatibility of the affine structure. (It is frame-independent because each displacement is a four-vector and the relation is linear.)

**Step 3: the interval is well-defined; a single-event "interval" is not.**

> [!note]- Derivation
> The [[Def - The Spacetime Interval|interval]] between $P$ and $Q$ is
> $$\Delta s^2 = \eta_{\mu\nu}\,\Delta x^\mu\Delta x^\nu, \qquad \Delta x^\mu = x_Q^\mu - x_P^\mu.$$
> It is built entirely from the displacement four-vector $\Delta x^\mu$, which transforms by $\Lambda$. Hence
> $$\Delta s'^2 = \eta_{\mu\nu}\Delta x'^\mu\Delta x'^\nu = \eta_{\mu\nu}\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta\Delta x^\alpha\Delta x^\beta = (\Lambda^{\mathsf T}\eta\Lambda)_{\alpha\beta}\Delta x^\alpha\Delta x^\beta = \eta_{\alpha\beta}\Delta x^\alpha\Delta x^\beta = \Delta s^2,$$
> using $\Lambda^{\mathsf T}\eta\Lambda = \eta$. It is also independent of the origin: shifting $O$ adds $a^\mu$ to both $x_P$ and $x_Q$, which cancels in $\Delta x^\mu$. By contrast, a putative "interval of a single event from the origin", $\eta_{\mu\nu}x^\mu x^\nu$, changes under the origin shift $x^\mu \mapsto x^\mu - a^\mu$, so it is *not* a well-defined geometric quantity — there is no canonical origin to measure it from. Only intervals *between* events are physical.

> [!note]- Complete formal solution
> Under $x'^\mu = \Lambda^\mu{}_\nu x^\nu + a^\mu$, a single event's coordinates acquire the additive constant $a^\mu$, so $x^\mu$ does not satisfy the homogeneous four-vector law $X'^\mu = \Lambda^\mu{}_\nu X^\nu$. Subtracting the law for two events, $x_Q'^\mu - x_P'^\mu = \Lambda^\mu{}_\nu(x_Q^\nu - x_P^\nu)$ — the $a^\mu$ cancels — so $\Delta x^\mu = \overrightarrow{PQ}$ is a four-vector. Chasles' relation $\overrightarrow{PQ} + \overrightarrow{QR} = (x_Q - x_P) + (x_R - x_Q) = x_R - x_P = \overrightarrow{PR}$ holds, expressing path-independence of displacement. The interval $\Delta s^2 = \eta_{\mu\nu}\Delta x^\mu\Delta x^\nu$ is therefore invariant ($\Lambda^{\mathsf T}\eta\Lambda = \eta$) and origin-independent ($a^\mu$ cancels in $\Delta x^\mu$), whereas $\eta_{\mu\nu}x^\mu x^\nu$ for a single event changes under an origin shift and is not well-defined. $\blacksquare$

---

# Key Takeaways

**A four-vector transforms homogeneously; an event's coordinates do not — and the affine structure is exactly this distinction.** The single most consequential foundational fact of the chapter is that Minkowski spacetime is an *affine* space, with no canonical origin, so the coordinates of a single event are not intrinsic: they shift by a constant under a change of origin. The four-vector transformation law $X'^\mu = \Lambda^\mu{}_\nu X^\nu$ is *homogeneous* — it has no additive term — and that is precisely what disqualifies single-event coordinates and qualifies differences of events. The trigger to recognise this everywhere: any time you are tempted to add two events, scale an event, or speak of "the position four-vector of an event", stop and ask whether you mean the *displacement from a chosen origin* (legal, a four-vector) or the bare point (not a four-vector). The relativistic position "four-vector" $x^\mu$ is an abuse of language tolerable only once an origin is fixed; the honest objects are displacements.

**The constant $a^\mu$ cancelling in a difference is the mechanism behind every "only differences are physical" statement in relativity.** This exercise isolates the algebraic reason: the Poincaré translation adds the same $a^\mu$ to every event, so it survives in absolute positions and vanishes in relative ones. The same cancellation recurs throughout the subject — proper time depends on the difference of events along a worldline, not on absolute coordinates; the interval depends on the separation, not on where you put the origin; energy and momentum differences are what conservation laws constrain. The reusable diagnostic: whenever a quantity must be physical (observer- and origin-independent), check that it is built from *differences* of event coordinates, equivalently from genuine four-vectors, and not from absolute positions. A quantity that changes under an origin shift is a coordinate artefact, not a geometric fact.

**Chasles' relation is the consistency condition that makes "displacement" a well-defined composition, and it is what an affine space adds beyond a bare set of points.** The relation $\overrightarrow{PQ} + \overrightarrow{QR} = \overrightarrow{PR}$ looks trivial in coordinates but carries the structural content that displacements *compose*: the vector from $P$ to $R$ is the sum of the legs, independent of the intermediate $Q$. This is what lets worldlines be built by concatenating timelike displacements, what makes the four-velocity a well-defined tangent vector, and what underlies the corollary that a sum of future-causal displacements is a future-causal displacement ([[Thm - Two Lemmas on Causal Vectors|the convexity corollary]]). The transferable lesson is that the affine axioms are not bureaucratic: they are exactly the rules that let geometry be done with displacements as the primitive vectorial objects, with points as the things displacements act on.
