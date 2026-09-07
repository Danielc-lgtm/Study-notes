---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Associated Bundle"
tags: [gauge-theory, principal-bundles, structure-group]
---

# Prerequisite Concepts

- [[Def - Principal G-Bundle]]
- [[Def - Associated Bundle]]

# Notation

Let $\varphi:G\to H$ be a Lie-group homomorphism and let $P\to B$ be a right principal $G$-bundle.

# The Definition

> [!definition] Extension of structure group
> The **extension of $P$ along $\varphi$** is
> $$
> P\times_\varphi H=(P\times H)/((p,h)\cdot g=(pg,\varphi(g)^{-1}h)).
> $$
> It is a principal $H$-bundle under $[p,h]h'=[p,hh']$.

> [!definition] Reduction of structure group
> If $G\subset H$ and $Q\to B$ is a principal $H$-bundle, a **reduction of $Q$ to $G$** is a principal $G$-bundle $P\to B$ together with an $H$-bundle isomorphism $P\times_GH\cong Q$.

If $g_{\alpha\beta}$ are transition functions for $P$, then $\varphi\circ g_{\alpha\beta}$ are those of its extension. This gives a local proof that the quotient above is a bundle.

# Operational Characterization

Reductions of $Q$ to a closed subgroup $G\subset H$ correspond to sections of the associated bundle
$$Q/G=Q\times_H(H/G)\longrightarrow B.$$
Given a reduction $P\subset Q$, the coset $P_bG$ defines a section. Conversely, the inverse image of a section under $Q\to Q/G$ is a principal $G$-subbundle. These constructions are inverse because a coset $qG$ records exactly which $G$-orbit of frames is allowed at $b$.

# Examples / Corollaries

- A Riemannian metric reduces the frame bundle from $\mathrm{GL}_n(\mathbb R)$ to $O(n)$; an orientation reduces it to $mathrm{GL}_n^+(\mathbb R)$, and both together to $SO(n)$.
- A Hermitian metric reduces $\mathrm{GL}_n(\mathbb C)$ to $U(n)$.
- A trivialization is a reduction to the identity subgroup; therefore it exists exactly when the principal bundle has a global section.
- Spin and $\operatorname{Spin}^c$ structures are lifts, not literal subgroup reductions, because the relevant maps to $SO(n)$ are covering homomorphisms.

# What Can Go Wrong

A reduction is additional data, not merely the statement that $G\subset H$. Its obstruction is the failure of $Q/G$ to admit a section. Different sections may define inequivalent reductions.
