---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie-Algebra-Valued Differential Form"
tags: [gauge-theory, graded-lie-algebra, differential-forms]
---

# The Definition

> [!definition] Graded bracket
> For decomposable forms $\alpha\otimes X\in\Omega^p(M;\mathfrak g)$ and $\beta\otimes Y\in\Omega^q(M;\mathfrak g)$, define
> $$
> [\alpha\otimes X,\beta\otimes Y]
> =(\alpha\wedge\beta)\otimes[X,Y],
> $$
> and extend bilinearly.

It satisfies
$$
[\eta,\zeta]=-(-1)^{pq}[\zeta,\eta],
$$
and the graded Jacobi identity. The exterior derivative is a graded derivation:
$$
d[\eta,\zeta]=[d\eta,\zeta]+(-1)^p[\eta,d\zeta].$$
Each identity follows on decomposable elements from the corresponding wedge-product identity and the ordinary Lie-algebra identity.

# Matrix Convention

If $\mathfrak g\subset\mathfrak{gl}_N$ and matrix multiplication is combined with wedge product, then
$$[\eta,\zeta]=\eta\wedge\zeta-(-1)^{pq}\zeta\wedge\eta.$$
For a $1$-form $A$,
$$\tfrac12[A,A]=A\wedge A.$$
This factor is why $dA+A\wedge A$ and $dA+\tfrac12[A,A]$ are the same curvature formula, not competing conventions.
