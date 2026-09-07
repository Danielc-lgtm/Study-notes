---
type: definition
subject: gauge-theory
prereqs: ["Def - Hodge Star in Arbitrary Signature", "Def - U(1) Gauge Field and Electromagnetic Connection"]
tags: [gauge-theory, maxwell, electromagnetism]
---

# Prerequisite Concepts

- [[Def - Hodge Star in Arbitrary Signature]]
- [[Def - U(1) Gauge Field and Electromagnetic Connection]]

# The Definition

> [!definition] Maxwell field
> On an oriented Lorentzian four-manifold, a $U(1)$ connection has real physical potential $A$ and field strength $F=dA$ locally. With current one-form $j$, Maxwell's equations are
> $$dF=0,\qquad d*F=*j.$$

The first equation is the abelian Bianchi identity and is therefore kinematic. The second is dynamical. Globally, $F$ need only be closed with integral normalized periods; a single global $A$ exists exactly when its de Rham class vanishes.

# Action Principle

With compactly supported variations and the convention
$$S[A]= -\frac12\int_M F\wedge *F+\int_M A\wedge *j,$$
one has $\delta F=d(\delta A)$ and
$$\delta S=-\int_Md(\delta A)\wedge *F+\int_M\delta A\wedge *j
=\int_M\delta A\wedge(-d*F+*j).$$
The boundary term vanishes, so stationarity for every $\delta A$ gives $d*F=*j$. Gauge invariance of the source term under $A\mapsto A+d\chi$ requires $d*j=0$, the continuity equation.

# Components

With $F_{0i}=E_i$ and $F_{ij}=-\varepsilon_{ijk}B^k$, $dF=0$ yields $\nabla\cdot B=0$ and $\partial_tB+\nabla\times E=0$; $d*F=*j$ yields Gauss's and Ampère–Maxwell laws. The differential-form equations package all four without choosing an inertial frame.

**True name:** Maxwell theory is the abelian curvature equation “closed and sourced co-closed.”
