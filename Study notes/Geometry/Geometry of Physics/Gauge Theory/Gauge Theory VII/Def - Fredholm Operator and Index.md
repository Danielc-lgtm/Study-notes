---
type: definition
subject: gauge-theory
prereqs: ["Def - Sobolev Space of Bundle Sections"]
tags: [gauge-theory, fredholm-operator, index]
---

# The Definition

> [!definition] Fredholm operator
> A bounded operator $T:X\to Y$ between Banach spaces is Fredholm when $\ker T$ is finite dimensional, $\operatorname{im}T$ is closed, and $\operatorname{coker}T=Y/\operatorname{im}T$ is finite dimensional. Its index is
> $$\operatorname{ind}T=\dim\ker T-\dim\operatorname{coker}T.$$

A Fredholm operator is invertible modulo finite-dimensional defects. Its index is locally constant under norm-continuous Fredholm perturbations and unchanged by compact perturbations. These properties make it the correct infinite-dimensional replacement for dimension difference.

# Calibration

Every map between finite-dimensional spaces is Fredholm and has index $\dim X-\dim Y$; this corrects the reversed sign sometimes produced by confusing kernel-minus-cokernel with target-minus-source. The unilateral shift on $\ell^2$ is Fredholm of index $-1$. Multiplication by $x$ on $L^2[-1,1]$ is a non-example because its range is not closed.

