---
type: definition
subject: gauge-theory
prereqs: ["Def - Mod-2 Degree of a Proper Fredholm Map", "Def - Determinant Line and Orientation of a Fredholm Operator"]
tags: [gauge-theory, degree, orientation]
---

# Prerequisite Concepts

- [[Def - Mod-2 Degree of a Proper Fredholm Map]]
- [[Def - Determinant Line and Orientation of a Fredholm Operator]]

# The Definition

> [!definition] Oriented Fredholm degree
> An orientation of an index-zero Fredholm map is a continuous orientation of $\det Df$. At a regular preimage $x$ of $y$, surjectivity and index zero make $D_xf$ an isomorphism, whose determinant-line orientation determines $\operatorname{sign}(x)=\pm1$. Define
> $$\deg(f)=\sum_{x\in f^{-1}(y)}\operatorname{sign}(x).$$

A transverse path between regular values yields an oriented compact one-dimensional cobordism. Its signed boundary count is zero, proving independence of the regular value. The same argument proves invariance under proper oriented Fredholm homotopies. Reducing signs modulo two recovers $\deg_2$.

# Orientation Transport

Along a path of Fredholm operators, the determinant line transports orientation continuously. Around a loop it may reverse; orientability is exactly triviality of the first Stiefel–Whitney class of the determinant line bundle.

