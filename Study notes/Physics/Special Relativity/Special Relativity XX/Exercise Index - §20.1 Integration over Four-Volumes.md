---
type: exercise-index
subject: special-relativity
section: "20.1"
tags: [physics, special-relativity]
---

## §20.1 Integration over Four-Volumes — Exercises

The exercises of §20.1 drill the metric four-volume element $\sqrt{|g|}\,\mathrm{d}^4x$ and the integral of a differential 4-form. The recurring technique is to find coordinates adapted to the region (so the region is a coordinate box), write down the correct volume factor $\sqrt{|g|}$, and reduce to an ordinary Lebesgue integral. The conceptual thread running through all three is the chapter's central dichotomy: the *four-volume* of a region is a metric quantity (it needs $\sqrt{|g|}$), while the *integral of a 4-form* is metric-free (the antisymmetric component absorbs the change-of-variable Jacobian on its own). The last exercise isolates exactly why antisymmetry is the property that makes a tensor integrable without a metric — the structural reason the whole theory is built on differential forms.

- [[Ex - Integrating a four-form over a region of spacetime]] (⭐⭐) — compute a four-volume in inertial and spherical coordinates and the integral of a density 4-form, confirming the $\sqrt{|g|}=r^2\sin\theta$ factor restores the familiar measure and the answer is coordinate-independent ([[Def - Integration of Forms and the Volume Element]], [[Def - The Levi-Civita Tensor]]).
- [[Ex - Coordinate-independence of the four-volume]] (⭐⭐) — prove from the change-of-variables formula that $\int\sqrt{|g|}\,\mathrm{d}^4x$ is coordinate-independent via $\sqrt{|g'|}=|J|\sqrt{|g|}$, and that the integral of a 4-form is coordinate-independent *without* the metric, exposing the metric/metric-free dichotomy at the level of transformation laws ([[Def - Integration of Forms and the Volume Element]]).
- [[Ex - Only an antisymmetric form integrates coordinate-independently]] (⭐⭐) — show the single component of a 4-form integrates coordinate-independently but a generic tensor's component does not, with an explicit two-dimensional symmetric counterexample, establishing antisymmetry as the precise condition for integrability without a metric ([[Def - Integration of Forms and the Volume Element]], [[Def - Alternate Forms and the Exterior Product]]).
