---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie Group"
  - "Def - The Lie Algebra of a Lie Group"
tags: [gauge-theory, lie-group, maurer-cartan]
---

# The Definition

> [!definition] Left Maurer–Cartan form
> For a Lie group $G$ with $\mathfrak g=T_eG$, the **left Maurer–Cartan form** is
> $$
> \theta_g=(dL_{g^{-1}})_g:T_gG\to\mathfrak g.
> $$
> For a matrix group, $\theta=g^{-1}dg$.

It identifies every tangent space with $\mathfrak g$ by left translation. On a left-invariant field $X^L$, $\theta(X^L)=X$. Under right translation,
$$R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta,$$
as follows from $L_{(gh)^{-1}}R_h=C_{h^{-1}}L_{g^{-1}}$ after differentiation.

# Axiom Motivation

A Lie group carries a canonical notion of “velocity measured in body coordinates”: translate a tangent vector back to the identity. On a trivial principal bundle this form measures vertical motion, making it the vertical part of every principal connection.

# Unlocked by This

Its integrability condition is the [[Thm - Maurer-Cartan Equation]]. Pulling $\theta$ back along $g:M\to G$ produces the pure-gauge form $g^{-1}dg$.
