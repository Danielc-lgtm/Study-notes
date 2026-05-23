---
type: exercise-index
subject: differential-geometry
section: "10.4"
tags: [geometry, differential-geometry, frobenius, foliation]
---

## §10.4 Foliations — Exercises

This section's exercises drill the global Frobenius perspective: [[Def - Foliation|foliations]] as global partitions induced by involutive distributions, and the cohomological computations that detect global obstructions to integrability. The unifying theme is the dichotomy between local existence (always achievable on contractible pieces via the Poincaré lemma) and global existence (obstructed by topology, measured by cohomology). The PDE exercise demonstrates the foliation viewpoint applied to first-order systems: the solution graphs are the leaves of the foliation determined by the associated involutive distribution.

Because §10.4 is a synthesis section combining cohomology and Frobenius, we reuse exercises from §10.3 (the distribution exercises) and §10.1–10.2 (the cohomology exercises) to illustrate the foliation perspective. The torus exercise, in particular, is the natural setting for [[Def - Foliation|foliations]]: $T^n$ has many natural foliations (by coordinate sub-tori, by lines of various slopes, etc.), and the cohomology computation packages all this structure.

- [[Ex - The de Rham Cohomology of the Torus]] (⭐⭐⭐) — the torus carries natural foliations by sub-tori $T^k \hookrightarrow T^n$, and the cohomology classes $[d\theta^{i_1} \wedge \cdots \wedge d\theta^{i_k}]$ are naturally adapted to these foliations. The [[Def - Dimension|dimension]] count $\binom{n}{k}$ matches the number of distinct $k$-dimensional sub-tori one can identify ([[Def - de Rham Cohomology]], [[Thm - The Mayer-Vietoris Sequence]])
- [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]] (⭐⭐) — the prototype *non*-foliation: a rank-$2$ distribution that fails to integrate to any $2$-dimensional foliation. The global obstruction is the non-zero $\alpha \wedge d\alpha$ everywhere, and the geometric meaning is that no foliation by surfaces can exist ([[Def - Foliation]], [[Def - Involutive Distribution]], [[Thm - Frobenius Theorem in Forms Language]])
- [[Ex - Frobenius Theorem Applied to an Overdetermined PDE]] (⭐⭐⭐) — when the compatibility condition holds, $\mathbb{R}^3$ is foliated by graphs $\{(x, y, u(x, y))\}$ — each leaf being a solution to the PDE. The foliation is parametrized by the initial value $u(x_0, y_0) = z_0$; different initial conditions give different leaves ([[Def - Foliation]], [[Thm - The Frobenius Theorem]])
