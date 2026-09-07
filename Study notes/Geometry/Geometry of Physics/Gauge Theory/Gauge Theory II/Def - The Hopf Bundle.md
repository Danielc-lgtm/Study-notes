---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Complex Line Bundle"
tags: [gauge-theory, hopf-fibration, principal-bundle]
---

# Prerequisite Concepts

- [[Def - Principal G-Bundle]]
- [[Def - Complex Line Bundle]]

# The Definition

> [!definition] Complex Hopf bundle
> Scalar multiplication gives a free right $U(1)$-action on
> $S^{2n+1}\subset\mathbb C^{n+1}$. The quotient map
> $$
> U(1)\longrightarrow S^{2n+1}\longrightarrow\mathbb{CP}^n,
> \qquad z\longmapsto[z],
> $$
> is the **Hopf principal bundle**. For $n=1$ this is $S^1\to S^3\to S^2$.

The fibre over a complex line $\ell$ is its unit circle. The associated line bundle for the weight-$1$ representation is the tautological line bundle or its dual according to the quotient convention; this sign must be fixed when naming its first Chern class.

# Local Description for $S^3\to S^2$

Identify $\mathbb{CP}^1$ with $\mathbb C\cup\{\infty\}$. On $U_0=\{[z_0:z_1]:z_0\ne0\}$ and $U_1=\{z_1\ne0\}$, normalize the representatives $(1,w)$ and $(w',1)$. On the equator the resulting unit sections differ by a map $S^1\to U(1)$ of degree $\pm1$. Therefore no global section exists: if it did, the transition map would be a coboundary and have zero winding.

# Quaternionic Analogue

The free scalar action of $Sp(1)\cong SU(2)$ gives
$$
Sp(1)\longrightarrow S^{4n+3}\longrightarrow\mathbb{HP}^n.
$$
For $n=1$, this is $S^3\to S^7\to S^4$, the basic nontrivial $SU(2)$ bundle over the four-sphere.

# Unlocked by This

The finite Hopf bundles approximate the universal bundles
$S^\infty\to\mathbb{CP}^\infty$ and $S^\infty\to\mathbb{HP}^\infty$. Their winding and degree-four charge become the first and second Chern classes.
