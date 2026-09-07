---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Fibre Bundle"
tags: [gauge-theory, classifying-spaces, principal-bundles]
---

# Prerequisite Concepts

- [[Def - Principal G-Bundle]]
- [[Def - Fibre Bundle]]

# Notation

Let $G$ be a topological group. All bases used for classification are paracompact Hausdorff spaces, in particular smooth manifolds.

# The Definition

> [!definition] Universal principal bundle
> A **universal principal $G$-bundle** is a principal bundle
> $$EG\longrightarrow BG$$
> whose total space $EG$ is contractible. The base $BG=EG/G$ is a **classifying space** for $G$.

The model is unique only up to homotopy equivalence, which is exactly the appropriate uniqueness: bundles pulled back along homotopic maps are isomorphic.

# Examples / Corollaries

For $U(1)$, take $EU(1)=S^\infty\subset\mathbb C^\infty$ with scalar action and $BU(1)=\mathbb{CP}^\infty$. For $SU(2)\cong Sp(1)$, take $ESU(2)=S^\infty\subset\mathbb H^\infty$ and $BSU(2)=\mathbb{HP}^\infty$. Finite-dimensional Hopf fibrations are restrictions of these universal bundles to finite skeleta.

Since $\mathbb{CP}^\infty$ is a $K(\mathbb Z,2)$,
$$[B,BU(1)]\cong H^2(B;\mathbb Z).$$
Since the first nonzero cell of $\mathbb{HP}^\infty$ is in degree four, maps from a four-dimensional CW complex are controlled by $H^4$; for $SU(2)$ bundles this class is represented by $c_2$.

# Axiom Motivation

Pullback converts one bundle over $BG$ into a bundle over every base. Contractibility of $EG$ removes hidden topology upstairs, so all topology is forced into the map to $BG$. This is the bundle analogue of describing covering spaces by maps to an Eilenberg–Mac Lane space.

# Unlocked by This

[[Thm - Classification of Principal Bundles by Maps to BG]] makes this universal property precise. Characteristic classes are then simply pullbacks of cohomology classes on $BG$.
