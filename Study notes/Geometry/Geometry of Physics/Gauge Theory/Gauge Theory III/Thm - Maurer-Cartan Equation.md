---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Def - Bracket of g-Valued Forms"
tags: [gauge-theory, maurer-cartan, structure-equation]
---

# Prerequisite Concepts

- [[Def - The Maurer-Cartan Form]]
- [[Def - Bracket of g-Valued Forms]]

# Statement

> [!theorem] Maurer–Cartan equation
> The left Maurer–Cartan form satisfies
> $$d\theta+\tfrac12[\theta,\theta]=0.$$
> For a matrix group, $d(g^{-1}dg)+(g^{-1}dg)\wedge(g^{-1}dg)=0$.

# Formal Proof

> [!proof]- Formal Proof
> Evaluate on left-invariant vector fields $X^L,Y^L$. Since $\theta(X^L)=X$ and $\theta(Y^L)=Y$ are constant,
> $$
> d\theta(X^L,Y^L)
> =X^L(\theta(Y^L))-Y^L(\theta(X^L))-\theta([X^L,Y^L])
> =-[X,Y].
> $$
> Meanwhile $\tfrac12[\theta,\theta](X^L,Y^L)=[X,Y]$. Their sum vanishes. Left-invariant fields span each tangent space, so the identity holds everywhere.
>
> In a matrix group, differentiating $g^{-1}g=I$ gives $d(g^{-1})=-g^{-1}(dg)g^{-1}$. Therefore
> $$d(g^{-1}dg)=d(g^{-1})\wedge dg=-g^{-1}dg\wedge g^{-1}dg,$$
> which is the same identity.

# Rederivation Scaffold

The Maurer–Cartan form makes left-invariant fields constant. Exterior differentiation then sees only their bracket, while $\frac12[\theta,\theta]$ restores exactly that bracket with the opposite sign.
