---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Fibre Bundle"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, principal-bundle]
---

# Notation

Let $G$ be a Lie group. All principal actions in this series are right actions, written $R_g(p)=pg$.

# The Definition

> [!definition] Principal bundle
> A **principal $G$-bundle** is a smooth fibre bundle $\pi:P\to B$ with a smooth right $G$-action such that
> 1. $\pi(pg)=\pi(p)$;
> 2. the action on each fibre is free and transitive; and
> 3. local trivializations may be chosen equivariantly:
> $$\Phi_U(pg)=(x,hg)\quad\text{whenever }\Phi_U(p)=(x,h).$$

Each fibre is a **$G$-torsor**: choosing $p\in P_b$ identifies it with $G$ by $g\mapsto pg$, but there is no preferred choice of $p$ and hence no preferred identity element in the fibre.

A morphism of principal $G$-bundles over the same base is a smooth equivariant map $F:P\to P'$ with $\pi'F=\pi$. Such a morphism is automatically an isomorphism: on each torsor it is a bijection, and local trivializations show its inverse is smooth.

# Local Sections and Cocycles

A local section $s_\alpha:U_\alpha\to P$ yields the equivariant trivialization
$$U_\alpha\times G\to P|_{U_\alpha},\qquad(x,g)\mapsto s_\alpha(x)g.$$
On overlaps define $s_\beta=s_\alpha g_{\alpha\beta}$. Then
$$g_{\alpha\alpha}=e,qquad g_{\beta\alpha}=g_{\alpha\beta}^{-1},qquad
 g_{\alpha\beta}g_{\beta\gamma}=g_{\alpha\gamma}.$$
Conversely such a cocycle glues $U_\alpha\times G$ into a principal bundle. If $s'_\alpha=s_\alpha h_\alpha$, then
$$g'_{\alpha\beta}=h_\alpha^{-1}g_{\alpha\beta}h_\beta.$$

# Examples / Corollaries

The trivial bundle is $B\times G$. The unitary frames of a Hermitian vector bundle form a principal $U(r)$-bundle. A free proper right action on $P$ produces a principal bundle $P\to P/G$; properness supplies a Hausdorff quotient and slices. Freeness by itself is not sufficient.

# Unlocked by This

A principal connection will be a $G$-equivariant way to split $TP$ into vertical and horizontal directions. Representations convert $P$ into associated matter bundles without choosing local frames.
