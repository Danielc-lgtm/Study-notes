---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Adjoint Bundle"
tags: [gauge-theory, gauge-group, automorphism]
---

# Prerequisite Concepts

- [[Def - Principal G-Bundle]]
- [[Def - Adjoint Bundle]]

# The Definition

> [!definition] Gauge group
> The **gauge group** $\mathcal G(P)$ is the group of principal-bundle automorphisms $\Phi:P\to P$ covering $\operatorname{id}_M$.

Every $\Phi$ is uniquely
$$\Phi(p)=p\,u(p)$$
for a smooth map $u:P\to G$ satisfying
$$u(pg)=g^{-1}u(p)g.$$
Indeed equivariance of $\Phi$ gives the condition; conversely the condition makes $p\mapsto pu(p)$ equivariant. Thus $\mathcal G(P)$ is the section group of the associated conjugation bundle $P\times_{\mathrm{Conj}}G$.

# Action on Connections

The active action is pullback by the inverse,
$$\Phi\cdot\omega=(\Phi^{-1})^*\omega,$$
so covariant objects transform with the same action as sections. In a local section and matrix notation, if the local gauge function is $g:U\to G$,
$$A\longmapsto gAg^{-1}-(dg)g^{-1},\qquad F\longmapsto gFg^{-1}.$$
Using pullback by $\Phi$ instead reverses $g$; both conventions describe the same orbit.

# Based Gauge Group

Fix $p_0\in P$. The subgroup $\mathcal G_0(P)=\{\Phi:\Phi(p_0)=p_0\}$ acts without constant conjugation at the base point. Quotienting first by $\mathcal G_0$ retains a residual $G$-action and is useful for constructing framed moduli spaces.
