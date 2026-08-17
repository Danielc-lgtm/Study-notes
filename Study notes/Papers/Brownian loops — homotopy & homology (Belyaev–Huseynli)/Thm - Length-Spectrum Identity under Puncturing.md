---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Brownian Loop Measure"
  - "Def - Polar Set"
tags: [paper, hyperbolic-geometry, loop-measures]
---

# Notation

- $X$ — a complete hyperbolic surface without boundary, possibly of infinite type, possibly with cusps or funnels
- $P\subset X$ — a non-empty, closed, [[Def - Polar Set|polar]] set; $X'=X\setminus P$
- $g$, $g'$ — the ambient metric on $X$, and the unique complete hyperbolic metric on $X'$; **these are different metrics**, $g'$ having a cusp at each point of $P$
- $\simeq_X$ — free homotopy as curves in $X$; $\ell_\gamma$, $\ell_{\gamma'}$ — primitive geodesic lengths measured in $X$ and in $X'$ respectively
- $\sigma$ — the conformal factor in a rescaling $g'=e^{2\sigma}g$
- $\phi$ — a Bernstein function; $\kappa\geq0$ a killing rate

---

# Type card

> [!abstract] Type card — Theorem 3.9 (Wang–Xue, length-spectrum identity)
> **Given.** A complete hyperbolic surface $X$ without boundary — possibly of infinite type, possibly with cusps or funnels — a non-empty closed [[Def - Polar Set|polar]] set $P\subset X$, and $X'=X\setminus P$ equipped with **its own** complete hyperbolic metric; a primitive geodesic $\gamma\in\mathcal{P}_X$ and $m\geq1$. Pure Brownian motion only.
>
> **Produces.** An identity between the geodesic length spectra of two different hyperbolic surfaces: a single term on $X$ equals a sum over all the classes on $X'$ that become freely homotopic to it in $X$.
>
> **Lets you.** Trade the two structural properties of the Brownian loop measure — restriction and conformal invariance — for an exact relation between length spectra; and, read the other way, see precisely which property each side of the identity is paying for, and hence why the identity dies for every nonlinear subordination.

---

# Statement

> **Theorem 3.9 (Wang–Xue).** Let $X$ be a complete hyperbolic surface without boundary, possibly of infinite type and possibly with cusps or funnels, and let $P\subset X$ be a non-empty, closed, polar set. Let $X'=X\setminus P$ equipped with its unique complete hyperbolic metric. Then for any $\gamma\in\mathcal{P}_X$ and $m\geq1$,
> $$\frac1m\cdot\frac{1}{e^{m\ell_\gamma}-1} = \sum_{\substack{\gamma'\in\mathcal{P}_{X'},\ m'\geq1\\ \gamma'^{m'}\simeq_X\gamma^m}}\frac{1}{m'}\cdot\frac{1}{e^{m'\ell_{\gamma'}}-1},$$
> where $\simeq_X$ denotes free homotopy as curves in $X$, and $\ell_\gamma$ and $\ell_{\gamma'}$ are the primitive geodesic lengths measured on $X$ and $X'$ respectively.

---

# Why it is true

Both sides are the same loop mass, computed on two surfaces that the loop measure cannot tell apart.

Read the left-hand side as $\mu_X(\mathcal{C}_X(\gamma^m))$, by the Brownian specialisation of [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]]. Now apply the two structural properties in turn. **Restriction** says that removing a set the process never visits changes nothing: since $P$ is polar, $\mu_X$ is supported on loops avoiding $P$, so $\mu_X(\mathcal{C}_X(\gamma^m))=\mu_{X\setminus P,g}(\mathcal{C}_X(\gamma^m))$ with $g$ still the ambient metric. **Conformal invariance** then says the metric may be changed within its conformal class without changing $\mu$: so the ambient $g$ restricted to $X'$ may be replaced by $g'$, the unique complete hyperbolic metric of the punctured surface — a genuinely different metric, with a cusp at each point of $P$.

Having changed the metric, one recomputes the same mass using the geometry of $X'$. But a single free homotopy class in $X$ generally splits into *many* classes in $X'$: loops that were freely homotopic in $X$ may be separated by the punctures. So the mass, computed downstairs on $X'$, is a sum over all classes $\mathcal{C}_{X'}(\gamma'^{m'})$ whose loops become freely homotopic to $\gamma^m$ once the punctures are filled in. Equating the two computations gives the identity.

**The mechanism in one line: restriction says puncturing costs nothing, conformal invariance says the punctured surface may be re-metrised for free, and the identity is the same number computed before and after — with the splitting of one homotopy class into many accounting for the sum.**

Note that the two sides are genuinely about different geometry. The lengths $\ell_{\gamma'}$ are measured in the hyperbolic metric of $X'$, and they are *longer* than the corresponding lengths in $X$ — adding a cusp lengthens the geodesics that have to go around it. The identity is a non-trivial constraint relating two length spectra, not a bookkeeping identity.

---

# Strategy

**Strategy.** Apply restriction to see that the mass is unchanged by deleting a polar set; then apply conformal invariance to replace the restricted metric by the complete hyperbolic metric of $X'$; then recompute the same mass on $X'$, where the single class splits into all the classes that fuse in $X$.

> [!note]- Proof (skippable)
> The paper cites this to Wang–Xue [WX25, Theorem 4.2] and does not reproduce the proof. The argument is exactly the two-step application of restriction and conformal invariance sketched above, with the Brownian mass formula $\mu_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{1}{e^{m\ell_\gamma}-1}$ substituted on both sides. The only technical point is that the classes on $X'$ mapping to a fixed class on $X$ form a countable family whose masses sum absolutely, which follows from positivity.

---

# What this assumes, and where to climb

**Both structural properties of the Brownian loop measure** — [[Constr - The Brownian Loop Measure]]. This is the only theorem in the paper that uses both at once, and it is worth seeing which does what: restriction handles the puncturing, conformal invariance handles the re-metrisation. Neither alone suffices.

**Polarity of $P$** — [[Def - Polar Set]]. A closed discrete set is polar; a curve is not. Cutting along a curve genuinely changes the loop measure.

**Uniformisation** — the existence and uniqueness of a complete hyperbolic metric on the punctured surface $X'$. This is quoted and is one of the [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes|five recorded gaps]]; its home node is *Riemann Surfaces* (🔵). Only this theorem needs it.

## What survives for a subordinate process, and what does not

**Restriction survives.** A killing rate does not change the paths, so for $\phi(\lambda)=\lambda+\kappa$ the polar sets are Brownian ones and $\mu^\kappa_X$ is supported on loops avoiding $P$. Hence
$$\mu^\kappa_{X,g}\big(\mathcal{C}_X(\gamma^m)\big) = \mu^\kappa_{X\setminus P,g}\big(\mathcal{C}_X(\gamma^m)\big),$$
with $g$ on the right the *ambient* metric restricted to $X\setminus P$, and the class measured in $X$ on both sides. This is genuine but weak: puncturing does not change the mass provided the metric is unchanged.

**Conformal invariance does not survive, and the obstruction is exact.** In two dimensions a conformal change $g'=e^{2\sigma}g$ rescales the Laplacian, $\Delta_{X,g'}=e^{-2\sigma}\Delta_{X,g}$. This conformal covariance is a *linear* phenomenon, and it is destroyed by $\phi$:
$$\phi\big(e^{-2\sigma}\Delta_{X,g}\big)\neq e^{-2\sigma}\phi\big(\Delta_{X,g}\big)\qquad\text{unless }\phi(\lambda)=c\lambda\text{ for some }c>0.$$
So for every nonlinear subordination the metric cannot be swapped, only the trivial restriction identity remains, and **the comparison of length spectra collapses**. This is the sharpest statement in the paper of what subordination costs.

---

# What consumes this

- [[§3 Decomposition over Homotopy Classes]] §3.4 — where the identity and its degeneration are discussed
- [[Def - Marked Length Spectrum]] and [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] — the neighbouring results of §3.4, which go the other way: rather than relating two surfaces, they recover one surface's geometry from its own loop masses

Nothing later in the paper depends on this theorem; §3.4 is a coda. Its value is diagnostic — it is where one learns exactly how much of the Brownian structure the subordinate framework gives up.

---

# Reading it against the rest of the paper

Wang–Xue's original setting is *Riemann* surfaces, which is the natural home for a conformally invariant object; the identity is one of their paper's main applications. The present paper reproduces it to make a point about the limits of its own generalisation: having built a framework covering four families of processes, §3.4 is where it says out loud that one of the two structural properties motivating the whole subject is available only in the original case.

The other place conformal invariance is spent is [[Thm - Polyakov's Formula via Brownian Loop Measure|Corollary 5.4]], and the mechanism there is the same — the loop-measure terms do not move under a conformal change, so all the metric dependence isolates into an explicit local functional. Reading the two together is the efficient way to see what conformal invariance is worth.
