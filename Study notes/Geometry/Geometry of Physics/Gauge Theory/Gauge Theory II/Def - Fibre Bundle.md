---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Local Trivialization"
tags: [geometry, fibre-bundle]
---

# Notation

Let $E,B,F$ be smooth manifolds and $\pi:E\to B$ a smooth map. Write $E_b=\pi^{-1}(b)$.

# The Definition

> [!definition] Smooth fibre bundle
> A **smooth fibre bundle with typical fibre $F$** is a surjective smooth map $\pi:E\to B$ such that every $b\in B$ has an open neighbourhood $U$ and a diffeomorphism
> $$\Phi_U:\pi^{-1}(U)\xrightarrow{\sim}U\times F$$
> satisfying $\operatorname{pr}_1\circ\Phi_U=\pi$. The map $\Phi_U$ is a **local trivialization**.

On an overlap, $\Phi_\alpha\Phi_\beta^{-1}$ preserves the base coordinate and therefore has the form
$$
(x,y)\longmapsto(x,g_{\alpha\beta}(x)y),
$$
where $g_{\alpha\beta}(x)$ is a diffeomorphism of $F$. Specifying a smaller structure group $G\subset\operatorname{Diff}(F)$ means requiring these maps to lie in $G$.

A **section** is a smooth map $s:B\to E$ with $\pi s=\operatorname{id}_B$. Unlike vector bundles, general fibre bundles need not possess any global section.

# Pullback

For $f:N\to B$, the pullback is
$$
f^*E=\{(x,e)\in N\times E:f(x)=\pi(e)\}\longrightarrow N,qquad(x,e)\mapsto x.
$$
Pulling back a trivialization over $U$ gives one over $f^{-1}(U)$, so this is again a fibre bundle with fibre $F$. It satisfies the universal property: maps $X\to f^*E$ over $N$ are equivalent to maps $X\to E$ whose projection equals $f$ composed with the map $X\to N$.

# Examples / Corollaries

Products $B\times F$ are trivial bundles. Vector bundles are fibre bundles with $F=\mathbb K^r$ and linear transition maps. The mapping torus
$$([0,1]\times F)/(1,y)\sim(0,\varphi(y))\to S^1$$
is a fibre bundle for any diffeomorphism $\varphi:F\to F$. For a curve $\gamma:I\to B$, sections of $\gamma^*TB$ are vector fields along $\gamma$.

# What Can Go Wrong

A surjective submersion need not be globally a fibre bundle without additional hypotheses: local product charts must use one fixed typical fibre and cover the base. Conversely, local triviality implies that $\pi$ is a surjective submersion.
