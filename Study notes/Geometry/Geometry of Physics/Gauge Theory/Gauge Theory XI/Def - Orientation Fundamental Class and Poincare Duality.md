---
type: definition
subject: gauge-theory
prereqs: ["Def - Singular Homology and Cohomology Operations"]
tags: [algebraic-topology, orientation, poincare-duality]
---
# The Definition
An $R$-orientation of an $n$-manifold $M$ is a coherent choice of generator of each local group $H_n(M,M\setminus\{x\};R)\cong R$. For compact connected oriented $M$, these local generators assemble uniquely into the **fundamental class** $[M]\in H_n(M;R)$.

# Poincaré duality
> [!theorem] Poincaré duality
> Cap product with $[M]$ is an isomorphism
> $$\operatorname{PD}:H^k(M;R)\xrightarrow\sim H_{n-k}(M;R)$$
> for a closed oriented $n$-manifold over a field, and with the standard integral refinements over $\mathbb Z$.

> [!proof]- Proof mechanism
> Triangulate $M$, take the dual cell decomposition, and send a cochain on each primal $k$-simplex to its coefficient on the transverse dual $(n-k)$-cell. The local orientation fixes all incidence signs. Coboundary of primal cochains corresponds, with those signs, to boundary of dual cells, so this is a chain isomorphism. Passing to (co)homology gives cap product with the sum of oriented top simplices, namely $[M]$. Subdivision independence makes the construction intrinsic.

# Operational form
A homology class represented by an oriented submanifold $N^{n-k}\subset M$ has a dual class characterized by
$$\langle\operatorname{PD}[N],[C]\rangle=C\cdot N.$$
This converts geometric intersection into cup product and is the entrance to the four-dimensional intersection form.
