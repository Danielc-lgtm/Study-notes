---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Flat Connections and Monodromy Representations"
  - "Def - Holonomy Group of a Principal Connection"
tags: [gauge-theory, flat-connection, holonomy, circle]
---

# Prerequisite Concepts

- [[Thm - Flat Connections and Monodromy Representations]]
- [[Def - Holonomy Group of a Principal Connection]]

# Problem Statement

Classify flat $U(1)$-connections on $S^1$ up to gauge equivalence. For
$A=i\alpha\,d\theta$ on the trivial bundle, determine when two real parameters
$\alpha$ and $\beta$ are gauge equivalent and compute the holonomy.

# Solution

> [!solution]- Solution
> Since $S^1$ has no nonzero two-forms, every connection is flat. The monodromy
> theorem gives
> $$\mathcal M_{\mathrm{flat}}(S^1,U(1))
> \cong\operatorname{Hom}(\mathbb Z,U(1))\cong U(1),$$
> with no conjugacy quotient to take because $U(1)$ is abelian.
>
> Parallel transport for $A=i\alpha d\theta$ solves
> $\dot U=-i\alpha\dot\theta,U$. Around the positively oriented circle,
> $U(2\pi)=e^{-2\pi i\alpha}$. A gauge map $g=e^{in\theta}$ is single-valued
> exactly when $n\in\mathbb Z$ and changes the passive potential by
> $A\mapsto A+g^{-1}dg=i(\alpha+n)d\theta$. Thus $alpha$ and $\beta$ are gauge
> equivalent exactly when $\beta-\alpha\in\mathbb Z$, and
> $e^{-2\pi i\alpha}$ is the complete invariant.

# Rederivation Scaffold

A flat connection remembers only the image of the generator of $\pi_1(S^1)=\mathbb Z$.
