---
type: definition
subject: gauge-theory
prereqs: ["Def - Connection on a Vector Bundle"]
tags: [gauge-theory, sobolev-space, functional-analysis]
---

# Motivation

Variational sequences rarely converge smoothly. Sobolev norms retain finitely many weak derivatives in $L^p$, producing complete spaces in which bounded sequences can have convergent subsequences. Gauge theory uses them both for fields and for gauge transformations.

# The Definition

> [!definition] Sobolev space of sections
> Let $E\to M$ be a metric vector bundle over a compact Riemannian manifold and choose a metric connection $\nabla$. For $k\in\mathbb N$ and $1<p<\infty$,
> $$\|s\|_{W^{k,p}}=\left(\sum_{j=0}^k\|\nabla^js\|_{L^p}^p\right)^{1/p},$$
> and $W^{k,p}(M;E)$ is the completion of smooth sections in this norm.

Equivalent weak-derivative and completion definitions agree. On a closed manifold, changing the metrics or connections changes the norm but not the topology: the difference of two connections is a smooth zeroth-order coefficient, and induction bounds every derivative for one choice by derivatives of no higher order for the other.

# Boundary Convention

On a domain with boundary, completing all smooth sections gives $W^{k,p}$, whereas completing compactly supported interior sections gives $W_0^{k,p}$ and encodes zero trace. Conflating them changes the boundary-value problem.

# Calibration

$W^{0,p}=L^p$. On $S^1$, $W^{1,2}$ functions have continuous representatives. A discontinuous step function belongs to $L^2$ but not $W^{1,2}$ because its distributional derivative is a delta measure.
**True name:** $W^{k,p}$ controls $k$ derivatives in an averaged $p$th-power sense.

