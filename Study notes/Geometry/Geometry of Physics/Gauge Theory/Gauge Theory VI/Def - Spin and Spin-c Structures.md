---
type: definition
subject: gauge-theory
prereqs: ["Def - Spin Group and Low-Dimensional Spin Groups", "Def - Orthonormal Frame Bundle"]
tags: [gauge-theory, spin-structure, spin-c]
---

# Motivation

The oriented frame bundle has structure group $SO(n)$, but spinor representations live on its double cover. A spin structure is the global lift required to associate spinors. When the lift is obstructed, adjoining a compensating $U(1)$ phase often removes the obstruction; this is the role of $\operatorname{Spin}^c$.

# The Definitions

> [!definition] Spin structure
> A spin structure on an oriented Riemannian $n$-manifold is a principal $\operatorname{Spin}(n)$-bundle $P_{Spin}\to M$ with an equivariant two-fold covering $P_{Spin}\to F_{SO}(M)$ over $M$.

> [!definition] Spin-c structure
> With
> $$\operatorname{Spin}^c(n)=(\operatorname{Spin}(n)\times U(1))/\{(1,1),(-1,-1)\},$$
> a $\operatorname{Spin}^c$ structure is a principal $\operatorname{Spin}^c(n)$-bundle whose quotient by the central $U(1)$ is $F_{SO}(M)$.

The determinant homomorphism is $[g,z]\mapsto z^2$ and defines the determinant line $L$. A connection on $L$, together with Levi–Civita, determines the spin-c connection. The square is essential: it makes the map independent of the representative $(g,z)\sim(-g,-z)$.

# Obstructions and Classification

A spin structure exists exactly when $w_2(TM)=0$; when nonempty, their isomorphism classes form a torsor for $H^1(M;\mathbb Z/2)$. A spin-c structure exists exactly when $w_2(TM)$ lifts to an integral class; then its determinant line satisfies
$$c_1(L)\equiv w_2(TM)\pmod2.$$
The set of spin-c structures is a torsor for $H^2(M;\mathbb Z)$, where twisting by a line bundle $K$ changes $L$ to $L\otimes K^2$. Every closed oriented four-manifold is spin-c.

**True name:** spin and spin-c structures are lifts of the oriented-frame cocycle through central extensions.

