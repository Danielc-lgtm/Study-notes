---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
tags: [gauge-theory, local-connection, gauge-potential]
---

# Prerequisite Concepts

- [[Def - Connection 1-Form on a Principal Bundle]]

# The Definition

> [!definition] Local gauge potential
> If $s:U\to P$ is a local section and $\omega$ a principal connection, the **local connection form** is
> $$A=s^*\omega\in\Omega^1(U;\mathfrak g).$$

The section identifies $P|_U$ with $U\times G$ by $(x,g)\mapsto s(x)g$. In this trivialization the global form is reconstructed from $A$ by
$$
\omega_{s(x)g}=\operatorname{Ad}_{g^{-1}}A_x+g^{-1}dg.
$$
Thus $A$ contains all connection data on $U$, but depends on the chosen section.

# Axiom Motivation

A section chooses one point in every local torsor, hence one local gauge. Pullback asks how that chosen point moves relative to the horizontal distribution. The resulting form is a computational representative, not a global tensor.

# Examples / Corollaries

The canonical section of a product bundle pulls the product connection back to $A=0$. For a $U(1)$ bundle with convention $\nabla=d+iqA_{\rm em}$, the Lie-algebra-valued potential is $iqA_{\rm em}$.
