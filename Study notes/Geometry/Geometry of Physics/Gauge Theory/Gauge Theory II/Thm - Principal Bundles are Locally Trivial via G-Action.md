---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
tags: [gauge-theory, principal-bundle, trivialization, section]
---

# Prerequisite Concepts

- [[Def - Principal G-Bundle]]

# Statement

> [!theorem] Sections and trivializations
> Let $P\xrightarrow\pi B$ be a principal $G$-bundle.
> 1. Local sections $s:U\to P$ are in bijection with equivariant local trivializations $P|_U\cong U\times G$.
> 2. The bundle is globally trivial if and only if it admits a global section.

# Why Is It True

A point in a principal fibre has a unique expression $s(x)g$ relative to a chosen section. Existence uses transitivity; uniqueness uses freeness.

# Formal Proof

> [!proof]- Formal Proof
> Given a section $s:U\to P$, define
> $$\Psi_s:U\times G\to P|_U,\qquad(x,g)\mapsto s(x)g.$$
> It is smooth, covers $U$, and is equivariant. For $p\in P_x$, transitivity gives $p=s(x)g$ for some $g$; freeness makes $g$ unique. Thus $\Psi_s$ is bijective. To see that its inverse is smooth, choose any principal trivialization $\Phi:P|_W\to W\times G$ near $x$. Write $\Phi(s(y))=(y,a(y))$ and $\Phi(p)=(y,b)$. Then the second coordinate of $\Psi_s^{-1}(p)$ is $a(y)^{-1}b$, a smooth function. Hence $\Psi_s$ is a diffeomorphism.
>
> Conversely, an equivariant trivialization $\Psi:U\times G\to P|_U$ defines the section $s(x)=\Psi(x,e)$. These constructions are inverse: equivariance gives $\Psi(x,g)=\Psi(x,e)g$.
>
> Taking $U=B$ proves both directions of the global statement. A global section produces $P\cong B\times G$ by $\Psi_s$; the trivial bundle has the section $x\mapsto(x,e)$.

# Rederivation Scaffold

A section chooses an origin in every $G$-torsor. Once an origin is chosen, the unique group element relating it to any other point is the missing trivialization coordinate.

# What Can Go Wrong

Every principal bundle has local sections by definition. A general fibre bundle may not: the group action and its distinguished identity are what turn a local product chart into a section automatically.
