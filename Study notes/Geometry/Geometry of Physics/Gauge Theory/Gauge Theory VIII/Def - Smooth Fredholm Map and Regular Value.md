---
type: definition
subject: gauge-theory
prereqs: ["Def - Fredholm Operator and Index"]
tags: [gauge-theory, fredholm-map, regular-value]
---

# Prerequisite Concepts

- [[Def - Fredholm Operator and Index]]

# The Definition

> [!definition] Smooth Fredholm map
> A smooth map $f:X\to Y$ between Banach manifolds is Fredholm of index $d$ if every derivative $D_xf:T_xX\to T_{f(x)}Y$ is Fredholm of index $d$. A point $y$ is regular when every $x\in f^{-1}(y)$ has surjective derivative.

At a regular point, the Banach implicit-function theorem identifies the level set locally with $\ker D_xf$; hence a regular fibre is a smooth $d$-manifold. Properness makes a zero-dimensional regular fibre finite.

# Calibration

A bounded Fredholm operator is a Fredholm map with constant derivative. Projection $H\oplus\mathbb R^d\to H$ has index $d$. A compact map on an infinite-dimensional space is generally not Fredholm because its derivative has nonclosed or infinite-codimensional range.
**True name:** a Fredholm map is a nonlinear map with finite-dimensional local failure of invertibility.

