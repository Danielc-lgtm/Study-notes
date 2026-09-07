---
type: definition
subject: gauge-theory
prereqs: ["Def - Fredholm Operator and Index"]
tags: [gauge-theory, determinant-line, orientation]
---

# Prerequisite Concepts

- [[Def - Fredholm Operator and Index]]

# The Definition

> [!definition] Determinant line
> For a Fredholm operator $D:X\to Y$,
> $$\det D=\Lambda^{\max}\ker D\otimes\bigl(\Lambda^{\max}\operatorname{coker}D\bigr)^*.$$
> An orientation of $D$ is an orientation of this real line.

For a continuous Fredholm family, these lines glue to a line bundle. The construction remains meaningful when kernel and cokernel dimensions jump because finite-dimensional stabilization gives compatible local trivializations: add a finite-dimensional map $\mathbb R^N\to Y$ making the stabilized operator surjective, then identify the determinant with the top exterior power of its kernel tensored with $(\Lambda^N\mathbb R^N)^*$.

# Why the Cokernel is Dualized

For a finite-dimensional map, the canonical determinant is $\det X\otimes(\det Y)^*$, and the exact sequences for kernel, image, and cokernel reduce it to the displayed formula. Dualization ensures multiplicativity under composition.

