---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
tags: [geometry, gauge-theory, curvature, trivial-bundle]
---

# Prerequisite Concepts

- [[Def - Connection on a Vector Bundle]]
- [[Def - Curvature of a Vector-Bundle Connection]]

# Problem Statement

On $E=M\times\mathbb K^r$, let $e=(e_1,\ldots,e_r)$ be the constant global frame and define $\nabla^0(eu)=e\,du$. Prove that $\nabla^0$ is a connection and $F_{\nabla^0}=0$. Then express the same connection in a moving frame $e'=eg$ and verify flatness directly.

# Convergent Strategy

The constant frame makes the connection matrix zero. In the moving frame the matrix is $g^{-1}dg$; the Maurer–Cartan cancellation, not the vanishing of the matrix, proves flatness.

# Solution

> [!proof]- Solution
> Linearity follows from linearity of $d$. For $f\in C^\infty(M)$,
> $$\nabla^0(e(fu))=e\,d(fu)=df\otimes eu+f\nabla^0(eu),$$
> so $\nabla^0$ is a connection. Since $\nabla^0e_a=0$, its matrix in $e$ is $A=0$, and therefore $F_A=dA+A\wedge A=0$.
>
> In the frame $e'=eg$, the passive frame-change law gives $A'=g^{-1}dg$. Differentiate $g^{-1}g=I$ to obtain $d(g^{-1})=-g^{-1}(dg)g^{-1}$. Consequently
> $$
> dA'=d(g^{-1}dg)=-g^{-1}dg\wedge g^{-1}dg=-A'\wedge A',
> $$
> and $F_{A'}=dA'+A'\wedge A'=0$. This agrees with the covariant transformation $F_{A'}=g^{-1}F_Ag$.

# Key Takeaways

A zero connection matrix is frame-dependent; zero curvature is not. A trivial bundle may carry non-flat connections $d+A$, and a flat bundle over a nonsimply-connected base need not have trivial holonomy.
