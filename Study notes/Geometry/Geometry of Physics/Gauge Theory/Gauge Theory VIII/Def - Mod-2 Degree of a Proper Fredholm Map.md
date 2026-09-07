---
type: definition
subject: gauge-theory
prereqs: ["Def - Smooth Fredholm Map and Regular Value"]
tags: [gauge-theory, degree, fredholm-map]
---

# Prerequisite Concepts

- [[Def - Smooth Fredholm Map and Regular Value]]

# The Definition

> [!definition] Mod-two degree
> Let $f:X\to Y$ be a proper Fredholm map of index zero between connected Banach manifolds. For a regular value $y$, define
> $$\deg_2(f)=\#f^{-1}(y)\pmod2.$$

Properness and regularity make the fibre a compact zero-manifold, hence finite. If $y_0,y_1$ are regular, choose a transverse path between them. Its inverse image is a compact one-manifold whose boundary is $f^{-1}(y_0)\sqcup f^{-1}(y_1)$. Every compact one-manifold has an even number of boundary points, proving independence of the regular value. Sard–Smale supplies regular values.

# Homotopy Invariance

A proper Fredholm homotopy gives the same cobordism argument after a generic perturbation. Properness cannot be omitted: points may escape to infinity and change the count.
**True name:** mod-two degree is the parity of solutions protected by proper Fredholm cobordism.

