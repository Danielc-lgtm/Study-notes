---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Representation of a Lie Group"
tags: [geometry, gauge-theory, associated-bundle]
---

# Prerequisite Concepts

- [[Def - Principal G-Bundle]]
- [[Def - Representation of a Lie Group]]

# Notation

Let $P\to B$ be a right principal $G$-bundle and let $G$ act smoothly on the left of a manifold $F$. For a vector bundle take $F=V$ and a representation $\rho:G\to\mathrm{GL}(V)$.

# The Definition

> [!definition] Associated bundle
> Define a right action on $P\times F$ by
> $$(p,y)g=(pg,g^{-1}y).$$
> The **associated bundle** is
> $$P\times_GF=(P\times F)/G\longrightarrow B,\qquad[p,y]\mapsto\pi(p).$$
> For a representation, write $P\times_\rho V$.

The inverse in $g^{-1}y$ is forced: it makes $(p g,y)$ and $(p,gy)$ represent the same geometric vector. If $s_\alpha$ is a local section of $P$, then
$$[s_\alpha(x)g,y]=[s_\alpha(x),gy],$$
which gives a local trivialization $[s_\alpha(x),y]\leftrightarrow(x,y)$. On overlaps the fibre coordinate changes by the representation of $g_{\alpha\beta}$.

# Sections as Equivariant Maps

Sections of $P\times_GF$ correspond bijectively to smooth maps $\phi:P\to F$ satisfying
$$\phi(pg)=g^{-1}\phi(p).$$
Given $\phi$, set $\sigma(x)=[p,\phi(p)]$ for any $p\in P_x$; equivariance makes this independent of $p$. Conversely, if $\sigma(\pi(p))=[p,y]$, define $\phi(p)=y$. Uniqueness of the fibre coordinate and the quotient relation prove these constructions are inverse.

# Examples / Corollaries

For the frame bundle $\operatorname{Fr}(E)$ and defining representation on $\mathbb K^r$,
$$\operatorname{Fr}(E)\times_{\mathrm{GL}_r}\mathbb K^r\cong E,\qquad[u,v]\mapsto u(v).$$
Dual, tensor, exterior, and endomorphism representations recover the corresponding bundles. For a closed subgroup $H\subset G$, $G\to G/H$ is a principal $H$-bundle and $G\times_HV\to G/H$ is a homogeneous vector bundle.

# Unlocked by This

A connection on $P$ induces compatible covariant derivatives on every associated vector bundle. This is why the principal connection, rather than one chosen matter representation, is the fundamental gauge field.
