---
type: theorem
subject: hyperbolic-geometry
prereqs:
  - "Def - Hyperbolic Plane"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
  - "Def - Brownian Loop Measure"
  - "Thm - Mass of a Free Homotopy Class"
tags: [paper, brownian-loops, hyperbolic-geometry, spectral-geometry, external-input]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 3.9"
---

# Notation

- $X$ — a complete hyperbolic surface (without boundary; may be of infinite type, with cusps or funnels).
- $P \subset X$ — a non-empty closed discrete subset ("puncture set"); each point of $P$ becomes a puncture (cusp) after removal.
- $X' := X \setminus P$ — the punctured surface. By the uniformisation theorem, $X'$ carries a *unique* complete hyperbolic metric $g'$ in which each point of $P$ becomes a cusp.
- $\gamma\in\mathcal{P}_X$, $m\ge 1$ — a primitive closed geodesic in $X$ and a winding number; $\ell_\gamma$ its length in $X$'s original metric $g$.
- $\gamma' \in \mathcal{P}_{X'}$, $m' \ge 1$ — analogous in $X'$; $\ell_{\gamma'}$ its length in the new hyperbolic metric $g'$ of $X'$.
- $\simeq_X$ — free homotopy in $X$ (not $X'$): $\gamma'^{m'} \simeq_X \gamma^m$ means the loop $\gamma'^{m'}$, when viewed as a loop in the larger surface $X$ (which contains $X'$ as an open subset), is freely homotopic to $\gamma^m$.

> [!recall]- Conformal equivalence of a punctured hyperbolic surface with the unique complete hyperbolic metric
> **Formally:** if $X$ is a complete hyperbolic surface and $P\subset X$ is a non-empty closed discrete set, then $X' = X\setminus P$ is again a smooth surface and (by the uniformisation theorem) carries a unique complete hyperbolic metric $g'$ in which every point of $P$ has become a cusp; $g'$ is conformally equivalent to the restricted metric $g|_{X'}$: $g' = e^{2\sigma}g|_{X'}$ for some conformal factor $\sigma : X'\to\mathbb{R}$ which blows up near the cusps.
> **In words:** if you remove a discrete set of points from a hyperbolic surface, the result can be re-equipped with a hyperbolic metric that makes each removed point look like the tip of a hyperbolic funnel-shrinking-to-a-puncture — and this new metric is the "same shape" as the original one up to a local rescaling (a conformal factor). The re-metrisation is *unique* once we insist on completeness.
> **Concretely:** remove a single point from the round sphere $S^2$; you get $\mathbb{R}^2$, which carries the flat metric (0-curvature) or, equivalently, a unique complete hyperbolic-like metric — actually the sphere has curvature $+1$ and its punctured version has a *unique* flat metric, not hyperbolic. Better: remove one point from a genus-2 hyperbolic surface; you get a genus-2 surface with one cusp, and the new metric near the cusp is (isometric to) $\{y > c\}/\langle z\mapsto z+1\rangle$ in the upper-half-plane model. This new metric is conformally related to the restriction of the original by $e^{2\sigma}$ with $\sigma$ growing near the puncture.

> [!recall]- Free homotopy in the ambient $X$ vs. in $X'$
> **Formally:** two loops on $X'$ can be freely homotopic *in $X'$* (a homotopy that stays inside $X'$) or freely homotopic *in $X$* (a homotopy allowed to pass through $P$). The second is a coarser relation: two $X'$-loops that are $X$-homotopic may be $X'$-inequivalent (they might be blocked from equivalence in $X'$ by the punctures). Explicitly, a class $C_{X'}(\gamma')$ in $X'$ maps to a class $C_X(\gamma'{,\ldots})$ in $X$ (its "image under inclusion"), and multiple $X'$-classes can map to the same $X$-class.
> **In words:** on a punctured surface, more loops become "different from each other" because the punctures block homotopies that would have gone through them. If you plug the punctures back in (embed $X'$ back into $X$), some of those distinct $X'$-classes fuse into one $X$-class.
> **Concretely:** on the once-punctured torus $X' = T^2\setminus\{p\}$ (view $X = T^2$), the class in $X'$ of "loop that goes once around the horizontal circle staying above the puncture" and the class of "once around, staying below" are two different $X'$-classes (they cannot be homotoped through the puncture). But viewed in the full torus $X = T^2$, both are freely homotopic — they are the same $X$-class $(1,0)$. So one $X$-class in $T^2$ splits into (at least) two $X'$-classes in $X'$.

> [!recall]- Polar set: puncturing does not affect Brownian paths
> **Formally:** $P\subset X$ is *polar* for Brownian motion if from every starting point $x$, the process almost surely never hits $P$ at any positive time. For 2-dimensional Brownian motion, every closed discrete set is polar (this is a classical fact: 2-D Brownian motion doesn't hit points).
> **In words:** invisible sets — the process never lands on them. Removing a polar set from the surface leaves the process's law unchanged, so all loop-measure integrals over the surface remain the same after puncturing (provided the metric doesn't change).
> **Concretely:** in $\mathbb{R}^2$, the single point $\{0\}$ is polar for planar Brownian motion; so is any countable set $\{x_1, x_2, \ldots\}$. Removing any such set from $\mathbb{R}^2$ leaves the Brownian loop measure and its class-masses unchanged. On a hyperbolic surface, the same holds: a discrete puncture set is polar. Full detail: Blumenthal–Getoor, potential theory of Markov processes.

> [!recall]- Conformal invariance of the Brownian loop measure
> **Formally:** the Brownian loop measure on a surface is invariant under conformal changes of metric: if $g' = e^{2\sigma}g$ with $\sigma:X\to\mathbb{R}$, then $\mu_{X,g'} = \mu_{X,g}$ as measures on loop space (paths, not path-with-parametrisation). Rescaling time appropriately, the Brownian process on $(X, g')$ has the same *path measure* as on $(X, g)$ up to a time change, and the loop measure (which integrates against $dt/t$, itself invariant under rescaling) is unchanged.
> **In words:** stretch and shrink the surface conformally — the Brownian loops don't care. Because the loop measure integrates over all time scales with the scale-invariant weight $dt/t$, the local metric rescaling cancels out.
> **Concretely:** on $\mathbb{R}^2$ with the standard flat metric $g$ vs. the metric $g' = e^{2\sigma}g$ obtained by stereographic projection from the round sphere (so $g'$ is the round-sphere metric restricted to $\mathbb{R}^2\cong S^2\setminus\{\text{pt}\}$): the Brownian loop measures on $(\mathbb{R}^2, g)$ and $(\mathbb{R}^2, g')$ agree as measures on loop space — the conformal factor changes the *speed* at which paths are traced but not *which paths* have how much mass. Only true for **Brownian** (not for subordinate/killed) processes, because subordination breaks conformal invariance.

---

# Statement

> **Theorem (Wang–Xue length-spectrum identity; Belyaev–Huseynli 3.9, after Wang–Xue [WX25, Thm 4.2]).** Let $X$ be a complete hyperbolic surface (without boundary, possibly infinite type, with cusps or funnels), $P \subset X$ a non-empty closed discrete polar subset, and $X' = X \setminus P$ equipped with its unique complete hyperbolic metric. Then for every primitive closed geodesic $\gamma\in\mathcal{P}_X$ and every $m\ge 1$,
> $$\frac{1}{m}\cdot\frac{1}{e^{m\ell_\gamma}-1} \;=\; \sum_{\substack{\gamma'\in\mathcal{P}_{X'},\;m'\ge 1 \\ \gamma'^{m'}\,\simeq_X\,\gamma^m}}\frac{1}{m'}\cdot\frac{1}{e^{m'\ell_{\gamma'}}-1},$$
> where the sum is over all pairs $(\gamma', m')$ of primitive $X'$-geodesic and winding number whose corresponding $X'$-loop is freely homotopic in $X$ to $\gamma^m$, and $\ell_\gamma, \ell_{\gamma'}$ are the primitive lengths in the respective hyperbolic metrics.

---

# In One Line

The Brownian class-mass of $C_X(\gamma^m)$ on the original surface equals the sum of the Brownian class-masses of the classes in $X'$ that fuse into $C_X(\gamma^m)$ once the punctures are filled in — a length-spectrum identity between two hyperbolic surfaces enforced by the conformal invariance of the Brownian loop measure.

---

# Why It's True

**Mechanism (one sentence).** *The Brownian loop mass of the class $C_X(\gamma^m)$ can be computed either on $(X, g)$ (giving the left-hand side, via [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] §3.1.1) or on $(X', g')$ (giving the right-hand side, via the same theorem applied per $X'$-class and summed over the classes fusing to $C_X(\gamma^m)$); the two answers agree because puncturing removes only a polar set (path-invariant) and the conformal change of metric $g\to g'$ preserves the Brownian loop measure.*

The identity is a **calculation done in two ways**:

- **Left-hand side:** apply [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] §3.1.1 (Brownian case) to the class $C_X(\gamma^m)$ in the original metric $g$: $\mu_{X,g}(C_X(\gamma^m)) = \frac{1}{m(e^{m\ell_\gamma} - 1)}$.
- **Right-hand side:** apply the same formula on the punctured surface $X'$ in its own hyperbolic metric $g'$: each $X'$-class $C_{X'}(\gamma'^{m'})$ has mass $\frac{1}{m'(e^{m'\ell_{\gamma'}} - 1)}$. Sum over all $X'$-classes that fuse into $C_X(\gamma^m)$ when reincluded into $X$ (i.e. all $(\gamma', m')$ with $\gamma'^{m'} \simeq_X \gamma^m$).

The two answers must agree because they are computing the *same* Brownian loop mass, viewed two ways: **(a)** removing the polar set $P$ leaves the Brownian process unchanged (so $\mu_{X,g}$-mass = $\mu_{X\setminus P, g|_{X\setminus P}}$-mass); **(b)** the loop measure is *conformally invariant* for Brownian motion, so switching from $g|_{X\setminus P}$ to the complete-hyperbolic $g'$ preserves the mass; **(c)** on $X'$ with $g'$, the class $C_X(\gamma^m)$ (viewed as a set of $X'$-loops via the inclusion $X'\subset X$) is the disjoint union of the $X'$-classes $C_{X'}(\gamma'^{m'})$ that map to it, and the loop measure is $\sigma$-additive, so its mass on $C_X(\gamma^m)$ is the sum of its masses on the $C_{X'}(\gamma'^{m'})$.

---

# Proof

> [!cite]- External input — Wang–Xue Theorem 4.2
> **Statement (typed):** as boxed above; the identity holds for every pair $(X, P)$ with $X$ a complete hyperbolic surface, $P\subset X$ non-empty closed discrete polar, $X' = X\setminus P$ carrying its unique complete hyperbolic metric.
> **Type check.** Both sides are positive real numbers (each summand on the right is finite and positive by the Brownian closed form; the sum converges because the fusing $X'$-classes have $\ell_{\gamma'} \ge \ell_\gamma$ in a coarse sense — the puncturing does not make loops shorter than they were before, and adds only geometrically-bounded extra homotopy types).
> **Why it's true (intuition).** Two ways of computing the same Brownian loop mass: polar-set-removal + conformal invariance make the removed-and-remetrised loop measure identical to the original, and $\sigma$-additivity over the finer partition on $X'$ turns the single class-mass on the left into the sum on the right.
> **Source.** Wang–Xue [WX25, Theorem 4.2]; the paper states it here for context and cites the source. The proof uses the two ingredients above: (a) polar-set removal (classical potential theory, e.g. Blumenthal–Getoor) and (b) conformal invariance of the Brownian loop measure (Le Jan, *Markov Paths, Loops and Fields*), plus the $\sigma$-additivity of the loop measure over the disjoint decomposition of $C_X(\gamma^m)$ into $X'$-subclasses.
> **Take on faith with the stated form.** The identity is not re-proved in these notes; a specialist reference is Wang–Xue.

**Why the paper cites but does not use this theorem structurally.** Belyaev–Huseynli state Theorem 3.9 for context — it is the *analogue* of what the paper proves for Brownian loops with killing, but the conformal invariance argument *fails* for subordinate processes (a conformal change rescales $\Delta_{X,g'} = e^{-2\sigma}\Delta_{X,g}$, and a nonlinear Bernstein $\phi$ does not commute with this rescaling: $\phi(e^{-2\sigma}\Delta) \ne e^{-2\sigma}\phi(\Delta)$ unless $\phi(\lambda) = c\lambda$). So the length-spectrum identity is a purely-Brownian phenomenon. The killed / subordinate versions of §3.4 use only the weaker "polar-set removal leaves the metric unchanged" step, yielding $\mu^\kappa_{X,g}(C_X(\gamma^m)) = \mu^\kappa_{X\setminus P,g}(C_X(\gamma^m))$ — no metric swap, no length-spectrum comparison.

---

# Where the paper uses this

Cited in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.4]] as context for the length-spectrum discussion; not directly used in the paper's own arguments (the killed / subordinate cases of §3.4 fall back to the weaker polar-set-only identity). The theorem is the "Brownian version" that motivates why the paper is interested in length-spectrum-type identities; Belyaev–Huseynli's own contribution is [[Prop - Loop Masses Determine the Length Spectrum|Prop 3.11]] and [[Cor - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]], which invert loop masses back to the length spectrum in the killed case.
