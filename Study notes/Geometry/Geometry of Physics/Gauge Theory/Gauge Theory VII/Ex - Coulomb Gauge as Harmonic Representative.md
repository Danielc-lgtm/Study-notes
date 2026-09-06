---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs: ["Thm - Hodge Theorem for an Elliptic Complex"]
tags: [gauge-theory, gauge-fixing, hodge-theory]
---

# Problem Statement

For the abelian deformation complex $\Omega^0\xrightarrow d\Omega^1\xrightarrow d\Omega^2$ on a closed manifold, prove that every closed one-form has a unique gauge-equivalent representative satisfying $d^*a=0$ after quotienting constant gauge parameters.

# Solution

> [!solution]- Solution
> Hodge decomposition writes a closed one-form as $a=df+h+d^*\beta$. Applying $d$ and pairing $dd^*\beta$ with $\beta$ gives $\|d^*\beta\|^2=0$, so $a=df+h$. The gauge transformation by $-f$ sends $a$ to harmonic $h$, which satisfies $d^*h=0$. If two harmonic representatives differ by $df$, then
> $$\|df\|^2=\langle df,df\rangle=\langle d^*df,f\rangle=0,$$
> so they coincide. The parameter $f$ is determined only up to a constant, precisely the stabilizer of the abelian gauge action.

