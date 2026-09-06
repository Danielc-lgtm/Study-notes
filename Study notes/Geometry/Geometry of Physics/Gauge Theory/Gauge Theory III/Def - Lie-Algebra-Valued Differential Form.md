---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Lie Algebra"
tags: [gauge-theory, differential-forms, lie-algebra]
---

# The Definition

> [!definition] Lie-algebra-valued form
> For a Lie algebra $\mathfrak g$, a **$\mathfrak g$-valued $k$-form** on $M$ is a section of $\Lambda^kT^*M\otimes\mathfrak g$:
> $$\Omega^k(M;\mathfrak g)=\Omega^k(M)\otimes\mathfrak g.$$

In a basis $(T_a)$, write $\alpha=\alpha^aT_a$. The exterior derivative acts only on the form coefficient, $d\alpha=(d\alpha^a)T_a$. A linear map $L:\mathfrak g\to\mathfrak h$ acts coefficientwise, and pullback by $f:N\to M$ acts on the differential-form factor.

# What Changes from Ordinary Forms

There is no canonical associative product on an abstract Lie algebra. The Lie bracket nevertheless combines coefficients and yields a graded bracket of valued forms, defined on [[Def - Bracket of g-Valued Forms]]. For matrix Lie algebras, matrix multiplication supplies the compact notation $A\wedge A$.

# Examples / Corollaries

A local gauge potential is a $\mathfrak g$-valued $1$-form; its curvature is a $\mathfrak g$-valued $2$-form. A principal connection form is a $\mathfrak g$-valued $1$-form on the total space satisfying additional reproduction and equivariance axioms.
