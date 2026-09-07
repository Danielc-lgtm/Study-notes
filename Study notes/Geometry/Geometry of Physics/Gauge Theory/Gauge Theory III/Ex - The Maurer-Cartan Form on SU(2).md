---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Thm - Maurer-Cartan Equation"
tags: [geometry, gauge-theory, lie-groups, differential-forms]
---

# Prerequisite Concepts

- [[Def - The Maurer-Cartan Form]]
- [[Thm - Maurer-Cartan Equation]]

# Problem Statement

Write $g=aI+i b^j\sigma_j\in SU(2)$ with $a^2+|b|^2=1$. Compute the left Maurer–Cartan form $g^{-1}dg$ and verify its structural equation.

# Solution

> [!solution]- Solution
> The Pauli identity
> $\sigma_j\sigma_k=\delta_{jk}I+i\varepsilon_{jk\ell}\sigma_\ell$
> implies $g^*g=(a^2+|b|^2)I$ and $\det g=a^2+|b|^2$. Hence the displayed
> matrices are exactly $SU(2)$, and the parameters identify it smoothly with
> $S^3$.
>
> Since $g^{-1}=aI-i b^j\sigma_j$,
> $$
> g^{-1}dg=(a\,da+b\cdot db)I
> +i\sigma_j\bigl(a\,db^j-b^jda+(b\times db)^j\bigr).
> $$
> The scalar term vanishes after differentiating $a^2+|b|^2=1$. With
> $T_j=-i\sigma_j/2$, for which $[T_j,T_k]=\varepsilon_{jk}{}^\ell T_\ell$,
> this becomes
> $$g^{-1}dg=T_j\theta^j,
> \qquad \theta^j=-2\bigl(a\,db^j-b^jda+\varepsilon^j{}_{k\ell}b^kdb^\ell\bigr).$$
> The three forms are pointwise independent because left translation
> identifies every tangent space of $SU(2)$ with $\mathfrak{su}(2)$.
>
> Finally differentiate $g^{-1}g=I$ to obtain
> $d(g^{-1})=-g^{-1}(dg)g^{-1}$. Therefore
> $$d(g^{-1}dg)=d(g^{-1})\wedge dg=-(g^{-1}dg)\wedge(g^{-1}dg).$$
> Writing both sides in the basis $T_j$ and using the Pauli commutator gives
> $$d\theta^j+\frac12\varepsilon^j{}_{k\ell}\theta^k\wedge\theta^\ell=0.$$
> This verifies the coordinate formulas without a separate lengthy expansion.

# Rederivation Scaffold

Multiply $g^{-1}$ by $dg$, use the sphere constraint to remove the scalar part, and derive Maurer–Cartan from $d(g^{-1})$.
