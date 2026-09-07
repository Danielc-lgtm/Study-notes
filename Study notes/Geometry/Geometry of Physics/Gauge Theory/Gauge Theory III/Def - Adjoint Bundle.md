---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Associated Bundle"
  - "Def - Adjoint Representation"
tags: [gauge-theory, adjoint-bundle]
---

# Prerequisite Concepts

- [[Def - Associated Bundle]]
- [[Def - Adjoint Representation]]

# The Definition

> [!definition] Adjoint bundle
> The **adjoint bundle** of $P\to M$ is
> $$\operatorname{Ad}P=P\times_{\operatorname{Ad}}\mathfrak g,$$
> with relation $[pg,\xi]=[p,\operatorname{Ad}_g\xi]$ under the associated-bundle convention.

Its sections correspond to equivariant maps $u:P\to\mathfrak g$ satisfying
$$u(pg)=\operatorname{Ad}_{g^{-1}}u(p).$$
The fibrewise Lie bracket is well defined because $\operatorname{Ad}_g$ is a Lie-algebra automorphism.

# Geometric Meaning

The vertical tangent bundle satisfies
$$VP\cong\pi^*(\operatorname{Ad}P),\qquad (p,[p,\xi])\longmapsto\xi_P(p).$$
Thus an adjoint-bundle section is an infinitesimal gauge transformation. Curvature descends as an element of $\Omega^2(M;\operatorname{Ad}P)$, and differences of connections lie in $\Omega^1(M;\operatorname{Ad}P)$.

# Abelian Case

For $G=U(1)$, the adjoint action is trivial, so $\operatorname{Ad}P\cong M\times i\mathbb R$ canonically even when $P$ is nontrivial. This is why abelian curvature may be treated as an ordinary imaginary-valued form on $M$.
