---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, gauge-theory, curvature]
---

# Notation

Let $\nabla$ be a connection on $E\to M$, with exterior covariant derivative $d_\nabla$. In a local frame, write $\nabla=d+A$.

# Axiom Motivation

Differentiating first along $X$ and then along $Y$ need not agree with doing it in the opposite order. When $X$ and $Y$ do not commute, their flows already fail to close by the amount $[X,Y]$; subtracting $\nabla_{[X,Y]}$ isolates the failure caused by the connection itself.

# The Definition

> [!definition] Curvature
> The **curvature** of $\nabla$ is the $\operatorname{End}(E)$-valued $2$-form
> $$
> F_\nabla(X,Y)s
> =\nabla_X\nabla_Ys-\nabla_Y\nabla_Xs-\nabla_{[X,Y]}s.
> $$
> Equivalently, $d_\nabla^2s=F_\nabla\wedge s$ for every section $s$.

In a local frame,
$$
F_A=dA+A\wedge A,qquad
(A\wedge A)^a{}_b=A^a{}_c\wedge A^c{}_b.
$$
To derive the formula, apply $(d+A)^2$ to a column $u$:
$$
d(du+Au)+A\wedge(du+Au)=(dA+A\wedge A)u,
$$
because $d(Au)=dA\,u-A\wedge du$.

Under $e'=eg$, one has $F_{A'}=g^{-1}F_Ag$. Thus the local matrices assemble into a global section of $\Lambda^2T^*M\otimes\operatorname{End}E$ even though $A$ itself does not.

# Relate to Other Fields / Compression

Curvature is the infinitesimal holonomy: parallel transport around a sufficiently small oriented parallelogram with side vectors $\varepsilon X$ and $\varepsilon Y$ differs from the identity by $-\varepsilon^2F_\nabla(X,Y)+O(\varepsilon^3)$, with the sign reversed if the transport convention is reversed. The invariant statement is that $F_\nabla=0$ exactly when the connection is locally gauge-equivalent to the trivial connection on a simply connected coordinate neighbourhood.

For a complex line bundle, endomorphisms commute, so $A\wedge A=0$ and $F_A=dA$. This abelian simplification is the geometric origin of the linearity of Maxwell theory.

# Unlocked by This

The curvature is tensorial by [[Thm - Curvature is C-Infinity Linear in Sections]] and obeys the [[Thm - Bianchi Identity for a Vector-Bundle Connection|Bianchi identity]]. Its invariant polynomials produce characteristic classes in Gauge Theory IV.
