---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Homogeneous Space"
  - "Def - Associated Bundle"
tags: [gauge-theory, homogeneous-space, associated-bundle]
---

# Notation

Let $G$ be a Lie group and $H\subset G$ a closed subgroup. Then $G/H$ denotes right cosets and $G\to G/H$ carries the right action of $H$.

# The Definition

> [!definition] Homogeneous bundle
> For a representation $\rho:H\to\mathrm{GL}(V)$, the bundle
> $$
> G\times_HV\longrightarrow G/H,qquad[g,v]\longmapsto gH,
> $$
> is the **homogeneous vector bundle** associated to $\rho$.

The left action of $G$ on itself commutes with the right $H$-action and descends to $G\times_HV$ by $a[g,v]=[ag,v]$. Hence the bundle looks the same over every point of the transitive $G$-space $G/H$.

# Tangent Bundle of a Homogeneous Space

Let $\mathfrak g,\mathfrak h$ be the Lie algebras. The isotropy representation of $H$ on $\mathfrak g/\mathfrak h$ is induced by $\operatorname{Ad}$. There is a natural isomorphism
$$
G\times_H(\mathfrak g/\mathfrak h)\xrightarrow{\sim}T(G/H),
\qquad[g,[X]]\longmapsto\left.\frac d{dt}\right|_0g\exp(tX)H.
$$
It is well defined because adding an element of $\mathfrak h$ gives zero tangent vector in the quotient and replacing $(g,[X])$ by $(gh,[\operatorname{Ad}_{h^{-1}}X])$ gives the same curve.

# Examples / Corollaries

$S^n\cong SO(n+1)/SO(n)$ and
$$TS^n\cong SO(n+1)\times_{SO(n)}\mathbb R^n.$$
Complex projective space is $\mathbb{CP}^n\cong U(n+1)/(U(1)\times U(n))$; its tautological and quotient bundles arise from the corresponding isotropy representations.
