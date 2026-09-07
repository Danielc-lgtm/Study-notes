---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs: ["Thm - Weitzenbock Formula for a Dirac Bundle"]
tags: [gauge-theory, spin-geometry, vanishing-theorem]
---

# Prerequisite Concepts

- [[Thm - Weitzenbock Formula for a Dirac Bundle]]

# Problem Statement

Let $M$ be a closed spin manifold with positive scalar curvature. Prove that its spin Dirac operator has zero kernel.

# Solution

> [!solution]- Solution
> The Lichnerowicz specialization of Weitzenböck is
> $$D^2=\nabla^*\nabla+\frac14\operatorname{scal}.$$
> If $D\psi=0$, formal self-adjointness and integration give
> $$0=\|D\psi\|_{L^2}^2=\|\nabla\psi\|_{L^2}^2+\frac14\int_M\operatorname{scal}|\psi|^2dV.$$
> Both terms are nonnegative, and the second vanishes only if $\psi=0$ because scalar curvature is everywhere positive. Hence $\ker D=0$.

