---
type: definition
subject: gauge-theory
prereqs: ["Def - Adjoint Bundle"]
tags: [gauge-theory, invariant-polynomial, chern-weil]
---

# Prerequisite Concepts

- [[Def - Adjoint Bundle]]

# Motivation

Curvature changes by conjugation when the gauge changes. A scalar polynomial can therefore turn curvature into a globally defined form only when it cannot detect conjugation. This is exactly the invariance imposed below.

# The Definition

> [!definition] Ad-invariant polynomial
> A degree-$k$ invariant polynomial on a Lie algebra $\mathfrak g$ is a symmetric $k$-linear map
> $$f:\mathfrak g^k\to\mathbb R$$
> satisfying
> $$f(\operatorname{Ad}_gX_1,\ldots,\operatorname{Ad}_gX_k)=f(X_1,\ldots,X_k).$$
> Its diagonal polynomial is $X\mapsto f(X,\ldots,X)$.

Differentiating invariance at $g=e^{tY}$ gives the infinitesimal identity
$$\sum_{j=1}^k f(X_1,\ldots,[Y,X_j],\ldots,X_k)=0.$$
Conversely this identity implies invariance under the identity component of $G$.

# Examples and Calibration

For matrix Lie algebras, $\operatorname{tr}(X^k)$ is invariant by cyclicity of trace. On $\mathfrak u(r)$ the coefficients in
$$\det\left(I+\frac{i}{2\pi}X\right)=1+c_1(X)+\cdots+c_r(X)$$
are invariant. A generic linear functional on $\mathfrak{su}(2)$ is a non-example: the adjoint action rotates $\mathfrak{su}(2)\cong\mathbb R^3$.

**True name:** an invariant polynomial is a gauge-blind scalar probe of adjoint-valued curvature.

**Calibration check.** Conjugate every input, differentiate the invariance law, and verify the resulting commutator sum vanishes.

# Unlocked by This

Applying $f$ to curvature produces the characteristic forms in [[Thm - Chern-Weil Theorem]].
