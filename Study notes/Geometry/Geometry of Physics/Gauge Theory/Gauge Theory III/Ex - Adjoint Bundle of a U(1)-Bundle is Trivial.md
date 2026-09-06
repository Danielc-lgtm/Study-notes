---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Adjoint Bundle"
  - "Def - Adjoint Representation"
tags: [geometry, gauge-theory, electromagnetism, abelian, adjoint-bundle]
---

# Problem Statement

Let $P\to M$ be a principal $U(1)$-bundle. Prove canonically that
$\operatorname{Ad}P\cong M\times i\mathbb R$. Deduce that its adjoint-valued forms are ordinary $i\mathbb R$-valued forms and that the induced covariant exterior derivative is $d$.

# Solution

> [!solution]- Solution
> The adjoint action is conjugation. Since $U(1)$ is abelian,
> $\operatorname{Ad}_z\xi=\xi$ for every $z\in U(1)$ and $\xi\in i\mathbb R$.
> Define
> $$\Psi:P\times_{\operatorname{Ad}}i\mathbb R\longrightarrow M\times i\mathbb R,
> \qquad [p,\xi]\longmapsto(\pi(p),\xi).$$
> The associated-bundle relation is $(pz,\xi)\sim(p,\operatorname{Ad}_z\xi)=(p,\xi)$,
> so $\Psi$ is well defined. Its inverse sends $(x,\xi)$ to $[p,\xi]$ for any
> $p\in P_x$; replacing $p$ by $pz$ does not change the class. Both maps are
> smooth in local trivializations and fibrewise linear, proving the canonical
> isomorphism.
>
> Consequently $\Omega^k(M;\operatorname{Ad}P)\cong\Omega^k(M;i\mathbb R)$.
> Locally $d_A\alpha=d\alpha+[A,\alpha]$, and the bracket term vanishes, so
> $d_A=d$. In particular, a $U(1)$ curvature is a globally defined closed
> $i\mathbb R$-valued two-form even when $P$ itself is nontrivial.

# Rederivation Scaffold

An associated bundle forgets twisting whenever its defining representation is trivial.
